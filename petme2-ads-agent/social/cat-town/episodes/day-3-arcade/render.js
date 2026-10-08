// node render.js DIR test T1,T2,...  |  node render.js DIR range i0 i1   (30 fps -> DIR/frames/fNNNN.jpg)
// needs a static server on :8772 whose root holds catcity.html + node_modules + DIR. Frames 0-1 s replay engine time D..D+1 (seamless loop);
// during the split, the top half is a Day 1 frame (e0.json) taken from a second page.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [dir, mode, a, b] = process.argv.slice(2); const DIR = path.resolve(dir), REL = path.basename(DIR);
const D = JSON.parse(fs.readFileSync(DIR + '/text.json'));
const eng = T => T < 1.0 ? D.duration + T : T;
(async () => {
  const Ts = mode === 'test' ? a.split(',').map(Number) : [...Array(+b - +a).keys()].map(i => (i + +a) / 30);
  const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const open = async e => { const p = await br.newPage({ viewport: { width: 1080, height: 1920 } }); p.on('pageerror', x => console.log('err', e, x.message));
    await p.goto(`http://127.0.0.1:8772/catcity.html?ep=${REL}/${e}.json`); await p.waitForFunction('window.ready === true', null, { timeout: 180000 }); return p; };
  const p1 = await open('e1'); await p1.addScriptTag({ path: __dirname + '/overlay.js' });
  const needTop = Ts.some(T => T >= D.split[0] && T < D.split[1]);
  const p0 = needTop ? await open('e0') : null; if (p0) await p0.addStyleTag({ content: '.ui,#tags,#cm{display:none!important}' });
  fs.mkdirSync(DIR + '/frames', { recursive: true });
  for (let i = 0; i < Ts.length; i++) { const T = Ts[i];
    if (p0 && T >= D.split[0] && T < D.split[1]) { await p0.evaluate(T => window.renderFrame(T - 9.0, T), T);
      const buf = await p0.screenshot({ type: 'jpeg', quality: 90, clip: { x: 0, y: 0, width: 1080, height: 1920 } }); await p1.evaluate(s => window.__top = s, 'data:image/jpeg;base64,' + buf.toString('base64')); }
    await p1.evaluate(([t, T, D]) => { window.renderFrame(t, t); window.ovDraw(T, D); }, [eng(T), T, D]);
    if (p0 && T >= D.split[0] && T < D.split[1]) await p1.waitForFunction(() => { const im = document.querySelector('#ov .top img'); return !im || im.complete; });
    const out = mode === 'test' ? `${DIR}/test_${T}.jpg` : `${DIR}/frames/f${String(i + +a).padStart(4, '0')}.jpg`;
    await p1.screenshot({ path: out, type: 'jpeg', quality: 92 }); }
  await br.close();
})();
