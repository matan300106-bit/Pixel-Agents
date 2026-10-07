# PETME2 Cat Town: "Top comment → we build it" video (rule-v1)

Final video (18.2 s, 1080x1920): project files `cat-town/top-comment/cat-town-top-comment.mp4` (not in git), cover `cover.jpg`, posting text `posting.md`.
Plan: `viral-plan.md` (also the daily template, section 7). Reviewer: `review.md` (cut 1 6.5/10, cut 2 READY 7.5/10; after that the hook camera was tilted so Mango sits clear of the headline).

## Rebuild (free tools only)
Scratch folder with `npm i three@0.170.0 @fontsource/nunito playwright`, a copy of `../../catcity.html` and `../../previews/p_1000.json`, served by `python3 -m http.server 8772`. Kokoro model files from github.com/thewh1teagle/kokoro-onnx releases in /tmp/tts.
1. `python3 voice_gen.py lines.json` in the work dir (writes l00..l08.wav + lines.json)
2. `python3 mk.py v` (3 engine pages: e0 real town + "Your idea here?" sign + example comment card, e1 + example Mango statue, e2 1,000-cat goal town)
3. `python3 text.py v` (voice timing, headlines, EXAMPLE stamp windows)
4. `node render.js v range 0 546` (split in 4 for speed), `python3 audio.py v`, ffmpeg mux.

Notes: the badge (PETME2 CAT TOWN + count + Day) is drawn by `overlay.js`; the counter is real (1 cat) except "1,000 · THE GOAL" in the goal shot. Demo comment and build are marked EXAMPLE. The engine turns Halloween on from Oct 24 by render date.
