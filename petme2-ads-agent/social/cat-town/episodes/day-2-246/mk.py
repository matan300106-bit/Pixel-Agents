# Day 2 (Matan's script): hook -> 1 follower = 1 cat house -> most liked comment (PIKA, no like count) -> "but wait" ->
# yesterday just Mango + empty road -> today 246 houses pop -> Mango is not alone anymore -> first house @idkhima on Meowstache Avenue -> slow fish supermarket build -> follow CTA.
import json, sys, csv
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 37.05
SH, T0 = 2.05, 16.8                                    # the Mango moment: everything from 16.8 s moves 2.05 s later
FOL = [r['handle'].lstrip('@') for r in list(csv.DictReader(open('/mnt/project-files/cat-town/followers.csv')))[1:]]
N = 246                                                # followers on Oct 8, afternoon (Matan): one house each
assert len(set(f.lower() for f in FOL)) == len(FOL)
POP = [round(13.2 + 2.8 * ((j + .5) / N) ** .7, 3) for j in range(N)]   # "Today? 246 new cats": every house pops, in follower order
H0p, H0l = [5, 8, 17], [0, 2.2, 0]                     # frame 0 = last frame: Mango between the fountain and the feeder
LOTp, LOTl = [-6, 11, 12], [0, 9, 44]                  # the empty lot with the "Your idea here?" sign
A1p, A1l = [-2, 42, 80], [35, 5, 8]                    # house #1 (@idkhima)
S = [
 (0.0, 3.2, H0p, [4.8, 7.8, 16.6], H0l, H0l, 0),                        # hook on Mango
 (3.2, 5.8, [4.8, 7.8, 16.6], LOTp, H0l, LOTl, 1),                      # turn to the empty lot
 (5.8, 8.9, LOTp, [-4, 10.5, 16], LOTl, LOTl, 0),                       # the most liked comment card
 (8.9, 9.9, [-4, 10.5, 16], [4, 7, 15], LOTl, H0l, 1),                  # "but wait": whip back to Mango
 (9.9, 12.8, [4, 7, 15], [3.5, 6.5, 13], H0l, H0l, 0),                  # yesterday: just Mango and an empty road
 (12.8, 15.6, [3.5, 6.5, 13], [0, 250, 150], H0l, [0, 0, 6], 1),        # today: pull back while every house pops
 (15.6, 16.8, [0, 250, 150], [60, 220, 150], [0, 0, 6], [0, 0, 0], 0),
 (16.8, 18.0, [60, 220, 150], [14, 16, 30], [0, 0, 0], [0, 2, 0], 1),   # Mango is not alone anymore: cats all around him
 (18.0, 18.85, [14, 16, 30], [13, 15.5, 28.5], [0, 2, 0], [0, 2, 0], 0),
 (16.8, 17.9, [13, 15.5, 28.5], A1p, [0, 2, 0], A1l, 1),                # the first house
 (17.9, 21.0, A1p, [1, 39, 75], A1l, A1l, 0),
 (21.0, 22.3, [1, 39, 75], [30, 32, -12], A1l, [0, 19, 47], 1),         # to the lot: build the top comment
 (22.3, 27.6, [30, 32, -12], [-26, 28, -8], [0, 19, 47], [0, 19, 47], 0),
 (27.6, 29.5, [-26, 28, -8], [36, 150, -62], [0, 19, 47], [0, 0, 50], 1),
 (29.5, 33.8, [36, 150, -62], [150, 105, 70], [0, 0, 50], [0, 0, 20], 0),
 (33.8, 35.0, [150, 105, 70], H0p, [0, 0, 20], H0l, 1),
]
sh_ = lambda t: t + SH if t >= T0 and t < 90 else t
S = S[:7] + S[7:9] + [(sh_(a), sh_(b), *r) for a, b, *r in S[9:]]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
cm = dict(list=[dict(by='PIKA', name='PIKA (winter arc☠️)', text='add a fish supermarket', likes=None)], win=0, t=dict(up=5.9, scroll=6.1, stop=7.3, down=8.85))
ep = dict(day=2, followersBefore=0, followersNew=N, order='index', newFrom=POP[0], newTo=POP[-1], appear=POP,
          residents=[dict(by=FOL[0], n=1)], landmarks=[], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=True, countFrom=0,
          lotSign='Your idea here?', comments=cm, newBuild=dict(kind='fishmarket', sign='Fish Supermarket', name='Fish Supermarket', by='PIKA', byName='PIKA', at=sh_(22.3), slow=4.5))
json.dump(ep, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('first house:', FOL[0], 'last pop', POP[-1])
