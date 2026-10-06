// Renders one Cat Town daily episode: node render_day.js <workdir> <i0> <i1>   (frames at 30 fps -> <workdir>/frames/fNNNN.jpg)
// <workdir> holds ep.json (engine episode) + text.json (overlay). The engine page is served from the cat-town folder on port 8772.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [wd, a, b] = process.argv.slice(2); const W = path.resolve(wd);
  const D = JSON.parse(fs.readFileSync(W + '/text.json'));
  const rel = path.relative(process.env.CT_ROOT, W);
  const br = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await br.newPage({ viewport: { width: 1080, height: 1920 } }); p.on('pageerror', x => console.log('err', x.message));
  await p.goto(`http://127.0.0.1:8772/catcity.html?ep=${rel}/ep.json`); await p.waitForFunction('window.ready === true', null, { timeout: 180000 });
  await p.addScriptTag({ path: __dirname + '/overlay.js' });
  if (D.keepCm) await p.evaluate(() => document.body.classList.add('keepcm'));
  fs.mkdirSync(W + '/frames', { recursive: true });
  const Ts = a === 'test' ? b.split(',').map(Number) : [...Array(+b - +a).keys()].map(i => (i + +a) / 30);
  for (let i = 0; i < Ts.length; i++) { const T = Ts[i];
    await p.evaluate(([T, D]) => { window.renderFrame(T, T + (D.animOff || 0)); window.ovDraw(T, D); }, [T, D]);
    await p.screenshot({ path: a === 'test' ? `${W}/test_${T}.jpg` : `${W}/frames/f${String(i + +a).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 92 }); }
  await br.close();
})();
