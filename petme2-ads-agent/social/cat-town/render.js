const { chromium } = require('playwright');
const fps = +process.argv[2] || 30, dur = 21, only = process.argv[3];
(async () => {
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('console', m => console.log('page:', m.text()));
  p.on('pageerror', e => console.log('err:', e.message));
  await p.goto('http://127.0.0.1:8765/scene.html');
  await p.waitForFunction('window.ready === true', null, { timeout: 30000 });
  await p.evaluate(() => document.fonts.ready);
  const times = only ? only.split(',').map(Number) : [...Array(Math.round(dur * fps)).keys()].map(i => i / fps);
  for (let i = 0; i < times.length; i++) {
    await p.evaluate(t => window.renderFrame(t), times[i]);
    await p.screenshot({ path: only ? `test_${times[i]}.png` : `frames/f${String(i).padStart(4, '0')}.png` });
  }
  await b.close();
})();
