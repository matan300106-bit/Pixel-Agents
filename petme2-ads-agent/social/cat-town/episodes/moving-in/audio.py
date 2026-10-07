# Music (code-synth music-box waltz, Disney-style) + SFX + voice mix for "Are you moving in?" -> DIR/mix.wav
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
SR = 48000; DUR = 22.0; N = int(SR * DUR); rng = np.random.default_rng(7)
mus = np.zeros(N); sfx = np.zeros(N); voc = np.zeros(N)
def env(n, a=.005, r=.3): x = np.arange(n) / SR; return np.minimum(1, x / a) * np.exp(-x / r)
def add(buf, s, sig, g=1):
    i = int(s * SR); j = min(N, i + len(sig))
    if 0 <= i < N: buf[i:j] += g * sig[:j - i]
mid = lambda n: 440 * 2 ** ((n - 69) / 12)
X = lambda d: np.arange(int(d * SR)) / SR
def tone(f, d, r=.4, a=.005, harm=(1, .5, .25)): x = X(d); return sum(h * np.sin(2 * np.pi * f * (k + 1) * x) for k, h in enumerate(harm)) * env(len(x), a, r)
def bell(f, d=1.2, r=.5):   # music box tine: inharmonic partials, quick decay
    x = X(d); return (np.sin(2 * np.pi * f * x) + .35 * np.sin(2 * np.pi * f * 2.76 * x) * np.exp(-x * 6) + .15 * np.sin(2 * np.pi * f * 5.4 * x) * np.exp(-x * 12)) * env(len(x), .001, r)
def pluck(f, d=.5, r=.18): x = X(d); return (np.sin(2 * np.pi * f * x) + .4 * np.sin(4 * np.pi * f * x)) * env(len(x), .003, r)
def pad(f, d, a=.4, rel=.5): x = X(d); return (np.sin(2 * np.pi * f * x) + .3 * np.sin(2 * np.pi * f * 1.003 * 2 * x)) * np.minimum(1, x / a) * np.minimum(1, (d - x) / rel)
def noise(d, lp=.1):
    n = rng.standard_normal(int(d * SR)); y = np.zeros_like(n)
    for i in range(1, len(n)): y[i] = y[i - 1] + lp * (n[i] - y[i - 1])
    return y
def sweep(f0, f1, d, g=1, a=.002, r=.1): x = X(d); f = f0 + (f1 - f0) * x / d; return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(x), a, r) * g
def whoosh(s, d=.7, lp=.08, g=1.2): w = noise(d, lp); x = X(len(w) / SR); add(sfx, s, w * np.sin(np.pi * x / d) ** 2, g)
def shimmer(s, d=.9, up=True, g=.22, n=14):   # magic sparkle glissando
    for k in range(n): f = mid(84 + (k if up else n - k) * 1.2 + 6 * rng.random()); add(sfx, s + d * k / n, bell(f, .5, .18), g * (.6 + .4 * rng.random()))
def ding(s, n=88, g=.5): add(sfx, s, bell(mid(n), 1.4, .6), g); add(sfx, s + .02, bell(mid(n + 7), 1.0, .4), g * .5)
def pop(s, f=600, g=1.0): add(sfx, s, sweep(f, f * 2.4, .14, 1, .002, .05), g)
def meow(s, f0=760, d=.42, g=.2):
    x = X(d); f = f0 + 380 * np.sin(np.pi * x / d) - 200 * x / d
    add(sfx, s, np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * x / d) ** 1.5 * (1 + .3 * np.sin(2 * np.pi * 2 * f * x)), g)
def chirp(s, g=.12):   # little bird
    for k in range(3): f0 = 2600 + 600 * rng.random(); add(sfx, s + k * .09, sweep(f0, f0 + 1400, .07, 1, .003, .03), g)
# ---- music: waltz in C, 138 bpm (oom-pah-pah), music-box melody on top
bt = 60 / 138; bar = 3 * bt
prog = [[48, 60, 64, 67], [45, 57, 60, 64], [41, 57, 60, 65], [43, 55, 59, 62]]   # C Am F G (bass, chord)
mel = [[76, 79, 84], [81, 79, 76], [77, 81, 84], [83, 79, 74]]
mel2 = [[84, 83, 81], [79, 81, 76], [77, 76, 74], [79, 83, 86]]
t = 0.0; b = 0
while t < DUR - .05:
    ch = prog[b % 4]; soft = 19.4 <= t; big = 17.2 <= t < 19.4
    add(mus, t, pluck(mid(ch[0]), .7, .3), .30 if not soft else .16)
    for k in (1, 2):
        for n in ch[1:]: add(mus, t + k * bt, pluck(mid(n), .3, .1), .07 if not soft else .04)
    m = (mel2 if (b // 4) % 2 else mel)[b % 4]
    for k, n in enumerate(m): add(mus, t + k * bt, bell(mid(n), 1.0, .45), .20)
    if big:
        for n in ch[1:]: add(mus, t, pad(mid(n), bar + .05, .15, .2), .07)
        add(mus, t, pad(mid(ch[0] - 12), bar, .1, .2), .12)
    t += bar; b += 1
for n in [60, 64, 67, 72, 76]: add(mus, 18.9, pad(mid(n), 1.6, .1, .8), .07)          # swell at 1,000
for n in [72, 76, 79, 84]: add(mus, 21.75, bell(mid(n), .8, .4), .15)                  # final sparkle chord into the loop
# ---- sfx
shimmer(0.0, .7); pop(0.5, 650, 1.0); ding(0.55, 88, .5); meow(0.75, 820, .35, .12)    # house pops
whoosh(2.2, 1.6, .05, 1.0); [chirp(s) for s in (2.6, 3.3, 4.0, 5.1, 6.4)]
add(sfx, 6.95, sweep(180, 520, .25, 1, .003, .3) * (1 + .5 * np.sin(2 * np.pi * 18 * X(.25))), .5)   # boing: grass
add(sfx, 8.3, np.concatenate([sweep(420, 380, .12, 1, .01, .3), sweep(380, 620, .18, 1, .01, .3)]), .22)   # "hmm?"
add(sfx, 9.5, tone(mid(36), 1.2, .5, .005, (1, .4)), .55); shimmer(9.5, .5, True, .26); ding(9.52, 91, .55)   # "You!"
shimmer(10.9, .8, True, .2); pop(11.75, 700, 1.0); ding(11.8, 86, .45); meow(12.0, 900, .3, .12)          # wand + house
pop(14.3, 800, .6)                                                                    # comment chip
add(sfx, 16.15, noise(.35, .5) * env(int(.35 * SR), .005, .08), .5); shimmer(16.1, .4, True, .24)   # poof
add(sfx, 16.3, noise(.6, .25) * env(int(.6 * SR), .01, .2) * .6, .5); ding(16.35, 84, .4)           # splash + ding
whoosh(17.2, 1.8, .06, 1.0)
for k in range(40): s = 17.35 + 1.5 * (k / 40) ** .8; f = 500 + 900 * rng.random(); add(sfx, s, sweep(f, f * 2, .07, 1, .002, .04), .3)
for s in (17.9, 18.25, 18.6, 18.95, 19.2):   # fireworks: thump + sparkle crackle
    add(sfx, s, tone(mid(40), .5, .2, .004, (1, .3)), .4)
    for k in range(14): add(sfx, s + .05 + k * .04 + .02 * rng.random(), noise(.03, .8) * env(int(.03 * SR), .001, .01), .2)
for k, n in enumerate([72, 76, 79, 84]): add(sfx, 18.92 + k * .07, tone(mid(n), .9, .35, .002, (1, .3)), .2)   # fanfare: 1,000!
add(sfx, 20.3, sweep(500, 900, .12, 1, .003, .08), .3)                                # wave "boop"
meow(21.05, 780, .45, .22)                                                            # "Meow!"
shimmer(21.5, .45, True, .24, 12)                                                     # sparkle wipe -> loop
# ---- voice
for l in json.load(open(f'{DIR}/timeline.json')):
    a, _ = sf.read(f"{DIR}/l{l['i']:02d}.wav"); add(voc, l['s'], a)
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .7 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc + .6 * mus * duck + .8 * sfx; mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.01 * SR)] = np.linspace(0, 1, int(.01 * SR)); fade[-int(.04 * SR):] = np.linspace(1, 0, int(.04 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-12.5:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
