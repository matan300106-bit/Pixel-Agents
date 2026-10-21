# Day 10: The Dogs Are Coming, Part 3 "The Giant" (51.6 s)

Matan (Oct 21): "Lets do a day 10". Story episode, follows the plan in project files cat-town/day-9/story-plan.md. No top comment build.
Opens on Day 9's frozen sepia frame (the giant's red eyes, TO BE CONTINUED arrow + a red PART 3 stamp), colour snaps back.

Story: the giant leans down, his eyes glow ("The giant... saw him.") -> spy: "Uh oh." -> "Run!" -> the dog camp wakes up and barks, the dogs chase -> "Faster!" ->
"And... jump!" the spy leaps the box wall in slow motion -> spy: "Mango! They have... a GIANT!" -> the cats panic (hop + spin, meows) ->
Mango: "If they have a giant... then we build our OWN giant!" -> 321 cats climb on each other, bottom first ("1 follower = 1 cat", "every follow = BIGGER") ->
MEGA MANGO (Mango rides on his head) -> the clock runs out, the sun comes up -> the giant walks out of the camp, BOOM BOOM -> Mega Mango stands up -> "MEOOOW!" ->
FREEZE "TO BE CONTINUED" -> end card "Day 11: who wins? Comment MANGO or GIANT / The battle starts / Follow = 1 more cat in Mega Mango".
Voices: narrator bm_george, Mango af_heart, the spy am_puck, Mega Mango = af_heart pitched way down + echo (voice_gen.py "mega").

Engine (catcity.html, `EP.war` extras, comment "Day 10 (Part 3)"): `wakeAt`, `bark` [t0, t1] (head jerks), `spyLook` as [[t0, t1], ...], `spyJump` [t0, t1, h], `mangoZ`, `panic` [t0, t1], `eyesOff`,
`giant.walk` [[t, z]] (legs swing), `giant.lean`, `giant.glow`, `mega` {at, dur, x, z, s, cs, fullAt, mangoTop, standAt, roar}: the cats fly to points sampled on Mango's sitting shape (face kept clear).
The spy now keeps facing the way he came when he stands still, from any start frame. Day 9 times are shifted by -43.3 so t = 0 is Day 9's freeze.

Build (server on :8772 in social/cat-town with catcity.html + node_modules three@0.170.0, @fontsource/nunito, playwright 1.56; work dir `d10`; Kokoro files in /tmp/tts):
1. in d10: `python3 ../episodes/day-10-dogs-part3/voice_gen.py ../episodes/day-10-dogs-part3/lines_in.json`
2. `python3 ../episodes/day-10-dogs-part3/mk.py .`, `python3 ../episodes/day-10-dogs-part3/text.py .`, `python3 ../episodes/day-10-dogs-part3/audio.py .`
3. from social/cat-town: `node episodes/day-10-dogs-part3/render.js d10 range 0 1548` (split in 4), ffmpeg mux (libx264 crf 18 + aac 192k).
Final: project files `cat-town/day-10/`. Not posted; Matan approves first. No website change.
