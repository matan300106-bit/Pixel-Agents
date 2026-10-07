"""PETME2 Cat Town: build one episode.

Rules of the series:
  - every new follower  -> 1 new cat + 1 new house
  - most-liked comment  -> we build whatever it asks for

Usage:
  python3 build_episode.py --day 2 --new-followers 7 --comment "build a cat cafe" --by "@anna"
  python3 build_episode.py --day 1 --new-followers 1 --first-day

Reads/updates town-state.json (the town keeps growing), writes episode.json (for town.html)
and voice.json (lines + start times for the voiceover).
"""
import argparse, json, math, random, re
from pathlib import Path

HERE = Path(__file__).parent
STATE = HERE / "town-state.json"

ROOFS = ["#2F5FE0", "#4F7BEA", "#1F3FA8", "#FFC93C", "#E85D5D", "#5BB98C", "#9B6FE0"]
WALLS = ["#FFFFFF", "#FFF4E6", "#EEF3FB", "#FDF2F2"]
CAT_COLORS = ["#F2A65A", "#8E8E9A", "#3B3B44", "#FFFFFF", "#D9A066", "#C47A4A", "#E8D5B5"]
KINDS = [
    ("cafe", r"caf[eé]|coffee|bakery|restaurant|food"),
    ("market", r"fish|market|shop|store|mall"),
    ("cattree", r"cat ?tree|scratch|climb|tower for cats"),
    ("statue", r"statue|monument|memorial"),
    ("pool", r"pool|lake|pond|beach|swim"),
    ("tower", r"tower|skyscraper|castle|hotel|apartment"),
    ("vet", r"vet|hospital|doctor|clinic"),
    ("park", r"park|playground|garden|field"),
    ("fountain", r"fountain|water"),
]


HIGHLIGHT = {"cats", "cat", "you", "follower", "followers", "house", "houses", "mango", "comment", "anything",
             "fountain", "built", "follow", "tomorrow", "build"}


def article(thing):
    """'a cat cafe' / 'an ice cream shop' / plurals and names get none."""
    t = thing.lower()
    if t.endswith("s") or t.split()[0] in ("more", "some", "the", "two", "three", "another"):
        return ""
    return "an " if t[0] in "aeiou" else "a "


def script_lines(a, n, build_text, by):
    """Voice script. Short, hooky, ends with the two rules + call to action."""
    if a.first_day:
        return [
            "I'm building a town for cats... and you decide what we build.",
            "Every new follower adds a new cat and a house. Meet Mango, our very first resident!",
            "And every day, the most liked comment builds anything it wants. Mango was thirsty, so day one: a fresh water fountain!",
            "Follow to move your cat in, and comment what we build tomorrow!",
        ]
    who = f" from {by.lstrip('@')}" if by else ""
    cats = "cat just moved in" if n == 1 else "cats just moved in"
    return [
        f"Day {a.day} of building a town for cats... and you decide what we build.",
        f"{n} new {'follower' if n == 1 else 'followers'}, so {n} new {cats}, each with their own house!",
        f"And the most liked comment{who} asked for {article(build_text)}{build_text}... so we built it!",
        "Follow to move your cat in, and comment what we build tomorrow!",
    ]


def kind_for(text):
    t = (text or "").lower()
    for k, pat in KINDS:
        if re.search(pat, t):
            return k
    return "custom"


def short_name(text):
    t = re.sub(r"^(please\s+)?(build|make|add|create)\s+(me\s+)?(a|an|the)?\s*", "", (text or "").strip(), flags=re.I)
    return t.strip(" .!?")[:22] or "something new"


def free_spot(taken, rmin, step, seed, min_dist):
    """Golden-angle spiral: first point that keeps min_dist from everything taken."""
    golden = math.pi * (3 - math.sqrt(5))
    i = 0
    while True:
        r = rmin + step * math.sqrt(i)
        a = i * golden + seed
        x, z = r * math.cos(a), r * math.sin(a)
        if all((x - tx) ** 2 + (z - tz) ** 2 >= (min_dist + tr) ** 2 for tx, tz, tr in taken):
            return round(x, 2), round(z, 2)
        i += 1


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"day": 0, "houses": [], "buildings": [], "cats": [], "followers": 0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--day", type=int, required=True)
    ap.add_argument("--new-followers", type=int, default=0)
    ap.add_argument("--comment", default="")
    ap.add_argument("--by", default="")
    ap.add_argument("--first-day", action="store_true")
    ap.add_argument("--reset", action="store_true", help="start the town from zero")
    ap.add_argument("--print-script", action="store_true", help="only print the voice lines (for TTS), change nothing")
    ap.add_argument("--timings", help="voice-timings.json from the TTS step (durations + word times)")
    ap.add_argument("--comments", help="JSON list of REAL comments [{by,text,likes,ago}] from the post; the winner = most likes")
    a = ap.parse_args()

    st = {"day": 0, "houses": [], "buildings": [], "cats": [], "followers": 0} if a.reset else load_state()
    rnd = random.Random(1000 + a.day)
    taken = [(0.0, 0.0, 2.6)] + [(h["x"], h["z"], .45) for h in st["houses"]] + [(b["x"], b["z"], 1.8) for b in st["buildings"]]
    for h in st["houses"]: h.pop("appear", None)
    for b in st["buildings"]: b.pop("appear", None)
    for c in st["cats"]: c.pop("appear", None)

    # ---- script (what the voice says) ----
    n = max(0, a.new_followers)
    build_text, by = ("fresh water fountain", "") if a.first_day else (short_name(a.comment), a.by)
    lines = script_lines(a, n, build_text, by)
    if a.print_script:
        print(json.dumps(lines)); return

    # ---- timeline from the real voice timings (gap 0.3 s between lines) ----
    tim = json.loads(Path(a.timings).read_text())
    # with a comments sheet, leave a 1.6 s beat before the "most liked comment" line so viewers see it scroll
    starts, t0 = [], 0.2
    for li, d in enumerate(tim["durs"]):
        if li == 2 and a.comments: t0 += 1.3
        starts.append(round(t0, 3)); t0 += d + 0.3
    duration = round(t0 + 1.0, 2)
    words = []
    for li, ws in enumerate(tim["words"]):
        for j, (w, s, e) in enumerate(ws):
            words.append({"w": w, "s": round(starts[li] + s, 3), "e": round(starts[li] + e, 3), "line": li,
                          "hl": w.lower().strip(".,!?") in HIGHLIGHT})
    def at(li, word, default):
        for x in words:
            if x["line"] == li and x["w"].lower().strip(".,!?") == word: return x["s"]
        return starts[li] + default
    t_houses = at(1, "house", 1.5) - .25 if a.first_day else starts[1] + .2
    pop_span = 0 if a.first_day else min(tim["durs"][1] - 1.0, max(1.2, n * 0.35))
    t_build = at(2, "fresh", 6) - .3 if a.first_day else at(2, "built", tim["durs"][2] - 1.2) - .5
    t_end = starts[3]

    # ---- new houses + cats ----
    for i in range(n):
        x, z = free_spot(taken, 3.6, 1.0, -1.75, 2.1)
        taken.append((x, z, .45))
        appear = round(t_houses + (pop_span * i / max(1, n)), 2)
        st["houses"].append({"x": x, "z": z, "ry": round(math.atan2(-x, -z), 2),
                             "roof": rnd.choice(ROOFS), "wall": rnd.choice(WALLS), "appear": appear, "day": a.day})
        ang = math.atan2(z, x)
        cat_t = at(1, "meet", 3) if a.first_day else appear + .3
        st["cats"].append({"x": round(x - 1.0 * math.cos(ang), 2), "z": round(z - 1.0 * math.sin(ang), 2),
                           "color": "#F2A65A" if a.first_day else rnd.choice(CAT_COLORS), "appear": round(cat_t - 1.4, 2),
                           "fromX": round(x * 1.0 + 6 * math.cos(ang), 2), "fromZ": round(z + 6 * math.sin(ang), 2)})

    # ---- the build ----
    if a.first_day:
        kind = "fountain"; x, z = 0.0, 0.0
    else:
        kind = kind_for(a.comment)
        x, z = free_spot(taken, 5.0, 1.4, 2.1, 3.2)
        taken.append((x, z, 1.8))
    st["buildings"].append({"kind": kind, "x": x, "z": z, "ry": round(math.atan2(-x, -z), 2) if (x or z) else 0,
                            "sign": "" if kind == "fountain" else build_text, "appear": round(t_build, 2),
                            "day": a.day, "by": by, "request": a.comment})

    # ---- island size, trees, camera ----
    far = max([math.hypot(h["x"], h["z"]) for h in st["houses"]] + [math.hypot(b["x"], b["z"]) + 1 for b in st["buildings"]] + [6.0])
    R = round(max(9.0, far + 2.6), 2)
    trng = random.Random(7)
    trees = []
    for _ in range(int(R * 1.3)):
        for _try in range(40):
            ang, r = trng.uniform(0, 2 * math.pi), trng.uniform(R * .62, R - .8)
            tx, tz = r * math.cos(ang), r * math.sin(ang)
            if all((tx - x0) ** 2 + (tz - z0) ** 2 >= (rr + 1.1) ** 2 for x0, z0, rr in taken):
                trees.append({"x": round(tx, 2), "z": round(tz, 2), "s": round(trng.uniform(.8, 1.2), 2)}); break
    k = R / 9.0

    st["day"] = a.day
    st["followers"] = st.get("followers", 0) + n
    STATE.write_text(json.dumps(st, indent=1))

    badges = []
    if n:
        badges.append({"from": t_houses, "to": starts[2] - .1, "html": f"+{n} new {'follower' if n == 1 else 'followers'} = +{n} {'cat' if n == 1 else 'cats'}"})
    badges.append({"from": starts[2], "to": t_end - .1,
                   "html": "Most-liked comment builds anything!" if a.first_day else (f"Top comment by {by}" if by else "Top comment")})

    comments = None
    if a.comments:
        lst = json.loads(Path(a.comments).read_text())
        win_c = max(lst, key=lambda c: c["likes"])
        others = [c for c in lst if c is not win_c][:5]
        ordered = others[:3] + [win_c] + others[3:]          # winner shows after a short scroll
        up = starts[2] - 1.6
        comments = {"list": ordered, "win": ordered.index(win_c),
                    "t": {"up": up, "scroll": up + .5, "stop": up + 2.0, "down": t_build - .5}}
    ep = {"day": a.day, "comments": comments, "duration": round(duration, 2), "islandRadius": R, "trees": trees,
          "houses": st["houses"], "buildings": st["buildings"], "cats": st["cats"],
          "words": words, "badges": badges, "timeline": {"end": t_end},
          "camera": {"angFrom": -.35, "angTo": .75, "rFrom": round(40 * k, 1), "rTo": round(29 * k, 1),
                     "yFrom": round(30 * k, 1), "yTo": round(19 * k, 1)}}
    (HERE / "episode.json").write_text(json.dumps(ep, indent=1))
    (HERE / "voice.json").write_text(json.dumps({"day": a.day, "duration": duration, "starts": starts, "lines": lines}, indent=1))
    print(f"Day {a.day}: +{n} houses/cats, build={kind} ('{build_text}'), town now {len(st['houses'])} houses, R={R}, {ep['duration']}s")


if __name__ == "__main__":
    main()
