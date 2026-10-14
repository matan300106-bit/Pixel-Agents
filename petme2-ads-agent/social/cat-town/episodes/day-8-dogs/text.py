# Voice timeline + on-screen text for Day 8 -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.25, 2.0, 5.6, 7.65, 13.7, 16.4, 17.4, 20.35, 21.55, 22.75, 23.95, 25.4, 27.6, 29.45, 34.3, 36.0]
SHOW = {3: 'An army of dogs is marching on Cat Town.', 5: 'MEEEOOOW!', 11: '321 cats.', 12: '150 dogs.'}
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=SHOW.get(l['i'], l['text']), s=s, e=round(s + l['dur'], 3), words=words))
for a, b in zip(lines, lines[1:]): assert a['e'] < b['s'], (a['text'], a['e'], b['s'])
D = 40.0; FREEZE = 34.0; assert lines[-1]['e'] < D
HOOK = 'DAY 8:<br>THE <r>DOGS</r><br>ARE COMING 🐕'
TOPS = [(20.3, '📦 BOX WALL'), (21.5, '🧶 YARN CANNONS'), (22.7, '⛑️ HELMETS ON'), (23.9, '🚩 FLAGS UP')]
beats = [dict(s=0, e=1.6, html=HOOK, still=True),
         dict(s=1.6, e=5.0, html='CAT TOWN 🐱<br><y>PEACEFUL...</y>'),
         dict(s=5.0, e=7.4, html='UNTIL<br><r>TODAY</r> 😨'),
         dict(s=7.4, e=10.8, html='🚨 <r>DOG ARMY</r> 🚨'),
         dict(s=10.8, e=13.6, html='150 DOGS<br><r>MARCHING IN</r> 🐕'),
         dict(s=13.6, e=16.35, html='MANGO\'S<br><y>BATTLE CRY</y>'),
         dict(s=16.35, e=17.0, html='<y>MEOOOW!!</y>', pop=True),
         dict(s=17.0, e=20.2, html='EVERY CAT<br><y>IN TOWN</y> 🐱🐱🐱')]
for k, (s, h) in enumerate(TOPS): beats.append(dict(s=s - .1, e=(TOPS[k + 1][0] - .1) if k + 1 < len(TOPS) else 25.2, html=h, pop=True))
beats += [dict(s=25.2, e=27.45, html='<y>321</y> CATS 🐱', small='1 follower = 1 cat', ss=25.6),
          dict(s=27.45, e=29.3, html='<r>150</r> DOGS 🐶', pop=True),
          dict(s=29.3, e=32.5, html='FACE<br><r>TO FACE</r> 😳'),
          dict(s=FREEZE, e=99, html='', tbc=True)]
json.dump(dict(duration=D, freeze=FREEZE, day=8, build=[20.3, 24.9], lines=lines, beats=beats), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
