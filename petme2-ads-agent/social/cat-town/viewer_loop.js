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
