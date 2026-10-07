# Self-made music + SFX + Kokoro voice for the "Be OK" video -> DIR/mix.wav. Happy ukulele-ish pluck + claps at 116 bpm (Mango's dance tempo),
# cut to silence when Mango freezes (EP.dance.stop). The creator can lay the trending sound over it in the TikTok app.
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
E = json.load(open(f'{DIR}/e1.json'))
SR = 48000; DUR = E['duration']; N = int(SR * DUR); rng = np.random.default_rng(5)
mus = np.zeros(N); sfx = np.zeros(N); voc = np.zeros(N)
STOP = E['dance']['stop']; BONK = E['bonk']; AP = E['appear']; RAIN = E['strays']['at']; PEEK = E['strays']['peek']
def env(n, a=.005, r=.3): x = np.arange(n) / SR; return np.minimum(1, x / a) * np.exp(-x / r)
def add(buf, s, sig, g=1):
    i = int(s * SR); j = min(N, i + len(sig))
    if 0 <= i < N: buf[i:j] += g * sig[:j - i]
mid = lambda n: 440 * 2 ** ((n - 69) / 12)
def pluck(f, d=.6):   # Karplus-Strong string: ukulele-ish
    n = int(d * SR); p = max(2, int(SR / f)); buf = rng.uniform(-1, 1, p); out = np.zeros(n)
    for i in range(n): out[i] = buf[i % p]; buf[i % p] = .5 * (buf[i % p] + buf[(i + 1) % p]) * .996
    return out * env(n, .002, .5)
def noise(d, lp=.1):
    n = rng.standard_normal(int(d * SR)); y = np.zeros_like(n)
    for i in range(1, len(n)): y[i] = y[i - 1] + lp * (n[i] - y[i - 1])
    return y
def tone(f, d, r=.4, a=.005, harm=(1, .5, .25)):
    x = np.arange(int(d * SR)) / SR; return sum(h * np.sin(2 * np.pi * f * (k + 1) * x) for k, h in enumerate(harm)) * env(len(x), a, r)
def sweep(f0, f1, d, r=.1): x = np.arange(int(d * SR)) / SR; f = f0 * (f1 / f0) ** (x / d); return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(x), .002, r)
PL = {}
def pl(n):
    if n not in PL: PL[n] = pluck(mid(n))
    return PL[n]
# music: C - G - Am - F, strummed 8ths (down-up feel), bass on 1 and 3, claps on 2 and 4, shaker 16ths
beat = 60 / 116; prog = [[60, 64, 67, 72], [55, 59, 62, 67], [57, 60, 64, 69], [53, 57, 60, 65]]
CL = noise(.12, .6) * env(int(.12 * SR), .001, .03); SH = noise(.05, .9) * env(int(.05 * SR), .001, .012)
k = 0
while k * beat / 2 < STOP - .01:
    t = k * beat / 2; ch = prog[(k // 8) % 4]; strum = [0, 1, 2, 3] if k % 2 == 0 else [3, 2, 1]
    for i, q in enumerate(strum): add(mus, t + i * .012, pl(ch[q]), .16 if k % 2 == 0 else .1)
    if k % 4 == 0: add(mus, t, tone(mid(ch[0] - 24), .5, .25, .01, (1, .4)), .32)
    if k % 4 == 2: add(mus, t, CL, .5)
    add(mus, t, SH, .12); add(mus, t + beat / 4, SH, .08)
    k += 1
mus[int(STOP * SR):] = 0                                                          # Mango freezes: the music just stops
# sfx
for j, t in enumerate(AP):                                                         # rule 1: houses pop
    if j % 2 == 0: add(sfx, t, sweep(500 + 4 * j, 1300 + 6 * j, .06, .04), .2)
for j, t in enumerate(RAIN):                                                       # rule 2: a soft plop as each cat lands, a few mrrps
    add(sfx, t, sweep(320, 140, .09, .05), .32)
    if j % 5 == 0: add(sfx, t + .05, sweep(700 + 10 * j, 1000 + 10 * j, .16, .1) * np.sin(np.linspace(0, np.pi, int(.16 * SR))), .14)
SA = E['strays']['shopAt']; x = np.arange(int(2.8 * SR)) / SR; add(sfx, SA, (np.sin(2 * np.pi * 60 * x) + .4 * np.sin(2 * np.pi * 120 * x)) * .5 * np.minimum(1, x / .05) * np.minimum(1, (2.8 - x) / .05), .12)   # fridge hum
for j in range(9): add(sfx, SA + .3 + j * .27, sweep(650 + 40 * (j % 3), 950 + 50 * (j % 4), .28, .2) * np.sin(np.linspace(0, np.pi, int(.28 * SR))), .1)   # crowded little meows
add(sfx, BONK, tone(mid(79), .2, .05, .001, (1, .2)), .55); add(sfx, BONK, noise(.05, .5) * env(int(.05 * SR), .001, .01), .5)   # bonk (wood block)
add(sfx, BONK + .04, sweep(300, 900, .35, .25) * (1 + .5 * np.sin(np.linspace(0, 60, int(.35 * SR)))), .25)   # boing
add(sfx, BONK + .72, sweep(260, 120, .1, .06), .3)                                  # the fish lands
pk = PEEK['at'] + PEEK['dur']; add(sfx, pk + .2, sweep(620, 880, .22, .15) * np.sin(np.linspace(0, np.pi, int(.22 * SR))), .3)   # one small mrrp
for l in json.load(open(f'{DIR}/timeline.json')):
    a, _ = sf.read(f"{DIR}/l{l['i']:02d}.wav"); add(voc, l['s'], a)
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .75 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc + duck * (.6 * mus + .8 * sfx); mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.005 * SR)] = np.linspace(0, 1, int(.005 * SR)); fade[-int(.02 * SR):] = np.linspace(1, 0, int(.02 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-14:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
