# Voice timeline + on-screen text for Day 10 (Part 3) -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.2, 1.6, 3.5, 4.5, 6.4, 9.0, 11.5, 13.9, 17.0, 19.9, 21.5, 24.2, 27.0, 31.2, 34.4, 41.6, 43.5, 45.7, 47.6]
SHOW = {12: '321 cats...', 16: 'MEOOOW!', 7: 'Mango! They have... a GIANT!'}
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=SHOW.get(l['i'], l['text']), s=s, e=round(s + l['dur'], 3), words=words, who=dict(am_onyx='dog', af_heart='mango', mega='mango', am_puck='spy').get(l['voice'], '')))
for a, b in zip(lines, lines[1:]): assert a['e'] < b['s'], (a['text'], a['e'], b['s'])
D = 51.6; FREEZE = 45.4; assert lines[-1]['e'] < D
beats = [dict(s=0, e=1.4, html='PART 3 🐕<br><y>WHAT DID HE SEE?</y>', still=True),
         dict(s=1.4, e=3.4, html='A <r>GIANT</r><br>DOG 😱'),
         dict(s=3.4, e=4.5, html='HE <r>SAW</r> HIM 👀', pop=True),
         dict(s=4.5, e=6.4, html='<y>RUN!</y> 🏃', pop=True),
         dict(s=6.4, e=9.4, html='THE DOGS<br><r>WOKE UP</r> 🐕'),
         dict(s=9.4, e=11.6, html='<y>FASTER!</y> 💨', pop=True),
         dict(s=11.6, e=13.7, html='<y>JUMP!</y>', pop=True),
         dict(s=13.7, e=16.8, html='"THEY HAVE<br>A <r>GIANT</r>"', pop=True),
         dict(s=16.8, e=19.6, html='<r>PANIC</r> 😱', pop=True),
         dict(s=19.6, e=21.5, html='MANGO HAS<br>AN <y>IDEA</y> 💡'),
         dict(s=21.5, e=23.6, html='"WE BUILD OUR<br><y>OWN GIANT</y>"', pop=True),
         dict(s=23.6, e=27.0, html='CATS CLIMB ON<br><y>EACH OTHER</y> 🐱', small='1 follower = 1 cat', ss=24.6),
         dict(s=27.0, e=31.0, html='<y>321</y> CATS<br>= ONE GIANT', small='every follow = BIGGER', ss=28.4),
         dict(s=31.0, e=34.2, html='<y>MEGA<br>MANGO</y> 🧡', pop=True),
         dict(s=34.2, e=37.0, html='<y>SUNRISE</y> 🌅', pop=True),
         dict(s=37.0, e=41.4, html='<r>BOOM.</r>', boom=[38.0, 39.0, 40.0, 41.0]),
         dict(s=41.4, e=43.4, html='MEGA MANGO<br><y>STANDS UP</y>'),
         dict(s=43.4, e=FREEZE, html='<y>MEOOOW!</y>', pop=True),
         dict(s=FREEZE, e=99, html='', tbc=True)]
json.dump(dict(duration=D, freeze=FREEZE, day=10, clock=[[1.4, 10000], [19.6, 1200], [23.6, 60], [25.2, 10], [34.4, 0]], sunrise=34.4, lines=lines, beats=beats), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
