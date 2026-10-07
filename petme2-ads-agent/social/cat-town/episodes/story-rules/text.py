# On-screen text for the rules story photos -> DIR/text.json (no voice, so no captions)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'r'
beats = [
 dict(s=0.0, e=2.0, html='HOW <y>CAT TOWN</y><br>WORKS 🐱', still=True, small='3 simple rules 👉', ss=0, st=740),       # 1.0 card 1
 dict(s=2.0, e=5.0, html='MANGO NEEDS<br><y>FRIENDS</y> 🐱', still=True, small='Follow + comment your idea 👇', ss=0, st=1480),  # 4.9 card 5
 dict(s=5.0, e=10.0, html='RULE 1 🐱<br><y>1 FOLLOW</y>', still=True, small='= 1 new cat + a house with your name 🏠', ss=0, st=1480),  # 9.5 card 2
 dict(s=10.0, e=15.0, html='RULE 3 🤪<br><y>WEIRD = GOOD</y>', still=True, small='Rude, political or unsafe ideas are skipped', ss=0, st=1480),  # 12.0 card 4
 dict(s=15.0, e=99, html='RULE 2 🏗️<br><y>TOP COMMENT</y>', still=True, small='Most likes in 24 h = we build it, with your @ on it', ss=0, st=1480),  # 19.5 card 3
]
json.dump(dict(duration=20.0, day=None, cats=1, lines=[], beats=beats, goal=[99, 99],
               hideTags=[[15.0, 20.0]], pinTags=[[5.5, 10.0]], example=[[5.7, 10.0, 'card'], [15.3, 20.0, 'statue']]), open(f'{out}/text.json', 'w'), indent=1)
