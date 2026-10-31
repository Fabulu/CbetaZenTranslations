#!/usr/bin/env python3
"""Verify settled semantic contracts and web-artifact parity."""

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
failures = []
index = json.loads((ROOT / "termbase.index.json").read_text(encoding="utf-8"))["Terms"]
shard_rows = [
    entry
    for path in sorted((ROOT / "termbase").glob("*.json"))
    for entry in json.loads(path.read_text(encoding="utf-8"))["Entries"]
]
shard_entries = {entry["Id"]: entry for entry in shard_rows}
if len(shard_entries) != len(shard_rows):
    failures.append("duplicate entry ID across shards")

rich_path = ROOT / "termbase.v2.json"
if rich_path.exists():
    entries = json.loads(rich_path.read_text(encoding="utf-8-sig"))["Entries"]
else:
    by_term = {entry["SourceTerm"]: entry for entry in shard_rows}
    if len(by_term) != len(shard_rows):
        failures.append("duplicate headword across shards")
    entries = [by_term[term] for term, _ in index if term in by_term]
    if len(entries) != len(shard_rows):
        failures.append("index headword set differs from shards")
by_id = {entry["Id"]: entry for entry in entries}


def require(entry_id, path, expected):
    value = by_id[entry_id]
    for key in path:
        value = value[key]
    if value != expected:
        failures.append(f"{entry_id} {path}: {value!r} != {expected!r}")


require("t_1c7d25824f85", ("Senses", 0, "PreferredTarget"), "what one originally is")
require(
    "t_1c7d25824f85",
    ("Senses", 0, "AlternateTargets", 3),
    "original face (literal/traditional calque)",
)
require(
    "t_59b880301320",
    ("Senses", 0, "PreferredTarget"),
    "what you were before your parents were born",
)
require(
    "t_0dacce0127d1",
    ("Senses", 0, "PreferredTarget"),
    "what someone or something really is",
)

for entry in entries:
    for sense_number, sense in enumerate(entry["Senses"]):
        # Explanations, source quotations, and search aliases may describe the
        # traditional calque. The settled rule applies to the displayed target.
        if "original face" in sense["PreferredTarget"].casefold():
            failures.append(
                f"forbidden preferred-target calque: {entry['Id']} sense {sense_number}"
            )

expected_index = []
for entry in entries:
    target = next(
        (sense["PreferredTarget"] for sense in entry["Senses"]
         if sense.get("SenseKey") is None),
        entry["Senses"][0]["PreferredTarget"],
    )
    expected_index.append([entry["SourceTerm"], target])
if index != expected_index:
    failures.append("index content or order differs from termbase.v2.json")

if set(shard_entries) != set(by_id):
    failures.append("shard ID set differs from termbase.v2.json")
for entry_id, entry in by_id.items():
    if shard_entries.get(entry_id) != entry:
        failures.append(f"shard content drift: {entry_id}")

search_path = ROOT / "termbase.search.json"
if search_path.exists():
    search = json.loads(search_path.read_text(encoding="utf-8"))
    rows = search.get("Entries", [])
    if search.get("schemaVersion") != 1 or len(rows) != len(entries):
        failures.append("search artifact schema or count differs from shards")
    elif {
        row.get("id"): row.get("sourceTerm") for row in rows
    } != {
        entry["Id"]: entry["SourceTerm"] for entry in entries
    }:
        failures.append("search artifact IDs or headwords differ from shards")

if failures:
    print("\n".join(failures))
    sys.exit(1)
print(f"dictionary integrity PASS: {len(entries)} entries")
