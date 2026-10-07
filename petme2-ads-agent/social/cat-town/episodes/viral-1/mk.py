# viral-1 "Lonely Mango -> 1,000 cats": camera shots + 4 engine pages.
# e0 real town (Mango alone + "Your name here?" sign), eh + 3 EXAMPLE houses, eg growth time-lapse to 1,000 houses, (e0 reused for the ask + loop)
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 14.8
H0p, H0l = [2.5, 4.5, 9], [0, 4.0, 0]            # frame 0 = last frame: Mango close, front 3/4
G1p, G1l = [185, 88, 128], [-25, 0, 0]
S = [
 (0.0, 2.2, H0p, [2.2, 4.35, 8.1], H0l, H0l, 0),                                    # hook: Mango alone, slow push in
 (2.2, 4.0, [-1, 4.2, -10], [1.2, 4.6, -11.6], [0, 1.8, 20], [0, 1.8, 20], 0),          # waiting, looking out at the empty road
 (4.0, 4.4, [0, 120, 150], [60.6, 18, 20.1], [0, 0, 0], [37.6, 3, 3.9], 1),          # whip dive to house 1
 (4.4, 5.25, [60.6, 18, 20.1], [59.4, 17.4, 19.3], [37.6, 3, 3.9], [37.6, 3, 3.9], 0),
 (5.25, 6.1, [40.7, 18, 49.2], [39.8, 17.4, 48.2], [22.9, 3, 30], [22.9, 3, 30], 0),   # house 2
 (6.1, 7.8, [-5, 18, 53.9], [-5.8, 16.8, 52.0], [-18.3, 3, 32.8], [-18.3, 3, 32.8], 0),  # house 3
 (7.8, 10.6, [-8, 46, 96], G1p, [-18.3, 3, 32.8], G1l, 1),                          # crane up while the town fills to 1,000
 (10.6, 13.4, [14, 26, 112], [13, 24, 104], [0, 7, 45], [0, 7, 45], 0),               # the empty lot: "Your name here?"
 (13.4, D, [10, 12, 34], H0p, [0, 5, 10], H0l, 1),                                    # back to lonely Mango (loop)
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
base = dict(day=1, followersBefore=0, followersNew=0, landmarks=[], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=False, countFrom=0)
json.dump({**base, 'landmarks': [dict(kind='reserved', sign='Your name here?')]}, open(f'{out}/e0.json', 'w'))
json.dump({**base, 'followersNew': 3, 'order': 'index', 'newFrom': 4.0, 'newTo': 6.54, 'residents': [{'by': 'you', 'n': 1}, {'by': 'you', 'n': 2}, {'by': 'you', 'n': 3}]}, open(f'{out}/eh.json', 'w'))
p = json.load(open('p_1000.json')); p.pop('still'); p.pop('day', None)
json.dump({**base, 'landmarks': p['landmarks'], 'followersBefore': 3, 'followersNew': 997, 'order': 'index', 'newFrom': 7.85, 'newTo': 10.1}, open(f'{out}/eg.json', 'w'))
