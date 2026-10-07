// Injected into the engine page for the "Be OK" video: hides the engine UI, draws TikTok-style white caption boxes (+ a live cat count during rule 2).
(() => {
  const css = `#brand,#count,#title,#end,#sub,#cm{display:none!important}
  #ov{position:absolute;inset:0;pointer-events:none;font-family:Nunito,sans-serif;z-index:5}
  #ov .tc{position:absolute;left:90px;right:150px;top:300px;text-align:center}
  #ov .tc span{display:inline;background:#fff;color:#111;font-weight:900;font-size:62px;line-height:1.42;padding:6px 18px;border-radius:14px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
  #ov .tc b{color:#E8384F}
  #ov .sb{margin-top:26px} #ov .sb span{background:#111;color:#fff;font-size:54px} #ov .sb b{color:#FFD23F}
  #ov .num{margin-top:30px;font-weight:900;font-size:120px;line-height:1;color:#fff;-webkit-text-stroke:12px #111;paint-order:stroke fill}
  .tag{font-size:42px!important}`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  document.querySelectorAll('#tags .tag small').forEach(el => { el.textContent = el.textContent.replace(/🐱 Cat #(\d+) moved in/, '🏠 follower #$1'); });
  const ov = document.createElement('div'); ov.id = 'ov'; document.body.appendChild(ov);
  const back = x => { x = Math.min(1, Math.max(0, x)); const c = 1.70158; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
  window.ovDraw = (T, D) => {
    const c = D.cards.find(x => T >= x.s && T < x.e); let h = '';
    if (c) { const k = c.s === 0 ? 1 : back((T - c.s) / .25);
      h += `<div class="tc" style="transform:scale(${.85 + .15 * k})"><span>${c.html}</span>`;
      if (c.sub && T >= c.ss) h += `<div class="sb" style="transform:scale(${back((T - c.ss) / .25)})"><span>${c.sub}</span></div>`;
      if (c.count) { const n = 128 + (window.__strays || 0); h += `<div class="num">🐱 ${n}</div>`; }
      h += '</div>'; }
    ov.innerHTML = h;
    const tg = document.getElementById('tags'); if (tg) tg.style.opacity = D.tags.some(([s, e]) => T >= s && T < e) ? 1 : 0;
  };
})();
