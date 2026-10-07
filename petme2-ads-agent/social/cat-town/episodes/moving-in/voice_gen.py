# Kokoro TTS (free, local) -> lNN.wav (trimmed, 48 kHz) + lines.json with durations.
# usage (in the work dir): python3 voice_gen.py in.json   items: {show, say} or {show, ph} (raw phonemes, for the long "Soooo")
import json, subprocess, soundfile as sf, sys
from kokoro_onnx import Kokoro
k = Kokoro('/tmp/tts/kokoro-v1.0.onnx', '/tmp/tts/voices-v1.0.bin')
out = []
for i, l in enumerate(json.load(open(sys.argv[1]))):
    a, sr = k.create(l.get('ph') or l['say'], voice=sys.argv[2] if len(sys.argv) > 2 else 'af_heart', speed=float(sys.argv[3]) if len(sys.argv) > 3 else 1.05, lang='en-us', is_phonemes='ph' in l)
    sf.write(f'raw{i:02d}.wav', a, sr)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'raw{i:02d}.wav','-af','silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse','-ar','48000','-ac','1',f'l{i:02d}.wav'],check=True)
    out.append({'i': i, 'text': l['show'], 'dur': round(sf.info(f'l{i:02d}.wav').duration, 3)})
print(json.dumps(out))
json.dump(out, open('lines.json','w'))
