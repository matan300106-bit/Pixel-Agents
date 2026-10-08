// PETME2 Cat Town – live, view-only 3D town (petme2.com/pages/cat-town).
// Town data comes from the page metafield custom.town_state (updated daily from social/cat-town/town-state.json).
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.170.0/+esm';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/controls/OrbitControls.js/+esm';

export function mountCatTown(root, ST) {
  const canvasWrap = root.querySelector('[data-town-canvas]');
  const tip = root.querySelector('[data-town-tip]');
  const W = () => canvasWrap.clientWidth, H = () => canvasWrap.clientHeight;

  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(W(), H());
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  canvasWrap.appendChild(renderer.domElement);

  const scene = new THREE.Scene();
  scene.background = new THREE.Color('#BFE3FF');
  scene.fog = new THREE.Fog('#BFE3FF', 70, 160);
  const camera = new THREE.PerspectiveCamera(38, W() / H(), 0.1, 400);
  const R = ST.islandRadius || 9;
  const k = (R / 9) * Math.max(1, 0.85 / (W() / H()));   // phones: step back so the whole island fits
  camera.position.set(-14 * k, 26 * k, 34 * k);

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.target.set(0, 0, 0);
  controls.enableDamping = true; controls.enablePan = false;
  controls.minDistance = 10; controls.maxDistance = 70 * k;
  controls.maxPolarAngle = Math.PI * 0.46; controls.minPolarAngle = Math.PI * 0.12;
  controls.autoRotate = true; controls.autoRotateSpeed = 0.6;
  let idle;
  controls.addEventListener('start', () => { controls.autoRotate = false; clearTimeout(idle); });
  controls.addEventListener('end', () => { idle = setTimeout(() => (controls.autoRotate = true), 6000); });

  scene.add(new THREE.HemisphereLight('#ffffff', '#9CC7A2', 1.1));
  const sun = new THREE.DirectionalLight('#fff4e0', 2.0);
  sun.position.set(14, 26, 12); sun.castShadow = true; sun.shadow.mapSize.set(2048, 2048);
  Object.assign(sun.shadow.camera, { left: -R - 4, right: R + 4, top: R + 4, bottom: -R - 4 });
  scene.add(sun);

  const mats = {};
  const flat = c => mats[c] || (mats[c] = new THREE.MeshStandardMaterial({ color: c, flatShading: true, roughness: .9 }));
  const mesh = (g, c, cast = true) => { const m = new THREE.Mesh(g, flat(c)); m.castShadow = cast; m.receiveShadow = true; return m; };
  const B = (w, h, d) => new THREE.BoxGeometry(w, h, d);
  const Cyl = (a, b, h, s = 12) => new THREE.CylinderGeometry(a, b, h, s);

  // island
  const sea = mesh(Cyl(R * 6, R * 6, .4, 48), '#7CC4F2', false); sea.position.y = -1.4; scene.add(sea);
  const town = new THREE.Group(); scene.add(town);
  const grass = mesh(Cyl(R, R + .4, 1, 12), '#8FD07A'); grass.position.y = -.5; town.add(grass);
  const cliff = mesh(Cyl(R + .4, R * .82, 2.4, 12), '#C99A6B'); cliff.position.y = -2.2; town.add(cliff);
  const plaza = mesh(Cyl(2.6, 2.6, .12, 10), '#EDE4D3'); plaza.position.y = .02; town.add(plaza);
  (ST.trees || []).forEach(t => {
    const g = new THREE.Group(), s = t.s;
    const trunk = mesh(Cyl(.15 * s, .2 * s, 1 * s, 6), '#8A5A3B'); trunk.position.y = .5 * s; g.add(trunk);
    const top = mesh(new THREE.ConeGeometry(.8 * s, 1.8 * s, 7), '#4FA65A'); top.position.y = 1.7 * s; g.add(top);
    g.position.set(t.x, 0, t.z); town.add(g);
  });

  function textSign(text) {
    const c = document.createElement('canvas'); c.width = 512; c.height = 128;
    const g = c.getContext('2d'); g.fillStyle = '#FFFFFF'; g.fillRect(0, 0, 512, 128);
    g.fillStyle = '#2F5FE0'; g.font = '900 52px Nunito, Arial, sans-serif'; g.textAlign = 'center'; g.textBaseline = 'middle';
    let s = String(text).toUpperCase(); while (g.measureText(s).width > 480 && s.length > 4) s = s.slice(0, -2);
    g.fillText(s, 256, 66);
    const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace;
    return new THREE.Mesh(new THREE.PlaneGeometry(2.4, .6), new THREE.MeshBasicMaterial({ map: tex, side: THREE.DoubleSide }));
  }

  function makeCat(color) {
    const c = new THREE.Group();
    const b = mesh(B(.5, .45, .9), color); b.position.y = .45; c.add(b);
    const h = mesh(B(.48, .42, .42), color); h.position.set(0, .82, .5); c.add(h);
    [-.15, .15].forEach(x => { const e = mesh(new THREE.ConeGeometry(.1, .2, 4), color); e.position.set(x, 1.12, .48); c.add(e); });
    [-.1, .1].forEach(x => { const eye = mesh(B(.06, .08, .02), '#1B2333', false); eye.position.set(x, .86, .72); c.add(eye); });
    const tail = mesh(B(.1, .1, .6), color); tail.position.set(0, .75, -.6); tail.rotation.x = -.7; c.add(tail); c.userData.tail = tail;
    const legs = [];
    [[-.16, .3], [.16, .3], [-.16, -.3], [.16, -.3]].forEach(([x, z]) => { const l = mesh(B(.12, .3, .12), color); l.position.set(x, .15, z); c.add(l); legs.push(l); });
    c.userData.legs = legs; return c;
  }

  function building(b) {
    const g = new THREE.Group(), kd = b.kind;
    if (kd === 'fountain') {
      const base = mesh(Cyl(1.1, 1.2, .35, 16), '#E7EDF7'); base.position.y = .18; g.add(base);
      const water = mesh(Cyl(.95, .95, .06, 16), '#5AB3F0', false); water.position.y = .38; g.add(water);
      const stem = mesh(Cyl(.18, .22, .8, 10), '#2F5FE0'); stem.position.y = .75; g.add(stem);
      const bowl = mesh(Cyl(.55, .3, .25, 14), '#FFFFFF'); bowl.position.y = 1.2; g.add(bowl);
      g.userData.drops = [];
      for (let i = 0; i < 26; i++) { const d = mesh(new THREE.SphereGeometry(.06, 6, 6), '#7FD0FF', false); d.userData.phase = i / 26; g.add(d); g.userData.drops.push(d); }
    } else if (kd === 'cafe') {
      const body = mesh(B(3, 1.8, 2.2), '#FFF4E6'); body.position.y = .9; g.add(body);
      for (let i = 0; i < 6; i++) { const s = mesh(B(.5, .12, .9), i % 2 ? '#FFFFFF' : '#E85D5D'); s.position.set(-1.25 + i * .5, 1.65, 1.45); s.rotation.x = .45; g.add(s); }
      const cup = mesh(Cyl(.3, .24, .45, 12), '#FFFFFF'); cup.position.set(0, 2.15, 0); g.add(cup);
    } else if (kd === 'market') {
      const stall = mesh(B(3, .9, 1.6), '#C98B5A'); stall.position.y = .45; g.add(stall);
      const roof = mesh(B(3.3, .12, 2), '#2F5FE0'); roof.position.y = 2.1; roof.rotation.x = -.15; g.add(roof);
      [[-1.4, .7], [1.4, .7], [-1.4, -.7], [1.4, -.7]].forEach(([x, z]) => { const p = mesh(Cyl(.06, .06, 1.6, 6), '#8A5A3B'); p.position.set(x, 1.2, z); g.add(p); });
    } else if (kd === 'cattree') {
      const post = mesh(Cyl(.22, .26, 4.2, 8), '#D9C2A3'); post.position.y = 2.1; g.add(post);
      [[.9, 1.2], [2.0, .9], [3.1, 1.1], [4.2, 1.3]].forEach(([y, r], i) => { const p = mesh(Cyl(r, r, .18, 10), i % 2 ? '#2F5FE0' : '#8FA9D9'); p.position.set(i % 2 ? .4 : -.4, y, 0); g.add(p); });
    } else if (kd === 'statue') {
      const ped = mesh(B(1.4, 1, 1.4), '#E7EDF7'); ped.position.y = .5; g.add(ped);
      const cat = makeCat('#FFC93C'); cat.scale.setScalar(2.2); cat.position.y = 1; g.add(cat);
    } else if (kd === 'pool') {
      const rim = mesh(B(3.4, .3, 2.4), '#E7EDF7'); rim.position.y = .15; g.add(rim);
      const w = mesh(B(3, .08, 2), '#5AB3F0', false); w.position.y = .32; g.add(w);
    } else if (kd === 'tower') {
      const t = mesh(B(2, 6, 2), '#FFFFFF'); t.position.y = 3; g.add(t);
      const top = mesh(new THREE.ConeGeometry(1.5, 1.2, 4), '#2F5FE0'); top.position.y = 6.6; top.rotation.y = Math.PI / 4; g.add(top);
    } else if (kd === 'vet') {
      const body = mesh(B(3, 2, 2.2), '#FFFFFF'); body.position.y = 1; g.add(body);
      const c1 = mesh(B(.9, .28, .06), '#E85D5D'); c1.position.set(0, 1.4, 1.12); g.add(c1);
      const c2 = mesh(B(.28, .9, .06), '#E85D5D'); c2.position.set(0, 1.4, 1.12); g.add(c2);
    } else if (kd === 'park') {
      const lawn = mesh(Cyl(1.8, 1.8, .1, 14), '#6FC06A'); lawn.position.y = .06; g.add(lawn);
      const ball = mesh(new THREE.IcosahedronGeometry(.35, 0), '#E85D5D'); ball.position.set(.6, .4, .4); g.add(ball);
    } else {
      const body = mesh(B(3, 2.2, 2.4), '#FFFFFF'); body.position.y = 1.1; g.add(body);
      const roof = mesh(new THREE.ConeGeometry(2.4, 1.3, 4), '#FFC93C'); roof.position.y = 2.85; roof.rotation.y = Math.PI / 4; g.add(roof);
    }
    if (b.sign) { const s = textSign(b.sign); s.position.set(0, kd === 'tower' ? 7.6 : 3.4, 0); g.add(s); g.userData.sign = s; }
    return g;
  }

  const pickables = [];
  (ST.houses || []).forEach((hh, i) => {
    const h = new THREE.Group();
    const body = mesh(B(1.8, 1.4, 1.6), hh.wall); body.position.y = .7; h.add(body);
    const r = mesh(new THREE.ConeGeometry(1.55, 1, 4), hh.roof); r.position.y = 1.9; r.rotation.y = Math.PI / 4; h.add(r);
    const door = mesh(B(.5, .75, .06), '#1B2333'); door.position.set(0, .38, .81); h.add(door);
    [-.55, .55].forEach(x => { const w = mesh(B(.35, .35, .05), '#9FD3FF'); w.position.set(x, .95, .81); h.add(w); });
    h.position.set(hh.x, 0, hh.z); h.rotation.y = hh.ry; town.add(h);
    h.userData.info = `House #${i + 1} · moved in on Day ${hh.day}`;
    pickables.push(h);
  });
  const builds = (ST.buildings || []).map(bb => {
    const g = building(bb); g.position.set(bb.x, 0, bb.z); g.rotation.y = bb.ry || 0; town.add(g);
    g.userData.info = bb.by ? `Day ${bb.day}: built for ${bb.by}${bb.request ? ` — “${bb.request}”` : ''}` : `Day ${bb.day}: ${bb.sign || 'fresh water fountain'}`;
    pickables.push(g); return g;
  });
  const cats = (ST.cats || []).map((cc, i) => { const c = makeCat(cc.color); c.userData.home = cc; c.userData.i = i; town.add(c); return c; });

  // tap / hover to see who built what (view only – nothing can be changed)
  const ray = new THREE.Raycaster(), ptr = new THREE.Vector2();
  function pick(ev) {
    const rect = renderer.domElement.getBoundingClientRect();
    ptr.set(((ev.clientX - rect.left) / rect.width) * 2 - 1, -((ev.clientY - rect.top) / rect.height) * 2 + 1);
    ray.setFromCamera(ptr, camera);
    const hit = ray.intersectObjects(pickables, true)[0];
    if (!hit) { tip.hidden = true; return; }
    let o = hit.object; while (o && !o.userData.info) o = o.parent;
    tip.textContent = o.userData.info; tip.hidden = false;
    tip.style.left = Math.min(ev.clientX - rect.left + 12, rect.width - 260) + 'px';
    tip.style.top = Math.max(ev.clientY - rect.top - 40, 8) + 'px';
  }
  renderer.domElement.addEventListener('click', pick);

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) controls.autoRotate = false;
  const clock = new THREE.Clock();
  function frame() {
    const t = clock.getElapsedTime();
    cats.forEach(c => {
      const u = c.userData.home, i = c.userData.i, a = t * .5 + i * 1.7;
      c.position.set(u.x + Math.sin(a) * .6, 0, u.z + Math.cos(a * .8) * .4);
      c.rotation.y = Math.atan2(Math.cos(a) * .6, -Math.sin(a * .8) * .32);
      c.userData.legs.forEach((l, j) => (l.rotation.x = Math.sin(t * 13 + (j % 2) * Math.PI + i) * .45));
      c.userData.tail.rotation.z = Math.sin(t * 4 + i) * .3;
    });
    builds.forEach(b => {
      if (b.userData.drops) b.userData.drops.forEach(d => { const p = (t * .9 + d.userData.phase) % 1, a = d.userData.phase * Math.PI * 2, rr = .2 + p * .75; d.position.set(Math.cos(a) * rr, 1.35 + p * .5 - p * p * 1.3, Math.sin(a) * rr); });
      if (b.userData.sign) b.userData.sign.lookAt(camera.position.x, b.userData.sign.getWorldPosition(new THREE.Vector3()).y, camera.position.z);
    });
    controls.update();
    renderer.render(scene, camera);
    requestAnimationFrame(frame);
  }
  frame();
  new ResizeObserver(() => { renderer.setSize(W(), H()); camera.aspect = W() / H(); camera.updateProjectionMatrix(); }).observe(canvasWrap);
}
