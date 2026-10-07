// Photo look for the rules story (v2, "catchier"): replaces ovDraw from ../story-1/overlay.js.
// Per card: tilted RULE tag, big headline, white sticker pill, optional Mango speech bubble. Brand pill only (no counter).
(() => {
  const css = `#ov .brand{top:222px!important} #ov .brand span{font-size:28px!important;padding:8px 22px!important}
  #ov .shade{position:absolute;left:0;right:0;top:0;height:900px;background:linear-gradient(rgba(20,28,48,.45),rgba(20,28,48,0))}
  #ov .tag2{position:absolute;left:0;right:0;top:330px;text-align:center}
  #ov .tag2 span{display:inline-block;background:#FF4F8B;color:#fff;font-weight:900;font-size:46px;letter-spacing:.06em;padding:10px 30px;border-radius:18px;border:5px solid #fff;transform:rotate(-5deg);box-shadow:0 10px 24px rgba(0,0,0,.25)}
  #ov .h{position:absolute;left:40px;right:40px;text-align:center;font-weight:900;font-size:112px;line-height:1.02;color:#fff;-webkit-text-stroke:16px #1B2333;paint-order:stroke fill;text-shadow:0 12px 0 rgba(27,35,51,.35)}
  #ov .h y{color:#FFD23F}
  #ov .pill{position:absolute;left:0;right:0;text-align:center}
  #ov .pill span{display:inline-block;background:#fff;color:#1B2333;font-weight:900;font-size:50px;padding:16px 34px;border-radius:999px;transform:rotate(2deg);box-shadow:0 12px 28px rgba(20,40,90,.28)}
  #ov .pill span b{color:#FF4F8B}
  #ov .bub{position:absolute;background:#fff;color:#1B2333;font-weight:900;font-size:54px;line-height:1.1;padding:22px 34px;border-radius:44px;border:6px solid #1B2333;box-shadow:0 12px 0 rgba(27,35,51,.25)}
  #ov .bub:after{content:'';position:absolute;bottom:-40px;width:0;height:0;border:22px solid transparent;border-top:24px solid #1B2333}
  #ov .bub.l:after{left:56px} #ov .bub.r:after{right:56px}
  #ov .ex{position:absolute;background:#E8384F;color:#fff;font-weight:900;font-size:34px;letter-spacing:.06em;padding:6px 18px;border-radius:12px;border:4px solid #fff;transform:rotate(-6deg)}`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  const ov = document.getElementById('ov');
  window.ovDraw = (T, D) => {
    const c = D.cards.find(x => T >= x.s && T < x.e); if (!c) return;
    let h = `<div class="shade"></div><div class="brand"><span>🐾 PETME2 CAT TOWN</span></div>`;
    let y = 330;
    if (c.tag) { h += `<div class="tag2"><span>${c.tag}</span></div>`; y = 440; }
    h += `<div class="h" style="top:${y}px">${c.html}</div>`;
    const lines = (c.html.match(/<br>/g) || []).length + 1;
    if (c.pill) h += `<div class="pill" style="top:${c.pillY || y + lines * 114 + 30}px"><span>${c.pill}</span></div>`;
    if (c.pill2) h += `<div class="pill" style="top:${y + lines * 114 + 30}px"><span style="transform:rotate(-2deg);background:#FFD23F">${c.pill2}</span></div>`;
    if (c.bub) h += `<div class="bub ${c.bub.side || 'l'}" style="left:${c.bub.x}px;top:${c.bub.y}px">${c.bub.text}</div>`;
    for (const [x, yy] of c.ex || []) h += `<div class="ex" style="left:${x}px;top:${yy}px">EXAMPLE</div>`;
    ov.innerHTML = h;
    const tg = document.getElementById('tags'); if (tg) { tg.style.opacity = c.hideTags ? 0 : 1; tg.classList.toggle('pin', !!c.pinTags); }
  };
})();
