# Cat Town Day 1 (v2) video

Final video (18.8 s, 1080x1920): project files `cat-town/day-1/cat-town-day1.mp4` (not in git, 18 MB). Cover: `cover.jpg`.
Plan: `viral-plan.md`. Reviewer report on the first cut: `review.md` (6/10); fixes applied after it: brand sign renamed "Pet Shop" in the goal town, captions hidden when they repeat the big text, end card cut to 4 words + "Follow" button, exact loop (last segment anim = T - 18.4 so the last frame matches frame 0, text fades out), tag kept inside the safe zone, louder pops, music lower, stereo audio, "TODAY: 1 CAT". Later polish: goal shot held 0.4 s longer (lines after it shifted), clean cover without subtitles.

## Free pipeline (no paid credits)
- Voice: Kokoro TTS (`af_heart`, speed 1.12) run locally (`voice_gen.py`; model files from github.com/thewh1teagle/kokoro-onnx releases). edge-tts is blocked from the cloud container (403), and files can't be copied back from the Composio sandbox.
- 3D: `catcity.html` (read-only copy) with `mk.py` (camera shots + 3 episode JSONs: e0 empty Day 1, e1 + 3 example houses, e2 1,000-cat goal town). `render.js` renders frames with the text layer `overlay.js` + `text.json`. Segments use different `anim` offsets so Mango drinks / eats on cue.
- Audio: `audio.py` (synth music, pops, whooshes, ducking) then ffmpeg loudnorm.

## Posting package (owner approves before anything is posted)
Caption:
Mango is the only cat in this town. Every new follow moves one more cat in. 🐱
Follow and your cat gets its own house with your @ on it. Most-liked comment picks what we build next (cat airport?) 👇
Day 1 of Cat Town. Goal: 1,000 cats.
#cattown #catsofinstagram #cats #3danimation

Pinned comment: Mango needs a neighbor. Follow + drop your cat's name, the first followers move in on Day 2. Most-liked reply = what we build next. Cat airport? Sushi bar?

Tips: post as a Trial Reel first, 6-8 pm, reply to every comment in the first hour.

## Open ideas (need the town build thread)
- Mango has no face; the reviewer's #1 hook fix is a simple face or a look-back + ear twitch at 0.4 s.
- A cat stepping out of each new house when it pops.
