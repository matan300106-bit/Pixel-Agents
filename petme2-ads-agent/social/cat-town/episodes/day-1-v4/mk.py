# Day 1 v4 "This is Mango": camera shots + 4 engine pages.
# e0 real town (Mango + "Your idea here?" sign), eh + 3 EXAMPLE houses, es + EXAMPLE comment card + Mango statue, eg 1,000-cat goal town.
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'f'
D = 20.4
H0p, H0l = [2.5, 4.5, 9], [0, 4.0, 0]            # frame 0 = last frame: Mango close, front 3/4
G1p, G1l = [185, 88, 128], [-25, 0, 0]
S = [
 (0.0, 1.0, H0p, [2.3, 4.4, 8.4], H0l, H0l, 0),
 (1.0, 3.0, [2.3, 4.4, 8.4], [12, 150, 120], H0l, [0, 0, -10], 1),
 (3.0, 4.1, [-0.5, 7.5, 21], [-1.5, 6.5, 17.5], [-3, 2.6, 0], [-3.2, 2.4, 0], 0),      # drinks at the fountain
 (4.1, 5.0, [7, 5, 11], [6.3, 4.6, 9.9], [0.6, 2.0, 0], [0.6, 2.0, 0], 0),            # eats at the feeder
 (5.0, 6.6, [-1, 4.2, -10], [1.5, 4.8, -12], [0, 1.8, 20], [0, 1.8, 20], 0),          # alone, looking out at the empty road
 (6.6, 7.1, [0, 120, 150], [60.6, 18, 20.1], [0, 0, 0], [37.6, 3, 3.9], 1),        # dive to house 1
 (7.1, 8.0, [60.6, 18, 20.1], [59.4, 17.4, 19.3], [37.6, 3, 3.9], [37.6, 3, 3.9], 0),
 (8.0, 8.9, [40.7, 18, 49.2], [39.8, 17.4, 48.2], [22.9, 3, 30], [22.9, 3, 30], 0),    # house 2
 (8.9, 10.0, [-5, 18, 53.9], [-5.6, 17, 52.4], [-18.3, 3, 32.8], [-18.3, 3, 32.8], 0),  # house 3
 (10.0, 12.6, [14, 30, 125], [13, 28, 118], [0, 9, 45], [0, 9, 45], 0),               # comment card over the empty lot
 (12.6, 14.6, [12, 20, 106], [10, 17, 97], [0, 10, 45], [0, 10.5, 45], 0),           # statue pops
 (14.6, 17.0, [275, 128, 185], G1p, [-40, 0, 0], G1l, 0),
 (17.0, 17.5, G1p, [181, 86, 125], G1l, [-24, 0, 1], 0),
 (17.5, D, [181, 86, 125], H0p, [-24, 0, 1], H0l, 1),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
base = dict(day=1, followersBefore=0, followersNew=0, landmarks=[], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=False, countFrom=0)
json.dump({**base, 'landmarks': [dict(kind='reserved', sign='Your idea here?')]}, open(f'{out}/e0.json', 'w'))
json.dump({**base, 'followersNew': 3, 'order': 'index', 'newFrom': 6.71, 'newTo': 9.4, 'residents': [{'by': 'you', 'n': 1}, {'by': 'you', 'n': 2}, {'by': 'you', 'n': 3}]}, open(f'{out}/eh.json', 'w'))
cm = dict(list=[dict(by='example.lior', text='A sushi bar for cats', likes=31), dict(by='example.dan', text='Giant scratching tower', likes=54),
                dict(by='example.anna', text='Build a Mango statue!', likes=87)], win=2, t=dict(up=10.05, scroll=10.4, stop=11.3, down=12.55))
json.dump({**base, 'comments': cm, 'newBuild': dict(kind='statue', sign='Mango Statue', name='Mango Statue', by='example.anna', at=12.75)}, open(f'{out}/es.json', 'w'))
p = json.load(open('p_1000.json')); p.pop('still'); p['landmarks'][0]['sign'] = 'Toy Shop'
json.dump({**base, **p, 'shots': shots, 'duration': D}, open(f'{out}/eg.json', 'w'))
