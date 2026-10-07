# Day 2 "Fish supermarket": camera shots + one engine page (Mango only, empty town; the real top comment card; the shop pops at 8.4 s).
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 18.3
H0p, H0l = [5, 8, 17], [0, 2.2, 0]              # frame 0 = last frame: Mango sitting between the fountain and the feeder
S = [
 (0.0, 1.4, H0p, [4.6, 7.6, 16], H0l, H0l, 0),
 (1.4, 3.3, [4.6, 7.6, 16], [12, 150, 120], H0l, [0, 0, -10], 1),                  # pull back: the whole empty town
 (3.3, 5.6, [-10, 26, -6], [-6, 11, 12], [0, 2, 40], [0, 9, 44], 1),               # over Mango to the empty lot ("Your idea here?" sign)
 (5.6, 8.6, [-6, 11, 12], [-4, 10.5, 16], [0, 9, 44], [0, 9, 44], 0),                   # the most-liked comment card over the empty lot
 (8.6, 11.0, [28, 30, -10], [-24, 28, -8], [0, 20, 47], [0, 19, 47], 0),            # the (big) shop pops, slow orbit
 (11.0, 13.0, [45, 260, -80], [36, 225, -62], [0, 0, 92], [0, 0, 88], 1),           # high above: the shop is the only building in town
 (13.0, 14.8, [36, 225, -62], [40, 120, -70], [0, 0, 88], [0, 0, 15], 1),           # down over the empty town
 (14.8, 17.6, [40, 120, -70], [130, 95, 60], [0, 0, 15], [0, 0, 20], 0),
 (17.6, D, [130, 95, 60], H0p, [0, 0, 20], H0l, 1),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
cm = dict(list=[dict(by='PIKA', name='PIKA (winter arc☠️)', text='add a fish supermarket', likes=None)], win=0, t=dict(up=5.65, scroll=5.9, stop=7.25, down=8.6))
ep = dict(day=2, followersBefore=0, followersNew=0, landmarks=[], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=False, countFrom=0, lotSign='Your idea here?',
          comments=cm, newBuild=dict(kind='fishmarket', sign='Fish Supermarket', name='Fish Supermarket', by='PIKA', byName='PIKA', at=8.75))
json.dump(ep, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
