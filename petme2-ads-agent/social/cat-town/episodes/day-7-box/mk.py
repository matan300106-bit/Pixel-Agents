# Day 7 (Matan, Oct 13): top comment by wil.son, "A giant box for all the cats" + the 1 week party (321 followers, 562 likes). Callback: on Day 6 Mango picked the box over the toy.
# Hook on the finished box -> comment card -> Mango looks at us -> the giant box drops, then flaps, cat doors, peek holes, scratch ramp, party flags (one per word)
# -> cats run in, heads pop out of every hole -> wide: "1 WEEK" + confetti -> "where's Mango?" -> Mango sits in his own small box -> "Meow!" -> CTA + "Day 8: your idea?" lot -> loop.
# Writes DIR/e1.json.
import json, sys, math
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 32.0                        # video length; frames 0-1 s replay engine time D..D+1, so the loop is seamless
BS, IDEA = (-0.1, -55.7, 0.0), (-78.4, -3.8, 1.52)    # SPOTS[5] giant box, SPOTS[6] next idea lot
def W(spot, lx, y, lz):         # spot local (x right, z toward the town centre) -> world
    x0, z0, ry = spot; X = (math.cos(ry), -math.sin(ry)); Z = (math.sin(ry), math.cos(ry))
    return [round(x0 + lx * X[0] + lz * Z[0], 2), y, round(z0 + lx * X[1] + lz * Z[1], 2)]
HK0, HK1, HKl = W(BS, 25, 29, 70), W(BS, 18, 25, 62), W(BS, -1, 8.5, 0)          # hook: the finished box full of cats
TOP0, TOP1, TOPl = [60, 150, 130], [25, 125, 150], [0, 0, 10]                 # the whole town
LT0, LT1, LTl = W(BS, -10, 22, 46), W(BS, -6, 18, 40), W(BS, 0, 3, 0)         # the empty lot + sign (comment card on top)
MG0, MG1, MGl = W(BS, -0.6, 4.3, 26.6), W(BS, -1.2, 4.0, 24.6), W(BS, -2.9, 2.6, 16.8)   # Mango looks at us
BD0, BD1, BDl = W(BS, -13.5, 36, 81), W(BS, -9, 31.5, 72), W(BS, 0, 9, 0)           # the build
PL0, PL1, PLl = W(BS, 13, 12, 59), W(BS, 8, 11.3, 51), W(BS, 0, 6.5, 3)          # cats get in, heads pop out
WD0, WD1, WDl = W(BS, -15.6, 37, 70), W(BS, -26, 50, 94), W(BS, 0, 9, 0)        # wide: 1 week party (slow pull back)
SR0, SR1, SRl0, SRl1 = W(BS, 14, 31, 31), W(BS, -8, 31, 31), W(BS, 4, 13, -2), W(BS, -6, 13, -2)   # "where's Mango?": pan across the heads on top
FC0, FC1, FCl = W(BS, -19, 10, 33), W(BS, -19, 9, 29.5), W(BS, -12, 5, 11)   # Mango in his small box, the giant box behind
ID0, ID1, IDl = W(IDEA, 6, 9, 30), W(IDEA, 4, 8, 25), W(IDEA, 0, 11, 0)      # "Day 8: your idea?" lot
S = [
 (1.0, 1.6, HK1, TOP0, HKl, TOPl, 1),               # cut away from the hook, up over the town
 (1.6, 2.9, TOP0, TOP1, TOPl, TOPl, 0),
 (2.9, 3.5, TOP1, LT0, TOPl, LTl, 1),               # to the empty lot (comment card)
 (3.5, 7.0, LT0, LT1, LTl, LTl, 0),
 (7.0, 9.6, MG0, MG1, MGl, MGl, 0),                 # Mango looks at us
 (9.6, 9.9, MG1, BD0, MGl, BDl, 1),
 (9.9, 15.8, BD0, BD1, BDl, BDl, 0),                # box, flaps, doors, holes, ramp, flags
 (15.8, 16.2, BD1, PL0, BDl, PLl, 1),
 (16.2, 18.6, PL0, PL1, PLl, PLl, 0),               # cats get in
 (18.6, 19.0, PL1, WD0, PLl, WDl, 1),
 (19.0, 23.6, WD0, WD1, WDl, WDl, 0),               # 1 week party
 (23.6, 24.0, WD1, SR0, WDl, SRl0, 1),
 (24.0, 25.2, SR0, SR1, SRl0, SRl1, 0),             # where's Mango?
 (25.2, 28.2, FC0, FC1, FCl, FCl, 0),               # in the small box, turns: "Meow!"
 (28.2, 28.7, FC1, ID0, FCl, IDl, 1),
 (28.7, 30.9, ID0, ID1, IDl, IDl, 0),               # Day 8: your idea?
 (30.9, 31.6, ID1, HK0, IDl, HKl, 1),               # back to the hook (= frame 0)
 (31.6, D + 1.05, HK0, HK1, HKl, HKl, 0),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
cm = dict(list=[dict(by='wil.son', name='wil.son', text='A giant box for all the cats', likes=None)], win=0, t=dict(up=2.95, scroll=3.1, stop=4.1, down=6.9))
PARTS = [9.85, 10.7, 11.55, 12.4, 13.25, 14.1]                          # giant box, flaps, cat doors, peek holes, scratch ramp, party flags
nb = dict(kind='box', sign='Giant Cat Box', name='Giant Cat Box', by='wil.son', byName='wil.son', at=7.0, slow=8.35, partsAt=PARTS, openAt=16.0)
e1 = dict(day=7, followersBefore=321, followersNew=0,
          landmarks=[dict(kind='fishmarket', sign='Fish Supermarket'), dict(kind='arcade', sign='Cat Arcade'), dict(kind='artstudio', sign='Art Studio'), dict(kind='pizza', sign='Giant Pizza'), dict(kind='toy', sign='Cat Toy Statue')],
          newBuild=nb, lotSign='For wil.son', lotUntil=10.3, idea=dict(spot=6, sign='Day 8: your idea?'), comments=cm, noReserved=True, shots=shots, duration=D + 1.1,
          starts=[0, 0, 0, 99], milestone=1e9, countFrom=0, box=dict(lookAt=[7.1, 9.5], boxAt=19.0, turnAt=27.3), confettiAt=[20.6])
json.dump(e1, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('ok', D)
