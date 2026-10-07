# Voice timeline + on-screen text/effects for "Are you moving in?" v2 (29 real cats) -> DIR/text.json, DIR/timeline.json
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v2'
L = json.load(open(f'{out}/lines.json'))
START = [0.15, 2.5, 4.55, 8.55, 11.5, 13.05, 14.3, 17.6, 20.85, 23.15]
lines = []
for l, s in zip(L, START):
    ws = l['text'].split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words))
HOOK = '<y>1 FOLLOWER</y> =<br>1 CAT HOUSE 🏠'
beats = [
 dict(s=0.0, e=2.4, html=HOOK, still=True),
 dict(s=2.4, e=4.4, html='PETME2<br><y>CAT TOWN</y> 🐾'),
 dict(s=4.4, e=6.4, html='DAY 1:<br>EMPTY ROAD 🛣️'),
 dict(s=6.4, e=8.4, html='DAY 1:<br>EMPTY ROAD 🛣️<br><g>+ A LITTLE GRASS</g> 🌱', nopop=True),
 dict(s=8.4, e=11.2, html='NOW:<br><y>29 CATS</y> 🎉'),
 dict(s=11.2, e=13.0, html='ONE THING IS<br>STILL MISSING…'),
 dict(s=13.0, e=14.1, html='<y>YOU!</y> 🫵💛', huge=True),
 dict(s=14.1, e=17.4, html='+ A <y>REAL</y><br><y>ADDRESS</y> 📍'),
 dict(s=17.4, e=20.7, html='<y>TOP COMMENT</y><br>→ WE BUILD IT 🏗️'),
 dict(s=20.7, e=22.9, html='THE GOAL:<br><y>1,000 CATS</y> 🎯'),
 dict(s=22.9, e=99, html='soooo… are you<br><y>moving in?</y> 🏠'),
]
# real followers shown by name (2 handles skipped for brand safety; their houses still count)
NAMES = ['idkhima', 'ugvtsvi', 'sillyy72', 'lina768940', 'warkitty4', 'space_orb', 'daisy.thefallen', 'rockstar_bear', 'tara4ever15', 'leanalex.medina']
SPOTS = [[60, 850], [610, 850], [60, 950], [610, 950], [60, 1050], [610, 1050], [60, 1150], [610, 1150], [60, 1250], [610, 1250]]
names = [[8.75 + i * .2, 8.75 + i * .2 + 1.15, SPOTS[i][0], SPOTS[i][1], '@' + n] for i, n in enumerate(NAMES)]
json.dump(dict(
  duration=25.5, day=1, cats=1, build=19.75, lines=lines, beats=beats,
  grade='saturate(1.28) brightness(1.06) contrast(1.02) sepia(.06)',
  # counter: [s, e, from, to, roll_start, roll_end, label]
  counter=[[0, 8.4, 1, 1, 0, 1, 'cat · Day 1'], [8.4, 20.7, 1, 29, 8.6, 10.3, 'cats · Day 1'], [20.7, 22.9, 29, 1000, 20.8, 22.4, 'cats · THE GOAL'], [22.9, 99, 29, 29, 0, 1, 'cats · Day 1']],
  sparkle=[[0.25, 'swirl', 540, 1050, 0, 0, 26], [0.5, 'burst', 540, 1080, 0, 0, 22], [10.3, 'burst', 540, 700, 0, 0, 30], [13.0, 'burst', 540, 980, 0, 0, 34],
           [14.4, 'trail', 150, 700, 540, 1060, 24], [15.25, 'burst', 540, 1060, 0, 0, 24], [19.6, 'burst', 540, 1000, 0, 0, 40], [25.05, 'wipe', 0, 0, 0, 0, 70]],
  fireworks=[[10.35, 270, 820, '#FFD23F'], [10.6, 800, 760, '#FF6BB5'], [21.4, 300, 760, '#FFD23F'], [21.75, 780, 700, '#FF6BB5'], [22.1, 520, 640, '#6BE3FF'], [22.45, 260, 600, '#B36BFF'], [22.7, 820, 820, '#7CFF6B']],
  emojis=[[7.75, 8.4, 470, 1120, '🌱', 150, 'boing'], [23.8, 99, 650, 900, '👋', 140, 'wave']],
  bubbles=[[11.8, 12.95, 'hmm? 🤔'], [24.5, 25.1, 'Meow! 💛']],
  htags=[[0.9, 2.4, 'A', '@you<small>🏠 moved in!</small>'], [15.65, 17.4, 'F', '@you<small>📍 12 Whisker Lane</small>'], [20.15, 20.7, 'B', '🏊 Cat Pool<small>idea by @example</small>']],
  chips=[[17.8, 19.75, 'example', 'A pool for cats! 🏊']],
  example=[[1.0, 2.4, 'A'], [15.75, 17.4, 'F'], [17.95, 20.7, 'chip']],
  names=names,
), open(f'{out}/text.json', 'w'), indent=1)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
