# Day 1 v3 "only ONE cat": camera shots + 4 engine pages.
# e0 real town (Mango + "Your idea here?" sign), eh + 3 EXAMPLE houses, es + EXAMPLE Mango statue, eg 1,000-cat goal town.
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'd'
D = 17.6
H0p, H0l = [2.5, 4.5, 9], [0, 4.0, 0]            # frame 0 = last frame: Mango close, front 3/4
G1p, G1l = [185, 88, 128], [-25, 0, 0]
S = [
 (0.0, 2.6, H0p, [12, 150, 120], H0l, [0, 0, -10], 1),
 (2.6, 4.5, [7, 5, 11], [6.3, 4.6, 9.9], [0.6, 2.0, 0], [0.6, 2.0, 0], 0),
 (4.5, 6.3, [0, 120, 150], [-8, 16, 60], [0, 0, 0], [-18.8, 5, 33.5], 1),
 (6.3, 7.8, [-8, 16, 60], [-10, 14, 56], [-18.8, 5, 33.5], [-18.8, 5, 33.5], 0),
 (7.8, 10.4, [14, 30, 125], [13, 28, 117], [0, 9, 45], [0, 9, 45], 0),
 (10.4, 12.0, [0.3, 13, 74], [0.3, 12, 66], [0.1, 1.2, 36], [0.1, 1.4, 36], 0),
 (12.0, 14.4, [275, 128, 185], G1p, [-40, 0, 0], G1l, 0),
 (14.4, 15.0, G1p, [181, 86, 125], G1l, [-24, 0, 1], 0),
 (15.0, D, [181, 86, 125], H0p, [-24, 0, 1], H0l, 1),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
base = dict(day=1, followersBefore=0, followersNew=0, landmarks=[], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=False, countFrom=0)
sign = [dict(kind='reserved', sign='Your idea here?')]
json.dump({**base, 'landmarks': sign}, open(f'{out}/e0.json', 'w'))
json.dump({**base, 'followersNew': 3, 'newFrom': 5.3, 'newTo': 7.4, 'residents': [{'by': 'you', 'n': 1}, {'by': 'you', 'n': 2}, {'by': 'you', 'n': 3}]}, open(f'{out}/eh.json', 'w'))
json.dump({**base, 'newBuild': dict(kind='statue', sign='Mango Statue', name='Mango Statue', by='example.anna', at=8.9)}, open(f'{out}/es.json', 'w'))
p = json.load(open('p_1000.json')); p.pop('still'); p['landmarks'][0]['sign'] = 'Toy Shop'
json.dump({**base, **p, 'shots': shots, 'duration': D}, open(f'{out}/eg.json', 'w'))
