# Voice timeline + on-screen text for the story -> DIR/text.json, DIR/timeline.json (subtitles on for every line)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.25, 1.75, 5.15, 6.85, 10.35, 11.75]
lines = []
for l, s in zip(L, START):
    ws = l['text'].split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False, top=1520 if s < 5 else 760 if s >= 10 else None))   # caption y: under Mango, default, above the sticker room
beats = [
 dict(s=0.0, e=1.7, html='THIS IS<br><y>MANGO</y> 🐱', still=True),
 dict(s=1.7, e=5.0, html='POPULATION:<br><y>1 CAT</y>'),
 dict(s=5.0, e=6.85, html='<y>1 FOLLOW</y><br>= 1 NEW CAT', still=True),
 dict(s=6.85, e=10.0, html='+ A HOUSE WITH<br><y>YOUR NAME</y>'),
 dict(s=10.0, e=99, html='WHAT DO WE<br><y>BUILD NEXT?</y>', still=True),
]
json.dump(dict(duration=15.0, day=None, cats=1, lines=lines, beats=beats, goal=[99, 99],
               hideTags=[], pinTags=[[5.5, 10.0]], example=[[5.7, 10.0, 'house']]), open(f'{out}/text.json', 'w'), indent=1)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
