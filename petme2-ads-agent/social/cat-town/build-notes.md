# Cat Town: build notes (builder, 2026-10-06)

Source of truth for this build: `design-review.md` (BUILD LIST, section 3). Engine: `catcity.html`. Web page: `viewer.html` (made by `python3 build_viewer.py`).

## What I built, and where

All engine code is in `catcity.html`. Search for the comment in the "Where" column.

| # | Item | Status | Where (comment in code) | Unlocks at |
|---|---|---|---|---|
| — | Shared helpers (`unlockT`, `popK`, `UNLOCK`, `polar`, `yawTo`, `paint`, `putCat`) | DONE | `shared helpers for the extras` | — |
| — | Pose kit: `CAT_SIT`, `CAT_LOAF`, `CAT_DRINK`, `CAT_BELLY` (800 slots each) + `WALK` (32 slots) | DONE | `pose kit` | — |
| 1 | Mango's Water Bar: white trough wall, water ring, blue lip, 36 droplets in 6 arcs, ripples, 17 drinking spots + Mango as host, in/out lanes (r 10.5 / r 9.3, always counter-clockwise), deadpan glance (every 3rd spot), dome breathing, `EP.fountainWave` | DONE | `Build 1: Mango's Water Bar` + `updateExtras` | Mango + ring: Day 1. Spot m: follower rank 1..17 (fill order 1, 17, 2, 16 …) |
| 2 | Circle traps: hero row of 4 dark circles on the plaza (3 sitters + the late 4th cat on a 20 s loop) and white garden circles (15% of garden trees) | DONE | `Build 2: cat circle traps` (gardens) + `Build 2 (hero row)` | Tape 20, cats 20-22, walker 23. Garden circles appear with their district |
| 3 | If it fits, I sits: hero box on the plaza (grey 1.6 loaf, weight shift every 9 s) + garden boxes (next 15% of garden trees) | DONE | `Build 3` (gardens) + `Build 3 (hero box)` | Hero box 5 |
| 4 | Big Mochi: sleeping ginger mountain cat (stripes, head, ears, closed eyes, nose, tail, paw), breathing, ear flick, 3 rising Z letters; trees within 75 cleared | DONE | `Build 4: Big Mochi` | Rises over 2 time units, finishing at 1,000 |
| 5 | Red Dot Beach: lighthouse (white/salmon), laser that tracks the dot, beam, red dot + halo, 5 chasers (pounce, butt wiggle), 1 belly-up quitter; palms cleared | DONE | `Build 5: Red Dot Beach` | 500 |
| 6 | Fish balloons: 5 balloons (2 draw calls), striped shell, eyes, tail fin, basket with 2 cats, moving shadows | DONE | `Build 6: fish balloons` | Balloon k at 500 × (k+1) |
| 7 | Bus stop "NEXT NAP / 5 MIN": shelter, own 2-line sign canvas, 2 loaf sleepers + 1 belly-up (breathing, roll) | DONE | `Build 7: one hero bus stop` | Shelter 10, sleepers 10-12 |
| 8 | Save postcard (web page only) | DONE | `viewer.html` shell (button + `.pc` overlay) and `viewer_loop.js` | — |
| fix | `textSign()` shrinks the font (104 → min 56 px) instead of cutting letters | DONE | `function textSign` | — |
| fix | `await document.fonts.load('900 100px Nunito')` (and 800) before any sign canvas is drawn | DONE | top of the module script | — |
| fix | Plaza disc lowered to top y .12 (it z-fought with the avenue road at y .14; this showed in the fountain close-ups) | DONE (extra) | `plaza.position.y = .05` | — |

Every item is a pure function of `t` / `anim` (no `Math.random()` in `renderFrame`). Two renders of the same `t` gave identical PNGs (same md5).

The old Mango road patrol is gone (`catMesh` slot 0 = ZERO). The City Hall Mango statue stays.

## Postcard (Build 8)

- The button "Save postcard" is in the first dock row, next to "Play growth". The page renders the current view, then draws a 1080×1350 card: the view is cover-cropped into the top 1080×1220, with a white footer reading "Cat Town · N cats · Day D" (900 40px Nunito, ink) and "@petme2" (800 30px, brand blue).
- **Deviation (from the manager's brief, not the review):** the review said share or download. The page sandbox blocks scripted downloads, so the card opens in an overlay as an `<img>` (data URL). The visitor long-presses or right-clicks it to save. The overlay has a Close button (focus moves to it; Esc and clicking the backdrop also close it). It uses the page CSS tokens (`--panel`, `--ink`, `--muted`, `--sky`).
- `build_viewer.py` no longer adds its own `fonts.load`, because the engine now has one.
- Phone dock (≤520 px): row buttons got slightly smaller padding, so "Followers · Save postcard · Play growth" fits on one row at 390 px.
- Tested (Playwright, SwiftShader) at 390×844 and 1280×800. The image is 1080×1350, the overlay opens, Esc closes it. No page errors.

## Deviations from the review (and why)

1. **Big Mochi angle 3.45 → 3.7** (`MOCHI_A`). At 3.45, Mochi was cut off at the left edge of `p_5000` (x ≈ 23 px). At 3.7 it is fully inside both `p_1000` (x ≈ 480–860, y ≈ 380–500) and `p_5000` (x ≈ 230–430, y ≈ 500–560). It sits a bit higher on screen than the review's 550–720 estimate, but still below the counter pill. Tree clearing uses the same constant. For the 1,000-followers episode shot, look at `(cos 3.7·500, 20, sin 3.7·500)` = (−424.9, 20, −263.6), not (−476, 20, −152).
2. **Balloon placement.** The review's `ANG = [2.25 … 4.95]` with r = 0.7·CR spreads the balloons around the whole city. The portrait camera only sees about 24° across, so `p_5000` showed 2 balloons and `p_1000` showed 1. I picked new spots with a projection check against `p_1000`, `p_5000` and both opening-shot cameras: `ANG = [4.1, 3.0, 1.0, 0.7, 1.8]`, radius factor `RF = [.6, .35, .5, .35, .35]` (× CR, clamped 60–240, + 12·sin 2.1k). Result: `p_1000` shows 2, `p_5000` shows all 5. None covers the fountain or Mochi in those frames, and none is in the opening shot near the fountain. Height, drift, wag and unlocks are as specified.
3. **Ripples use `RingGeometry(.8, 1)`, not a `Torus(1, .035)`.** A torus scaled to .15–.7 has a tube about .01 wide, which is invisible even in the close-up. A flat ring scaled in x/z keeps a visible band.
4. **`CAT_DRINK` tail rx +1.2, not −1.2.** With −1.2 the tail hangs down at the back. +1.2 gives the "tail up = happy cat" the design asked for.
5. **Tiny-box flaps on the box's long sides, drooping outward (rz ±.5).** With the spec (flaps at z ±.38), the oversized loaf covered both flaps completely. The loaf also sits a little higher (sunk .04, not .1), and the hero box is turned to a profile view (yaw +1.2), so the "cat way bigger than box" reads from the `q_box` camera.
6. **Balloon tail** is a flat fin (cone with its tip toward the body, flattened in x), not a cone pointing −z (that looked like a second nose). **Basket cats** sit at y −10.65, not −11.2: at −11.2 only ear tips showed above the rim.
7. **Big Mochi tail torus** is a bit smaller and higher (r 43, tube 5, x-scale 1.26, y 7, arc 1.05π instead of 46/6/1.3/5/1.1π). The bigger ring read as a plate rim around the cat.
8. **Palms:** besides the ones within 10 of the lighthouse, palms in the dot's play area (z 26–114) are also removed when the beach unlocks. Otherwise chasers run through palm trunks and the canopies hide the dot. Removal happens after all `rnd()` calls, so other trees, palms and boats don't move.
9. **Tape:** garden circles and the hero row share one `InstancedMesh` (the hero row uses the last 4 slots). Same for boxes and flaps (the hero box uses the last slot). This is as specified, just noting where the slots are.
10. **Bus stop sleepers** sit on the real bench top (local y .715; the review's .86 included the group's .14 lift). The belly-up sleeper lies along the bench (yaw +π/2).

## Cost

- p_5000 frame (SwiftShader, 1080×1920, including the 4096 shadow map): **5.2–5.4 s** after the build vs **5.5–5.9 s** before. That is within run-to-run noise, so under the +10% budget.
- Per frame: about 130 matrix writes for the extras (spots, Mango, droplets, ripples, circle and box heroes, beach, balloons, bus stop) plus the instanced-matrix uploads of the pose meshes. Nothing new runs per house or per lot. Garden circles and boxes use `grown()` like the other garden items.
- New draw calls: about 25 in total, not counting shadow passes (4 pose meshes, WALK, ring/lip/wall/water, droplets, ripples, tape, box, flaps, Mochi about 10 meshes, lighthouse/laser/beam/dot/halo, 2 balloon meshes, bus stop shelter + sign).

## Checks run (stills in `previews/`, configs next to them)

| Still | Result |
|---|---|
| `p_day1`, `q_fountain_day1` | Ring + droplets + Mango only. No circles, box, bus stop, beach, balloons or Mochi. |
| `q_fountain` (t=3), `fountain-flower-top` | 17 spots + Mango. Drinkers' heads over the water, ripples at noses. At t=11.4 a cat stands and stares at the camera. Ring never empty and never full at t = 0, 3, 6 … 21 (4–7 drinking, 8–13 walking, 0–2 empty). |
| Fountain Wave (`fountainWave: 2`, t 3.5) | All 17 + Mango drinking: a flower from above. Lifts run in order m = 1…17, then Mango. |
| `q_circles` (t=5.5) | 4 dark circles on the cream plaza, 4 sitters with the same yaw. At t=3 the 4th cat is still walking in. |
| `q_box` / `tiny-box` | Grey loaf much larger than its box, flaps at the sides. Garden boxes are visible in `p_1000street`. |
| `q_mochi`, `p_1000`, `p_5000` | Mochi reads as a sleeping ginger cat in front of the mountains, with Z letters. Viewer slider: nothing at 910, rising at 968, nearly up at 998. |
| `red-dot-beach`, `red-dot-beach-qa` | Lighthouse, laser and beam, bright dot + halo, 5 chasers, belly-up quitter, no palms in the play area. |
| `fish-balloon`, `p_5000` | 5 balloons with shadows in `p_5000`, 2 in `p_1000`, none at `p_day1`/`p_100`. |
| `bus-stop`, `bus-stop-qa` | Yellow-roof shelter facing out, "NEXT NAP / 5 MIN" in full, 2 loaves + 1 belly-up on the bench. |
| Signs | "PETME2 PET SHOP" and "YOUR IDEA HERE?" show in full. |
| Episode (video) mode | A test episode (980 → 1,020 followers) rendered at t = 0, 1.5, 6, 12, 18: title, subtitles, counter, comment card and end card all work. No balloon over the fountain in the opening. No page errors. |
| Brand | `#FF2A2A` is used only on the dot, halo, laser tip and beam. No new PETME2 text except the postcard's "@petme2". |

## Known issues

- **Episode shots don't visit the new features yet** (except the fountain, which is in every opening). Adding a Mochi shot or a beach shot means adding `EP.shots` entries in the episode JSON (see deviation 1 for the Mochi look-at point). `EP.fountainWave` must be set in the episode JSON to use the wave.
- **In the viewer's default desktop angle**, Mochi sits right behind the big counter when it rises. Auto-rotate moves it into view within about 10 s. On phone it shows under the counter.
- The QA cameras `q_beach` and `q_busstop` from the review crop the lighthouse and the sign at the frame edge. I kept them as specified and added better-framed preview cameras (`v_beach.json`, `v_busstop.json`, `v_balloon.json`).
- The 2 basket cats line up behind each other when a balloon is seen exactly side-on.
- Cats have no faces (engine style), so the "deadpan glance" reads as a head turn toward the camera, not a stare.
- `q_circles` at t=3 shows the 4th circle empty (that cat is still walking in). This is by design; use t ≥ 4.4 for a full row.
- In the test harness Google Fonts is blocked, so the postcard footer was checked with a fallback font. On the live page it uses Nunito from Google Fonts. A tight phone row might wrap again if a much wider font is used.
- `CITY_PLAN.md` still names `town2.html` as the episode engine (noted in the review; not changed here).

## Update 2026-10-06 (evening): real PETME2 fountain + feeder, bigger square, move-around controls

Owner asks: "make a real fountain, like what we actually sell", "make a bigger circle", "fountain & feeder next by", plus web page controls (arrows, zoom, double-tap to fly).

### Engine (`catcity.html`)
| Item | Where (comment in code) | Notes |
|---|---|---|
| Square sizes in one place | `const SQ = {…}` (next to `RING0`) | plaza 16 → **28**, lane 12 → 19, island 8 → 13.6, lawn 7.2 → 12.8, water-bar wall 6.4 → 10 (about 1.7x). Ring roads did not need to move (`RING0` stays 42). |
| Street plan follows the square | spokes `r0: SQ.lane`; lots `r < SQ.plaza + 4`; always-visible roads `< SQ.plaza + 5`; inner garden band 28 → 34.5; countryside trees inside `SQ.plaza + 4` removed after the `rnd()` calls (other trees keep their places) | No houses, gardens or trees on the square (checked top-down). Lots: 6,502 → 6,464 (enough for 5,000). |
| PETME2 Stainless Steel Fountain (3.2L) | `FT` block ("Mango's square + the PETME2 Stainless Steel Cat Water Fountain") | Brushed-steel bowl (r 6.1 → 6.6, h 6, canvas map with lighter vertical facets, `#C9CED6`-ish, metalness .3, roughness .35), top plate with 4 ring grooves, pump cap, goose-neck spout (`TubeGeometry` on a CatmullRom curve, rises 7.85 = 1.3x bowl), clear stream with scrolling streaks, splash drops + ripples where it lands, dark oval water-level window with a light-grey "PETME2" above it (canvas on a curved patch). Height about 15.2. The old dome, blue ears and PETME2 billboard are gone. |
| Water Bar resized | `Build 1` + `updateExtras` | Radii in `WB` (`R_AV` 19.5, `R_FAR` 31, in-lane 17.2, out-lane 15.4, drink spot 10.4, nose 9.35), `Hpath` follows `SQ.island`. Paths are ~1.7x longer, so the drinker loop is 30 s (walk in 9.5, drink 9, turn, walk out 9); Mango keeps his 24 s loop. Mango sits at z 11.2, ripple at 8.6. Droplets/ripples now belong to the spout stream. |
| PETME2 Dual Bowl Automatic Feeder | `FD` block | White tank + domed lid + blue clip, dark window strip with kibble level, white base with 4 LED dots + round button, 4 angled wooden legs (`#A8784F`), 2 food chutes into 2 shallow steel bowls with kibble. On the plaza at angle .78, r 23.5, facing along the plaza. Visible from Day 1. |
| Feeder regulars | "feeder regulars" + `updateExtras` ("Feeder:") | 2 eaters (WALK 24/25 + drink pose, 26 s loop, unlock at followers 3 and 6) and a deadpan starer (WALK 26 + sit pose, head tilted up at the tank, 34 s loop, unlock 8). All pure functions of `t`/`anim`. |
| Plaza heroes moved | `ROW` (r 24, angles 1.71–1.95), `HB` (polar(2.88, 24)), bus stop (polar(6.02, 24), moved out of the feeder's sector) | Cameras `q_fountain`, `q_fountain_day1`, `q_circles`, `q_busstop`, `q_box`, `v_busstop` re-aimed (demo folder + `previews/`). New: `q_fountain_feeder.json`, `q_square_top.json`. |
| Episode opening | default shot looks at y 5–6 (taller fountain) | |

### Web page (`viewer_loop.js` + shell in `viewer.html`)
- Tap info: fountain group (bowl, spout and water ring) shows "💧 PETME2 Stainless Steel Fountain"; feeder shows "🍽️ PETME2 Dual Bowl Feeder". No prices. The old radius-based fountain check is removed; the pin height comes from `userData.info.pinY`.
- Move-around pad (bottom right, above the dock): ▲ ▼ ◀ ▶ pan over the ground (25% of the camera distance, 0.3 s ease; hold = keeps moving), + / − zoom, ◎ flies back to Mango's square. 48 px buttons, pressed state, `navigator.vibrate(8)`, aria-labels, focus ring. Keyboard: arrow keys, + / −. Pan is clamped to 1.3x `__CR`. Any button stops auto-rotate.
- Double-tap / double-click flies there (ground plane y = 0, 0.8 s, distance x0.6) with a yellow ring marker. A single tap now opens the card after 250 ms, so a double tap cancels it (no card flicker, and the scene raycast no longer blocks the second tap).
- One-time hint "Double-tap to fly there · drag to look around · tap a house" (4 s, `localStorage` flag in try/catch). Reduced motion: moves are instant.
- Card titles wrap normally now (`overflow-wrap: anywhere` instead of `word-break: break-all`, which broke "Feeder" into "Feed er").
- Debug helpers for tests: `window.__cam()`, `window.__screenOf(x, y, z)`, `window.__ffPos()`.
- LITE settings are unchanged (no shadows/antialias on phones, fewer trees, 30 fps cap, pause off screen).

### Shopify (`build_shopify.py`)
- **Fixed a break from the LITE change:** the shell now writes `window.CAT_VIEWER…; window.CITY = …` in one script, and the old regex looked for `<script>window.CITY =` only, so the script crashed (and the last port had no LITE/VIEWER flags). It now carries the whole flags + city script over.
- `[data-nav]` and `.dock` lookups are scoped to the section; `#pad`/`#hint` get the `pcc-` prefix; `.pad`/`.hint` become `position: absolute`; the hint flag key is `pm2CatTownHintSeen`.

### Checks
- Stills (SwiftShader 1080x1920): `p_day1`, `p_100`, `p_1000`, `p_1000street`, `q_fountain`, `q_fountain_day1`, `q_circles`, `q_busstop`, `q_box`, `v_busstop`, new close-ups. Top view at anim 0/5/10/15/20/25: cats come in on the lane, 4–8 drink at a time, leave on the inner lane; Mango drinks at anim ~20. Feeder: eaters walk in, eat, leave; the starer sits and looks up.
- `p_1000` full still: **5.5 s** (6.6 s before in the same session), so no slowdown.
- `vtest` (400x860 phone), 360x740, 1280x800: pad visible, not over the dock, counter or card. `taptest`: house, fountain and feeder cards correct. `navtest.js` (demo folder): home, up, hold right, zoom in/out, arrow key, + key, single tap fountain/feeder, double-tap (fly + card unchanged), dblclick all move the view as expected. No page errors, except 2 `setPointerCapture` errors that OrbitControls throws for the test's synthetic pointer events (test only).
- Test note: under SwiftShader a frame takes a few hundred ms, so two real Playwright touch taps arrive > 300 ms apart. The double-tap test therefore dispatches both taps in one page tick; mouse `dblclick` works directly.

### Previews
`final_fountain_feeder.jpg` (camera `q_fountain_feeder.json`, anim 5.6), `final_square_top.jpg` (`q_square_top.json`), `final_city_1000.jpg`, `final_day1.jpg` refreshed.

### Known issues
- At 360 px the "Play growth" button wraps to a second row of the dock (that row was not changed here); the pad moves up with the dock height (`--dockH`).
- The feeder hides part of the fountain from some angles of the default `q_fountain` camera; `q_fountain_feeder` frames both.
- The starer's "look up" is a whole-body tilt (cats have no separate head in the pose kit).

## Update 2026-10-06 (night): figure 8 "food & drink stops"

Owner ask: fountain and feeder each in its own circle, side by side like an 8; cats walk in from the streets and gather (drink around the fountain, eat around the feeder); more cats; Mango hosts between the circles.

- `SQ` is now `{ plaza: 33, laneX: 29.8, laneZ: 18.4, C: 11.5, island: 12.8, lawn: 12, wall: 9.4 }`. Two islands + lawns at x = ±C make the 8; the roundabout lane is an oval (`laneR(a)`), and the 6 inner avenues start at the oval's edge.
- Fountain group sits at x = −C (its Water Bar ring is part of it); `FT.tip` / `FT.hit` are world coordinates. Feeder group sits at x = +C on the lawn, facing +z, with its own "food bar" ring (white walls, kibble trough with 260 kibble pieces, blue lip). Tapping either still opens its card.
- Build 1 rewritten: `WB.N = 26` spots per circle (the side facing the other circle is left for Mango). Each cat walks in from the plaza edge along the ring's normal, drinks/eats 14 s, turns, walks out beside its in-path (34 s loop). Fountain and feeder ranks alternate (1, 2, 3 …), so a small city shows both. 10 loungers (sit/loaf) per lawn unlock after the spots. WALK slots: 0 Mango, 30–55 drinkers, 56–81 eaters (WALK has 90). Ripples: drinkers 0–51, Mango 52–53, stream 54–59.
- Mango sits at the waist (0, 0) facing +z, turns left to drink at the fountain, back, turns right to eat at the feeder, back (36 s loop).
- Removed the old feeder regulars (2 eaters + starer). Hero circle row moved to angles 3.75–3.99 r 27, hero box to angle 2.0 r 27, bus stop to angle 5.0 r 27 (off the oval lane and off the avenues). Inner garden band follows `SQ.plaza + 2.5`.
- New cameras: `q_food_stops.json`, `q_food_stops_close.json`; `q_square_top.json` raised to y 118 to fit the whole 8. Older `q_circles`, `q_box`, `q_busstop`, `q_fountain*` cameras still point at the old spots.
- Checks: stills `q_food_stops`, `q_square_top`, `p_day1`, `p_1000`; viewer at 400x860 (touch): loads, home button, tapping fountain and feeder opens the right cards, no page errors.
- Uploaded to theme copy 188910403796 (only `assets/pm2-cat-city.js` changed; checksums match).

## Update 2026-10-06 (late night): shop button, Halloween, feeding time

- Fountain and feeder cards have a "See it in the shop" button (`.info__shop`, product URLs in `viewer_loop.js`).
- Halloween (`HW`): on Oct 24-31 automatically, or with `?halloween=1` / `EP.halloween`. Pumpkins at every house, witch hats on every other street cat, loungers and Mango, a 12 black-cat parade on the oval lane (WALK 90-101, unlocks at rank 13), candy-colored kibble, "Trick or treat!" sign over the feeder.
- Feeding time (`FEED`, 14 s): tapping the feeder (food) or fountain (water) calls `window.feedTime(kind)`; the viewer also runs it every 45 s, alternating. Street cats near the square walk to the plaza edge, the matching spot cats rush in; kibble rains onto the food bar, or water arcs into the Water Bar ring. Preview with `EP.feed = {kind, at}`.
- `build_viewer.py` now escapes all non-ASCII (HTML entities outside scripts, `\uXXXX` inside), so symbols show right even when no charset is sent.
- Size chips fly closer on small towns (Day 1 now opens near the fountain and feeder). Big Mochi fits the 400x860 phone view.
- Cameras: `q_hw.json`, `q_hw_wide.json`, `q_feed_food.json`, `q_feed_water.json`.
- The store has 20 themes (Shopify's limit), so `themeDuplicate` returns null. Uploaded to the unpublished copy 188910403796 instead (renamed). Theme names must be 50 characters or fewer.
- Owner feedback (same night): the whole city rushing in looked funny. Now only about 1 in 3 street cats within 75 of the square walk over (`l.r < 75 && hash01(k*7+3) < .3`); the circle's own drinkers/eaters still gather. Card notes say "the cats nearby".

## Update 2026-10-06 (go-live): Mango only

- Owner: go live with 0 cats, only Mango. `build_viewer.py` data now has `"live": {"followers": 0}`. In live mode the viewer sets the slider to that number, hides the slider, size chips and Play growth, and starts the camera close on the square (84 phone / 70 desktop) while followers < 100.
- To grow the real town later: raise `live.followers` in `build_viewer.py` (and add real handles), rebuild, upload. Remove `live` to bring back the growth demo.
- Uploaded to 188910403796, renamed "PETME2 — Cat Town LIVE (Mango only)". Owner publishes it.
- Owner (23:17): remove "Save postcard" from the website. The button is now hidden in `viewer_loop.js`; in live mode the whole top row of the dock is hidden. Built files: pm2-cat-city.js md5 fd90ca427b11917c73349200268b9a3f (liquid unchanged). Owner had already published 188910403796, so this change needs an unpublished copy (188909420756 matches live except the Cat Town files) and a re-publish. Upload not done yet: the write was blocked by a permission check, waiting for the owner's OK.

## Update 2026-10-07: real live version + "Find your cat house"

- Data: page metafield `cattown.town` (JSON, definition "Cat Town residents" on the Cat Town page). Shape: `{"start": "2026-10-07", "residents": [{"name": "...", "ig": "...", "tt": "...", "day": 1}, ...]}`. List order = move-in order; Cat # = position. The section prints it as `window.CITY_LIVE`; `build_viewer.py` (LIVE_JS) turns it into `EP.live.residents/followers/day` before the engine starts. Updating the metafield changes the page right away, no theme publish.
- Counter: residents + Mango, "Day N" = days since `start` + 1 (counts up by itself).
- Search under the counter: exact match on Instagram / TikTok handle (with or without @) or name, then partial match (3+ letters). Hit: camera flies to the house, pin + ring, card (@handle, cat #, moved in on day X, name/TikTok, house kind). Miss: "Not in Cat Town yet / Follow @petme2 to move in!". The card/hint are placed under the search box by JS (`placeLow`).
- Save postcard button hidden; in live mode the dock top row, slider, chips and Play growth are hidden.
- `viewer.html` now has a viewport meta, so local phone tests match real phones.
- /cat-town already redirects to /pages/cat-town (UrlRedirect 606478794964), so the short link works.
- Uploaded to new copy 188916498644 (old copy 188909420756 had been deleted, so a duplicate worked). Tested with sample residents in the test browser only.
- Owner (00:40): small "Updated <date, time> · Next update in a few hours" line under the counter. Comes from the metafield's `updated` field (ISO time, e.g. `2026-10-07T00:50:00Z`), shown in the visitor's own time zone. Set `updated` every time the resident list changes.
