# Day 8 (Matan, Oct 14): "dogs are invading town" mini movie, part 1. The dog army marches on Cat Town, Mango calls every cat,
# they build a box wall + yarn cannons, helmets on, flags up, face-off, the general and Mango meet nose to nose... TO BE CONTINUED (Day 9).
# Writes DIR/e1.json. Camera shots are in the battlefield frame (x sideways, z away from town toward the dogs), see W().
import json, sys, math
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 40.0
R0, ANG = 150, math.pi                        # cats' front line: 150 west of the square
WF = (math.cos(ANG) * R0, math.sin(ANG) * R0, math.atan2(math.cos(ANG), math.sin(ANG)))
def W(lx, y, lz):
    x0, z0, ry = WF; return [round(x0 + lx * math.cos(ry) + lz * math.sin(ry), 2), y, round(z0 - lx * math.sin(ry) + lz * math.cos(ry), 2)]
DOGS = [[0, 95], [1.6, 88], [1.6001, 235], [24.5, 52], [99, 52]]   # front row distance (keyframes)
def dz(t):
    for (a, va), (b, vb) in zip(DOGS, DOGS[1:]):
        if t < b: return va + (vb - va) * (t - a) / (b - a)
    return DOGS[-1][1]
S = []
def shot(t0, t1, p0, p1, l0, l1, io=0, fov=None): S.append(dict(t0=t0, t1=t1, p0=W(*p0), p1=W(*p1), l0=W(*l0), l1=W(*l1), inout=bool(io), **({'fov': fov} if fov else {})))
def wshot(t0, t1, p0, p1, l0, l1, io=0): S.append(dict(t0=t0, t1=t1, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)))
g0, g1 = dz(0) - 6, dz(1.6) - 6
shot(0, 1.6, (9, 2.6, g0 - 15), (7, 2.8, g1 - 14.5), (0, 4, g0 + 6), (0, 4, g1 + 6))                       # hook: low, the general + army march at us
wshot(1.6, 5.0, [60, 150, 130], [25, 118, 150], [0, 0, 10], [0, 0, 0])                                     # peaceful Cat Town from above
shot(5.0, 7.4, (-1.6, 2.7, 13.5), (-1.0, 2.4, 11.6), (0, 2.0, 6), (0, 2.0, 6))                            # Mango, the ground shakes
shot(7.4, 10.8, (2.6, 3.0, -1.5), (1.6, 4.2, 1.5), (0, 3.5, dz(7.4)), (0, 3, dz(10.8) + 8), fov=[42, 14])   # over Mango's shoulder, then a slow zoom: the dog army on the horizon
shot(10.8, 13.6, (4, 2.4, dz(10.8) - 20), (3, 2.6, dz(13.6) - 20), (0, 3.6, dz(10.8) - 3), (0, 3.6, dz(13.6) - 3))   # tracking: the army marches at us
shot(13.6, 17.0, (1.2, 2.2, 15.5), (.6, 1.9, 13.2), (0, 2.4, 6), (0, 2.6, 6))                              # Mango: MEOW
shot(17.0, 20.2, (-30, 62, -105), (-20, 52, -86), (0, 0, 5), (0, 0, 25))                                  # every cat runs out of town
shot(20.2, 25.2, (16, 25, 50), (7, 21, 46), (0, 1, -10), (0, 1, -12))                                     # box wall, yarn cannons, helmets, flags
shot(25.2, 27.45, (3, 13, -44), (2, 12, -38), (0, 2, 40), (0, 2, 40))                                      # behind the cats: 321 cats
shot(27.45, 29.3, (-4, 9, 92), (-3, 8.5, 86), (0, 2, 0), (0, 2, 0))                                        # behind the dogs: 150 dogs
shot(29.3, 32.5, (10, 5, -2), (8.5, 4.5, 7), (0, 3, 40), (0, 3, 24))                                      # the general walks out, Mango too
shot(32.5, 34.2, (18, 3.4, 21.2), (15, 3.2, 21.2), (0, 3.0, 21.1), (0, 3.1, 21.2))                    # nose to nose
shot(34.2, D + 1, (15, 3.2, 21.2), (15, 3.2, 21.2), (0, 3.1, 21.2), (0, 3.1, 21.2))
war = dict(ang=ANG, r=R0, cats=321, dogs=DOGS, gatherAt=16.8, meowAt=16.35, wallAt=20.3, cannonAt=21.5, helmetAt=22.7, flagAt=23.9, stepAt=29.4, mangoAt=30.4, meetZ=20, jawAt=33.5,
           dusk=[[0, .6], [1.6, .6], [1.61, 0], [7.4, 0], [10.8, .3], [25, .55], [34, .62]], shake=[[5.05, 7.4, .12], [10.8, 13.6, .04]])
e1 = dict(day=8, followersBefore=321, followersNew=0,
          landmarks=[dict(kind='fishmarket', sign='Fish Supermarket'), dict(kind='arcade', sign='Cat Arcade'), dict(kind='artstudio', sign='Art Studio'), dict(kind='pizza', sign='Giant Pizza'), dict(kind='toy', sign='Cat Toy Statue'), dict(kind='box', sign='Giant Cat Box')],
          noReserved=True, shots=S, duration=D + 1.1, starts=[0, 0, 0, 99], milestone=1e9, countFrom=0, war=war)
json.dump(e1, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('ok', D, WF)
