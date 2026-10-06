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
  controls.update(); window.renderFrame(tOf(Math.round(cur)), ANIM); }

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
if (typeof BS !== 'undefined' && BS.g) BS.g.userData.info = { icon: '🚏', title: 'Nap Bus Stop', line: 'NEXT NAP: 5 MIN. The bus has never come. Nobody minds.', note: '' };
const infoBox = $('info'), infoBody = $('infoBody');
const PIN = new THREE.Mesh(new THREE.ConeGeometry(.9, 1.8, 4).rotateX(Math.PI), new THREE.MeshBasicMaterial({ color: '#FFC93C' })); PIN.visible = false; scene.add(PIN);
let pinY = 0;
const showInfo = (html, pos, y) => { infoBody.innerHTML = html; infoBox.hidden = false; if (pos) { PIN.position.set(pos.x, y, pos.z); pinY = y; PIN.visible = true; } else PIN.visible = false; controls.autoRotate = false; };
const hideInfo = () => { infoBox.hidden = true; PIN.visible = false; };
$('infoClose').addEventListener('click', hideInfo);
const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
let downX = 0, downY = 0;
renderer.domElement.addEventListener('pointerdown', e => { downX = e.clientX; downY = e.clientY; });
renderer.domElement.addEventListener('pointerup', e => {
  if (Math.hypot(e.clientX - downX, e.clientY - downY) > 6) return;          // a drag, not a tap
  const r = renderer.domElement.getBoundingClientRect(); ndc.set((e.clientX - r.left) / r.width * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
  ray.setFromCamera(ndc, camera);
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
      showInfo(`<div class="info__icon">${I.icon}</div><div><b class="info__title">${I.title}</b><span class="info__line">${I.line}</span>${I.note ? `<span class="info__note">${I.note}</span>` : ''}</div>`, p, o === (typeof MO !== 'undefined' && MO.g) ? 60 : 16); return; }
    const pt = h.point;
    if (Math.hypot(pt.x, pt.z) < 9.5 && pt.y > .2) { showInfo(`<div class="info__icon">💧</div><div><b class="info__title">Mango’s Water Bar</b><span class="info__line">The PETME2 fountain. Cats walk in from every street to drink. Mango is the host.</span></div>`, new THREE.Vector3(0, 0, 0), 10); return; }
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
