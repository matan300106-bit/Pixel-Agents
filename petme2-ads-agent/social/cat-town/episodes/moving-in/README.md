# Cat Town "Are you moving in?" (happy, Disney-style, about 22 s)

Matan's own script (2026-10-07), polished: "One follow… one cat house! / Welcome to PETME2 Cat Town! / Right now, it's just an empty road… and a little bit of grass! /
Only one thing is missing… / You! / Every follower gets a cat house, with a real address! / And every day, the top comment decides what we build! /
Together, we grow the city! / Soooo… are you moving in?" Script + research: project files `cat-town/script/moving-in-script.md` (v3) and `viral-psychology-research.md`.

Look: warm grade + glow, sparkles (swirl, burst, wand trail, wipe), fireworks, emoji pops (grass boing, wave), speech bubbles, EXAMPLE stamps.
Sound: code-synth music-box waltz in C (138 bpm), birds, boing, chimes, poof + splash, fireworks, meows.

Build (same free pipeline as viral-1): work dir with catcity.html, p_1000.json (from ../../previews), node_modules (three@0.170.0, @fontsource/nunito, playwright),
Kokoro model files (kokoro-v1.0.onnx, voices-v1.0.bin from github.com/thewh1teagle/kokoro-onnx releases) in /tmp/tts, `python3 -m http.server 8772`.
In the work dir: `cd v && python3 voice_gen.py in.json` (in.json = copy of lines.json; "PETME2" is said as "Pet Me Two", the long "Soooo" uses raw phonemes),
then `mk.py v`, `text.py v`, `audio.py v`, `node render.js v range 0 660` (split in 4), ffmpeg mux.
Notes: the build spot (SPOTS[0]) is at x 0, z 50.3; hook house = lot 1 (blue cat-face house), second house = lot 2 (box house).
