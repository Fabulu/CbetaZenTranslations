# CbetaZenTranslations

English translations of **CBETA Zen / Chan texts**, with community-contributed translation data.

This repository is the **translations companion** to [CbetaZenTexts](https://github.com/Fabulu/CbetaZenTexts), which hosts the original Chinese CBETA XML corpus.

---

## Repository Structure

### `xml-p5t` — English Translations (Work in Progress)

Contains translated CBETA XML files with **English translations added** alongside the original Chinese text.

Each translated file preserves the full original CBETA header intact.

**Currently translated texts include:**

| Text | Location |
|------|----------|
| T 1 — Long Agama Sutra | `xml-p5t/T/T01/T01n0001.xml` |
| T 1987A — Record of Caoshan | `xml-p5t/T/T47/T47n1987A.xml` |
| T 1987B — Record of Caoshan (alt.) | `xml-p5t/T/T47/T47n1987B.xml` |
| T 2003 — Record of Zhaozhou | `xml-p5t/T/T48/T48n2003.xml` |
| T 2004 — Record of Yunmen | `xml-p5t/T/T48/T48n2004.xml` |
| T 2005 — Record of Xuefeng | `xml-p5t/T/T48/T48n2005.xml` |
| T 2010 — Blue Cliff Record | `xml-p5t/T/T48/T48n2010.xml` |
| T 2012A — Gateless Gate | `xml-p5t/T/T48/T48n2012A.xml` |
| J B137 — Record of Huangbo | `xml-p5t/J/J24/J24nB137.xml` |
| X 1217 — Bodhidharma Four Practices | `xml-p5t/X/X63/X63n1217.xml` |
| X 1333 — Sayings of Xutang | `xml-p5t/X/X69/X69n1333.xml` |
| B a005 — Additional text | `xml-p5t/B/B07/B07na005.xml` |

### `community/` — Community Translation Data

Community-contributed data organized by contributor:

- `translations/` — per-user translation XML files
- `collections/` — text collection definitions
- `reviews/` — translation review records
- `termbases/` — terminology databases

### Root Metadata Files

- `termbase.json` — shared terminology database
- `titles.jsonl` — text title index
- `translation-memory.approved.jsonl` — approved translation memory
- `translation-review.jsonl` — review ledger
- `zen_texts.json` — curated Zen text collection definition

---

## CBETA Non-Commercial Requirement

The CBETA texts are provided under a **non-commercial use requirement**.

- CBETA retains ownership of the original texts
- Redistribution is allowed **only for non-commercial use**
- The **full CBETA header must remain intact** in every file
- Translations are subject to the same non-commercial condition

---

## Contributing

The easiest way to contribute translations is to use the official desktop app:

**CBETA Translator** — https://github.com/Fabulu/CBETA-Translator

### Quick Workflow

1. Download and open **CBETA Translator**
2. Clone this repository using the built-in **Git tab**
3. Open a text from `xml-p5t`
4. Translate or improve a section
5. Press **Save** in the Translation view
6. Go to the **Git tab** and commit + push

The app handles forking, committing, and pull request creation automatically.

### Translation Philosophy

This project supports **high-quality machine translation workflows**. Machine translation is acceptable and encouraged as a baseline for iterative improvement.

### Translator Annotation

Please add a short annotation at the top of translated files indicating who you are and whether machine translation was used.

---

## Related Repositories

- **[CbetaZenTexts](https://github.com/Fabulu/CbetaZenTexts)** — Original CBETA Chinese XML corpus (read-only source)
- **[CBETA-Translator](https://github.com/Fabulu/CBETA-Translator)** — Desktop app for reading and translating CBETA texts

---

## License

See [LICENSE](LICENSE) for details. All materials are distributed under CBETA's non-commercial use terms.
