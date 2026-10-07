# PETME2 Cat Town - "Top comment = we build it" (rule-v1) Viral Blueprint + Daily Template

Format: 1080x1920, 30 fps, target **18.3 s** (hard range 15-22 s). Engine render (catcity.html, read-only) + injected overlay, Kokoro TTS `af_heart` (speed 1.12), code-synth music + SFX. Free tools only.

**Core message (owner's words, said in the video):**
- **"Top comment? We build it."** This is the hook, the rule and the catchphrase. It opens every episode.
- **"Let's build the city together."** This is the payoff line, said over the big shot in every episode.

**Goal metric:** comments first, follows second.

**Brand rule (owner update):** the engine's own badge stays on screen the whole video: the white "🐾 PETME2 CAT TOWN" pill, the big number and the dark "cat · Day N" pill (`#brand`, `#count`). "No brand" now means only: no product names, no prices, no sales lines and no links in the video.

---

## 0. What to keep and what to change from earlier videos

**Day 1 video (18.4 s, reviewer 7/10)**

*Keep:*
- Big stroked headline style (white with yellow, dark stroke).
- Word-by-word captions, hidden when they repeat the headline.
- The 1,000-cat goal shot: the most rewatchable frame we have, full of funny signs.
- The seamless loop.
- Pop SFX, ducked music.

*Change:*
1. **The rule came too late.** The follow rule landed at 7.4 s and the comment rule was not in the video at all. Here the rule *is* frame 0.
2. **Faceless back of Mango in the hook.** We still cannot give him a face (engine ask #1). So the hook does not open on Mango. It opens on the real "YOUR IDEA HERE?" lot sign, which the engine already draws, and Mango appears later in a side shot where he *moves* (the turn to drink). Motion reads as character; a static back does not.
3. **The "Water? Yes. Food? Yes." beat** spent 2 s on fountain and feeder close-ups. That is product time, and with the brand badge now on screen it would read as an ad. This time the fountain and feeder only appear in passing.
4. **The goal shot was too short (1.45 s).** Hold it for 2.7 s this time. It is the "together" shot.

**daily/example-day-02 template (auto Day-N maker)**

*Keep:*
- Engine comment card with hearts, scroll-to-winner, 👑 crown and the like count rolling up. This is native-looking and instantly understood.
- `newBuild` pop with confetti and the "@x 🏗️ built the Y" tag.
- Auto voice timing in `make_day.py` and the auto caption that thanks the winner.
- The `kind_for()` name-to-building mapping.

*Change:*
1. **The payoff is too late.** The building pops at 10.5 s of 15.3 s, and the hook says "You asked for CAT AIRPORT" over the square, where there is no airport. Day-N must show the *real winning comment* in frame 0 and pop the building by about 3 s.
2. **"You asked" is anonymous.** A real person (@handle + their words) winning is the reason others comment. So the winner's card is the hook.
3. **The counter lies for a moment.** The pill says "1 cat · Day 2" while the voice says "12 new cats". Use the engine `#count`: it counts up as houses pop, with `milestone` for the gold pulse, so it is always true on screen.
4. **Two CTAs in one 11-word line** ("Follow to move your cat in, and comment what we build tomorrow!"). The comment CTA is spoken; the follow CTA goes on screen only.
5. **The ending is not a loop.** It ends on a generic far aerial. Day-N must end on the *next empty lot* ("YOUR IDEA HERE?"). That is the open loop for tomorrow and the loop point to frame 0.
6. **The comment card runs off the safe area.** `.cm` is left 90 / right 90, so x reaches 990. Override it in the overlay CSS to `right:140px`, which gives x 90-940.
7. **No deadline, no platform, no fallback rule.** Add "24 h", which app the comment came from, and "rude/political/unsafe = skipped".

---

## 1. Why it can go viral

- **The comment *is* the ticket.** To take part you only type an idea. No follow, no link, no effort. Any idea counts ("anything, cat version"), so the bar is zero and the ceiling is fun. People comment to be funny for *other commenters*, so the comment section itself becomes entertainment. Reading it adds time on the post, and the replies feed ranking.
- **A second, cheaper action: liking comments = voting.** People who won't write still scroll and like ideas, which means more time in the comments. They also come back to check whether their pick is winning. Friends rally friends ("go like my sushi bar"): this is the shareability engine, the Boaty McBoatface effect.
- **Real reward, visible tomorrow.** The winner gets the build *and* their @ on it in a video seen by thousands. Status + creative ownership is a stronger pull than a giveaway, and it costs nothing.
- **Stakes + deadline.** One winner a day and "most likes in 24 h". Scarcity and a clock make people comment *now*, not "later".
- **Open loop.** The video ends on an empty lot with a "?" sign: "what gets built tomorrow?" You only find out by following (follows second).
- **"Weirder is better."** It gives permission for absurd ideas (cat airport, laser tower, a pyramid of boxes). Absurd ideas get more likes and more replies, and absurd comments get screenshotted and shared.
- **Rewatch.**
  - The example build pops with confetti at 6.2 s.
  - The goal city is dense with readable funny signs (CAT AIRPORT, CAT CINEMA, FISH MARKET, MANGO STATUE). Viewers pause to read them.
  - The last frame is the first frame, so it loops.
- **Series habit.** The same catchphrase opens every day ("Top comment? We build it."), the same lot sign closes it, and it posts at the same time. Viewers learn the ritual: watch, see who won, comment, return tomorrow.
- **Honest by design.** The demo comment and build are stamped EXAMPLE. Then we hard-cut to the *real* town: 1 cat, 0 buildings. The honesty itself is the stake: "nothing is built yet, so YOUR idea is first." Being the first build of a city is a strong pull for early commenters.

**Why they come back tomorrow:**
- To see if their idea (or their friend's) won.
- To see how we turned a weird idea into a "cat version".
- To vote again on the next lot.

The answer only arrives in the next video, so the open loop pays off each day and opens again.

---

## 2. Hook options (first 1.5 s, must work muted)

| # | Spoken (starts 0.15 s) | On-screen text | First shot |
|---|---|---|---|
| **A** | "Top comment? We build it." | **TOP COMMENT → WE BUILD IT** | Low, fast push-in on the real empty lot: orange cones + the engine's "YOUR IDEA HERE?" sign, Mango's square small behind it, PETME2 Cat Town badge up top |
| B | "This comment got the most likes... so we built it." | Example comment card (87 ❤, 👑) + EXAMPLE sticker | Comment card full-width over the lot; statue pops at 1.2 s |
| C | "Let's build the city together." | TODAY ↔ THE GOAL | 0.7 s of the 1,000-cat city, hard cut to the empty town, same camera |

**Pick: A.**
- It is the owner's exact line, so the rule is the hook.
- It reads fully muted: the words plus a physical "YOUR IDEA HERE?" sign mean "you comment, it appears here".
- It is 100% real footage (the lot and the sign exist in the live town).
- Frame 0 equals the last frame, so the loop is clean.

**Why not the others:**
- B is the strongest payoff-first hook, but here the comment would be fake. Leading with an EXAMPLE stamp in frame 0 kills trust. **B becomes the Day-N hook**, where the comment is real.
- C is beautiful but abstract without the rule; it repeats Day 1's trick. Its shot is used at 9.9 s as the "together" beat.

---

## 3. Final voice script (Kokoro `af_heart`, speed 1.12, warm, light deadpan; times are targets, re-time from the TTS)

| # | Time | Line | Subtitle |
|---|---|---|---|
| L1 | 0.15-1.45 | "Top comment? We build it." | hidden (= headline) |
| L2 | 1.75-3.30 | "Every day. Anything you want." | hidden (= headline) |
| L3 | 3.55-5.60 | "The comment with the most likes wins..." | shown |
| L4 | 5.85-6.90 | "...and we build it!" | shown |
| L5 | 7.10-8.30 | "With the winner's name on it." | shown |
| L6 | 8.55-9.70 | "Mango's review: ten out of ten." | hidden (= headline) |
| L7 | 10.00-12.00 | **"Let's build the city together."** | hidden (= headline) |
| L8 | 12.75-14.20 | "Right now? One cat. Zero buildings." | hidden (= headline) |
| L9 | 14.50-17.60 | "So comment what we build first. Weirder is better." | shown |
| - | 17.6-18.3 | no voice: a soft meow at 17.9 s; the music resolves to the intro note so the loop lands on L1 | - |

**Rules:**
- Lines are 9 words or fewer.
- Gaps between lines are 0.35 s or less, except a 0.75 s hold after L7 so the goal shot breathes.
- No product names, prices or "link in bio".
- The loop reads as one sentence: "...Weirder is better. / Top comment? We build it."

---

## 4. Shot list (mapped to the engine)

**Engine pages**

Three episode JSONs, like Day 1's `mk.py`, with a `SEG(T)` map in render.js:

- **e0 = real town today.**
  - `followersBefore` = real follower count (0 today), `followersNew: 0`, `landmarks: []`.
  - No `newBuild`. `noReserved: false`, so the engine places the "Your idea here?" sign + cones at SPOTS[0] and SPOTS[1].
  - `day` = the real series day.
  - `EP.comments` with the 3 example comments (see below).
  - `shots` = custom camera.
- **e1 = example build.** Same as e0, plus:
  - `newBuild: {kind:"statue", sign:"Mango Statue", name:"Mango Statue", by:"example.anna", at:6.20}`. The statue pops at SPOTS[0], the same lot as the hook sign, with confetti.
  - `starts:[0,99,99,8.4]`, so the engine's build tag hides at 8.4 s.
- **e2 = goal town.**
  - `previews/p_1000.json` with `still` removed and the landmark sign "PETME2 Pet Shop" renamed "Toy Shop" (a shop sign in the goal town still reads as an ad).
  - Same `shots` array.

**Comment card data** (`EP.comments`, in e0):

```json
{"list":[{"by":"example.lior","text":"A sushi bar for cats","likes":31},
         {"by":"example.dan","text":"Giant scratching tower","likes":54},
         {"by":"example.anna","text":"A giant Mango statue!","likes":87}],
 "win":2,"t":{"up":3.5,"scroll":3.85,"stop":5.0,"down":6.05}}
```

The statue is the only built-in kind that looks *exactly* like its request. Don't demo "Cat Airport" here (custom = white box + yellow roof), or the very first build looks like a broken promise.

**Lot coordinates**
- SPOTS are deterministic but not exposed. Get them once with a probe: a scratch *copy* of catcity.html with `window.__SPOTS = SPOTS` appended. This copy is only for reading numbers, never for rendering.
- Save the result to `episodes/rule-v1/spots.json`.
- Every shot below that says "lot" means SPOTS[0]: position `(s.x, 0, s.z)`; it faces the center (`ry = atan2(-x,-z)`).
- Camera "outside the lot looking in" = `lot + 30·(lot/|lot|) + (0,6,0)`, looking at `(lot.x, 5, lot.z)`. The sign sits at y≈6.5, and Mango's square sits behind it.

| Time | Page / anim | Camera move (EP `shots`) | What happens | Interrupt |
|---|---|---|---|---|
| 0.00-1.60 | e0 | **Lot close, low, outside looking in**: push-in from 34 → 24 units, `inout` | "YOUR IDEA HERE?" sign + orange cones fill the middle third; Mango's square is small behind it | Headline pop at 0.05 s + pop SFX |
| 1.60-3.50 | e0 | **Crane up and back** to a high aerial `[0,150,120] → look [0,0,-10]` (Day 1 shot 2), `inout` | Whole empty town, both reserved lots with cones visible, tiny Mango | Whoosh |
| 3.50-6.15 | e0 | Slow drift down toward the lot from above `(lot·1.6 + (0,70,0)) → (lot·1.3 + (0,40,0))`, lot in the lower half | `EP.comments` card slides in at 3.5 s, scrolls 3.85→5.0, 👑 + likes roll 48→87 at 5.0, slides out 6.05 | Card slide, scroll tick SFX, crown "ding" |
| 6.15-8.40 | e1 (cut at 6.15, 2-frame white flash) | Lot medium-close, same angle as 0.0 s but 40 units out, slow orbit 15° | `newBuild` statue grows at 6.20, confetti 6.6-10.6, engine tag "@example.anna 🏗️ built the Mango Statue" at 7.0 | Pop + fanfare + confetti crackle |
| 8.40-9.90 | e0, anim = T - 1.3 | Square side close: `[9,5,9] → [8,4.6,8]`, look `[0,2,0]`. Frame it **away from the fountain front window** (keeps product details small) | Mango sits, then turns left at about 9.3 s (anim u=8.0) toward the fountain: the "deadpan judge" beat | Cut + soft "hm" synth blip |
| 9.90-12.60 | e2 | Goal aerial `[275,128,185] → [232,106,155]`, look `[-40,0,0]` (Day 1 shot) | Dense 1,000-cat city, readable signs, fish balloons | Biggest change, music swell |
| 12.60-14.40 | e0 | **Same camera as 9.90-12.60** (match cut), held | The exact same view, now empty: 1 cat, 0 buildings | Record-scratch synth + 0.25 s music dropout |
| 14.40-18.30 | e0 | Dive from the goal-angle aerial down to the 0.0 s lot pose (`inout`). The last 0.4 s matches frame 0 exactly (same p/l, anim = T - 18.3 like Day 1) | Ends on the "YOUR IDEA HERE?" sign | Push-in, meow 17.9 s |

**Notes**
- A visual change (cut, move, pop or text change) happens at least every 2.7 s.
- The **e0 → e1 cut at 6.15** hides the swap from the sign to the empty lot (in e1 the reserved sign moves to SPOTS[1]). The statue then grows at 6.20, so it reads as "the sign became the statue".
- **The demo statue never appears in e0.** After the demo every shot is the real empty town again.
- **Badge in the goal shot:** e2 has 1,000 followers, so `#count` would show "1,001 cats". In 9.9-12.6 hide `#count` (overlay CSS on the e2 page) and show the overlay pill "THE GOAL · 1,000 cats" in its place. `#brand` stays.
- **Halloween:** the engine forces Halloween from Oct 24 by the render machine's date (no off switch). Render this video before Oct 24. Later days will be Halloween-themed whether we like it or not (engine ask #6).

---

## 5. On-screen text per beat + layout

**Layout** (safe zone x 60-940, y 220-1500). Repositioned with overlay CSS only (`!important` beats the engine's inline styles), no engine edit:

| Element | Where | How |
|---|---|---|
| `#brand` "🐾 PETME2 CAT TOWN" | top **232 px**, centered (x≈370-710) | `#brand{top:232px!important;opacity:1!important}`. The engine fades it after `starts[1]`, so force it on. |
| `#count` big number + "cat · Day N" pill | top **284 px**, scaled 0.7 → number y≈284-390, pill y≈400-450 | `#count{top:284px!important;transform:scale(.7);transform-origin:top center;opacity:1!important}`. The engine's `countN` pulse still works. Set `countFrom:0`. |
| `#title` (DAY N), `#end`, `#sub` | hidden | as in Day 1's overlay |
| Big headline (`.big`) | **top 500 px**, x 60-940, max 2 lines (~500-720) | moved down from 330 so it sits under the badge |
| Small line (`.small`) | y 740-800 | yellow, 56 px |
| Comment card `#cm` | **top 800 px, left 90, right 140** (x 90-940, y 800-1060) | the 👑 crown sits at its top-right, inside 940 |
| Captions (`.cap`) | y 1290-1450, x 60-940 | current word yellow |
| EXAMPLE stamp | red rounded tag, rotated -6°, 40 px; on the card's top-left corner (x 100-330, y 770) and later next to the build tag | |

The badge, headline and card stack top to bottom and never overlap. The headline never shares the screen with the card for more than 0.3 s; while the card is up the headline is the short "MOST LIKES WINS".

| Time | Big headline (≤6 words) | Small / extras |
|---|---|---|
| 0.05-1.60 | TOP COMMENT →<br><y>WE BUILD IT</y> | - |
| 1.60-3.50 | EVERY DAY.<br><y>ANYTHING.</y> | small at 2.2 s: "(cat version 🐱)" |
| 3.50-6.15 | MOST LIKES <y>WINS</y> | card y 800-1060 + **EXAMPLE** stamp on the card; caption L3 |
| 6.15-8.40 | <y>BUILT!</y> | engine build tag over the statue (clamped x 250-830) + **EXAMPLE** stamp beside it; caption L4/L5 |
| 8.40-9.90 | Mango's review:<br><y>10/10</y> | - |
| 9.90-12.60 | LET'S BUILD THE CITY<br><y>TOGETHER</y> | `#count` hidden; overlay pill "THE GOAL · 1,000 cats" at y 284 |
| 12.60-14.40 | TODAY: <y>1 CAT</y><br><r>0 BUILDINGS</r> | `#count` back, showing the real "1" |
| 14.40-18.00 | COMMENT 👇<br><y>WHAT WE BUILD</y> | small at 15.2 s: "Most likes in 24 h wins"; at 16.6 s it swaps to "Follow to see it built"; caption L9. Arrow "👉" at x 880, y 1180, bobbing toward the app's right-rail comment icon |
| 18.00-18.30 | fade all overlay text over 9 frames (the badge stays, it is on frame 0 too) | - |

Max on screen at once: headline + one small line, about 10 words, plus the badge.

---

## 6. Ending, loop and CTA

- **Spoken CTA (only one): comment.**
  - "So comment what we build first. Weirder is better."
  - "First" is the hook: the first building of a whole city, and "your idea goes first".
- **Reasons to comment right now:**
  1. **24 h deadline** (on screen + pinned).
  2. **First build ever** (said).
  3. **The winner's @ on it** (said at 7.1 s, shown by the engine tag).
  4. **Weird = good** (permission).
  5. **Liking = voting** (pinned comment), so even lurkers act.
- **Follow** is only on screen ("Follow to see it built") and in the caption. The follow = cat rule lives in the caption and the pinned comment. One new rule per video.
- **Loop:**
  - The last frame is the frame-0 lot pose (same camera p/l, same anim phase).
  - The badge is identical on both frames.
  - The headline fades out at 18.0-18.3 and pops back in at 0.05.
  - Music ends on the intro's first chord.
  - Voice: "...Weirder is better." → "Top comment? We build it."
- No end card and no logo slate (the badge already carries the name).

---

## 7. The TEMPLATE (announcement → Day-N)

**Fixed every day (the ritual)**
1. The catchphrase **"Top comment? We build it."** in the first 1.5 s.
2. The comment card → 👑 → **build pop with confetti** → "@x built the Y" tag.
3. The **Mango's review: N/10** gag (a recurring bit; low scores like "6/10, needs fish" make people argue in the comments).
4. **"Let's build the city together."** over the widest real aerial.
5. End on the **next empty lot** ("YOUR IDEA HERE?" is automatic: the engine puts it on the next free spot), with the spoken comment CTA and an exact loop to frame 0.
6. The badge (brand + true counter) on screen all the time; same music, same text style, same posting time.

**Variables (one small JSON per day)**
```json
{
  "day": 3,
  "mode": "daily",                       // "announce" (this video) or "daily"
  "winner": {"by": "anna", "text": "Build a cat airport!", "likes": 87, "app": "IG"},
  "others": [{"by": "dan", "text": "Sushi bar", "likes": 54}, {"by": "lior", "text": "Laser tower", "likes": 31}],
  "build": {"name": "Cat Airport", "kind": "custom"},   // kind optional (kind_for() guesses)
  "new_followers": 12,                   // real; total cats = state followers + new + 1 (Mango)
  "mango_score": "9/10",
  "deadline": "6 pm ET"
}
```
- **From `state.json` (already exists):** the followers before today and past landmarks. `--commit` appends the build and its `by` after the owner approves.
- **The script fills:** voice lines (one template string each), beats, `ep.json` (`comments`, `newBuild`, `followersNew`, `milestone`, shots) and the caption.

**Day-N timeline (about 15-16 s): the same skeleton, payoff first**

| Time | Beat | Voice (template) | Engine |
|---|---|---|---|
| 0.0-1.6 | Hook: real winning comment | "Top comment? {short text}." (or "Top comment? We build it." if the text is over 5 words) | `EP.comments` card up **from t=0** (`up:0`), starting on 3rd place and scrolling to the winner by 1.4 s, 👑 at 1.4 s; lot with sign behind it; headline "DAY {N}" |
| 1.6-3.0 | Likes + rule | "{likes} likes. So we build it." | Card slides out at 2.8 s; camera pushes to the lot |
| 3.0-5.0 | Build pop | "Here it is: the {build}!" | `newBuild.at = 3.1`, confetti, tag "@{by} 🏗️ built the {build}" from 3.9 s (the real handle, read on screen only, never by TTS) |
| 5.0-6.4 | Mango review | "Mango's review: {score}." | Mango side shot, anim offset to his turn |
| 6.4-9.4 | Town grows | "Plus {X} new cats moved in!" / X=0: "No new cats today... yet." | Aerial; houses pop with @ tags (`newFrom/newTo`), `#count` counts up, `milestone` gold pulse |
| 9.4-11.2 | Together | "Let's build the city together." | Widest real aerial showing all builds so far |
| 11.2-15.5 | Next lot + CTA | "Tomorrow's lot is empty. Comment what we build next!" | Dive to the next reserved lot, the exact frame-0 pose (the loop) |

**What changes from the announcement to Day-N**
- The hook is a **real comment card** (no EXAMPLE stamp, real handles; runner-ups may show their text + likes).
- The build pops **by 3 s**, not 6 s.
- The rule explanation (L2-L5) shrinks to 1 line.
- The goal-town flash is replaced by **real progress**: new houses + counter. Reuse the goal flash only on milestone days (e.g. 100 cats).
- The CTA "first" becomes "next".

**Code notes for whoever extends `make_day.py`**
- Add a `mode` switch. Use the overlay CSS above for the badge, the card at top 800 / right 140, and the headline at 500.
- Replace the default camera with explicit `shots` built from `spots.json[len(landmarks)]` (today's build) and `spots.json[len(landmarks)+1]` (tomorrow's lot).
- Keep `kind_for()`. Add "statue" words: "mango", "giant cat", "golden".

**Daily rules (write them in the pinned comment, enforce them in the script)**
- The comment counts at **T+22 h** (screenshot it as proof).
- Ties go to the earliest comment.
- Our own account's comments are excluded.
- Rude, political or unsafe ideas are skipped, and the next one wins.
- Duplicate ideas are not merged (one comment = one ballot).
- One build per day across both apps: the highest raw like count wins, and the video says which app it came from.
- If there are no comments, say so honestly: "No comments yet, so Mango picked." Never invent a commenter.

---

## 8. Posting package

### Instagram (Reel)
- **Caption line 1 (82 chars):** "Top comment = we build it. Every day. Let's build the city together 🐱🏗️"
- **Line 2:** "Comment what we build first 👇 Most likes in 24 h wins, and your @ goes on it."
- **Line 3:** "Weird ideas welcome (we make the cat version). Rude, political or unsafe ideas are skipped."
- **Line 4:** "Plus: every new follower = one new cat moves in."
- **Hashtags (5):** #cattown #catsofinstagram #cats #3danimation #lowpoly
- **Pinned comment (posted from our account, not a vote):** "📌 RULES: Most-liked comment by tomorrow 6 pm ET gets built, with your @ on it. Like the ideas you want, likes = votes. Weird = good. Rude/political/unsafe ideas are skipped. (Mango votes for a nap tower 😼, but his vote doesn't count.)"
- **Cover:** the 0.4 s frame: lot sign + "TOP COMMENT → WE BUILD IT" + badge. Everything important sits in y 240-1680, so it survives the 3:4 grid crop. Make a clean cover without subtitles.
- **Tips:**
  - Post to the **main grid, not as a Trial Reel**. Followers must learn the rule.
  - Then **pin it to the profile** (it is the "rules" reel).
  - Post Tue-Thu, 6-8 pm in the main audience time zone. Post every Day-N at the same time: the deadline = the next post time.
  - Reply to every comment for the first 60 min. Short replies that invite likes: "this one could win 👀", "cat version: a box-shaped airport?".
  - At about T+12 h, post a Story with a **countdown sticker** ("Comments close") + "current leader: X (54 ❤)".
  - Next day, use **IG "reply with reel"** on the winning comment if possible: the real comment shows natively.
  - Day-N later: use Trial Reels only for *re-cuts* of the best days, not for the daily results (voters must see them).

### TikTok
- **Caption (under 125):** "The top comment decides what we build in Cat Town 🐱 Comment your idea 👇 #cattown #catsoftiktok #3danimation #lowpoly"
- **Pinned comment:** the same rules as IG, shorter: "📌 Most likes by tomorrow 6 pm ET = we build it + your @ on it. Weird = good. Rude/political/unsafe = skipped."
- **Cover:** the same frame. Add TikTok's cover title "TOP COMMENT = WE BUILD IT" in the app (centered, inside the safe area).
- **Tips:**
  - Upload our audio at 100%. Optionally add a trending sound at 5-10 % (keep the voice clear).
  - Same post time as IG.
  - **Day-N on TikTok = "Reply to comment" video:** the winning comment sticker is native, which is the strongest proof of honesty and a reason others comment ("maybe they reply to mine").
  - Turn on "Allow Stitch/Duet".
  - Reply-with-video to one funny losing comment mid-day as a bonus post ("Too weird? Let's see if it wins").

**Safety note (both apps):** we only build safe, kind ideas. Rude, political, hateful, violent or unsafe asks are skipped and the next most-liked comment wins. Hide or delete abusive comments; don't argue in replies.

---

## 9. Reviewer checklist (pass/fail, test against the rendered video)

1. Spec: 1080x1920, 30 fps, H.264 + stereo AAC; length 15-22 s; no black frames; loudness about -14 to -16 LUFS; no clipping.
2. Frame 0 (0.0 s) shows the real "YOUR IDEA HERE?" lot sign, and the headline "TOP COMMENT → WE BUILD IT" is readable by 0.2 s.
3. Muted test: the first 1.5 s alone explain "comment → it gets built".
4. "Top comment? We build it." is spoken by 1.5 s, and "Let's build the city together." is spoken over the goal shot.
5. The PETME2 Cat Town badge (`#brand` + `#count`) is visible the whole time, inside y 220-500, and never overlaps the headline or the comment card.
6. The counter never shows more than the real number of cats: the real count (1 today) everywhere, and hidden or replaced by "THE GOAL · 1,000 cats" in the goal shot.
7. Every demo comment card and demo build carries a visible EXAMPLE stamp, and the demo handles start with "example.". The demo statue appears only in the 6.15-8.4 s segment.
8. The comment card scrolls to the winner, the 👑 appears, and the like count rolls up; the card sits inside x 60-940.
9. The statue pops with confetti on the same lot where the sign was, with a cut or flash that hides the swap; the build tag sits inside x 60-940.
10. Mango is on screen and moves (turns) in the review beat; the fountain's front is not the focus of any shot.
11. The goal shot is held 2.5 s or longer, and the next shot is a match cut (same camera) to the empty town.
12. There is a visual change at least every 3 s; no static stretch over 3 s.
13. One spoken CTA (comment). The follow appears only as small on-screen text. "24 h" is on screen.
14. All text is inside the safe zone (x 60-940, y 220-1500); a headline is 6 words or fewer; subtitles never duplicate the headline.
15. No product names, prices, links or sales lines in voice, text or signs (the goal-town shop sign reads "Toy Shop", not "PETME2 Pet Shop").
16. The last frame matches frame 0 (mean pixel diff under 1.0, same badge); the loop has no jump; the posting package (both captions, pinned comments, cover) exists in the folder.

---

## 10. Engine asks (only the engine owner can do these), ranked by virality impact

1. **Mango face + reactions on cue.**
   - Two square eyes, a pink nose and blinks.
   - An `EP.mango: [{at, act: "look" | "hop" | "spin" | "headTilt"}]` option, so he can look at the camera in the hook and react to each build (a real "Mango's review").
   - This is the reviewer's #1 open item and the biggest lever for the 3 s hold.
2. **Permanent credit on builds.**
   - The landmark sign gets a second line "by @handle" (`landmarks[].by`), and the live web town shows it when tapped.
   - It makes "your @ on it forever" literally true. Today the @ only lives in the video tag.
3. **More request-shaped build kinds + a construction animation.**
   - Kinds: airport (plane on a runway), tower or scratching post, rocket, castle, sushi bar, roller coaster, plus `custom` with a big emoji billboard on the roof, so "anything" looks right.
   - Also a 2 s crane/scaffold build-up instead of an instant pop (more satisfying, more rewatch).
4. **Expose camera helpers.**
   - `window.__SPOTS` and `NBpos`, or `EP.cam: "lot:k"` shots, so the template can aim at today's build and tomorrow's lot without a probe copy.
5. **Badge options.**
   - An `EP.badge` to set its top offset and scale, plus `EP.countOverride` / a "goal" label, so the goal-town flash shows "GOAL 1,000" natively instead of overlay CSS hacks.
   - A configurable comment-card label + "EXAMPLE" flag + app icon (IG/TikTok).
6. **`EP.halloween: false` actually forces Halloween off.** Today the render machine's date turns it on from Oct 24 with no way out.
7. **Crowd reaction:** on `newBuild` the town's cats walk to the new building for a few seconds (social-proof shot; reuses the feeding-time run-to-square logic).
8. **A "next lot" highlight:** a soft pulsing ring or spotlight on the next reserved lot, so the open-loop ending pops at phone size.
