# "Are you moving in?" v2 (29 real cats, excited voice): camera shots + engine pages.
# eA: hook house pops | e0: Day 1 empty town | eM: the real 28 houses pop (mini town) | eF: one more house (EXAMPLE) | eB: cat pool build | eG: growth to 1,000
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v2'
D = 25.5
H0p, H0l = [2.5, 4.5, 9], [0, 4.0, 0]
G1p, G1l = [185, 88, 128], [-25, 0, 0]
S = [
 (0.0, 2.4, [41.5, 17, 50.5], [39.6, 15.2, 47.6], [22.9, 3.5, 30], [22.9, 3.5, 30], 0),       # A hook: a house pops (lot 1)
 (2.4, 4.4, [12, 150, 120], [9, 34, 44], [0, 0, -10], [0, 3, 0], 1),                          # B storybook fly-down
 (4.4, 8.4, [-1, 4.2, -10], [1.5, 4.8, -12.5], [0, 1.8, 20], [0, 1.8, 20], 0),                 # C Day 1: empty road behind Mango
 (8.4, 11.2, [8, 105, 118], [22, 150, 150], [0, 0, 0], [0, 0, -6], 1),                            # M rise over the mini town (28 real houses pop)
 (11.2, 13.0, [3.0, 4.7, 10.5], [2.3, 4.4, 8.4], H0l, H0l, 0),                                # D Mango close
 (13.0, 13.25, [2.3, 4.4, 8.4], [1.3, 3.95, 5.2], H0l, [0, 3.7, 0], 1),                        # E snap zoom: "You!"
 (13.25, 14.1, [1.3, 3.95, 5.2], [1.2, 3.92, 4.9], [0, 3.7, 0], [0, 3.7, 0], 0),
 (14.1, 17.4, [-21, 16, 1], [-24.5, 14.2, 3.5], [-47.9, 3.5, 10.7], [-47.9, 3.5, 10.7], 0),    # F one more house (lot 28, EXAMPLE)
 (17.4, 20.7, [5, 22, 78], [9, 38, 106], [0, 2.5, 50], [0, 3, 50], 0),                        # G sign -> poof -> cat pool
 (20.7, 22.9, [-8, 46, 96], G1p, [-18.3, 3, 32.8], G1l, 1),                                   # H crane up: 29 -> 1,000
 (22.9, D, [3.1, 4.75, 11], H0p, H0l, H0l, 0),                                                # I Mango: "are you moving in?"
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
base = dict(day=1, followersBefore=0, followersNew=0, landmarks=[], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=False, countFrom=0)
REAL = 28
w = lambda n, d: json.dump(d, open(f'{out}/{n}.json', 'w'))
w('eA', {**base, 'followersBefore': 1, 'followersNew': 1, 'order': 'index', 'newFrom': .5, 'newTo': .5})
w('e0', {**base, 'landmarks': [dict(kind='reserved', sign='Your idea here?')]})
w('eM', {**base, 'landmarks': [dict(kind='reserved', sign='Your idea here?')], 'followersNew': REAL, 'order': 'index', 'newFrom': 8.6, 'newTo': 10.3})
w('eF', {**base, 'followersBefore': REAL, 'followersNew': 1, 'order': 'index', 'newFrom': 15.25, 'newTo': 15.25})
w('eB', {**base, 'followersBefore': REAL, 'newBuild': dict(kind='pool', sign='Cat Pool', name='Cat Pool', by='example', at=19.75)})
p = json.load(open('p_1000.json')); p.pop('still'); p.pop('day', None)
w('eG', {**base, 'landmarks': p['landmarks'], 'followersBefore': REAL, 'followersNew': 1000 - 1 - REAL, 'order': 'index', 'newFrom': 20.8, 'newTo': 22.4})
