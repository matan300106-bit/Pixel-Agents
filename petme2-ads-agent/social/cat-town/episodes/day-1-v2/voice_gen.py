import json, soundfile as sf
from kokoro_onnx import Kokoro
k = Kokoro('kokoro.onnx', 'voices.bin')
lines = ["This is Mango.", "He's the only cat in this town.", "No neighbors. No friends.", "He has water, and food,", "but nobody to share it with.", "So here's the deal:", "every new follow brings one more cat.", "With its own little house,", "and your name on it.", "The goal?", "This.", "Today?", "One cat.", "Follow to be Mango's first neighbor."]
out = []
for i, l in enumerate(lines):
    a, sr = k.create(l, voice='af_heart', speed=1.12, lang='en-us')
    sf.write(f'l{i:02d}.wav', a, sr); out.append({'i': i, 'text': l, 'dur': round(len(a)/sr, 3)})
json.dump(out, open('lines.json', 'w'), indent=1); print(json.dumps(out))
