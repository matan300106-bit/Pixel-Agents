# Review: rule-v1 "Top comment? We build it." (cut1.mp4)

**Verdict: NEEDS FIXES.** None of the fixes needs an engine change. All of them are cheap: cameras, overlay, timing and gain.
**Virality score: 6.5 / 10.** It can reach 8 after fixes 1-5.

The structure is right:
- The rule is the hook.
- The reveal is honest (the match cut).
- The goal shot is strong.
- The loop is clean.

What holds it back:
- The hook frame looks like a product shot (fountain + feeder), and frame 0 has no text.
- The payoff build is weak and mis-framed.
- The Mango beat carries a misleading EXAMPLE stamp.
- The ending sits on a near-static 2 s stretch before the CTA.

---

## Tech facts (measured)

| Item | Value |
|---|---|
| Container | H.264 High, yuv420p, 1080x1920, 30 fps, 546 frames, 18.20 s, ~10.1 Mb/s |
| Audio | AAC stereo 48 kHz, 192 kb/s |
| Loudness | **-16.1 LUFS integrated** (edge of the -14 to -16 target), LRA 1.8 LU, true peak -4.8 dBFS (no clipping) |
| Black frames | none (blackdetect d=0.05) |
| Silence | none over 0.3 s at -40 dB |
| Hard cuts (scene > 0.25) | 3.50, 5.97, 7.90, 9.90, 12.60 |
| Loop | f0000 vs f0545 mean diff **0.24** (f0544: 1.04). Audio: head -28 dB, tail -33 dB, so no click |
| Badge | white pill top at y≈227; number + "cat · Day 2" pill end ≈ y 430; headline starts ≈ y 460 |
| Low-motion stretch | 12.9-14.6 s (frame-diff 0.5-1.5, near static); 8.3-8.9 s is also low (0.76) |
| Voice | L1 0.15-1.50, L7 "Let's build the city together." 10.10-11.39 (inside the goal shot 9.9-12.6), CTA 15.00-17.48 |

---

## Checklist (plan section 9)

| # | Item | Result | Evidence |
|---|---|---|---|
| 1 | Spec | **FAIL (marginal)** | Everything passes except loudness: -16.1 LUFS is 0.1 LU outside the range. There is 4.8 dB of peak headroom, so add +1.5 dB to reach about -14.6. |
| 2 | Frame 0 = lot sign; headline by 0.2 s | PASS (with note) | The sign is centered in f0000. The headline is fully in at f0003 (0.10 s). **But f0000 itself has no text** (it is the auto-thumbnail and the first frame some feeds show). See fix 1. |
| 3 | Muted 1.5 s explains comment → build | PASS (weak) | The headline plus the "YOUR IDEA HERE?" sign carry the idea. However, the largest objects in the frame are the PETME2-labelled fountain (top-left, x 0-180) and the feeder (right). Mango is a 30 px orange speck, and the bottom 40 % (y 1150-1920) is empty grass. |
| 4 | Catchphrase by 1.5 s; payoff over goal shot | PASS | 0.15-1.50 s; 10.10-11.39 s within 9.9-12.6 s |
| 5 | Badge always visible, y 220-500, no overlaps | PASS | Visible in all 546 frames. y 227-430. The headline starts at about 460 and the card at about 800. |
| 6 | Counter honest | PASS | Shows "1" everywhere. Shows "1,000 cats · THE GOAL" only in 9.9-12.6. |
| 7 | EXAMPLE on demo card and build; handles example.*; statue only in its segment | PASS (with issue) | The stamp is on the card (3.5-5.75) and on the build (5.97-7.9). All handles are example.*. The statue appears only in 5.97-7.9. **Issue:** the stamp stays up through 7.9-9.9, but that shot is the Mango close-up and **has no statue in it**. The stamp sits next to Mango (x≈90-290, y≈1090), so it reads as "Mango / this footage is fake". The planned deviation (build on screen through the review beat) was not actually executed. |
| 8 | Card scrolls to winner, crown, likes roll; inside x 60-940 | PASS (minor) | Scroll goes lior 31 → dan 54 → anna. The "MOST LIKED" crown pill appears at 5.0. Likes roll 53 → 81, but the card fades at 5.75 **before reaching 87**. Card x ≈ 90-940. |
| 9 | Statue pops on the sign's lot with a cut/flash hiding the swap; tag in safe x | **FAIL (partial)** | The cut at 5.97 lands on a low, ground-level angle facing a tree line, so the lot, the cones and the town are not visible and nothing ties it to the hook's sign. From 5.97 to ~6.2 "BUILT!" sits over empty grass and trees before anything grows. The statue then reads as a mustard block with ears, small in the frame. The tag "@example.anna built the Mango Statue" is legible and sits at x≈300-860 (pass). |
| 10 | Mango on screen and turns; fountain front never the focus | **FAIL** | Mango turns at about 9.4 (pass). But in the hook (0-1.6) and the loop end (17.4-18.2), the fountain with the "PETME2" print and the feeder are the two biggest objects in frame, framed like a product hero shot. In 3.5-5.9 they also sit directly behind "MOST LIKES WINS". |
| 11 | Goal ≥2.5 s; match cut to the empty town | PASS | 9.9-12.6 (2.7 s). The cut at 12.6 uses the same camera. |
| 12 | Visual change ≤3 s; no static >3 s | PASS (weak) | The longest gap between changes is 12.6 → 14.75 (2.15 s). Inside it the camera is nearly still (frame-diff about 0.5-1.5) and the shot is an aerial of trees. It is the dullest 2 s, placed right before the CTA. |
| 13 | One spoken CTA; follow only on screen; "24 h" on screen | PASS (note) | The only spoken CTA is "So comment what we build first". "Follow to see it built" is small text from 16.7. "Most likes in 24 h wins" is shown 15.3-16.7 **only (1.4 s)**, then replaced. |
| 14 | Safe zone, headline ≤6 words, no caption duplicates | PASS (minor) | All text sits in x 60-940, y 227-1450. All headlines are 6 words or fewer. In 14.75-17.5 the caption "So comment what we build first" half-duplicates the headline "COMMENT WHAT WE BUILD". |
| 15 | No product names, prices, links or sales lines | PASS | The goal town shows "TOY SHOP". There are no prices or links. The "PETME2" print on the fountain is the engine asset and the brand name is allowed, but see #10. |
| 16 | Loop diff <1.0; posting package exists | **PASS / FAIL** | The loop diff is 0.24 (pass). The episode folder contains only `viral-plan.md`: there are no caption, pinned-comment or cover files. |

---

## Top fixes, ranked by impact on reach

1. **Put the hook text on frame 0 and on the last frame (hook + loop + thumbnail).**
   - Today f0000 is textless, and the last 0.3 s fades the CTA to nothing.
   - Show "TOP COMMENT → WE BUILD IT" from **0.00 s** with no pop-in (or a 2-frame scale from 0.95 to 1.0).
   - In the end beat, swap the headline at **17.5 s** from "COMMENT WHAT WE BUILD" to "TOP COMMENT → WE BUILD IT". Hold it to the last frame, so f0545 = f0000 *with* text.
   - The loop then reads "...Weirder is better. / TOP COMMENT → WE BUILD IT" visually as well as aurally. The first frame works as the cover and as the first-impression frame in feeds.

2. **Reframe the hook and loop camera so the sign and Mango are the hero, not the fountain and feeder.**
   - Same lot, but **lower the camera to y≈3 and swing it about 25-30° around the lot**, so the fountain leaves the frame or sits small and soft behind the sign.
   - Bring the **sign up to y≈700-1000**, which fills the empty lower 40 %.
   - Aim so Mango sits just right of the sign post, at least 3x his current size. A push-in from 30 → 18 units does both.
   - Apply the identical pose to the last 0.4 s (keep anim = T - 18.2) so the loop stays under 1.0.
   - This is the biggest "is this an ad?" scroll-away risk in the first second.

3. **Fix the build payoff (5.95-7.9).**
   - Cut at 5.95 to a camera **outside the lot looking in at about 25° down, 30-35 units out**, so cones, road and the town centre are visible behind the statue. That tells the viewer "the sign became this".
   - Start "BUILT!" at **6.25 s**, the moment the statue starts growing, not at 5.95 over empty trees.
   - Move the statue pop closer to the voice: have L4 "...and we build it!" end on the pop (shift L4 to 5.75-6.45, `newBuild.at` 6.20).
   - Add a 1.0 → 1.08 scale punch-in (camera dolly 4 units) on the pop.
   - Let the card's likes reach **87** before it fades (slide-out at 5.9 instead of 5.75).

4. **Remove the EXAMPLE stamp from the Mango shot, or actually put the statue in it.**
   - Option A (preferred, doable): frame the review beat from the statue lot toward Mango: camera behind/beside the statue at `[lot + toward-centre·8, 4, ...]`, looking at Mango, with the statue's base in the left third. The EXAMPLE stamp then sits on the statue and Mango "reviews" it.
   - Option B: end the stamp at 7.9 together with the statue.
   - The current state makes the only real character look fake.
   - Also start the review voice on the cut (L6 at 7.95, as now), but trim the hold so Mango's turn (about 9.3-9.5) lands on "ten out of ten" (9.0-9.7). Retime the turn with anim offset so it starts at about 8.95.

5. **Kill the dead stretch 12.6-14.75 and give "24 h" real screen time.**
   - Keep the match cut at 12.6, but start the dive at **13.4 s** instead of 14.75: a slow push and descent toward the lot. The "0 BUILDINGS" reveal then has motion and lands on the sign earlier.
   - Optionally trim 0.3 s from the gap between L7 and L8 (start L8 at 12.65) to tighten pacing to about 17.9 s.
   - Keep "Most likes in 24 h wins" on screen **15.3-17.5** (2.2 s). Put "Follow to see it built" *under* it from 16.7 rather than replacing it.

6. **Loudness: add +1.5 dB to the master** (from -16.1 to about -14.6 LUFS, true peak about -3.3 dBFS). TikTok and IG normalise, but sitting at the bottom edge loses punch against neighbours.

7. **Make the goal-town signs rewatchable.** Today "CAT AIRPORT", "CAT CAFE" and "FISH MARKET" are about 20 px tall, so they are unreadable at phone size. In 11.4-12.6 push the goal camera about 40 % closer to the centre ring, so 3-4 signs reach 40 px or more. Use the *same* end pose for the empty-town shot at 12.6 so the match cut still holds.

8. **Small text polish.**
   - End headline: "COMMENT <y>YOUR IDEA</y> 👇". It is more personal and does not duplicate the caption. Alternatively hide the caption's first sentence and show only "Weirder is better."
   - Make "(the cat version 🐱)" 64 px. It is about 30 px now and hard to read.

9. **Posting package files.** Save the IG and TikTok captions plus the pinned comments from plan section 8 as files in `episodes/rule-v1/`. Export a clean cover from the fixed frame 0 (sign + headline + badge, no captions).

---

## What works (keep for the daily template)

- The rule is spoken and shown by 1.5 s, in the owner's exact words.
- The badge is always on, never overlaps anything, and the counter is honest ("1,000 · THE GOAL" only in the goal shot).
- The comment card is native-looking and readable; the scroll-to-winner plus MOST LIKED pill is clear.
- The goal shot (9.9-12.6) is the best frame in the video. The **match cut to the empty town at 12.6 is the strongest moment**: honest, and it creates the stakes.
- The loop is technically seamless (diff 0.24). Voice is clear, the English is simple, the lines are short, and there is one spoken CTA.

---

## Re-check (cut 2): /tmp/ct2/v/cut2.mp4

**Verdict: READY** (one optional camera tweak below). **Virality score: 7.5 / 10.**
The score went up because:
- The hook text is on frame 0.
- The build payoff now reads as "the lot became this", and Mango is in the shot.
- The misleading stamp on Mango is gone.
- The CTA has time to land.
The remaining cap on the score is the engine: Mango is faceless and the statue is a plain block. Those are engine asks, not edit fixes.

### Tech (measured)
- 1080x1920, 30 fps, 546 frames, 18.20 s, H.264 + AAC stereo.
- **-15.1 LUFS** (pass), true peak -4.8 dBFS. No black frames.
- Cuts at 3.50, 5.97, 7.90, 9.90 and 12.60.
- **Loop diff f0000 vs f0545 = 0.14** (pass). Text is identical on both frames.

### Checklist (only the items that changed)

| # | Cut 1 | Cut 2 | Evidence |
|---|---|---|---|
| 1 | FAIL (marginal) | **PASS** | -15.1 LUFS |
| 2 | PASS (note) | **PASS** | "TOP COMMENT → WE BUILD IT" is fully on in f0000. The sign sits at y≈1000-1150. |
| 3 | PASS (weak) | PASS | The sign is bigger and lower. The fountain and feeder are still large at the top corners, but they are now clearly background. |
| 7 | PASS (issue) | **PASS** | The EXAMPLE stamp shows on the card 3.5-5.85 and on the build 6.2-7.9 only. It is not on Mango. |
| 8 | PASS (minor) | **PASS** | Likes reach 86-87 before the card leaves at 5.85. |
| 9 | FAIL (partial) | **PASS** | Camera is outside the lot looking in, with the town centre and Mango (right) visible behind the statue. "BUILT!" and the statue both start at 6.2; L4 ends at 6.34. The tag (x≈280-930) and the stamp sit below the statue's head. |
| 10 | FAIL | **PASS (soft)** | The fountain front is no longer the hero of any shot. It still sits right behind the statue in 6.2-7.9; acceptable. Mango's turn lands at about 8.95-9.5 on "ten out of ten". |
| 12 | PASS (weak) | PASS | Now static only 12.9-14.0 (about 1.1 s, right after the match cut, which is good for the reveal). The dive moves from 14.0. |
| 13 | PASS (note) | **PASS** | "Most likes in 24 h wins" is on screen 15.3-17.5 (2.2 s). "Follow to see it built" sits under it from 16.3. |
| 14 | PASS (minor) | PASS | The end headline "COMMENT YOUR IDEA" no longer duplicates the caption. All text stays in y 227-1450. The sign briefly crosses x<60 at about 16.5 s during the dive (it is scenery, not overlay; OK). |
| 16 | PASS / FAIL | PASS / pending | Loop 0.14. Posting files are being written; check they land in `episodes/rule-v1/` together with a cover made from f0000. |

### Remaining fixes (only ones worth a re-render)

1. **Optional, small: Mango's head is hidden behind "WE BUILD IT" in the hook and the loop end.**
   - In f0000 Mango is at about x 480-550 and y 640-740, and only his body shows under the yellow line. At 1.3 s his ears touch the text.
   - Tilt the hook and end camera's look-at point up by about 3-4° (or raise the look-at y by about 2 units) so the scene drops about 120 px. Mango then sits at about y 760-860, clear of the headline (which ends at about y 670).
   - The sign moves to about y 1120-1270 at frame 0, still inside 1500. Check that the 1.5 s push-in keeps the sign above y 1500.
   - Apply the identical change to the last 0.4 s so the loop stays under 1.0.
   - The hook is the daily template, so the one character should be visible in it every day. It is worth doing if the re-render is cheap; skip it if not.

Not worth a re-render:
- The tag partly covers the statue's lower body.
- The fountain sits behind the statue.
- The goal-town signs are still small.
