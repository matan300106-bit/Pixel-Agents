# Music (code synth, bright and bouncy; it stops dead for "where's Mango?") + SFX + voice mix for Day 7 -> DIR/mix.wav (stereo, loudnorm)
import numpy as np, json, soundfile as sf, subprocess, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else 'v'
SR = 48000; DUR = 32.0; N = int(SR * DUR); rng = np.random.default_rng(3)
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
# music: bright I-vi-IV-V plucks (120 bpm), a record scratch stops it at "where's Mango?", it comes back on Mango in his small box
prog = [[60, 64, 67, 72], [57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67]]; beat = 60 / 120; b = 0; T = 0.0
MUTE = (23.65, 25.35)
while T < DUR - .25:
    ch = prog[(b // 4) % 4]
    if not (MUTE[0] <= T < MUTE[1]):
        add(mus, T, tone(mid(ch[b % 4] + (12 if b % 8 >= 4 else 0)), 1.0, .3, .003, (1, .5, .25)), .16)
        if b % 4 == 0: add(mus, T, tone(mid(ch[0] - 24), 2.0, .8, .02, (1, .3)), .22)
        if b % 2 == 0: add(mus, T, noise(.03, .6) * env(int(.03 * SR), .001, .01), .1)
    b += 1; T = b * beat / 2
i0, i1 = int(MUTE[0] * SR), int(MUTE[0] * SR) + 2400; mus[i0:] *= 1; mus[i0:i1] *= np.linspace(1, 0, i1 - i0); mus[int(MUTE[0] * SR) + 2400:int(MUTE[1] * SR)] = 0   # hard stop (tails cut)
# sfx
E = json.load(open(f'{DIR}/e1.json')); NB = E['newBuild']; PA = NB['partsAt']; BY = E['box']; OA = NB['openAt']
add(sfx, 0.3, pop(400, 1400, .2), .5)
for t in (1.0, 2.9, 9.6, 15.8, 18.6, 23.6, 28.2, 30.9): whoosh(t, .7, .08, 1.0)
add(sfx, 3.0, pop(300, 900, .1), .6); whoosh(2.95, .35, .2, .6)                 # comment card slides up
for k, n in enumerate([84, 88]): add(sfx, 4.1 + k * .09, tone(mid(n), .8, .3, .002, (1, .3)), .3)   # crown ding
for k, n in enumerate([79, 76]): add(sfx, 7.2 + k * .12, tone(mid(n), .4, .2, .002, SQ), .12)        # Mango looks at us (boop boop)
land = PA[0] + .45; add(sfx, land, tone(45, .9, .35, .002, (1, .6, .3)), 1.0); add(sfx, land, noise(.6, .05) * env(int(.6 * SR), .002, .25), 2.2)   # the giant box lands: big cardboard THUD + dust
for k in range(4): add(sfx, PA[1] + .42 + k * .07, noise(.06, .3) * env(int(.06 * SR), .001, .02), .5); add(sfx, PA[1] + .42 + k * .07, pop(200, 320, .06), .4)   # flaps flop open
for k in range(4): add(sfx, PA[2] + .42 + k * .05, pop(700 - 60 * k, 300, .07), .45)   # cat doors: pop pop pop pop
for k in range(7): add(sfx, PA[3] + .42 + k * .045, pop(900 + 80 * k, 1500 + 80 * k, .04), .3)   # peek holes
for k in range(6): add(sfx, PA[4] + .42 + k * .06, noise(.05, .7) * env(int(.05 * SR), .001, .02), .35)   # scratch ramp: scritch
x = np.arange(int(.5 * SR)) / SR; horn = np.sign(np.sin(2 * np.pi * (520 + 40 * np.sin(2 * np.pi * 7 * x)) * x)) * env(len(x), .02, .5) * np.minimum(1, (.5 - x) / .08)
add(sfx, PA[5] + .42, horn, .12); jingle(PA[5] + .5, [79, 84, 88, 91], .06, .18)    # party flags: party horn + jingle
be = NB['at'] + NB['slow']
for k, n in enumerate([72, 76, 79, 84, 88]): add(sfx, be + .1 + k * .07, tone(mid(n), .9, .35, .002, (1, .3)), .24)   # done fanfare
for k in range(10): add(sfx, OA + .15 + k * .13, pop(900, 1300, .03), .18)          # paws: cats run in
for k in range(13): add(sfx, OA + 1.5 + k * .17 + .1, pop(500 + 50 * (k % 5), 1200 + 60 * (k % 5), .07), .32)   # heads pop out of the holes
for k in range(3): add(sfx, OA + 1.6 + k * .5, tone(70, .3, .12, .002, (1, .5)), .35)   # the box shakes (thump thump)
ca = E['confettiAt'][0] + .4; add(sfx, ca - .1, horn, .14); add(sfx, ca, noise(.3, .6) * env(int(.3 * SR), .002, .1), .5)   # 1 week party: horn + confetti pop
for k, n in enumerate([72, 76, 79, 84, 79, 84, 88]): add(sfx, ca + .1 + k * .1, tone(mid(n), .7, .3, .002, SQ), .14)
for k in range(5): add(sfx, BY['boxAt'] + .1 + k * .28, pop(500, 380, .05), .2)     # Mango tip-toes to his small box
x = np.arange(int(.45 * SR)) / SR; f = 900 * np.exp(-x * 5); sc = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * env(len(x), .005, .3) + noise(.45, .4)[:len(x)] * .6
add(sfx, MUTE[0], sc, .45)                                                       # record scratch
add(sfx, 24.0, pop(600, 900, .08), .25); add(sfx, 24.6, pop(600, 900, .08), .25)  # looking around (blip blip)
hp = BY['boxAt'] + 1.4; add(sfx, hp, sweep(300, 700, .3, .08)); add(sfx, hp + .42, tone(80, .4, .15, .002, (1, .5)), .5)   # boing... plop in the small box
add(sfx, BY['turnAt'], pop(700, 1100, .1), .4)
add(sfx, 28.7, pop(300, 1000, .14), .6)                                          # Day 8 sign
# voice
for l in json.load(open(f'{DIR}/timeline.json')):
    a, _ = sf.read(f"{DIR}/l{l['i']:02d}.wav"); add(voc, l['s'], a)
vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .75 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
mix = voc + .55 * mus * duck + .8 * sfx; mix *= .89 / np.max(np.abs(mix))
fade = np.ones(N); fade[:int(.01 * SR)] = np.linspace(0, 1, int(.01 * SR)); fade[-int(.04 * SR):] = np.linspace(1, 0, int(.04 * SR))
sf.write(f'{DIR}/mix_raw.wav', mix * fade, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{DIR}/mix_raw.wav', '-af', 'loudnorm=I=-12.5:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), f'{DIR}/mix.wav'], check=True)
print('ok')
