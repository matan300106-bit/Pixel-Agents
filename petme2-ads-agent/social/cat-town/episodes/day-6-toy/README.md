# Day 6: bean's Huge Cat Toy Statue (29.0 s)

Matan (Oct 13): "lets build day 6". Top comment by ‿ ◟🍏 beαn 🐾˳ ꒱: "CAN WE GET A HUGE CAT TOY STATUE FOR THE CATS TO PLAY WITH". Same style as Day 5 (no counting). The older night idea (`cat-town/day-1-lights/day6-night-script.md`) is not used.
Story: hook on the finished toy -> bean's comment (no like count) -> Mango looks at us: "As big as a building" -> a cardboard box drops (THUD, dust), then pedestal, giant yarn ball, feather wand, toy mouse on a string, jingle bells (one per word, progress bar) -> "Cats... go play!" (cats run in, two jump at the swinging mouse, two climb the yarn ball) -> wide shot -> "Well... almost every cat." (music stops, record scratch) Mango walks past the toy and hops into the box it came in -> "Mango, really? The box?" -> he turns: "Meow!" -> "follow = your house · top comment = we build it" over a "Day 7: your idea?" lot -> loops to the toy.

Engine (catcity.html): landmark kind `toy` (parts: box, lot + pedestal + "FOR THE CATS" plaque, yarn ball + loose strand, feather wand, mouse on a string, bells); `newBuild.openAt` = cats run in and play; `EP.toy = { lookAt: [t0, t1], boxAt, turnAt }`; `toyFrame()` runs the play each frame. A finished `toy` landmark (website) has everyone in place, Mango in the box, the mouse swinging. Fish, arcade, art studio, pizza = spots 0-3; toy = spot 4; the Day 7 lot = spot 5.

Build (server on :8772 in social/cat-town with catcity.html + node_modules three@0.170.0, @fontsource/nunito, playwright; work dir `d6` there; Kokoro files in /tmp/tts):
1. in d6: `python3 ../episodes/day-6-toy/voice_gen.py ../episodes/day-6-toy/lines_in.json 1.15`
2. `python3 ../episodes/day-6-toy/mk.py .`, `python3 ../episodes/day-6-toy/text.py .`, `python3 ../episodes/day-6-toy/audio.py .`
3. from social/cat-town: `node episodes/day-6-toy/render.js d6 range 0 870` (split in 4), ffmpeg mux (libx264 crf 18 + aac 192k).
Final: project files `cat-town/day-6/`. Not posted; Matan approves first.
Website: theme copy 189188800724 "PETME2 — Cat Town Day 6 toy statue" (duplicate of live 188939337940), 5 builds. Not published.
