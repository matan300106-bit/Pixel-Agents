# Voice timeline + on-screen text/effects for "Are you moving in?" -> DIR/text.json, DIR/timeline.json (subtitles on every line)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
L = json.load(open(f'{out}/lines.json'))
START = [0.15, 2.35, 4.35, 7.95, 9.55, 10.8, 14.1, 17.35, 19.65]
lines = []
for l, s in zip(L, START):
    ws = l['text'].split(); n = sum(len(w) for w in ws); t = s; words = []
    for w in ws:
        d = l['dur'] * len(w) / n; words.append(dict(w=w, s=round(t, 3), e=round(t + d, 3))); t += d
    lines.append(dict(i=l['i'], text=l['text'], s=s, e=round(s + l['dur'], 3), words=words))
HOOK = '<y>1 FOLLOW</y> =<br>1 CAT HOUSE 🏠'
beats = [
 dict(s=0.0, e=2.2, html=HOOK, still=True),
 dict(s=2.2, e=4.2, html='PETME2<br><y>CAT TOWN</y> 🐾'),
 dict(s=4.2, e=6.1, html='EMPTY ROAD 🛣️'),
 dict(s=6.1, e=7.8, html='EMPTY ROAD 🛣️<br><g>+ A LITTLE GRASS</g> 🌱', nopop=True),
 dict(s=7.8, e=9.5, html='ONLY ONE THING<br>IS MISSING…'),
 dict(s=9.5, e=10.6, html='<y>YOU!</y> 🫵💛', huge=True),
 dict(s=10.6, e=13.9, html='+ A <y>REAL</y><br><y>ADDRESS</y> 📍'),
 dict(s=13.9, e=17.2, html='<y>TOP COMMENT</y><br>→ WE BUILD IT 🏗️'),
 dict(s=17.2, e=19.4, html='WE GROW<br>THE CITY! 🎉'),
 dict(s=19.4, e=99, html='soooo… are you<br><y>moving in?</y> 🏠'),
]
json.dump(dict(
  duration=22.0, day=1, cats=1, build=16.25, lines=lines, beats=beats,
  grade='saturate(1.28) brightness(1.06) contrast(1.02) sepia(.06)',
  roll=[17.3, 18.9, 1, 1000], goal=[17.2, 19.4],
  # sparkles: [t, kind, x0, y0, x1, y1, n]
  sparkle=[[0.25, 'swirl', 540, 1050, 0, 0, 26], [0.5, 'burst', 540, 1080, 0, 0, 22], [9.5, 'burst', 540, 980, 0, 0, 34],
           [10.9, 'trail', 150, 700, 560, 1060, 24], [11.75, 'burst', 560, 1060, 0, 0, 24], [16.1, 'burst', 540, 1000, 0, 0, 40],
           [21.55, 'wipe', 0, 0, 0, 0, 70]],
  fireworks=[[17.9, 300, 760, '#FFD23F'], [18.25, 780, 700, '#FF6BB5'], [18.6, 520, 640, '#6BE3FF'], [18.95, 260, 600, '#B36BFF'], [19.2, 820, 820, '#7CFF6B']],
  # emoji pops: [s, e, x, y, emoji, size, anim]
  emojis=[[6.95, 7.8, 470, 1120, '🌱', 150, 'boing'], [20.3, 99, 650, 900, '👋', 140, 'wave']],
  bubbles=[[8.3, 9.45, 'hmm? 🤔'], [21.0, 21.6, 'Meow! 💛']],
  htags=[[0.9, 2.2, 'A', '@you<small>🏠 moved in!</small>'], [12.15, 13.9, 'F', '@you<small>📍 12 Whisker Lane</small>'], [16.65, 17.2, 'B', '🏊 Cat Pool<small>idea by @example</small>']],
  chips=[[14.3, 16.25, 'example', 'A pool for cats! 🏊']],
  example=[[1.0, 2.2, 'A'], [12.25, 13.9, 'F'], [14.45, 17.2, 'chip']],
), open(f'{out}/text.json', 'w'), indent=1)
json.dump([dict(i=l['i'], s=l['s'], e=l['e']) for l in lines], open(f'{out}/timeline.json', 'w'))
for l in lines: print(l['s'], l['e'], l['text'])
