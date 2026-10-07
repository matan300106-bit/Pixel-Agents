# "Are you moving in?" (happy, Disney-style): camera shots + engine pages.
# eA: house pops (hook) | e0: real empty town + "Your idea here?" sign | eF: house 2 pops | eB: the comment build (cat pool) pops | eG: growth to 1,000
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 22.0
H0p, H0l = [2.5, 4.5, 9], [0, 4.0, 0]            # Mango close, front 3/4
G1p, G1l = [185, 88, 128], [-25, 0, 0]
S = [
 (0.0, 2.2, [41.5, 17, 50.5], [39.6, 15.2, 47.6], [22.9, 3.5, 30], [22.9, 3.5, 30], 0),   # A hook: a house pops (lot 1)
 (2.2, 4.2, [12, 150, 120], [9, 34, 44], [0, 0, -10], [0, 3, 0], 1),                       # B storybook fly-down into town
 (4.2, 7.8, [-1, 4.2, -10], [1.5, 4.8, -12.5], [0, 1.8, 20], [0, 1.8, 20], 0),              # C empty road behind Mango
 (7.8, 9.5, [3.0, 4.7, 10.5], [2.3, 4.4, 8.4], H0l, H0l, 0),                               # D Mango close, head turns
 (9.5, 9.75, [2.3, 4.4, 8.4], [1.3, 3.95, 5.2], H0l, [0, 3.7, 0], 1),                      # E snap zoom: "You!"
 (9.75, 10.6, [1.3, 3.95, 5.2], [1.2, 3.92, 4.9], [0, 3.7, 0], [0, 3.7, 0], 0),
 (10.6, 13.9, [-4.2, 17, 56], [-5.8, 15.4, 52.4], [-18.3, 3.5, 32.8], [-18.3, 3.5, 32.8], 0),   # F another house grows (lot 2)
 (13.9, 17.2, [5, 22, 78], [9, 38, 106], [0, 2.5, 50], [0, 3, 50], 0),                # G sign -> poof -> cat pool
 (17.2, 19.4, [-8, 46, 96], G1p, [-18.3, 3, 32.8], G1l, 1),                                # H crane up while the town fills
 (19.4, D, [3.1, 4.75, 11], H0p, H0l, H0l, 0),                                             # I Mango: "are you moving in?"
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
base = dict(day=1, followersBefore=0, followersNew=0, landmarks=[], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=False, countFrom=0)
POP_A, POP_F, BUILD = 0.5, 11.75, 16.25
w = lambda n, d: json.dump(d, open(f'{out}/{n}.json', 'w'))
w('eA', {**base, 'followersBefore': 1, 'followersNew': 1, 'order': 'index', 'newFrom': POP_A, 'newTo': POP_A, 'residents': [{'by': 'you', 'n': 1}, {'by': 'you', 'n': 2}]})
w('e0', {**base, 'landmarks': [dict(kind='reserved', sign='Your idea here?')]})
w('eF', {**base, 'followersBefore': 2, 'followersNew': 1, 'order': 'index', 'newFrom': POP_F, 'newTo': POP_F, 'residents': [{'by': 'you', 'n': k} for k in (1, 2, 3)]})
w('eB', {**base, 'newBuild': dict(kind='pool', sign='Cat Pool', name='Cat Pool', by='example', at=BUILD)})
p = json.load(open('p_1000.json')); p.pop('still'); p.pop('day', None)
w('eG', {**base, 'landmarks': p['landmarks'], 'followersBefore': 3, 'followersNew': 997, 'order': 'index', 'newFrom': 17.3, 'newTo': 18.9})
