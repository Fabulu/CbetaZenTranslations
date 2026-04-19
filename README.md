# CbetaZenTranslations

English translations of **CBETA Zen / Chan texts**, with community-contributed translation data.

This repository is the **translations companion** to [CbetaZenTexts](https://github.com/Fabulu/CbetaZenTexts), which hosts the original Chinese CBETA XML corpus.

---

## Project status

12 texts translated out of ~4,990 in the collection. Early stage -- contributions welcome.

---

## What's in here

### `xml-p5t/` -- English Translations (Work in Progress)

Contains translated CBETA XML files with **English translations added** alongside the original Chinese text.

Each translated file preserves the full original CBETA header intact.

**Currently translated texts:**

| Text | Location |
|------|----------|
| T 1 -- Long Agama Sutra (Changahan Jing) | `xml-p5t/T/T01/T01n0001.xml` |
| T 1987A -- Record of Caoshan Yuanzheng (Caoshan Yuanzheng Chanshi Yulu) | `xml-p5t/T/T47/T47n1987A.xml` |
| T 1987B -- Record of Caoshan Benji (Caoshan Benji Chanshi Yulu) | `xml-p5t/T/T47/T47n1987B.xml` |
| T 2003 -- Blue Cliff Record (Biyanlu) | `xml-p5t/T/T48/T48n2003.xml` |
| T 2004 -- Book of Serenity (Congrong'an Lu) | `xml-p5t/T/T48/T48n2004.xml` |
| T 2005 -- Gateless Barrier (Wumenguan) | `xml-p5t/T/T48/T48n2005.xml` |
| T 2010 -- Inscription on Trusting the Mind (Xinxinming) | `xml-p5t/T/T48/T48n2010.xml` |
| T 2012A -- Huangbo's Essentials of Transmitting the Mind (Chuanxin Fayao) | `xml-p5t/T/T48/T48n2012A.xml` |
| J B137 -- Recorded Sayings of Zhaozhou (Zhaozhou Heshang Yulu) | `xml-p5t/J/J24/J24nB137.xml` |
| X 1217 -- Bodhidharma's Four Practices (Rudao Sixing Guan) | `xml-p5t/X/X63/X63n1217.xml` |
| X 1333 -- Record of Xuefeng Yicun (Xuefeng Yicun Chanshi Yulu) | `xml-p5t/X/X69/X69n1333.xml` |
| B a005 -- Supplement to the Canon, Vol. 7: Editorial Notes | `xml-p5t/B/B07/B07na005.xml` |

### `community/` -- Community Translation Data

Community-contributed data organized by contributor:

- `translations/` -- per-user translation XML files
- `collections/` -- text collection definitions
- `reviews/` -- translation review records
- `termbases/` -- terminology databases

### Root metadata files

| File | Description |
|------|-------------|
| `masters.json` | Database of 205 Zen masters with biographical data (~5,000 lines) |
| `master-corpus.json` | Cross-references 200 masters against the full 4,990-text corpus with mention counts |
| `grammar-particles.json` | Classical Chinese grammar particles with roles, glosses, and examples (15 entries) |
| `termbase.json` | Shared terminology database |
| `titles.jsonl` | Text title index |
| `translation-memory.approved.jsonl` | Approved translation memory |
| `translation-review.jsonl` | Review ledger |
| `zen_texts.json` | Curated Zen text collection definition |

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

**[Read Zen](https://github.com/Fabulu/ReadZen)** -- Desktop app for reading and translating Zen texts

### Quick workflow

1. Download and open **Read Zen**
2. Clone this repository using the built-in **Git tab**
3. Open a text from `xml-p5t`
4. Translate or improve a section
5. Press **Save** in the Translation view
6. Go to the **Git tab** and commit + push

The app handles forking, committing, and pull request creation automatically.

### Translation philosophy

This project supports **high-quality machine translation workflows**. Machine translation is acceptable and encouraged as a baseline for iterative improvement.

### Translator annotation

Please add a short annotation at the top of translated files indicating who you are and whether machine translation was used.

---

## Related repositories

| Repository | Description |
|---|---|
| [OpenZenTexts](https://github.com/Fabulu/OpenZenTexts) | Open-licensed Chinese Zen source texts (commercial use OK) |
| [OpenZenTranslations](https://github.com/Fabulu/OpenZenTranslations) | Translations of open-licensed texts (commercial use OK) |
| [CbetaZenTexts](https://github.com/Fabulu/CbetaZenTexts) | CBETA Chinese Zen source texts (non-commercial) |
| [Read Zen](https://github.com/Fabulu/ReadZen) | Desktop app for reading and translating Zen texts |

---

## License

See [LICENSE](LICENSE) for details. All materials are distributed under CBETA's non-commercial use terms.
