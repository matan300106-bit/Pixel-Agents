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
let last = performance.now();
function loop(now) { const dt = Math.min(.05, (now - last) / 1000); last = now; ANIM += reduce ? 0 : dt;
  if (playing) { cur = Math.min(FMAX, cur + Math.max(4, cur * .35) * dt * 2.2); target = cur; slider.value = Math.round(cur); if (cur >= FMAX) setPlay(false); }
  else cur += (target - cur) * Math.min(1, dt * 8);
  if (Math.abs(target - cur) < .5) cur = target;
  slider.setAttribute('aria-valuetext', Math.round(cur) + ' followers');
  controls.update(); window.renderFrame(tOf(Math.round(cur)), ANIM);
  requestAnimationFrame(loop); }
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
