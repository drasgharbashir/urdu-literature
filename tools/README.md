# Classical Urdu Library

Finds public-domain classical Urdu books on the Internet Archive (archive.org), downloads them, turns loose page scans into one PDF per book, and gets the text ready for translation.

## Setup (once)

1. Install Python 3.9 or newer.
2. `pip install pillow python-docx ocrmypdf`
3. Install Tesseract with the Urdu language pack:
   - **Windows:** use the UB-Mannheim Tesseract installer and tick "Urdu" under additional languages. Ghostscript is also needed, for ocrmypdf.
   - **Mac:** `brew install tesseract tesseract-lang ghostscript`
   - **Ubuntu/Debian:** `sudo apt install tesseract-ocr tesseract-ocr-urd ghostscript`

Keep `urdu_library.py` and `authors.json` in the same folder.

## Use

```
python urdu_library.py run                           # find + download + prepare everything
python urdu_library.py search                        # only build the catalog (library/catalog.csv)
python urdu_library.py download --author Ghalib      # download one author's books
python urdu_library.py prepare --limit 3             # OCR three downloaded books
python urdu_library.py status                        # progress counts
python urdu_library.py merge path/to/page_images --out book.pdf --ocr
```

You can stop it at any time and run the same command again. It picks up where it left off, and `library/catalog.csv` records each book's status.

## What you get for each book (`library/books/<Author>/<id>/`)

| File | Use |
|---|---|
| `<id>.pdf` | The book as scanned. If archive.org only offers page images, they are merged into one PDF. |
| `<id>.searchable.pdf` | The same PDF with a hidden text layer. **Best for uploading to your website.** |
| `<id>.docx` / `<id>.md` | The Urdu text page by page, with an empty "Translation:" slot under each page. **Best for translating.** |
| `archive_ocr.txt` | archive.org's own text recognition, when it has some. |
| `metadata.json` | Title, publisher, year, etc., for your credits page. |

## Rules it follows

- **Authors:** the list in `authors.json` (58 poets and prose writers, from the Deccani period up to 1961). Each one died at least 65 years ago, so their works are out of copyright in both Pakistan (life + 50 years) and India (life + 60 years).
- **Books searched:** besides those authors, it also catalogs every Urdu book printed up to 1930 (change this with `--year-cutoff`).
- **Skipped automatically:** archive.org lending-library and print-disabled items. Only freely downloadable books are taken.
- **`needs_review = yes`:** books with no year, or printed after 1960. A modern edition can add copyrighted notes, introductions or editing, or the book may be by a modern writer with the same name. These are not downloaded unless you add `--include-review`.
- **US copyright:** if your website's audience or host is in the US, a work first published in 1931 or later can still be under copyright there, even if its author died long ago. Check the first-publication date before uploading those.

## About text recognition quality

Tesseract's Urdu model handles Naskh print well but struggles with Nastaliq calligraphy and lithographs, and most classical books are printed that way. If the `.docx` text comes out poor, upload the PDF to Google Drive and choose **Open with → Google Docs**. Google's recognition is usually much better on Nastaliq. Then translate from that document.

## Adding authors

Add an entry to `authors.json` with the author's death year and the spellings archive.org might use (`"search": [...]`). Then run `search` again.
