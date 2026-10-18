# Voice timeline + on-screen text for Day 4 -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.3, 4.1, 8.15, 12.15, 17.4, 18.85, 22.45, 23.45, 26.0, 28.95, 32.05]
SHOW = {1: '261 of you followed. That is 261 houses.', 2: 'But 479 of you liked. That is 479 cats.', 3: '479 cats. 261 houses. 218 cats have no home!'}   # captions with digits
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words))
for a, b in zip(lines, lines[1:]): assert a['e'] < b['s'], (a['text'], a['e'], b['s'])
D = 33.8; assert lines[-1]['e'] < D
HOOK = 'DAY 4:<br><r>218 CATS</r><br>HAVE NO HOME 😿'
beats = [
 dict(s=0, e=3.9, html=HOOK, still=True),
 dict(s=3.9, e=8.0, html='1 FOLLOW<br>= <y>1 HOUSE</y> 🏠'),
 dict(s=8.0, e=12.0, html='1 LIKE<br>= <y>1 CAT</y> 🐱'),
 dict(s=12.0, e=17.2, html='479 − 261<br>= <r>218</r>', small='cats with no home 😿', ss=14.6, smallTop=720),
 dict(s=17.2, e=18.75, html='STILL<br><y>WAITING...</y> 🥺'),
 dict(s=18.75, e=22.35, html='THE MOST<br><y>LIKED COMMENT</y> 👑'),
 dict(s=22.35, e=25.4, html="LET'S <y>BUILD IT!</y> 🎨"),
 dict(s=25.4, e=28.7, html='A <y>STATUE</y><br>FOR MANGO! 🏆', small='made by cats with no home', ss=26.6, smallTop=720),
 dict(s=28.7, e=31.9, html='1 FOLLOW<br>= <y>1 MORE HOUSE</y> 🏠'),
 dict(s=31.9, e=D, html='CAN WE GET<br><y>EVERY CAT</y><br>A HOME? 🏠', small='Follow 🐾', ss=32.6, smallTop=800),
 dict(s=D, e=99, html=HOOK, still=True),
]
json.dump(dict(duration=D, day=4, houses=261, cats=479, nohome=218, rollH=[4.3, 7.6], rollC=[8.3, 11.6], nohomeAt=12.3, houseAt=29.6, homeAt=30.6,
               counters=[3.9, 31.9], build=[22.35, 25.35], lines=lines, beats=beats), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
