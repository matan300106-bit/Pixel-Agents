// Render town.html (episode.json) to frames/f0000.png ... at 30 fps.
// Usage: node render_town.js [fps] [comma-separated test times]
const { chromium } = require('playwright');
const fs = require('fs');
const fps = +process.argv[2] || 30, only = process.argv[3];
const port = process.env.PORT || 8766;
(async () => {
  const ep = JSON.parse(fs.readFileSync(__dirname + '/episode.json'));
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.log('err:', e.message));
  await p.goto(`http://127.0.0.1:${port}/town.html`);
  await p.waitForFunction('window.ready === true', null, { timeout: 60000 });
  fs.mkdirSync(__dirname + '/frames', { recursive: true });
  const times = only ? only.split(',').map(Number) : [...Array(Math.round(ep.duration * fps)).keys()].map(i => i / fps);
  for (let i = 0; i < times.length; i++) {
    await p.evaluate(t => window.renderFrame(t), times[i]);
    await p.screenshot({ path: only ? `${__dirname}/frames/test_${times[i]}.png` : `${__dirname}/frames/f${String(i).padStart(4, '0')}.png` });
  }
  await b.close();
})();
