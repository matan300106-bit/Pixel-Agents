# Day 8: The Dogs Are Coming (Part 1) (40.0 s)

Matan (Oct 14): "I want day 8 to be special... dogs are invading town... all the cats are starting to gather up and prepare for a fight... like a mini movie. Show army of dogs walking, coming into our cat town. Dramatic... episode 9 will continue, like episodes."
A story episode (no top comment build). Movie trailer narrator (Kokoro bm_george), Mango's battle cry (af_heart + echo), cinematic bars, ends on a cliffhanger.

Story: hook (the dog general + army march at us, "DAY 8: THE DOGS ARE COMING") -> "Cat Town was peaceful." (town from above) -> "Until today." (Mango, the ground shakes) -> over Mango's shoulder, slow zoom: the dog army on the horizon (bone flags, dust) -> tracking shot: 150 dogs marching in step -> "So Mango called every cat in town." MEOOOW! -> every cat runs out of town and lines up (321 cats = 321 followers) -> getting ready bar: box wall, yarn cannons, helmets on (pots and bowls), flags up -> "321 cats." (behind the cats) / "150 dogs." (behind the dogs) -> the general steps forward, Mango too -> nose to nose, heartbeat, the general opens his mouth... FREEZE, sepia, "TO BE CONTINUED" arrow -> end card: "Day 9: what happens next? Top comment decides. Follow = 1 more cat in the army".

Engine (catcity.html): `EP.war` (see the comment above `WAR`): a battlefield frame `ang`/`r` (west of town, trees cleared), dog soldiers (instanced body/face/helmet + 4 swinging legs, all in step), 4 bone banners, dust, the dog general (spiked helmet, red cape, angry brows, jaw opens at `jawAt`), Mango with a red cape (MEOW at `meowAt`, walks out at `mangoAt` to `meetZ`), 321 cats running in at `gatherAt` with helmets at `helmetAt`, box wall `wallAt`, yarn cannons `cannonAt`, cat flags `flagAt`, `dogs` front row keyframes, `dusk` keyframes, camera `shake`. Shots can now zoom: `shots[].fov = [from, to]`.

Build (server on :8772 in social/cat-town with catcity.html + node_modules three@0.170.0, @fontsource/nunito, playwright 1.56; work dir `d8`; Kokoro files in /tmp/tts):
1. in d8: `python3 ../episodes/day-8-dogs/voice_gen.py ../episodes/day-8-dogs/lines_in.json`
2. `python3 ../episodes/day-8-dogs/mk.py .`, `python3 ../episodes/day-8-dogs/text.py .`, `python3 ../episodes/day-8-dogs/audio.py .`
3. from social/cat-town: `node episodes/day-8-dogs/render.js d8 range 0 1200` (split in 4), ffmpeg mux (libx264 crf 18 + aac 192k).
Final: project files `cat-town/day-8/`. Not posted; Matan approves first. No website change (story episode).

Episode 9 hook: the general's mouth is open, nobody knows what he says. Ideas for Part 2 (pick from the top comment): a battle with yarn cannons; the dogs just want to play / be friends; the dogs are hungry and the cats share the Fish Supermarket; the general says "...meow?"; the dogs ask to move into Cat Town (Dog Street).
