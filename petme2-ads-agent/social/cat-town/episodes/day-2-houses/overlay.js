// Injected into each engine page (copy of day-2-fish/overlay.js + house counter and house tags): hides the engine's own UI (keeps the comment card + build tag), draws the badge + text layer.
(() => {
  const css = `#brand,#count,#title,#end,#sub{display:none!important}
  #cm{top:880px!important;left:50px!important;right:50px!important}
  .cm__label{font-size:40px!important;padding:10px 26px!important}
  .cm__win,.card{height:250px!important} .card__av{flex-basis:110px!important;height:110px!important;font-size:52px!important}
  .card__name{font-size:38px!important} .card__text{font-size:58px!important;white-space:normal!important;line-height:1.05} .card__like svg{width:72px!important;height:72px!important}
  .crown{font-size:38px!important;top:-12px!important}
  #ov{position:absolute;inset:0;pointer-events:none;font-family:Nunito,sans-serif;z-index:5}
  #ov .brand{position:absolute;top:226px;left:0;right:0;text-align:center}
  #ov .brand span{display:inline-block;background:rgba(255,255,255,.95);color:#2F5FE0;font-weight:900;font-size:32px;letter-spacing:.08em;padding:10px 26px;border-radius:999px;box-shadow:0 8px 24px rgba(20,40,90,.18)}
  #ov .cnt{position:absolute;top:288px;left:0;right:0;text-align:center}
  #ov .cnt b{display:block;font-weight:900;font-size:104px;line-height:1;color:#fff;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cnt b.g{color:#FFD23F}
  #ov .cnt span{display:inline-block;margin-top:6px;background:#1B2333;color:#fff;font-weight:900;font-size:32px;padding:7px 24px;border-radius:999px}
  #ov .big{position:absolute;left:60px;right:140px;top:500px;text-align:center;font-weight:900;font-size:96px;line-height:1.04;color:#fff;-webkit-text-stroke:14px #1B2333;paint-order:stroke fill;text-shadow:0 12px 0 rgba(27,35,51,.3)}
  #ov .big y{color:#FFD23F} #ov .big r{color:#FF6B6B}
  #ov .small{position:absolute;left:60px;right:140px;top:712px;text-align:center;font-weight:900;font-size:60px;color:#FFD23F;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .ex{position:absolute;background:#E8384F;color:#fff;font-weight:900;font-size:34px;letter-spacing:.06em;padding:6px 18px;border-radius:12px;border:4px solid #fff;box-shadow:0 8px 20px rgba(0,0,0,.25);transform-origin:left center}
  #ov .arrow{position:absolute;left:800px;top:1110px;font-size:110px}
  #ov .cap{position:absolute;left:60px;right:140px;top:1500px;text-align:center;font-weight:900;font-size:64px;line-height:1.15}
  #ov .cap span{display:inline-block;margin:0 8px;color:#fff;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cap span.on{color:#FFD23F}
  .tag{font-size:42px!important}
  #tags.pin .tag{top:1760px!important;left:540px!important}
`;
  const lab = document.querySelector('.cm__label'); if (lab) lab.textContent = '🗳️ Your likes picked it';
  document.querySelectorAll('#tags .tag small').forEach(el => { el.textContent = el.textContent.replace(/🐱 Cat #(\d+) moved in/, '🏠 follower #$1 moved in'); });
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  const ov = document.createElement('div'); ov.id = 'ov'; document.body.appendChild(ov);
  const back = x => { x = Math.min(1, Math.max(0, x)); const c = 1.70158; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
  window.ovDraw = (T, D) => {
    const end = 1;   // the last beat repeats the hook text, so the loop lands on frame 0 with text
    let h = '', b = '';
    const goal = T >= D.goal[0] && T < D.goal[1];
    b += `<div class="brand"><span>🐾 PETME2 CAT TOWN</span></div>`;
    const fol = D.followers ? (T >= D.roll[0] && T < D.roll[1] ? Math.round(D.followers * Math.pow((T - D.roll[0]) / (D.roll[1] - D.roll[0]), 2)) : D.followers) : 0;   // follower count rolls up while the voice says it
    if (D.houses) { const n = Math.max(0, (window.__shown || 1) - 1); b += `<div class="cnt"><b class="${n >= 128 ? 'g' : ''}">${n}</b><span>🏠 houses · 1 per follower</span></div>`; } else
    b += goal ? `<div class="cnt"><b class="g">1,000</b><span>cats · THE GOAL</span></div>` : D.followers ? `<div class="cnt"><b class="${T >= D.roll[0] && T < D.roll[1] + 1 ? 'g' : ''}">${fol}</b><span>followers · Day ${D.day}</span></div>` : `<div class="cnt"><b>${D.cats}</b><span>${D.cats === 1 ? 'cat' : 'cats'} · Day ${D.day}</span></div>`;
    const beat = D.beats.find(x => T >= x.s && T < x.e);
    if (beat) { const k = beat.still ? 1 : back((T - beat.s) / .3); h += `<div class="big" style="transform:scale(${.6 + .4 * k});opacity:${beat.still ? 1 : Math.min(1, (T - beat.s) / .1)}">${beat.html}</div>`;
      if (beat.small && T >= beat.ss) h += `<div class="small" style="${beat.smallTop ? 'top:' + beat.smallTop + 'px;' : ''}transform:scale(${back((T - beat.ss) / .3)})">${beat.small}</div>`;
      if (beat.small2 && T >= beat.ss2) h += `<div class="small" style="top:790px;color:#fff;transform:scale(${back((T - beat.ss2) / .3)})">${beat.small2}</div>`;
      if (beat.arrowDown) { const a = T - beat.s - .4; if (a > 0) h += `<div class="arrow" style="left:490px;top:${760 + 18 * Math.sin(a * 9)}px;transform:scale(${back(a / .3)})">👇</div>`; }
      if (beat.arrow) { const a = T - beat.s - .5; if (a > 0) h += `<div class="arrow" style="transform:translateX(${18 * Math.sin(a * 9)}px) scale(${back(a / .3)})">👉</div>`; } }
    for (const [s, e, kind] of D.example) { if (T < s || T >= e) continue; const k = back((T - s) / .3);
      let x = 96, y = 1064;
      if (kind === 'house') { const tg = [...document.querySelectorAll('#tags .tag')].find(el => el.style.display === 'block'); if (!tg) continue; const r = tg.getBoundingClientRect(); x = r.left - 10; y = r.top - 44; }
      if (kind === 'statue') { x = 200; y = 1180; }
      if (kind === 'card') { x = 96; y = 1064; }
      h += `<div class="ex" style="left:${x}px;top:${y}px;transform:rotate(-6deg) scale(${k})">EXAMPLE</div>`; }
    if (D.build && T >= D.build[0] - .15 && T < D.build[1] + .5) {   // slow build: progress bar under the headline
      const k = Math.min(1, Math.max(0, (T - D.build[0]) / (D.build[1] - D.build[0]))), pct = Math.round(100 * k), done = k >= 1;
      h += `<div style="position:absolute;left:170px;right:170px;top:640px;text-align:center;font-weight:900;font-size:46px;color:#fff;-webkit-text-stroke:9px #1B2333;paint-order:stroke fill">${done ? '✅ 100%' : '🚧 Building... ' + pct + '%'}</div>
        <div style="position:absolute;left:170px;right:170px;top:712px;height:38px;border-radius:999px;background:rgba(27,35,51,.85);border:5px solid #fff;overflow:hidden"><div style="height:100%;width:${100 * k}%;background:${done ? '#5BB98C' : '#FFD23F'}"></div></div>`; }
    const line = D.lines.find(l => !l.hide && T >= l.s - .05 && T < l.e + .3);
    if (line) h += `<div class="cap">${line.words.map(w => `<span class="${T >= w.s && T < w.e + .05 ? 'on' : ''}">${w.w}</span>`).join(' ')}</div>`;
    ov.innerHTML = b + `<div style="opacity:${end}">${h}</div>`;
    const tg = document.getElementById('tags'); if (tg) tg.style.opacity = (D.hideTags || []).some(([s, e]) => T >= s && T < e) ? 0 : 1; if (tg) tg.classList.toggle('pin', (D.pinTags || []).some(([s, e]) => T >= s && T < e));
  };
})();
