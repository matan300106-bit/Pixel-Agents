# Voice timeline + on-screen text for Day 2 (Matan's script) -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.5, 3.3, 6.0, 7.55, 9.0, 10.3, 12.9, 15.65, 17.0, 21.1, 27.2, 29.6, 31.8]
SHOW = {6: 'Today? We have 128 new cats in town!', 8: 'Welcome our very first house: @idkhima, on Meowstache Avenue!'}   # caption text when it differs from the spoken words
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False))
HOOK = 'DAY 2 OF BUILDING<br>THE FIRST <y>TIKTOK</y><br><y>CAT TOWN</y> 🐱'
beats = [
 dict(s=0.0, e=3.2, html=HOOK, still=True),
 dict(s=3.2, e=5.85, html='<y>1 FOLLOWER</y><br>= 1 CAT HOUSE 🏠'),
 dict(s=5.85, e=8.9, html="THE MOST<br><y>LIKED COMMENT</y> 👑"),
 dict(s=8.9, e=10.2, html='BUT WAIT...<br><y>ONE MOMENT</y> ✋'),
 dict(s=10.2, e=12.85, html='YESTERDAY?<br>JUST <y>MANGO</y> 🐱', small='and an empty road 🛣️', ss=11.6),
 dict(s=12.85, e=15.6, html='TODAY?<br><y>128</y> NEW CATS! 😱'),
 dict(s=15.6, e=16.9, html='WE DID <r>NOT</r><br>EXPECT THAT! 🙀'),
 dict(s=16.9, e=21.0, html='OUR <y>FIRST</y><br>CAT HOUSE 🏠'),
 dict(s=21.0, e=22.3, html="LET'S BUILD<br>THE <y>TOP COMMENT</y> 🚧"),
 dict(s=22.3, e=26.8, html="LET'S <y>BUILD IT!</y> 🚧"),
 dict(s=26.8, e=27.6, html='<y>BUILT!</y> 🎉🐟', small='“add a fish supermarket” ✅', ss=27.0, smallTop=1300),
 dict(s=27.6, e=29.5, html='TOP COMMENT<br>EVERY DAY<br>= <y>WE BUILD IT</y>'),
 dict(s=29.5, e=31.6, html='FOLLOW<br>= <y>+1 CAT HOUSE</y> 🏠'),
 dict(s=31.6, e=34.5, html='ARE YOU<br><y>COMING?</y> 👇', small='Follow to move in 🐱', ss=33.0),
 dict(s=34.5, e=99, html=HOOK),
]
json.dump(dict(duration=35.0, day=2, houses=True, cats=1, followers=0, roll=[0, 0], build=[22.3, 26.8], firstStreet='Meowstache Ave 🪧', lines=lines, beats=beats, goal=[99, 99],
               hideTags=[[0, 17.6], [21.0, 99]], pinTags=[], example=[]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
