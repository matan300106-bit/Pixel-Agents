# Voice timeline + on-screen text for the "Be OK" video with voice (22 s) -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.05, 3.15, 6.2, 8.1, 9.5, 11.75, 14.5, 17.45, 17.8, 19.3, 20.95]
tl = [dict(i=l['i'], s=s, e=round(s + l['dur'], 3)) for l, s in zip(L, START)]
for a, b in zip(tl, tl[1:]): assert a['e'] <= b['s'] + .01, (a, b)
cards = [
 dict(s=0.0, e=3.1, html="POV: you're the mayor of a cat city <b>the internet controls</b>"),
 dict(s=3.1, e=6.1, html='rule 1: you follow = you get a house with <b>YOUR name</b> on it 🏠', sub='(128 houses)', ss=4.8),
 dict(s=6.1, e=9.4, html='rule 2: every like = a <b>new cat</b> 🐱', count=True),
 dict(s=9.4, e=11.6, html='194 cats − 128 houses =', sub='66 cats with <b>no home</b>', ss=9.9),
 dict(s=11.6, e=14.4, html='they live in the <b>fish supermarket</b> now', sub="it's fine 🙂", ss=13.6),
 dict(s=14.4, e=19.1, html='rule 3: top comment gets <b>built every day</b>', sub='the fish store WAS a comment.', ss=17.8),
 dict(s=19.1, e=22.0, html='comment what we build tomorrow 👇', sub='(please say houses)', ss=20.95),
]
json.dump(dict(duration=22.0, cards=cards, tags=[[3.1, 6.1]]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump(tl, open(f'{out}/timeline.json', 'w'))
for x in tl: print(x)
