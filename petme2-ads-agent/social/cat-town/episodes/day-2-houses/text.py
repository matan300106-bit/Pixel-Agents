# Voice timeline + on-screen text for "every follower gets a house" -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.15, 2.6, 4.4, 7.45, 8.9, 10.6, 11.9, 13.75]
SHOW = {2: 'Today? We have 128 new cats in town!'}   # caption text when it differs from the spoken words
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False))
HOOK = 'DAY 2 OF BUILDING<br>A <y>TIKTOK</y><br><y>CAT TOWN</y> 🐱'
beats = [
 dict(s=0.0, e=2.45, html=HOOK, still=True),
 dict(s=2.45, e=4.3, html='YESTERDAY?<br>JUST <y>MANGO</y> 🐱'),
 dict(s=4.3, e=7.35, html='TODAY?<br><y>128</y> NEW CATS! 😱'),
 dict(s=7.35, e=8.7, html='WE DID <r>NOT</r><br>EXPECT THAT! 🙀'),
 dict(s=8.7, e=10.55, html='<y>1 FOLLOW</y><br>= 1 HOUSE 🏠'),
 dict(s=10.55, e=11.7, html='WITH <y>YOUR NAME</y><br>ON IT 🏷️'),
 dict(s=11.7, e=13.65, html='MANGO IS<br><y>NOT ALONE</y><br>ANYMORE 🐱💛'),
 dict(s=13.65, e=16.4, html='THE ONLY THING<br>MISSING IS <y>YOU</y> 🫵', small='Follow = your house 🏠', ss=15.0),
 dict(s=16.4, e=99, html=HOOK),
]
json.dump(dict(duration=17.0, day=2, houses=True, cats=1, followers=0, roll=[0, 0], lines=lines, beats=beats, goal=[99, 99], hideTags=[[0, 9.1], [11.6, 99]], pinTags=[], example=[]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
