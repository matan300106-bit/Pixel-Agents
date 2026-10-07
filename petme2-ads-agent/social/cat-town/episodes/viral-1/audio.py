# Music (code synth) + SFX + voice mix for viral-1 -> DIR/mix.wav (stereo, loudnorm -14)
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
SR = 48000; DUR = 14.8; N = int(SR * DUR); rng = np.random.default_rng(2)
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
# music: sad sparse piano (A minor, slow) while Mango is alone; bouncy C major plucks once the follows start; sad again for the loop
beat = 60 / 108
def piano(n, d=1.8, g=.2): add(mus, n[0], tone(mid(n[1]), d, .9, .004, (1, .35, .12)), g)
for s0 in (0.0, 13.4):
    seq = [(0, 57), (.45, 64), (.9, 69), (1.35, 72), (2.0, 53), (2.45, 60), (2.9, 65), (3.35, 69)] if s0 == 0 else [(0, 57), (.45, 64), (.9, 69)]
    for t, n in seq:
        if s0 + t < (4.0 if s0 == 0 else DUR - .1): piano((s0 + t, n), 1.6, .2)
    add(mus, s0, tone(mid(45), 3.6 if s0 == 0 else 1.4, 1.4, .02, (1, .3)), .16)
prog = [[60, 64, 67, 72], [57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67]]; b = 0; T = 4.0
while T < 13.3:
    ch = prog[(b // 4) % 4]
    add(mus, T, tone(mid(ch[b % 4] + (12 if b % 8 >= 4 else 0)), 1.0, .3), .17)
    if b % 4 == 0: add(mus, T, tone(mid(ch[0] - 24), 2.0, .8, .02, (1, .3)), .24)
    b += 1; T = 4.0 + b * beat / 2
for n in [60, 64, 67, 72, 76]:   # warm pad swell when the town hits 1,000
    x = np.arange(int(2.6 * SR)) / SR; add(mus, 9.9, np.sin(2 * np.pi * mid(n) * x) * np.minimum(1, x / .3) * np.minimum(1, (2.6 - x) / .4), .08)
# sfx
def meow(s, f0=700, d=.45, g=.2):
    x = np.arange(int(d * SR)) / SR; f = f0 + 350 * np.sin(np.pi * x / d) - 250 * x / d
    add(sfx, s, np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * x / d) ** 1.5 * (1 + .3 * np.sin(2 * np.pi * 2 * f * x)), g)
whoosh(0.0, .8, .03, .5)                                                     # soft wind: empty town
meow(2.3, 560, .7, .14)                                                     # small lonely meow
add(sfx, 3.95, (lambda x: np.sin(2 * np.pi * np.cumsum(900 - 700 * x / x[-1]) / SR) * env(len(x), .002, .12))(np.arange(int(.25 * SR)) / SR), .5)   # record scratch: "But"
whoosh(4.0, .5, .2, 1.3)                                                    # whip dive to house 1
for s, f in [(4.6, 600), (5.45, 700), (6.19, 800)]:
    add(sfx, s, pop(f, f * 2.4, .14), 1.1); add(sfx, s + .08, tone(f * 2, .6, .25, .003, (1, .3)), .3); meow(s + .18, 900, .3, .12)   # house pops
whoosh(7.8, 1.6, .06, 1.2)                                                  # crane up
for k in range(46):                                                          # the town fills: a cascade of pops that speeds up
    s = 7.9 + 2.2 * (k / 46) ** .8; f = 500 + 900 * rng.random(); add(sfx, s, pop(f, f * 2, .07), .35)
add(sfx, 10.12, pop(400, 1500, .16), 1.1)
for k, n in enumerate([72, 76, 79, 84, 88]): add(sfx, 10.18 + k * .07, tone(mid(n), .9, .35, .002, (1, .3)), .24)   # fanfare: 1,000!
for k in range(16): add(sfx, 10.5 + k * .05, noise(.04, .7) * env(int(.04 * SR), .001, .01), .25)   # confetti crackle
whoosh(10.6, .5, .15, .8)
for k in range(3): add(sfx, 11.3 + k * .45, pop(800, 1700, .08), .5)        # comment chips pop in
whoosh(13.4, 1.2, .05, .9)                                                  # drift back to lonely Mango
meow(14.0, 540, .6, .12)                                                    # soft lonely meow under "anyone?"
for k in range(3): add(sfx, 10.6 + k * .06, pop(1400 - k * 300, 500, .09), .3)   # rewind blip: back to 1 cat
# voice
for l in json.load(open(f'{DIR}/timeline.json')):
    a, _ = sf.read(f"{DIR}/l{l['i']:02d}.wav"); add(voc, l['s'], a)
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .8 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc + .55 * mus * duck + .8 * sfx; mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.01 * SR)] = np.linspace(0, 1, int(.01 * SR)); fade[-int(.04 * SR):] = np.linspace(1, 0, int(.04 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-12.5:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
