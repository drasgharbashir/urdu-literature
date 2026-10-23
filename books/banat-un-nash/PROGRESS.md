# Banat-un-Nash (banat-un-nash)

Produced by the cloud project thread "University-ready book list" (queue: /mnt/project-files/notes/book-queue.md).

## Source
- Author: Deputy Nazir Ahmad (1830/31-1912). Written c.1872 as Part 2 of Mirat-ul-Uroos (1869); the author's preface says Mirat-ul-Uroos was first printed "two and a quarter years" earlier. Public domain (author died 1912, first published before 1931); us_status not needed.
- Urdu text: archive.org `in.ernet.dli.2015.498588` (Digital Library of India, scanned at Allama Iqbal Library, University of Kashmir), catalogued "Binat-ul-nash", date 1950. Delhi reprint published by the author's grandson Muhammad Muslim Ahmad. 221 printed pages.
- Scan quirks: PDF63/64, PDF67/68 and PDF219/220 are page pairs in swapped order (fixed).

## Chapters
1 About this edition + Introduction (new); 2 Preface; 3-21 the author's sections with his own headings (ch20 holds two sections and keeps both headings); 22 Glossary (new, 40 entries).
The author's footnotes collected per chapter under "# حواشی" / "# Notes". Some headings carry a note marker, as printed (ch06, ch12, ch14, ch20).
All 22 chapters: ur/en block parity checked (tools/check_lang_parity.py and the thread's own checker).

## Left out
- Publisher's khatima (pp.221-222), signed by Muhammad Muslim Ahmad: modern editorial matter.
- Two footnotes that name Nazir Ahmad in the third person (p149 on Muntakhab-ul-Hikayat, p210 on Mirat-ul-Uroos): publisher's notes; dropped and the notes renumbered.
- Kept: the author's footnote dated 1888 (a later lifetime edition), marked with a TN.

## Status
- 23 Oct 2026: ur + en complete, reviewed against the Urdu, book.json written.
- book.json has "is_published": false on purpose: this is the book's first publication, which needs the owner's go-ahead (CLAUDE.md). Flip it to true when publishing.
- NEXT (PC): cover, publish_book.py, deploy, per the usual pipeline.
- 43 [illegible] spots, mostly footnotes cut off at the foot of the scan; a second scan of an early edition would fill them.

## Uncertain readings (page = printed page)
- p48 last word 'غریب' faint (read from context)
- p61: printed note 1 ('منہ' ...) could not be matched to a word in the text; omitted
- p73: 'دو روپے کا آٹھ گز کا تھان' as printed; answer 6 annas/yard fits 3 rupees for 8 yards
- p74: cistern sum 'دو سو تین من پانچ سیر' read as printed (6x6x2=72 cu yd x3 x25 x15 /16 ser... not checked)
- p78: speaker name محمودہ supplied at start (continues her speech across heading)
- p83: 'روپیہ بھر جگہ میں پانچ سیر' as printed (air pressure ~ per square inch)
- p84: 'چٹکی بھر . . . . میں' a word is blank/unprinted in the scan
- p88: 'بچے کی لینڈ دوڑتی' reading uncertain (bottom line half cut)
- p93: colour list 'زرد، سیاہ، سرخ' as printed (probably misprint for نیلا)
- p94: 'پلٹا جی' (earlier list said قدم شریف) as printed
- p98: 'کشش زمین . . . . ہم کو' gap in print; 'خدا جانے کے کروڑ کے لاکھ دفعہ' as printed
- p102: two note markers on p102 (bhai jan, etc.) — notes cut off at foot of scan, markers dropped
- p115: 'اے، ہے لازم نہیں' read as printed (اے ہے، لازم نہیں)
- p119: 'بوندا باندی کی ذرا' reading uncertain; 'جینا گوشت' as printed
- p120: 'ان سے بھی سوچ سمجھ کر کیا ہوئے ہیر نے کہا' and 'ٹینٹ پڑ جائیں، انار رکھے' reading uncertain
- p123: 'بھی سر پر بال رکھنے تھے' and 'جب تک بال چھوڑے ہی' reading uncertain
- p127: 'گھر ہی میں' read as گھر دل؟ ; fn3 'دیہات والے دلی میں' partly blurred; 'چنے پرمل'
- p128: 'بھنتے ہوئے' (print looks like بھلتے); 'منہ سوئی، پیٹ کوئی' reading uncertain; fn2 'بھربھرے' faint
- p129: 'ست بجی' (ست نجی?) uncertain; 'زبیدہ جیسی شیخوں کے نام لیوا' (word 'ہیں' supplied? check); last word after (ہڈی) blurred
- p132: 'روکھی بھدی' (print روڑھی?), 'ہنڈری کی چنری' obscure, 'دبلا دبیل', 'سوکھے ہوئے' (print سونتے?), 'روگی اور اپاہج' faint; doha 'ہر کا بھجے' as printed
- p133: fn5 read as 'گرمی ملاقات' (print looks گھڑی?); quote closing after narration line appears in print but treated as narration
- p135: 'تنجن' in print read as متنجن (sweet rice) per footnote
- p136: heading 'طولانی' has small gloss (طویل) in print, omitted; 'ادھی کی دوا' (half-pice); speech of استانی جی continues without opening quote
- p137: 'اس حد کو پہنچایا' (print looks 'اس ہدڑے کو')
- p138: footnotes 1-4 cut off at foot of scan; 'وید' (print بیاد?); 'تیج تہوار' (print 'تیر تہوار'), 'جو' supplied
- p140: 'ایک چالیسے کے کال' (print 'ایک چوآلی'?) uncertain; 'جس کو تم سا کہتی ہو' unclear (سستا?); 'ایک برسات' as printed (? اے بیٹی); possible fn marker on شاذ و نادر with no visible note
- p141: 'گے باولے' (print), 'بانہہ' supplied for 'بانھ'; fn1 'اس جگہ کو' read
- p143: "دونوں وقت ملے جا ضرور جانے سے" uncertain; speaker of "خدا کی پناہ، لڑکی!..." looks like میں in scan but must be نانی (next line is میں) — set to نانی
- p144: 'چندرے' + fn1 'یعنی چند روزہ اور' partly unclear; 'مجھی سر کی تھی' as printed; 'اولتیوں' (eaves) for print اولیتوں
- p146: 'جھلائے گا' as printed (جھلائیے گا?)
- p147: 'بھچا بھچا' (cramped) as printed; 'ٹھہریں پر نہ ٹھہریں' (print 'ٹھہریں پر نہ ٹھہریں'?)
- p148: 'کچھ ایسی گھڑی کاٹا کیا ہے' as printed (? گھڑی کا نہ کیا); closing quote for استانی جی's long speech (opened p135) placed after 'بسر ہوتی ہے۔'; 'خدا کی سنوار' as printed
- p149: footnote on منتخب الحکایات ('ڈپٹی نذیر احمد کی مشہور کتاب جو بچوں کے لیے ہے...') names the author in the third person = 1950 publisher's note; DROPPED as modern editorial matter
- p150: last line before p151 cut off at foot of scan -> [illegible]; p151: stray superscript after 'جو کتاب' with no visible note, ignored
- p152: verse kept as printed 'آدمیت اور شے ہے، عقل ہے کچھ اور چیز' (Zauq's usual text has علم); 'یک من' marker ۴ fn cut off
- p158: 'غش یہ تو' as printed; final sentence parenthesised (print has no brackets, it is narration after the speech)
- p159: fn1 second word unclear ('پھڑک گئی'?); two consecutive نازپرورد labels as printed
- p162: footnotes 1-4 cut off (۴ probably 'جابر کی بی بی کا نام'); 'پرتو' marker position guessed; 'عذرا' = Jabir's wife (not named before in text)
- p163: 'طلاق قن ہے' as printed (? طلاق دی ہے/مطلقہ ہے) unclear
- p166: 'دس میں گو حج کرا دیا' as printed (unclear); fn3 illegible; page header missing in scan
- p172: right margin of scan cropped; the 2nd paragraph is labelled حسن آرا in print but reads like کلثوم's answer — label kept as printed, cropped words [illegible]
- p173: handwritten margin note in scan ignored
- p174: hill-station names as printed: 'سبا تو' (Sabathu), 'لنڈھور' (Landour)
- p174 end: last line partly cut off -> [illegible]
- p180: markers ۱ (اشتعال) and ۲ (نیستان) present but the footnotes are not on this page in the scan
- p182: 'نوک دار چیز سے گریز کرتی ہے' as printed (factually inverted, kept); 'کلس دیکھتی ہو' as printed
- p183: speaker label at start of 2nd paragraph faint, read as حسن آرا
- p185: 'بابا اصل' as printed (name? 'Miss Baba Ethel'?) — kept; 'پیاز پہیلی' as printed (? پھیلی)
- p187: 'ایسا تو کوئی ہندوستانی بھی اگر نہیں رہا' as printed (sense: not even an Indian tenant has been so quiet); 'اکھڑتی' (? اکھڑتی/جھڑکتی)
- p188: 'خدا ایسا دکھیں نہ بیاہا' as printed, obscure; no footnote on بساط visible (marker uncertain) — removed marker
- p189: 'جب یہ آپس میں ملاپ رکھیں' as printed — sense requires 'نہ رکھیں'; kept as printed
- p190: 'دو سو روپیہ کا دو سو روپے مہینہ' as printed (dittography); footnotes cut off (۱ بے لطفی, ۲ ناسازگاری?, ۳ فریفتہ)
- p192: 'طسلہ' (طشلہ = washbasin) as printed; last words 'ایک کنیز منگا طشتری' read uncertainly (? ایک کشتی منگا، طشتریوں)
- p198: footnote marker on درگزر with no footnote printed; marker dropped
- p200: final line cut off after 'ورنہ روئے زمین'; closing quote supplied
- p202: fn1 marker is on اجرام in the heading; moved into first text line? NOTE: heading has [1] — fix at build (headings can't carry markers)
- p204: 'ڈیڑھ کوس' as printed though teacher said 'ڈیڑھ میل'
- p210: fn on مراۃ العروس ('مولانا نذیر احمد کی سبق آموز دلچسپ کتابیں') is publisher matter, dropped & renumbered; 'مانجھوں بیٹھنے' (print 'مایوں بیٹھنے')
- p211: 'سچل' (marker ۴ 'عمدہ') read uncertainly; dialogue 'میں:' inside سلطانہ بیگم's report kept as printed
- p216: 'باہر، شہر، ہر جگہ تمہارے واسطے نہیں' as printed (sense: distance is nothing for you); 'اگر آنا چاہو تو پھر نہیں' as printed (? 'تو دور نہیں')
- p217: fn4 and fn6 glosses read uncertainly; fn11 end runs into binding margin
- p218: 'جو فائدہ تم کو اس مکتب سے پہنچا رہے گا' sentence incomplete as printed
- p220: printed closing quote after 'ساتھ جاتے ہیں' then new para without quote — treated as continuous speech of استانی جی (closing quote dropped)
- END: book text ends p221 'فقط'. Following 'خاتمہ' (pp.221-222) signed by Muhammad Muslim Ahmad, grandson, publisher's afterword — DROPPED as modern editorial matter. Last page has Allama Iqbal Library (Kashmir Univ, Srinagar) stamp.
