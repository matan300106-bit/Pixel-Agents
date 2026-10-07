# Camera shots + 3 engine pages for the "Top comment -> we build it" video (rule-v1).
# e0 = the real town today (Mango only, empty lots), e1 = same + EXAMPLE build (Mango statue), e2 = 1,000-cat goal town.
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
LOT = [0.09, 50.27]          # SPOTS[0] (probe): straight in front of Mango, who sits at 0,0 facing +z
D = 18.2
H0p, H0l = [0.3, 13, 74], [0.1, 5.6, 36]      # frame 0 = last frame: the lot sign, Mango behind it between the water + food stops
G1p, G1l = [185, 88, 128], [-25, 0, 0]          # end of the goal push = start of the empty-town match cut
S = [  # t0, t1, p0, p1, l0, l1, inout
 (0.0, 1.6, H0p, [0.3, 12, 66], H0l, [0.1, 5.8, 36], 0),
 (1.6, 3.5, [0.3, 12, 66], [30, 135, 150], [0.1, 5.8, 36], [0, 0, 10], 1),
 (3.5, 5.95, [24, 120, 150], [10, 62, 112], [0, 0, 18], [0, 0, 30], 0),
 (5.95, 7.9, [12, 16, 100], [10, 14.5, 92], [0, 12, 45], [0, 11.5, 45], 0),
 (7.9, 9.9, [6.5, 4, 11], [5.6, 3.8, 9.6], [0, 3, 0], [0, 3, 0], 0),
 (9.9, 12.6, [275, 128, 185], G1p, [-40, 0, 0], G1l, 0),
 (12.6, 13.4, G1p, [181, 86, 125], G1l, [-24, 0, 1], 0),
 (13.4, D, [181, 86, 125], H0p, [-24, 0, 1], H0l, 1),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
base = dict(day=2, followersBefore=0, followersNew=0, landmarks=[], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=False, countFrom=0)
cm = dict(list=[dict(by='example.lior', text='A sushi bar for cats', likes=31), dict(by='example.dan', text='Giant scratching tower', likes=54),
                dict(by='example.anna', text='A giant Mango statue!', likes=87)], win=2, t=dict(up=3.5, scroll=3.8, stop=4.7, down=5.85))
json.dump({**base, 'landmarks': [dict(kind='reserved', sign='Your idea here?')], 'comments': cm}, open(f'{out}/e0.json', 'w'))
json.dump({**base, 'newBuild': dict(kind='statue', sign='Mango Statue', name='Mango Statue', by='example.anna', at=6.2)}, open(f'{out}/e1.json', 'w'))
p = json.load(open('p_1000.json')); p.pop('still'); p['landmarks'][0]['sign'] = 'Toy Shop'
json.dump({**base, **p, 'shots': shots, 'duration': D}, open(f'{out}/e2.json', 'w'))
