# Music (code synth: minor while the cats have no home, bright from the build) + SFX + voice mix for Day 4 -> DIR/mix.wav (stereo, loudnorm)
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
SR = 48000; DUR = 33.8; N = int(SR * DUR); rng = np.random.default_rng(3)
mus = np.zeros(N); sfx = np.zeros(N); voc = np.zeros(N)
def env(n, a=.005, r=.3): x = np.arange(n) / SR; return np.minimum(1, x / a) * np.exp(-x / r)
def add(buf, s, sig, g=1):
    i = int(s * SR); j = min(N, i + len(sig))
    if 0 <= i < N: buf[i:j] += g * sig[:j - i]
def tone(f, d, r=.4, a=.005, harm=(1, .5, .25)):
    x = np.arange(int(d * SR)) / SR; return sum(h * np.sin(2 * np.pi * f * (k + 1) * x) for k, h in enumerate(harm)) * env(len(x), a, r)
SQ = (1, 0, .33, 0, .2, 0, .14)                      # square-ish: odd harmonics (8-bit arcade)
mid = lambda n: 440 * 2 ** ((n - 69) / 12)
def pop(f0=500, f1=1400, d=.12): x = np.arange(int(d * SR)) / SR; f = f0 + (f1 - f0) * x / d; return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(x), .002, .05)
def sweep(f0, f1, d, g=1): x = np.arange(int(d * SR)) / SR; f = f0 + (f1 - f0) * x / d; s = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * .3 + np.sin(2 * np.pi * np.cumsum(f) / SR); return s * np.minimum(1, x / .03) * np.minimum(1, (d - x) / .05) * g
def noise(d, lp=.1):
    n = rng.standard_normal(int(d * SR)); y = np.zeros_like(n)
    for i in range(1, len(n)): y[i] = y[i - 1] + lp * (n[i] - y[i - 1])
    return y
def whoosh(s, d=.7, lp=.08, g=1.4): w = noise(d, lp); x = np.arange(len(w)) / SR; add(sfx, s, w * np.sin(np.pi * x / d) ** 2, g)
def jingle(s, notes, step=.075, g=.22): [add(sfx, s + k * step, tone(mid(n), .35, .18, .002, SQ), g) for k, n in enumerate(notes)]
# music: soft minor plucks while the cats have no home, bright I-vi-IV-V once the studio builds (112 bpm)
sad = [[57, 60, 64, 69], [53, 57, 60, 65], [48, 52, 55, 60], [55, 59, 62, 67]]
prog = [[60, 64, 67, 72], [57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67]]; beat = 60 / 112; b = 0; T = 0.0
while T < DUR - .25:
    happy = 22.35 <= T < 31.9 or T < 1.0; ch = (prog if happy else sad)[(b // 4) % 4]
    add(mus, T, tone(mid(ch[b % 4] + (12 if b % 8 >= 4 else 0)), 1.2, .35, .003, (1, .5, .25)), .16)
    if b % 4 == 0: add(mus, T, tone(mid(ch[0] - 24), 2.4, .9, .02, (1, .3)), .22)
    if happy and b % 2 == 0: add(mus, T, noise(.03, .6) * env(int(.03 * SR), .001, .01), .1)
    b += 1; T = b * beat / 2
# sfx
E = json.load(open(f'{DIR}/e1.json')); X = json.load(open(f'{DIR}/text.json'))
add(sfx, 0.3, pop(900, 250, .35), .5)                                        # uh-oh on the hook
whoosh(0.98, .5, .1, .7); whoosh(3.9, .8, .08, 1.0)                          # up over the town
def ticks(r, n=36, f=600):
    for k in range(n): t = r[0] + (r[1] - r[0]) * ((k + .5) / n) ** .8; add(sfx, t, pop(f + 12 * k, f * 2 + 20 * k, .04), .18)
ticks(X['rollH']); ticks(X['rollC'], 40, 700)
for r in (X['rollH'], X['rollC']):
    for k, n in enumerate([72, 76, 79, 84]): add(sfx, r[1] + .05 + k * .07, tone(mid(n), .9, .35, .002, (1, .3)), .2)
whoosh(8.0, .9, .08, 1.0); whoosh(12.0, .9, .08, 1.0)
add(sfx, X['nohomeAt'], pop(800, 200, .4), .6)                               # 218: sad drop
for k, n in enumerate([67, 63, 60]): add(sfx, 14.6 + k * .16, tone(mid(n), .7, .3, .002, (1, .3)), .2)
whoosh(17.2, .8, .08, 1.0); add(sfx, 17.5, pop(1300, 900, .12), .3)         # lonely meow-ish blip
add(sfx, 18.85, pop(300, 900, .1), .6); whoosh(18.8, .35, .2, .6)           # comment card slides up
for k, n in enumerate([84, 88]): add(sfx, 19.95 + k * .09, tone(mid(n), .8, .3, .002, (1, .3)), .3)   # crown ding
whoosh(18.75, 1.3, .06, .9); whoosh(22.3, .6, .1, .8)
for k, t in enumerate(E['newBuild']['partsAt']):                            # each piece lands
    add(sfx, t + .45, pop(220 + 40 * k, 480 + 60 * k, .09), .8); add(sfx, t + .45, noise(.05, .5) * env(int(.05 * SR), .001, .012), .45)
be = E['newBuild']['at'] + E['newBuild']['slow']
for k, n in enumerate([72, 76, 79, 84, 88]): add(sfx, be + .1 + k * .07, tone(mid(n), .9, .35, .002, (1, .3)), .22)   # done fanfare
for k in range(6): add(sfx, E['newBuild']['openAt'] + k * .2 + .4, pop(900, 1300, .03), .2)   # cats run in
whoosh(25.4, .9, .08, .9); sa = E['statueAt']
add(sfx, sa, sweep(180, 420, 2.3, .12))                                      # statue rises
for k in range(5): add(sfx, sa + .3 + k * .42, noise(.04, .6) * env(int(.04 * SR), .001, .01), .5)   # chisel taps
for k, n in enumerate([72, 76, 79, 84, 88, 91]): add(sfx, sa + 2.4 + k * .07, tone(mid(n), 1.0, .4, .002, (1, .3)), .24)   # ta-da
whoosh(28.7, .9, .08, 1.0); L = E['lone']
add(sfx, L['houseAt'], pop(250, 800, .14), .9); add(sfx, L['houseAt'], noise(.05, .5) * env(int(.05 * SR), .001, .012), .5)   # house pops
add(sfx, L['runAt'], pop(900, 1400, .05), .3); add(sfx, X['homeAt'], pop(600, 1500, .12), .5)
for k, n in enumerate([76, 79, 84, 88]): add(sfx, X['homeAt'] + .1 + k * .07, tone(mid(n), .9, .35, .002, (1, .3)), .22)   # 217!
whoosh(31.9, .9, .08, 1.1); add(sfx, 32.6, pop(700, 1600, .12), .45)
# voice
for l in json.load(open(f'{DIR}/timeline.json')):
    a, _ = sf.read(f"{DIR}/l{l['i']:02d}.wav"); add(voc, l['s'], a)
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .8 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc + .55 * mus * duck + .8 * sfx; mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.01 * SR)] = np.linspace(0, 1, int(.01 * SR)); fade[-int(.04 * SR):] = np.linspace(1, 0, int(.04 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-12.5:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
