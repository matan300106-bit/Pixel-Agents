const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [name, w] of [['desktop', 1280], ['phone', 390]]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: w < 500 ? 2 : 1 });
    await p.route(/cdn\.shopify\.com/, r => r.abort());
    await p.goto('file://' + __dirname + '/redesign-preview.html');
    await p.addStyleTag({ content: '.pm2-cmp__img,.pm2-px__pairimg{display:flex!important;align-items:center;justify-content:center;color:#aaa;font-size:11px}.pm2-cmp__img::after,.pm2-px__pairimg::after{content:"product photo"}img{display:none!important}' });
    await p.screenshot({ path: `redesign-${name}.png`, fullPage: true });
  }
  await b.close();
})();
