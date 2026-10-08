# Day 3 (Matan approved the script Oct 8): hook on the glowing arcade -> francisco12321's comment -> his lot -> split Day 1 vs today (253 houses, 467 cats)
# -> more cats than houses (crowd under "No home yet") -> evening falls, the Cat Arcade builds piece by piece -> neon on, cats run in, Mango wins a fish -> follow CTA -> Day 4 lot -> loop.
# Writes DIR/e1.json (Day 3 town) and DIR/e0.json (Day 1: Mango alone, top half of the split screen).
import json, sys, math
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 31.2                       # video length; frames 0-1 s replay engine time D..D+1 (the hero shot), so the loop is seamless
HOUSES, LIKES = 253, 467       # Matan, Oct 8: 253 followers = 253 houses, 467 likes = 467 cats (Mango is one of them)
STRAYS = LIKES - 1 - HOUSES    # cats with no house yet
A, B, C3 = (44.6, -25.8, -1.05), (-44.7, -25.7, 1.05), (-47.1, 27.3)   # SPOTS[2] arcade, SPOTS[1] Day 4 lot, SPOTS[3] the homeless crowd
def W(spot, lx, y, lz):        # arcade/lot local (x right, z toward Mango) -> world
    x0, z0, ry = spot; X = (math.cos(ry), -math.sin(ry)); Z = (math.sin(ry), math.cos(ry))
    return [round(x0 + lx * X[0] + lz * Z[0], 2), y, round(z0 + lx * X[1] + lz * Z[1], 2)]
H0p, H0l = [5, 8, 17], [0, 2.2, 0]
HERO0, HERO1, HEROl = W(A, -36, 30, 58), W(A, -30, 27, 51), W(A, 0, 11, -2)
LOTp, LOTl = W(A, 0, 9, 30), W(A, 0, 10, 0)
CRp0, CRp1, CRl = [-12, 22, 7], [-20, 17, 11.5], [-47.1, 9, 27.3]
BLD0, BLD1 = W(A, -38, 34, 64), W(A, -26, 26, 52)
CLW0, CLW1, CLWl = W(A, -4, 11, 30), W(A, -6, 9, 24), W(A, -7.2, 6.5, 5.4)
UPp, UPl = [95, 150, 120], [0, 0, 0]
D4p, D4l = W(B, 0, 9, 30), W(B, 0, 6.5, 0)
S = [
 (1.0, 3.0, [60, 120, 140], [12, 32, 48], [0, 0, 0], H0l, 0),          # day: the town, down toward Mango
 (3.0, 6.9, [12, 32, 48], [-30, 60, 95], H0l, [0, 0, 10], 0),          # comment card over the town
 (6.9, 8.95, [-30, 60, 95], LOTp, [0, 0, 10], LOTl, 1),                # fly to Francisco's lot
 (8.95, 9.0, LOTp, LOTp, LOTl, LOTl, 0),
 (9.0, 14.5, [0, 270, 180], [30, 230, 200], [0, 0, 0], [0, 0, 10], 0),  # split bottom: the whole town, strays pop in
 (14.5, 16.6, CRp0, CRp1, CRl, CRl, 0),                                # the crowd with no home
 (16.6, 17.5, CRp1, [0, 75, -8], CRl, [20, 0, -12], 1),                 # whip up over the fountain while evening falls
 (17.5, 18.4, [0, 75, -8], BLD0, [20, 0, -12], HEROl, 1),               # down to Francisco's lot
 (18.4, 22.9, BLD0, BLD1, HEROl, HEROl, 0),                            # slow build, neon on, cats run in
 (22.9, 25.7, CLW0, CLW1, CLWl, CLWl, 0),                              # Mango at the claw machine
 (25.7, 27.2, CLW1, UPp, CLWl, UPl, 1),                                # pull up over the glowing town
 (27.2, 28.7, UPp, [110, 160, 90], UPl, UPl, 0),
 (28.7, 29.6, [110, 160, 90], D4p, UPl, D4l, 1),                       # the Day 4 lot
 (29.6, 30.3, D4p, W(B, 0, 8, 25), D4l, D4l, 0),
 (30.3, 30.95, W(B, 0, 8, 25), HERO0, D4l, HEROl, 1),                 # back to the glowing arcade (= frame 0)
 (30.95, D + 1.05, HERO0, HERO1, HEROl, HEROl, 0),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
CN = 70
at = []
for j in range(STRAYS):        # roof/street strays pop while the voice says "467 cats"; the crowd pops on "more cats than houses"
    if 12 <= j < 12 + CN: at.append(round(14.55 + .7 * (j - 12) / CN, 3))
    else: k = j if j < 12 else j - CN; at.append(round(11.2 + 2.8 * ((k + .5) / (STRAYS - CN)) ** .8, 3))
cm = dict(list=[dict(by='francisco12321', name='francisco12321', text='can u show me next time ? and make a cat arcade!', likes=None)], win=0, t=dict(up=3.05, scroll=3.2, stop=4.25, down=6.85))
nb = dict(kind='arcade', sign='Cat Arcade', name='Cat Arcade', by='francisco12321', byName='@francisco12321', at=18.55, slow=3.3,
          partsAt=[18.6, 19.35, 19.75, 20.2, 20.6, 21.0], lightsAt=21.62, openAt=21.95)
e1 = dict(day=3, followersBefore=HOUSES, followersNew=0, landmarks=[dict(kind='fishmarket', sign='Fish Supermarket'), dict(kind='reserved', sign='Day 4: your idea?')],
          newBuild=nb, lotSign='For @francisco12321', comments=cm, noReserved=True, shots=shots, duration=D + 1.1, starts=[0, 0, 0, 99], milestone=1e9, countFrom=0,
          dusk=dict(**{'from': 16.7, 'to': 18.5}), clawAt=23.05, strays=dict(n=STRAYS, at=at, near=[0, 0], crowd=CN, crowdSpot=3, sign='No home yet', signAt=14.5))
json.dump(e1, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
e0 = dict(day=1, followersBefore=0, followersNew=0, landmarks=[], noReserved=True, duration=D + 1.1, starts=[0, 0, 0, 99], milestone=1e9,
          shots=[dict(t0=0, t1=99, p0=[9, 16, 34], p1=[7, 13, 28], l0=[0, 4, 0], l1=[0, 4, 0], inout=False)])
json.dump(e0, open(f'{out}/e0.json', 'w'), ensure_ascii=False)
print('strays', STRAYS, 'hero', HERO0, 'claw', CLWl)
