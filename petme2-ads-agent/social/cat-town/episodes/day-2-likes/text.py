# Voice timeline + on-screen text for Day 2 (Matan's script + likes = cats) -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.5, 3.3, 7.2, 8.75, 10.1, 11.4, 14.0, 18.4, 22.05, 25.0, 29.1, 35.3, 37.7, 42.2]
SHOW = {6: 'Today? We have 128 followers, so 128 houses!', 7: 'And 194 likes, so 194 cats!', 12: 'Like = one more cat. Follow = one more house. 66 cats still need a home!', 9: 'Welcome our very first house: @idkhima, on Meowstache Avenue!'}   # caption text when it differs from the spoken words
lines = []
for l, s in zip(L, START):
    ws = SHOW.get(l['i'], l['text']).split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words, hide=False))
HOOK = 'DAY 2 OF BUILDING<br>THE FIRST <y>TIKTOK</y><br><y>CAT TOWN</y> 🐱'
beats = [
 dict(s=0.0, e=3.2, html=HOOK, still=True),
 dict(s=3.2, e=7.05, html='<y>FOLLOW</y> = HOUSE 🏠<br><y>LIKE</y> = CAT 🐱'),
 dict(s=7.05, e=10.0, html="THE MOST<br><y>LIKED COMMENT</y> 👑"),
 dict(s=10.0, e=11.3, html='BUT WAIT...<br><y>ONE MOMENT</y> ✋'),
 dict(s=11.3, e=14.0, html='YESTERDAY?<br>JUST <y>MANGO</y> 🐱', small='and an empty road 🛣️', ss=12.7),
 dict(s=14.0, e=18.3, html='<y>128</y> FOLLOWERS<br>= <y>128</y> HOUSES 🏠'),
 dict(s=18.3, e=21.95, html='<y>194</y> LIKES<br>= <y>194</y> CATS 🐱'),
 dict(s=21.95, e=24.9, html='MORE <y>CATS</y><br>THAN <y>HOUSES</y>?!'),
 dict(s=24.9, e=29.0, html='OUR <y>FIRST</y><br>CAT HOUSE 🏠'),
 dict(s=29.0, e=30.4, html="LET'S BUILD<br>THE <y>TOP COMMENT</y> 🚧"),
 dict(s=30.4, e=34.9, html="LET'S <y>BUILD IT!</y> 🚧"),
 dict(s=34.9, e=35.7, html='<y>BUILT!</y> 🎉🐟', small='“add a fish supermarket” ✅', ss=35.1, smallTop=1300),
 dict(s=35.7, e=37.6, html='TOP COMMENT<br>EVERY DAY<br>= <y>WE BUILD IT</y>'),
 dict(s=37.6, e=41.9, html='<y>66 CATS</y><br>NEED A HOME 🥺', small='Follow = +1 house 🏠', ss=39.6, smallTop=1330),
 dict(s=41.9, e=45.0, html='ARE YOU<br><y>COMING?</y> 👇', small='Follow to move in 🐱', ss=43.3),
 dict(s=45.0, e=99, html=HOOK),
]
json.dump(dict(duration=45.5, day=2, houses=True, catsCounter=True, cats=1, followers=0, roll=[0, 0], build=[30.4, 34.9], firstStreet='Meowstache Ave 🪧', lines=lines, beats=beats, goal=[99, 99],
               hideTags=[[0, 25.7], [29.0, 99]], pinTags=[], example=[]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
