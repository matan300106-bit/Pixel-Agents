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
LIVE_JS = """const EP = window.CITY;
if (EP.live) {   // live town: residents come from the page metafield (window.CITY_LIVE = { start: 'YYYY-MM-DD', residents: [{ name, ig, tt, day }], updated: ISO time })
  const L = window.CITY_LIVE || {}, R = (Array.isArray(L.residents) ? L.residents : []).filter(r => r && (r.name || r.ig || r.tt));
  const st = new Date((L.start || '') + 'T00:00:00'), dn = isNaN(st) ? 1 : Math.floor((Date.now() - st) / 864e5) + 1;
  EP.live.residents = R; EP.live.updated = L.updated || ''; EP.live.followers = R.length; EP.live.day = Math.max(1, dn); EP.followersNew = Math.max(EP.followersNew || 0, R.length); }"""
js = js.replace("const EP = window.CITY;", LIVE_JS, 1)
R("const W = 1080, H = 1920;", "const stage = document.getElementById('stage'); let W = stage.clientWidth, H = stage.clientHeight;")
R("renderer.setSize(W, H); renderer.setPixelRatio(1);", "renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, LITE ? 1.25 : 2)); renderer.setSize(W, H);")
R("document.body.prepend(renderer.domElement);", "stage.appendChild(renderer.domElement);")
R("sun.shadow.mapSize.set(4096, 4096);", "sun.shadow.mapSize.set(2048, 2048);")
LOOP = open('viewer_loop.js').read()
R("await document.fonts.ready;\nwindow.ready = true;", LOOP)
data = {"live": {"followers": 0}, "pad": False, "shopCards": False, "day": 1, "followersBefore": 0, "followersNew": 1000, "order": "index", "newFrom": 0, "newTo": 100, "noReserved": True, "dayRange": [1, 40], "landmarks": []}
# Real top-comment builds (always there, first spots = right in front of Mango). Day 2: "add a fish supermarket" by PIKA.
for k, sg, note in [("fishmarket", "Fish Supermarket", "Top comment on Day 2, idea by PIKA")]:
    data["landmarks"].append({"kind": k, "sign": sg, "at": 0, "note": note})
for k, sg, f in [("petshop", "PETME2 Pet Shop", 10), ("cafe", "Cat Café", 40), ("statue", "Mango Statue", 70), ("cityhall", "City Hall", 100), ("market", "Toy Market", 250),
                 ("pool", "Cat Pool", 400), ("custom", "Cat Airport", 700), ("custom", "Cat Cinema", 900)]:
    data["landmarks"].append({"kind": k, "sign": sg, "at": 100 * ((f - .5) / 1000) ** .8, "unlock": f})
head = re.sub(r"<script>window.CAT_VIEWER.*?</script>|<script>window.CITY = .*?</script>", lambda m: "<script>window.CAT_VIEWER = true; window.CAT_LITE = matchMedia('(pointer: coarse)').matches || innerWidth < 820; window.CITY = " + json.dumps(data, ensure_ascii=False) + ";</script>", head, flags=re.S)
if '.info__shop' not in head:
    head = head.replace("  .info__note {", "  .info__shop { display: inline-block; margin-top: 10px; padding: 8px 14px; border-radius: 999px; background: var(--brand); color: #fff; font-weight: 800; font-size: 13px; text-decoration: none; }\n  .info__note {", 1)
# Escape every non-ASCII character so symbols never break, whatever charset the server sends.
def esc_html(t): return ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in t)
def esc_js(t): return ''.join(c if ord(c) < 128 else ''.join('\\u%04x' % u for u in __import__('struct').unpack('<%dH' % (len(c.encode('utf-16-le')) // 2), c.encode('utf-16-le'))) for c in t)
def esc_page(h):
    parts = re.split(r'(<script\b[^>]*>.*?</script>)', h, flags=re.S)
    return ''.join(esc_js(x) if x.startswith('<script') else esc_html(x) for x in parts)
open('viewer.html', 'w').write(esc_page(head) + '<script type="module">' + esc_js(js) + '</script>\n')
print('viewer.html built', len(head + js), 'bytes')
