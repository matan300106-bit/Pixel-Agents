# Music (code synth, bright and bouncy; it stops dead for the pineapple joke) + SFX + voice mix for Day 5 -> DIR/mix.wav (stereo, loudnorm)
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
SR = 48000; DUR = 30.6; N = int(SR * DUR); rng = np.random.default_rng(3)
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
# music: bright I-vi-IV-V plucks (120 bpm), a record scratch stops it at the pineapple, it comes back with the fish
prog = [[60, 64, 67, 72], [57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67]]; beat = 60 / 120; b = 0; T = 0.0
MUTE = (18.35, 19.95)
while T < DUR - .25:
    ch = prog[(b // 4) % 4]
    if not (MUTE[0] <= T < MUTE[1]):
        add(mus, T, tone(mid(ch[b % 4] + (12 if b % 8 >= 4 else 0)), 1.0, .3, .003, (1, .5, .25)), .16)
        if b % 4 == 0: add(mus, T, tone(mid(ch[0] - 24), 2.0, .8, .02, (1, .3)), .22)
        if b % 2 == 0: add(mus, T, noise(.03, .6) * env(int(.03 * SR), .001, .01), .1)
    b += 1; T = b * beat / 2
i0, i1 = int(MUTE[0] * SR), int(MUTE[0] * SR) + 2400; mus[i0:] *= 1; mus[i0:i1] *= np.linspace(1, 0, i1 - i0); mus[int(MUTE[0] * SR) + 2400:int(MUTE[1] * SR)] = 0   # hard stop (tails cut)
# sfx
E = json.load(open(f'{DIR}/e1.json')); X = json.load(open(f'{DIR}/text.json')); NB = E['newBuild']; PA = NB['partsAt']
add(sfx, 0.3, pop(400, 1400, .2), .5)
for t in (1.0, 2.9, 9.4, 22.1, 27.0, 29.6): whoosh(t, .7, .08, 1.0)
add(sfx, 3.0, pop(300, 900, .1), .6); whoosh(2.95, .35, .2, .6)                 # comment card slides up
for k, n in enumerate([84, 88]): add(sfx, 4.1 + k * .09, tone(mid(n), .8, .3, .002, (1, .3)), .3)   # crown ding
for k, n in enumerate([79, 76]): add(sfx, 7.4 + k * .12, tone(mid(n), .4, .2, .002, SQ), .12)        # Mango looks at us (boop boop)
land = PA[1] + .45; add(sfx, land, tone(48, .9, .35, .002, (1, .6, .3)), 1.0); add(sfx, land, noise(.6, .05) * env(int(.6 * SR), .002, .25), 2.2)   # crust BOOM + dust
for k, t in enumerate(PA[2:-2]):                                                # each topping lands: a different little pop
    add(sfx, t + .42, pop(260 + 45 * k, 700 + 70 * k, .09), .8); add(sfx, t + .42, noise(.04, .5) * env(int(.04 * SR), .001, .01), .35)
pa = PA[-2] + .42; add(sfx, pa, pop(300, 900, .1), .7)                           # pineapple lands...
x = np.arange(int(.45 * SR)) / SR; f = 900 * np.exp(-x * 5); sc = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * env(len(x), .005, .3) + noise(.45, .4)[:len(x)] * .6
add(sfx, MUTE[0], sc, .45)                                                       # ...record scratch
for k in range(4): add(sfx, E['pizza']['walkAt'] + .2 + k * .45, pop(500, 380, .05), .25)   # one cat walks off (tip-toe)
fl = PA[-1] + .42; add(sfx, fl, pop(200, 1200, .16), .8); add(sfx, fl, noise(.12, .3) * env(int(.12 * SR), .001, .05), .6)   # fish: splat
be = NB['at'] + NB['slow']
for k, n in enumerate([72, 76, 79, 84, 88]): add(sfx, be + .1 + k * .07, tone(mid(n), .9, .35, .002, (1, .3)), .24)   # done fanfare
for k in range(8): add(sfx, NB['openAt'] + .3 + k * .2, pop(900, 1400, .03), .2)  # cats hop on
ba = E['pizza']['biteAt'] + .5; add(sfx, ba, noise(.08, .5) * env(int(.08 * SR), .001, .03), 1.2); add(sfx, ba + .14, noise(.06, .5) * env(int(.06 * SR), .001, .02), .9)   # chomp chomp
add(sfx, ba + .3, sweep(500, 1300, .5, .06))                                     # cheese stretch... boing
add(sfx, E['pizza']['turnAt'], pop(700, 1100, .1), .4)
add(sfx, 27.7, pop(300, 1000, .14), .6)                                          # Day 6 sign
# voice
for l in json.load(open(f'{DIR}/timeline.json')):
    a, _ = sf.read(f"{DIR}/l{l['i']:02d}.wav"); add(voc, l['s'], a)
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .75 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc + .55 * mus * duck + .8 * sfx; mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.01 * SR)] = np.linspace(0, 1, int(.01 * SR)); fade[-int(.04 * SR):] = np.linspace(1, 0, int(.04 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-12.5:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
