// Injected into each engine page: hides the engine's own UI (keeps the comment card + build tag), draws the badge + text layer.
(() => {
  const css = `#brand,#count,#title,#end,#sub{display:none!important}
  #cm{top:800px!important;right:140px!important}
  #ov{position:absolute;inset:0;pointer-events:none;font-family:Nunito,sans-serif;z-index:5}
  #ov .brand{position:absolute;top:226px;left:0;right:0;text-align:center}
  #ov .brand span{display:inline-block;background:rgba(255,255,255,.95);color:#2F5FE0;font-weight:900;font-size:32px;letter-spacing:.08em;padding:10px 26px;border-radius:999px;box-shadow:0 8px 24px rgba(20,40,90,.18)}
  #ov .cnt{position:absolute;top:288px;left:0;right:0;text-align:center}
  #ov .cnt b{display:block;font-weight:900;font-size:104px;line-height:1;color:#fff;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cnt b.g{color:#FFD23F}
  #ov .cnt span{display:inline-block;margin-top:6px;background:#1B2333;color:#fff;font-weight:900;font-size:32px;padding:7px 24px;border-radius:999px}
  #ov .big{position:absolute;left:50px;right:180px;top:500px;text-align:center;font-weight:900;font-size:96px;line-height:1.04;color:#fff;-webkit-text-stroke:14px #1B2333;paint-order:stroke fill;text-shadow:0 12px 0 rgba(27,35,51,.45),0 0 40px rgba(27,35,51,.35)}
  #ov .big y{color:#FFD23F} #ov .big r{color:#FF6B6B}
  #ov .small{position:absolute;left:50px;right:180px;top:712px;text-align:center;font-weight:900;font-size:60px;color:#FFD23F;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .ex{position:absolute;background:#E8384F;color:#fff;font-weight:900;font-size:34px;letter-spacing:.06em;padding:6px 18px;border-radius:12px;border:4px solid #fff;box-shadow:0 8px 20px rgba(0,0,0,.25);transform-origin:left center}
  #ov .arrow{position:absolute;left:800px;top:1110px;font-size:110px}
  #ov .cap{position:absolute;left:50px;right:180px;top:1290px;text-align:center;font-weight:900;font-size:64px;line-height:1.15}
  #ov .cap span{display:inline-block;margin:0 8px;color:#fff;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cap span.on{color:#FFD23F}
  #ov .chip{position:absolute;left:70px;display:flex;align-items:center;gap:18px;background:rgba(255,255,255,.96);border-radius:999px;padding:12px 34px 12px 14px;box-shadow:0 10px 26px rgba(20,40,90,.25);transform-origin:left center}
  #ov .chip i{display:inline-flex;align-items:center;justify-content:center;width:64px;height:64px;border-radius:50%;font-style:normal;font-size:36px;font-weight:900;color:#fff}
  #ov .chip b{font-weight:900;font-size:46px;color:#1B2333} #ov .chip em{font-style:normal;font-weight:800;font-size:30px;color:#7A8499;margin-right:6px}
  #ov .tint{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 55%,rgba(40,60,110,0) 35%,rgba(20,30,60,.55) 100%),rgba(70,100,170,.16)}
  #ov .flash{position:absolute;inset:0;background:radial-gradient(circle at 50% 50%,#fff 0%,rgba(255,236,170,.85) 45%,rgba(255,210,63,0) 85%)}
  #ov .bub{position:absolute;left:300px;top:930px;background:#fff;color:#1B2333;font-weight:900;font-size:50px;padding:16px 34px;border-radius:40px;box-shadow:0 10px 28px rgba(0,0,0,.3);transform-origin:30% 100%}
  #ov .bub:after{content:'';position:absolute;left:90px;bottom:-26px;border:16px solid transparent;border-top:20px solid #fff}
  #ov .htag{position:absolute;background:#1B2333;color:#fff;font-weight:900;font-size:56px;padding:12px 30px;border-radius:24px;border:5px solid #fff;box-shadow:0 10px 24px rgba(0,0,0,.3);white-space:nowrap;text-align:center;line-height:1.05;transform-origin:50% 100%}
  #ov .htag small{display:block;font-size:32px;color:#FFD23F}
  #ov .plus{position:absolute;font-weight:900;font-size:110px;color:#FFD23F;-webkit-text-stroke:12px #1B2333;paint-order:stroke fill;white-space:nowrap}
  .tag{font-size:42px!important}
  #tags.pin .tag{top:900px!important}
`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  const ov = document.createElement('div'); ov.id = 'ov'; document.body.appendChild(ov);
  const back = x => { x = Math.min(1, Math.max(0, x)); const c = 1.70158; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
  window.ovDraw = (T, D) => {
    const end = 1;   // the last beat repeats the hook text, so the loop lands on frame 0 with text
    let h = '', b = '', h0 = '';
    const goal = T >= D.goal[0] && T < D.goal[1];
    b += `<div class="brand"><span>🐾 PETME2 CAT TOWN</span></div>`;
    const R = D.roll, rc = R ? Math.round(R[2] + (R[3] - R[2]) * Math.pow(Math.min(1, Math.max(0, (T - R[0]) / (R[1] - R[0]))), 1.6)) : 1000;
    b += goal ? `<div class="cnt"><b class="g">${rc.toLocaleString('en-US')}</b><span>${rc >= 1000 ? 'cats · THE DREAM 🎉' : 'cats · THE DREAM'}</span></div>` : `<div class="cnt"><b>${D.cats}</b><span>${D.cats === 1 ? 'cat' : 'cats'} · Day ${D.day}</span></div>`;
    const beat = D.beats.find(x => T >= x.s && T < x.e);
    if (beat) { const k = beat.still ? 1 : back((T - beat.s) / .3); h += `<div class="big" style="transform:scale(${.6 + .4 * k});opacity:${beat.still ? 1 : Math.min(1, (T - beat.s) / .1)}">${beat.html}</div>`;
      if (beat.small && T >= beat.ss) h += `<div class="small" style="transform:scale(${back((T - beat.ss) / .3)})">${beat.small}</div>`;
      if (beat.small2 && T >= beat.ss2) h += `<div class="small" style="top:790px;color:#fff;transform:scale(${back((T - beat.ss2) / .3)})">${beat.small2}</div>`;
      if (beat.arrow) { const a = T - beat.s - .5; if (a > 0) h += `<div class="arrow" style="transform:translateX(${18 * Math.sin(a * 9)}px) scale(${back(a / .3)})">👉</div>`; } }
    const g0 = (D.grade || []).find(([s, e]) => T >= s && T < e); if (g0 && g0[3]) h0 += `<div class="tint"></div>`;
    if (D.flash && T >= D.flash && T < D.flash + .3) h0 += `<div class="flash" style="opacity:${1 - (T - D.flash) / .3}"></div>`;
    for (const [s, e, txt] of (D.bubbles || [])) if (T >= s && T < e) h += `<div class="bub" style="transform:scale(${back((T - s) / .3)})">${txt}</div>`;
    for (const [s, e, kind] of D.example) { if (T < s || T >= e) continue; const k = back((T - s) / .3);
      let x = 96, y = 1064;
      if (kind === 'house') { const tg = [...document.querySelectorAll('#tags .tag')].find(el => el.style.display === 'block'); if (!tg) continue; const r0 = tg.getBoundingClientRect(), r = { left: r0.left, width: r0.width, top: 950 }; const cx = Math.min(820, Math.max(260, r.left + r.width / 2));
        const pk = (D.pops || []).filter(p => T >= p).pop(), pa = T - pk;
        h += `<div class="htag" style="left:${cx - 190}px;top:${r.top - 60}px;width:320px;transform:scale(${back(pa / .3)})">@you<small>🐱 moved in</small></div>`;
        if (pa < 1) h += `<div class="plus" style="left:${Math.min(700, cx + 120)}px;top:${r.top + 80 - 90 * pa}px;opacity:${Math.min(1, 3 * (1 - pa))};transform:scale(${back(pa / .25)})">+1 🐱</div>`;
        x = cx - 230; y = r.top - 92; }
      if (kind === 'statue') { x = 200; y = 1180; }
      if (kind === 'card') { x = 96; y = 1064; }
      if (kind === 'chips') { x = 640; y = 1060; }
      h += `<div class="ex" style="left:${x}px;top:${y}px;transform:rotate(-6deg) scale(${k})">EXAMPLE</div>`; }
    const COL = ['#FF6B6B', '#2F5FE0', '#22B07D', '#B36BFF', '#FF9F1C'];
    const nc = (D.chips || []).filter(c => T >= c[0]).length;   // comment chips stack up, newest at the bottom
    if (T < 13.4) (D.chips || []).forEach(([s, name], i) => { if (T < s) return; const k = back((T - s) / .3);
      h += `<div class="chip" style="top:1170px;transform:translateY(${(i - (nc - 1)) * 96}px) scale(${k})"><i style="background:${COL[i % 5]}">${name[0]}</i><em>💬</em><b>${name}</b></div>`; });
    const line = [...D.lines].reverse().find(l => !l.hide && T >= l.s - .05 && T < l.e + .3);
    if (line) h += `<div class="cap">${line.words.map(w => `<span class="${T >= w.s && T < w.e + .05 ? 'on' : ''}">${w.w}</span>`).join(' ')}</div>`;
    const g = (D.grade || []).find(([s, e]) => T >= s && T < e); const cv = document.querySelector('canvas'); if (cv && g) cv.style.filter = g[2];
    ov.innerHTML = h0 + b + `<div style="opacity:${end}">${h}</div>`;
    const tg = document.getElementById('tags'); if (tg) tg.style.opacity = (D.hideTags || []).some(([s, e]) => T >= s && T < e) ? 0 : 1; if (tg && (D.pinTags || []).some(([s, e]) => T >= s && T < e)) tg.style.opacity = 0; if (tg) tg.classList.toggle('pin', (D.pinTags || []).some(([s, e]) => T >= s && T < e));
  };
})();
