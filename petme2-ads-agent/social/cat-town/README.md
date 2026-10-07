# PETME2 Cat Town – Instagram Reels series

**Rules (said in every episode):**
1. Every new follower = 1 new cat + 1 new house in the town.
2. The most-liked comment builds anything it wants.

The town is saved in `town-state.json` and keeps growing every day.

## Daily steps (Claude does all of them)
1. Owner tells Claude: new followers since last episode + the most-liked comment (+ who wrote it).
   (If the PETME2 Instagram Business account is connected, Claude reads these itself.)
2. `python3 build_episode.py --day N --new-followers X --comment "..." --by "@user" --print-script` → voice lines.
3. Voice (edge-tts, en-US-AvaMultilingualNeural, rate +6%) made on the remote workbench, with **exact word timings** → `episodes/day-N/voice-timings.json`.
4. `python3 build_episode.py --day N --new-followers X --comment "..." --by "@user" --timings episodes/day-N/voice-timings.json`
   → `episode.json` (houses, cats, the build, word subtitles) and updates the town.
5. Serve this folder (`npx http-server -p 8766`), `node render_town.js 30`, ffmpeg → `episodes/day-N/silent.mp4`.
6. Remote mix: voice + original music (made in code, no copyright) + pop sounds on each build → final MP4 (Shopify Files, private) for the owner to watch.
Nothing is posted until the owner says so.

## What every episode has (built to go viral)
- Hook in the first second ("I'm building a town for cats... and you decide what we build").
- Word-by-word subtitles: big bold words, the word being said turns yellow (most people watch muted).
- Live counters (cats / houses), "+X followers" badge, "Top comment by @user" badge.
- Things pop in exactly on the spoken word (house on "house", fountain on "fresh water fountain").
- End card with the 2 rules + "Follow & comment @petme2".

## Builds the town knows
fountain, café, market, cat tree, statue, pool, tower, vet, park — anything else becomes a big building with the request written on a sign.

## Episode 1
Voice: "I'm building a town for cats... and you decide what we build." / "Every new follower adds a new cat and a house. Meet Mango, our very first resident!" / "And every day, the most liked comment builds anything it wants. Mango was thirsty, so day one: a fresh water fountain!" / "Follow to move your cat in, and comment what we build tomorrow!"
Caption: see below. Cover: `episodes/day-1/cover.png`.

**Caption (Day 1):**
Every follower = a new cat + a house in our town 🐱🏠 The most-liked comment builds ANYTHING. What should Mango get next? 👇
#cattown #cats #catsofinstagram #catlover #petme2 #cutecats #3danimation #buildingtogether
