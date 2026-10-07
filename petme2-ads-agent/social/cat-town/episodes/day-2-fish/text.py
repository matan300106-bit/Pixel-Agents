# Voice timeline + on-screen text for Day 2 -> DIR/text.json, DIR/timeline.json (subtitles on for every line)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.15, 1.5, 3.4, 5.75, 7.05, 8.5, 10.9, 13.1, 14.85, 16.3]
lines = []
for l, s in zip(L, START):
    ws = l['text'].split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False))
HOOK = 'CAT TOWN<br><y>DAY 2</y> 🐱'
beats = [
 dict(s=0.0, e=1.4, html=HOOK, still=True),
 dict(s=1.4, e=3.3, html='POPULATION:<br><y>1 CAT</y>'),
 dict(s=3.3, e=5.6, html='TOP COMMENT<br>= <y>WE BUILD IT</y>'),
 dict(s=5.6, e=8.25, html="TODAY'S<br><y>TOP COMMENT</y>"),
 dict(s=8.25, e=10.8, html='<y>BUILT!</y> 🎉🐟'),
 dict(s=10.8, e=13.0, html='NOW HE NEEDS<br><y>FRIENDS</y> 🥺'),
 dict(s=13.0, e=14.8, html='<y>1 FOLLOW</y><br>= 1 NEW CAT'),
 dict(s=14.8, e=16.2, html="LET'S BUILD IT<br><y>TOGETHER</y>"),
 dict(s=16.2, e=17.9, html='WHAT DO WE<br>BUILD <y>NEXT?</y> 👇', small='Top comment gets built', ss=16.6),
 dict(s=17.9, e=99, html=HOOK),
]
json.dump(dict(duration=18.3, day=2, cats=1, lines=lines, beats=beats, goal=[99, 99], hideTags=[[10.8, 99]], pinTags=[[8.25, 10.8]], example=[]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
