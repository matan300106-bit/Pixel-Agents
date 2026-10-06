# PETME2 Cat Town – Instagram Reels series

Idea (from @telbatata's "city grows every day" reels): a tiny low-poly island where cats live. Every episode builds ONE thing that followers asked for in the comments. PETME2 products show up naturally (fountain plaza, feeding hall).

## Episode 1 (ready): `cat-town-day-1.mp4` (1080x1920, 12.5 s, no sound)
Empty island → first cat house pops up, orange cat walks in → fresh-water fountain appears, grey cat runs to drink → end card "What should the cats build next? Comment below & follow @petme2".

**Caption:**
Day 1 of building a town for cats 🐾 The first cat moved in and we built a fresh water fountain 💧
What should we build next? Comment 👇 The most liked idea gets built tomorrow! Follow so you don't miss it.
#cattown #cats #catsofinstagram #catlover #petme2 #cutecats #catlife #3danimation #buildingtheworld

**Posting tips:**
- In Instagram, add a trending song (Reels → Add audio). Trending audio gives more reach than the silent file.
- Cover: `cover-day-1.png`.
- Pin a comment: "Vote here 👇 cat café ☕ / fish market 🐟 / cat tree tower 🌳".
- Post at the same time daily (e.g. 6–8 pm US Eastern).

## Next episodes (build what comments ask; ideas if quiet)
- Day 2: Cat café · Day 3: "Feeding Hall" with the PETME2 dual feeder · Day 4: cat tree tower · Day 5: fish market · Day 6: a second house + new cat.

## How it's made (no AI video tools)
`scene.html` is a Three.js scene; `render.js` (Playwright) renders it frame by frame; ffmpeg makes the MP4.
To render: in a folder with `npm i three@0.170.0 @fontsource/nunito@5`, serve it (`npx http-server -p 8765`), run `node render.js 30`, then
`ffmpeg -framerate 30 -i frames/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4`.
