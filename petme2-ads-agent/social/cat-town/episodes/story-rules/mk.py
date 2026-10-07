# Cat Town rules story (photos): scenes reused from ../story-1 + a statue scene. One 20 s timeline, stills picked by render.js test.
# 1.0 Mango, 4.9 whole empty town, 9.5 EXAMPLE house, 12.0 "Your idea here?" sign, 19.5 EXAMPLE Mango statue.
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'r'
D = 20.0
H0p, H0l = [4, 7, 17], [0, 5.5, 0]
S = [
 (0.0, 1.7, H0p, [3.4, 6.6, 14.8], H0l, H0l, 0),
 (1.7, 5.0, [3.4, 6.6, 14.8], [12, 150, 120], H0l, [0, 0, -10], 1),
 (5.0, 5.5, [0, 120, 150], [60.6, 18, 20.1], [0, 0, 0], [37.6, 3, 3.9], 1),
 (5.5, 6.4, [60.6, 18, 20.1], [59.4, 17.4, 19.3], [37.6, 3, 3.9], [37.6, 3, 3.9], 0),
 (6.4, 7.3, [40.7, 18, 49.2], [39.8, 17.4, 48.2], [22.9, 3, 30], [22.9, 3, 30], 0),
 (7.3, 10.0, [-5, 18, 53.9], [-6.5, 16.5, 51.5], [-18.3, 3, 32.8], [-18.3, 3, 32.8], 0),
 (10.0, 15.0, [0.3, 14, 84], [0.3, 12.6, 72], [0.1, 5.4, 36], [0.1, 5.7, 36], 0),
 (15.0, D, [12, 20, 106], [10, 17, 97], [0, 13, 45], [0, 13.5, 45], 0),             # the EXAMPLE statue on the lot
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
base = dict(day=1, followersBefore=0, followersNew=0, landmarks=[], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=False, countFrom=0)
json.dump({**base, 'landmarks': [dict(kind='reserved', sign='Your idea here?')]}, open(f'{out}/e0.json', 'w'))
json.dump({**base, 'followersNew': 3, 'order': 'index', 'newFrom': 5.11, 'newTo': 7.8, 'residents': [{'by': 'you', 'n': 1}, {'by': 'you', 'n': 2}, {'by': 'you', 'n': 3}]}, open(f'{out}/eh.json', 'w'))
json.dump({**base, 'newBuild': dict(kind='statue', sign='Mango Statue', name='Mango Statue', by='example.anna', at=15.2)}, open(f'{out}/es.json', 'w'))
