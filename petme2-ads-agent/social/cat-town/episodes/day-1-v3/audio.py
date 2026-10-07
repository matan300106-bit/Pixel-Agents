# Music (code synth) + SFX + voice mix for rule-v1 -> DIR/mix.wav (stereo, loudnorm -14)
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
SR = 48000; DUR = 17.6; N = int(SR * DUR); rng = np.random.default_rng(2)
mus = np.zeros(N); sfx = np.zeros(N); voc = np.zeros(N)
def env(n, a=.005, r=.3): x = np.arange(n) / SR; return np.minimum(1, x / a) * np.exp(-x / r)
def add(buf, s, sig, g=1):
    i = int(s * SR); j = min(N, i + len(sig))
    if 0 <= i < N: buf[i:j] += g * sig[:j - i]
def tone(f, d, r=.4, a=.005, harm=(1, .5, .25)):
    x = np.arange(int(d * SR)) / SR; return sum(h * np.sin(2 * np.pi * f * (k + 1) * x) for k, h in enumerate(harm)) * env(len(x), a, r)
mid = lambda n: 440 * 2 ** ((n - 69) / 12)
def pop(f0=500, f1=1400, d=.12): x = np.arange(int(d * SR)) / SR; f = f0 + (f1 - f0) * x / d; return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(x), .002, .05)
def noise(d, lp=.1):
    n = rng.standard_normal(int(d * SR)); y = np.zeros_like(n)
    for i in range(1, len(n)): y[i] = y[i - 1] + lp * (n[i] - y[i - 1])
    return y
def whoosh(s, d=.7, lp=.08, g=1.4): w = noise(d, lp); x = np.arange(len(w)) / SR; add(sfx, s, w * np.sin(np.pi * x / d) ** 2, g)
# music: bouncy I-vi-IV-V pluck arps at 108 bpm, bass on the bar; quiet in the goal->today drop
prog = [[60, 64, 67, 72], [57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67]]; beat = 60 / 108; b = 0; T = 0.0
while T < DUR - .25:
    ch = prog[(b // 4) % 4]; quiet = 14.4 <= T < 14.75
    if not quiet:
        add(mus, T, tone(mid(ch[b % 4] + (12 if b % 8 >= 4 else 0)), 1.2, .35), .16)
        if b % 4 == 0: add(mus, T, tone(mid(ch[0] - 24), 2.4, .9, .02, (1, .3)), .22)
    b += 1; T = b * beat / 2
for n in [60, 64, 67, 72, 76]:   # warm pad swell under "together" (goal shot)
    x = np.arange(int(2.4 * SR)) / SR; add(mus, 12.0, np.sin(2 * np.pi * mid(n) * x) * np.minimum(1, x / .5) * np.minimum(1, (2.4 - x) / .15), .08)
add(mus, DUR - .2, tone(mid(60), .2, .1), .1)    # lands on the intro chord root so the loop restarts clean
# sfx
whoosh(0.3, 1.6, .06, 1.2)                                                            # pull back to the empty town
for k in range(6): add(sfx, 2.75 + k * .11, noise(.05, .6) * env(int(.05 * SR), .001, .015), .5)   # crunch (Mango eats alone)
whoosh(4.4, .7, .1, 1.3)                                                    # dive to the lot
for s, f in [(5.65, 600), (6.35, 700), (7.05, 800)]:
    add(sfx, s, pop(f, f * 2.4, .14), 1.1); add(sfx, s + .08, tone(f * 2, .6, .25, .003, (1, .3)), .3)   # house pops
add(sfx, 8.9, pop(400, 1500, .16), 1.2)                                    # statue pop
for k, n in enumerate([72, 76, 79, 84, 88]): add(sfx, 8.97 + k * .07, tone(mid(n), .9, .35, .002, (1, .3)), .24)   # fanfare
for k in range(16): add(sfx, 9.3 + k * .05, noise(.04, .7) * env(int(.04 * SR), .001, .01), .3)   # confetti crackle
add(sfx, 10.4, pop(700, 1600, .12), .5)
add(sfx, 14.4, (lambda x: np.sin(2 * np.pi * np.cumsum(900 - 700 * x / x[-1]) / SR) * env(len(x), .002, .12))(np.arange(int(.25 * SR)) / SR), .5)   # record-scratch drop
add(sfx, 14.42, tone(110, .5, .15, .002, (1, .6, .3)), .35)
whoosh(14.95, 1.0, .08, 1.3)                                                # dive back to Mango
for s in [15.0, 15.8, 17.0]: add(sfx, s, pop(700, 1600, .12), .45)
x = np.arange(int(.45 * SR)) / SR; f = 700 + 350 * np.sin(np.pi * x / .45) - 200 * x / .45   # soft synth meow
add(sfx, 17.1, np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * x / .45) ** 1.5 * (1 + .3 * np.sin(2 * np.pi * 2 * f * x)), .22)
# voice
for l in json.load(open(f'{DIR}/timeline.json')):
    a, _ = sf.read(f"{DIR}/l{l['i']:02d}.wav"); add(voc, l['s'], a)
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .8 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc + .55 * mus * duck + .8 * sfx; mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.01 * SR)] = np.linspace(0, 1, int(.01 * SR)); fade[-int(.04 * SR):] = np.linspace(1, 0, int(.04 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-12.5:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
