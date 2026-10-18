# Day 9: The Dogs Are Coming, Part 2 "The Spy" (48.5 s)

Matan (Oct 18): "make a day 9, continue with the dogs. lets build tension over here. i want couple days for it to go. Feel free to be creative."
Story episode, no top comment build. Opens on Day 8's frozen sepia frame (TO BE CONTINUED arrow + a red PART 2 stamp), colour snaps back.

Story: the general speaks ("Cats of Cat Town... Give us... your fountain.") -> the PETME2 fountain in town ("the heart of Cat Town") -> Mango: "NEVER!" ->
"Then at sunrise... we attack." -> the dogs howl -> they walk back, night falls, a clock starts (ATTACK IN 10:00:00, runs down) -> dog camp fires across the field, "nobody slept" ->
321 pairs of glowing cat eyes -> Mango sends a spy cat (grey, black mask) "Go. Be careful." -> past the sleeping dogs -> past the camp fires -> he stops, looks up:
a GIANT dog against the moon, red eyes open -> FREEZE "TO BE CONTINUED" -> end card "Day 10: what did the spy see? Guess in the comments / The dogs attack at sunrise / Follow = 1 more cat in the army".
Voices: narrator bm_george, Mango af_heart, the dog general am_onyx pitched down (voice_gen.py). Next parts: project files cat-town/day-9/story-plan.md.

Engine (catcity.html, `EP.war` extras, see the comment above `GLOW`): `talk` (general's jaw), `mangoTalk`, `howl`, `genBack`, `mangoBack`, `sleepAt` (dogs lie down), `eyesAt` (glowing cat eyes),
`campAt` (tents + fires with point lights), `spy` path + `spyLook`, `giant` {at, x, z, s, eyesAt} (dark copy of the general), `moon`; `duskAt` k 1..2 = evening -> night (moon + stars), `shots[].lin` = constant-speed shot.
Day 8 times are shifted by -34 so t = 0 is Day 8's freeze frame.

Build (server on :8772 in social/cat-town with catcity.html + node_modules three@0.170.0, @fontsource/nunito, playwright 1.56; work dir `d9`; Kokoro files in /tmp/tts):
1. in d9: `python3 ../episodes/day-9-dogs-part2/voice_gen.py ../episodes/day-9-dogs-part2/lines_in.json`
2. `python3 ../episodes/day-9-dogs-part2/mk.py .`, `python3 ../episodes/day-9-dogs-part2/text.py .`, `python3 ../episodes/day-9-dogs-part2/audio.py .`
3. from social/cat-town: `node episodes/day-9-dogs-part2/render.js d9 range 0 1455` (split in 4), ffmpeg mux (libx264 crf 18 + aac 192k).
Final: project files `cat-town/day-9/`. Not posted; Matan approves first. No website change.
