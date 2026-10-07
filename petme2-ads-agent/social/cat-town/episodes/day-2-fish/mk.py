# Day 2 "Fish supermarket": camera shots + one engine page.
# Town now full: the 128 Day-1 followers' houses (followersBefore=128) + Mango; the real most-liked comment card; the shop builds slowly, piece by piece (9.0 -> 13.5 s).
import json, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 21.7
FOL = 128
H0p, H0l = [5, 8, 17], [0, 2.2, 0]              # frame 0 = last frame: Mango sitting between the fountain and the feeder
LOTp, LOTl = [-6, 11, 12], [0, 9, 44]           # the empty lot with the "Your idea here?" sign
S = [
 (0.0, 1.8, H0p, [4.6, 7.6, 16], H0l, H0l, 0),
 (1.8, 4.4, [4.6, 7.6, 16], [70, 190, 170], H0l, [0, 0, -10], 1),                  # pull back: the town full of new houses
 (4.4, 5.8, [70, 190, 170], LOTp, [0, 0, -10], LOTl, 1),                           # swoop down to the empty lot
 (5.8, 8.8, LOTp, [-4, 10.5, 16], LOTl, LOTl, 0),                                  # the most-liked comment card over the lot
 (8.8, 14.6, [30, 32, -12], [-26, 28, -8], [0, 19, 47], [0, 19, 47], 0),           # slow build, slow orbit, sign + confetti at the end
 (14.6, 16.4, [45, 260, -80], [36, 225, -62], [0, 0, 92], [0, 0, 88], 1),          # high above: the only shop among the houses
 (16.4, 18.1, [36, 225, -62], [40, 120, -70], [0, 0, 88], [0, 0, 15], 1),
 (18.1, 21.0, [40, 120, -70], [150, 105, 70], [0, 0, 15], [0, 0, 20], 0),
 (21.0, D, [150, 105, 70], H0p, [0, 0, 20], H0l, 1),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
cm = dict(list=[dict(by='PIKA', name='PIKA (winter arc☠️)', text='add a fish supermarket', likes=None)], win=0, t=dict(up=5.85, scroll=6.1, stop=7.4, down=8.75))
ep = dict(day=2, followersBefore=FOL, followersNew=0, landmarks=[], shots=shots, duration=D, starts=[0, 0, 0, 99], milestone=1e9, noReserved=False, countFrom=FOL, lotSign='Your idea here?',
          comments=cm, newBuild=dict(kind='fishmarket', sign='Fish Supermarket', name='Fish Supermarket', by='PIKA', byName='PIKA', at=9.0, slow=4.5))
json.dump(ep, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
