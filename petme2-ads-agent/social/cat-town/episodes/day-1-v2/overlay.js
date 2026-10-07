// Injected into each engine page: hides the engine's own UI (keeps house tags) and draws the Day 1 text layer.
(() => {
  const css = `#brand,#count,#title,#cm,#end,#sub{display:none!important}
  #ov{position:absolute;inset:0;pointer-events:none;font-family:Nunito,sans-serif;z-index:5}
  #ov .pill{position:absolute;left:60px;top:236px;background:#1B2333;color:#fff;font-weight:900;font-size:44px;padding:12px 30px;border-radius:999px;box-shadow:0 10px 30px rgba(0,0,0,.25)}
  #ov .pill b{color:#FFD23F}
  #ov .big{position:absolute;left:50px;right:150px;top:330px;text-align:center;font-weight:900;font-size:104px;line-height:1.04;color:#fff;-webkit-text-stroke:15px #1B2333;paint-order:stroke fill;text-shadow:0 12px 0 rgba(27,35,51,.3)}
  #ov .big y{color:#FFD23F} #ov .big r{color:#FF6B6B}
  #ov .small{position:absolute;left:50px;right:150px;text-align:center;font-weight:900;font-size:56px;color:#FFD23F;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .follow{position:absolute;left:50%;top:700px;transform:translateX(-50%);background:#2F7BFF;color:#fff;font-weight:900;font-size:60px;padding:20px 60px;border-radius:24px;box-shadow:0 14px 40px rgba(0,0,0,.3)}
  #ov .cap{position:absolute;left:60px;right:150px;top:1290px;text-align:center;font-weight:900;font-size:66px;line-height:1.15}
  #ov .cap span{display:inline-block;margin:0 8px;color:#fff;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cap span.on{color:#FFD23F}
  .tag{font-size:44px!important;margin-left:-110px} #ov .tag{margin-left:0}`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  const ov = document.createElement('div'); ov.id = 'ov'; document.body.appendChild(ov);
  const back = x => { x = Math.min(1, Math.max(0, x)); const c = 1.70158; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
  window.ovDraw = (T, D) => {
    let h = '';
    const beat = D.beats.find(b => T >= b.s && T < b.e);
    if (D.pill && !(T >= 12.8 && T < 14.65)) { const k = back((T - .25) / .35); h += `<div class="pill" style="transform:scale(${k});transform-origin:left center">🐱 <b>1</b> cat · Day 1</div>`; }
    if (beat) { const k = back((T - beat.s) / .3); h += `<div class="big" style="transform:scale(${.6 + .4 * k});opacity:${Math.min(1, (T - beat.s) / .12)}">${beat.html}</div>`;
      if (beat.small && T >= beat.ss) h += `<div class="small" style="top:${beat.sy}px;transform:scale(${back((T - beat.ss) / .3)})">${beat.small}</div>`;
      if (beat.follow && T >= beat.fs) { const k2 = back((T - beat.fs) / .35), pulse = 1 + .05 * Math.sin((T - beat.fs) * 8); h += `<div class="follow" style="transform:translateX(-50%) scale(${k2 * pulse})">Follow 👇</div>`; } }
    (D.otags || []).forEach(g => { if (T >= g.s && T < g.e) h += `<div class="tag" style="left:${g.x}px;top:${g.y}px;transform:translate(-50%,-100%) scale(${back((T - g.s) / .35)})">@you<small>moved in (example)</small></div>`; });
    const line = D.lines.find(l => !l.hide && T >= l.s - .05 && T < l.e + .3);
    if (line) h += `<div class="cap">${line.words.map(w => `<span class="${T >= w.s && T < w.e + .05 ? 'on' : ''}">${w.w}</span>`).join(' ')}</div>`;
    const tg = document.getElementById('tags'); if (tg) tg.style.visibility = T < 11.1 ? 'hidden' : 'visible';
    ov.innerHTML = h; ov.style.opacity = Math.min(1, Math.max(0, (18.8 - 1/30 - T) / .3)); if (tg) tg.style.opacity = ov.style.opacity;
  };
})();
