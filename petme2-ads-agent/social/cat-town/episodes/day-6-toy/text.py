# Voice timeline + on-screen text for Day 6 -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.3, 3.0, 7.05, 10.1, 10.9, 11.75, 12.9, 13.75, 14.6, 15.75, 16.95, 20.6, 22.65, 24.4, 25.4]
SHOW = {1: 'bean said: can we get a huge cat toy statue... for the cats to play with?'}
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=SHOW.get(l['i'], l['text']), s=s, e=round(s + l['dur'], 3), words=words))
for a, b in zip(lines, lines[1:]): assert a['e'] < b['s'], (a['text'], a['e'], b['s'])
D = 29.0; assert lines[-1]['e'] < D
HOOK = 'DAY 6:<br>A <y>HUGE CAT TOY</y><br>STATUE 🧶'
TOPS = [(10.1, '📦 DELIVERY!'), (10.9, 'PEDESTAL'), (11.75, 'YARN BALL 🧶'), (12.9, 'FEATHER WAND'), (13.75, 'TOY MOUSE 🐭'), (14.6, 'JINGLE BELLS 🔔')]
beats = [dict(s=0, e=1.0, html=HOOK, still=True),
         dict(s=1.0, e=2.9, html='DAY 6 🧶'),
         dict(s=2.9, e=7.0, html='THE MOST<br><y>LIKED COMMENT</y> 👑'),
         dict(s=7.0, e=9.9, html='AS BIG AS<br>A <y>BUILDING?!</y> 😳')]
for k, (s, h) in enumerate(TOPS): beats.append(dict(s=s - .1, e=(TOPS[k + 1][0] - .1) if k + 1 < len(TOPS) else 15.6, html=h, pop=True))
beats += [dict(s=15.6, e=16.9, html='CATS...<br><y>GO PLAY!</y> 🐾', pop=True),
          dict(s=16.9, e=20.5, html='THE <y>HUGE CAT TOY</y><br>IS DONE! 🎉', small='every cat loves it 😻', ss=18.2, smallTop=700),
          dict(s=20.5, e=22.5, html='...<y>ALMOST</y> 👀', small='almost every cat', ss=21.0, smallTop=640),
          dict(s=22.5, e=25.3, html='MANGO,<br>REALLY?! <y>THE BOX?!</y> 📦'),
          dict(s=25.3, e=D, html='FOLLOW = <y>YOUR HOUSE</y> 🏠<br>TOP COMMENT<br>= <y>WE BUILD IT</y> 💬'),
          dict(s=D, e=99, html=HOOK, still=True)]
json.dump(dict(duration=D, day=6, build=[9.9, 15.35], lines=lines, beats=beats, tagOn=[16.2, 18.7]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
