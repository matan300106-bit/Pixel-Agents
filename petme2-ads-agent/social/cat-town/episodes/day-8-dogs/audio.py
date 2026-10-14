# Day 8 sound (all code synth, free): war drums for the dog march, a peaceful pluck tune that cuts out, rumble, Mango's battle cry (echo),
# heroic drums while the cats get ready, wind for the face-off, heavy steps, a heartbeat, the freeze "dun dun DUN" + voice mix -> DIR/mix.wav
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
SR = 48000; DUR = 40.0; N = int(SR * DUR); rng = np.random.default_rng(8)
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
    n = rng.standard_normal(int(d * SR)); y = np.zeros_like(n)
    for i in range(1, len(n)): y[i] = y[i - 1] + lp * (n[i] - y[i - 1])
    return y
def pop(f0=500, f1=1400, d=.12): x = np.arange(int(d * SR)) / SR; f = f0 + (f1 - f0) * x / d; return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(x), .002, .05)
def drum(f0=90, d=.9, g=1):    # taiko: pitch drop + thump noise
    x = np.arange(int(d * SR)) / SR; f = f0 * (1 + 1.2 * np.exp(-x * 30)); s = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(x), .002, .28)
    return (s + .5 * noise(d, .25)[:len(x)] * env(len(x), .001, .03)) * g
def snare(d=.18): return noise(d, .7) * env(int(d * SR), .001, .05)
def brass(notes, d=1.2, a=.06, r=.6): return sum(tone(mid(n), d, r, a, SAW) for n in notes)
def whoosh(s, d=.7, lp=.08, g=1.0): w = noise(d, lp); x = np.arange(len(w)) / SR; add(sfx, s, w * np.sin(np.pi * x / d) ** 2, g)
TL = {l['i']: l for l in json.load(open(f'{DIR}/timeline.json'))}
E = json.load(open(f'{DIR}/e1.json'))['war']
# 0-1.6 hook: drums + brass hit
for k, t in enumerate([0.0, .4, .8, 1.0, 1.2, 1.4]): add(mus, t, drum(70 if k % 3 == 0 else 95), .9 if k % 3 == 0 else .6)
add(mus, 0.0, brass([38, 45, 50]), .16)
# 1.6-5.0 peaceful plucks (Day 7 tune), fades into the cut
prog = [[60, 64, 67, 72], [57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67]]; b = 0
while True:
    t = 1.65 + b * .25
    if t > 4.95: break
    ch = prog[(b // 4) % 4]; add(mus, t, tone(mid(ch[b % 4] + 12), .8, .3, .003), .12)
    if b % 4 == 0: add(mus, t, tone(mid(ch[0] - 12), 1.4, .6, .02, (1, .3)), .16)
    b += 1
# 5.0 the cut: deep boom + rumble while the ground shakes
add(sfx, 5.0, tone(38, 2.5, 1.2, .004, (1, .5)), 1.0); r = noise(2.6, .02); add(sfx, 5.0, r * np.minimum(1, np.arange(len(r)) / SR / .2) * np.minimum(1, (2.6 - np.arange(len(r)) / SR) / .5), 3.5)
# 7.4-13.6 the dog march: drums on every step (100 bpm), drone, brass stabs; snare from 10.8
def drone(t0, t1, notes, g):
    d = t1 - t0; x = np.arange(int(d * SR)) / SR; s = sum(sum(np.sin(2 * np.pi * mid(n) * (k + 1) * x) / (k + 1) for k in range(5)) for n in notes)
    add(mus, t0, s * np.minimum(1, x / 1.0) * np.minimum(1, (d - x) / .4), g)
drone(7.4, 13.6, [38, 45, 50], .05); drone(13.6, 16.3, [38, 45], .035)
BT = .6; t = 7.4; k = 0
while t < 13.55:
    add(mus, t, drum(62 if k % 4 == 0 else 85), .95 if k % 4 == 0 else .55)
    if t >= 10.8: add(mus, t + BT / 2, snare(), .22)
    if k % 8 == 0: add(mus, t, brass([38, 45, 50, 53]), .1)
    t += BT; k += 1
for t in np.arange(13.7, 16.2, .8): add(mus, t, drum(55, .9), .5)       # Mango shot: slow, low
# 16.35 MEOW: big hit; 17.0-25.2 the cats get ready: heroic, faster drums, major brass
add(mus, 16.35, drum(60, 1.2), 1.0); add(mus, 16.35, brass([50, 57, 62, 66], 1.6, .03, .8), .14)
drone(17.0, 25.2, [50, 57, 62], .035)
t = 17.0; k = 0
while t < 25.1:
    add(mus, t, drum(70 if k % 2 == 0 else 100), .8 if k % 4 == 0 else .45); add(mus, t + .2, snare(.1), .12)
    if k % 8 == 0: add(mus, t, brass([50, 54, 57, 62] if (k // 8) % 2 == 0 else [48, 52, 55, 60]), .09)
    t += .4; k += 1
whoosh(17.0, .7, .08, 1.0); whoosh(20.2, .7, .08, .8)
# cat feet running in (lots of tiny pops)
for j in range(70): add(sfx, E['gatherAt'] + .1 + rng.random() * 2.6, pop(900 + rng.random() * 500, 1300 + rng.random() * 500, .03), .1)
# prep: box wall thuds, cannon creak, helmet clinks, flags flap
for j in range(9): add(sfx, E['wallAt'] + .3 + j * .07, tone(55 + j * 3, .4, .14, .002, (1, .5)), .5); add(sfx, E['wallAt'] + .3 + j * .07, noise(.08, .3) * env(int(.08 * SR), .001, .03), .4)
for j in range(2): add(sfx, E['cannonAt'] + .35 + j * .2, pop(180, 120, .25), .5); add(sfx, E['cannonAt'] + .4 + j * .2, tone(mid(76), .5, .2, .002, (1, .3)), .12)
for j in range(14): f = 1800 + rng.random() * 1400; add(sfx, E['helmetAt'] + .25 + j * .09, tone(f, .25, .08, .001, (1, 0, .4, 0, .25)), .07)   # metallic clinks
for j in range(4): whoosh(E['flagAt'] + .1 + j * .12, .35, .3, .5)
for k2, n in enumerate([62, 66, 69, 74]): add(sfx, 24.95 + k2 * .08, tone(mid(n), .9, .35, .002, (1, .3)), .2)   # READY! fanfare
# 25.2-29.3 face-off: wind + low drone, one drum per cut
w = noise(8.2, .05); xw = np.arange(len(w)) / SR; add(sfx, 25.2, w * (.6 + .4 * np.sin(xw * 1.3)) * np.minimum(1, xw / .5) * np.minimum(1, (8.2 - xw) / .4), 1.6)
drone(25.2, 32.5, [38, 45], .04); add(mus, 25.2, drum(55, 1.2), .8); add(mus, 27.45, drum(55, 1.2), .8)
# 29.3-32.5 the general's heavy steps, Mango's little steps
for j in range(4): add(sfx, E['stepAt'] + .35 + j * .63, tone(42, .6, .22, .002, (1, .6)), .9); add(sfx, E['stepAt'] + .35 + j * .63, noise(.12, .15) * env(int(.12 * SR), .001, .05), .8)
for j in range(8): add(sfx, E['mangoAt'] + .1 + j * .24, pop(700, 520, .04), .2)
# 32.5-34.0 silence + heartbeat + a thin rising tone; the jaw opens
for t in [32.6, 33.3]: add(sfx, t, tone(48, .25, .09, .003, (1, .4)), .9); add(sfx, t + .16, tone(44, .25, .08, .003, (1, .4)), .7)
x = np.arange(int(1.45 * SR)) / SR; add(mus, 32.55, np.sin(2 * np.pi * np.cumsum(500 + 400 * x / 1.45) / SR) * np.minimum(1, x / .8) * .5, .05)
add(sfx, E['jawAt'], noise(.4, .05) * env(int(.4 * SR), .05, .2), .5)   # a low breath in
# 34.0 FREEZE: hit + "dun dun DUNNN", then a soft drum bed under the end card
F = 34.0; add(sfx, F, drum(50, 1.5), 1.0); add(sfx, F, noise(.5, .5) * env(int(.5 * SR), .001, .15), .5)
for k2, (n, d) in enumerate([(50, .35), (49, .35), (46, 1.6)]): add(mus, F + .45 + k2 * .42, brass([n - 12, n, n + 7], d + .5, .02, .5 if k2 < 2 else 1.2), .16)
t = 36.0; k = 0
while t < 39.6: add(mus, t, drum(70 if k % 4 == 0 else 95, .7), .4 if k % 4 == 0 else .25); t += .6; k += 1
add(mus, 39.4, drum(55, .6), .8)
# voice (Mango's battle cry gets an echo)
for i, l in TL.items():
    a, _ = sf.read(f"{DIR}/l{i:02d}.wav")
    if i == 5: a = np.concatenate([a, np.zeros(int(.9 * SR))]); e = a.copy(); [add(voc, l['s'] + d, e * g) for d, g in ((.17, .45), (.34, .25), (.51, .12))]
    add(voc, l['s'], a)
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .6 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc * 1.1 + .6 * mus * duck + .75 * sfx * (.6 + .4 * duck); mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.01 * SR)] = np.linspace(0, 1, int(.01 * SR)); fade[-int(.3 * SR):] = np.linspace(1, 0, int(.3 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-12.5:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
