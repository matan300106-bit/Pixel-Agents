// node still.js ep.json out.png t anim
const { chromium } = require('playwright');
(async () => {
  const [ep, out, t, anim] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.log('err:', e.message));
  await p.goto(`http://127.0.0.1:8772/catcity.html?ep=${ep}`);
  await p.waitForFunction('window.ready === true', null, { timeout: 120000 });
  await p.evaluate(([t, a]) => window.renderFrame(t, a), [+t, +(anim ?? t)]);
  await p.screenshot({ path: out, type: out.endsWith('jpg') ? 'jpeg' : 'png', quality: out.endsWith('jpg') ? 80 : undefined });
  await b.close();
})();
