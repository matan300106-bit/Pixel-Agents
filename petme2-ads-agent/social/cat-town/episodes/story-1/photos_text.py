# Photo version of the story (Matan wants images, not video): same scenes, no voice captions, full text on each card -> DIR/text.json
# Card 2: house tag pinned under the headline, its small line under the house, EXAMPLE stamp lower left, so both stay clear of the headline.
# Render: node render.js DIR test 1.0,9.5,14.9  (card 1 Mango, card 2 houses, card 3 sign)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'p'
beats = [
 dict(s=0.0, e=5.0, html='THIS IS<br><y>MANGO</y> 🐱', still=True, small='The only cat in Cat Town', ss=0),
 dict(s=5.0, e=10.0, html='<y>1 FOLLOW</y><br>= 1 NEW CAT', still=True, small='+ a house with your name 🏠', ss=0, st=1480),
 dict(s=10.0, e=99, html='WHAT DO WE<br><y>BUILD NEXT?</y>', still=True, small='Reply with your idea 👇', ss=0),
]
json.dump(dict(duration=15.0, day=None, cats=1, lines=[], beats=beats, goal=[99, 99],
               hideTags=[], pinTags=[[5.5, 10.0]], example=[[5.7, 10.0, 'card']]), open(f'{out}/text.json', 'w'), indent=1)
