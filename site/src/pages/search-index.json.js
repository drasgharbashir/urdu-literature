import { getBooks, plainText } from '../lib/content.js';

export function GET() {
  const items = getBooks().flatMap((b) => b.pages.map((p) => ({
    b: b.slug, bt: b.title_en, n: p.num, t: p.titleEn,
    en: plainText(p.en), ur: plainText(p.ur),
  })));
  return new Response(JSON.stringify(items), { headers: { 'Content-Type': 'application/json' } });
}
