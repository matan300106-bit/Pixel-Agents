# Day 2 (Matan's script + likes = cats): follow = house, like = cat -> most liked comment (PIKA, no like count) -> "but wait" -> yesterday just Mango ->
# 128 followers = 128 houses pop -> 194 likes = 194 cats (66 strays pop on roofs and streets) -> first house @idkhima on Meowstache Avenue -> fish supermarket build -> 66 cats need a home.
import json, sys, csv
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 45.5
LIKES = 194
FOL = [r['handle'].lstrip('@') for r in list(csv.DictReader(open('/mnt/project-files/cat-town/followers.csv')))[1:]]
assert len(FOL) == 128 and len(set(f.lower() for f in FOL)) == 128
NS = LIKES - len(FOL)                                  # 66 cats with no house
STRAYS = [round(18.8 + 2.6 * ((j + .5) / NS) ** .8, 3) for j in range(NS)]
POP = [round(14.4 + 3.2 * ((j + .5) / len(FOL)) ** .7, 3) for j in range(len(FOL))]   # 128 followers = 128 houses, in follower order
H0p, H0l = [5, 8, 17], [0, 2.2, 0]                     # frame 0 = last frame: Mango between the fountain and the feeder
LOTp, LOTl = [-6, 11, 12], [0, 9, 44]                  # the empty lot with the "Your idea here?" sign
A1p, A1l = [-2, 42, 80], [35, 5, 8]                    # house #1 (@idkhima)
S = [
 (0.0, 3.2, H0p, [4.8, 7.8, 16.6], H0l, H0l, 0),                        # hook on Mango
 (3.2, 7.0, [4.8, 7.8, 16.6], LOTp, H0l, LOTl, 1),                      # turn to the empty lot
 (7.0, 10.0, LOTp, [-4, 10.5, 16], LOTl, LOTl, 0),                      # the most liked comment card
 (10.0, 11.0, [-4, 10.5, 16], [4, 7, 15], LOTl, H0l, 1),                # "but wait": whip back to Mango
 (11.0, 14.0, [4, 7, 15], [3.5, 6.5, 13], H0l, H0l, 0),                 # yesterday: just Mango and an empty road
 (14.0, 18.2, [3.5, 6.5, 13], [0, 250, 150], H0l, [0, 0, 6], 1),        # 128 houses pop
 (18.2, 21.9, [0, 250, 150], [75, 75, 100], [0, 0, 6], [25, 0, 15], 1),  # 194 cats: the 66 strays pop on roofs and streets
 (21.9, 23.2, [75, 75, 100], A1p, [25, 0, 15], A1l, 1),                 # more cats than houses: crowded roofs near house #1
 (23.2, 29.0, A1p, [1, 39, 75], A1l, A1l, 0),                           # the first house
 (29.0, 30.4, [1, 39, 75], [30, 32, -12], A1l, [0, 19, 47], 1),         # to the lot: build the top comment
 (30.4, 35.7, [30, 32, -12], [-26, 28, -8], [0, 19, 47], [0, 19, 47], 0),
 (35.7, 37.6, [-26, 28, -8], [36, 150, -62], [0, 19, 47], [0, 0, 50], 1),
 (37.6, 41.9, [36, 150, -62], [150, 105, 70], [0, 0, 50], [0, 0, 20], 0),
 (41.9, 44.3, [150, 105, 70], [120, 90, 90], [0, 0, 20], [0, 0, 20], 0),
 (44.3, D, [120, 90, 90], H0p, [0, 0, 20], H0l, 1),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
cm = dict(list=[dict(by='PIKA', name='PIKA (winter arc☠️)', text='add a fish supermarket', likes=None)], win=0, t=dict(up=7.1, scroll=7.3, stop=8.5, down=10.0))
ep = dict(day=2, followersBefore=0, followersNew=len(FOL), order='index', newFrom=POP[0], newTo=POP[-1], appear=POP,
          residents=[dict(by=FOL[0], n=1)], landmarks=[], strays=dict(n=NS, at=STRAYS, near=[30, 17]), shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=True, countFrom=0,
          lotSign='Your idea here?', comments=cm, newBuild=dict(kind='fishmarket', sign='Fish Supermarket', name='Fish Supermarket', by='PIKA', byName='PIKA', at=30.4, slow=4.5))
json.dump(ep, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('first house:', FOL[0], 'houses done', POP[-1], 'strays', NS, 'done', STRAYS[-1])
