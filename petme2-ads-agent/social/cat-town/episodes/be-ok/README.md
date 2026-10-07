# "Be OK" trend video (19 s, captions only)

Matan (Oct 7): funny video for adults; a trend check (Later Oct 2, NewEngen Oct 5) picked the "Be OK" format: Mango dances happily while the captions admit the mess. All 3 city rules kept.
Engine (opt-in, `catcity.html`): `EP.dance = { bpm, stop }` (Mango bounces facing the camera with a happy face, freezes at stop), `EP.bonk` (a fish falls on Mango's head),
`EP.strays.rain` (strays fall from the sky around the square), `EP.strays.shopAt` (they jump to packed spots on the fish supermarket: roof, awning, counters, doorway), `EP.strays.peek` (one grey cat slides in next to Mango).
Final: project files `cat-town/be-ok/`. Not posted.
Build: scratch server on :8772 (three@0.170.0, @fontsource/nunito, playwright, copy of catcity.html), work dir `beok`: `python3 mk.py beok` once to get the shop spot from `node render.js beok test 1` (prints it; save as beok/shop.json), then `python3 mk.py . shop`, `python3 text.py .`, `python3 audio.py .`, `node render.js beok range 0 570` (split in 3), ffmpeg mux (libx264 crf 18 + aac 192k).
