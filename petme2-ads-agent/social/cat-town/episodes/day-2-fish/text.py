# Voice timeline + on-screen text for Day 2 -> DIR/text.json, DIR/timeline.json (subtitles on for every line)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.15, 1.85, 4.45, 5.75, 7.3, 8.85, 11.1, 13.1, 14.85, 16.3]
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
 dict(s=4.4, e=5.6, html='WE DID <r>NOT</r><br>EXPECT THAT! 🙀'),
 dict(s=5.6, e=8.6, html="THE MOST<br><y>LIKED COMMENT</y> 👑"),
 dict(s=8.6, e=11.0, html='<y>BUILT!</y> 🎉🐟', small='“add a fish supermarket” ✅', ss=9.3, smallTop=1300),
 dict(s=11.0, e=13.0, html='THE <y>ONLY</y> BUILDING<br>IN TOWN 🐟', arrowDown=True),
 dict(s=13.0, e=14.8, html='<y>1 FOLLOW</y><br>= 1 NEW CAT'),
 dict(s=14.8, e=16.2, html="LET'S BUILD IT<br><y>TOGETHER</y>"),
 dict(s=16.2, e=17.9, html='WHAT DO WE<br>BUILD <y>NEXT?</y> 👇', small='Top comment gets built', ss=16.6),
 dict(s=17.9, e=99, html=HOOK),
]
json.dump(dict(duration=18.3, day=2, cats=1, followers=128, roll=[1.9, 3.3], lines=lines, beats=beats, goal=[99, 99], hideTags=[[11.0, 99]], pinTags=[[8.6, 11.0]], example=[]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
