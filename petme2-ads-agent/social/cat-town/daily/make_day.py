"""Cat Town daily episode: new followers move in as cats, the most-liked comment gets built, one 1080x1920 video.

Usage (from this folder, after ./setup.sh):
  python3 make_day.py days/day-02.json            # makes days/day-02/ (voice, frames, video.mp4, cover.jpg)
  python3 make_day.py days/day-02.json --test     # only a few test stills (fast check of the shots)
  python3 make_day.py days/day-02.json --commit   # after the owner approves: add the day to state.json

Day file: {"day": 2, "new_followers": 12,
           "comments": [{"by": "anna", "text": "Build a cat airport!", "likes": 87}, ...],   # top few, any order
           "build": {"name": "Cat Airport"}}   # what the winning comment asks for, cat version (Claude picks it)
Optional in "build": "kind" (cafe, pool, market, statue, cityhall, petshop, custom). Without it the kind comes from the name.
The winner is the comment with the most likes. Skip rude/political/unsafe ones by leaving them out of "comments".
"""
import json, os, subprocess, sys, shutil
from pathlib import Path
import numpy as np, soundfile as sf

HERE = Path(__file__).resolve().parent
CT = HERE.parent                                     # the cat-town folder (catcity.html lives here)
TTS = Path(os.environ.get('KOKORO_DIR', '/tmp/tts'))
OUT_SHARE = Path(os.environ.get('CAT_TOWN_OUT', '/mnt/project-files/cat-town'))
SR = 48000
KINDS = [('cafe', ['cafe', 'café', 'coffee', 'bakery', 'restaurant', 'pizza', 'sushi', 'diner']),
         ('pool', ['pool', 'swim', 'water park', 'spa']), ('market', ['market', 'fish', 'shop', 'store', 'mall']),
         ('statue', ['statue', 'monument']), ('cityhall', ['city hall', 'town hall', 'castle', 'palace', 'museum'])]


def kind_for(name):
    n = name.lower()
    for k, words in KINDS:
        if any(w in n for w in words):
            return k
    return 'custom'


def say_n(n):
    return f'{n:,}'


def voice_lines(day, X, total, build):
    a = 'an' if build[0].lower() in 'aeiou' else 'a'
    cats = 'one new cat' if X == 1 else f'{say_n(X)} new cats'
    fol = 'one new follower' if X == 1 else f'{say_n(X)} new followers'
    return [
        ('hook', f'Day {day}. You asked for {a} {build}.'),
        ('cats', f'{fol}... so {cats} moved in!' if X else 'No new cats today... yet.'),
        ('total', f'Cat Town has {say_n(total)} cats now.'),
        ('comment', 'And the most liked comment wants...'),
        ('build', f'{a} {build}!'),
        ('built', 'So we built it!'),
        ('cta', 'Follow to move your cat in, and comment what we build tomorrow!'),
    ]


def make_voice(lines, wd):
    from kokoro_onnx import Kokoro
    k = Kokoro(str(TTS / 'kokoro.onnx'), str(TTS / 'voices.bin'))
    gaps = {'hook': .35, 'cats': .15, 'total': .45, 'comment': .25, 'build': .45, 'built': .5}
    t, out = .15, []
    for i, (role, text) in enumerate(lines):
        a, sr = k.create(text, voice='af_heart', speed=1.12, lang='en-us')
        raw, trimmed = wd / f'v{i}.wav', wd / f'v{i}t.wav'
        sf.write(raw, a, sr)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', raw, '-af', 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse', '-ar', str(SR), '-ac', '1', trimmed], check=True)
        d = sf.info(trimmed).duration
        out.append(dict(role=role, text=text, s=round(t, 3), e=round(t + d, 3), wav=str(trimmed)))
        t += d + gaps.get(role, .3)
    return out


def words(l):
    ws = l['text'].split(); n = sum(len(w) for w in ws); t = l['s']; r = []
    for w in ws:
        d = (l['e'] - l['s']) * len(w) / n; r.append({'w': w, 's': round(t, 3), 'e': round(t + d, 3)}); t += d
    return r


def main():
    cfg_path = Path(sys.argv[1]).resolve(); flags = sys.argv[2:]
    cfg = json.load(open(cfg_path)); day = cfg['day']
    state_p = HERE / 'state.json'; state = json.load(open(state_p))
    wd = cfg_path.with_suffix(''); wd.mkdir(exist_ok=True)
    comments = sorted(cfg['comments'], key=lambda c: -c['likes'])
    win = comments[0]; build = cfg['build']['name']; kind = cfg['build'].get('kind') or kind_for(build)
    if '--commit' in flags:
        state['followers'] += cfg['new_followers']; state['day'] = day
        state['landmarks'].append({'kind': kind, 'sign': build, 'by': win['by'], 'day': day})
        json.dump(state, open(state_p, 'w'), indent=1); print('state.json updated:', state['followers'], 'followers,', len(state['landmarks']), 'builds'); return
    X = cfg['new_followers']; F0 = state['followers']; total = F0 + X + 1   # + Mango
    V = {l['role']: l for l in make_voice(voice_lines(day, X, total, build), wd)}
    dur = round(V['cta']['e'] + .7, 2)
    shown = sorted(comments[:4], key=lambda c: c['likes']); wi = shown.index(win)   # winner last, so the card scrolls down to it
    ep = dict(day=day, followersBefore=F0, followersNew=X, landmarks=[{'kind': l['kind'], 'sign': l['sign']} for l in state['landmarks']],
              newBuild=dict(kind=kind, sign=build, name=build, by=win['by'], at=round(V['built']['s'] + .15, 2)),
              starts=[0, V['cats']['s'] - .1, V['comment']['s'], V['cta']['s']], milestone=V['comment']['s'] - .1,
              newFrom=V['cats']['s'] + .2, newTo=V['total']['e'], duration=dur, title=f'DAY {day}',
              comments=dict(list=[dict(by=c['by'], text=c['text'], likes=c['likes']) for c in shown], win=wi,
                            t=dict(up=V['comment']['s'], scroll=V['comment']['s'] + .35, stop=V['build']['s'], down=V['built']['s'] + .1)))
    json.dump(ep, open(wd / 'ep.json', 'w'))
    B = build.upper()
    beats = [dict(s=0.05, e=V['cats']['s'], html=f'You asked for<br><y>{B}</y>'),
             dict(s=V['cats']['s'], e=V['comment']['s'], html=f'+{say_n(X)} NEW {"CAT" if X == 1 else "CATS"}' if X else 'Waiting for<br><y>new cats</y>'),
             dict(s=V['built']['s'], e=V['cta']['s'], html='<y>BUILT!</y>'),
             dict(s=V['cta']['s'], e=99, html='Your cat<br><y>moves in next</y>', follow=True, fs=V['cta']['s'] + .4)]
    lines = [dict(s=l['s'], e=l['e'], words=words(l), hide=l['role'] in ('build',)) for l in V.values()]
    json.dump(dict(day=day, duration=dur, pill=True, keepCm=True, beats=beats, lines=lines, tagsFrom=0), open(wd / 'text.json', 'w'))
    json.dump(list(V.values()), open(wd / 'voice.json', 'w'), indent=1)
    env = dict(os.environ, CT_ROOT=str(CT))
    srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8772'], cwd=CT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        if '--test' in flags:
            ts = [0.3, V['cats']['s'] + 1, V['total']['s'], V['comment']['s'] + 1, V['build']['e'], V['built']['s'] + 1, V['cta']['s'] + 1.5]
            subprocess.run(['node', HERE / 'render_day.js', wd, 'test', ','.join(f'{t:.2f}' for t in ts)], env=env, check=True)
            print('test stills in', wd); return
        n = int(dur * 30); shutil.rmtree(wd / 'frames', ignore_errors=True); P = 4
        ps = [subprocess.Popen(['node', HERE / 'render_day.js', wd, str(n * i // P), str(n * (i + 1) // P)], env=env) for i in range(P)]
        if any(p.wait() for p in ps): sys.exit('render failed')
    finally:
        srv.terminate()
    make_audio(V, ep, dur, wd)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', wd / 'frames/f%04d.jpg', '-i', wd / 'mix.wav', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18',
                    '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-shortest', wd / 'video.mp4'], check=True)
    shutil.copy(wd / 'frames/f0015.jpg', wd / 'cover.jpg')
    share = OUT_SHARE / f'day-{day}'
    if OUT_SHARE.exists():
        share.mkdir(exist_ok=True); shutil.copy(wd / 'video.mp4', share / f'cat-town-day{day}.mp4'); shutil.copy(wd / 'cover.jpg', share / f'cat-town-day{day}-cover.jpg')
    a = 'an' if build[0].lower() in 'aeiou' else 'a'
    cap = (f'Day {day} of Cat Town: you asked for {a} {build}, so we built it 🏗️🐱\n'
           f'{say_n(X)} new followers = {say_n(X)} new cats moved in. Cat Town now has {say_n(total)} cats.\n'
           f'Follow to move your cat in. Most-liked comment builds tomorrow 👇 (thanks @{win["by"]}!)\n'
           '#cattown #catsofinstagram #cats #3danimation')
    open(wd / 'caption.txt', 'w').write(cap)
    print('done:', wd / 'video.mp4'); print(cap)


def make_audio(V, ep, dur, wd):
    N = int(SR * dur); mus = np.zeros(N); sfx = np.zeros(N); rng = np.random.default_rng(ep['day'])
    env = lambda n, a=.005, r=.3: np.minimum(1, (np.arange(n) / SR) / a) * np.exp(-(np.arange(n) / SR) / r)
    def add(buf, s, sig, g=1):
        i = int(s * SR); j = min(N, i + len(sig))
        if i < N: buf[i:j] += g * sig[:j - i]
    def tone(f, d, r=.4, a=.005, harm=(1, .5, .25)):
        x = np.arange(int(d * SR)) / SR; return sum(h * np.sin(2 * np.pi * f * (k + 1) * x) for k, h in enumerate(harm)) * env(len(x), a, r)
    mid = lambda n: 440 * 2 ** ((n - 69) / 12)
    def pop(f0=500, f1=1400, d=.12):
        x = np.arange(int(d * SR)) / SR; f = f0 + (f1 - f0) * x / d; return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(x), .002, .05)
    def noise(d, lp=.1):
        n = rng.standard_normal(int(d * SR)); y = np.zeros_like(n)
        for i in range(1, len(n)): y[i] = y[i - 1] + lp * (n[i] - y[i - 1])
        return y
    prog = [[60, 64, 67, 72], [57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67]]; beat = 60 / 104; b = 0; T = 0.0
    while T < dur:
        ch = prog[(b // 4) % 4]; add(mus, T, tone(mid(ch[b % 4] + (12 if b % 8 >= 4 else 0)), 1.2, .35), .16)
        if b % 4 == 0: add(mus, T, tone(mid(ch[0] - 24), 2.4, .9, .02, (1, .3)), .22)
        b += 1; T = b * beat / 2
    X = ep['followersNew']
    for k in range(min(X, 10)):   # pops while the houses come in (rising pitch)
        s = ep['newFrom'] + (ep['newTo'] - ep['newFrom']) * (k + .5) / min(X, 10); f = 500 + 60 * k
        add(sfx, s, pop(f, f * 2.4, .12), .9)
    w = noise(.8); x = np.arange(len(w)) / SR; add(sfx, ep['starts'][2] - .3, w * np.sin(np.pi * x / .8) ** 2, 1.3)
    st = ep['comments']['t']['stop']; add(sfx, st, pop(700, 1700, .14), 1.0)
    bt = ep['newBuild']['at']
    for k, n in enumerate([72, 76, 79, 84, 88]): add(sfx, bt + k * .07, tone(mid(n), .9, .35, .002, (1, .3)), .22)   # fanfare
    for k in range(14): add(sfx, bt + .4 + k * .05, noise(.04, .7) * env(int(.04 * SR), .001, .01), .25)               # confetti crackle
    add(sfx, ep['starts'][3] + .4, pop(700, 1600, .12), .5)
    voc = np.zeros(N)
    for l in V.values():
        a, _ = sf.read(l['wav']); add(voc, l['s'], a)
    vm = np.convolve(np.abs(voc), np.ones(2400) / 2400, 'same'); duck = np.convolve(1 - .7 * np.clip(vm * 12, 0, 1), np.ones(4800) / 4800, 'same')
    mix = voc + .6 * mus * duck + .8 * sfx; mix *= .89 / np.max(np.abs(mix))
    mix[-int(.4 * SR):] *= np.linspace(1, 0, int(.4 * SR))
    sf.write(wd / 'mix_raw.wav', mix, SR)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wd / 'mix_raw.wav', '-af', 'loudnorm=I=-14:TP=-2:LRA=11,alimiter=limit=0.79:level=false', '-ac', '2', '-ar', str(SR), wd / 'mix.wav'], check=True)


if __name__ == '__main__':
    main()
