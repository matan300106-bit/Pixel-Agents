# Day 3: the Cat Arcade (31 s)

Matan (Oct 8): Day 3. 253 followers, 467 likes. Top comment by francisco12321: "can u show me next time ? and make a cat arcade!" Script approved by Matan (project files `cat-town/day-3-arcade/day3-script.md`).
Story: hook on the glowing arcade → Francisco's comment (no like count) → his lot, "For @francisco12321" → split screen Day 1 (Mango alone) vs today (253 houses, 467 cats roll up, strays pop) → more cats than houses (crowd under "No home yet") → evening falls, the arcade builds piece by piece (floor, walls, roof + cat head, claw machine, game cabinets, neon) → lights on, cats run in, Mango wins a fish at the claw machine → follow = 1 cat house, top comment = we build it → Day 4 lot → loops to the hook.

Engine (catcity.html): landmark kind `arcade`; `EP.newBuild.partsAt` (time per build piece), `lightsAt` (neon flickers on + point lights), `openAt` (cats run in); `EP.clawAt` (claw grabs the fish, Mango hops); `EP.dusk {from,to}` (day → evening sky, fog, sun); `window.__spots`.
Render: frames 0-1 s replay engine time 31.2-32.2 (seamless loop); during 9.0-14.5 s the top half is a Day 1 frame from e0.json (second page).

Build (server on :8772 with catcity.html + node_modules three@0.170.0, @fontsource/nunito, playwright; work dir `d3` in the server root; Kokoro files in /tmp/tts):
1. `python3 voice_gen.py lines_in.json` in the work dir
2. `python3 mk.py d3`, `python3 text.py d3`
3. `node render.js d3 range 0 936` (split in 4), `python3 audio.py d3`, ffmpeg mux (libx264 crf 18 + aac 192k).
Final: project files `cat-town/day-3-arcade/`. Not posted; Matan approves first.
