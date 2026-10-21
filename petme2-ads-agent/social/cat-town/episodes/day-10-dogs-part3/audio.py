# Day 10 sound (all code synth, free): the Day 9 freeze sting, the giant's breath + growl, a fast chase (drums + brass) with barking dogs, a slow-motion jump,
# panic meows, a magic chime for Mango's idea, a heroic build while the cats climb (pops as they land), the MEGA MANGO hit, the last 10 clock ticks, a sunrise swell,
# the giant's BOOM steps, the MEOW hit, the freeze "dun dun DUNNN" + voice mix -> DIR/mix.wav
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
SR = 48000; DUR = 51.6; N = int(SR * DUR); rng = np.random.default_rng(10)
mus = np.zeros(N); sfx = np.zeros(N); voc = np.zeros(N)
def env(n, a=.005, r=.3): x = np.arange(n) / SR; return np.minimum(1, x / a) * np.exp(-x / r)
def add(buf, s, sig, g=1):
    i = int(s * SR); j = min(N, i + len(sig))
    if 0 <= i < N and j > i: buf[i:j] += g * sig[:j - i]
def tone(f, d, r=.4, a=.005, harm=(1, .5, .25)):
    x = np.arange(int(d * SR)) / SR; return sum(h * np.sin(2 * np.pi * f * (k + 1) * x) for k, h in enumerate(harm)) * env(len(x), a, r)
SAW = tuple(1 / k for k in range(1, 9))
mid = lambda n: 440 * 2 ** ((n - 69) / 12)
def noise(d, lp=.1):
    n = rng.standard_normal(int(d * SR)); y = np.zeros_like(n); a = 0.0
    for i in range(len(n)): a += lp * (n[i] - a); y[i] = a
    return y
def pop(f0=500, f1=1400, d=.12): x = np.arange(int(d * SR)) / SR; f = f0 + (f1 - f0) * x / d; return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(x), .002, .05)
def drum(f0=90, d=.9, g=1):
    x = np.arange(int(d * SR)) / SR; f = f0 * (1 + 1.2 * np.exp(-x * 30)); s = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(x), .002, .28)
    return (s + .5 * noise(d, .25)[:len(x)] * env(len(x), .001, .03)) * g
def brass(notes, d=1.2, a=.06, r=.6): return sum(tone(mid(n), d, r, a, SAW) for n in notes)
def whoosh(s, d=.7, lp=.08, g=1.0): w = noise(d, lp); x = np.arange(len(w)) / SR; add(sfx, s, w * np.sin(np.pi * x / d) ** 2, g)
def drone(t0, t1, notes, g, buf=None):
    d = t1 - t0; x = np.arange(int(d * SR)) / SR; s = sum(sum(np.sin(2 * np.pi * mid(n) * (k + 1) * x) / (k + 1) for k in range(5)) for n in notes)
    add(mus if buf is None else buf, t0, s * np.minimum(1, x / 1.0) * np.minimum(1, (d - x) / .4), g)
def beat(t, g=.9): add(sfx, t, tone(48, .25, .09, .003, (1, .4)), g); add(sfx, t + .16, tone(44, .25, .08, .003, (1, .4)), g * .75)
TL = {l['i']: l for l in json.load(open(f'{DIR}/timeline.json'))}
W = json.load(open(f'{DIR}/e1.json'))['war']; BOOMS = json.load(open(f'{DIR}/fx.json'))['booms']
def bark(t, g=1.0, f0=None):
    f0 = f0 or 380 + rng.random() * 260; d = .16; x = np.arange(int(d * SR)) / SR; f = f0 * (1.25 - .5 * x / d)
    s = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * .35 + np.sin(2 * np.pi * np.cumsum(f) / SR); add(sfx, t, (s + .4 * noise(d, .5)[:len(x)]) * env(len(x), .004, .05), g)
def meow(t, g=1.0, f0=None):
    f0 = f0 or 550 + rng.random() * 350; d = .35 + rng.random() * .2; x = np.arange(int(d * SR)) / SR; u = x / d; f = f0 * (1 + .5 * np.sin(np.pi * u ** .8)) * (1 + .02 * np.sin(2 * np.pi * 7 * x))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) + .3 * np.sin(4 * np.pi * np.cumsum(f) / SR); add(sfx, t, s * np.minimum(1, x / .03) * np.minimum(1, (d - x) / .1), g)
# 0-1.4 Day 9's freeze: low hit, the PART 3 stamp slam, a reverse swell into colour
add(sfx, 0.0, drum(50, 1.2), .6); add(sfx, .35, drum(45, 1.0), 1.0); add(sfx, .35, noise(.3, .6) * env(int(.3 * SR), .001, .08), .6)
rv = noise(.8, .2) * np.linspace(0, 1, int(.8 * SR)) ** 2; add(sfx, .4, rv, .9); add(mus, 1.2, brass([26, 33, 38, 39], 1.4, .01, .7), .14); add(sfx, 1.2, drum(40, 1.6), .9)
# 1.4-4.5 the giant looks down: breath, a growl, heartbeat speeds up, crickets
drone(1.4, 4.6, [26, 33, 39], .05); br = noise(2.0, .02); xb = np.arange(len(br)) / SR; add(sfx, 1.6, br * np.sin(np.pi * xb / 2.0) ** 2, 5.0)
x = np.arange(int(1.8 * SR)) / SR; gr = np.sin(2 * np.pi * (55 + 8 * np.sin(2 * np.pi * 9 * x)) * x) * (1 + .5 * noise(1.8, .05)[:len(x)] * 8) * np.minimum(1, x / .3) * np.minimum(1, (1.8 - x) / .4); add(sfx, 2.6, gr, .5)
for t in [1.7, 2.5, 3.1, 3.6, 4.0, 4.3]: beat(t, .9)
t = 1.5
while t < 4.4:
    for q in range(3): add(sfx, t + q * .045, tone(4300 + rng.random() * 300, .03, .012, .001, (1,)), .03)
    t += .38 + rng.random() * .5
# 4.5-13.7 RUN: the chase (fast drums + a brass ostinato), the dogs bark, the jump in slow motion
add(mus, 4.5, drum(55, 1.2), 1.0); add(mus, 4.5, brass([38, 45, 50], .8, .01, .4), .16); whoosh(4.45, .5, .2, 1.0)
CH = [38, 38, 41, 38, 43, 38, 41, 36]; t = 4.75; k = 0
while t < 11.7:
    add(mus, t, tone(mid(CH[k % 8] + 12), .16, .07, .002, SAW), .07); add(mus, t, drum(70 if k % 2 == 0 else 110, .3), .35 if k % 4 == 0 else .15)
    if k % 8 == 4: add(mus, t, noise(.1, .7) * env(int(.1 * SR), .001, .04), .25)
    t += .15; k += 1
for t in np.arange(4.8, 11.6, .25): add(sfx, t, noise(.05, .3) * env(int(.05 * SR), .001, .02), .3)   # little running steps
for j in range(60): bark(W['bark'][0] + rng.random() * (W['bark'][1] - W['bark'][0] - .3), .05 + rng.random() * .07)
J0, J1, _ = W['spyJump']; whoosh(J0, 1.2, .05, 1.6); x = np.arange(int(1.4 * SR)) / SR; add(mus, J0, sum(np.sin(2 * np.pi * mid(n) * x) for n in [62, 66, 69, 74]) * np.minimum(1, x / .5) * np.exp(-x / 1.2), .05)
add(sfx, J1, drum(70, .5), .8); add(sfx, J1, noise(.2, .3) * env(int(.2 * SR), .001, .06), .4)
# 13.7-16.8 "They have a GIANT": a tense drone, one hit on GIANT
drone(13.7, 16.8, [33, 39, 45], .045); add(mus, TL[7]['e'] - .35, drum(42, 1.4), .9); add(mus, TL[7]['e'] - .35, brass([27, 34, 39], 1.4, .01, .7), .15)
# 16.8-19.6 PANIC: meows everywhere, a fast pizz
P0, P1 = W['panic']
for j in range(34): meow(P0 + rng.random() * (P1 - P0 - .5), .03 + rng.random() * .05)
t = P0; k = 0
while t < P1 - .2: add(mus, t, tone(mid([64, 67, 70, 73][k % 4] + (k // 4 % 2) * 2), .14, .05, .002, (1, .4)), .12); t += .11; k += 1
# 19.6-23.6 Mango's idea: a magic chime, then a hero hit on "OWN GIANT"
for j, n in enumerate([72, 76, 79, 84, 88]): add(mus, 19.7 + j * .07, tone(mid(n), 1.2, .6, .002, (1, .2)), .05)
drone(19.6, 23.6, [45, 52], .03); add(mus, 22.6, drum(55, 1.4), .9); add(mus, 22.6, brass([45, 52, 57, 61], 1.4, .02, .8), .14)
# 23.6-31 the cats climb: a heroic build (rising chords), pops as cats land, the clock ticks from 0:00:10
M = W['mega']; prog = [[45, 52, 57, 61], [47, 54, 59, 62], [49, 56, 61, 64], [50, 57, 62, 66], [52, 59, 64, 68]]; t = M['at']; k = 0
while t < M['fullAt'] - .1:
    ch = prog[min(4, int((t - M['at']) / (M['fullAt'] - M['at']) * 5))]; add(mus, t, tone(mid(ch[k % 4] + 12), .22, .1, .002, SAW), .05); add(mus, t, drum(80, .3), .18 if k % 2 == 0 else .08)
    if k % 4 == 0: add(mus, t, brass(ch[:3], .7, .05, .4), .05)
    t += .2; k += 1
for j in range(110): add(sfx, M['at'] + .85 + rng.random() * M['dur'], pop(600 + rng.random() * 900, 1500 + rng.random() * 600, .07), .07)
for j in range(10): meow(M['at'] + .5 + rng.random() * M['dur'], .03)
F2 = M['fullAt']; add(mus, F2, drum(45, 2.0), 1.0); add(mus, F2, brass([38, 45, 50, 54, 57], 2.2, .01, 1.4), .2); add(sfx, F2, noise(.8, .3) * env(int(.8 * SR), .001, .3), .4)
CK = json.load(open(f'{DIR}/text.json'))['clock']; t0 = [a for a, v in CK if v == 10][0]; t1 = CK[-1][0]
for j in range(11): add(sfx, t0 + (t1 - t0) * j / 10, tone(1900, .06, .03, .001, (1, .3)), .1 if j < 10 else 0); 
for t in np.arange(31.6, t1, .5): beat(t, .7)
# 34.4 sunrise: a warm swell + bell, birds
SU = t1; x = np.arange(int(3.2 * SR)) / SR; add(mus, SU, sum(np.sin(2 * np.pi * mid(n) * x) / (1 + k2) for k2, n in enumerate([45, 52, 57, 61, 64])) * np.minimum(1, x / 1.0) * np.minimum(1, (3.2 - x) / .8), .06)
add(mus, SU, tone(mid(81), 3.0, 1.4, .002, (1, 0, .5, 0, .3)), .08)
for j in range(8): add(sfx, SU + .8 + j * .25 + rng.random() * .1, tone(3000 + rng.random() * 800, .07, .04, .002, (1,)), .03)
# 37-41.4 BOOM BOOM: the giant walks, low rumble, dogs bark again
drone(37.0, 41.6, [26, 33], .05)
for b in BOOMS: add(sfx, b, drum(34, 2.2), 1.3); add(sfx, b, noise(1.0, .06) * env(int(1.0 * SR), .002, .4), 1.6); add(mus, b, brass([22, 29], 1.0, .01, .6), .14)
for j in range(16): bark(37.2 + rng.random() * 3.8, .04)
# 41.4-45.4 Mega Mango stands up (rising brass), the MEOW hit
x = np.arange(int(2.0 * SR)) / SR; f = mid(45) * 2 ** (x / 2.0); add(mus, 41.4, np.sin(2 * np.pi * np.cumsum(f) / SR) * np.minimum(1, x / .3), .07); whoosh(41.6, 1.2, .04, 1.4)
R0_ = M['roar'][0]; add(sfx, R0_, drum(40, 1.8), 1.0); add(mus, R0_, brass([33, 40, 45, 49, 52], 1.8, .01, 1.0), .2)
# 45.4 FREEZE: hit + "dun dun DUNNN", then a soft drum bed under the end card
F = 45.4; add(sfx, F, drum(50, 1.5), 1.0); add(sfx, F, noise(.5, .5) * env(int(.5 * SR), .001, .15), .5)
for k2, (n, d) in enumerate([(50, .35), (49, .35), (46, 1.6)]): add(mus, F + .45 + k2 * .42, brass([n - 12, n, n + 7], d + .5, .02, .5 if k2 < 2 else 1.2), .16)
t = 47.4; k = 0
while t < 51.2: add(mus, t, drum(70 if k % 4 == 0 else 95, .7), .4 if k % 4 == 0 else .25); t += .6; k += 1
add(mus, 51.0, drum(55, .6), .8)
# voice: the spy is breathless (a bit quieter), Mega Mango's MEOW is huge
for i, l in TL.items():
    a, _ = sf.read(f"{DIR}/l{i:02d}.wav")
    add(voc, l['s'], a * (1.25 if i == 16 else .9 if i in (2, 7) else 1))
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .6 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc * 1.1 + .6 * mus * duck + .75 * sfx * (.6 + .4 * duck); mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.01 * SR)] = np.linspace(0, 1, int(.01 * SR)); fade[-int(.3 * SR):] = np.linspace(1, 0, int(.3 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-12.5:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
