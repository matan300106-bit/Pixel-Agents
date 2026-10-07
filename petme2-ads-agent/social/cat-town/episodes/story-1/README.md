# Cat Town Instagram story (story-1): 3 cards x 5 s

Final files: project files `cat-town/story/`: 3 photos cat-town-story-photo-1/2/3.jpg (Matan asked for photos, not video; `photos_text.py` + `node render.js p test 1.0,9.5,14.9`), plus the earlier video cards cat-town-story-1/2/3.mp4 + all-in-one, posting.md with sticker spots. Not in git.
Cards: 1 Mango alone ("This is Mango", population 1 cat), 2 three EXAMPLE houses pop (1 follow = 1 new cat + your name), 3 "Your idea here?" sign, "What do we build next?" with grass left empty for a Question sticker.

Build (same free pipeline as ../rule-v1/README.md, one 15 s timeline then cut at 5 s and 10 s):
1. `python3 voice_gen.py lines.json` in the work dir v/ (Kokoro af_heart, speed 1.12)
2. `python3 mk.py v`, `python3 text.py v`
3. `node render.js v range 0 450` (split in 4), `python3 audio.py v`
4. ffmpeg: frames + mix.wav -> full.mp4, then `-ss 0/5/10 -t 5` per card with a short audio fade.

The reference story Matan linked (Instagram) could not be opened from the cloud container (403).
