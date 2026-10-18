# Voice timeline + on-screen text for Day 9 (Part 2) -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.2, 1.5, 3.8, 6.55, 9.5, 11.0, 20.0, 23.3, 26.8, 30.0, 32.9, 36.3, 41.0, 43.6, 45.5]
SHOW = {1: 'Cats of Cat Town...', 4: 'NEVER!', 7: '321 cats... watching the dark.'}
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=SHOW.get(l['i'], l['text']), s=s, e=round(s + l['dur'], 3), words=words, who=dict(am_onyx='dog', af_heart='mango').get(l['voice'], '')))
for a, b in zip(lines, lines[1:]): assert a['e'] < b['s'], (a['text'], a['e'], b['s'])
D = 48.5; FREEZE = 43.3; assert lines[-1]['e'] < D
beats = [dict(s=0, e=1.4, html='PART 2 🐕<br><y>WHAT DID HE SAY?</y>', still=True),
         dict(s=1.4, e=3.8, html='THE DOG<br>GENERAL <r>SPEAKS</r>'),
         dict(s=3.8, e=6.4, html='"GIVE US YOUR<br><r>FOUNTAIN</r>" 💧', pop=True),
         dict(s=6.4, e=9.2, html='THE <y>FOUNTAIN</y> 💧', small='the heart of Cat Town', ss=7.3),
         dict(s=9.45, e=10.8, html='<y>NEVER!</y> 😾', pop=True),
         dict(s=12.3, e=14.4, html='"AT <r>SUNRISE</r>...<br>WE ATTACK" 🌅', pop=True),
         dict(s=14.45, e=16.8, html='<r>AWOOOOO!</r> 🐺', pop=True),
         dict(s=16.8, e=19.6, html='THE <r>ATTACK</r>:<br>AT SUNRISE 🌅'),
         dict(s=19.6, e=23.0, html='NOBODY<br><y>SLEPT</y> 🌙'),
         dict(s=23.0, e=26.6, html='<y>321</y> PAIRS<br>OF EYES 👀', small='1 follower = 1 cat', ss=24.0),
         dict(s=26.6, e=32.6, html='MANGO SENDS<br>A <y>SPY</y> 🕵️'),
         dict(s=32.6, e=36.0, html='🤫 <y>SHHH...</y>'),
         dict(s=36.0, e=39.2, html='THE <r>DOG CAMP</r> 🔥'),
         dict(s=FREEZE, e=99, html='', tbc=True)]
json.dump(dict(duration=D, freeze=FREEZE, day=9, clock=[16.8, FREEZE], lines=lines, beats=beats), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
