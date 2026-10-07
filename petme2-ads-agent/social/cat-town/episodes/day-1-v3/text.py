# Voice timeline + on-screen text for Day 1 v3 -> DIR/text.json, DIR/timeline.json (subtitles on for every line)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'd'
L = json.load(open(f'{out}/lines.json'))
START = [0.15, 2.6, 4.85, 6.4, 8.0, 10.5, 12.25, 14.6]
lines = []
for l, s in zip(L, START):
    ws = l['text'].split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False))
HOOK = 'POPULATION:<br><y>1 CAT</y>'
beats = [
 dict(s=0.0, e=2.6, html=HOOK, still=True),
 dict(s=2.6, e=4.5, html='FRIENDS: <r>0</r>'),
 dict(s=4.5, e=6.3, html='<y>1 FOLLOW</y><br>= 1 NEW CAT'),
 dict(s=6.3, e=7.8, html='+ A HOUSE WITH<br><y>YOUR NAME</y>'),
 dict(s=7.8, e=10.4, html='TOP COMMENT<br>= <y>WE BUILD IT</y>'),
 dict(s=10.4, e=12.0, html='ANYTHING.<br><y>YOU DECIDE.</y>'),
 dict(s=12.0, e=14.4, html="LET'S BUILD<br>A <y>CAT TOWN</y>"),
 dict(s=14.4, e=17.0, html='COMMENT<br><y>BELOW</y> 👇', small='Top comment gets built', ss=15.0, small2='Follow = 1 new cat 🐱', ss2=15.8),
 dict(s=17.0, e=99, html=HOOK),
]
json.dump(dict(duration=17.6, day=1, cats=1, lines=lines, beats=beats, goal=[12.0, 14.4], hideTags=[[7.8, 10.4]],
               example=[[5.5, 7.8, 'house'], [9.05, 10.4, 'statue']]), open(f'{out}/text.json', 'w'), indent=1)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
