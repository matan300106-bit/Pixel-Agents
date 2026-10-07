# Voice timeline + on-screen text for Day 1 v4 -> DIR/text.json, DIR/timeline.json (subtitles on for every line)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'f'
L = json.load(open(f'{out}/lines.json'))
START = [0.15, 1.15, 3.2, 4.25, 5.15, 6.8, 8.6, 10.3, 12.75, 14.85, 17.4]
lines = []
for l, s in zip(L, START):
    ws = l['text'].split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False))
HOOK = 'THIS IS<br><y>MANGO</y> 🐱'
beats = [
 dict(s=0.0, e=1.0, html=HOOK, still=True),
 dict(s=1.0, e=3.0, html='POPULATION:<br><y>1 CAT</y>'),
 dict(s=3.0, e=4.1, html='WATER? <y>YES</y> ✅'),
 dict(s=4.1, e=5.0, html='FOOD? <y>YES</y> ✅'),
 dict(s=5.0, e=6.6, html='FRIENDS: <r>0</r>'),
 dict(s=6.6, e=8.6, html='<y>1 FOLLOW</y><br>= 1 NEW CAT'),
 dict(s=8.6, e=10.0, html='+ A HOUSE WITH<br><y>YOUR NAME</y>'),
 dict(s=10.0, e=12.6, html='TOP COMMENT<br>= <y>WE BUILD IT</y>'),
 dict(s=12.6, e=14.6, html='<y>BUILT!</y> 🎉'),
 dict(s=14.6, e=17.0, html="LET'S BUILD<br>A <y>CAT TOWN</y>"),
 dict(s=17.0, e=19.9, html='COMMENT<br><y>BELOW</y> 👇', small='Top comment gets built', ss=17.6, small2='Follow = 1 new cat 🐱', ss2=18.4),
 dict(s=19.9, e=99, html=HOOK),
]
json.dump(dict(duration=20.4, day=1, cats=1, lines=lines, beats=beats, goal=[14.6, 17.0],
               hideTags=[[12.6, 14.6]], pinTags=[[7.1, 10.0]], example=[[7.3, 10.0, 'house'], [10.05, 12.55, 'card'], [12.6, 14.6, 'statue']]), open(f'{out}/text.json', 'w'), indent=1)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
