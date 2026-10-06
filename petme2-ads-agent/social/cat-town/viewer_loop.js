window.__noCam = true;
const controls = new OrbitControls(camera, renderer.domElement);
controls.target.set(-10, 2, 0); if (innerWidth < 700) camera.position.set(150, 125, 165); else camera.position.set(190, 100, 150);
controls.enableDamping = true; controls.maxPolarAngle = Math.PI * .47; controls.minDistance = 12; controls.maxDistance = 900;
controls.autoRotate = true; controls.autoRotateSpeed = .35; renderer.domElement.addEventListener('pointerdown', () => { controls.autoRotate = false; });
const fit = () => { W = stage.clientWidth; H = stage.clientHeight; renderer.setSize(W, H); camera.aspect = W / H; camera.fov = W / H < .8 ? 55 : 42; camera.updateProjectionMatrix(); };
addEventListener('resize', fit); fit();
const slider = $('grow'), FMAX = +slider.max, tOf = f => f <= 0 ? -1 : EP.newFrom + (EP.newTo - EP.newFrom) * Math.pow((f - .5) / FN, .8) + 1e-6;
let target = +slider.value, cur = target, playing = false, ANIM = 0;
const setPlay = on => { playing = on; $('play').textContent = on ? 'Pause' : 'Play growth'; };
slider.addEventListener('input', () => { target = +slider.value; setPlay(false); });
document.querySelectorAll('[data-f]').forEach(b => b.addEventListener('click', () => { target = +b.dataset.f; slider.value = target; setPlay(false); }));
$('play').addEventListener('click', () => { if (playing) return setPlay(false); if (cur >= FMAX - 1) cur = 0; setPlay(true); });
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches; if (reduce) controls.autoRotate = false;
let last = performance.now(), onScreen = true;
// phones: draw at most 30 frames a second; everywhere: stop drawing while the city is scrolled off screen or the tab is hidden
new IntersectionObserver(es => { onScreen = es[0].isIntersecting; }, { threshold: 0.01 }).observe(stage);
const FRAME_MS = LITE ? 33 : 0;
function loop(now) { requestAnimationFrame(loop); if (!onScreen || document.hidden || now - last < FRAME_MS) return;
  const dt = Math.min(.05, (now - last) / 1000); last = now; ANIM += reduce ? 0 : dt;
  if (playing) { cur = Math.min(FMAX, cur + Math.max(4, cur * .35) * dt * 2.2); target = cur; slider.value = Math.round(cur); if (cur >= FMAX) setPlay(false); }
  else cur += (target - cur) * Math.min(1, dt * 8);
  if (Math.abs(target - cur) < .5) cur = target;
  slider.setAttribute('aria-valuetext', Math.round(cur) + ' followers');
  navStep(now, dt); controls.update(); window.renderFrame(tOf(Math.round(cur)), ANIM); }

// ---------- move around like a game: D-pad, + / -, back to the center, arrow keys, double-tap to fly there ----------
controls.touches = { ONE: THREE.TOUCH.ROTATE, TWO: THREE.TOUCH.DOLLY_PAN };
const UP = new THREE.Vector3(0, 1, 0), GROUND = new THREE.Plane(UP, 0), NV = new THREE.Vector3(), NV2 = new THREE.Vector3();
let FLY = null, HOLD = null;   // FLY: eased camera flight; HOLD: a D-pad button held down (continuous move)
const tick = () => { try { navigator.vibrate?.(8); } catch (e) {} };
const stopSpin = () => { controls.autoRotate = false; };
const clampT = v => { const R = 1.3 * (window.__CR || 300), d = Math.hypot(v.x, v.z); if (d > R) { v.x *= R / d; v.z *= R / d; } return v; };
const groundDir = (dx, dz, out) => { NV.subVectors(controls.target, camera.position).setY(0); if (NV.lengthSq() < 1e-6) NV.set(0, 0, -1); NV.normalize();   // dz: forward on screen, dx: right
  NV2.crossVectors(NV, UP).normalize(); return out.set(0, 0, 0).addScaledVector(NV, dz).addScaledVector(NV2, dx); };
function flyTo(tgt, pos, dur) { clampT(tgt); const off = pos.clone().sub(tgt), d = THREE.MathUtils.clamp(off.length(), controls.minDistance, controls.maxDistance); pos = tgt.clone().add(off.setLength(d));
  if (reduce || !dur) { FLY = null; controls.target.copy(tgt); camera.position.copy(pos); return; }
  FLY = { t0: performance.now(), dur: dur * 1000, a: controls.target.clone(), b: tgt, pa: camera.position.clone(), pb: pos }; }
function panStep(dx, dz) { stopSpin(); const dist = camera.position.distanceTo(controls.target), m = groundDir(dx, dz, new THREE.Vector3()).multiplyScalar(dist * .25);
  const base = FLY ? FLY.b : controls.target, basePos = FLY ? FLY.pb : camera.position;
  const tgt = clampT(base.clone().add(m)); flyTo(tgt, basePos.clone().add(tgt.clone().sub(base)), .3); }
function zoomStep(f) { stopSpin(); const base = FLY ? FLY.b : controls.target, basePos = FLY ? FLY.pb : camera.position; flyTo(base.clone(), base.clone().add(basePos.clone().sub(base).multiplyScalar(f)), .3); }
function goHome() { stopSpin(); const off = camera.position.clone().sub(controls.target).setLength(75); if (off.y < 25) off.setY(25).setLength(75); flyTo(new THREE.Vector3(0, 4, 0), new THREE.Vector3(0, 4, 0).add(off), .8); }
const MARK = new THREE.Mesh(new THREE.RingGeometry(.75, 1, 40).rotateX(-Math.PI / 2), new THREE.MeshBasicMaterial({ color: '#FFC93C', transparent: true, opacity: 0, depthWrite: false })); MARK.visible = false; MARK.renderOrder = 2; scene.add(MARK);
let markT = -1;
function navStep(now, dt) {
  if (HOLD && now - HOLD.t0 > 300) { FLY = null; const dist = camera.position.distanceTo(controls.target), sp = Math.min(1, (now - HOLD.t0 - 300) / 400) * dist * .85 * dt;   // held: keep moving, ramping up
    if (HOLD.zoom) { const f = Math.pow(HOLD.zoom, dt * 3.3), off = camera.position.clone().sub(controls.target).multiplyScalar(f); off.setLength(THREE.MathUtils.clamp(off.length(), controls.minDistance, controls.maxDistance)); camera.position.copy(controls.target).add(off); }
    else { const m = groundDir(HOLD.dx, HOLD.dz, NV.clone()).multiplyScalar(sp), before = controls.target.clone(); clampT(controls.target.add(m)); camera.position.add(controls.target.clone().sub(before)); } }
  if (FLY) { const k = Math.min(1, (now - FLY.t0) / FLY.dur), e = k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
    controls.target.lerpVectors(FLY.a, FLY.b, e); camera.position.lerpVectors(FLY.pa, FLY.pb, e); if (k >= 1) FLY = null; }
  if (markT >= 0) { const k = (now - markT) / 800; if (k >= 1) { MARK.visible = false; markT = -1; } else { const sc = 1 + 5 * k; MARK.scale.set(sc, 1, sc); MARK.material.opacity = .9 * (1 - k); } } }
const PAD = { up: [0, 1], down: [0, -1], left: [-1, 0], right: [1, 0] };
document.querySelectorAll('[data-nav]').forEach(b => {
  const act = b.dataset.nav, mv = PAD[act], zf = act === 'in' ? .7 : act === 'out' ? 1 / .7 : 0;
  const end = () => { HOLD = null; b.classList.remove('is-down'); };
  b.addEventListener('pointerdown', e => { e.preventDefault(); b.classList.add('is-down'); tick();
    if (mv) { panStep(mv[0], mv[1]); HOLD = { t0: performance.now(), dx: mv[0], dz: mv[1] }; }
    else if (zf) { zoomStep(zf); HOLD = { t0: performance.now(), zoom: zf }; }
    else goHome();
    try { b.setPointerCapture(e.pointerId); } catch (er) {} });
  ['pointerup', 'pointercancel', 'lostpointercapture'].forEach(ev => b.addEventListener(ev, end));
  b.addEventListener('click', e => { if (e.detail === 0) { if (mv) panStep(mv[0], mv[1]); else if (zf) zoomStep(zf); else goHome(); } });   // keyboard Enter / Space
});
addEventListener('keydown', e => { const tg = e.target; if (tg && (tg.tagName === 'INPUT' || tg.tagName === 'TEXTAREA' || tg.isContentEditable)) return;
  if (!pcBox.hidden) return;
  const k = e.key, mv = { ArrowUp: [0, 1], ArrowDown: [0, -1], ArrowLeft: [-1, 0], ArrowRight: [1, 0] }[k];
  if (mv) { e.preventDefault(); panStep(mv[0], mv[1]); } else if (k === '+' || k === '=') { e.preventDefault(); zoomStep(.7); } else if (k === '-' || k === '_') { e.preventDefault(); zoomStep(1 / .7); } });
renderer.domElement.addEventListener('dblclick', e => e.preventDefault());
const syncDock = () => { const d = document.querySelector('.dock'); if (d) stage.parentElement.style.setProperty('--dockH', d.offsetHeight + 'px'); };
addEventListener('resize', syncDock); syncDock();
{ const hint = $('hint'); let seen = false; try { seen = localStorage.getItem('catTownHintSeen') === '1'; } catch (e) {}
  if (hint && !seen) { hint.hidden = false; requestAnimationFrame(() => hint.classList.add('is-on'));
    setTimeout(() => { hint.classList.remove('is-on'); setTimeout(() => { hint.hidden = true; }, 500); }, 4000); try { localStorage.setItem('catTownHintSeen', '1'); } catch (e) {} } }
window.__screenOf = (x, y, z) => { const v = new THREE.Vector3(x, y, z).project(camera), r = renderer.domElement.getBoundingClientRect(); return [r.left + (v.x + 1) / 2 * r.width, r.top + (1 - v.y) / 2 * r.height]; };   // test helper
window.__ffPos = () => [FT.g.position.toArray(), FD.g.position.toArray()];
window.__cam = () => ({ pos: camera.position.toArray().map(v => +v.toFixed(2)), target: controls.target.toArray().map(v => +v.toFixed(2)) });

// ---------- tap a house or a building: who lives there / what it is ----------
const PICK = new Map();   // instanced mesh -> (instance index -> house number)
Object.values(HP).forEach(m => PICK.set(m, new Int32Array(Math.max(1, m.count)).fill(-1)));
houseParts.forEach((p, n) => p.forEach(([m, i]) => { const a = PICK.get(m); if (a) a[i] = n; }));
const HA = ['whisker', 'mochi', 'purr', 'biscuit', 'tuna', 'nap', 'beans', 'meow', 'sushi', 'luna', 'ziggy', 'socks', 'paws', 'zoomie', 'loaf', 'noodle'], HB2 = ['lover', 'queen', 'king', 'club', 'squad', 'daily', 'world', 'fan', 'life', 'mom', 'dad', 'bestie'];
const handleOf = n => (EP.handles && EP.handles[n]) || ('demo.' + HA[Math.floor(hash01(n * 37 + 11) * HA.length)] + '_' + HB2[Math.floor(hash01(n * 53 + 7) * HB2.length)] + ((n * 7) % 97));
const KIND = { A: 'Cat-face house', B: 'Cardboard box house', C: 'Cat-cave pod' };
const DIST = ['Blue Whisker', 'Box Town', 'Pastel Pods', 'Catnip Green', 'Purple Purr', 'Tuxedo Row'];
const LM_UNLOCK = (EP.landmarks || []).map(l => l.unlock);
const LM_TXT = { petshop: 'Toys, treats and fresh water for every cat in town.', cityhall: 'Mayor Mango works here (mostly naps).', cafe: 'Built by the most-liked comment.', statue: 'A golden Mango. He posed for 3 seconds.', market: 'Fresh fish every morning.', pool: 'Nobody swims. Everyone watches.', custom: 'Built by the most-liked comment.' };
landmarks.forEach((lm, k) => { if (LMG[k]) LMG[k][0].userData.info = { icon: '🏛️', title: lm.sign, line: LM_TXT[lm.kind] || 'Built by the most-liked comment.', note: LM_UNLOCK[k] ? 'Unlocked at ' + LM_UNLOCK[k].toLocaleString('en-US') + ' cats' : '' }; });
if (typeof MO !== 'undefined' && MO.g) MO.g.userData.info = { icon: '😴', title: 'Big Mochi', line: 'The sleeping mountain cat. Please do not wake her.', note: 'Unlocked at 1,000 cats' };
if (typeof FT !== 'undefined' && FT.g) FT.g.userData.info = { icon: '💧', title: 'PETME2 Stainless Steel Fountain', line: 'Mango’s Water Bar: fresh moving water for every cat in town.', note: 'Mango is the host.', pinY: 18 };
if (typeof FD !== 'undefined' && FD.g) FD.g.userData.info = { icon: '🍽️', title: 'PETME2 Dual Bowl Feeder', line: 'Breakfast at 7, dinner at 6. The cats are always early.', note: '', pinY: 15.5 };
if (typeof BS !== 'undefined' && BS.g) BS.g.userData.info = { icon: '🚏', title: 'Nap Bus Stop', line: 'NEXT NAP: 5 MIN. The bus has never come. Nobody minds.', note: '' };
const infoBox = $('info'), infoBody = $('infoBody');
const PIN = new THREE.Mesh(new THREE.ConeGeometry(.9, 1.8, 4).rotateX(Math.PI), new THREE.MeshBasicMaterial({ color: '#FFC93C' })); PIN.visible = false; scene.add(PIN);
let pinY = 0;
const showInfo = (html, pos, y) => { infoBody.innerHTML = html; infoBox.hidden = false; { const h = $('hint'); if (h) h.hidden = true; } if (pos) { PIN.position.set(pos.x, y, pos.z); pinY = y; PIN.visible = true; } else PIN.visible = false; controls.autoRotate = false; };
const hideInfo = () => { infoBox.hidden = true; PIN.visible = false; };
$('infoClose').addEventListener('click', hideInfo);
const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
let downX = 0, downY = 0, lastTap = { t: 0, x: 0, y: 0 };
renderer.domElement.addEventListener('pointerdown', e => { downX = e.clientX; downY = e.clientY; });
renderer.domElement.addEventListener('pointerup', e => {
  if (Math.hypot(e.clientX - downX, e.clientY - downY) > 6) return;          // a drag, not a tap
  const r = renderer.domElement.getBoundingClientRect(); ndc.set((e.clientX - r.left) / r.width * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
  ray.setFromCamera(ndc, camera);
  const now = performance.now(), dbl = now - lastTap.t < 300 && Math.hypot(e.clientX - lastTap.x, e.clientY - lastTap.y) < 25;
  lastTap = dbl ? { t: 0, x: 0, y: 0 } : { t: now, x: e.clientX, y: e.clientY };
  if (dbl) {   // double-tap / double-click: fly there (ground plane y = 0, not the scene); the first tap's card stays as it is
    const gp = ray.ray.intersectPlane(GROUND, new THREE.Vector3()); if (!gp) return; stopSpin(); tick(); clampT(gp);
    flyTo(gp.clone(), gp.clone().add(camera.position.clone().sub(controls.target).multiplyScalar(.6)), .8);
    MARK.position.set(gp.x, .3, gp.z); MARK.visible = true; markT = now; return; }
  const tNow = tOf(Math.round(cur));
  for (const h of ray.intersectObjects(scene.children.filter(o => !o.isInstancedMesh || PICK.has(o)), true)) {
    const map = PICK.get(h.object);
    if (map && h.instanceId != null && map[h.instanceId] >= 0) { const n = map[h.instanceId], l = houseLots[n];
      if (APPEAR[n] >= 0 && tNow < APPEAR[n]) continue;
      const day = Math.max(1, Math.round(EP.dayRange[0] + (EP.dayRange[1] - EP.dayRange[0]) * (n + 1) / Math.max(1, F)));
      showInfo(`<div class="info__icon">🏠</div><div><b class="info__title">@${handleOf(n)}</b><span class="info__line">Cat #${(n + 1).toLocaleString('en-US')} · moved in on day ${day}</span><span class="info__line">${KIND[l.kind]} · ${DIST[l.d]} district</span>${EP.handles ? '' : '<span class="info__note">Example name. Real followers’ Instagram names show here.</span>'}</div>`, l, l.kind === 'C' ? 3.4 : 4.4);
      return; }
    let o = h.object; while (o && !o.userData.info) o = o.parent;
    if (o && o.visible) { const I = o.userData.info, p = new THREE.Vector3(); o.getWorldPosition(p);
      showInfo(`<div class="info__icon">${I.icon}</div><div><b class="info__title">${I.title}</b><span class="info__line">${I.line}</span>${I.note ? `<span class="info__note">${I.note}</span>` : ''}</div>`, p, I.pinY || (o === (typeof MO !== 'undefined' && MO.g) ? 60 : 16)); return; }
    const pt = h.point;
    if (pt.y > 25 && Math.hypot(pt.x, pt.z) < 450) { showInfo(`<div class="info__icon">🐟</div><div><b class="info__title">Fish balloon</b><span class="info__line">Sky tours for cats. Two passengers, zero pilots.</span></div>`, null); return; }
    if (pt.x > COAST_X - 10 && pt.y > 1) { showInfo(`<div class="info__icon">🔴</div><div><b class="info__title">Red Dot Lighthouse</b><span class="info__line">Cats have chased this dot since day 1. Nobody has caught it.</span><span class="info__note">Unlocked at 500 cats</span></div>`, null); return; }
    if (h.object.isInstancedMesh || h.object.isMesh) break;
  }
  hideInfo();
});
const _render = window.renderFrame;
window.renderFrame = (t, a) => { if (PIN.visible) { PIN.position.y = pinY + Math.abs(Math.sin(a * 3)) * .8; PIN.rotation.y = a * 2; } _render(t, a); };
requestAnimationFrame(loop);
document.body.classList.add('ready');
// "Save postcard": render the current view into a 1080x1350 card and show it as an image (the page sandbox blocks scripted downloads,
// so the visitor long-presses / right-clicks the image to save it).
const pcBox = $('pcBox'), pcBtn = $('postcard');
const closePC = () => { pcBox.hidden = true; pcBtn.focus(); };
pcBtn.addEventListener('click', async () => {
  controls.update(); window.renderFrame(tOf(Math.round(cur)), ANIM);
  const src = renderer.domElement, c = document.createElement('canvas'); c.width = 1080; c.height = 1350; const g = c.getContext('2d');
  const sw = src.width, sh = src.height, ar = 1080 / 1220; let cw = sw, ch = sw / ar; if (ch > sh) { ch = sh; cw = sh * ar; }
  g.drawImage(src, (sw - cw) / 2, (sh - ch) / 2, cw, ch, 0, 0, 1080, 1220);
  g.fillStyle = '#FFFFFF'; g.fillRect(0, 1220, 1080, 130);
  try { await document.fonts.load('900 40px Nunito'); await document.fonts.load('800 30px Nunito'); } catch (e) {}
  g.textBaseline = 'middle'; g.fillStyle = '#1B2333'; g.font = '900 40px Nunito, sans-serif'; g.textAlign = 'left';
  g.fillText('Cat Town · ' + $('countN').textContent + ' ' + $('countL').textContent, 48, 1285);
  g.fillStyle = '#2F5FE0'; g.font = '800 30px Nunito, sans-serif'; g.textAlign = 'right'; g.fillText('@petme2', 1032, 1285);
  $('pcImg').src = c.toDataURL('image/png'); pcBox.hidden = false; $('pcClose').focus();
});
$('pcClose').addEventListener('click', closePC);
pcBox.addEventListener('click', e => { if (e.target === pcBox) closePC(); });
addEventListener('keydown', e => { if (e.key === 'Escape' && !pcBox.hidden) closePC(); });
