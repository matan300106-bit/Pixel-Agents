"""Build viewer.html (interactive Cat Town page) from the catcity.html engine.
Usage: python3 build_viewer.py   (run from social/cat-town). Keeps the page shell of the current viewer.html."""
import re, json
s = open('catcity.html').read()
v = open('viewer.html').read(); head = v.split('<script type="module">', 1)[0]
js = s.split('<script type="module">', 1)[1].rsplit('</script>', 1)[0]
def R(a, b):
    global js
    assert a in js, 'missing: ' + a[:80]; js = js.replace(a, b, 1)
R("import * as THREE from 'three';\nimport { mergeGeometries } from './node_modules/three/examples/jsm/utils/BufferGeometryUtils.js';",
  "import * as THREE from 'three';\nimport { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';\nimport { OrbitControls } from 'three/addons/controls/OrbitControls.js';")
js = re.sub(r"const EP = await \(await fetch\(.*?\)\)\.json\(\);", "const EP = window.CITY;", js)
R("const W = 1080, H = 1920;", "const stage = document.getElementById('stage'); let W = stage.clientWidth, H = stage.clientHeight;")
R("renderer.setSize(W, H); renderer.setPixelRatio(1);", "renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2)); renderer.setSize(W, H);")
R("document.body.prepend(renderer.domElement);", "stage.appendChild(renderer.domElement);")
R("sun.shadow.mapSize.set(4096, 4096);", "sun.shadow.mapSize.set(2048, 2048);")
LOOP = open('viewer_loop.js').read()
R("await document.fonts.ready;\nwindow.ready = true;", LOOP)
data = {"day": 1, "followersBefore": 0, "followersNew": 5000, "order": "index", "newFrom": 0, "newTo": 100, "noReserved": True, "dayRange": [1, 150], "landmarks": []}
for k, sg, f in [("petshop", "PETME2 Pet Shop", 10), ("cafe", "Cat Café", 40), ("statue", "Mango Statue", 70), ("cityhall", "City Hall", 100), ("market", "Fish Market", 250),
                 ("pool", "Cat Pool", 500), ("custom", "Cat Airport", 900), ("custom", "Cat Cinema", 1400), ("custom", "Cat Stadium", 2000), ("cafe", "Sushi Bar", 2700), ("custom", "Cat School", 3500), ("market", "Toy Store", 4300)]:
    data["landmarks"].append({"kind": k, "sign": sg, "at": 100 * ((f - .5) / 5000) ** .8})
head = re.sub(r"<script>window.CITY = .*?</script>", lambda m: "<script>window.CITY = " + json.dumps(data, ensure_ascii=False) + ";</script>", head, flags=re.S)
open('viewer.html', 'w').write(head + '<script type="module">' + js + '</script>\n')
print('viewer.html built', len(head + js), 'bytes')
