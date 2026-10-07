# Cat Town rules story (photos, IG + TikTok)

Final files: project files `cat-town/story-rules/` (cat-town-rules-1..5.jpg + posting.md with sticker spots). Not in git.
Cards: hook (Mango) · Rule 1 follow = new cat + house (EXAMPLE) · Rule 2 top comment in 24 h gets built (EXAMPLE Mango statue) · Rule 3 weird = good, rude/political/unsafe skipped (sign) · "Mango needs friends, follow + comment" (whole town).

Build (same setup as ../story-1, static server on :8772 at the scratch root): `python3 mk.py r`, `python3 text.py r`,
`node render.js r test 1.0,9.5,19.5,12.0,4.9` (card order 1..5). Uses ../story-1/overlay.js features (beat.st for the small-line y).
