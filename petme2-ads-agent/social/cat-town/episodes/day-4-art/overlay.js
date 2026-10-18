// Day 4 overlay (from day-3-arcade/overlay.js): hides the engine UI (keeps the comment card + build tag), draws the badge, house / cat / no-home counters,
// big beat text, the build progress bar and word-by-word captions.
(() => {
  const css = `#brand,#count,#title,#end,#sub{display:none!important}
  #cm{top:880px!important;left:50px!important;right:50px!important}
  .cm__label{font-size:40px!important;padding:10px 26px!important}
  .cm__win,.card{height:250px!important} .card__av{flex-basis:110px!important;height:110px!important;font-size:52px!important}
  .card__name{font-size:38px!important} .card__text{font-size:50px!important;white-space:normal!important;line-height:1.05} .card__like svg{width:72px!important;height:72px!important}
  .crown{font-size:38px!important;top:-12px!important}
  canvas{transform-origin:top left}
  #ov{position:absolute;inset:0;pointer-events:none;font-family:Nunito,sans-serif;z-index:5}
  #ov .brand{position:absolute;top:226px;left:0;right:0;text-align:center}
  #ov .brand span{display:inline-block;background:rgba(255,255,255,.95);color:#2F5FE0;font-weight:900;font-size:32px;letter-spacing:.08em;padding:10px 26px;border-radius:999px;box-shadow:0 8px 24px rgba(20,40,90,.18)}
  #ov .cnt{position:absolute;left:0;right:0;text-align:center}
  #ov .cnt .row{display:flex;justify-content:center;gap:30px}
  #ov .cnt b{display:block;font-weight:900;font-size:96px;line-height:1;color:#fff;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cnt b.g{color:#FFD23F} #ov .cnt b.r{color:#FF6B6B} #ov .cnt b.gr{color:#5BB98C}
  #ov .cnt i{display:block;font-style:normal;margin-top:4px;font-weight:900;font-size:30px;color:#fff;background:#1B2333;padding:5px 18px;border-radius:999px}
  #ov .chip{display:inline-block;font-weight:900;font-size:44px;color:#1B2333;background:#FFD23F;padding:8px 28px;border-radius:999px;border:5px solid #1B2333;margin-bottom:10px}
  #ov .top{position:absolute;left:0;right:0;top:0;height:960px;overflow:hidden}
  #ov .top img{position:absolute;left:0;top:-480px;width:1080px;height:1920px}
  #ov .div{position:absolute;left:0;right:0;top:954px;height:12px;background:#fff;box-shadow:0 0 0 5px #1B2333}
  #ov .big{position:absolute;left:60px;right:60px;top:500px;text-align:center;font-weight:900;font-size:96px;line-height:1.04;color:#fff;-webkit-text-stroke:14px #1B2333;paint-order:stroke fill;text-shadow:0 12px 0 rgba(27,35,51,.3)}
  #ov .big y{color:#FFD23F} #ov .big r{color:#FF6B6B}
  #ov .small{position:absolute;left:60px;right:60px;top:712px;text-align:center;font-weight:900;font-size:60px;color:#FFD23F;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cap{position:absolute;left:60px;right:60px;top:1520px;text-align:center;font-weight:900;font-size:64px;line-height:1.15}
  #ov .cap span{display:inline-block;margin:0 8px;color:#fff;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cap span.on{color:#FFD23F}
  .tag{font-size:42px!important}
`;
  const lab = document.querySelector('.cm__label'); if (lab) lab.textContent = '🗳️ Your likes picked it';
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  const ov = document.createElement('div'); ov.id = 'ov'; document.body.appendChild(ov);
  const cv = document.querySelector('canvas');
  const back = x => { x = Math.min(1, Math.max(0, x)); const c = 1.70158; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
  const fmt = n => n.toLocaleString('en-US');
  window.ovDraw = (T, D) => {
    const bt = document.querySelector('#tags .tag:last-child small'); if (bt && !bt.dataset.d) { bt.textContent = "💡 Tilly's idea: an Art Studio"; bt.dataset.d = 1; }
    let h = '', b = '';
    b += `<div class="brand"><span>🐾 PETME2 CAT TOWN</span></div>`;
    const roll = (r, n0, n1) => { const u = Math.min(1, Math.max(0, (T - r[0]) / (r[1] - r[0]))), k = u * u * (3 - 2 * u); return T < r[0] ? n0 : Math.round(n0 + (n1 - n0) * k); };
    const live = r => T >= r[0] && T < r[1] + .8;
    if (T >= D.counters[0] && T < D.counters[1]) { const kin = back((T - D.counters[0]) / .35);
      const hN = roll(D.rollH, 0, D.houses) + (T >= D.houseAt ? 1 : 0), cN = roll(D.rollC, 1, D.cats), nN = D.nohome - (T >= D.homeAt ? 1 : 0);
      const pulse = a => T >= a && T < a + .35 ? 1 + .3 * (1 - (T - a) / .35) : 1;
      let row = `<div><b class="${live(D.rollH) || (T >= D.houseAt && T < D.houseAt + 1.5) ? 'g' : ''}" style="transform:scale(${pulse(D.houseAt)})">${fmt(hN)}</b><i>🏠 houses</i></div>`;
      row += `<div><b class="${live(D.rollC) ? 'g' : ''}">${fmt(cN)}</b><i>🐱 cats</i></div>`;
      if (T >= D.nohomeAt) row += `<div style="transform:scale(${back((T - D.nohomeAt) / .35) * pulse(D.homeAt)})"><b class="${T >= D.homeAt && T < D.homeAt + 1.5 ? 'gr' : 'r'}">${fmt(nN)}</b><i>😿 no home</i></div>`;
      b += `<div class="cnt" style="top:290px;transform:scale(${kin})"><div class="row">${row}</div></div>`; }
    const beat = D.beats.find(x => T >= x.s && T < x.e);
    const bigTop = T >= D.counters[0] && T < D.counters[1] ? 470 : 500;
    if (beat) { const kk = beat.still ? 1 : back((T - beat.s) / .3); h += `<div class="big" style="top:${bigTop}px;transform:scale(${.6 + .4 * kk});opacity:${beat.still ? 1 : Math.min(1, (T - beat.s) / .1)}">${beat.html}</div>`;
      if (beat.small && T >= beat.ss) h += `<div class="small" style="top:${beat.smallTop || 712}px;transform:scale(${back((T - beat.ss) / .3)})">${beat.small}</div>`; }
    if (D.build && T >= D.build[0] - .15 && T < D.build[1] + .5) {   // slow build: progress bar under the headline
      const kb = Math.min(1, Math.max(0, (T - D.build[0]) / (D.build[1] - D.build[0]))), pct = Math.round(100 * kb), done = kb >= 1;
      h += `<div style="position:absolute;left:170px;right:170px;top:600px;text-align:center;font-weight:900;font-size:46px;color:#fff;-webkit-text-stroke:9px #1B2333;paint-order:stroke fill">${done ? '✅ 100%' : '🚧 Building... ' + pct + '%'}</div>
        <div style="position:absolute;left:170px;right:170px;top:672px;height:38px;border-radius:999px;background:rgba(27,35,51,.85);border:5px solid #fff;overflow:hidden"><div style="height:100%;width:${100 * kb}%;background:${done ? '#5BB98C' : '#FFD23F'}"></div></div>`; }
    const line = D.lines.find(l => T >= l.s - .05 && T < l.e + .3);
    if (line) h += `<div class="cap">${line.words.map(w => `<span class="${T >= w.s && T < w.e + .05 ? 'on' : ''}">${w.w}</span>`).join(' ')}</div>`;
    ov.innerHTML = b + h;
    const tg = document.getElementById('tags'); if (tg) tg.style.opacity = T >= 22.35 && T < 28.7 ? 1 : 0;
  };
})();
