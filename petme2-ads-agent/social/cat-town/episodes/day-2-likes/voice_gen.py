import json, subprocess, soundfile as sf, sys
from kokoro_onnx import Kokoro
k = Kokoro('/tmp/tts/kokoro.onnx', '/tmp/tts/voices.bin')
L = json.load(open(sys.argv[1]))
out = []
for i, l in enumerate(L):
    a, sr = k.create(l, voice='af_heart', speed=1.12, lang='en-us')
    sf.write(f'raw{i:02d}.wav', a, sr)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'raw{i:02d}.wav','-af','silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse','-ar','48000','-ac','1',f'l{i:02d}.wav'],check=True)
    out.append({'i': i, 'text': l, 'dur': round(sf.info(f'l{i:02d}.wav').duration, 3)})
print(json.dumps(out, indent=0))
json.dump(out, open('lines.json','w'))
