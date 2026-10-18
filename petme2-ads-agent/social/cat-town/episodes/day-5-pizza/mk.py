# Day 5 (Matan said "go" Oct 11): top comment by MrFireman, "ADD A GIANT SLICE OF PIZZA WITH EVERY SINGLE PIECE OF TOPPING ON IT". Fun, no counting.
# Hook on the finished slice -> comment card -> Mango looks at us -> crust drops, sauce, cheese, every topping (one per word) -> pineapple (one cat walks off)
# -> a fish on top -> wide shot with the fish shop, arcade and art studio -> Mango bites, turns with cheese on his face -> CTA + "Day 6: your idea?" lot -> loop.
# Writes DIR/e1.json.
import json, sys, math
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 30.6                        # video length; frames 0-1 s replay engine time D..D+1, so the loop is seamless
PZ, IDEA = (-47.1, 27.3, 2.1), (47.2, 27.2, -2.09)    # SPOTS[3] pizza, SPOTS[4] next idea lot
FISH, ARC, ST = (-0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (44.6, -25.8, -1.05)   # SPOTS[0..2], filled from window.__spots below
try:
    sp = json.load(open(f'{out}/spots.json')); FISH, ARC, ST = tuple(sp[0]), tuple(sp[1]), tuple(sp[2])
except FileNotFoundError: pass
def W(spot, lx, y, lz):         # spot local (x right, z toward Mango) -> world
    x0, z0, ry = spot; X = (math.cos(ry), -math.sin(ry)); Z = (math.sin(ry), math.cos(ry))
    return [round(x0 + lx * X[0] + lz * Z[0], 2), y, round(z0 + lx * X[1] + lz * Z[1], 2)]
HK0, HK1, HKl = W(PZ, 16, 24, 46), W(PZ, 11, 21, 40), W(PZ, 0, 7, -3)          # hook: the finished slice
TOP0, TOP1, TOPl = [60, 150, 130], [25, 125, 150], [0, 0, 10]                 # the whole town
LT0, LT1, LTl = W(PZ, -10, 22, 46), W(PZ, -6, 18, 40), W(PZ, 0, 3, 0)         # the empty lot + sign (comment card on top)
MG0, MG1, MGl = W(PZ, 2.5, 4.2, 25), W(PZ, 1.8, 3.9, 23), W(PZ, 0, 2.6, 14)
BD0, BD1, BDl = W(PZ, -19, 27, 52), W(PZ, -14, 23, 46), W(PZ, 0, 6, -4)       # the build
PN0, PN1, PNl = W(PZ, 6, 12, 30), W(PZ, 4, 11, 27), W(PZ, 0, 3, 14)           # pineapple: the spectators freeze, one walks off
WD0, WD1, WDl = W(PZ, 26, 58, 92), W(PZ, 16, 50, 82), W(PZ, 0, 4, 8)         # wide: pizza + the other builds toward the centre
BT0, BT1, BTl = W(PZ, -15, 6.5, 14), W(PZ, -13, 6, 13), W(PZ, 0, 2.4, 11.5)
FC0, FC1, FCl = W(PZ, 1.4, 4.3, 22.8), W(PZ, 1.0, 4.1, 21.6), W(PZ, 0, 3.0, 14.4)
ID0, ID1, IDl = W(IDEA, 6, 9, 30), W(IDEA, 4, 8, 25), W(IDEA, 0, 11, 0)      # "Day 6: your idea?" lot
S = [
 (1.0, 1.6, HK1, TOP0, HKl, TOPl, 1),               # cut away from the hook, up over the town
 (1.6, 2.9, TOP0, TOP1, TOPl, TOPl, 0),
 (2.9, 3.5, TOP1, LT0, TOPl, LTl, 1),               # to the empty lot (comment card)
 (3.5, 7.2, LT0, LT1, LTl, LTl, 0),
 (7.2, 9.4, MG0, MG1, MGl, MGl, 0),                 # Mango looks at us
 (9.4, 9.75, MG1, BD0, MGl, BDl, 1),
 (9.75, 17.7, BD0, BD1, BDl, BDl, 0),               # crust, sauce, cheese, every topping
 (17.7, 20.2, PN0, PN1, PNl, PNl, 0),               # pineapple
 (20.2, 22.1, BD1, BD0, BDl, BDl, 0),               # the fish, cats climb on
 (22.1, 22.7, BD0, WD0, BDl, WDl, 1),
 (22.7, 24.6, WD0, WD1, WDl, WDl, 0),               # wide: fish shop, arcade, studio
 (24.6, 25.8, BT0, BT1, BTl, BTl, 0),               # bite
 (25.8, 27.0, FC0, FC1, FCl, FCl, 0),               # cheesy face, meow
 (27.0, 27.7, FC1, ID0, FCl, IDl, 1),
 (27.7, 29.6, ID0, ID1, IDl, IDl, 0),               # Day 6: your idea?
 (29.6, 30.3, ID1, HK0, IDl, HKl, 1),               # back to the hook (= frame 0)
 (30.3, D + 1.05, HK0, HK1, HKl, HKl, 0),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
TXT = 'ADD A GIANT SLICE OF PIZZA WITH EVERY SINGLE PIECE OF TOPPING ON IT'
cm = dict(list=[dict(by='MrFireman', name='MrFireman', text=TXT, likes=None)], win=0, t=dict(up=2.95, scroll=3.1, stop=4.1, down=7.1))
PARTS = [9.6, 9.75, 10.4, 11.05,                                      # stand, crust, sauce, cheese
         11.8, 12.55, 13.3, 13.95, 14.6, 15.25, 15.85,                # pepperoni, mushrooms, olives, peppers, onions, corn, bacon
         16.45, 16.6, 16.75,                                          # "everything": tomato, jalapeño, basil
         17.95, 20.45]                                                # pineapple, fish
nb = dict(kind='pizza', sign='Giant Pizza', name='Giant Pizza', by='MrFireman', byName='MrFireman', at=7.2, slow=14.2, partsAt=PARTS, openAt=21.4)
e1 = dict(day=5, followersBefore=261, followersNew=0, landmarks=[dict(kind='fishmarket', sign='Fish Supermarket'), dict(kind='arcade', sign='Cat Arcade'), dict(kind='artstudio', sign='Art Studio')],
          newBuild=nb, lotSign='For @MrFireman', lotUntil=10.15, idea=dict(spot=4, sign='Day 6: your idea?'), comments=cm, noReserved=True, shots=shots, duration=D + 1.1,
          starts=[0, 0, 0, 99], milestone=1e9, countFrom=0, pizza=dict(lookAt=[7.3, 9.05], walkAt=18.75, biteAt=24.95, turnAt=25.9))
json.dump(e1, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('ok', D)
