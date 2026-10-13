# Day 5: MrFireman's Giant Pizza (every topping) (30.6 s)

Matan (Oct 11): Day 5. Top comment by MrFireman: "ADD A GIANT SLICE OF PIZZA WITH EVERY SINGLE PIECE OF TOPPING ON IT". Fun, no counting (no follower/like numbers). Script approved ("Go ahead"), project files `cat-town/day-5/day5-script.md`.
Story: hook on the finished slice -> MrFireman's comment (no like count) -> Mango looks at us: "Every. Single. Topping." -> the crust drops (BOOM, dust, cats hop), sauce, cheese, then one topping per word (pepperoni, mushrooms, olives, peppers, onions, corn, bacon, "everything": tomato, jalapeño, basil) -> "And... pineapple." (music stops, record scratch, one cat walks off) -> a fish on top ("it is a cat town"), cats climb on, one naps in the cheese -> wide shot -> Mango bites the tip, cheese string -> turns with cheese on his face: "Meow!" -> "follow = your house · top comment = we build it" over a "Day 6: your idea?" lot -> loops to the slice.

Engine (catcity.html): landmark kind `pizza` (parts: stand + plate, crust, sauce, cheese + drips, then one part per topping, pineapple (with one giant ring), fish); `newBuild.openAt` = cats climb on; `EP.pizza = { lookAt: [t0, t1], walkAt, biteAt, turnAt }`. Also new: `EP.lotUntil` (lot sign stays until the crust lands), `EP.idea = { spot, sign }` (extra empty lot with a sign), a finished `artstudio` landmark now shows the statue + painters. Fish supermarket, arcade, art studio = spots 0, 1, 2; pizza = spot 3; the Day 6 lot = spot 4.

Build (server on :8772 in social/cat-town with catcity.html + node_modules three@0.170.0, @fontsource/nunito, playwright; work dir `d5` there; Kokoro files in /tmp/tts):
1. `python3 voice_gen.py lines_in.json 1.15` in the work dir
2. `python3 mk.py d5`, `python3 text.py d5` (put `[[0.1,50.3,-3.14],[-44.7,-25.7,1.05],[44.6,-25.8,-1.05]]` in d5/spots.json)
3. `node render.js d5 range 0 918` (split in 4), `python3 audio.py d5`, ffmpeg mux (libx264 crf 18 + aac 192k).
Final: project files `cat-town/day-5/`. Not posted; Matan approves first.
