# Voice timeline + on-screen text for viral-1 -> DIR/text.json, DIR/timeline.json (subtitles on for every line)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.1, 2.35, 4.0, 5.32, 6.42, 8.0, 10.75, 13.55]
lines = []
for l, s in zip(L, START):
    ws = l['text'].split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False))
HOOK = 'POPULATION:<br><y>1 CAT</y> 😿'
beats = [
 dict(s=0.0, e=2.2, html=HOOK, still=True),
 dict(s=2.2, e=4.0, html='FRIENDS:<br><r>ZERO</r> 💔'),
 dict(s=4.0, e=5.25, html='<y>1 FOLLOW</y><br>= 1 NEW CAT 🐱'),
 dict(s=5.25, e=7.8, html='+ A HOUSE WITH<br><y>YOUR NAME</y> 🏠'),
 dict(s=7.8, e=10.6, html='HELP HIM GET<br>TO <y>1,000</y> 🙏'),
 dict(s=10.6, e=13.4, html='COMMENT<br><y>YOUR NAME</y> 👇', small="I'll build YOUR house next!", ss=10.9),
 dict(s=13.4, e=14.45, html='BECAUSE<br><y>RIGHT NOW</y>...'),
 dict(s=14.45, e=99, html=HOOK, still=True),
]
# grade: cool grey when Mango is alone, warm when the town fills (CSS filter on the engine canvas)
SAD = 'saturate(.38) brightness(.9) contrast(1.04)'; WARM = 'saturate(1.22) brightness(1.04) sepia(.1)'
grade = [[0, 4.0, SAD, 1], [4.0, 13.4, WARM, 0], [13.4, 99, SAD, 1]]
chips = [[11.3, 'Noa'], [11.75, 'Leo'], [12.2, 'Maya']]
json.dump(dict(duration=14.8, day=1, cats=1, lines=lines, beats=beats, goal=[7.8, 10.6], roll=[7.85, 10.1, 1, 1000], grade=grade, chips=chips, flash=4.0, pops=[4.6, 5.45, 6.19], bubbles=[[0.5, 2.2, 'anyone? 🥺'], [13.9, 14.45, 'anyone? 🥺']],
               pinTags=[[4.4, 7.8]], example=[[4.5, 7.8, 'house'], [11.0, 13.4, 'chips']]), open(f'{out}/text.json', 'w'), indent=1)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
