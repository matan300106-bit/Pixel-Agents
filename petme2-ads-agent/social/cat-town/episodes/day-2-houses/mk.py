# "Every follower gets a house" (Matan's script): yesterday just Mango -> today 128 new cats (every house pops) -> houses #1/#2 with names -> Mango not alone -> the only thing missing is you.
# House k = follower k (followers.csv order, same as the website). The Fish Supermarket (Day 2 build) stands from the start.
import json, sys, csv
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 17.0
FOL = [r['handle'].lstrip('@') for r in list(csv.DictReader(open('/mnt/project-files/cat-town/followers.csv')))[1:]]
assert len(FOL) == 128 and len(set(f.lower() for f in FOL)) == 128
FAST = [round(4.7 + 2.9 * ((j + .5) / len(FOL)) ** .7, 3) for j in range(len(FOL))]   # "Today? 128 new cats": every house pops, in follower order
H0p, H0l = [5, 8, 17], [0, 2.2, 0]                     # frame 0 = last frame: Mango between the fountain and the feeder
A1p, A1l = [-2, 42, 80], [35, 5, 8]                    # houses #1 and #2 lined up: #2 near, #1 behind it (name tags)
S = [
 (0.0, 2.4, H0p, [4.8, 7.8, 16.6], H0l, H0l, 0),                        # hook on Mango
 (2.4, 4.3, [4.8, 7.8, 16.6], [3.5, 6.5, 13], H0l, H0l, 0),            # "Yesterday? It was just Mango": slow push-in, empty town
 (4.3, 7.4, [3.5, 6.5, 13], [0, 250, 150], H0l, [0, 0, 6], 1),         # "Today? 128 new cats": pull back while every house pops
 (7.4, 8.6, [0, 250, 150], [60, 220, 150], [0, 0, 6], [0, 0, 0], 0),
 (8.6, 9.6, [60, 220, 150], A1p, [0, 0, 0], A1l, 1),                    # down to houses #1 and #2 with their names
 (9.6, 11.6, A1p, [1, 39, 75], A1l, A1l, 0),
 (11.6, 13.0, [1, 39, 75], [14, 16, 30], A1l, [0, 2, 0], 1),           # Mango, not alone anymore: cats all around
 (13.0, 13.7, [14, 16, 30], [13, 15.5, 28.5], [0, 2, 0], [0, 2, 0], 0),
 (13.7, 16.2, [13, 15.5, 28.5], [60, 120, 140], [0, 2, 0], [0, 0, 0], 1),   # up over the full town: the only thing missing is you
 (16.2, D, [60, 120, 140], H0p, [0, 0, 0], H0l, 1),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
ep = dict(day=2, followersBefore=0, followersNew=len(FOL), order='index', newFrom=FAST[0], newTo=FAST[-1], appear=FAST,
          residents=[dict(by=FOL[k], n=k + 1) for k in range(2)],
          landmarks=[dict(kind='fishmarket', sign='Fish Supermarket', at=0)], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=True, countFrom=0)
json.dump(ep, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('tags:', FOL[:2], 'last pop', FAST[-1])
