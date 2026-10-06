# Cat Town: design review (idea checker, 2026-10-06)

Input: `design-ideas.md` (designer), engine `catcity.html`, rules `CITY_PLAN.md`, previews in `previews/`.
Output: a verdict for each idea, the build list (max 8 items), and the QA checks.

---

## 0. Engine facts the verdicts are based on

These are measured from `catcity.html`, not taken from the ideas doc.

- **Center block:** plaza `Cyl(16)` top y .14. Roundabout road disc `Cyl(12)` top ~.17. Island `Cyl(8)` top .50. Lawn `Cyl(7.2)` top **.54**. Fountain base `Cyl(4.4→4.8, h1.2)` spans y .5–1.7. Blue bowl `Cyl(4.0→3.6)` at y 2.5. Water dome `r 3.2` at y 3.3 (top 6.5). `PETME2` sign at y 7.4.
- **First 6 avenues at r 14** (after the `spokeA` wobble) sit at angles **.29, 1.41, 2.38, 3.31, 4.38, 5.55**. The road is 4.4 wide and sidewalk+road 8.4 wide. So the plaza ring (r 12–16) has **6 free sectors**. Their centers are .85, 1.89, 2.85, 3.85, 4.97, 6.0. Each is about 5 units wide at r 14 before you hit a road edge.
- **House lots start at r 18.** House fronts sit about 3.5 from the road center, and the sidewalk edge is 4.2. **There is no free room on house sidewalks** for shelters or props.
- **Cameras.** Portrait 1080×1920 with vertical FOV 42°, so the horizontal FOV is only **~24°**. Things far left or right of the look direction leave the frame quickly.
  - The preview stills (`p_100`, `p_1000`, `p_5000`) all look from the sea side (+x) toward angle ~3.45 (the -x side).
  - Episode shots look from +z toward -z, steeply down. The horizon and the mountains are **not** in episode frames.
- **Fog** starts at max(320, CR×1.4) and ends at 1150. Anything at r ≥ 500 is 60–70% fog in the previews, so pale colours disappear (see `round-city.jpg`, where the mountains are almost white).
- **Per frame today:** about 5,000 cat matrices are written every frame. When `t` changes, every house is re-placed (~8 matrix multiplies × 5,000) and the whole `GROWN` list is re-walked. New features must add **no per-frame work per house or per lot**. A few hundred animated instances is fine (<5% extra).
- **Viewer quirk:** the viewer renders at `t = tOf(followers)`, so anything that pops at exactly that time has scale ≈ 0. Rule for every new item: the pop must **finish** when follower *n* moves in (start it at `unlockT(n) − d`).
- **Existing bugs seen in previews:**
  - `textSign()` cuts long text ("PETME2 PET SH", "YOUR IDEA HER").
  - Sign canvases may draw before Nunito is loaded. `catcity.html` has no `document.fonts.load` before `textSign` runs; the viewer build does.
  - New signs must be ≤ 10 characters per line or use their own canvas.

---

## 1. Verdict per idea

| # | Idea | Verdict | Why (one line) |
|---|---|---|---|
| — | Pose kit (`CAT_DRINK`, `CAT_SIT`, `CAT_LOAF` + belly-up) | **BUILD SIMPLER** | Needed by most items. But the "belly-up = CAT_GEO rotated rz PI" trick puts the cat on its ear tips, floating 0.5 above the ground. Add a real 4th geometry, `CAT_BELLY`. |
| 1 | Mango's Water Bar (drinking fountain) | **BUILD SIMPLER** | Required and on brand. As written the geometry clips: the wall top (1.04) is above the cat chins, and heads at r 5.9 sit over the wall, not the water. Drop the tongue, the splash gag, the paw crosswalks and the chalkboard ("WATER BAR · ALL CATS WELCOME" would be cut by `textSign`). Use the corrected sizes in Build 1. |
| 2 | Sleeping Mountain "Big Mochi" | **BUILD SIMPLER** | Huge "wait, is that a cat?" moment in previews and the web page. But cream `#EDE6DD` at r 540 turns into fog colour and vanishes. Use warm ginger with `fog:false`, r 500, and a footprint cleared of trees. Not visible in episode shots unless a custom shot is added. |
| 3 | Red Dot Lighthouse | **BUILD SIMPLER** | The most universal cat joke. The dot path as written crosses the tower, so move the tower to the shore edge. Drop the leg-paddle (merged geometry can't move legs). Off-frame in the default previews, so QA needs a beach still. |
| 4 | If It Fits, I Sits | **BUILD SIMPLER** | As written the loaf (.63 wide) is *narrower* than the .9 box, so the joke does not read. Use one variant only: a tiny box with an oversized loaf on top, plus one hero box on the plaza. |
| 5 | Cat Circle Traps | **BUILD SIMPLER** | The hero row at angles 2.07–2.92 runs over avenue 2 (2.38). Use 4 circles in plaza sector 1.89 with **dark** tape (white tape on the cream plaza is invisible). Drop the squares and the landmark circles. |
| 6 | Runaway Yarn Ball | **LATER** | A .08-wide thread is about 1 px from the aerial camera, so the "red line across town" does not read. It also costs ~300 animated instances. When built: thread .25 wide, max 3 events. |
| 7 | Bus stop "NEXT NAP: 5 MIN" | **BUILD SIMPLER** | No room on house sidewalks: a 1.6-deep shelter clips the house fronts and the taxi lane. Build **one hero stop on the plaza** with its own 2-line sign canvas. Drop the taxi-turnaround stops and the taxi pause. |
| 8 | Find Your House (+ postcard) | **SPLIT: postcard BUILD NOW, search LATER** | We have no real follower handles. Demo handles on a public page would look like fake residents (fake social proof), so don't put them there. Build "Save postcard" now; it needs no data. Build the search once real handles exist (see section 4). |
| 9 | Fish Balloons | **BUILD NOW (promoted)** | 2 draw calls and 5 instances. Reads in every aerial and preview shot, and the moving shadows give big wow for little cost. Needs a fixed placement so balloons never cover the fountain or Big Mochi. |
| 10 | Knock-It-Off Rooftop | LATER | Close-up only; invisible from the aerial camera. Good episode gag later. |
| 11 | Sunbeam Shuffle | LATER | A pale patch at .45 opacity on light grass is low contrast, and transparent sorting over 100 patches adds risk. |
| 12 | Cat Nap Park (hammocks) | LATER | Great answer for a comment build. Build as a `landmark()` kind when someone asks. |
| 13 | Cardboard Box Castle | LATER | Same: a comment-build landmark kind. Sign must be ≤ 10 chars ("BOX CASTLE" is OK). |
| 14 | Catnip Greenhouse | LATER | Fine and brand-safe (a plant, not a product). The sign must be shortened to "CATNIP". |
| 15 | Zoomies Hour | LATER | Cheap (6 cats). First in line for the next batch. |
| 16 | Cat-Ear Clouds | **DROP** | At y 90–120 they sit at the opening camera height (y 120) and can block the shot. From above, the ears read as bumps. Low value. |
| 17 | Loaf Bakery | LATER | Comment-build landmark. Keep "no prices, nothing for sale". |
| 18 | Find Mango | LATER | Needs click raycast + daily hiding logic, and conflicts with Mango hosting the Water Bar in video. Web-page-only mode later. |
| 19 | Pet-a-Cat | LATER | Cheap and nice for visitors (one raycast per tap). First pick for the next web-page batch. |
| — | Paw crosswalks, chalkboard, tongue, splash gag, cat-flap exit | DROP for now | They add effort without changing what reads at phone size. |
| — | "Fountain Wave" hero shot | BUILD (inside Build 1) | About 15 lines. Turned on only by `EP.fountainWave`. |

**Rule conflicts found**
- `CITY_PLAN.md` said "cars with cat ears" while also saying "No cars." **Fixed:** the cars mention is removed. The engine already has no cars.
- `CITY_PLAN.md` says the episode engine is `town2.html`, but the city is `catcity.html`. Everything here targets `catcity.html` (and `viewer.html` via `build_viewer.py`).
- The Day 1 rule "only the roundabout, fountain and Mango" is kept. Every plaza prop below unlocks at a follower count, so the Day 1 frame shows only the fountain and Mango.
- Milestones beyond "100 = City Hall" need owner approval. The numbers below (500 / 1,000 / 500-step balloons) are defaults in one constant each (`UNLOCK.redDot`, `UNLOCK.mochi`, `UNLOCK.balloonStep`), so they are easy to change.

---

## 2. Shared helpers (build these first, inside Build 1)

```js
// time when follower n (1-based) moves in; -Infinity = already there; Infinity = not in this city
const unlockT = n => n <= 0 ? -Infinity : n > F ? Infinity : (APPEAR[n-1] < 0 ? -Infinity : APPEAR[n-1]);
// pop that FINISHES when follower n arrives (works in video and in the viewer)
const popK = (t, n, d = .6) => { const t1 = unlockT(n); return t1 === -Infinity ? 1 : t1 === Infinity ? 0 : back((t - (t1 - d)) / d); };
const UNLOCK = { hostBox: 5, busStop: 10, circles: 20, redDot: 500, mochi: 1000, balloonStep: 500 };
const polar = (a, r) => [Math.cos(a) * r, Math.sin(a) * r];
const yawTo = (dx, dz) => Math.atan2(dx, dz);              // engine convention: geometry faces +z
const paint = (g, hex) => { g = g.index ? g.toNonIndexed() : g; const c = new THREE.Color(hex), n = g.attributes.position.count, a = new Float32Array(n * 3);
  for (let i = 0; i < n; i++) c.toArray(a, i * 3); g.setAttribute('color', new THREE.BufferAttribute(a, 3)); return g; };  // for vertex-coloured merges
```
- Call `await document.fonts.load('900 100px Nunito')` **before** the first `textSign` and before any new sign canvas, as `viewer.html` already does.
- **Pose kit:** four merged geometries. Use the same box/cone parts as `CAT_GEO` and the `merge()` helper. All face +z with feet at y 0.

| Pose | Parts (size → position, rotation) |
|---|---|
| `CAT_SIT` | haunch B(.55,.3,.5)→(0,.15,-.15); torso B(.5,.7,.5) rx -.35→(0,.5,-.02); head B(.48,.42,.42)→(0,1.0,.12); ears Cone(.1,.22,4)→(±.15,1.31,.10); front legs B(.12,.45,.12)→(±.13,.22,.20); tail B(.1,.08,.7) ry .9→(.30,.04,.05) |
| `CAT_LOAF` | body B(.55,.4,.95)→(0,.2,0); head B(.48,.42,.42)→(0,.45,.5); ears→(±.15,.76,.48); tail B(.1,.08,.7)→(.30,.04,-.05) |
| `CAT_DRINK` | body B(.5,.45,.9) rx .12→(0,.42,0); head B(.48,.42,.42) rx .6→(0,.40,.70); ears Cone(.1,.22,4) rx .6→(±.15,.66,.88); tail B(.1,.1,.6) rx -1.2→(0,.85,-.55); 4 legs B(.12,.3,.12)→(±.16,.15,±.3) |
| `CAT_BELLY` | body B(.5,.45,.9)→(0,.225,0); head B(.48,.42,.42) rx -.3→(0,.21,.5); ears Cone(.1,.22,4) rx PI/2→(±.15,.15,.80); 4 legs B(.12,.3,.12)→(±.16,.60,±.3) (pointing up); tail B(.1,.08,.6)→(0,.04,-.62) |

- Make one `InstancedMesh` per pose with capacity 800. Set all unused slots to `ZERO`. Use a tiny allocator: `const slot = pose => pose.used++`. After all features are built, set `pose.count = pose.used`.
- Colours: `setColorAt` from `CAT_COLORS[(n*5+3) % 9]`, where *n* = a follower index. Mango is always `#F28C28`.
- Add one more `InstancedMesh` of `CAT_GEO`, **`WALK`** (capacity 32), for every animated walking or standing extra (drinkers, the circle cat, red-dot chasers, Mango while turning).
- Static instances get their matrix once. Only the slots listed under "Animation" are written per frame.

---

## 3. BUILD LIST (in order)

### Build 1. Mango's Water Bar: the drinking fountain (REQUIRED)

**Geometry** (new static meshes; nothing existing moves):

| Part | Geometry | Position | Material |
|---|---|---|---|
| Trough wall | `Cyl(6.4, 6.4, .26, 40)` | y .67 (spans .54–.80) | `#FFFFFF` |
| Water surface | `Cyl(6.22, 6.22, .04, 40)` | y .82 (top .84) | `#7FD0FF`, roughness .2. Visible as a ring from r ~4.7 (the base edge) to 6.22. |
| Blue lip | `Torus(6.32, .10, 6, 48)` rotated x PI/2 | y .84 | `#2F5FE0` (brand blue stays on the fountain only) |
| Droplets | `Icosahedron(.16, 0)`, InstancedMesh **36** (6 arcs × 6) | animated | `#BFE9FF`, emissive `#7FD0FF` .3, no shadow |
| Ripples | `Torus(1, .035, 3, 20)` rotated x PI/2, InstancedMesh **44** | y .85 | `MeshBasic #FFFFFF`, transparent, opacity .8 |

**Spots** (18 petals; from above the city centre is a flower of cats):
- Petal *m* = 0..17 sits at angle `a_m = PI/2 + m*PI/9`. **m = 0 is Mango** (front, facing the +z opening camera). m = 1..17 are small cats.
- Small cat: `CAT_DRINK`, scale 1.15, at r **6.8**, y .54, facing the center (`yaw = yawTo(-cos a, -sin a)`). That puts the head centre at r ~6.0 over the water, with the chin just under the water line .84.
- **Active small spots = min(17, followers shown).** Fill order: m = 1, 17, 2, 16, 3, 15, … so the first cats flank Mango. **Day 1 has Mango only.**
- Colour of spot m = the colour of follower m.

**Paths** (built once per spot as `{pts, cum}` so `sampleRoad()` works):
- **In-avenue** = the first-ring avenue with the largest angle ≤ a_m (wrap around). **Out-avenue** = the next one, counter-clockwise. Cats always move counter-clockwise, like a real roundabout.
- **In-path:** along the in-avenue (`spokeA(spokes[i], r)`) from r 22 down to r 12.5 in 1.5 steps. Then an arc at **r 10.5** from the avenue angle to a_m (steps of .08 rad). Then radially in to (a_m, 6.8).
- **Out-path:** radially out to r **9.3**, then an arc at r 9.3 from a_m to the out-avenue angle, then out along that avenue to r 22. The two lanes (10.5 in, 9.3 out) never cross.
- **Height on any path:** `y = .16 + .37*smoothstep(8.6, 8.0, r) + .25*max(0, 1 - |r - 8.3| / .4)`. That is road height outside, lawn height inside, and a small hop onto the island.

**Animation** (pure function of `anim`; spot period P = 24 s; `u = (anim + hash01(m*41+3)*P) % P`):

| u (s) | Beat | Mesh |
|---|---|---|
| 0–.3 | pop in at the path start, `back` ease | WALK |
| 0–7 | walk in: `sampleRoad(in, u/7*len)`, yaw = path direction, bounce `|sin(anim*11+m)|*.15` | WALK |
| 7–15 | drink. Whole-instance pitch `.05*sin(anim*14+m)` (laps). 2 ripples at the nose point (r 5.75, y .85): `f = frac(anim*1.6 + m*.37 + q*.5)`, scale `.15+.55f`, ZERO when f > .92 | CAT_DRINK |
| 11–11.8, only if m % 3 == 0 | **deadpan glance**: standing pose, yaw turns toward `camera.position`, clamped to ±.7 rad from facing the fountain, then back | WALK |
| 15–15.5 | turn to the out-path direction (yaw ease) | WALK |
| 15.5–22 | walk out, `sampleRoad(out, …)`. First 1.5 s: happy hop, bounce .22 | WALK |
| 22–22.4 | scale to 0 | WALK |
| 22.4–24 | empty (so the ring is never perfectly full; that looks alive) | — |

Each frame, every slot writes its matrix to exactly one of WALK or CAT_DRINK and `ZERO` to the other.

**Mango (m = 0)**, period 24, phase 0:
- **Sit:** `CAT_SIT` scale 2.6 at (PI/2, r 7.6), y .52, facing **outward** (to the camera) for u 0–16. Head-watch: whole-instance yaw `±.35*sin(anim*.6)`.
- **Turn:** standing `CAT_GEO` (WALK) for 16–16.6, yaw lerps to face the center.
- **Drink:** `CAT_DRINK` scale 2.6 at r **7.4**, extra pitch +.15, for 16.6–22.6. Ripples ×2 size.
- **Turn back:** 22.6–23.2. Then sit again.
- **Remove the old roundabout patrol:** catMesh slot 0 = `ZERO`. The City Hall Mango statue stays.

**Droplet arcs:**
- Arc k = 0..5 sits at angle `PI/2 + PI/18 + k*PI/3`, which is always between two petals.
- Droplet i = 0..5: `f = frac(anim*.7 + i/6)`, `r = 5.5f`, `y = 6.8(1−f) + .84f + 6f(1−f)`. This starts above the dome top (6.5) and clears the bowl rim (y 3.65 at r 4.0).
- One extra ripple per arc at r 5.5, using the same f rule. That makes the 44 ripples: 2 × 17 + 2 (Mango) + 6 + 2 spare.
- The existing dome breathes: `water.scale.y = 1 + .02*sin(anim*3)`.

**Fountain Wave** (only when `EP.fountainWave = t0`):
- For anim in [t0, t0+6], every active spot plus Mango is forced into the drink state at its spot. A cut hides the jump.
- Spot q (in order of angle from Mango, counter-clockwise) shows the standing pose from `t0+3+q*.12` for .5 s, so heads go up like a stadium wave. Mango lifts last.

**Growth:** the water ring, Mango and the droplets are there from Day 1. Small spot m is active once `followersShown ≥ its fill-order rank`; use `unlockT(rank) ≤ t`.
**Cost:** ~120 matrix writes per frame, 6 draw calls (+3 pose meshes shared).

### Build 2. Cat Circle Traps (row + one exception)

- **Hero row**, plaza sector 1.89:
  - 4 circles at r **14.6**, angles **1.70, 1.83, 1.96, 2.09**.
  - Tape: `Torus(.75, .05, 4, 24)` rotated x PI/2, `MeshBasic #3B3B44` (dark, so it shows on the cream plaza), y .16. One InstancedMesh for all tape; garden tape uses instance colour `#FFFFFF`.
  - Cats 0–2: `CAT_SIT` 1.15 at each circle centre, **all the same yaw**, facing outward (`yawTo(cos 1.83, sin 1.83)`).
- **The exception (circle 4, angle 2.09):**
  - Period 20 s. A WALK cat starts at the point 6 units along the tangent toward larger angles (ends on avenue 2's sidewalk).
  - 0–4 s: walks a straight line into the circle (bounce .1).
  - 4–4.4: turns to the row's yaw.
  - 4.4–16: `CAT_SIT`, row complete.
  - 16–16.4: turns. 16.4–19.6: walks back out. 19.6–20: scales to 0.
- **Garden circles:** in the gardens block, a `tree` item becomes `circle` when `hash01(i*53 + k*7 + 1) < .15`. Do **not** change the `kinds` array, so other gardens stay where they are.
  - White tape `Torus(.95, .05, 4, 24)` at y .1. `CAT_SIT` 1.15 in the centre, yaw `hash01(i*7+k)*6.28`.
  - Uses `grown(…, o.t)` so it appears with the district.
- **Growth:** the hero tape pops at `UNLOCK.circles` (20). Cat c (0..2) pops at 20 + c. The exception cat runs from 23.
- **Cost:** ~40–50 static rings and cats at 5,000; 1 animated cat; +1 draw call.

### Build 3. If It Fits, I Sits (tiny boxes)

- **Unit:**
  - Box `B(.55, .40, .55)` `#C99A62` at y .20.
  - 2 flaps `B(.55, .03, .30)` `#BC8C55` at (0, .42, ±.38), rx ±.6 (open outward).
  - Cat `CAT_LOAF` **scale 1.3** at y .30, sunk into the box. The cat is .72 × 1.24 on a .55 box, so it clearly overflows on every side.
- **Hero box:**
  - Plaza sector 2.85, r 14.2, base y .14.
  - Cat `CAT_LOAF` scale **1.6**, colour `#8E8E9A`.
  - Yaw shift: `+.15` for 1 s every 9 s (`frac(anim/9) < .11`). This is the only animated box.
- **Garden boxes:** a `tree` item becomes `tinybox` when `.15 ≤ hash01(i*53 + k*7 + 1) < .30`. Uses `grown(…, o.t)`.
- **Growth:** the hero box pops at `UNLOCK.hostBox` (5). Garden boxes appear with their garden.
- **Cost:** ~40 boxes, 80 flaps and 40 cats at 5,000, all static. +2 draw calls.

### Build 4. Big Mochi: the sleeping mountain cat

- **Group** at `polar(3.45, 500)` = (−476.4, 0, −151.8). `group.rotation.y = atan2(-x, -z)`, so local +z faces the city.
- **All materials** are `MeshStandardMaterial({ flatShading: true, roughness: .95, fog: false })`, with no cast shadow. The colours are pre-hazed so they look atmospheric but stay readable through the fog.
- **Parts** (local coordinates):
  - **Body:** `Icosahedron(40, 2)` scaled (1.35, .55, 1.0) at (0, 14, 0).
    - Non-indexed with vertex colours: a face is stripe `#DDA06A` when `sin(cx*.16) > .55 && cy > 0` (cx, cy = face centroid before scaling). Otherwise body `#F2C9A0`.
  - **Head:** `Icosahedron(17, 1)` scaled (1, .9, .95) at (44, 16, 22), `#F2C9A0`.
  - **Ears:** `Cone(6, 10, 4)` at (36, 31, 22) rz .35 (up), and the flopped ear at (54, 26, 22) rz −1.1.
  - **Closed eyes:** `B(5, .8, .8)` `#7A5A48` at (40, 17, 38.5) rz .25 and (50, 17, 37.5) rz −.25.
  - **Nose:** `Cone(1.6, 2, 3)` pointing +z, `#E58FA0`, at (45, 13, 39).
  - **Tail:** `Torus(46, 6, 6, 24, PI*1.1)` rotateX(+PI/2), scaled x 1.3, at (0, 5, 0), `#DDA06A`. It wraps the front from −x to the head side.
  - **Paw:** `B(10, 6, 14)` `#F2C9A0` at (30, 3, 36).
  - **Zzz:** one merged Z geometry. Top and bottom bars `B(8, 1.2, 1.2)` at y ±5; diagonal `B(1.2, 12.8, 1.2)` rz −.675. White, `fog:false`. InstancedMesh(3).
- **Trees:** countryside trees within **75** units of the centre get removal time = Mochi time. In still mode with F ≥ 1000, give them a ZERO matrix.
  - Do the check **after** `rnd()` is called for the tree scale and type, so the random sequence for all other trees, palms and boats does not change.
  - Mountains overlapping the back of the body are fine; it reads as the cat lying at the foot of the mountains.
- **Animation:**
  - Body breathes: `scale.y = 1 + .03*sin(anim*1.1)`. The head rises `+.6*sin(anim*1.1)`.
  - The flopped ear flicks rz −1.1 → −.6 → −1.1 over .4 s every 7 s.
  - Z letter k: `f = frac(anim*.25 + k/3)`, position = (44, 34, 22) + (10f, 30f, 0), scale `1.2*sin(PI*f)`.
- **Growth:** rises from y −50 to 0 with `ease` over 2 time units, finishing at follower `UNLOCK.mochi` (1,000). Hidden before that.
- **Episode use:** episode shots never look at it. For the 1,000-followers episode, add an `EP.shots` entry: p0 (330, 95, 120) → p1 (150, 60, 40), look at (−476, 20, −152).
- **Brand:** generic cat; no leaf on the head, no bus shape, nothing like known film characters.
- **Cost:** ~6 draw calls, 4 animated meshes, 3 Z instances.

### Build 5. Red Dot Beach (lighthouse + laser dot)

- Let `cx = coastAt(60)` ≈ 209.2. The **lighthouse** sits at (cx + 25, −.4, 60), on a rock `Cyl(4, 4.5, 2, 10)` `#B8B0A0` at y .2.
- **Tower:**
  - `Cyl(2.2, 3.0, 18, 10)` `#FFFFFF` at y 9.
  - 3 bands `#E85D5D` (salmon, *not* the dot red), height 1.6, at y 4 / 9 / 14, radius = tower radius at that height + .06.
  - Gallery `Cyl(3.2, 3.2, .4, 10)` `#3B3B44` at y 18.2. Lamp room `B(3, 2.4, 3)` `#9FD3FF` at y 19.6.
  - Merge into one vertex-coloured geometry with `paint()`.
- **Laser:**
  - Body `Cyl(.6, .6, 4.5, 10)` rotateX(PI/2) `#3B3B44` at (lx, 21.4, 60). Every frame, `lookAt(dot)`.
  - Tip `Cyl(.35, .35, .3)` `#FF2A2A`, emissive 1, at local z +2.4.
  - Beam: `Cyl(.08, .08, 1, 6)` rotateX(PI/2).translate(0, 0, .5). `MeshBasic #FF2A2A`, opacity .35, `depthWrite: false`. Positioned at the tip, `lookAt(dot)`, `scale.z = distance`.
- **Dot:**
  - `Cyl(1.3, 1.3, .04, 20)` `MeshBasic #FF2A2A` at y .06.
  - Halo `Cyl(2.2, 2.2, .03, 20)`, same colour, opacity .3, at y .05.
  - **Pure `#FF2A2A` is used nowhere else in town.**
- **Dot path:** `z = 70 + 28*sin(.47τ) + 7*cos(1.7τ)`, `x = coastAt(z) + 5 + 8*sin(.9τ) + 3*sin(2.3τ)`, with τ = anim. This stays on flat sand, x from cx−6 to cx+16, and never reaches the tower.
- **Chasers:**
  - 5 WALK cats. Cat k is at `D(anim − .35 − .3k)` + a sideways offset `(k%2 ? 1 : −1)*.7k`, with yaw toward `D(anim)`.
  - Cat 0 pounces every 3 s: `y = 1.0*sin(PI*q)` with `q = (anim % 3)/.5` (for q ≤ 1).
  - Cat 2 butt-wiggles: yaw `+= .12*sin(anim*22)` while `|D − pos| < 3`.
- **Quitter:** `CAT_BELLY` 1.15 at (cx + 14, 0, 50). Whole-body roll `rz = .08*sin(anim*2)`.
- **Palms** within 10 units of the lighthouse: ZERO matrix, set after their `rnd()` calls.
- **Growth:** everything pops at `UNLOCK.redDot` (500). Hidden before that.
- **Cost:** ~6 draw calls, ~10 matrix writes per frame.

### Build 6. Fish Balloons (promoted from LATER)

- **Balloon geometry** (two merged geometries, nose along +z):
  - **(a) Instance-coloured shell:** body `Sphere(6, 12, 8)` scaled (.9, 1, 1.6); tail `Cone(3, 4, 4)` pointing −z at z −11; 2 stripe rings `Torus(5.5, .4)` at z ±3.
    - Vertex colour white (1,1,1) on the body and tail, and .75 grey on the stripes, so the instance colour × vertex colour makes darker stripes.
  - **(b) Fixed-colour parts** (vertex colours, instance colour white):
    - Eye whites `Sphere(.9)` at (±4.6, 1.5, 5.5); pupils `Sphere(.45)` `#1B2333` at (±5.3, 1.5, 5.8).
    - 4 ropes `Cyl(.05, .05, 4)` `#3B3B44` at (±1, −8, ±1). Basket `B(2, 1.4, 2)` `#C98B5A` at y −10.7.
- **Basket cats:** 2 `CAT_SIT` cats, scale 1.0, at (±.45, −11.2, 0). Ears just above the rim. Updated with the balloon each frame.
- **Colours** k = 0..4: `#FF9F43, #7FB6E8, #F4A7B9, #FFC93C, #5BB98C`. Shell casts shadow (the moving shadows are the point).
- **Placement:**
  - `ANG = [2.25, 2.75, 3.95, 4.45, 4.95]`. This keeps them out of the opening camera's line to the fountain and off Big Mochi in `p_1000` / `p_5000`.
  - `angle = ANG[k] + .06*sin(anim*.05 + k)`, `r = clamp(CR*.7, 60, 240) + 12*sin(2.1k)`, `y = 56 + 8*(k%3) + 3*sin(anim*.5 + k)`.
  - Yaw = the counter-clockwise tangent, plus a wag `.1*sin(anim*1.5 + k)`.
- **Growth:** balloon k pops at follower `UNLOCK.balloonStep*(k+1)` (500, 1,000 … 2,500).
- **Cost:** 2 draw calls (+shadow), 5 + 10 cat instances, 20 writes per frame.

### Build 7. Bus stop "NEXT NAP / 5 MIN" (one hero stop)

- **Group** at `polar(.85, 14.2)`, y .14, `rotation.y = yawTo(cos .85, sin .85)` (local +z faces outward, toward the cameras).
- **Shelter** (local coordinates):
  - Back panel `B(4, 2.4, .12)` `#9FD3FF` at (0, 1.34, −.6). Roof `B(4.4, .2, 1.6)` `#FFC93C` at (0, 2.64, 0).
  - 4 posts `Cyl(.08, .08, 2.5, 6)` `#3B3B44` at (±1.9, 1.39, ±.6).
  - Bench `B(3.6, .15, .7)` `#C98B5A` at (0, .64, −.2) on 2 legs `B(.12, .5, .6)` at (±1.6, .39, −.2).
  - Merge with `paint()` into one mesh.
- **Sign:**
  - Post `Cyl(.06, .06, 3)` at (2.7, 1.5, .4). Board `PlaneGeometry(2.4, .9)` at (2.7, 2.9, .42), facing +z, single-sided.
  - **Own canvas** 1024×384: white roundRect, 14 px border `#1B2333`, text `#1B2333` 900 150px Nunito. Line 1 "NEXT NAP" at y 140, line 2 "5 MIN" at y 300. Draw it after the font is loaded.
  - **Not** in `signs[]`; it does not turn to face the camera.
- **Sleepers** (bench top y .86 local):
  - `CAT_LOAF` 1.15 at (−1.1, .86, −.2).
  - `CAT_LOAF` 1.15 at (0, .86, −.2), yaw .5.
  - `CAT_BELLY` 1.15 at (1.1, .86, −.2).
  - Breathing `scale.y × (1 + .04*sin(anim*1.4 + k))`. The belly cat rolls `rz ±.05*sin(anim*6)` for 1 s every 8 s.
- **Growth:** the shelter and sign pop at `UNLOCK.busStop` (10). Sleeper c pops at 10 + c.
- **Dropped:** taxi-turnaround stops (no room) and the taxi pause. Never add a cat-shaped bus, rain or umbrellas; that keeps it far from any famous film bus-stop scene.
- **Cost:** ~4 draw calls, 3 writes per frame.

### Build 8. "Save postcard" on the web page (no handles needed)

- **Where:** `viewer.html` shell. Add `<button id="postcard" type="button">Save postcard</button>` in the first `.row` of the dock. The logic goes in `viewer_loop.js` (inlined by `build_viewer.py`, so `renderer`, `$`, `tOf`, `cur` and `ANIM` are in scope). **No changes to video mode.**
- **On click:**
  1. Call `controls.update()` and `window.renderFrame(tOf(Math.round(cur)), ANIM)`.
  2. Create a 2D canvas 1080×1350.
  3. Draw `renderer.domElement` cover-cropped into the top 1080×1220.
  4. Fill the bottom 130 px band white. Left: "Cat Town · " + `$('countL').textContent` in 900 40px Nunito `#1B2333`. Right: "@petme2" in 800 30px `#2F5FE0`. This is the only brand mark, kept small.
  5. If `navigator.canShare?.({ files })`, share it as a PNG. Otherwise download it as `cat-town-postcard.png`.
- **Cost:** zero render cost.

### Also fix while in the file (small; not a build item)

- `textSign()`: shrink the font until the text fits (start at 104 px, step −6, minimum 56) instead of cutting letters. This fixes "PETME2 PET SH" and "YOUR IDEA HER".
- In `catcity.html`, add `await document.fonts.load('900 100px Nunito')` before the first sign is drawn.

---

## 4. Find Your House: data decision

- **Decision: defer the handle search.** We have no list of real follower handles yet.
- **Don't use made-up handles on the public page.** They would look like fake residents or fake social proof, which is a brand and trust risk.
- **When to build:** once the owner can export handles (Instagram API or a manual list). Use only exact-match search, with no browsable list of followers. Show only public handles, and honour any "remove me" request.
- **Testing before then:** the builder may use `?demo=1` with handles `demo_cat_001…` and a visible red "DEMO DATA" badge. This is never linked or published.
- **Today:** "Save postcard" (Build 8) gives visitors something to share without any data.

---

## 5. QA acceptance checks

Render each still with `catcity.html` and the existing JSON (`previews/p_day1.json`, `p_100.json`, `p_1000.json`, `p_5000.json`, `p_1000street.json`). Add these new close-up stills (same JSON shape, `still: {pos, look}`, with `followersBefore` 1000 unless noted):

| Still | pos | look |
|---|---|---|
| `q_fountain` | (0, 18, 32) | (0, 1, 2) |
| `q_fountain_day1` (followersBefore 0) | (0, 18, 32) | (0, 1, 2) |
| `q_busstop` | (17.2, 7, 19.5) | (9.4, 1.6, 10.6) |
| `q_circles` | (−8.4, 9, 24.6) | (−4.7, .5, 13.8) |
| `q_box` | (−21.3, 5, 5.6) | (−13.7, .6, 3.6) |
| `q_beach` | (290, 34, 122) | (214, 1, 70) |

**For every item:**
- No console errors.
- Two renders of the same `t` give identical pixels (no `Math.random()` in `renderFrame`).
- The `p_5000` frame time is no more than 10% above the current engine (SwiftShader, 1080×1920).

| Build | Must be true |
|---|---|
| 1 Water Bar | **Day 1** (`p_day1`, `q_fountain_day1`): blue-lipped water ring around the fountain, droplet arcs, Mango big and orange at the front, **no other cats**. **q_fountain** (1,000): 17 small cats + Mango around the ring; drinking cats have heads down, chins at the water, no body inside the white wall; ripples at noses; ≥ 1 cat in a "glance" pose at t = 11.4 for some phase. **Street** (`p_1000street`): a ring of cats visible around the fountain. **Video check:** at t = 0, 6, 12, 18 the ring is never empty and never perfectly full; cats enter only on the r 10.5 lane and leave on r 9.3, always counter-clockwise; with `EP.fountainWave = 2`, every cat is drinking at t 2–5 and heads lift in order around the circle. Mango's old patrol on the road is gone. |
| 2 Circles | **Day 1:** no tape on the plaza. **q_circles** (≥ 23 followers): 4 dark circles on the cream plaza, not on the road; 3 cats sitting with the same yaw; the 4th cat walks in from the avenue and sits (t = 0 → 5). **p_1000 / street:** a few white circles with one sitting cat each in gardens. |
| 3 Tiny boxes | **Day 1:** no box. **q_box:** a grey loaf clearly larger than its small box on the plaza; flaps visible. **Street / p_1000:** a few small boxes with overflowing cats between houses; no box overlaps a road, lot or pond. |
| 4 Big Mochi | **p_100:** not visible (only mountains). **p_1000 and p_5000:** a ginger sleeping cat (head, ears, closed eyes, tail) reads as a cat in front of the mountains, around screen y 550–720, not under the counter; no trees poking through it; "Z" letters visible. **Viewer:** slider 900 → 1,000 shows it rise. |
| 5 Red Dot | **p_100 / p_day1:** nothing on the beach. **q_beach** (1,000): white/salmon lighthouse at the shore, a bright red dot on the sand with a faint beam from the laser, 5 cats chasing (one mid-pounce at some t), 1 belly-up cat. The dot never passes under the tower; no palm through the tower. **p_5000:** the red dot is visible as a red speck near the bottom-right of the beach. |
| 6 Balloons | **p_day1 / p_100:** none. **p_1000:** 2 balloons. **p_5000:** 5 balloons with shadows on the city; none covers the fountain or Big Mochi; 2 cat heads per basket are visible in the viewer close-up. **Opening shot** (episode t = 0–2): no balloon over the fountain. |
| 7 Bus stop | **Day 1:** absent. **q_busstop** (≥ 13 followers): yellow-roof shelter facing outward; sign reads "NEXT NAP" / "5 MIN" fully (no cut letters); 2 loaf cats + 1 belly-up cat on the bench; nothing clips a road or house. **Street:** shelter visible at the plaza edge. |
| 8 Postcard | **Viewer** (desktop and 390 px-wide phone): button visible, no layout break; the PNG is 1080×1350, shows the current view, the footer reads "Cat Town · N cats · day D" and "@petme2", with no other branding. |
| Fixes | Every landmark sign shows the full text ("PETME2 PET SHOP", "YOUR IDEA HERE?") in Nunito. |

**Brand checks across all stills:**
- `#FF2A2A` appears only on the dot, the laser tip and the beam.
- PETME2 appears only on the fountain sign, the pet shop and the postcard footer.
- No cars, no milk, no prices or "for sale", no supplements, no text over 4 words on any 3D sign, no real people or brands.

---

## Summary

I checked all 19 ideas against the engine and rules. **Build now, in order:**
1. Water Bar fountain (required), with the geometry corrected so cats actually drink.
2. Circle traps.
3. Tiny boxes.
4. Big Mochi.
5. Red Dot Beach.
6. Fish Balloons (moved up from LATER).
7. One hero bus stop.
8. A "Save postcard" button.

Every item has exact sizes, positions and the follower count it appears at. Day 1 still shows only the fountain and Mango. Together they add under 5% per-frame cost.

- **Find Your House:** search deferred until we have real handles; no fake handles in public.
- **Later:** yarn ball, zoomies, pet-a-cat and the comment-build landmarks.
- **Dropped:** cat-ear clouds.
- **Bugs to fix:** sign text is cut and the sign font may not be loaded.
- **`CITY_PLAN.md`:** "cars with cat ears" removed.
