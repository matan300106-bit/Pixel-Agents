# On-screen text for the "Be OK" video (captions only, TikTok-style white boxes) -> DIR/text.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
# each card: [start, end, html]; an optional second line pops in later
cards = [
 dict(s=0.0, e=2.5, html="POV: you're the mayor of a cat city <b>the internet controls</b>"),
 dict(s=2.5, e=5.0, html='rule 1: you follow = you get a house with <b>YOUR name</b> on it 🏠', sub='(128 houses)', ss=4.0),
 dict(s=5.0, e=8.0, html='rule 2: every like = a <b>new cat</b> 🐱', count=True),
 dict(s=8.0, e=10.0, html='194 cats − 128 houses =', sub='66 cats with <b>no home</b>', ss=8.6),
 dict(s=10.0, e=13.0, html='they live in the <b>fish supermarket</b> now'),
 dict(s=13.0, e=16.0, html='rule 3: top comment gets <b>built every day</b>', sub='the fish store WAS a comment.', ss=14.6),
 dict(s=16.0, e=19.0, html='comment what we build tomorrow 👇', sub='(please say houses)', ss=17.4),
]
json.dump(dict(duration=19.0, cards=cards, tags=[[2.5, 5.0]]), open(f'{out}/text.json', 'w'), indent=1, ensure_ascii=False)
