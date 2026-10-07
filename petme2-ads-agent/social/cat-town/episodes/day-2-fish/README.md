# Day 2: "Fish supermarket" (18.3 s)

Top comment (real, by PIKA): "add a fish supermarket". Matan: keep the town empty (only Mango, 1 cat) and don't show the like count.
Story: Day 2 → population 1 cat → top comment = we build it → the comment card (heart, no number) → the Fish Supermarket pops with confetti and a "PIKA built the Fish Supermarket" tag → "Now Mango just needs friends to shop with" → 1 follow = 1 new cat → let's build it together → what do we build next? → loops to the hook.

Final: project files `cat-town/day-2-fish/` (mp4, cover, posting.md, close-up, website phone view). Not posted; Matan approves first.

Build (free tools, same as rule-v1): scratch folder with three@0.170.0, @fontsource/nunito, playwright, a copy of `../../catcity.html`, served on :8772. Kokoro files in /tmp/tts.
1. `python3 voice_gen.py lines_in.json` in the work dir `v` (writes l00..l09.wav + lines.json)
2. `python3 mk.py v` (one engine page e1.json), `python3 text.py v`
3. `node render.js v range 0 549` (split in 4), `python3 audio.py v`, ffmpeg mux (libx264 crf 18 + aac 192k).
