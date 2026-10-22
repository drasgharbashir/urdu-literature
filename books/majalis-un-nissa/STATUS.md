# Majalis-un-Nissa — WORK IN PROGRESS (do not publish yet)

There is deliberately no `book.json` here, so this folder cannot be published as it stands.

Author: Altaf Husain Hali (d. 1914), public domain.
Source: archive.org `in.ernet.dli.2015.373957` ("Majalis Unnisa", Hali Press, Panipat, 1924 / 1342 AH; State Central Library Hyderabad copy), 244 PDF pages.
Page map: part 1 book p = PDF p - 2 (pp. 1-130 = PDF 3-132); part 2 pp. 1-106 = PDF 137-242.
The 1924 publisher's ads and press notes are omitted.

## Done
| Majlis | Book pages | Urdu transcribed | English | Chapter files |
|---|---|---|---|---|
| 1 | I.1-22 | yes | yes, parity checked | chapters/02-ur.txt, 02-en.txt |
| 2 | I.23-47 | yes | yes, parity checked | chapters/03 |
| 3 | I.48-75 | yes | yes, parity checked | chapters/04 |
| 4 | I.76-101 | yes | yes, parity checked | chapters/05 |
| 5 | I.102-130 (end of part 1) | yes: work/m5.txt, processed work/m5.ur | NOT yet translated | - |

## To do
1. Translate majlis 5 (write work/m5.en with the same blocks as m5.ur; footnotes [1]-[4]; then `python3 notes.py m5` with an m5.nmap.json, and `split.py` to split long paragraphs). Contains a Persian couplet (Sa'di, *Bustan*: "سپردم بتو مایۂ خویش را / تو دانی حساب کم و بیش را") that needs a translation plus the original in a note.
2. Part 2: majalis 6 (II.1), 7 (II.22), 8 (II.58), 9 (II.79) to the end "تمام شد" at II.106; check whether a 10th majlis starts between II.79 and II.106.
3. Chapter 01 "About this edition" + introduction; final glossary chapter; book.json (slug majalis-un-nissa, genre novel); PROGRESS.md; catalog row.

## Conventions used
- Speaker abbreviations expanded: آ = آتوجی (Atu-ji), م / م ب = محمودہ بیگم, ب ب = بڑی بیگم, م ز = مریم زمانی.
- Printed word-gloss footnotes kept, renumbered per chapter as [n], listed at chapter end under "# حواشی" / "# Notes".
- Uncertain readings to note in PROGRESS.md: I.4 "جمی جم"; I.9 "اداسی چھا گئی" (library stamp); I.14 "دہشت" (print looks like "دباغت"); I.18 "اپنے پڑھنے سے"; I.36 right-margin letters restored from context; I.42 "بیڑی روٹی"; I.45 line 3 faint; I.48 "علم کا چرچا نہیں"; I.56 "ہیضہ کو تھتکارا" as printed; I.82 "دو من دس سیر" (print unclear); I.85 "تلا چڑھوا"; I.87 "ڈھکنی", "نماز کی چوکی" (smudged); I.100 "اکڑا"; I.116 "رونکھی".
- Scripts in work/: proc.py (raw page transcription to blocks + notes), notes.py, split.py, crop.py.

## Majlis 6 (II.1–21) notes
- II.16: printed "دیکھو، کبھی تم ان کو عیب نہ جانو" contradicts the sense; translated by sense with a [TN].
- II.17: read "ایک جمعے کے دن تو سفر نہ کرنا" (the word is smudged; "عذر" is the other possible reading but makes no sense).
- II.20: read "مگر بہت ضرور تینوں زبانوں کا سیکھنا ہے".
- II.2/II.3: the catchword at the foot of II.2 ("اس") is not repeated in the text.
