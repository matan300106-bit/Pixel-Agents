# Day 4 (Matan approved the script Oct 10): 261 followers = houses, 479 likes = cats -> 218 cats with no home (crowd under "No home yet").
# Hook on the homeless crowd -> houses roll up -> cats roll up -> 479 - 261 = 218 -> one stray waits alone -> Tilly's comment
# -> the Art Studio builds, the homeless cats come in and paint -> a gold Mango statue rises -> a house pops, the lone stray runs in (218 -> 217) -> CTA -> loop.
# Writes DIR/e1.json.
import json, sys, math
out = sys.argv[1] if len(sys.argv) > 1 else 'v'
D = 33.8                        # video length; frames 0-1 s replay engine time D..D+1, so the loop is seamless
HOUSES, LIKES = 261, 479        # Matan, Oct 10
NOHOME = LIKES - HOUSES         # 218 (Matan's number): 217 in the crowd/roofs/streets + the lone stray
ST, LN, CR = (44.6, -25.8, -1.05), (47.2, 27.2, -2.09), (-47.1, 27.3, 2.1)   # SPOTS[2] art studio, SPOTS[4] the lone stray's lot, SPOTS[3] the homeless crowd
def W(spot, lx, y, lz):         # spot local (x right, z toward Mango) -> world
    x0, z0, ry = spot; X = (math.cos(ry), -math.sin(ry)); Z = (math.sin(ry), math.cos(ry))
    return [round(x0 + lx * X[0] + lz * Z[0], 2), y, round(z0 + lx * X[1] + lz * Z[1], 2)]
CRa, CRb, CRc, CRl = W(CR, -8, 27, 31), W(CR, -6, 24, 27), W(CR, -3, 20, 22), W(CR, 0, 0, -13)
CRw0, CRw1 = W(CR, -10, 32, 40), W(CR, -5, 23, 27)
TOP0, TOP1, TOPl = [60, 150, 130], [25, 125, 150], [0, 0, 10]
ROOF0, ROOF1, ROOFl = [-10, 55, 85], [-28, 40, 62], [-45, 0, 20]
LN0, LN1, LNl = W(LN, 3, 6, 18), W(LN, 2, 4.5, 13.5), W(LN, 0, 1.6, 5)
CM0, CM1, CMl = W(ST, -34, 32, 60), W(ST, -30, 28, 54), W(ST, 0, 8, 0)
BLD0, BLD1, BLDl = W(ST, -38, 34, 64), W(ST, -26, 26, 52), W(ST, 0, 11, -2)
SA0, SA1, SAl = W(ST, -18, 24, 44), W(ST, -13, 20, 38), W(ST, 0, 6, 2)
HS0, HS1, HSl = W(LN, 7, 13, 31), W(LN, 5, 11, 27), W(LN, 0, 9, 0)
S = [
 (1.0, 3.9, CRb, CRc, CRl, CRl, 0),                 # hook: the homeless crowd (continues the D..D+1 shot)
 (3.9, 4.7, CRc, TOP0, CRl, TOPl, 1),               # up over the whole town
 (4.7, 8.0, TOP0, TOP1, TOPl, TOPl, 0),             # 261 houses
 (8.0, 9.0, TOP1, ROOF0, TOPl, ROOFl, 1),           # down over the roofs: cats everywhere
 (9.0, 12.0, ROOF0, ROOF1, ROOFl, ROOFl, 0),        # 479 cats
 (12.0, 13.0, ROOF1, CRw0, ROOFl, CRl, 1),          # the crowd
 (13.0, 17.2, CRw0, CRw1, CRl, CRl, 0),             # 479 - 261 = 218
 (17.2, 17.95, CRw1, LN0, CRl, LNl, 1),             # one stray alone on an empty lot
 (17.95, 18.75, LN0, LN1, LNl, LNl, 0),
 (18.75, 20.0, LN1, CM0, LNl, CMl, 1),              # Tilly's comment, over to the studio lot
 (20.0, 22.35, CM0, CM1, CMl, CMl, 0),
 (22.35, 25.4, BLD0, BLD1, BLDl, BLDl, 0),          # slow build, painter cats run in
 (25.4, 26.2, BLD1, SA0, BLDl, SAl, 1),             # the statue rises, Mango looks up
 (26.2, 28.7, SA0, SA1, SAl, SAl, 0),
 (28.7, 29.5, SA1, HS0, SAl, HSl, 1),               # the lone stray's lot: a house pops, the cat runs in
 (29.5, 31.9, HS0, HS1, HSl, HSl, 0),
 (31.9, 32.8, HS1, CRa, HSl, CRl, 1),               # back to the crowd (= frame 0)
 (32.8, D + 1.05, CRa, CRb, CRl, CRl, 0),
]
shots = [dict(t0=a, t1=b, p0=p0, p1=p1, l0=l0, l1=l1, inout=bool(io)) for a, b, p0, p1, l0, l1, io in S]
cm = dict(list=[dict(by='Tilly', name='Tilly', text='you should build an art studio and the cats at the studio build mango a statue ♡', likes=None)], win=0, t=dict(up=18.8, scroll=18.95, stop=19.95, down=22.3))
nb = dict(kind='artstudio', sign='Art Studio', name='Art Studio', by='Tilly', byName='Tilly', at=22.35, slow=3.0, partsAt=[22.4, 22.85, 23.3, 23.75, 24.2], openAt=24.3)
e1 = dict(day=4, followersBefore=HOUSES, followersNew=0, landmarks=[dict(kind='fishmarket', sign='Fish Supermarket'), dict(kind='arcade', sign='Cat Arcade')],
          newBuild=nb, lotSign='For Tilly', comments=cm, noReserved=True, shots=shots, duration=D + 1.1, starts=[0, 0, 0, 99], milestone=1e9, countFrom=0,
          statueAt=25.7, lone=dict(spot=4, at=-1, houseAt=29.6, runAt=30.5, sign='Home at last!'),
          strays=dict(n=NOHOME - 1, at=[-1] * (NOHOME - 1), near=[0, 0], crowd=70, crowdSpot=3, sign='No home yet', signAt=-1))
json.dump(e1, open(f'{out}/e1.json', 'w'), ensure_ascii=False)
print('no home', NOHOME)
