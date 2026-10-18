# Day 9 sound (all code synth, free): the Day 8 freeze sting, a growly drone under the general, a sad pluck tune at the fountain, hits on NEVER and ATTACK,
# a wolf-pack howl, night (crickets, camp fire crackle, dog snores), a sneaky pizzicato for the spy, then silence, heartbeat, the giant's breath + a BRAAM when his eyes open,
# the freeze "dun dun DUNNN" + voice mix -> DIR/mix.wav
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
SR = 48000; DUR = 48.5; N = int(SR * DUR); rng = np.random.default_rng(9)
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
W = json.load(open(f'{DIR}/e1.json'))['war']
# 0-1.2 Day 8's freeze: low hit, the PART 2 stamp slam, a reverse swell into colour
add(sfx, 0.0, drum(50, 1.2), .6); add(sfx, .35, drum(45, 1.0), 1.0); add(sfx, .35, noise(.3, .6) * env(int(.3 * SR), .001, .08), .6)
rv = noise(.8, .2) * np.linspace(0, 1, int(.8 * SR)) ** 2; add(sfx, .4, rv, .9); add(sfx, 1.2, brass([38, 45, 50], 1.4, .01, .7), .14); add(sfx, 1.2, drum(55, 1.2), .9)
# 1.4-6.4 the general speaks: low drone + wind, a slow heartbeat
drone(1.4, 6.4, [38, 45], .045); w = noise(13.0, .04); xw = np.arange(len(w)) / SR; add(sfx, 1.4, w * (.6 + .4 * np.sin(xw * 1.1)) * np.minimum(1, xw / .5) * np.minimum(1, (13 - xw) / .5), 1.3)
for t in [2.0, 3.3, 4.6, 5.9]: beat(t, .6)
add(mus, 3.8, drum(48, 1.4), .6)
# 6.4-9.2 the fountain: soft plucks (minor) + water
prog = [[57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67], [52, 56, 59, 64]]; b = 0
while 6.45 + b * .28 < 9.1:
    t = 6.45 + b * .28; ch = prog[(b // 4) % 4]; add(mus, t, tone(mid(ch[b % 4] + 12), .8, .35, .003), .1)
    if b % 4 == 0: add(mus, t, tone(mid(ch[0] - 12), 1.4, .6, .02, (1, .3)), .14)
    b += 1
wt = noise(2.8, .5); add(sfx, 6.4, wt * np.minimum(1, np.arange(len(wt)) / SR / .3) * np.minimum(1, (2.8 - np.arange(len(wt)) / SR) / .3), .25)
for j in range(14): add(sfx, 6.5 + rng.random() * 2.5, pop(1400 + rng.random() * 800, 900, .05), .05)
# 9.2-10.8 NEVER!: a heroic hit
add(mus, 9.45, drum(60, 1.2), 1.0); add(mus, 9.45, brass([50, 57, 62, 66], 1.4, .02, .7), .15)
# 10.8-14.4 "at sunrise... we attack": drone, a timpani roll that grows, BOOM on "attack"
drone(10.8, 14.4, [38, 44, 50], .05)
t = 11.0; k = 0
while t < 13.3: add(mus, t, drum(58, .5), .12 + .5 * (t - 11) / 2.3); t += max(.06, .22 - .07 * (t - 11)); k += 1
add(mus, 13.3, drum(45, 1.6), 1.0); add(mus, 13.3, brass([26, 33, 38, 41], 1.6, .01, .9), .2); add(sfx, 13.3, noise(.6, .4) * env(int(.6 * SR), .001, .2), .5)
# 14.4-16.8 the howl: a pack of wolf voices (gliding sines with vibrato), echo
def howl(d, f0, f1, f2, vib=5.5):
    x = np.arange(int(d * SR)) / SR; u = x / d; f = np.where(u < .3, f0 + (f1 - f0) * (u / .3) ** .7, f1 + (f2 - f1) * (np.clip(u - .3, 0, 1) / .7) ** 1.5) * (1 + .012 * np.sin(2 * np.pi * vib * x))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) + .25 * np.sin(4 * np.pi * np.cumsum(f) / SR); return s * np.minimum(1, x / .15) * np.minimum(1, (d - x) / .5)
H = np.zeros(int(3.2 * SR))
for j in range(14):
    d = 1.6 + rng.random() * .6; f1 = 520 + rng.random() * 260; h = howl(d, f1 * .55, f1, f1 * .7); o = int((rng.random() * .35) * SR); H[o:o + len(h)] += h * (.35 + rng.random() * .3) * (1.6 if j == 0 else 1)
add(sfx, 14.5, H, .12); [add(sfx, 14.5 + dl, H, g) for dl, g in ((.28, .05), (.56, .025))]
drone(14.4, 16.8, [38, 45, 50, 53], .04)
# 16.8-20.5 night falls: low pad, a single bell
drone(16.8, 26.6, [33, 40, 45], .035); add(mus, 17.0, tone(mid(69), 3.5, 1.6, .002, (1, 0, .5, 0, .3, .2)), .09); add(mus, 18.6, tone(mid(68), 3.5, 1.6, .002, (1, 0, .5, 0, .3, .2)), .08)
# night bed (20 -> 41): crickets + an owl
t = 19.8
while t < 41.3:
    for q in range(3): add(sfx, t + q * .045, tone(4300 + rng.random() * 300, .03, .012, .001, (1,)), .03)
    t += .38 + rng.random() * .5
for t in [21.4, 22.1]: add(sfx, t, tone(380, .45, .25, .05, (1, .2)), .08)
# camp fire crackle in the camp shots
for a, b2, g in ((19.6, 23.0, .5), (36.0, 41.4, 1.0)):
    for j in range(int((b2 - a) * 9)): add(sfx, a + rng.random() * (b2 - a), noise(.02, .8) * env(int(.02 * SR), .001, .006), .25 * g)
# 23.0-26.6 eyes: a shimmer as they open
for j in range(18): add(sfx, W['eyesAt'] + .1 + j * .08, tone(mid(84 + (j * 5) % 12), .5, .3, .002, (1, .2)), .025)
# 26.6-39.2 the spy: sneaky pizzicato (E minor walking line) + soft snare brushes
SNEAK = [40, 47, 43, 47, 40, 47, 45, 43]; t = 27.0; k = 0
while t < 39.1:
    n = SNEAK[k % 8] + (12 if k % 16 >= 8 else 0); add(mus, t, tone(mid(n), .25, .09, .002, (1, .4, .15)), .3)
    if k % 2 == 1: add(mus, t, noise(.08, .6) * env(int(.08 * SR), .002, .03), .05)
    t += .3; k += 1
# 32.6-36 the dogs snore
for t in np.arange(32.8, 36.0, .9): sn = noise(.55, .03); xs = np.arange(len(sn)) / SR; add(sfx, t + rng.random() * .2, sn * np.sin(np.pi * xs / .55) ** 2 * (1 + .6 * np.sin(2 * np.pi * 28 * xs)), 1.4)
# 39.2-41.4 the music stops: only crickets, slow heartbeat, steps stop
for t in [39.5, 40.4, 41.2]: beat(t, .8)
# 41.4-43.3 the giant: deep breath, heartbeat speeds up, BRAAM when the eyes open (42.55)
br = noise(1.6, .02); xb = np.arange(len(br)) / SR; add(sfx, 41.4, br * np.sin(np.pi * xb / 1.6) ** 2, 5.0); add(sfx, 41.4, tone(31, 1.8, 1.0, .5, (1, .5)), .6)
for t in [41.7, 42.05]: beat(t, 1.0)
E2 = W['giant']['eyesAt']; add(sfx, E2, drum(38, 2.0), 1.0)
x = np.arange(int(1.6 * SR)) / SR; bm = sum(np.sign(np.sin(2 * np.pi * mid(n) * x)) * .5 + np.sin(2 * np.pi * mid(n) * x) for n in [26, 33, 38, 39])
add(mus, E2, bm * np.minimum(1, x / .05) * np.exp(-x / .9), .1)
# 43.3 FREEZE: hit + "dun dun DUNNN", then a soft drum bed under the end card
F = 43.3; add(sfx, F, drum(50, 1.5), 1.0); add(sfx, F, noise(.5, .5) * env(int(.5 * SR), .001, .15), .5)
for k2, (n, d) in enumerate([(50, .35), (49, .35), (46, 1.6)]): add(mus, F + .45 + k2 * .42, brass([n - 12, n, n + 7], d + .5, .02, .5 if k2 < 2 else 1.2), .16)
t = 45.3; k = 0
while t < 48.1: add(mus, t, drum(70 if k % 4 == 0 else 95, .7), .4 if k % 4 == 0 else .25); t += .6; k += 1
add(mus, 47.9, drum(55, .6), .8)
# voice: the general gets a short slap echo, Mango's "Go. Be careful." is a whisper (quieter)
for i, l in TL.items():
    a, _ = sf.read(f"{DIR}/l{i:02d}.wav")
    if i in (1, 2, 5): e = np.concatenate([a, np.zeros(int(.5 * SR))]); [add(voc, l['s'] + d, e * g) for d, g in ((.12, .22), (.24, .1))]
    add(voc, l['s'], a * (.7 if i == 9 else 1))
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .6 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc * 1.1 + .6 * mus * duck + .75 * sfx * (.6 + .4 * duck); mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.01 * SR)] = np.linspace(0, 1, int(.01 * SR)); fade[-int(.3 * SR):] = np.linspace(1, 0, int(.3 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-12.5:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
