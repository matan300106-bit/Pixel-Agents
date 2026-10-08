# Day 2: likes = cats, follows = houses (45.5 s)

Matan (Oct 7): every like brings a cat, every follower a house; show we have more likes than followers. His approved Day 2 script + this idea; 194 likes (his number), 128 followers, so 66 cats with no house.
Engine: `EP.strays = { n, at, near }` adds cats with no house of their own (sitting on roofs, nearest to `near` first, and on streets). Overlay: `catsCounter` shows 🏠 houses and 🐱 cats (houses + strays, Mango not counted).
Final: project files `cat-town/day-2-likes/`. Not posted. Build: same steps as ../day-2-script (work dir `likes`, `node render.js likes range 0 1365`).
