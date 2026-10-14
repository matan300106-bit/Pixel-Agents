# Voice timeline + on-screen text for Day 2 (Matan's script) -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
SH, T0 = 2.05, 16.8
sh_ = lambda x: x + SH if x >= T0 and x < 90 else x
START = [0.5, 3.3, 6.0, 7.55, 9.0, 10.3, 12.9, 15.75, 17.0] + [sh_(x) for x in [17.0, 21.1, 27.2, 29.6, 31.8]]
SHOW = {6: 'Today? We have 246 new cats in town!', 9: 'Welcome our very first house: @idkhima, on Meowstache Avenue!'}   # caption text when it differs from the spoken words
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False))
HOOK = 'DAY 2 OF BUILDING<br>THE FIRST <y>TIKTOK</y><br><y>CAT TOWN</y> 🐱'
beats = [
 dict(s=sh_(0.0), e=sh_(3.2), html=HOOK, still=True),
 dict(s=sh_(3.2), e=sh_(5.85), html='<y>1 FOLLOWER</y><br>= 1 CAT HOUSE 🏠'),
 dict(s=sh_(5.85), e=sh_(8.9), html="THE MOST<br><y>LIKED COMMENT</y> 👑"),
 dict(s=sh_(8.9), e=sh_(10.2), html='BUT WAIT...<br><y>ONE MOMENT</y> ✋'),
 dict(s=sh_(10.2), e=sh_(12.85), html='YESTERDAY?<br>JUST <y>MANGO</y> 🐱', small='and an empty road 🛣️', ss=sh_(11.6)),
 dict(s=sh_(12.85), e=sh_(15.6), html='TODAY?<br><y>246</y> NEW CATS! 😱'),
 dict(s=15.6, e=16.9, html='WE DID <r>NOT</r><br>EXPECT THAT! 🙀'),
 dict(s=16.9, e=18.85, html='MANGO IS<br><y>NOT ALONE</y><br>ANYMORE 🐱💛'),
 dict(s=sh_(16.9), e=sh_(21.0), html='OUR <y>FIRST</y><br>CAT HOUSE 🏠'),
 dict(s=sh_(21.0), e=sh_(22.3), html="LET'S BUILD<br>THE <y>TOP COMMENT</y> 🚧"),
 dict(s=sh_(22.3), e=sh_(26.8), html="LET'S <y>BUILD IT!</y> 🚧"),
 dict(s=sh_(26.8), e=sh_(27.6), html='<y>BUILT!</y> 🎉🐟', small='“add a fish supermarket” ✅', ss=sh_(27.0), smallTop=1300),
 dict(s=sh_(27.6), e=sh_(29.5), html='TOP COMMENT<br>EVERY DAY<br>= <y>WE BUILD IT</y>'),
 dict(s=sh_(29.5), e=sh_(31.6), html='FOLLOW<br>= <y>+1 CAT HOUSE</y> 🏠'),
 dict(s=sh_(31.6), e=sh_(34.5), html='ARE YOU<br><y>COMING?</y> 👇', small='Follow to move in 🐱', ss=sh_(33.0)),
 dict(s=sh_(34.5), e=sh_(99), html=HOOK),
]
json.dump(dict(duration=37.05, day=2, houses=True, housesTotal=246, cats=1, followers=0, roll=[0, 0], build=[sh_(22.3), sh_(26.8)], firstStreet='Meowstache Ave 🪧', lines=lines, beats=beats, goal=[99, 99],
               hideTags=[[0, sh_(17.6)], [sh_(21.0), 99]], pinTags=[], example=[]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
