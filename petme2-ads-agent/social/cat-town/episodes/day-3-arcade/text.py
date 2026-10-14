# Voice timeline + on-screen text for Day 3 -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.4, 3.1, 7.0, 9.15, 10.4, 14.6, 16.7, 18.6, 19.35, 20.15, 20.95, 22.45, 25.1, 28.9]
SHOW = {4: 'Today: 253 houses, and 467 cats!'}   # caption text when it differs from the spoken words
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words))
for a, b in zip(lines, lines[1:]): assert a['e'] < b['s'], (a['text'], a['e'], b['s'])
HOOK = 'DAY 3:<br>WE BUILT A<br><y>CAT ARCADE</y> 🕹️'
beats = [
 dict(s=0, e=3.0, html=HOOK, still=True),
 dict(s=3.0, e=6.9, html='THE MOST<br><y>LIKED COMMENT</y> 👑'),
 dict(s=6.9, e=9.0, html='<y>FRANCISCO,</y><br>THIS ONE IS<br>FOR YOU! 💛'),
 dict(s=14.5, e=16.6, html='WAIT... <r>MORE</r><br><r>CATS</r> THAN<br>HOUSES! 🙀'),
 dict(s=16.6, e=18.45, html='BUT FIRST...<br><y>THE ARCADE!</y> 🕹️'),
 dict(s=18.45, e=21.62, html="LET'S <y>BUILD IT!</y> 🚧"),
 dict(s=21.62, e=22.9, html='<y>LIGHTS ON!</y> ✨'),
 dict(s=22.9, e=25.7, html='THE <y>CAT ARCADE</y><br>IS OPEN! 🕹️', small='Mango won a fish! 🐟', ss=24.3, smallTop=760),
 dict(s=25.7, e=27.2, html='FOLLOW<br>= <y>1 CAT HOUSE</y> 🏠'),
 dict(s=27.2, e=28.7, html='TOP COMMENT<br>= <y>WE BUILD IT</y> 🔨'),
 dict(s=28.7, e=30.3, html='DAY 4:<br><y>YOUR IDEA?</y> 👇', small='Comment it 💬', ss=29.3, smallTop=760),
 dict(s=30.3, e=99, html=HOOK, still=True),
]
json.dump(dict(duration=31.2, day=3, houses=253, cats=467, split=[9.0, 14.5], roll=[10.9, 14.1], build=[18.55, 21.62], lines=lines, beats=beats,
               counterFrom=9.0), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
