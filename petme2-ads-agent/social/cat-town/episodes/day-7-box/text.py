# Voice timeline + on-screen text for Day 7 -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.3, 3.0, 7.05, 10.1, 10.95, 11.8, 12.65, 13.5, 14.35, 15.75, 18.7, 21.0, 23.75, 25.4, 27.35, 28.4]
SHOW = {1: 'wil.son said: a giant box... for all the cats!', 11: 'Today, 321 followers. Thank you!'}
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=SHOW.get(l['i'], l['text']), s=s, e=round(s + l['dur'], 3), words=words))
for a, b in zip(lines, lines[1:]): assert a['e'] < b['s'], (a['text'], a['e'], b['s'])
D = 32.0; assert lines[-1]['e'] < D
HOOK = 'DAY 7:<br>A <y>GIANT BOX</y><br>FOR ALL THE CATS 📦'
TOPS = [(10.1, '📦 GIANT BOX!'), (10.95, 'FLAPS OPEN'), (11.8, 'CAT DOORS 🚪'), (12.65, 'PEEK HOLES 👀'), (13.5, 'SCRATCH RAMP'), (14.35, 'PARTY FLAGS 🎉')]
beats = [dict(s=0, e=1.0, html=HOOK, still=True),
         dict(s=1.0, e=2.9, html='DAY 7 📦'),
         dict(s=2.9, e=7.0, html='THE MOST<br><y>LIKED COMMENT</y> 👑'),
         dict(s=7.0, e=9.9, html='MANGO<br><y>LOVES BOXES</y> 📦')]
for k, (s, h) in enumerate(TOPS): beats.append(dict(s=s - .1, e=(TOPS[k + 1][0] - .1) if k + 1 < len(TOPS) else 15.6, html=h, pop=True))
beats += [dict(s=15.6, e=18.6, html='ALL THE CATS...<br><y>GET IN!</y> 🐾', pop=True),
          dict(s=18.6, e=23.6, html='<y>1 WEEK</y><br>OF CAT TOWN 🎂', small='321 followers · 562 likes 💛', ss=21.0, smallTop=700),
          dict(s=23.6, e=25.3, html='WAIT...<br>WHERE\'S <y>MANGO?</y> 👀'),
          dict(s=25.3, e=28.3, html='MANGO...<br>YOU HAVE A<br><y>GIANT BOX!</y> 😹'),
          dict(s=28.3, e=D, html='FOLLOW = <y>YOUR HOUSE</y> 🏠<br>TOP COMMENT<br>= <y>WE BUILD IT</y> 💬'),
          dict(s=D, e=99, html=HOOK, still=True)]
json.dump(dict(duration=D, day=7, build=[9.9, 15.35], lines=lines, beats=beats, tagOn=[16.2, 18.6]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
