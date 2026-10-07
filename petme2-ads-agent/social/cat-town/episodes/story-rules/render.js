// node render.js DIR test T1,T2,...  |  node render.js DIR range i0 i1   (30 fps -> DIR/frames/fNNNN.jpg)
// needs a static server on :8772 whose root holds catcity.html + node_modules + DIR
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [dir, mode, a, b] = process.argv.slice(2); const DIR = path.resolve(dir), REL = path.basename(DIR);
const D = JSON.parse(fs.readFileSync(DIR + '/text.json'));
// page per time: e0 Mango/town, eh EXAMPLE houses, e0 sign, es EXAMPLE statue
const SEG = T => T < 5.0 ? ['e0', 0] : T < 10.0 ? ['eh', 0] : T < 15.0 ? ['e0', 0] : ['es', 0];
(async () => {
  const Ts = mode === 'test' ? a.split(',').map(Number) : [...Array(+b - +a).keys()].map(i => (i + +a) / 30);
  const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pages = {};
  for (const e of [...new Set(Ts.map(T => SEG(T)[0]))]) { const p = await br.newPage({ viewport: { width: 1080, height: 1920 } }); p.on('pageerror', x => console.log('err', e, x.message));
    await p.goto(`http://127.0.0.1:8772/catcity.html?ep=${REL}/${e}.json`); await p.waitForFunction('window.ready === true', null, { timeout: 180000 });
    await p.addScriptTag({ path: __dirname + '/overlay.js' });
    if (e === 'eh') await p.evaluate(() => document.querySelectorAll('#tags .tag').forEach(el => { el.innerHTML = '@you<small>🐱 moved in</small>'; }));
    pages[e] = p; }
  fs.mkdirSync(DIR + '/frames', { recursive: true });
  for (let i = 0; i < Ts.length; i++) { const T = Ts[i], [e, off] = SEG(T), p = pages[e];
    await p.evaluate(([T, an, D]) => { window.renderFrame(T, an); window.ovDraw(T, D); }, [T, T + off, D]);
    const out = mode === 'test' ? `${DIR}/test_${T}.jpg` : `${DIR}/frames/f${String(i + +a).padStart(4, '0')}.jpg`;
    await p.screenshot({ path: out, type: 'jpeg', quality: 92 }); }
  await br.close();
})();
