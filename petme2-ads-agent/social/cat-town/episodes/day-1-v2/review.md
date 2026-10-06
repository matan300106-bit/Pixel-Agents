# Cat Town Day 1 (v2): Virality Review

Video: /tmp/ct/v/day1.mp4. Reviewed with 552 frames (contact sheets every 10th frame, full-size key moments), ffprobe and ffmpeg (loudnorm, silencedetect, blackdetect, scene>0.3), a per-frame motion diff and the audio RMS envelope.

## Verdict: NEEDS FIXES (small ones). Virality score: 6/10
The structure is strong. It has a clear lonely-cat premise, one rule, a big goal flash and a near-loop. The 1,000-cat town at 12.8 s is the best shot: it is dense, full of funny labels (CAT AIRPORT, CAT CAFE, CAT POOL, FISH MARKET) and makes people pause and rewatch. It is held back by three things: a faceless back-view of Mango in the hook, a brand name visible in the goal shot, and text clutter at the end. Fixes 1-5 below would move it to about 7-7.5.

## Tech facts
- H.264 yuv420p, 1080x1920, 30 fps, 18.4 s (551 frames). AAC 48 kHz **mono**.
- Loudness -15.0 LUFS integrated, true peak -2.0 dBTP (no clipping), LRA 1.2 LU.
- No silence over 0.4 s at -40 dB, except a deliberate dip to about -27 dB at 14.6-14.9 s. No black frames.
- Hard cuts (scene>0.3) at 2.80, 4.57, 5.80, 6.60, 7.40, 10.30, 11.10, 12.80 and 14.27 s. Between them the camera keeps moving (push-out, aerial, dive, push-in).
- Lowest-motion stretches: 0.8-1.1 s, where Mango is static, and 14.4-15.9 s, a slow settle. Both are under 3 s, and the text changes during them.

## Checklist (section 8)
| # | Result | Evidence |
|---|---|---|
| 1 | PASS | Mango fills frame 0 (back view). First word "This" starts at 0.15 s. |
| 2 | PASS | "POPULATION: 1 CAT" is fading in by 0.07 s and solid by 0.17 s, over a lone orange cat. |
| 3 | PASS | 18.4 s. Longest line is 7 words ("every new follow brings one more cat"). |
| 4 | PASS | Spoken at 8.38-10.10 s. On screen "1 FOLLOW = 1 NEW CAT" at 7.4-10.3 s. |
| 5 | PASS | Cuts every 0.8-2.8 s up to 14.27 s, then a settle and a push-in to 18.4 s. No dead stretch over 3 s. |
| 6 | PASS | Goal flash at 12.8-14.27 s: a dense golden-hour city with a blimp. It reads very differently from the empty town. |
| 7 | PASS | All 3 tags read "@you / new cat moved in (example)". The counter shows "1 cat · Day 1" the whole time. |
| 8 | **FAIL** | Drinks at 4.6-5.8 s and eats at 5.8-6.6 s, which is natural. But a **"PETME2 PET SHOP"** label is visible in the goal town at 12.8-14.27 s (left of the fountain, about x 290-390, y 1030 on f0400). |
| 9 | **FAIL** | The @you tag at 11.9-12.8 s runs to about x 1075, past 940 and under IG's right button rail. The end card (16.6-18.4 s) shows about 17 words at once: pill, headline, "Top comment builds next", "+ Follow" and a 6-word subtitle. |
| 10 | **FAIL** | Word-by-word yellow highlighting works, and nothing physically overlaps. But subtitles repeat the big text: 7.4-10.3 s has "1 FOLLOW = 1 NEW CAT" plus "every new follow brings one more cat", and 15.9-18.4 s shows "Be Mango's first neighbor" twice. The plan says to hide them. |
| 11 | **FAIL** (minor) | Framing nearly matches and there is no black frame. But Mango is slightly turned in f0551 vs f0000, and every overlay (pill, headline, CTA, button, subtitle) vanishes at the loop cut, so the jump is visible. |
| 12 | PASS | One spoken CTA ("Follow to be Mango's first neighbor"). The comment CTA appears only as small yellow text. |
| 13 | PASS (weak) | No clipping. House pops at 9.75, 10.65 and 11.55 s are only about +3-4 dB over the bed. Music between lines sits at about -18 to -21 dB vs voice at about -12 to -15 dB, so it is ducked only about 5 dB. Mono. |
| 14 | PASS | 1080x1920, 30 fps, H.264, no letterbox, no watermark. |
| 15 | **FAIL** | Caption line 1 is 68 chars and there are 4 hashtags (OK). **No cover file exists** in the episode folder or in /tmp/ct/v. |

Score: 10 PASS / 5 FAIL.

## Top fixes, ranked by impact on reach
1. **Hook, 0.0-1.2 s (hook / 3 s hold).** Mango is a faceless orange block seen from behind and does not move at 0.6-1.1 s. Viewers bond with a face, not a back.
   - Give him a minimal face (two black square eyes and a pink nose) and start in a 3/4 view, or have him look back over his shoulder at about 0.4 s with an ear twitch and a tail flick.
   - Add a soft meow at 0.1 s.
   - This is the single biggest lever.
2. **Remove "PETME2 PET SHOP" from the goal town at 12.8-14.27 s (trust / comments).** Rename it "PET SHOP" or "YOUR IDEA HERE?". A brand inside the "pure" cat video turns comments into "it's an ad".
3. **Cut text clutter (retention / readability).**
   - At 7.4-10.3 s and 15.9-18.4 s, hide the subtitles while the headline says the same thing.
   - On the end card keep three items: headline, "Top comment builds next" and the button. That is 6 words or fewer at a time.
4. **Seamless loop at 18.1-18.4 s (rewatch).**
   - Match the camera and Mango's rotation exactly to f0000.
   - Fade all overlays out over the last 8-10 frames so the loop lands on a clean frame 0, or put the pill and "POPULATION" on frame 0 so text persists across the cut.
5. **Move the @you tag at 11.9-12.8 s left (safe zone).** Its right edge should be at x 940 or less. The tag center can go to about x 700, or the house can sit more to the left.
6. **Make "follow = cat" literal (follows).** The box house at 10.0 s and the house at 12.0 s say "new cat moved in" but no cat is visible.
   - Pop a grey cat out of each house with a meow.
   - Raise the pop SFX about 6 dB and make them ascending pitches.
7. **Audio mix.** Duck the music 10-12 dB under the voice. A stereo export is optional.
8. **"+ Follow" fake button at 16.2-18.4 s.** It is not tappable, and a tap only pauses the video. Replace it with "Follow ↓" pointing toward IG's real username / Follow area at the bottom-left, or keep it but expect no click-through.
9. **Small text fixes.**
   - "TODAY: 1" at 14.25 s should read "TODAY: 1 CAT" so it stays clear when muted.
   - Hold the goal flash about 0.3 s longer, since it is the pause-and-rewatch shot.

## Posting package (judgement + final version)
- **Caption:** the plan's is good. The tight final version:
  - "Mango is the only cat in this town. Every new follow moves one more cat in."
  - "Follow and your cat gets its own house with your @ on it. Most-liked comment picks what we build next (cat airport?)."
  - "Day 1 of Cat Town. Goal: 1,000 cats."
- **Hashtags:** keep 4: #cattown #catsofinstagram #cats #3danimation.
- **Pinned comment:** the plan's "I'll build its house on Day 2" promises a house per commenter, which does not scale. Final version: "Mango needs a neighbor. Follow + drop your cat's name, the first followers move in on Day 2. Most-liked reply = what we build next. Cat airport? Sushi bar?"
- **Cover:** missing; make it. The plan's aerial frame (about 2.0 s) leaves Mango as a dot in a 3:4 grid thumbnail. Use about 0.5 s (f0015): big Mango, "POPULATION: 1 CAT" and the pill, all within y 240-1680 so it survives the 3:4 crop. Once fix 1 is in, use the version with a face.
- **Posting:** Trial Reel first, as the plan says. Reply to every comment within 60 min.

## Re-check (render of 22:27): 15/15 pass. READY. Virality 7/10
- **Tech:** H.264, 1080x1920, 30 fps, 18.4 s.
  - AAC is now **stereo**. -16.1 LUFS, true peak -4.5 dBTP.
  - No black frames and no silence gaps.
  - The cuts are unchanged (2.8 to 14.27 s), so nothing broke.

| # | Result | Evidence |
|---|---|---|
| 1 | PASS | Mango fills frame 0. Voice starts at 0.15 s. |
| 2 | PASS | "POPULATION: 1 CAT" by about 0.17 s. |
| 3 | PASS | 18.4 s. Lines are 7 words or fewer. |
| 4 | PASS | Spoken at 8.4-10.1 s and on screen at 7.4-10.3 s. |
| 5 | PASS | Same cut map as before. No stretch over 3 s without a change. |
| 6 | PASS | Goal flash at 12.8-14.27 s is unchanged. |
| 7 | PASS | Tags read "@you / moved in (example)". The counter stays at 1 cat. |
| 8 | PASS | The sign now says "PET SHOP" (f0400). No brand text found. |
| 9 | PASS | @you tag at 12.0 s spans x about 525-915. The end card is the headline plus "Follow 👇", about 6 words. |
| 10 | PASS | Subtitles are hidden at 7.4-10.3 s and 15.9-18.4 s. No double text. |
| 11 | PASS | f0551 vs f0000 mean pixel diff is 0.31, near identical. The text fades out over f0540-551. |
| 12 | PASS | One spoken CTA. The comment CTA is now only in the caption and pinned comment, which is OK. |
| 13 | PASS | Pops are +5 to +8 dB over the bed (9.75 / 10.65 / 11.55 s). Music is lower, with gaps at about -21 to -23 dB. No clipping. |
| 14 | PASS | Spec OK. Stereo. |
| 15 | PASS | cover.jpg exists: Mango, the pill and "POPULATION: 1 CAT", all inside the 3:4 crop. Caption and hashtags are OK. |

- **Still open (not blocking):**
  - Mango has no face and is seen from behind in the hook. This is the main thing between 7 and 8+ for the next episode.
  - The goal shot is still only 1.45 s.
  - Optional: drop the "This is Mango." subtitle from cover.jpg for a cleaner grid tile.
