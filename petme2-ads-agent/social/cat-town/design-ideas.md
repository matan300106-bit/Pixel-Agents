# Cat Town: design ideas (designer pass, 2026-10-06)

This doc is based on `CITY_PLAN.md`, `catcity.html` and the two previews. All sizes are in world units, using the engine's own scale: houses are about 3.6 wide, cats about 1.2 long (catMesh scale 1.15), roads 4.4 wide (8.4 with sidewalks), ring roads 30 apart, the first ring at r = 42, and the 6 first avenues start at r = 12 at angles `.26 + i*PI/3`. All motion is a pure function of `anim`, so a video frame always renders the same way. Use `hash01(...)` and never `Math.random()` inside `renderFrame`.

---

## 1. Vibe

**One line:** *A sunny Sunday afternoon in a town where the cats are completely serious about very silly things.*

- **Time of day:** late golden afternoon, fixed. There is no day/night cycle, because it costs shadows and breaks the daily episodes. Sun `#FFE2B8`, intensity 2.4, and the sun lowered from ~55 deg to ~40 deg elevation for longer, softer shadows. Shadow camera bounds stay as they are now. Exposure 1.1. Keep the existing sky gradient and fog. The haze on the mountains is part of the look.
- **Palette:** cream sidewalks `#E9E3D3`, soft slate roads (`#4A4F5C` can go a little warmer to `#4F515C`), grass greens `#A9D27A`/`#8CC56A`, pastel walls, and the taxi yellow `#FFC93C` as the happy accent. **PETME2 blue `#2F5FE0` is used only on the fountain, the pet shop and existing roofs.** It stays special. **Pure red `#FF2A2A` is used for one thing only: the laser red dot.** If nothing else in town is that red, the eye finds the dot at once.
- **Visual humor rules (it must work with the sound off, because Instagram autoplays muted):**
  1. **Deadpan cats.** Cats never react to the absurd thing. A cat sits in a box three sizes too small and looks fine with it.
  2. **Rows + one exception.** Five cats do the same thing and one does it wrong. That is the joke and the screenshot.
  3. **Readable in 1 second at phone size.** Every gag must read as a silhouette from the episode camera (~30-60 units away). Text is used only on signs, never more than 4 words.
  4. **Real cat behavior, slightly exaggerated.** Boxes, circles, red dots, knocking things off, sunbeams, zoomies. People share what they recognize from their own cat.
- **Kindness:** nothing scary, nothing breaks, no cat gets hurt or pranked. Things that fall land softly.

---

## 2. Shared foundation: the "pose kit" (build once, used by many ideas)

Today there is one merged cat geometry (`CAT_GEO`, facing +z: body `.5×.45×.9` at y .45, head `.48×.42×.42` at (0,.82,.5), ears, tail, legs). Add **3 more merged geometries** (~100 triangles each) and one trick:

| Pose | Build (same parts as `CAT_GEO`, moved) | Used by |
|---|---|---|
| `CAT_DRINK` | body rotated rx +.12 (front lower); head moved to (0,.50,.72) and rotated rx +.6 (nose down); ears move with the head; tail raised: box `.1×.1×.6` at (0,.95,-.55), rx -1.2 (tail up = happy cat); legs unchanged | Fountain (1) |
| `CAT_SIT` | haunch box `.55×.3×.5` at (0,.15,-.15); upright body `.5×.7×.5` at (0,.5,-.05), rx -.35; head at (0,1.0,.15); ears at y 1.3; front legs `.12×.45×.12` at (±.13,.22,.18); tail flat on the ground `.1×.08×.7` at (.3,.05,.1), ry .9 | Circles, bus stop, Mango, boxes |
| `CAT_LOAF` | body `.55×.4×.95` at y .2 (no legs: the "loaf"); head at (0,.5,.5); tail laid along the side `.1×.08×.7` at (.3,.08,0) | Boxes, bus stop, bakery |
| *Belly-up* (no new geometry) | `CAT_GEO` with instance rotation rz = PI, lifted to y = 1.25×scale, so the legs point at the sky | Nap park, catnip, bus stop |

Each pose is **one InstancedMesh** sized for every idea that uses it. That is 3 draw calls in total, with per-instance colors from `CAT_COLORS`. Static poses get their matrix once. Only animated ones are updated per frame.

---

## 3. The ideas

Legend: **MUST** = top 8, best fun for the effort, build first. **LATER** = good, but after the MUST list. Cost is counted at a 5,000-house / 5,000-cat city. "Draw calls" means InstancedMeshes or meshes added (shadow pass +1 each if they cast shadows).

---

### 1. Mango's Water Bar: the drinking fountain — **MUST**

**What you see.** Around the PETME2 fountain is a new low blue-rimmed water ring, the town's "water bowl". Cats trot in from the avenues, line up around the rim like spokes of a wheel, lower their heads and lap, sometimes look up straight at the camera, then walk away happy with their tails up. Mango, the biggest cat at the bar, sits at the front as host and drinks too. From above, the drinking cats form a ring of petals around the fountain: **the bullseye of the round city is a flower made of cats.**

**Why it's shareable.** It is the brand promise (cats love drinking from a fountain) shown as pure behavior with no sales talk. Every cat owner knows the head-down lapping pose, and the "glance at the camera mid-drink" is a meme-able moment. The **Fountain Wave** (below) is a made-for-video hero shot.

**Build spec**

*New fountain parts* (static meshes added to the existing center block; nothing existing moves):
| Part | Geometry | Position | Color |
|---|---|---|---|
| Water ring wall | `Cyl(6.0, 6.2, .5, 32)` | y .79 (sits on lawn top .54, top at 1.04) | `#FFFFFF` |
| Water surface | `Cyl(5.9, 5.9, .04, 32)` | y 1.0 (shows as a ring from r 4.8 to 5.9; the fountain base covers the inside) | `#7FD0FF`, roughness .2 |
| Blue lip | `Torus(6.0, .12, 6, 40)`, rotated flat | y 1.06 | `#2F5FE0` |
| Water arcs | 6 arcs × 8 droplets, `Icosahedron(.16, 0)` InstancedMesh (48) | see animation | `#BFE9FF`, emissive `#7FD0FF` .3 |
| Paw crosswalks | existing `pawGeo` at scale .6, 5 per avenue across the roundabout road (r 8.2 to 11.8 along each first-ring avenue), InstancedMesh (30) | y .17 | white `MeshBasic` |
| Chalkboard | small A-frame (2 boxes `1.2×1.6×.08`, tilted ±.25) + `textSign('WATER BAR · ALL CATS WELCOME', 2.4)` | at r 14.5, angle PI/2 + .35 (beside the +z entrance, faces the opening camera) | `#3B3B44` board |

*Drinking spots:* 18 angles `a_j = .26 + j*PI/9` (every 20 deg). Skip the 2 spots nearest PI/2: that is **Mango's VIP spot** (angle PI/2, r 7.9, scale 2.6, front-center in the opening camera at +z). That leaves **16 drinking spots**. A small cat stands at **r 6.7**, yaw = facing the center. With `CAT_DRINK` at scale 1.15 the head reaches r ~5.9 and the chin is at y ~.95, right at the water line (1.0).

*Paths:* each spot belongs to its nearest first-ring avenue `i`. Precompute two polylines per spot, with `cum[]` like `ROADS` so the existing `sampleRoad()` works:
- **In-path:** along avenue `i` from r 26 down to r 12 (`angle = spokeA(sp_i, r)`), then across the roundabout to (a_j, 6.7), with the angle eased by smoothstep and r linear. Length ~20 units.
- **Out-path:** from the spot out along avenue `(i+1) % 6` to r 26, so cats leave by a different street than they came. That looks like real traffic, not a ping-pong.
- *Polish (optional):* start the in-path at the cat-flap door of the nearest house lot on that avenue. Cats squeeze out of the flap (scale z 0 to 1 over .3 s), which is funny up close.

*Instances:* the walking cat uses `catMesh`-style `CAT_GEO` in a small InstancedMesh **Walkers (17)**, the drinking cat uses the `CAT_DRINK` pose mesh (17 slots incl. Mango), and Mango's sitting uses `CAT_SIT`. Each frame, every slot writes its matrix into exactly one of these and `ZERO` into the others. Mango's `catMesh` slot 0 is set to `ZERO`; his old roundabout patrol is replaced. Extras: **Ripples** `Torus(1, .04, 3, 20)` flat, white `MeshBasic`, InstancedMesh (40). **Tongue** `B(.12,.03,.14)` `#F28FA6`, InstancedMesh (17).

**Animation** (per spot `j`, period P = 24 s, `u = (anim + hash01(j*41+3)*P) % P`):

| u (s) | Beat | How |
|---|---|---|
| 0 – .3 | appear at the start of the in-path | scale 0 to 1.15 (`back` ease) |
| 0 – 6 | **thirsty trot** in (~3.3 u/s) | `sampleRoad(in, u/6*len)`, yaw = path direction, bounce `y = |sin(anim*11+j)|*.15` (faster than normal cats: they're thirsty) |
| 6 – 6.4 | arrive, settle | squash: scale y × (1 − .06·sin(PI·k)) |
| 6.4 – 14.4 | **drink** | swap to `CAT_DRINK`. Lapping: instance pitch `rx = .05*sin(anim*14 + j)` (~2.2 laps/s). Two ripples at the nose point (r 5.75, y 1.02): `f = frac(anim*1.6 + j*.37 + q*.5)`, scale `.15 + .6f`, `ZERO` when f > .95 |
| 10.4 – 11.0 (only when `j % 3 == 0`) | **suspicious glance** | swap to standing `CAT_GEO`, yaw turns toward `camera.position` (clamped to ±.7 rad of facing the fountain), hold, then back to drinking. Deadpan. |
| 14.4 – 15.0 | head up + **lick** | standing pose; tongue box visible in front of the mouth at (0,.78,.75)×scale for 0.3 s with `y += .02*sin(anim*30)` |
| 15.0 – 15.6 | turn around | yaw eases toward the out-path start direction |
| 15.6 – 23.7 | **happy walk out** (~2.5 u/s) | `sampleRoad(out, …)`; first 2 s: a little hop, bounce amplitude .22 |
| 23.7 – 24 | disappear | scale to 0 |

*Mango (VIP spot):* `CAT_SIT` at scale 2.6 for u 0–16, slowly turning his head side to side (whole-instance yaw `±.35*sin(anim*.6)`) as he watches arrivals like a host. For u 16–22 he swaps to `CAT_DRINK` at scale 2.6, placed at r 8.3, extra pitch +.25 so his chin reaches the water. Biggest cat, biggest ripples (scale ×2).

*Water arcs:* droplet `i` of arc `k`: `f = frac(anim*.7 + i/8)`, angle `k*PI/3 + .5`, `r = .6 + 4.8f`, `y = (1−f)*6.3 + f*1.0 + 4.8*f*(1−f)`. The arc clears the blue bowl rim (y 3.5 at r 4.0). Where it lands (r 5.4) it spawns a splash ripple. Also make the existing dome water "breathe": `scale.y = 1 + .02*sin(anim*3)`.

*The splash gag (one per loop):* once every 24 s, droplet 0 of arc 0 is scaled ×2.5 and its arc ends on spot 4's head. That cat jumps (`y += .5*sin(PI*k)` over .3 s), shakes (`rz = .25*sin(anim*40)` for .5 s), then goes straight back to drinking as if nothing happened.

*Fountain Wave (video hero shot):* when `EP.fountainWave = t0`, every spot's phase is forced so all 16 cats + Mango are drinking from t0 to t0+3 (a perfect flower from above). Then they lift their heads one after another around the circle (spot `j` lifts at `t0 + 3 + j*.12`) like a stadium wave, and drop back down. Use it as the "Day N" title shot.

**Cost.** 48 droplets + 30 paws + 40 ripples + 17 tongues + 17×3 cat instances ≈ **190 instances, ~70 animated per frame**, +6 draw calls, +3 static meshes. Free next to the 5,000 walking cats.

---

### 2. The Sleeping Mountain ("Big Mochi") — **MUST**

**What you see.** In front of the mountains lies a cat the size of a hill, curled in a donut with its tail over its nose, fast asleep. Every few seconds its whole side rises and falls. Little "Z" letters float up.

**Why it's shareable.** City-scale wow: in every overview shot people zoom in and say "wait, is that a CAT?" That second look is what gets shares. It also works as a milestone reveal ("1,000 followers: the mountain is... a cat?").

**Build spec** (one `Group`, all `flatShading`, color `#EDE6DD` cream-white with `#C9BBAA` stripes so it stands out against green hills and fog):
- Body: `Icosahedron(40, 1)` scaled (1.35, .55, 1.0). Center y 8.
- Head: `Icosahedron(17, 1)` at (+38, 10, +18) relative, tucked against the body, rotated so the face points at the city. Ears: 2 × `Cone(6, 10, 3)`, one flopped flat (rz 1.2) for sleepiness. Closed eyes: 2 × `B(5, .6, .6)` `#5A4F45`, slightly curved down (rz ±.25). Nose: `Cone(1.5, 2, 3)` `#F28FA6`.
- Tail: `Torus(46, 6.5, 6, 18, PI*1.25)` lying flat around the front of the body, ending over the nose.
- Stripes: 5 × `Torus(arc)` segments in `#C9BBAA` across the back.
- Front paw: `B(10, 6, 16)` with rounded corners (2 scaled boxes) peeking under the head.
- "Zzz": 3 letters, each 3 thin boxes (top / diagonal / bottom), `#FFFFFF`, letter height 6.
- **Where:** polar angle 3.45 rad, r 540. That is behind the city, in front of the mountain arc (mountains are at r 580–690, angles 1.8–4.8 rad). Before the trees are placed, clear countryside trees within 75 units of it (one extra `if` in the tree spot filter).

**Animation:** breathing `body.scale.y = .55*(1 + .03*sin(anim*1.1))`, and the head rises with it by `+.6*sin(anim*1.1)`. Every 7 s the flat ear flicks (`rz` 1.2 to .6 and back over .4 s). Each Z: `f = frac(anim*.25 + k/3)`, position = above the head + (f*8, f*22, 0), scale `sin(PI*f)` (it grows, then shrinks to 0).

**Cost.** ~16 static meshes, 3 animated. **~20 draw calls if built as separate meshes. Merge the static parts into 2 meshes (body color + stripe color) for 5 draw calls.** No instancing needed. Zero per-cat cost.

---

### 3. Red Dot Lighthouse — **MUST**

**What you see.** A white-and-red-striped lighthouse on the beach. Instead of a lamp, a giant laser pointer sits on top, aiming down at the sand. A bright red dot zips around the beach in loops, and a gang of 7 cats chases it forever. One cat is always mid-pounce, one is doing the butt-wiggle before the jump, and one has given up and is lying belly-up.

**Why it's shareable.** It's the most universal cat joke there is. "The lighthouse that keeps the town's cats busy" is a one-line caption that writes itself.

**Build spec:**
- Tower: `Cyl(2.2, 3.0, 18, 10)` `#FFFFFF`. 3 bands `Cyl(·, ·, 1.6, 10)` in `#E85D5D` at y 4, 9, 14 (the salmon red, so it doesn't compete with the dot). Gallery: `Cyl(3.2, 3.2, .4, 10)` `#3B3B44` at y 18.2. Lamp room: `B(3, 2.4, 3)` with light-blue `#9FD3FF` sides.
- Laser pointer on top: `Cyl(.6, .6, 4.5, 10)` `#3B3B44`, lying down, pitched ~-0.5 rad toward the beach. Tip: `Cyl(.35, .35, .3)` `#FF2A2A` emissive 1.
- Dot: `Cyl(1.3, 1.3, .03, 20)`, `MeshBasicMaterial #FF2A2A`, plus a soft halo `Cyl(2.2, 2.2, .02, 20)` transparent .35. Optional beam: thin `Cyl(.06, .06, 1)` `#FF2A2A` opacity .25, stretched each frame from the tip to the dot.
- **Where:** on the sand at `z = 60`, `x = coastAt(60) + 6`. The dot plays on the beach strip `x ∈ [coastAt(z) − 8, coastAt(z) + 14]`, `z ∈ [30, 110]`.
- **Unlock:** suggest a milestone (e.g. 500 followers) or the first beach-themed comment build.

**Animation:**
- Dot: `D(t) = (cx + 9*sin(t*.9) + 4*sin(t*2.3), z0 + 30*sin(t*.47) + 8*cos(t*1.7))`, evaluated at `t = anim`. It looks erratic but loops.
- Chasers k = 0..5 (`CAT_GEO` InstancedMesh, 6): position = `D(anim − .35 − .3k)` + a small sideways offset `(k % 2 ? 1 : −1) * .8k`, yaw toward `D(anim)`. Cat 0 pounces every 3 s: `y = 1.0*sin(PI*k)` over .5 s, pitched nose-down on landing, always landing just after the dot has moved away.
- Butt-wiggle cat (k = 2, while the dot is within 3 units): body yaw `±.12*sin(anim*22)` and scale z 1.05 (the pre-pounce shimmy).
- Quitter: 1 belly-up cat on the sand near the tower, static except its legs (rz `±.08*sin(anim*2)`).

**Cost.** ~10 static meshes + 2 animated (dot, beam) + 7 cat instances. **≤ 4 draw calls** if the tower is merged.

---

### 4. If It Fits, I Sits — **MUST**

**What you see.** All over town, cats sit in cardboard boxes clearly too small for them: a fat loaf spilling over a box the size of a shoebox, a cat whose box is so small only its front paws fit, and once per district a pizza-size flat box with a cat sitting on it perfectly square.

**Why it's shareable.** Every cat owner has this photo. Close-up shots of these get the "this is literally my cat" comments. It also fits the town's cardboard-box houses.

**Build spec** (new garden kind `'tinybox'`, added to the `kinds` list of the gardens block, ~1 in 9 garden spots):
- Variant A "loaf overflow": box `B(.9, .5, .8)` `#C99A62` at y .25, 2 open flaps `B(.9, .03, .35)` tilted ±.6, cat `CAT_LOAF` at scale 1.15, y .45. The cat is about 1.4× wider than the box.
- Variant B "paws only": smaller box `B(.45, .35, .45)` at the cat's front; `CAT_SIT` positioned so the front legs are inside the box.
- Variant C "the square": flat box `B(1.6, .15, 1.6)` with `CAT_SIT` dead center, exact same yaw as the box.
- Variant chosen by `hash01(i)`: A 60%, B 30%, C 10%.
- **Where:** garden spots between streets (same rules as ponds and yarn: `any(roadHash…)`, `any(lotHash…)`), appearing with the city (`grown(...)` using `timeNear`).

**Animation:** almost none; that's the joke. Every ~9 s (`frac(anim/9 + hash) < .05`) the cat shifts its yaw by `±.15` and back. Boxes are static.

**Cost.** ~170 spots at 5,000 houses → **~170 box + ~340 flap + ~170 cat instances**, all static (matrix set once). +2 draw calls (box, flap); the cats go into the existing pose meshes.

---

### 5. Cat Circle Traps — **MUST**

**What you see.** White tape circles are painted on the plaza, in parks and in front of landmarks, and inside each one sits exactly one cat, perfectly centered. On Mango's square there is a row of 5 circles, each with a sitting cat, and one empty circle. A cat walks slowly toward the empty circle, steps in, sits, and the row is complete.

**Why it's shareable.** It is the famous "cat circle trap" internet trend, shown as a 3D town feature. The "complete the row" moment is a perfect 3-second loop, and the row + one-exception rule makes it read at once.

**Build spec:**
- Circle: `Torus(1.0, .05, 4, 24)` rotated flat, `MeshBasic #FFFFFF`, y .1 (on grass, y .1; on the plaza, y .16), scale .95–1.15 by hash.
- 1 in 12 circles is a **square** instead: 4 thin boxes `B(2, .02, .1)`. Same joke, extra nerdy.
- Cat: `CAT_SIT` at the center, random yaw.
- **Where:** (a) **hero row**: 6 circles on Mango's plaza ring at r 14, angles PI/2 + .5 … + .5 + 5×.17 (beside the Water Bar chalkboard); (b) 1 in 10 garden spots (new kind `'circle'`); (c) 1 circle in front of every landmark spot (at the spot center + 9 units toward the road).

**Animation:** hero row: the 6th cat walks a 6-unit straight line into its circle over 4 s (`CAT_GEO`, bounce), turns to match its neighbors' yaw (.4 s), swaps to `CAT_SIT`, holds 12 s, walks back out of frame, then repeats (period 20 s). The other circle cats are static, with a tail-flick ear twitch (yaw ±.05 every 5 s).

**Cost.** ~150 rings + ~150 sitting cats, static. **+1 draw call** (rings). 1 animated cat.

---

### 6. The Runaway Yarn Ball — **MUST**

**What you see.** A big yarn ball rolls down an avenue, unrolling a wiggly red thread behind it, shrinking as it goes. Five cats chase it at full sprint, plus one more cat back at the start, completely tangled in thread and happy about it.

**Why it's shareable.** Motion plus a chase reads instantly in the overview shots (a red line drawing itself across the city). Close-up, the tangled cat is the punchline.

**Build spec:**
- Ball: reuse the yarn geometry `Icosahedron(1.1, 1)` in its own InstancedMesh, color from the yarn palette.
- Thread: `B(1, .03, .08)` segments, InstancedMesh, 40 per event, same color as the ball.
- Chasers: 5 `CAT_GEO` instances per event (a small own InstancedMesh, so the walking-cat loop isn't touched).
- Tangled cat: `CAT_SIT` + 3 `Torus(.45, .04, 3, 12)` rings around its body at different tilts, in the thread color.
- **Where:** first-ring avenues `i = event index` (max 6), from r 20 outward, rolling 70 units. Number of events: `min(6, max(1, floor(F/1000)))`, only once that avenue is built (its `PIECES.t` has passed).

**Animation** (period 18 s, `f = (anim + 3k) % 18 / 16`; for f > 1 the ball is hidden and the scene resets):
- Ball: `s = 20 + 70f` along the road via `sampleRoad`. Roll: rotation about the road's sideways axis by `−s/r`. Radius `r = 1.1*(1 − .55f)`, so it visibly gets smaller as it unrolls.
- Thread segment `q` (0..39): placed at `s_q = 20 + 70f*(q/40)`, sideways offset `.4*sin(q*1.7 + k)` for a loose, wiggly line, yaw from the road direction, length 70f/40 + .2.
- Chasers at gaps of 2.5, 4, 6, 9 and 15 units behind the ball. The last one runs 1.4× faster and catches up near the end of each loop. Run bounce .2 at 13 Hz.
- At the loop end the ball pops back at r 20 (scale `back`), and the thread segments disappear tail-first over .5 s.

**Cost.** Per event: 1 + 40 + 5 + 4 ≈ 50 instances. Max 6 events → **~300 animated instances**, +4 draw calls.

---

### 7. Cat Bus Stop: "NEXT NAP: 5 MIN" — **MUST**

**What you see.** A yellow bus shelter (same yellow as the Cat Taxi strollers) with a sign: **NEXT NAP: 5 MIN**. On the bench, three cats are fast asleep: a loaf, a curl, and one completely belly-up with its legs in the air. A Cat Taxi stroller rolls up, stops for 2 seconds... and leaves. Nobody got on.

**Why it's shareable.** It's a text gag readable in under a second, and the stroller leaving empty-handed is a mini story. It also makes the Cat Taxi system feel real.

**Build spec:**
- Shelter (merged into one geometry, InstancedMesh): back panel `B(4, 2.4, .12)` `#9FD3FF`, roof `B(4.4, .2, 1.6)` `#FFC93C` at y 2.6, 2 posts `Cyl(.08, .08, 2.6)` `#3B3B44`, bench `B(3.6, .25, .8)` `#C98B5A` at y .7. Merge it as a vertex-colored geometry (or 3 InstancedMeshes by color).
- Sign: one post `Cyl(.06, .06, 3)` + a board `PlaneGeometry(1.8, .6)` with **one shared** canvas texture: `NEXT NAP: 5 MIN` on top and a small zZz paw icon. All stops share 1 material.
- Cats: `CAT_LOAF`, `CAT_SIT` with its head lowered (sleeping), and belly-up `CAT_GEO`, all at bench height y .85.
- **Where:** one stop at each Cat Taxi's turnaround point (`s0 − L/2` on its road, on the sidewalk at offset 3.6, on the side opposite the lamp). That's ≤ 26 stops. Plus one hero stop at Mango's square (r 14.5, angle PI/2 − .6).

**Animation:**
- Taxi pause: in `walkPos` for taxis, make the triangle wave plateau at its ends (hold 2 s at `f = 0`), so the stroller stops right at the shelter, then leaves.
- Sleepers: breathing `scale.y × (1 + .04*sin(anim*1.4 + k))`; the belly-up cat's legs paddle a little in a dream (rz `±.05*sin(anim*6)`, for 1 s every 8 s).
- Optional: a "Zzz" (reuse the Big Mochi Z boxes at scale .08) floating above the bench.

**Cost.** ≤ 27 stops × (1 shelter + 1 sign + 3 cats) ≈ **135 instances**, +3 draw calls, 1 shared texture.

---

### 8. Find Your House (+ save a postcard) — **MUST** (interactive page)

**What you see (on the web page).** A search box: "Find your cat house: @your_name". Type your handle and the camera flies across town to your house, the house does a happy bounce, your name tag pops up ("@name · Cat #1,234 · moved in Day 37"), and your cat walks out of the cat-flap door. A button says **Save my postcard**.

**Why it's shareable.** It is the strongest share engine you can build: every follower has a reason to visit, find their own house and post a screenshot ("I live in Cat Town"). That brings more followers, which brings more houses. It makes the "every follower gets a house" rule personal.

**Build spec:**
- Page mode `?play=1` (the video mode stays untouched). The `city.json` needs a `residents` list (public handle → house number `n`), the same data the episodes already use for name tags.
- Lookup: handle → `n` → `houseLots[n]` (x, z, ry).
- Camera: 2 s `inout` flight from the current view to `lot + (dir_out × 18, 14, …)`, looking at the lot.
- Bounce: call `placeHouse(n, back(k))` with k going 0.6 → 1 again.
- Tag: reuse the `.tag` CSS (already built for episodes).
- That house's cat: force `CATW[n].nap = false` and start it at the door for 3 s.
- Postcard: render one frame, `canvas.toDataURL()` (`preserveDrawingBuffer` is already true), crop to 1080×1350 and add a frame: "My house in PETME2 Cat Town · Cat #N · @petme2", saved as a PNG download. Brand presence is one small line.
- Not found: "Not in town yet. Follow @petme2 and you'll get a house in tomorrow's episode!"

**Animation:** only the camera tween and the house bounce described above.

**Cost.** **Zero runtime cost** (no new meshes). About 80 lines of UI.

---

### 9. Fish Balloons — LATER (easy, big wow)

**What you see.** Five hot-air balloons shaped like fat cartoon fish float slowly over the city. Two cats peek out of each basket, ears just over the rim.

**Why it's shareable.** It adds height and color to the overview shots, and the balloon shadows sliding over the rooftops look expensive while costing almost nothing. "Fish in the sky" is a cat dream.

**Build spec:** body `Sphere(6, 12, 8)` scaled (1.6, 1, .9); tail `Cone(3, 4, 4)` rotated to point backward; eye: white `Sphere(.9)` + black `Sphere(.45)`; stripes 2 × `Torus(5.5, .4)` in a darker shade. Colors `#FF9F43`, `#7FB6E8`, `#F4A7B9`, `#FFC93C`, `#5BB98C`. Ropes: 4 × `Cyl(.05, .05, 4)`. Basket `B(2, 1.4, 2)` `#C98B5A`, 2 cat heads (only the head + ears part, or `CAT_SIT` at y so only the heads show). Fly height 55–75. Merge each balloon into one geometry (vertex colors) → one InstancedMesh.

**Animation:** orbit `angle = k*1.26 + anim*.015`, `r = CR*.55 + 20*sin(k)`, `y = 62 + 3*sin(anim*.5 + k)`, yaw facing the direction of travel. The tail fin wags `ry ±.15*sin(anim*1.5)`.

**Cost.** 5 instances, 1–2 draw calls; cast shadows ON (they are the point).

---

### 10. Knock-It-Off Rooftop — LATER

**What you see.** A cat on a roof edge slowly, deliberately pushes a mug toward the edge with one paw, looking straight at the camera. The mug falls... and lands softly in a flower bush. The cat looks satisfied.

**Why it's shareable.** It's a classic cat behavior, and the eye contact with the viewer is the joke. A nice close-up gag.

**Build spec:** the cat is a roof-napping cat (the `nap` cats, `k % 5 == 0`), on 1 in 40 of them (~25 at 5k houses), on cat-face houses only (flat roof top at y 2.75). Mug: `Cyl(.22, .2, .4, 10)` `#FFFFFF` + handle `Torus(.12, .04)`. Bush: `Icosahedron(.8, 0)` `#4FA65A` + 3 flower cones at the base of the house wall.

**Animation** (period 12 s): 0–5 s the mug slides from the roof center to the edge (cat yaw oscillates `±.2` = paw pushes); 5–5.4 s the cat turns its head to the camera; 5.4–6.2 s the mug falls in a parabola with a spin (rx `+= 8*dt`) into the bush, and the bush squashes (scale y .8 → 1, `back`); 6.2–12 s the mug pops back on the roof (scale 0 → 1).

**Cost.** 25 mugs + 25 bushes, animated. +3 draw calls.

---

### 11. Sunbeam Shuffle — LATER

**What you see.** On lawns, soft yellow patches of sunlight slowly slide across the grass. A cat lying in each one inches along to stay inside the light. It never gets up; it just scoots.

**Why it's shareable.** It's very real cat behavior and very calm. It works as a quiet "good vibes" moment between gags.

**Build spec:** patch `PlaneGeometry(2.6, 1.8)` flat, `MeshBasic #FFF1B8`, opacity .45, `depthWrite: false`, y .06. Cat: belly-up or `CAT_LOAF` on its side (rz PI/2). On 1 in 15 garden spots.

**Animation:** the patch moves `x' = 2.5*frac(anim/20 + hash)` along a fixed direction (the same direction everywhere, matching the sun), resetting with a .5 s fade (scale 0). The cat follows in steps: `catX = patchX` rounded down to .5-unit steps, with a quick .15 s scoot each step.

**Cost.** ~100 patches + ~100 cats, animated (cheap math). +1 draw call.

---

### 12. Cat Nap Park (hammocks) — LATER (great comment-build answer)

**What you see.** A park full of tiny hammocks between posts, each with a cat sleeping belly-up, all swaying gently in sync, plus one empty hammock with a cat underneath it, asleep on the grass instead.

**Why it's shareable.** Rows of 12 swaying sleeping cats are pure "good vibes", and the one cat that chose the ground is the joke.

**Build spec:** landmark kind `'napPark'` on a reserved spot: grass pad `Cyl(14, 14, .1)` `#9FD47F`; 12 hammocks in a 4×3 grid at 4.5 spacing. Each: 2 posts `Cyl(.1, .1, 1.8)` `#8A5A3B` 2.6 apart; sling `Cyl(.6, .6, 2.2, 8, 1, true, 0, PI)` rotated so it sags, in `#E85D8A`/`#7FB6E8`/`#FFC93C`; belly-up cat inside. Sign: `textSign('CAT NAP PARK')`.

**Animation:** sling + cat rz `= .12*sin(anim*1.2 + col*.2)` (a gentle traveling wave across columns), pivoting at the post height.

**Cost.** ~60 meshes in one Group (only built once); merge the posts. ~6 draw calls.

---

### 13. Cardboard Box Castle — LATER (landmark / comment build)

**What you see.** A castle made entirely of stacked cardboard boxes: towers of boxes, battlements made of open box flaps, a drawbridge that is a flattened box, and fish-shaped flags. Cats peek out of the holes.

**Why it's shareable.** It's the ultimate "cat version" build. It fits the town's box houses and would look great as a comment-winning reveal.

**Build spec:** base `B(14, 4, 10)` `#C99A62`; 4 corner towers = 3 stacked boxes `B(3.2, 3.2, 3.2)` each, alternating `#C99A62`/`#D6AE76`, yaw ±.1 for wonkiness; flaps on tower tops `B(3.2, .05, 1.2)` tilted .6 (4 per tower); tape strips `B(.5, .02, 3.22)` `#E9D3A8`; drawbridge `B(3, .1, 4)` tilted; flags = the street-lamp fish shape at scale .6 on `Cyl(.06)` poles; 5 cat heads in round holes (`Cyl(.5)` `#3A2A1C` + `CAT_SIT`). Text: `textSign('BOX CASTLE')`.

**Animation:** flags wag `ry ±.25*sin(anim*2 + k)`; one cat pops its head up and down out of a tower top every 6 s (y −.8 → 0 with `back`).

**Cost.** ~45 meshes in one Group. Build it like the existing `landmark()` kinds.

---

### 14. Catnip Greenhouse — LATER

**What you see.** A small glass greenhouse full of green plants, with a sign "CATNIP · PLEASE BE CALM". Outside, four cats roll on their backs in total bliss, while one serious cat sits by the door like a guard.

**Why it's shareable.** Cat owners know the catnip roll. It has a funny "guard vs. party" contrast and is brand-safe (a plant, not a product).

**Build spec:** glass `B(10, 5, 7)` `#BFE9FF` opacity .3, `depthWrite: false`; frame edges as 12 thin `B(·, .15, .15)` `#FFFFFF`; roof = 2 tilted panels; plants 20 × `Cone(.5, 1.4, 5)` greens in rows; 4 belly-up cats on the grass; 1 `CAT_SIT` guard; sign `textSign('CATNIP · PLEASE BE CALM', 7)`.

**Animation:** rolling cats: rz `= PI + .5*sin(anim*3 + k)` (rocking on their backs), legs-up paddling. The guard does not move. That's the joke.

**Cost.** ~40 meshes, 1 Group, 4 animated cats.

---

### 15. Zoomies Hour — LATER

**What you see.** Every so often, one cat in each neighborhood suddenly sprints in laps around a fish pond at 4× normal speed, with little white speed lines behind it, then stops dead and sits as if nothing happened.

**Why it's shareable.** "The 3 AM zoomies" is a top cat-owner joke, and it adds random energy to the overview shots.

**Build spec:** 1 pond per district (6). Cat `CAT_GEO`; 3 speed lines `B(.8, .04, .04)` `#FFFFFF` behind it at heights .4/.6/.8.

**Animation** (period 30 s, phase per district): 0–4 s laps at `angle = anim*5.5`, `r = 4.2` around the pond (yaw tangent, lean `rz = −.3` into the turn, bounce .25 at 16 Hz); 4–4.2 s sudden stop; 4.2–30 s `CAT_SIT`, static, facing away.

**Cost.** 6 cats + 18 lines. Negligible.

---

### 16. Cat-Ear Clouds — LATER (easy)

**What you see.** Puffy low-poly clouds drift over the city, and if you look closely, every cloud has two little cat ears.

**Why it's shareable.** A tiny "did you notice?" detail. It makes the sky part of the brand world in every wide shot.

**Build spec:** each cloud = 4 `Icosahedron(r, 0)` (r 6–10) merged + 2 `Cone(2.5, 4, 3)` ears, `#FFFFFF`, roughness 1, `castShadow` false (shadows over 5,000 houses would look dirty and cost a shadow-pass draw). 12 instances of one merged geometry, y 90–120.

**Animation:** drift `x += anim*.6` wrapped over 1,600 units; scale breathing ±2%.

**Cost.** 12 instances, 1 draw call.

---

### 17. Loaf Bakery — LATER (comment build)

**What you see.** A cute bakery with a big front window. On the shelves inside, rows of cats sit in perfect "loaf" pose, like bread on display. Sign: **FRESH LOAVES**. One "loaf" in the row is actually a real bread loaf, and one cat on the top shelf has fallen asleep belly-up.

**Why it's shareable.** "Cat loaf" is a famous pun, and the one real bread among the cats is the find-it joke.

**Build spec:** shop `B(12, 6, 8)` `#FFF4E6`, awning stripes like the café (`#E85D5D`/white), window `B(8, 3, .1)` `#9FD3FF` opacity .5; 3 shelves `B(7.6, .15, 1.2)`; 12 `CAT_LOAF` cats in assorted `CAT_COLORS` (shelf spacing 1.2); 1 bread = `B(.9, .45, .55)` `#D9A066` + 3 thin `#C47A4A` score lines. No prices, no "for sale". It's a display.

**Animation:** one loaf cat per shelf blinks via head nod (pitch ±.1 every 5 s); the belly-up one paddles its legs.

**Cost.** ~25 meshes + 14 cats. Built like the other `landmark()` kinds.

---

### 18. Find Mango — LATER (interactive)

**What you see (on the page).** A button: **Where's Mango today?** Mango has left the fountain and is napping somewhere in town (on a roof, in a box, in a circle, in a balloon basket). Tap him to win: confetti, and "Found Mango in 0:23! Can your friends beat you?"

**Why it's shareable.** It's a daily mini-game, and the time challenge gives a reason to send the link to friends.

**Build spec:** the hiding place is picked by `hash01(dayNumber)` from a list of candidate spots (roof nap spots, tinybox spots, circles, balloon baskets). Mango is placed there in the matching pose at a **normal cat scale of 1.15** (not his giant 2.6; that's the challenge), still orange `#F28C28`. Raycast on click: `raycaster.intersectObject(poseMesh)` → check `instanceId === mangoIdx`. Reuse the existing `CONF` confetti. A tiny hint after 60 s: a soft orange pulse ring around the hiding spot (`Torus`, scale `1 + .3*sin(anim*4)`).

**Cost.** Zero new instances (Mango moves into an existing pose mesh). ~60 lines of UI.

---

### 19. Pet-a-Cat — LATER (interactive)

**What you see (on the page).** Tap any cat and it purrs: three little hearts pop above it, and it flops over belly-up for 1.5 s before going back to what it was doing.

**Why it's shareable.** It makes the town feel alive and responsive. A cheap moment of joy that keeps people clicking around and exploring.

**Build spec:** raycast `catMesh` on pointer-down (InstancedMesh raycast gives an `instanceId`; with 5k instances it's fine on click, not on hover). Hearts: 3 HTML `<div>` hearts positioned with the existing `proj()` helper (no 3D needed). Override: a small map `{instanceId: tStart}`; while it's active, that cat's matrix becomes belly-up at its current position.

**Cost.** Zero new instances. One raycast per tap.

---

## 4. MUST list at a glance

| # | Idea | Seen from | Draw calls added | Instances (animated) | Effort |
|---|---|---|---|---|---|
| 1 | Mango's Water Bar (drinking fountain) | center close-up + top view | ~6 | ~190 (~70) | M |
| 2 | Sleeping Mountain cat | city overview | ~5 merged | ~16 meshes (3) | S |
| 3 | Red Dot Lighthouse | beach / mid | ~4 | ~20 (9) | S |
| 4 | If It Fits, I Sits | street close-up | 2 | ~680 (0) | S |
| 5 | Cat Circle Traps | street + plaza | 1 | ~300 (1) | S |
| 6 | Runaway Yarn Ball | overview + street | 4 | ~300 (~300) | M |
| 7 | Bus stop "NEXT NAP: 5 MIN" | street close-up | 3 | ~135 (~30) | S |
| 8 | Find Your House + postcard | interactive page | 0 | 0 | M |

**Shared foundation first:** the pose kit (`CAT_DRINK`, `CAT_SIT`, `CAT_LOAF` + the belly-up trick), +3 draw calls.

**Total for all MUST items:** about **+28 draw calls**, **~1,650 new instances**, and **~410 matrices updated per frame**, against ~5,000 cat matrices already updated every frame today. That is under 10% extra CPU per frame, with no textures loaded from the internet (only 3–4 canvas-text signs, drawn in the page with the bundled Nunito font).

---

## 5. Brand-safety and consistency notes

- **No milk river.** Most adult cats are lactose intolerant, and "cats + milk" is a myth a pet-water brand shouldn't repeat. If someone asks for it in a comment, build a "Sparkle Creek" (a blue water stream with fish-skeleton-shaped bridges) instead.
- **No cucumber-scare gags or any prank that scares a cat.** Nothing mean, nothing falls on a cat. Things that drop land in bushes.
- **PETME2 stays small:** the fountain (with its existing sign), the small pet shop, the postcard footer line. The Water Bar chalkboard says "ALL CATS WELCOME" and makes no product claims. Nothing in town is shown as "for sale", and that includes supplements, the bakery and the catnip.
- **No real people or brands, no copyrighted characters.** Strollers are pushed by generic low-poly humans (as now).
- **Follower handles** appear only as already done in episodes (name tags) and in Find Your House when the visitor types their own handle.
- **Conflict to fix in `CITY_PLAN.md`:** the "Style" row still says *"cars with cat ears"*, but the "Life on the streets" row says *"No cars."* Suggest deleting "cars with cat ears" so no future episode builds one by mistake.
- **Milestone hooks (owner to approve):** Red Dot Lighthouse at 500, Sleeping Mountain at 1,000 ("the mountain is... a cat?"), Fish Balloons at 2,500. Each is a ready-made episode headline.
