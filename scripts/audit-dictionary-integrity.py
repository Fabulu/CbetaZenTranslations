#!/usr/bin/env python3
"""Verify settled semantic contracts and web-artifact parity."""

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
entries = json.loads((ROOT / "termbase.v2.json").read_text(encoding="utf-8-sig"))["Entries"]
by_id = {entry["Id"]: entry for entry in entries}
failures = []


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

allowed = ("t_1c7d25824f85", "Senses.0.AlternateTargets.3")


def walk(value, path=()):
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk(item, path + (str(index),))
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from walk(item, path + (key,))


for entry in entries:
    for path, text in walk(entry):
        if "original face" in text.casefold():
            location = (entry["Id"], ".".join(path))
            if location != allowed:
                failures.append(f"forbidden calque at {location}: {text}")

index = dict(json.loads((ROOT / "termbase.index.json").read_text(encoding="utf-8"))["Terms"])
for entry in entries:
    expected = entry["Senses"][0]["PreferredTarget"]
    if index.get(entry["SourceTerm"]) != expected:
        failures.append(f"index drift: {entry['SourceTerm']}")

shard_entries = {}
for path in sorted((ROOT / "termbase").glob("*.json")):
    for entry in json.loads(path.read_text(encoding="utf-8"))["Entries"]:
        shard_entries[entry["Id"]] = entry
if set(shard_entries) != set(by_id):
    failures.append("shard ID set differs from termbase.v2.json")
for entry_id, entry in by_id.items():
    if shard_entries.get(entry_id) != entry:
        failures.append(f"shard content drift: {entry_id}")

if failures:
    print("\n".join(failures))
    sys.exit(1)
print(f"dictionary integrity PASS: {len(entries)} entries")
