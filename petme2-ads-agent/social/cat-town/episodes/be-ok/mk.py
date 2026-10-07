# "Be OK" trend video (19 s, captions only): Mango dances happily while the captions admit the mess.
# rule 1 follow = house (128 pop) -> rule 2 like = cat (66 strays rain down, 194 cats) -> 66 with no home -> they live in the fish supermarket now
# -> rule 3 top comment gets built (a fish falls on Mango, the dance goes on) -> Mango freezes, a stray peeks in -> loops to frame 0.
import json, sys, csv
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 19.0
LIKES = 194
FOL = [r['handle'].lstrip('@') for r in list(csv.DictReader(open('/mnt/project-files/cat-town/followers.csv')))[1:]]
assert len(FOL) == 128 and len(set(f.lower() for f in FOL)) == 128
NS = LIKES - len(FOL)                                   # 66 cats with no house
POP = [round(2.7 + 2.2 * ((j + .5) / len(FOL)) ** .75, 3) for j in range(len(FOL))]
RAIN = [round(5.25 + 2.4 * ((j + .5) / NS) ** .8, 3) for j in range(NS)]
SHOP = json.load(open(f'{out}/shop.json')) if len(sys.argv) > 2 else None   # [x, z, ry] of the fish supermarket (from a test render)
import math
sx, sz, ry = SHOP or [0, 50, 0]
fx, fz = math.sin(ry), math.cos(ry)                     # the shop's front faces the square
SHp = [sx + fx * 62 + fz * 12, 24, sz + fz * 62 - fx * 12]; SHl = [sx + fx * 2, 7, sz + fz * 2]
SHp2 = [sx + fx * 54 - fz * 8, 20, sz + fz * 54 + fx * 8]
M0p, M0l = [3, 6.5, -17], [0, 3.6, 0]                    # close on Mango (frame 0 = last frame)
S = [
 (0.0, 2.5, M0p, [2.6, 6.2, -16], M0l, M0l, 0),
 (2.5, 5.0, [2.6, 6.2, -16], [8, 40, -88], M0l, [0, 2, 30], 1),          # rule 1: the houses pop behind Mango
 (5.0, 8.0, [8, 40, -88], [4, 19, -50], [0, 2, 30], [0, 1, 4], 0),      # rule 2: cats rain down
 (8.0, 10.0, [4, 19, -50], [-4, 13, -40], [0, 1, 4], [-2, 1, -14], 0),   # drift to the cats with nowhere to go
 (10.0, 13.0, SHp, SHp2, SHl, SHl, 0),                                  # hard cut: they live in the fish supermarket now
 (13.0, 16.0, [2.4, 6.2, -16], [3, 6.5, -17], M0l, M0l, 0),               # hard cut back: Mango still dancing, the fish bonk
 (16.0, D, [3, 6.5, -17], M0p, M0l, M0l, 0),                             # Mango freezes, a stray peeks in
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
ep = dict(day=2, followersBefore=0, followersNew=len(FOL), order='index', newFrom=POP[0], newTo=POP[-1], appear=POP,
          residents=[dict(by=FOL[0], n=1)], landmarks=[], noReserved=True, countFrom=0, milestone=1e9, shots=shots, duration=D, starts=[0, 0, 0, 99],
          strays=dict(n=NS, at=RAIN, rain=True, shopAt=10.0, scale=1.3, peek={'at': 17.0, 'dur': 1.3, 'from': [8.5, -2.0], 'to': [2.9, -2.6]}),
          dance=dict(bpm=116, stop=16.0), bonk=14.6,
          newBuild=dict(kind='fishmarket', sign='Fish Supermarket', name='Fish Supermarket', by='PIKA', byName='PIKA', at=-5))
json.dump(ep, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('houses', POP[0], POP[-1], 'strays', NS, RAIN[0], RAIN[-1])
