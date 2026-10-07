# Day 1 v4: "This is Mango" (about 20.4 s)

Matan's improved Day 1 video. Story: This is Mango, the only cat in town. He has water and food, but no one to share it with.
Every new follow brings a new cat with a house and your name (3 house pops with sounds and @you tags).
Every day the top comment gets built (IG-style comment card, likes roll up, "Build a Mango statue!" wins, a medium-to-big Mango statue pops with confetti).
Then the 1,000-cat goal town, "Comment below", and a loop back to "This is Mango".

Free pipeline: Kokoro TTS (af_heart, speed 1.12), headless Chromium + the Cat Town engine, numpy synth music/SFX, ffmpeg.

Build (scratch dirs as in day-1-v3): `voice.py` on lines.json, then `mk.py OUT`, `text.py OUT`, `audio.py OUT`,
then `node render.js OUT range i0 i1` (612 frames at 30 fps), then mux with ffmpeg.

Notes:
- New houses use `order: 'index'` so they pop at 7.35 / 8.25 / 9.03 s, one per shot.
- overlay.js `pinTags` pins the house tags at y=900 so they sit under the headline; `hideTags` hides the statue build tag (it covered the badge).
- Demo content (comments, @you, statue) carries EXAMPLE stamps. Not posted; Matan approves first.
