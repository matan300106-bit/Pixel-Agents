# Voice timeline + on-screen text for rule-v1 -> v/text.json, v/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.15, 1.75, 3.50, 5.60, 6.45, 8.00, 10.10, 12.75, 15.00]
HIDE = {0, 1, 4, 5, 6, 7}            # these lines say the same as the big headline
lines = []
for l, s in zip(L, START):
    e = s + l['dur']; ws = l['text'].split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(e, 3), words=words, hide=l['i'] in HIDE))
beats = [
 dict(s=0.0, e=1.6, html='TOP COMMENT<br>→ <y>WE BUILD IT</y>', still=True),
 dict(s=1.6, e=3.5, html='EVERY DAY.<br><y>ANYTHING.</y>', small='(the cat version 🐱)', ss=2.3),
 dict(s=3.5, e=6.2, html='MOST LIKES <y>WINS</y>'),
 dict(s=6.2, e=7.9, html='<y>BUILT!</y>'),
 dict(s=7.9, e=9.9, html="Mango's review:<br><y>10/10</y>"),
 dict(s=9.9, e=12.6, html="LET'S BUILD<br>THE CITY <y>TOGETHER</y>"),
 dict(s=12.6, e=14.75, html='TODAY: <y>1 CAT</y><br><r>0 BUILDINGS</r>'),
 dict(s=14.75, e=17.5, html='COMMENT<br><y>YOUR IDEA</y>', small='Most likes in 24 h wins', ss=15.3, small2='Follow to see it built', ss2=16.3, arrow=True),
 dict(s=17.5, e=99, html='TOP COMMENT<br>→ <y>WE BUILD IT</y>'),
]
json.dump(dict(duration=18.2, day=2, cats=1, lines=lines, beats=beats, goal=[9.9, 12.6], example=[[3.5, 5.85, 'card'], [6.2, 7.9, 'build']]), open(f'{out}/text.json', 'w'), indent=1)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
