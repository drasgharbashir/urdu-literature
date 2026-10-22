# Classical Urdu Library

Public-domain classical Urdu books (authors who died in 1961 or earlier), with the Urdu original and a faithful English translation side by side, plus bilingual PDF and EPUB downloads. See `CLAUDE.md` for the full pipeline, translation rules and copyright rules.

## Layout

```
tools/urdu_library.py   find, download and OCR books from archive.org (see tools/README.md)
tools/export_book.py    build the bilingual PDF and EPUB for one book
tools/authors.json      the classical authors list
library/catalog.csv     one row per book and its pipeline status
content/books/<slug>/   meta.json, glossary.json, urdu/NNNN.md, en/NNNN.md
site/                   Astro website, deployed to GitHub Pages
```

## Site

```
cd site
npm install
SHOW_DRAFTS=1 npm run dev      # preview, including books not yet published
npm run build                  # only books with "status": "published"
```

A book appears on the site only when its `meta.json` has `"status": "published"`. Pushing to `main` builds the PDFs, EPUBs and site and deploys them to GitHub Pages (Settings → Pages → Source: GitHub Actions).

## Content format

Each `urdu/NNNN.md` and `en/NNNN.md` is one page of the source scan, with the same number. A line starting with `#` gives the page's table-of-contents title (for a diwan, the ghazal's opening words). Inside a ghazal, each misra is a line and each sher is separated by a blank line.
