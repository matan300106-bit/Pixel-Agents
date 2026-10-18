# Day 2 extra: "Every follower gets a house" (17 s)

Matan (Oct 7): make sure every follower brings a new house, then another video. Separate from the Day 2 fish cut.
Check: engine gives house k to follower k (houseLots unique, `slice(0, F)`), the website shows exactly n houses for n residents (viewer tOf), followers.csv has 128 unique handles = 128 houses.
Story: Mango alone, 0 houses → house #1 @idkhima and #2 @ugvtsvi pop with name tags → whip to #3 @sillyy72 → the other houses pop fast while the camera pulls back, counter to 128 → "we did not expect that" → "Now Mango is not alone anymore" → "The only thing missing in this town... is you!" → loops to the hook.

Engine: `EP.appear` (exact pop time per new house), `EP.residents` (name tags). Overlay = day-2-fish overlay + `houses` counter (counts popped houses) and "follower #N moved in" tags; captions at 1500 px.
Final: project files `cat-town/day-2-houses/`. Not posted; Matan approves first.

Build (same tools as day-2-fish, server on :8772, work dir `houses` in the server root):
1. `python3 voice_gen.py lines_in.json` in the work dir
2. `python3 mk.py houses`, `python3 text.py houses`
3. `node render.js houses range 0 510` (split in 3), `python3 audio.py .` in the work dir, ffmpeg mux (libx264 crf 18 + aac 192k).
