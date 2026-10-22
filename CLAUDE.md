# Classical Urdu Library — project instructions

## Goal
Find public-domain classical Urdu books, download them, extract the Urdu text, translate them into English, and publish each book on the website with the Urdu original and the English translation side by side, plus PDF and EPUB downloads.

## Repository layout
```
tools/urdu_library.py      # finder/downloader/OCR tool (search, download, prepare, merge, status)
tools/authors.json         # classical authors list (death years, search spellings)
library/catalog.csv        # one row per book, its status and paths (committed)
library/books/...          # downloaded PDFs and OCR output (NOT committed; .gitignore)
content/books/<slug>/      # cleaned text and translations (committed)
  meta.json                #   title (Urdu + English), author, year, source URL, page count
  urdu/0001.md ...         #   cleaned Urdu text, one file per page
  en/0001.md ...           #   English translation, same numbering
site/                      # Astro website
```

## Pipeline for each book (statuses in catalog.csv)
`found → downloaded → ocr_done → cleaned → translated → reviewed → published`

1. **Download:** `python tools/urdu_library.py download --limit N`.
2. **OCR:** `python tools/urdu_library.py prepare`. If the Tesseract output is garbage (Nastaliq print), view the page images directly and transcribe the Urdu yourself, one page at a time.
3. **Clean:** fix OCR errors, rejoin broken lines, keep verse lines (misre) as separate lines and couplets (sher) together, and remove page headers, footers and page numbers. Write the result to `content/books/<slug>/urdu/NNNN.md`.
4. **Translate:** follow the rules below and write to `en/NNNN.md` with the same page numbers.
5. **Review:** re-read the translation against the Urdu, check that every page has a translation, and set the status to `reviewed`.
6. **Publish:** build the site, generate the PDF and EPUB, and set the status to `published`.

Update `catalog.csv` after every step. Commit after each book (`book: <slug> <status>`).

## Translation rules
- Translate faithfully into clear, modern English. Don't summarise or skip anything; note any unreadable passage as `[illegible]`.
- **Poetry:** translate each sher as two lines and keep line breaks. Accuracy comes before rhyme. Keep the takhallus (pen name) as a name.
- **Prose:** keep the paragraph structure. Dialogue stays as dialogue.
- **Cultural terms:** keep key Urdu/Persian terms in italics with a short gloss the first time they appear, e.g. *ghazal* (lyric poem), *mushaira* (poetry gathering). Add a glossary page per book.
- **Names:** use one consistent transliteration per book, recorded in `meta.json`: Ghalib, Mir Taqi Mir, Dilli/Delhi, Lakhnau/Lucknow.
- **Quotations:** translate Arabic and Persian quotations too, keeping the original in a note.
- Mark translator's notes as `[TN: …]`. Never invent content to fill gaps.

## Copyright rules (must follow)
- Only use books whose author died **1961 or earlier** (out of copyright in Pakistan and India). Only download from freely downloadable sources (archive.org, not lending-library items). Never download from Rekhta or any site that restricts downloads.
- Skip rows marked `needs_review=yes` unless I approve them. Modern editions may carry copyrighted introductions, notes or editing: use only the author's original text and drop modern editorial matter.
- Record the source URL, edition and year in `meta.json`, and show them on the book's page.
- Flag any work first published in 1931 or later in `meta.json` as `"us_status": "check"` (it may still be under US copyright).

## Website (site/)
- Astro static site, deployed with GitHub Pages (free).
- Pages: home, authors (from `authors.json`), each author's page, each book's page with a table of contents and reading pages (Urdu right-to-left on one side, English on the other; stacked on mobile), glossary, search, and an about/copyright page.
- Urdu font: Noto Nastaliq Urdu (Google Fonts), `dir="rtl" lang="ur"`. English: a clean serif.
- Downloads per book: bilingual PDF and EPUB generated from `content/` (pandoc or WeasyPrint).
- Each page gets its own title, description and Open Graph tags for search engines.

## Working style
- Work in batches. Finish one book end-to-end before starting the next, unless I ask for bulk downloading.
- Start with short, high-value books: Diwan-e-Ghalib, Bagh-o-Bahar, Mirat-ul-Uroos, Umrao Jaan Ada, Musaddas-e-Hali.
- Never commit large PDFs or images. Keep `library/books/` in `.gitignore`.
- Stop and ask me before publishing a book for the first time, deleting anything, or changing these rules.
