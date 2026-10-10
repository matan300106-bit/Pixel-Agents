// node render.js DIR test T1,T2,...  |  node render.js DIR range i0 i1   (30 fps -> DIR/frames/fNNNN.jpg)
// needs a static server on :8772 whose root holds catcity.html + node_modules + DIR. Frames 0-1 s replay engine time D..D+1 (seamless loop).
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [dir, mode, a, b] = process.argv.slice(2); const DIR = path.resolve(dir), REL = path.basename(DIR);
const D = JSON.parse(fs.readFileSync(DIR + '/text.json'));
const eng = T => T < 1.0 ? D.duration + T : T;
(async () => {
  const Ts = mode === 'test' ? a.split(',').map(Number) : [...Array(+b - +a).keys()].map(i => (i + +a) / 30);
  const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p1 = await br.newPage({ viewport: { width: 1080, height: 1920 } }); p1.on('pageerror', x => console.log('err', x.message));
  await p1.goto(`http://127.0.0.1:8772/catcity.html?ep=${REL}/e1.json`); await p1.waitForFunction('window.ready === true', null, { timeout: 180000 });
  await p1.addScriptTag({ path: __dirname + '/overlay.js' });
  fs.mkdirSync(DIR + '/frames', { recursive: true });
  for (let i = 0; i < Ts.length; i++) { const T = Ts[i];
    await p1.evaluate(([t, T, D]) => { window.renderFrame(t, t); window.ovDraw(T, D); }, [eng(T), T, D]);
    const out = mode === 'test' ? `${DIR}/test_${T}.jpg` : `${DIR}/frames/f${String(i + +a).padStart(4, '0')}.jpg`;
    await p1.screenshot({ path: out, type: 'jpeg', quality: 92 }); }
  await br.close();
})();
