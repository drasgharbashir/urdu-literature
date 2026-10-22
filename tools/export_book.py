#!/usr/bin/env python3
"""Build the bilingual PDF and EPUB for one book from content/books/<slug>/.

    python tools/export_book.py diwan-e-ghalib            # writes site/public/downloads/
    python tools/export_book.py diwan-e-ghalib --out dist

PDF: WeasyPrint (pip install weasyprint), Urdu and English side by side.
EPUB: pandoc, each page as Urdu followed by English (e-readers have no columns).
Fonts: Noto Nastaliq Urdu and Source Serif 4 are downloaded once into
tools/fonts/ (not committed) and embedded in both files.
"""
import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOKS = ROOT / "content" / "books"
FONT_DIR = Path(__file__).resolve().parent / "fonts"
# Google Fonts CSS API: with no browser User-Agent it answers with plain TTF URLs.
FONTS = {
    "NotoNastaliqUrdu.ttf": "https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu",
    "SourceSerif4.ttf": "https://fonts.googleapis.com/css2?family=Source+Serif+4",
}


def fonts():
    FONT_DIR.mkdir(exist_ok=True)
    for name, src in FONTS.items():
        dest = FONT_DIR / name
        if not dest.exists():
            print(f"Downloading font {name}")
            css = urllib.request.urlopen(src).read().decode()
            ttf = re.search(r"url\((https://[^)]+\.ttf)\)", css).group(1)
            with urllib.request.urlopen(ttf) as r, open(dest, "wb") as f:
                shutil.copyfileobj(r, f)
    return {n: FONT_DIR / n for n in FONTS}


def load(slug):
    d = BOOKS / slug
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
    nums = sorted({p.stem for sub in ("urdu", "en") for p in (d / sub).glob("[0-9][0-9][0-9][0-9].md")})
    pages = []
    for n in nums:
        ur = d / "urdu" / f"{n}.md"
        en = d / "en" / f"{n}.md"
        pages.append((n, ur.read_text(encoding="utf-8") if ur.exists() else "",
                      en.read_text(encoding="utf-8") if en.exists() else ""))
    g = d / "glossary.json"
    glossary = json.loads(g.read_text(encoding="utf-8")) if g.exists() else []
    return meta, pages, glossary


def md_to_html(md):
    """Small Markdown subset used in content/: headings, *italics*, **bold**,
    blank-line paragraphs, single newlines as line breaks."""
    out = []
    for block in re.split(r"\n\s*\n", md.strip()):
        if not block.strip():
            continue
        m = re.match(r"^(#{1,3})\s+(.+)$", block.strip())
        if m and "\n" not in block.strip():
            out.append(f"<h3>{inline(m.group(2))}</h3>")
        else:
            out.append("<p>" + "<br/>".join(inline(l) for l in block.strip().split("\n")) + "</p>")
    return "\n".join(out)


def inline(s):
    s = html.escape(s.strip())
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def source_html(meta):
    rows = [("Author", meta.get("author", "")), ("Edition", meta.get("edition", "")),
            ("Year", meta.get("edition_year", "")), ("First published", meta.get("first_published", "")),
            ("Scan", meta.get("source_url", ""))]
    return "".join(f"<tr><th>{k}</th><td>{html.escape(str(v))}</td></tr>" for k, v in rows if v)


def glossary_html(glossary):
    items = sorted(glossary, key=lambda t: t["term"].lower())
    return "".join(
        f'<dt><em>{html.escape(t["term"])}</em> <span lang="ur" dir="rtl">{html.escape(t.get("ur", ""))}</span></dt>'
        f'<dd>{html.escape(t["gloss"])}</dd>' for t in items)


def build_pdf(meta, pages, glossary, out, f):
    from weasyprint import HTML
    body = []
    for n, ur, en in pages:
        body.append(f'<section class="page"><div class="pno">{int(n)}</div><table class="pair"><tr>'
                    f'<td class="en" lang="en">{md_to_html(en) or "<p>—</p>"}</td>'
                    f'<td class="ur" lang="ur" dir="rtl">{md_to_html(ur) or "<p>—</p>"}</td>'
                    f'</tr></table></section>')
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(meta['title_en'])}</title>
<style>
@font-face {{ font-family: Nastaliq; src: url('{f["NotoNastaliqUrdu.ttf"].as_uri()}'); }}
@font-face {{ font-family: Serif; src: url('{f["SourceSerif4.ttf"].as_uri()}'); }}
@page {{ size: A4; margin: 18mm 16mm; @bottom-center {{ content: counter(page); font: 9pt Serif; color: #777; }} }}
body {{ font-family: Serif; font-size: 10.5pt; line-height: 1.5; color: #222; }}
[lang=ur] {{ font-family: Nastaliq; line-height: 2.2; }}
.title {{ text-align: center; page-break-after: always; padding-top: 60mm; }}
.title .ur {{ font-size: 30pt; }}
.title h1 {{ font-size: 24pt; font-weight: 600; margin: 8mm 0 4mm; }}
.title table {{ margin: 20mm auto 0; font-size: 9.5pt; text-align: left; }}
.title th {{ padding-right: 6mm; color: #666; font-weight: normal; }}
.page {{ page-break-inside: auto; margin-bottom: 8mm; }}
.pno {{ font-size: 8.5pt; color: #999; border-bottom: .4pt solid #ccc; margin-bottom: 3mm; }}
table.pair {{ width: 100%; border-collapse: collapse; table-layout: fixed; }}
table.pair td {{ vertical-align: top; width: 50%; }}
td.en {{ padding-right: 5mm; }}
td.ur {{ padding-left: 5mm; text-align: right; font-size: 12.5pt; }}
p {{ margin: 0 0 3.5mm; }}
h3 {{ font-size: 11pt; margin: 0 0 3mm; color: #7a2e1f; }}
td.ur h3 {{ font-size: 13pt; }}
.gloss {{ page-break-before: always; }}
.gloss dt {{ margin-top: 3mm; font-weight: 600; }}
.gloss dd {{ margin: 0; }}
</style></head><body>
<div class="title"><div class="ur" lang="ur" dir="rtl">{html.escape(meta['title_ur'])}</div>
<h1>{html.escape(meta['title_en'])}</h1><div>{html.escape(meta.get('author', ''))}</div>
<table>{source_html(meta)}</table></div>
{''.join(body)}
{'<section class="gloss"><h2>Glossary</h2><dl>' + glossary_html(glossary) + '</dl></section>' if glossary else ''}
</body></html>"""
    HTML(string=doc, base_url=str(ROOT)).write_pdf(out)


def build_epub(meta, pages, glossary, out, f):
    if not shutil.which("pandoc"):
        sys.exit("pandoc is not installed")
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        chapters = [f'<section class="title"><p class="ur" lang="ur" dir="rtl">{html.escape(meta["title_ur"])}</p>'
                    f'<p>{html.escape(meta.get("author", ""))}</p><table>{source_html(meta)}</table></section>']
        for n, ur, en in pages:
            first = (re.search(r"^#{1,3}\s+(.+)$", en, re.M) or [None, f"Page {int(n)}"])[1]
            chapters.append(f'<section><h1>{inline(first)}</h1>'
                            f'<div class="ur" lang="ur" dir="rtl">{md_to_html(ur)}</div>'
                            f'<div class="en" lang="en">{md_to_html(en)}</div></section>')
        if glossary:
            chapters.append(f'<section><h1>Glossary</h1><dl>{glossary_html(glossary)}</dl></section>')
        src = tmp / "book.html"
        src.write_text(f'<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(meta["title_en"])}</title></head>'
                       f'<body>{"".join(chapters)}</body></html>', encoding="utf-8")
        css = tmp / "epub.css"
        css.write_text("""
@font-face { font-family: Nastaliq; src: url(NotoNastaliqUrdu.ttf); }
@font-face { font-family: Serif; src: url(SourceSerif4.ttf); }
body { font-family: Serif, serif; line-height: 1.5; }
.ur { font-family: Nastaliq, serif; line-height: 2.2; text-align: right; direction: rtl; font-size: 1.15em; margin-bottom: 1em; }
.en { border-top: 1px solid #ccc; padding-top: .8em; }
h1 { font-size: 1.1em; color: #7a2e1f; }
.title { text-align: center; }
""", encoding="utf-8")
        cmd = ["pandoc", str(src), "-f", "html", "-o", str(out), "--css", str(css),
               "--metadata", f"title={meta['title_en']}", "--metadata", f"author={meta.get('author', '')}",
               "--metadata", "lang=en", "--split-level=1"]
        for font in f.values():
            cmd += ["--epub-embed-font", str(font)]
        subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--out", default=str(ROOT / "site" / "public" / "downloads"))
    ap.add_argument("--only", choices=["pdf", "epub"])
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    meta, pages, glossary = load(args.slug)
    if not pages:
        sys.exit(f"{args.slug} has no pages yet")
    f = fonts()
    if args.only != "epub":
        build_pdf(meta, pages, glossary, out / f"{args.slug}.pdf", f)
        print("Wrote", out / f"{args.slug}.pdf")
    if args.only != "pdf":
        build_epub(meta, pages, glossary, out / f"{args.slug}.epub", f)
        print("Wrote", out / f"{args.slug}.epub")


if __name__ == "__main__":
    main()
