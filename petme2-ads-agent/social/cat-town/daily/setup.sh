#!/bin/sh
# One-time setup in a fresh cloud container: three.js + fonts + playwright for the engine, Kokoro voice (free, local).
set -e
cd "$(dirname "$0")/.."
[ -d node_modules/three ] || npm i --no-save three@0.170.0 @fontsource/nunito playwright >/dev/null
pip install -q kokoro-onnx soundfile numpy 2>/dev/null
K=${KOKORO_DIR:-/tmp/tts}; mkdir -p $K
[ -s $K/kokoro.onnx ] || curl -sSL -o $K/kokoro.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx
[ -s $K/voices.bin ] || curl -sSL -o $K/voices.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
echo "Cat Town daily: ready"
