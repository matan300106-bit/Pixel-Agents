# Day 9: narrator (bm_george), Mango (af_heart), the dog general (am_onyx, pitched down = a growly villain). lines_in.json = [[text, voice, speed], ...] -> lNN.wav + lines.json (run in the work dir)
import json, subprocess, soundfile as sf, sys
from kokoro_onnx import Kokoro
k = Kokoro('/tmp/tts/kokoro.onnx', '/tmp/tts/voices.bin')
L = json.load(open(sys.argv[1])); out = []
TRIM = 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse'
for i, (text, voice, speed) in enumerate(L):
    a, sr = k.create(text, voice=voice, speed=speed, lang='en-gb' if voice.startswith('b') else 'en-us')
    sf.write(f'raw{i:02d}.wav', a, sr)
    fx = f'asetrate={sr}*0.84,aresample={sr},atempo=1.08,bass=g=6,' if voice == 'am_onyx' else ''   # the general: lower + heavier
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'raw{i:02d}.wav','-af',fx + TRIM,'-ar','48000','-ac','1',f'l{i:02d}.wav'],check=True)
    out.append({'i': i, 'text': text, 'voice': voice, 'dur': round(sf.info(f'l{i:02d}.wav').duration, 3)})
for o in out: print(o['i'], o['dur'], o['text'])
json.dump(out, open('lines.json','w'))
