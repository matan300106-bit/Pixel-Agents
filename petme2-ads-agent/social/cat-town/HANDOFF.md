# Cat Town — handoff (read this first in a new session)

Owner: PETME2 (cat/dog fountains + feeders). Reply in simple, short English. Owner rule: "always do whatever is needed, don't ask me" — only hand the owner what no tool can do (publishing a theme, logins).

## What it is
An Instagram series + interactive web page: a low-poly 3D **city built for cats**.
- Every new follower = 1 cat + their own little house (tap a house → their Instagram name).
- Most-liked comment builds anything (cat version). No rude/political builds.
- Plan and decisions: `CITY_PLAN.md`. Ideas: `design-ideas.md`, `design-review.md`. Build log: `build-notes.md`. QA: `qa-report.md`.

## Files (all in `petme2-ads-agent/social/cat-town/`)
| File | What |
|---|---|
| `catcity.html` | The engine (Three.js 0.170). Round street plan, cat houses (cat-face / box / pod), gardens, walking cats, cat-taxi strollers, Mango's Water Bar fountain, Big Mochi, red-dot lighthouse, fish balloons, nap bus stop, circle traps, landmarks, growth mode, video UI. `window.renderFrame(t, anim)`. |
| `viewer_loop.js` | Web-page controls: orbit, slider, play growth, postcard, tap house/building info card, phone LITE mode (no shadows/AA, 30 fps, pause off-screen). Arrows / double-tap fly-to / game feel: being added (see "In progress"). |
| `build_viewer.py` | Builds `viewer.html` (interactive page, example capped at 1,000 followers, example handles "demo.*"). |
| `build_shopify.py` | Ports `viewer.html` → `../../shopify-theme-tech/sections/pm2-cat-town.liquid` + `assets/pm2-cat-city.js` (ids prefixed `pcc-`, CSS scoped `.pm2-city`, three.js via jsdelivr `+esm`). |
| `previews/` | Still images (`final_*.jpg`) + camera configs (`p_*.json`, `q_*.json`). |
| `town.html`, `town2.html`, `city.html`, `build_episode.py`, `render_town.js` | Older engines / Day-1 video pipeline (kept for history). |

## How to render / test (cloud container)
- Static server on port 8772 serving a scratch folder that has `node_modules` (three, @fontsource/nunito) + `render_still2.js`, `vtest.js`, `taptest.js`. If the scratch folder is gone: `npm i three@0.170.0 @fontsource/nunito playwright` in a new folder, copy `catcity.html` there, `python3 -m http.server 8772`, and write a tiny playwright script that opens `catcity.html?ep=<config>.json`, waits for `window.ready`, calls `window.renderFrame(3)` and screenshots (1080×1920; Chromium flags `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`).
- Web page test: build viewer, route `https://cdn.jsdelivr.net/npm/three@0.170.0/**` to local `node_modules/three/...` in playwright.

## Where it lives (links)
- Private interactive link (Claude artifact): https://claude.ai/artifact/1Kt6gGXdFVUKNLovgrmMgw (republish from the same file path in the session that created it; from a new session pass this URL as `url`).
- Picture page: https://claude.ai/artifact/J5eZctn7UsJmcoA4QQBSMF
- Shopify page: petme2.com/pages/cat-town (page template `page.cat-town`, section `pm2-cat-town`).
  - LIVE theme now (owner published it 2026-10-06): `PETME2 — Cat Town fountain + feeder + controls` (188909420756).
  - Preview theme: `PETME2 — Cat Town figure 8 food & drink stops` (188910403796) → fountain circle + feeder circle side by side, many more cats, Mango between. Preview: https://petme2.com/pages/cat-town?preview_theme_id=188910403796
  - Theme writes only to UNPUBLISHED copies (live theme writes are blocked). If the owner publishes the copy, duplicate the live theme again and write to the new copy. Upload big files via `stagedUploadsCreate` (curl POST) + `themeFilesUpsert` with body type URL, then verify `checksumMd5`. Log every change in `../../changes-log.csv`.

## Day-1 video pipeline (when real data arrives)
Voice: edge-tts `en-US-AvaMultilingualNeural` rate +6% with WordBoundary timings (Composio remote workbench); original synth music + pop SFX; mix with ffmpeg sidechain; render frames headless → H.264; deliver via Shopify Files link. Needs real data from the owner: new follower count, top comments with likes, Instagram handle (@petme2 unconfirmed). Do not post anything without owner approval.

## Status (2026-10-06 night, Cat Town session in the "Cat Town" project)
Live: real fountain + feeder + controls. Preview 188910403796: figure 8 "food & drink stops" (see `build-notes.md`, "Update 2026-10-06 (night)"). Waiting for the owner to check and publish.
Note: this cloud container can't open petme2.com (proxy blocks it), so live-page checks are done locally with `viewer.html` + Playwright.

## Open polish items
Phone: Mochi starts cut at the edge; Day-1 web view far; episode shots don't visit Mochi/beach; "Find your house" search waits for real handles (no demo names on a public page except clearly-labelled examples).
