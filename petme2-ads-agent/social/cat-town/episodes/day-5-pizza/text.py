# Voice timeline + on-screen text for Day 5 -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.3, 3.0, 7.35, 9.95, 10.6, 11.25, 12.0, 12.75, 13.5, 14.15, 14.8, 15.45, 16.05, 16.65, 17.6, 19.0, 20.4, 22.4, 26.35, 27.2]
SHOW = {1: 'MrFireman said: a giant slice of pizza... with every single topping!'}
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=SHOW.get(l['i'], l['text']), s=s, e=round(s + l['dur'], 3), words=words))
for a, b in zip(lines, lines[1:]): assert a['e'] < b['s'], (a['text'], a['e'], b['s'])
D = 30.6; assert lines[-1]['e'] < D
HOOK = 'DAY 5:<br>A <y>GIANT PIZZA</y><br>WITH <r>EVERY</r> TOPPING 🍕'
TOPS = [(9.95, 'CRUST'), (10.6, 'SAUCE'), (11.25, 'CHEESE 🧀'), (12.0, 'PEPPERONI'), (12.75, 'MUSHROOMS 🍄'), (13.5, 'OLIVES 🫒'), (14.15, 'PEPPERS 🫑'),
        (14.8, 'ONIONS 🧅'), (15.45, 'CORN 🌽'), (16.05, 'BACON 🥓'), (16.65, '<y>EVERYTHING!</y>')]
beats = [dict(s=0, e=1.0, html=HOOK, still=True),
         dict(s=1.0, e=2.9, html='DAY 5 🍕'),
         dict(s=2.9, e=7.2, html='THE MOST<br><y>LIKED COMMENT</y> 👑'),
         dict(s=7.2, e=9.75, html='EVERY.<br>SINGLE.<br><y>TOPPING.</y> 😳')]
for k, (s, h) in enumerate(TOPS): beats.append(dict(s=s - .1, e=(TOPS[k + 1][0] - .1) if k + 1 < len(TOPS) else 17.6, html=h, pop=True))
beats += [dict(s=17.6, e=20.2, html='...<y>PINEAPPLE?!</y> 🍍', small='he said EVERY topping', ss=19.0, smallTop=730),
          dict(s=20.2, e=22.1, html='+ A <y>FISH</y> 🐟', small="it's a cat town", ss=20.9, smallTop=640),
          dict(s=22.1, e=24.6, html='THE <y>GIANT PIZZA</y><br>IS DONE! 🍕'),
          dict(s=24.6, e=27.0, html='MANGO,<br>HOW IS IT? 😋'),
          dict(s=27.0, e=D, html='FOLLOW = <y>YOUR HOUSE</y> 🏠<br>TOP COMMENT<br>= <y>WE BUILD IT</y> 💬'),
          dict(s=D, e=99, html=HOOK, still=True)]
json.dump(dict(duration=D, day=5, build=[9.75, 20.95], lines=lines, beats=beats, tagOn=[21.0, 24.6]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
