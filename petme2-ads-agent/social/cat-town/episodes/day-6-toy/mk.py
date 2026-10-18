# Day 6 (Matan said "lets build" Oct 13): top comment by bean, "CAN WE GET A HUGE CAT TOY STATUE FOR THE CATS TO PLAY WITH". Fun, no counting.
# Hook on the finished toy -> comment card -> Mango looks at us -> a box drops, then pedestal, yarn ball, feather wand, toy mouse, bells (one per word)
# -> cats run in and play -> wide shot -> "almost every cat": Mango walks past the toy and hops into the box it came in -> "Meow!" -> CTA + "Day 7: your idea?" lot -> loop.
# Writes DIR/e1.json.
import json, sys, math
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 29.0                        # video length; frames 0-1 s replay engine time D..D+1, so the loop is seamless
TS, IDEA = (47.2, 27.2, -2.09), (-0.1, -55.7, 0.0)    # SPOTS[4] toy, SPOTS[5] next idea lot
def W(spot, lx, y, lz):         # spot local (x right, z toward the town centre) -> world
    x0, z0, ry = spot; X = (math.cos(ry), -math.sin(ry)); Z = (math.sin(ry), math.cos(ry))
    return [round(x0 + lx * X[0] + lz * Z[0], 2), y, round(z0 + lx * X[1] + lz * Z[1], 2)]
HK0, HK1, HKl = W(TS, 19, 27, 52), W(TS, 14, 24, 46), W(TS, -2, 10, -1)        # hook: the finished toy statue
TOP0, TOP1, TOPl = [60, 150, 130], [25, 125, 150], [0, 0, 10]                 # the whole town
LT0, LT1, LTl = W(TS, -10, 22, 46), W(TS, -6, 18, 40), W(TS, 0, 3, 0)         # the empty lot + sign (comment card on top)
MG0, MG1, MGl = W(TS, -0.6, 4.3, 26.6), W(TS, -1.2, 4.0, 24.6), W(TS, -2.9, 2.6, 16.8)   # Mango looks at us
BD0, BD1, BDl = W(TS, -12, 31, 64), W(TS, -8, 27, 57), W(TS, -3, 10, 0)       # the build
PL0, PL1, PLl = W(TS, 21, 17, 31), W(TS, 17, 15, 27.5), W(TS, 3, 3.5, 6)          # the cats play
WD0, WD1, WDl = W(TS, -26, 58, 92), W(TS, -16, 50, 82), W(TS, 0, 6, 6)        # wide: the toy + the other builds
BX0, BX1, BXl = W(TS, -2, 9, 31), W(TS, -5, 8, 27), W(TS, -9, 3, 10)          # Mango walks to the box
FC0, FC1, FCl = W(TS, -10.8, 6.6, 19.5), W(TS, -11.4, 6.1, 17.4), W(TS, -12.8, 3.7, 7.0)   # Mango in the box
ID0, ID1, IDl = W(IDEA, 6, 9, 30), W(IDEA, 4, 8, 25), W(IDEA, 0, 11, 0)      # "Day 7: your idea?" lot
S = [
 (1.0, 1.6, HK1, TOP0, HKl, TOPl, 1),               # cut away from the hook, up over the town
 (1.6, 2.9, TOP0, TOP1, TOPl, TOPl, 0),
 (2.9, 3.5, TOP1, LT0, TOPl, LTl, 1),               # to the empty lot (comment card)
 (3.5, 7.0, LT0, LT1, LTl, LTl, 0),
 (7.0, 9.6, MG0, MG1, MGl, MGl, 0),                 # Mango looks at us
 (9.6, 9.9, MG1, BD0, MGl, BDl, 1),
 (9.9, 15.8, BD0, BD1, BDl, BDl, 0),                # box, pedestal, yarn ball, wand, mouse, bells
 (15.8, 16.2, BD1, PL0, BDl, PLl, 1),
 (16.2, 18.7, PL0, PL1, PLl, PLl, 0),               # cats play
 (18.7, 19.2, PL1, WD0, PLl, WDl, 1),
 (19.2, 20.4, WD0, WD1, WDl, WDl, 0),               # wide
 (20.4, 20.8, WD1, BX0, WDl, BXl, 1),
 (20.8, 22.4, BX0, BX1, BXl, BXl, 0),               # "almost every cat": Mango walks to the box
 (22.4, 24.9, FC0, FC1, FCl, FCl, 0),               # in the box, turns: "Meow!"
 (24.9, 25.5, FC1, ID0, FCl, IDl, 1),
 (25.5, 27.9, ID0, ID1, IDl, IDl, 0),               # Day 7: your idea?
 (27.9, 28.6, ID1, HK0, IDl, HKl, 1),               # back to the hook (= frame 0)
 (28.6, D + 1.05, HK0, HK1, HKl, HKl, 0),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
TXT = 'CAN WE GET A HUGE CAT TOY STATUE FOR THE CATS TO PLAY WITH'
NAME = '‿ ◟🍏 beαn 🐾˳ ꒱'
cm = dict(list=[dict(by='bean', name=NAME, text=TXT, likes=None)], win=0, t=dict(up=2.95, scroll=3.1, stop=4.1, down=6.9))
PARTS = [9.85, 10.65, 11.5, 12.65, 13.5, 14.35]                         # box, pedestal, yarn ball, feather wand, toy mouse, bells
nb = dict(kind='toy', sign='Cat Toy Statue', name='Cat Toy Statue', by='bean', byName='bean', at=7.0, slow=8.35, partsAt=PARTS, openAt=16.0)
e1 = dict(day=6, followersBefore=261, followersNew=0,
          landmarks=[dict(kind='fishmarket', sign='Fish Supermarket'), dict(kind='arcade', sign='Cat Arcade'), dict(kind='artstudio', sign='Art Studio'), dict(kind='pizza', sign='Giant Pizza')],
          newBuild=nb, lotSign='For bean', lotUntil=10.3, idea=dict(spot=5, sign='Day 7: your idea?'), comments=cm, noReserved=True, shots=shots, duration=D + 1.1,
          starts=[0, 0, 0, 99], milestone=1e9, countFrom=0, toy=dict(lookAt=[7.1, 9.5], boxAt=20.7, turnAt=23.9))
json.dump(e1, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('ok', D)
