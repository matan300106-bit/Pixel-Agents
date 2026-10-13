# Day 7: wil.son's Giant Cat Box + 1 week (32.0 s)

Matan (Oct 13): "Day 7, wil.son: A giant box for all the cats. Celebrating 1 week! 0 following, 321 followers, 562 likes". Same style as Day 6 (no counting animation; the real numbers appear once on the 1 week card).
Story: hook on the finished box full of cats -> wil.son's comment (no like count) -> Mango looks at us: "Mango loves boxes. So... let's go big!" (callback: on Day 6 he picked the box over the toy) -> the giant box drops (THUD, dust), then flaps open, cat doors, peek holes, scratch ramp, party flags + "1 WEEK!" banner (one per word, progress bar) -> "All the cats... get in!" (cats run in through the doors, heads pop out of every hole and over the rim, the box shakes) -> wide: "One week ago, this town had one cat. Today, 321 followers. Thank you!" + confetti -> record scratch: "Wait... where's Mango?" -> Mango sits in his own small box in front of the giant one: "Mango... you have a giant box!" -> he turns: "Meow!" -> "follow = your house · top comment = we build it" over a "Day 8: your idea?" lot -> loops to the hook.

Engine (catcity.html): landmark kind `box` (parts: giant box on a round lot, flaps, arched cat doors, round peek holes, scratch ramp, party flags + "1 WEEK!" banner; Mango's small box; cat heads in the holes, cats on the rim, two in the front doors); `newBuild.openAt` = cats run in and pop out; `EP.box = { lookAt: [t0, t1], boxAt, turnAt }`; `boxFrame()` runs it each frame. `EP.confettiAt: [t]` = extra confetti bursts. A finished `box` landmark (website) has every cat in place and Mango in his small box. Fish, arcade, art studio, pizza, toy = spots 0-4; box = spot 5; the Day 8 lot = spot 6.

Build (server on :8772 in social/cat-town with catcity.html + node_modules three@0.170.0, @fontsource/nunito, playwright; work dir `d7` there; Kokoro files in /tmp/tts):
1. in d7: `python3 ../episodes/day-7-box/voice_gen.py ../episodes/day-7-box/lines_in.json 1.15`
2. `python3 ../episodes/day-7-box/mk.py .`, `python3 ../episodes/day-7-box/text.py .`, `python3 ../episodes/day-7-box/audio.py .`
3. from social/cat-town: `node episodes/day-7-box/render.js d7 range 0 960` (split in 4), ffmpeg mux (libx264 crf 18 + aac 192k).
Final: project files `cat-town/day-7/`. Not posted; Matan approves first.
Website: theme copy 189188800724 renamed "PETME2 — Cat Town Day 7 giant box (+toy)" (themes are 20/20, so the Day 6 copy got the box too), 6 builds, counts 321/562. Not published.
