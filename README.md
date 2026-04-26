# CbetaZenTranslations

English translations of CBETA texts, with community-contributed translation data, 301 Zen master profiles, and corpus metadata.

This is the **translations companion** to [CbetaZenTexts](https://github.com/Fabulu/CbetaZenTexts), which hosts the complete ~5,000-text CBETA XML corpus.

---

## Project status

12 texts translated out of ~4,990 in the collection. Early stage - contributions welcome.

---

## What's in here

### `xml-p5t/` - English Translations (Work in Progress)

Contains translated CBETA XML files with English translations added alongside the original Chinese text. Each translated file preserves the full original CBETA header intact.

**Currently translated texts:**

| Text | Location |
|------|----------|
| T 1 - Long Agama Sutra (Changahan Jing) | `xml-p5t/T/T01/T01n0001.xml` |
| T 1987A - Record of Caoshan Yuanzheng | `xml-p5t/T/T47/T47n1987A.xml` |
| T 1987B - Record of Caoshan Benji | `xml-p5t/T/T47/T47n1987B.xml` |
| T 2003 - Blue Cliff Record (Biyanlu) | `xml-p5t/T/T48/T48n2003.xml` |
| T 2004 - Book of Serenity (Congrong Lu) | `xml-p5t/T/T48/T48n2004.xml` |
| T 2005 - Gateless Barrier (Wumenguan) | `xml-p5t/T/T48/T48n2005.xml` |
| T 2010 - Inscription on Trusting the Mind (Xinxinming) | `xml-p5t/T/T48/T48n2010.xml` |
| T 2012A - Huangbo's Essentials of Transmitting the Mind | `xml-p5t/T/T48/T48n2012A.xml` |
| J B137 - Recorded Sayings of Zhaozhou | `xml-p5t/J/J24/J24nB137.xml` |
| X 1217 - Bodhidharma's Four Practices | `xml-p5t/X/X63/X63n1217.xml` |
| X 1333 - Record of Xuefeng Yicun | `xml-p5t/X/X69/X69n1333.xml` |
| B a005 - Supplement to the Canon, Vol. 7 | `xml-p5t/B/B07/B07na005.xml` |

### `community/` - Community Translation Data

Community-contributed data organized by contributor:

- `translations/` - per-user translation XML files
- `collections/` - text collection definitions
- `reviews/` - translation review records
- `termbases/` - terminology databases
- `stars/` - translation star ratings

### Root metadata files

| File | Description |
|------|-------------|
| `masters.json` | Database of 301 Zen masters with biographical data |
| `master-corpus.json` | Cross-references masters against the full corpus with mention counts |
| `corpus/masters/` | Per-master sharded corpus data (276 files + index) |
| `grammar-particles.json` | Classical Chinese grammar particles with roles, glosses, and examples |
| `termbase.json` | Shared terminology database |
| `titles.jsonl` | Text title index (~4,990 entries) |
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

The easiest way to contribute translations is through the official app:

**[Read Zen](https://github.com/Fabulu/ReadZen)** - Desktop + web app for reading and translating Zen texts

### Quick workflow

1. Download and open **Read Zen**
2. Clone this repository using the built-in **Git tab**
3. Open a text from `xml-p5t`
4. Translate or improve a section
5. Press **Save** in the Translation view
6. Go to the **Git tab** and commit + push

The app handles forking, committing, and pull request creation automatically.

---

## Related repositories

| Repository | Description |
|---|---|
| [OpenZenTexts](https://github.com/Fabulu/OpenZenTexts) | Freely-licensed Zen source texts (commercial use OK) |
| [OpenZenTranslations](https://github.com/Fabulu/OpenZenTranslations) | Translations of freely-licensed texts (commercial use OK) |
| [CbetaZenTexts](https://github.com/Fabulu/CbetaZenTexts) | Complete CBETA XML corpus (~5,000 texts, non-commercial) |
| [Read Zen](https://github.com/Fabulu/ReadZen) | Desktop + web app for reading and translating Zen texts |
| [readzen.pages.dev](https://readzen.pages.dev) | Web app - read, search, and explore online |

---

## License

See [LICENSE](LICENSE) for details. All materials are distributed under CBETA's non-commercial use terms.
