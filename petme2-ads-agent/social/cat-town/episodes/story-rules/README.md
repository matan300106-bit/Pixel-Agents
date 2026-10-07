# Cat Town rules story (photos, IG + TikTok)

Final files: project files `cat-town/story-rules/` (cat-town-rules-1..5.jpg + posting.md with sticker spots). Not in git.
Cards (v2, catchier, drawn by photo_overlay.js): MEET MANGO + bubble · RULE #1 you follow, a cat moves in (EXAMPLE house) · RULE #2 top comment gets built (EXAMPLE statue) · RULE #3 weird ideas? yes pls · FILL THE TOWN, goal 1,000 cats, follow + comment.

Build (same setup as ../story-1, static server on :8772 at the scratch root): `python3 mk.py r`, `python3 text.py r`,
`node render.js r test 1.0,9.5,19.5,12.0,4.9` (card order 1..5). Uses ../story-1/overlay.js features (beat.st for the small-line y).
