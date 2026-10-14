# Day 8: a deep movie-trailer narrator (bm_george) + Mango (af_heart). lines_in.json = [[text, voice, speed], ...] -> lNN.wav + lines.json (run in the work dir)
import json, subprocess, soundfile as sf, sys
from kokoro_onnx import Kokoro
k = Kokoro('/tmp/tts/kokoro.onnx', '/tmp/tts/voices.bin')
L = json.load(open(sys.argv[1])); out = []
for i, (text, voice, speed) in enumerate(L):
    a, sr = k.create(text, voice=voice, speed=speed, lang='en-gb' if voice.startswith('b') else 'en-us')
    sf.write(f'raw{i:02d}.wav', a, sr)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'raw{i:02d}.wav','-af','silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse','-ar','48000','-ac','1',f'l{i:02d}.wav'],check=True)
    out.append({'i': i, 'text': text, 'voice': voice, 'dur': round(sf.info(f'l{i:02d}.wav').duration, 3)})
for o in out: print(o['i'], o['dur'], o['text'])
json.dump(out, open('lines.json','w'))
