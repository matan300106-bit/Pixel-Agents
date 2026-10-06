// node render.js test T1,T2,...   |  node render.js range i0 i1  (frames at 30 fps -> v/frames/fNNNN.jpg)
const { chromium } = require('playwright'); const fs = require('fs');
const D = JSON.parse(fs.readFileSync(__dirname + '/v/text.json'));
const SEG = T => T < 4.55 ? ['e0', 0] : T < 5.8 ? ['e0', 5] : T < 6.6 ? ['e0', 15] : T < 7.4 ? ['e0', 8] : T < 12.8 ? ['e1', 18] : T < 14.65 ? ['e2', 0] : ['e0', -18.8];
(async () => {
  const [mode, a, b] = process.argv.slice(2);
  const Ts = mode === 'test' ? a.split(',').map(Number) : [...Array(+b - +a).keys()].map(i => (i + +a) / 30);
  const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pages = {}; const need = [...new Set(Ts.map(T => SEG(T)[0]))];
  for (const e of need) { const p = await br.newPage({ viewport: { width: 1080, height: 1920 } }); p.on('pageerror', x => console.log('err', e, x.message));
    await p.goto(`http://127.0.0.1:8772/catcity.html?ep=v/${e}.json`); await p.waitForFunction('window.ready === true', null, { timeout: 180000 });
    await p.addScriptTag({ path: __dirname + '/overlay.js' });
    await p.evaluate(() => { const L = [['you', 'Cat #2 moved in'], ['you', 'Cat #3 moved in'], ['you', 'Cat #4 moved in']]; document.querySelectorAll('#tags .tag').forEach((el, i) => { if (window.TAGS && window.TAGS[i]) el.innerHTML = window.TAGS[i]; }); });
    pages[e] = p; }
  if (pages.e1) await pages.e1.evaluate(tags => document.querySelectorAll('#tags .tag').forEach((el, i) => { if (tags[i]) el.innerHTML = tags[i]; }), D.tags || []);
  fs.mkdirSync(__dirname + '/v/frames', { recursive: true });
  for (let i = 0; i < Ts.length; i++) { const T = Ts[i], [e, off] = SEG(T), p = pages[e];
    await p.evaluate(([T, an, D]) => { window.renderFrame(T, an); window.ovDraw(T, D); }, [T, T + off, D]);
    const out = mode === 'test' ? `${__dirname}/v/test_${T}.jpg` : `${__dirname}/v/frames/f${String(i + +a).padStart(4, '0')}.jpg`;
    await p.screenshot({ path: out, type: 'jpeg', quality: 92 });
    if (mode === 'test' && e === 'e1') console.log(T, await p.evaluate(() => [...document.querySelectorAll('#tags .tag')].map(el => el.style.display).join(',')));
  }
  await br.close();
})();
