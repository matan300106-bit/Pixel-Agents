# Music (code synth, turns 8-bit after the neon goes on) + SFX + voice mix for Day 3 -> DIR/mix.wav (stereo, loudnorm)
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
SR = 48000; DUR = 31.2; N = int(SR * DUR); rng = np.random.default_rng(3)
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
# music: bouncy I-vi-IV-V at 112 bpm; plucks before the lights, square leads after
prog = [[60, 64, 67, 72], [57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67]]; beat = 60 / 112; b = 0; T = 0.0
while T < DUR - .25:
    ch = prog[(b // 4) % 4]; arc = T >= 21.62 or T < 1.0 or T >= 30.3
    add(mus, T, tone(mid(ch[b % 4] + (12 if b % 8 >= 4 else 0)), .6 if arc else 1.2, .2 if arc else .35, .003, SQ if arc else (1, .5, .25)), .12 if arc else .16)
    if b % 4 == 0: add(mus, T, tone(mid(ch[0] - 24), 2.4, .9, .02, (1, .3)), .22)
    if arc and b % 2 == 0: add(mus, T, noise(.03, .6) * env(int(.03 * SR), .001, .01), .12)   # hi-hat ticks
    b += 1; T = b * beat / 2
# sfx
jingle(0.02, [72, 76, 79, 84], .07, .2)                                     # arcade start jingle on the hook
whoosh(0.98, .5, .1, .9)                                                     # cut to day
add(sfx, 3.1, pop(300, 900, .1), .6); whoosh(3.05, .35, .2, .6)             # comment card slides up
for k, n in enumerate([84, 88]): add(sfx, 4.25 + k * .09, tone(mid(n), .8, .3, .002, (1, .3)), .3)   # crown ding
whoosh(6.85, 2.0, .06, 1.0)                                                  # fly to Francisco's lot
add(sfx, 9.0, pop(500, 1500, .14), .8); whoosh(8.95, .5, .15, 1.0)          # split screen
E = json.load(open(f'{DIR}/e1.json')); AT = E['strays']['at']
for k in range(40): t = 10.9 + 3.2 * ((k + .5) / 40) ** .8; add(sfx, t, pop(600 + 12 * k, 1200 + 20 * k, .04), .18)   # counter ticks
for k, n in enumerate([72, 76, 79, 84, 88]): add(sfx, 14.15 + k * .07, tone(mid(n), .9, .35, .002, (1, .3)), .22)        # 253 / 467 fanfare
add(sfx, 14.6, pop(900, 250, .35), .6)                                       # uh-oh
for k, t in enumerate(sorted(a for a in AT if 14.5 <= a < 15.4)):
    if k % 3 == 0: add(sfx, t, pop(400 + 5 * k, 900 + 8 * k, .05), .2)
whoosh(16.6, 1.0, .07, 1.1); whoosh(17.45, 1.0, .07, 1.0)
for k, t in enumerate(E['newBuild']['partsAt']):                             # each piece lands
    add(sfx, t + .45, pop(220 + 40 * k, 480 + 60 * k, .09), .8); add(sfx, t + .45, noise(.05, .5) * env(int(.05 * SR), .001, .012), .45)
la = E['newBuild']['lightsAt']
for k in range(4): add(sfx, la + k * .125, (np.sign(np.sin(2 * np.pi * 120 * np.arange(int(.06 * SR)) / SR)) * env(int(.06 * SR), .001, .04)), .25)   # neon buzz flicker
jingle(la + .45, [60, 64, 67, 72, 76, 79, 84], .06, .24)                    # lights on: power-up
for k in range(10): add(sfx, E['newBuild']['openAt'] + k * .22 + .3, pop(900, 1300, .03), .2)   # cats run in
ca = E['clawAt']
add(sfx, ca, sweep(300, 220, .7, .18)); add(sfx, ca + .7, pop(1200, 400, .08), .6); add(sfx, ca + .78, noise(.04, .6) * env(int(.04 * SR), .001, .01), .4)   # claw down + grab
add(sfx, ca + 1.0, sweep(220, 320, .8, .18))                                 # claw up
add(sfx, ca + 1.8, pop(1400, 500, .25), .5)                                  # fish drops out
jingle(ca + 2.3, [76, 79, 84, 88, 91], .07, .26)                            # winner!
whoosh(25.7, 1.4, .07, 1.1)
add(sfx, 25.75, pop(600, 1400, .1), .5); add(sfx, 27.25, pop(600, 1400, .1), .5)
whoosh(28.7, .9, .08, 1.0); add(sfx, 29.3, pop(700, 1600, .12), .45)
whoosh(30.3, .7, .1, 1.2)
# voice
for l in json.load(open(f'{DIR}/timeline.json')):
    a, _ = sf.read(f"{DIR}/l{l['i']:02d}.wav"); add(voc, l['s'], a)
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .8 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc + .55 * mus * duck + .8 * sfx; mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.01 * SR)] = np.linspace(0, 1, int(.01 * SR)); fade[-int(.04 * SR):] = np.linspace(1, 0, int(.04 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-12.5:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
