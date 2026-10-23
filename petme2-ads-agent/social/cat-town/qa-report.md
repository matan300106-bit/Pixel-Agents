# Cat Town: final QA report (2026-10-06)

Checked against `design-review.md` section 5, the owner rules in `CITY_PLAN.md`, and `build-notes.md`.
All renders are my own: `catcity.html` and `viewer.html` (rebuilt), Playwright + SwiftShader, 1080x1920 stills.
Scratch renders: `scratchpad/demo1000/still_qa/`, `qa_*.png`.

**Verdict: PASS, with 2 small fixes made and a few minor issues listed below.**

## 1. Build items (design-review acceptance checks)

| Build | Result | Evidence |
|---|---|---|
| 1 Water Bar (fountain) | PASS | Day 1 (`p_day1`, `q_fountain_day1`): water ring, blue lip, droplets, big orange Mango at the front, no other cats. At 1,000: drinkers around the ring, heads over the water, ripples at the noses. Top view at t = 0, 6, 12, 18: the ring is never empty and never full (about 6-9 drinkers + walkers). Old Mango road patrol is gone. Fountain Wave (`fountainWave: 2`): every spot plus Mango drinking at t 2.5-5.5 (a "flower of cats" from above). |
| 2 Circle traps | PASS | `q_circles`: 4 dark circles on the cream plaza, not on the road. 3 sitters with the same yaw; at t = 3 the 4th circle is still empty (its cat is walking in, by design). None on Day 1. Garden circles: not clearly seen at phone size (not a blocker). |
| 3 Tiny boxes | PASS (weak) | `q_box`: big grey loaf on a small box. The box is mostly hidden under the cat, so the joke reads only in close-up. None on Day 1. |
| 4 Big Mochi | PASS | Not in `p_100`. In `p_1000` / `p_5000` a ginger sleeping cat with stripes, head, ears, closed eyes, pink nose and Z letters, fully inside the frame. Web page: absent at 901, rising at 971, up at 1,001. Close-up `final_mochi.jpg` reads as a cat. |
| 5 Red Dot Beach | PASS | `v_beach`: lighthouse, laser beam, red dot + halo, chasers. `p_5000`: dot and beam visible at the bottom right. `q_beach` (review camera) crops the lighthouse at the edge (known, kept). |
| 6 Fish balloons | PASS | None at Day 1 / 100. 2 in `p_1000`, 5 in `p_5000` (with shadows), none over the fountain or Mochi in those frames. |
| 7 Bus stop | PASS after fix | "NEXT NAP / 5 MIN" in full, 2 loaves + 1 belly-up on the bench. **Bug found and fixed:** the sign post went through the board, so "5 MIN" read "5 NIN". |
| 8 Postcard | PASS | Phone 390x844: button in the first row, click gives a 1080x1350 image, footer "Cat Town · 971 cats · Day 30" + "@petme2", Esc closes it. No page errors. |
| Sign text | PASS | "PETME2 PET SHOP" and "YOUR IDEA HERE?" show in full in `p_1000` / street. |
| Determinism | PASS | Same `t` rendered twice gives the same md5 (`p_5000` t=3, top view t=0). |

## 2. Owner rules

| Rule | Result | Note |
|---|---|---|
| Every follower has their own small house | PASS | `houseLots = cand.slice(0, F)`, one lot per follower (6,502 lots available, enough for 5,000). |
| No cars | PASS | No car models. The only vehicles are human-pushed yellow cat-taxi strollers. |
| Cats walk the streets | PASS | One walker per house on the sidewalks, some nap on roofs. |
| A few humans with cat-taxi strollers | PASS | `min(26, F/120 + 2)`: 2 at Day 1, about 10 at 1,000, 26 at 5,000. Not too many. |
| Round, organic layout (not a grid) | PASS | Ring roads + curvy avenues (see `final_city_5000.jpg`). |
| Mango orange at the center | PASS | `#F28C28`, sits in front of the fountain, drinks every 24 s. |
| PETME2 small | PASS | Only on the fountain sign, the pet shop, the top pill and the "@petme2" footer / end card. |
| No milk, no prices, nothing mean or copyrighted | PASS | grep found nothing. No cat bus, no film references. `#FF2A2A` only on the dot, halo, laser tip and beam. |

## 3. Web page growth mode (phone 390x844, desktop 1280x800)

| Followers | Result |
|---|---|
| 0 (Day 1) | "1 cat · Day 1": roundabout + fountain only, nothing floating. |
| 100 | First rings of houses, City Hall, pet shop. No Mochi, no balloons. |
| 1,000 | City + Mochi + balloons. |
| 5,000 | Full round city. |
| Errors | 0 page errors. Only console noise: Google Fonts blocked by the test sandbox (harness only) and one three.js warning "toNonIndexed(): already non-indexed" (harmless). No horizontal scroll. |

## 4. Performance

`p_5000` frame, SwiftShader 1080x1920, timed with a GPU sync:

| Engine | First frame | Next frames |
|---|---|---|
| Before the build (`catcity_orig.html`) | 4.5 s | 3.0-3.2 s |
| Now | 5.1 s | 3.1-3.4 s |

Whole still (load + first frame + screenshot) is about 5.9 s. Steady frames are +3-6% (OK). The first frame is about +12%, mostly shader compile for the new materials. That is a one-time cost, not a per-frame regression. Not blocking.

## 5. Fixes I made

1. **Bus stop sign** (`catcity.html`, Build 7): the sign post moved from z .4 to z .33, behind the board. Before, it went through the text ("5 NIN"). Verified in `v_busstop`.
2. **Phone chips row** (`viewer.html` shell CSS, `@media (max-width: 520px)`): "5,000" wrapped onto a second line. The chips now share one row (`flex: 1 1 0`, nowrap). Verified at 390 px. `viewer.html` was rebuilt with `build_viewer.py`.
3. **Stale preview cameras**: `previews/p_100.json`, `p_1000.json`, `p_1000street.json` and `p_5000.json` were older than the builder's renders. With the old cameras, Mochi was cut off at the right edge, a balloon covered Mochi, and in the street view a balloon covered the counter. I synced them to the cameras the builder really used (the demo folder versions). Those frame everything correctly.

## 6. Open issues (minor, not fixed)

- **Phone web page at 1,000+:** with the default camera, Mochi sits at the top-left edge, partly cut off, and its Z letters touch the counter number. Auto-rotate moves it into view. Fix idea: start the phone camera turned about 20° or a little lower.
- **Web page Day 1** is a small fountain in a big empty field from far away. That is fine as "empty land", but a closer Day 1 camera would look more inviting.
- **Episode end card (t=18):** a fish balloon sits behind the "PETME2 CAT TOWN" pill at the top. Small; move the balloon or the end shot camera if it bothers.
- **Mochi's Z letters** are white on pale mountains, so they have low contrast in wide shots.
- **Tiny box** joke reads only in close-ups (the box hides under the cat).
- `q_beach` / `q_busstop` review cameras crop their subject. The builder's `v_*` cameras are better; use those.
- Garden circles and garden boxes were not clearly seen in the wide stills (they are small). Not a blocker.

## 7. Final previews (in `previews/`)

`final_fountain.jpg`, `final_day1.jpg`, `final_city_1000.jpg`, `final_city_5000.jpg`, `final_street.jpg`, `final_mochi.jpg` (camera in `final_mochi.json`), `final_beach.jpg`, `final_webpage_phone.jpg`.
