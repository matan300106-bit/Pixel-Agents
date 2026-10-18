# Day 9 (Matan, Oct 18): "continue with the dogs, build tension, a couple of days". Part 2 of the dog invasion mini movie.
# Opens on Day 8's frozen frame. The general: "Give us your fountain." Mango: "Never!" "Then at sunrise... we attack." The dogs howl, night falls,
# 321 pairs of cat eyes glow in the dark, Mango sends a spy cat past the sleeping dogs and the camp fires... and he sees a GIANT dog. TO BE CONTINUED.
# Writes DIR/e1.json. Camera shots are in the battlefield frame (x sideways, z away from town toward the dogs), see W(). Day 8 times are shifted by -34 (Day 8's freeze = t 0).
import json, sys, math
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 48.5; FREEZE = 43.3
R0, ANG = 150, math.pi
WF = (math.cos(ANG) * R0, math.sin(ANG) * R0, math.atan2(math.cos(ANG), math.sin(ANG)))
def W(lx, y, lz):
    x0, z0, ry = WF; return [round(x0 + lx * math.cos(ry) + lz * math.sin(ry), 2), y, round(z0 - lx * math.sin(ry) + lz * math.cos(ry), 2)]
S = []
def shot(t0, t1, p0, p1, l0, l1, io=0, fov=None, lin=0): S.append(dict(t0=t0, t1=t1, p0=W(*p0), p1=W(*p1), l0=W(*l0), l1=W(*l1), inout=bool(io), **({'fov': fov} if fov else {}), **({'lin': True} if lin else {})))
def wshot(t0, t1, p0, p1, l0, l1, io=0): S.append(dict(t0=t0, t1=t1, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)))
SPY = [[27.0, 1.8, 7.5], [31.0, 1.8, 7.5], [32.6, 1.75, 12.5],          # leaves the gate
       [32.61, 1.65, 47], [36.0, 1.65, 64],                               # between the sleeping dogs
       [36.01, 1.2, 90], [39.2, .4, 106],                                 # past the tents + fires
       [39.21, .4, 113], [41.1, .4, 120.5]]                               # behind the camp: stops
shot(0, 1.4, (15, 3.2, 21.2), (15, 3.2, 21.2), (0, 3.1, 21.2), (0, 3.1, 21.2))                                  # Day 8's frozen frame
shot(1.4, 6.4, (3.0, 1.6, 15.8), (2.4, 1.8, 17.2), (0, 3.9, 23.6), (0, 3.9, 23.6))                               # the general talks (Mango in front)
wshot(6.4, 9.2, [-48, 26, 46], [-38, 20, 36], [-11.5, 2, 0], [-11.5, 2, 0])                                    # the fountain in town
shot(9.2, 10.8, (1.9, 2.3, 23.6), (1.5, 2.1, 23.0), (0, 1.8, 20), (0, 1.8, 20))                                # Mango: NEVER!
shot(10.8, 14.4, (-3.4, 2.0, 17.2), (-2.7, 2.3, 18.5), (0, 3.6, 23.6), (0, 3.7, 23.6))                           # the general: at sunrise we attack
shot(14.4, 16.8, (-6.5, 1.8, 16.5), (-5.5, 2.1, 17.8), (0, 5, 29), (0, 5.4, 29))                                             # the dogs howl
shot(16.8, 19.6, (22, 28, -12), (18, 34, -16), (0, 0, 30), (0, 0, 40))                                           # walk back, night falls
shot(19.6, 23.0, (6, 7, -3), (5, 7.5, -2), (0, 2, 95), (0, 2.5, 95), fov=[28, 22])                               # the dog camp fires across the field
shot(23.0, 26.6, (10, 8.5, 4), (7, 7.5, 3), (0, 0, -22), (0, 0, -20))                                            # 321 pairs of eyes
shot(26.6, 32.6, (5.2, 3.2, 15), (4.0, 2.6, 13.5), (.9, 1.3, 6.5), (1.6, 1.0, 9.5))                                # Mango sends the spy
shot(32.6, 36.0, (5.5, 4.6, 40), (5.0, 4.6, 57), (1.65, .6, 47), (1.65, .6, 64), lin=1)                          # past the sleeping dogs
shot(36.0, 39.2, (-3, 2.4, 84), (-3.5, 2.2, 100), (1.2, .8, 90), (.4, .8, 106), lin=1)                           # past the camp fires
shot(39.2, 41.4, (2.2, 1.4, 106), (1.6, 1.3, 113.5), (.4, 1.0, 113), (.4, 1.3, 120.5))                          # behind the camp, he stops
shot(41.4, FREEZE, (1.4, 1.0, 112), (1.2, .5, 108), (.4, 1.5, 120.5), (0, 20, 160), io=1)                    # ...the camera tilts up: a GIANT dog, red eyes open
shot(FREEZE, D + 1, (1.2, .5, 108), (1.2, .5, 108), (0, 20, 160), (0, 20, 160))
war = dict(ang=ANG, r=R0, cats=321, dogs=[[0, 52]], gatherAt=-17.2, meowAt=-17.65, wallAt=-13.7, cannonAt=-12.5, helmetAt=-11.3, flagAt=-10.1, stepAt=-4.6, mangoAt=-3.6, meetZ=20, jawAt=-.5,
           talk=[[1.5, 3.42], [3.8, 6.0], [11.0, 13.85]], mangoTalk=[[9.5, 9.95], [30.0, 31.05]], howl=[14.5, 16.6], genBack=16.7, mangoBack=17.0, campAt=18.0, sleepAt=19.4, eyesAt=22.6,
           spy=SPY, spyLook=41.5, giant=dict(at=41.35, x=0, z=175, s=18, eyesAt=42.55), moon=[30, 300, 740],
           dusk=[[0, .62], [6.4, .62], [9.2, .62], [16.8, .7], [20.5, 2]], shake=[[42.5, 43.3, .05]])
e1 = dict(day=9, followersBefore=321, followersNew=0,
          landmarks=[dict(kind='fishmarket', sign='Fish Supermarket'), dict(kind='arcade', sign='Cat Arcade'), dict(kind='artstudio', sign='Art Studio'), dict(kind='pizza', sign='Giant Pizza'), dict(kind='toy', sign='Cat Toy Statue'), dict(kind='box', sign='Giant Cat Box')],
          noReserved=True, shots=S, duration=D + 1.1, starts=[0, 0, 0, 99], milestone=1e9, countFrom=0, war=war)
json.dump(e1, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('ok', D)
