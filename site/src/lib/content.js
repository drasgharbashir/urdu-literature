// Reads books from ../content/books and authors from ../tools/authors.json
// at build time. Nothing here runs in the browser.
import fs from 'node:fs';
import path from 'node:path';
import { marked } from 'marked';

const ROOT = path.resolve(process.cwd(), '..');
const BOOKS_DIR = path.join(ROOT, 'content', 'books');
const AUTHORS_FILE = path.join(ROOT, 'tools', 'authors.json');

marked.setOptions({ breaks: true });

export function slugify(s) {
  return s.toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

export function getAuthors() {
  const authors = JSON.parse(fs.readFileSync(AUTHORS_FILE, 'utf-8'));
  return authors.map((a) => ({ ...a, slug: slugify(a.name) }));
}

function readPages(dir) {
  if (!fs.existsSync(dir)) return {};
  const out = {};
  for (const f of fs.readdirSync(dir).filter((f) => /^\d{4}\.md$/.test(f)).sort()) {
    out[f.slice(0, 4)] = fs.readFileSync(path.join(dir, f), 'utf-8');
  }
  return out;
}

// A page file may start with "# Heading" (e.g. a ghazal's radif); that line
// becomes the page's table-of-contents entry.
function pageTitle(md) {
  const m = md.match(/^#{1,3}\s+(.+)$/m);
  return m ? m[1].trim() : '';
}

export function render(md) {
  return marked.parse(md || '');
}

export function plainText(md) {
  return (md || '').replace(/^#+\s*/gm, '').replace(/[*_`>[\]]/g, '').replace(/\s+/g, ' ').trim();
}

// Only books whose status is "published" (or every book when SHOW_DRAFTS=1)
// are built into the site.
export function getBooks() {
  if (!fs.existsSync(BOOKS_DIR)) return [];
  const showDrafts = process.env.SHOW_DRAFTS === '1';
  const authors = getAuthors();
  const books = [];
  for (const slug of fs.readdirSync(BOOKS_DIR).sort()) {
    const metaFile = path.join(BOOKS_DIR, slug, 'meta.json');
    if (!fs.existsSync(metaFile)) continue;
    const meta = JSON.parse(fs.readFileSync(metaFile, 'utf-8'));
    if (meta.status !== 'published' && !showDrafts) continue;
    const ur = readPages(path.join(BOOKS_DIR, slug, 'urdu'));
    const en = readPages(path.join(BOOKS_DIR, slug, 'en'));
    const nums = [...new Set([...Object.keys(ur), ...Object.keys(en)])].sort();
    const pages = nums.map((n) => ({
      num: n,
      ur: ur[n] || '',
      en: en[n] || '',
      titleUr: pageTitle(ur[n] || ''),
      titleEn: pageTitle(en[n] || ''),
    }));
    const glossFile = path.join(BOOKS_DIR, slug, 'glossary.json');
    const glossary = fs.existsSync(glossFile) ? JSON.parse(fs.readFileSync(glossFile, 'utf-8')) : [];
    const author = authors.find((a) => a.name === meta.author) || null;
    books.push({ ...meta, slug, pages, glossary, authorSlug: author ? author.slug : slugify(meta.author || '') });
  }
  return books;
}

export function url(p = '') {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${p.replace(/^\//, '')}`;
}
