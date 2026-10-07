# Script v2 review: Cat Town launch ("Mango is alone")

**Pick: Option A, "Mayor Mango", tightened.** As written, A is about 81 words, which is about 32 s at 2.5 words/s. That is far too long. The final version below is **49 words, about 19 s**.

## Scores (tough reviewer, /10)

| | Hook (0-2 s) | Funny | 3 rules clear | Length | Simple English | Comment bait | Loop | Doable in engine | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| A Mayor Mango | 8: "won the election" + confetti grabs attention | 8: "One vote. His own." is a real joke at 2 s | 7: all three are there, but buried in extra lines | **3: about 32 s** | 9 | 6: "Cat airport? Sushi bar?" is good, but the end asks for two actions | 8: ends on lonely Mango | 8 (confetti without a build needs an overlay) | **7.0** |
| B Real-estate ad | 5: "Now selling" reads as an ad and gets scrolled | 6: "Neighbors? ... Mango. Just Mango." is good | 7 | 6 (about 24 s) | 9 | 6 | 5 | 9 | **5.5** |
| C Mango's diary | 6 | 7: the fountain and bowl jokes are cute | 6 | 6 (about 24 s) | 9 | 6 | 6 | **3: needs a second voice; jokes about talking to things need a face** | **5.5** |

Why not B and C:
- **B** sells a "house" for "one follow" and says "free water, free food". With the PETME2 badge on screen, it reads as a sales pitch and product copy. It breaks the "no sales lines" rule, and ad-feel kills reach.
- **C** relies on Mango's own voice and facial reactions. We have neither. Save it for after engine ask #1 (Mango's face).

What to fix in A:
- **Too long.** Lines 5, 7 and 9 repeat ideas.
- **The end asks for two actions** ("Follow + Comment"). Comments are goal #1, so speak only the comment ask. The follow ask goes on screen, and it is funny if framed as "voters".
- **Drop "Cat airport"** on screen. Our engine's custom building is a white box. Only show what we can pop (the statue).
- **Keep the catchphrase "Top comment? We build it."** from rule-v1, word for word. It is the series ritual.
- **"Mayor/vote" is a cute civic joke, not politics.** Never name real parties, people or slogans.

---

## Final script: "Mayor Mango" (49 words, about 19.0 s)

Deadpan narrator (Kokoro `af_heart`). Timings are estimates at about 2.6 words/s plus short gaps; re-time from the TTS. The badge (PETME2 CAT TOWN + counter) stays on the whole time.

| # | Time (est.) | Voice | On screen (headline / small) | Shot (engine) |
|---|---|---|---|---|
| 1 | 0.00-1.40 | "Mango just became mayor!" | **MAYOR MANGO 🏆** on frame 0 (no pop) | Mango in the square, side 3/4 angle, medium close. Overlay CSS confetti falling. Fanfare sting. |
| 2 | 1.55-2.15 | "One vote." | **VOTES: <y>1</y>** | Hold on Mango; the confetti thins. |
| 3 | 2.30-2.95 | "His own." | small: *(his own)* | Record-scratch SFX, confetti freezes and drops, a 0.3 s music dropout. Slow push-in on Mango. |
| 4 | 3.15-5.00 | "He's the only cat in town." | **POPULATION: <y>1</y>** | Fast crane-out to the high aerial: huge empty town, tiny Mango. The real counter shows "1". |
| 5 | 5.20-6.90 | "Every follow brings a cat..." | **1 FOLLOW = <y>🐱 + 🏠</y>** + **EXAMPLE** stamp | Example page: one follower house pops on a street with a cat walking out (`followersNew: 1`). **Hide `#count` or show "EXAMPLE" in its place**, so the badge never says 2. |
| 6 | 7.00-8.70 | "...and a house with your name." | engine tag "@your.name" + **EXAMPLE** | Push in on the house's name tag. |
| 7 | 8.95-10.50 | "Top comment? We build it." | **TOP COMMENT → <y>WE BUILD IT</y>** + EXAMPLE | Cut to the "YOUR IDEA HERE?" lot, 2-frame flash, Mango statue pops with confetti (`newBuild`). |
| 8 | 10.65-12.60 | "Giant Mango statue? He'd vote yes." | **MANGO: <y>YES ✅</y>** | Side close on Mango; time the anim offset so his turn lands on "yes". |
| 9 | 12.85-14.40 (hold to 15.3) | "Let's build a cat town." | **LET'S BUILD A <y>CAT TOWN</y>**; badge pill "1,000 cats · THE GOAL" | The 1,000-cat goal aerial, slow push. Music swell. |
| 10 | 15.40-18.40 | "Comment what we build first. Mango needs voters." | **COMMENT <y>YOUR IDEA</y> 👇**; small at 15.6 "Most likes in 24 h wins"; under it from 16.8 "Follow = 1 new cat 🐱" | Match cut to the same camera over the empty town ("1" returns). Dive down to Mango beside the "YOUR IDEA HERE?" lot. |
| - | 18.40-19.00 | (soft meow at 18.6) | headline swaps to **MAYOR MANGO 🏆** at 18.4 | The final pose equals the frame-0 pose, so the loop is seamless: "...Mango needs voters. / Mango just became mayor!" |

Word count per line: 4 / 2 / 2 / 6 / 5 / 6 / 5 / 6 / 5 / 8 = **49**.

## Notes

**Rules clarity:**
- Follow = cat + house: lines 5-6, shown on screen as an equation.
- Top comment = built: line 7, the catchphrase.
- Together: line 9, over the goal town.
- Each rule gets its own shot and one headline of 6 words or fewer.

**Comment bait:**
- "Comment what we build first" is the spoken ask.
- The "Mango: YES ✅" gag invites "Mango would vote for a nap tower" style replies.
- Pinned comment: "📌 Most likes in 24 h gets built, with your @ on it. Weirder = better. Mango already voted for a tuna fountain. His vote doesn't count."

**Honesty:**
- Every demo house, tag and building carries an EXAMPLE stamp.
- The badge never shows more than the real cat count.
- No prices, links or sales lines.
- The fountain and feeder stay small and in the background. No "free water/food" line.

**Engine feasibility:**
- Everything above uses existing pages, cameras, overlay and timing.
- Only line 1's confetti is new, and it is overlay CSS.
- If overlay confetti looks cheap, fall back to the engine's milestone gold pulse plus a fanfare.

**Template value:** "Mayor Mango" becomes the running character. Daily line: "Mayor Mango approves: 8/10."
