# Cat Town viral-1: "Population: 1 cat" (14.8 s, TikTok-first)

Made 2026-10-07 for Matan's ask "make a different video that goes viral, freestyle it".
Final: project files `cat-town/viral-1/` (cat-town-viral.mp4, cover, posting.md). Not posted; Matan approves first.

Story (sad to happy, your name in it, seamless loop):
0-4 s lonely Mango, grey grade + vignette, "POPULATION: 1 CAT 😿", "anyone? 🥺" bubble, "FRIENDS: ZERO 💔", sad piano.
4.0 record scratch + flash, "But every time you follow," 3 EXAMPLE @you houses pop with "+1 🐱".
7.8-10.6 crane up while the town fills to 1,000 (counter rolls, "THE DREAM"), fanfare.
10.6-13.4 counter rewinds to 1, "COMMENT YOUR NAME 👇 / I'll build YOUR house next!", EXAMPLE name chips, "Your name here?" sign.
13.4-14.8 "Because right now..." back to grey Mango; last frame = frame 0, so it loops into "Mango is the only cat in this whole town."

Why: 2026 TikTok ranks watch time, completion and rewatches first, then shares/comments. Short (under 15 s), tension on frame 0,
a change every 1-3 s, payoff before 15 s, loop, comment bait with a personal stake, and the part 2 = video replies to name comments.

Build (same free pipeline as day-1-v4): work dir with catcity.html, p_1000.json, node_modules (three@0.170.0, @fontsource/nunito, playwright),
`python3 -m http.server 8772`; in v/: `voice_gen.py in.json` (copy of lines.json), then `mk.py v`, `text.py v`, `audio.py v`,
`node render.js v range 0 444` (split in 4), ffmpeg mux. Reviewer: cut 1 6/10, cut 2 7.5/10 READY after 2 small fixes (done in cut 3).
