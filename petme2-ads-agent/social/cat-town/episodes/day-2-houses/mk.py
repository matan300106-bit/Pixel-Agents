# "Every follower gets a house": Mango alone -> the first followers' houses pop one by one with their names -> the rest pop fast up to 128.
# House k = follower k (followers.csv order, same as the website). The Fish Supermarket (Day 2 build) stands from the start.
import json, sys, csv
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 17.0
FOL = [r['handle'].lstrip('@') for r in list(csv.DictReader(open('/mnt/project-files/cat-town/followers.csv')))[1:]]
assert len(FOL) == 128 and len(set(f.lower() for f in FOL)) == 128
SLOW = [2.9, 3.9, 5.05, 5.7, 6.1]                      # the first 5 houses, one by one (with name tags)
FAST = [round(6.5 + 3.7 * ((j + .5) / (len(FOL) - len(SLOW))) ** .7, 3) for j in range(len(FOL) - len(SLOW))]
H0p, H0l = [5, 8, 17], [0, 2.2, 0]                     # frame 0 = last frame: Mango between the fountain and the feeder
A1p, A1l = [-2, 42, 80], [35, 5, 8]               # houses #1 and #2 lined up: #2 near, #1 behind it
A3p, A3l = [-66, 40, 46], [-31, 2, 19]             # house #3 (west side)
S = [
 (0.0, 0.9, H0p, [4.8, 7.8, 16.6], H0l, H0l, 0),
 (0.9, 2.7, [4.8, 7.8, 16.6], A1p, H0l, A1l, 1),                        # fly out over the empty town to the first lot
 (2.7, 4.45, A1p, [1, 39, 75], A1l, A1l, 0),                          # #1 and #2 pop
 (4.45, 4.95, [1, 39, 75], A3p, A1l, A3l, 1),                         # whip across town to #3
 (4.95, 6.3, A3p, [-60, 36, 42], A3l, A3l, 0),
 (6.3, 10.6, [-60, 36, 42], [0, 250, 150], A3l, [0, 0, 6], 1),         # pull back while the rest pop
 (10.6, 12.1, [0, 250, 150], [90, 210, 150], [0, 0, 6], [0, 0, 0], 0),
 (12.1, 13.7, [90, 210, 150], [14, 16, 30], [0, 0, 0], [0, 2, 0], 1),   # down to Mango: not alone anymore, cats all around
 (13.7, 16.2, [14, 16, 30], [60, 120, 140], [0, 2, 0], [0, 0, 0], 1),    # up over the full town: the only thing missing is you
 (16.2, D, [60, 120, 140], H0p, [0, 0, 0], H0l, 1),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
ep = dict(day=2, followersBefore=0, followersNew=len(FOL), order='index', newFrom=SLOW[0], newTo=FAST[-1], appear=SLOW + FAST,
          residents=[dict(by=FOL[k], n=k + 1) for k in range(len(SLOW))],
          landmarks=[dict(kind='fishmarket', sign='Fish Supermarket', at=0)], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=True, countFrom=0)
json.dump(ep, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('slow:', FOL[:len(SLOW)], 'last pop', FAST[-1])
