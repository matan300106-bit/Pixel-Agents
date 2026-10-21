# Day 10 (Matan, Oct 21): "Lets do a day 10". Part 3 of the dog invasion mini movie, "The Giant" (plan: project files cat-town/day-9/story-plan.md).
# Opens on Day 9's frozen frame (the giant's red eyes). The giant looks down at the spy, the spy RUNS, the dog camp wakes up and barks, the spy jumps the box wall,
# "Mango! They have a GIANT!", the cats panic, Mango: "Then we build our OWN giant!", 321 cats climb on each other = MEGA MANGO (Mango rides on top), the sun comes up,
# the giant walks out of the camp (BOOM BOOM), Mega Mango stands up, MEOW. TO BE CONTINUED.
# Writes DIR/e1.json. Camera shots are in the battlefield frame (x sideways, z away from town toward the dogs), see W(). Day 9 times are shifted by -43.3 (Day 9's freeze = t 0).
import json, sys, math
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 51.6; FREEZE = 45.4; O = -43.3
R0, ANG = 150, math.pi
WF = (math.cos(ANG) * R0, math.sin(ANG) * R0, math.atan2(math.cos(ANG), math.sin(ANG)))
def W(lx, y, lz):
    x0, z0, ry = WF; return [round(x0 + lx * math.cos(ry) + lz * math.sin(ry), 2), y, round(z0 - lx * math.sin(ry) + lz * math.cos(ry), 2)]
S = []
def shot(t0, t1, p0, p1, l0, l1, io=0, fov=None, lin=0): S.append(dict(t0=t0, t1=t1, p0=W(*p0), p1=W(*p1), l0=W(*l0), l1=W(*l1), inout=bool(io), **({'fov': fov} if fov else {}), **({'lin': True} if lin else {})))
SPY = [[-1, .4, 120.5], [4.5, .4, 120.5], [4.8, .6, 118], [6.4, 1.2, 104], [8.0, 1.6, 82], [9.6, 1.8, 58], [11.2, 5.0, 20], [11.8, 5.4, 11],   # runs back through the camp + the dogs
       [13.2, 4.8, -1.2], [13.7, 2.6, -1.7]]                                                                                                        # over the box wall, to Mango
BOOMS = [38.0, 39.0, 40.0, 41.0]
shot(0, 1.4, (1.2, .5, 108), (1.2, .5, 108), (0, 20, 160), (0, 20, 160))                                         # Day 9's frozen frame
shot(1.4, 4.5, (1.2, .5, 108), (2.0, 1.0, 110.5), (0, 20, 160), (0, 13, 160))                                    # the giant looks down at him
shot(4.5, 6.4, (-1.6, 1.5, 112.5), (-1.6, 1.8, 101), (.4, 1.4, 119), (1.1, 1.6, 104), lin=1)                      # the spy turns and RUNS
shot(6.4, 9.4, (20, 9, 72), (17, 8, 56), (1, 1.5, 80), (1.5, 1.5, 58))                                           # the camp wakes up, barking
shot(9.4, 11.6, (7.5, 3.4, -4), (7.0, 3.6, -2.5), (3, 1.6, 40), (5, 2.2, 13))                                     # behind the wall: he comes, the dogs behind him
shot(11.6, 13.7, (3, 1.6, 22), (3.2, 1.8, 20), (5, 5, 6), (4.8, 6, 0))                                        # the jump (slow)
shot(13.7, 16.8, (7.6, 3.4, -9.6), (6.9, 3.2, -9.0), (1.3, 1.5, -2.4), (1.2, 1.6, -2.4))                         # "Mango! They have a GIANT!"
shot(16.8, 19.6, (26, 15, -6), (22, 13, -10), (0, 0, -20), (0, 0, -20))                                         # panic
shot(19.6, 23.6, (.9, 2.6, 1.6), (.6, 2.4, .8), (0, 2.0, -3), (0, 2.1, -3))                                     # Mango: "then we build our OWN giant"
shot(23.6, 31.0, (40, 8, 28), (56, 24, 40), (0, 8, -20), (0, 14, -20), io=1)                                      # the cats climb: the tower grows
shot(31.0, 34.2, (13, 4, 33), (11, 5, 29), (0, 20, -20), (0, 22, -20), fov=[50, 48])                                           # MEGA MANGO
shot(34.2, 37.0, (-16, 26, -58), (-14, 24, -54), (0, 12, 120), (0, 14, 120))                                    # the sun comes up
shot(37.0, 41.4, (30, 4, 30), (28, 4.5, 27), (0, 20, 150), (0, 22, 105))                                       # BOOM BOOM: the giant walks out of the camp
shot(41.4, 43.4, (3, 2.5, 38), (4, 3.5, 41), (0, 20, -20), (0, 25, -20), fov=[50, 50])                                          # Mega Mango stands up
shot(43.4, FREEZE, (-24, 10, -82), (-23, 11, -78), (6, 24, 100), (6, 25, 100))                                    # face to face: MEOW
shot(FREEZE, D + 1, (-23, 11, -78), (-23, 11, -78), (6, 25, 100), (6, 25, 100))
sh = lambda v: round(v + O, 3)
war = dict(ang=ANG, r=R0, cats=321, dogs=[[0, 52], [6.6, 52], [9.4, 44]], gatherAt=sh(-17.2), meowAt=sh(-17.65), wallAt=sh(-13.7), cannonAt=sh(-12.5), helmetAt=sh(-11.3), flagAt=sh(-10.1),
           stepAt=sh(-4.6), mangoAt=sh(-3.6), meetZ=20, jawAt=sh(-.5), talk=[[sh(1.5), sh(3.42)], [sh(11.0), sh(13.85)]], genBack=sh(16.7), mangoBack=sh(17.0), mangoZ=-3,
           campAt=sh(18.0), sleepAt=sh(19.4), eyesAt=sh(22.6), eyesOff=34.6, wakeAt=6.0, bark=[6.1, 12.5], panic=[16.9, 19.6],
           mangoTalk=[[19.9, 21.05], [21.5, 23.45]], spy=SPY, spyLook=[[-5, 4.4]], spyJump=[11.8, 13.2, 8],
           giant=dict(at=sh(41.35), x=0, z=175, s=18, eyesAt=sh(42.55), walk=[[37.0, 175], [41.0, 100]], lean=[[0, .16], [1.6, .16], [3.4, .34], [4.6, .34], [5.8, .16]], glow=[[1.4, 1], [2.8, 1.7], [5.0, 1.7], [6.2, 1]]),
           mega=dict(at=23.6, dur=6.0, x=0, z=-20, s=24, cs=2.4, fullAt=30.9, mangoTop=30.9, standAt=41.6, roar=[43.45, 44.5]),
           moon=[30, 300, 740], dusk=[[0, 2], [1.3, 2], [1.6, 1.6], [33.8, 1.6], [36.8, 1.0], [40.5, .55]],
           shake=[[0, .25, .05], [30.9, 31.4, .25]] + [[b, b + .45, .45] for b in BOOMS] + [[43.45, 44.3, .2]])
e1 = dict(day=10, followersBefore=321, followersNew=0,
          landmarks=[dict(kind='fishmarket', sign='Fish Supermarket'), dict(kind='arcade', sign='Cat Arcade'), dict(kind='artstudio', sign='Art Studio'), dict(kind='pizza', sign='Giant Pizza'), dict(kind='toy', sign='Cat Toy Statue'), dict(kind='box', sign='Giant Cat Box')],
          noReserved=True, shots=S, duration=D + 1.1, starts=[0, 0, 0, 99], milestone=1e9, countFrom=0, war=war)
json.dump(e1, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
json.dump(dict(booms=BOOMS), open(f'{out}/fx.json', 'w'))
print('ok', D)
