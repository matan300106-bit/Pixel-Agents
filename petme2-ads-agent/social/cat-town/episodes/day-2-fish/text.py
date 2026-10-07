# Voice timeline + on-screen text for Day 2 -> DIR/text.json, DIR/timeline.json (subtitles on for every line)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.15, 1.85, 4.45, 5.9, 7.45, 8.75, 13.65, 14.7, 16.5, 18.2, 19.65]
lines = []
SHOW = {1: 'On day one, 128 of you followed.'}   # caption text when it differs from the spoken words
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False))
HOOK = 'DAY 2 OF<br>BUILDING A<br><y>CAT TOWN</y> 🐱'
beats = [
 dict(s=0.0, e=1.8, html=HOOK, still=True),
 dict(s=1.8, e=4.4, html='<y>128</y> FOLLOWERS<br>ON DAY 1 😱'),
 dict(s=4.4, e=5.8, html='WE DID <r>NOT</r><br>EXPECT THAT! 🙀'),
 dict(s=5.8, e=8.75, html="THE MOST<br><y>LIKED COMMENT</y> 👑"),
 dict(s=8.75, e=13.5, html="LET'S <y>BUILD IT!</y> 🚧"),
 dict(s=13.5, e=14.6, html='<y>BUILT!</y> 🎉🐟', small='“add a fish supermarket” ✅', ss=14.0, smallTop=1300),
 dict(s=14.6, e=16.4, html='THE <y>ONLY SHOP</y><br>IN TOWN 🐟', arrowDown=True),
 dict(s=16.4, e=18.1, html='<y>1 FOLLOW</y><br>= 1 NEW CAT'),
 dict(s=18.1, e=19.5, html="LET'S BUILD IT<br><y>TOGETHER</y>"),
 dict(s=19.5, e=21.3, html='WHAT DO WE<br>BUILD <y>NEXT?</y> 👇', small='Top comment gets built', ss=19.9),
 dict(s=21.3, e=99, html=HOOK),
]
json.dump(dict(duration=21.7, day=2, cats=1, followers=128, roll=[1.9, 3.3], build=[9.0, 13.5], lines=lines, beats=beats, goal=[99, 99], hideTags=[[14.6, 99]], pinTags=[[13.5, 14.6]], example=[]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
