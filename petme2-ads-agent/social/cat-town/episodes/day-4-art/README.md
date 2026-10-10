# Day 4: 218 cats have no home + Tilly's Art Studio (33.8 s)

Matan (Oct 10): Day 4. 261 followers, 479 likes: "just mention how many cats don't have a house" (479 - 261 = 218). Top comment by Tilly: "you should build an art studio and the cats at the studio build mango a statue ♡". Script approved by Matan ("do it"), project files `cat-town/day-4/day4-script.md`.
Story: hook on the homeless crowd ("No home yet") -> 261 houses roll up -> 479 cats roll up -> 479 - 261 = 218 -> one stray waits alone on an empty lot -> Tilly's comment (no like count) -> the Art Studio builds piece by piece, the homeless cats run in and paint Mango -> a gold Mango statue rises, Mango hops -> a house pops on the lone stray's lot, the cat runs in (houses 262, no home 217) -> "Can we get every cat a home?" -> loops to the crowd.

Engine (catcity.html): landmark kind `artstudio` (parts: yard, studio + window, roof + giant palette, easels with Mango paintings, pedestal; `newBuild.openAt` = painter cats run in and sit; `EP.statueAt` = gold Mango statue rises); `EP.lone = { spot, at, houseAt, runAt, sign }` (one stray on an empty lot, a house pops, the cat runs in; `window.__lone`). The Fish Supermarket and Cat Arcade are normal landmarks (spots 0, 1), the studio is the new build on spot 2, the crowd on spot 3, the lone stray on spot 4.

Build (server on :8772 with catcity.html + node_modules three@0.170.0, @fontsource/nunito, playwright; work dir `d4` in the server root; Kokoro files in /tmp/tts):
1. `python3 voice_gen.py lines_in.json 1.22` in the work dir
2. `python3 mk.py d4`, `python3 text.py d4`
3. `node render.js d4 range 0 1014` (split in 4), `python3 audio.py d4`, ffmpeg mux (libx264 crf 18 + aac 192k).
Final: project files `cat-town/day-4/`. Not posted; Matan approves first.
