# Voice timeline + on-screen text for "every follower gets a house" -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.15, 3.0, 4.0, 4.9, 6.4, 9.05, 10.95, 12.2, 13.85]
SHOW = {4: 'On day one, 128 of you followed.', 5: 'So 128 houses!'}   # caption text when it differs from the spoken words
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False))
HOOK = 'EVERY FOLLOWER<br>GETS A <y>HOUSE</y> 🏠'
beats = [
 dict(s=0.0, e=2.8, html=HOOK, still=True),
 dict(s=2.8, e=4.8, html='<y>1 FOLLOW</y><br>= 1 HOUSE'),
 dict(s=4.8, e=6.3, html='WITH <y>YOUR NAME</y><br>ON IT 🏷️'),
 dict(s=6.3, e=9.0, html='<y>128</y> FOLLOWERS<br>ON DAY 1 😱'),
 dict(s=9.0, e=10.9, html='<y>128</y> NEW<br>HOUSES 🏘️'),
 dict(s=10.9, e=12.3, html='WE DID <r>NOT</r><br>EXPECT THAT! 🙀'),
 dict(s=12.1, e=13.75, html='MANGO IS<br><y>NOT ALONE</y><br>ANYMORE 🐱💛'),
 dict(s=13.75, e=16.4, html='THE ONLY THING<br>MISSING IS <y>YOU</y> 🫵', small='Follow = your house 🏠', ss=15.0),
 dict(s=16.4, e=99, html=HOOK),
]
json.dump(dict(duration=17.0, day=2, houses=True, cats=1, followers=0, roll=[0, 0], lines=lines, beats=beats, goal=[99, 99], hideTags=[[6.4, 99]], pinTags=[], example=[]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
