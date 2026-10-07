# On-screen text for the rules story photos (v2, catchier) -> DIR/text.json. Drawn by photo_overlay.js.
# Card order 1..5 = times 1.0, 9.5, 19.5, 12.0, 4.9 (see README).
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'r'
cards = [
 dict(s=0.0, e=2.0, html='MEET<br><y>MANGO</y> 👋', pill='the <b>ONLY</b> cat in town 😿',
      bub=dict(text='help me find<br>friends? 🥺', x=520, y=1010, side='l')),                                   # 1.0 card 1
 dict(s=2.0, e=5.0, html='FILL THE<br><y>TOWN</y> 🏡', pill2='goal: <b>1,000</b> cats 🎯', pill='follow + comment 👇', pillY=1500,
      bub=dict(text="that's me 👋", x=445, y=850, side='l')),                  # 4.9 card 5
 dict(s=5.0, e=10.0, tag='RULE #1', html='YOU FOLLOW,<br><y>A CAT MOVES IN</y>', pill='with <b>YOUR</b> name on the house 🏠', pillY=1470,
      pinTags=True, ex=[[96, 1064]]),                                                                            # 9.5 card 2
 dict(s=10.0, e=15.0, tag='RULE #3', html='WEIRD IDEAS?<br><y>YES PLS</y> 🤪', pill='just keep it nice 😇', pillY=1480),  # 12.0 card 4
 dict(s=15.0, e=99, tag='RULE #2', html='TOP COMMENT<br><y>GETS BUILT</y> 🏗️', pill='most likes in <b>24h</b> wins 🏆', pillY=1500,
      hideTags=True, ex=[[200, 1180]]),                                                                          # 19.5 card 3
]
json.dump(dict(duration=20.0, cards=cards), open(f'{out}/text.json', 'w'), indent=1)
