// Injected into each engine page: hides the engine UI, draws badge, text, captions, sparkles, fireworks, emoji pops (happy, Disney-style).
(() => {
  const css = `#brand,#count,#title,#end,#sub,#cm,#tags{display:none!important}
  #ov{position:absolute;inset:0;pointer-events:none;font-family:Nunito,sans-serif;z-index:5;overflow:hidden}
  #ov .glow{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(255,236,170,.32) 0%,rgba(255,236,170,0) 55%),radial-gradient(ellipse at 50% 60%,rgba(0,0,0,0) 55%,rgba(255,170,90,.18) 100%)}
  #ov .brand{position:absolute;top:226px;left:0;right:0;text-align:center}
  #ov .brand span{display:inline-block;background:rgba(255,255,255,.95);color:#2F5FE0;font-weight:900;font-size:32px;letter-spacing:.08em;padding:10px 26px;border-radius:999px;box-shadow:0 8px 24px rgba(20,40,90,.18)}
  #ov .cnt{position:absolute;top:288px;left:0;right:0;text-align:center}
  #ov .cnt b{display:block;font-weight:900;font-size:104px;line-height:1;color:#fff;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cnt b.g{color:#FFD23F}
  #ov .cnt span{display:inline-block;margin-top:6px;background:#1B2333;color:#fff;font-weight:900;font-size:32px;padding:7px 24px;border-radius:999px}
  #ov .big{position:absolute;left:50px;right:180px;top:500px;text-align:center;font-weight:900;font-size:92px;line-height:1.06;color:#fff;-webkit-text-stroke:17px #1B2333;paint-order:stroke fill;text-shadow:0 12px 0 rgba(27,35,51,.45),0 0 40px rgba(27,35,51,.3)}
  #ov .big.huge{font-size:190px;top:470px}
  #ov .big y{color:#FFD23F} #ov .big g{color:#8CEB6B}
  #ov .cap{position:absolute;left:50px;right:180px;top:1300px;text-align:center;font-weight:900;font-size:62px;line-height:1.15}
  #ov .cap span{display:inline-block;margin:0 8px;color:#fff;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cap span.on{color:#FFD23F}
  #ov .sp{position:absolute;color:#FFE27A;text-shadow:0 0 18px #fff,0 0 30px rgba(255,210,63,.9);font-weight:900;line-height:1;transform-origin:center}
  #ov .fw{position:absolute;width:16px;height:16px;border-radius:50%}
  #ov .em{position:absolute;line-height:1;transform-origin:50% 100%}
  #ov .bub{position:absolute;left:330px;top:900px;background:#fff;color:#1B2333;font-weight:900;font-size:54px;padding:16px 34px;border-radius:40px;box-shadow:0 10px 28px rgba(0,0,0,.3);transform-origin:30% 100%}
  #ov .bub:after{content:'';position:absolute;left:90px;bottom:-26px;border:16px solid transparent;border-top:20px solid #fff}
  #ov .htag{position:absolute;background:#1B2333;color:#fff;font-weight:900;font-size:58px;padding:12px 34px;border-radius:26px;border:5px solid #fff;box-shadow:0 10px 24px rgba(0,0,0,.3);white-space:nowrap;text-align:center;line-height:1.05;transform-origin:50% 100%}
  #ov .htag small{display:block;font-size:34px;color:#FFD23F}
  #ov .ex{position:absolute;background:#E8384F;color:#fff;font-weight:900;font-size:32px;letter-spacing:.06em;padding:5px 16px;border-radius:12px;border:4px solid #fff;box-shadow:0 8px 20px rgba(0,0,0,.25)}
  #ov .chip{position:absolute;left:70px;top:1110px;display:flex;align-items:center;gap:18px;background:rgba(255,255,255,.97);border-radius:999px;padding:14px 38px 14px 16px;box-shadow:0 10px 26px rgba(20,40,90,.25);transform-origin:left center}
  #ov .chip i{display:inline-flex;align-items:center;justify-content:center;width:68px;height:68px;border-radius:50%;font-style:normal;font-size:40px;background:#FF6BB5;color:#fff}
  #ov .chip b{font-weight:900;font-size:50px;color:#1B2333} #ov .chip em{font-style:normal;font-weight:800;font-size:30px;color:#7A8499;display:block}
`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  const ov = document.createElement('div'); ov.id = 'ov'; document.body.appendChild(ov);
  const cl = x => Math.min(1, Math.max(0, x));
  const back = x => { x = cl(x); const c = 1.70158; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
  const rnd = s => { const x = Math.sin(s * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };
  const POS = { A: [540, 1000], F: [560, 1000], B: [560, 960] };   // where the @you tag sits per shot
  const star = (x, y, sz, op, rot, k) => `<div class="sp" style="left:${x - sz / 2}px;top:${y - sz / 2}px;font-size:${sz}px;opacity:${op};transform:rotate(${rot}deg)">${k % 3 ? '✦' : '✧'}</div>`;
  window.ovDraw = (T, D) => {
    let h = '<div class="glow"></div>';
    h += `<div class="brand"><span>🐾 PETME2 CAT TOWN</span></div>`;
    const goal = T >= D.goal[0] && T < D.goal[1], R = D.roll;
    if (goal) { const rc = Math.round(R[2] + (R[3] - R[2]) * Math.pow(cl((T - R[0]) / (R[1] - R[0])), 1.6)); h += `<div class="cnt"><b class="g">${rc.toLocaleString('en-US')}</b><span>cats · THE DREAM ${rc >= 1000 ? '🎉' : ''}</span></div>`; }
    else h += `<div class="cnt"><b>${D.cats}</b><span>cat · Day ${D.day}</span></div>`;
    const beat = D.beats.find(x => T >= x.s && T < x.e);
    if (beat) { const k = beat.still || beat.nopop ? 1 : back((T - beat.s) / .3); h += `<div class="big${beat.huge ? ' huge' : ''}" style="transform:scale(${.6 + .4 * k});opacity:${beat.still || beat.nopop ? 1 : cl((T - beat.s) / .1)}">${beat.html}</div>`; }
    for (const [s, e, sh, html] of D.htags) if (T >= s && T < e) { const [x, y] = POS[sh]; h += `<div class="htag" style="left:${x - 230}px;top:${y - 150}px;width:400px;transform:scale(${back((T - s) / .35)})">${html}</div>`; }
    for (const [s, e, w] of D.example) if (T >= s && T < e) { const [x, y] = w === 'chip' ? [730, 1095] : [POS[w][0] - 250, POS[w][1] - 190]; h += `<div class="ex" style="left:${x}px;top:${y}px;transform:rotate(-6deg) scale(${back((T - s) / .3)})">EXAMPLE</div>`; }
    for (const [s, e, by, txt] of D.chips) if (T >= s && T < e) h += `<div class="chip" style="transform:scale(${back((T - s) / .3) * (T > e - .2 ? cl((e - T) / .2) : 1)})"><i>💬</i><div><em>@${by}</em><b>${txt}</b></div></div>`;
    for (const [s, e, x, y, em, sz, an] of D.emojis) if (T >= s && T < e) { const a = T - s; let tf = `scale(${back(a / .35)})`;
      if (an === 'boing') tf = `scale(${1 + .25 * Math.sin(a * 22) * Math.exp(-a * 4)},${back(a / .3) * (1 - .25 * Math.sin(a * 22) * Math.exp(-a * 4))})`;
      if (an === 'wave') tf = `scale(${back(a / .3)}) rotate(${22 * Math.sin(a * 11)}deg)`;
      h += `<div class="em" style="left:${x}px;top:${y}px;font-size:${sz}px;transform:${tf}">${em}</div>`; }
    for (const [s, e, txt] of D.bubbles) if (T >= s && T < e) h += `<div class="bub" style="transform:scale(${back((T - s) / .3)})">${txt}</div>`;
    D.sparkle.forEach(([t0, kind, x0, y0, x1, y1, n], si) => { const a = T - t0; if (a < 0 || a > 1.4) return;
      for (let i = 0; i < n; i++) { const r1 = rnd(si * 100 + i), r2 = rnd(si * 100 + i + 50), r3 = rnd(si * 100 + i + 77); let x, y, op, sz = 30 + 50 * r3;
        if (kind === 'burst') { const ang = r1 * 6.283, sp = 260 + 420 * r2, f = 1 - Math.exp(-a * 4); x = x0 + Math.cos(ang) * sp * f; y = y0 + Math.sin(ang) * sp * f + 120 * a * a; op = cl(1 - a / 1.1); }
        else if (kind === 'swirl') { const d = i / n * .7, b = a - d; if (b < 0) continue; const ang = b * 9 + r1 * .6, rad = 330 * (1 - b / 1.2); x = x0 + Math.cos(ang) * rad; y = y0 + Math.sin(ang) * rad * .7; op = cl(1 - b / 1.0); }
        else if (kind === 'trail') { const d = i / n * .6, b = a - d; if (b < 0) continue; const f = cl(b / .25); x = x0 + (x1 - x0) * (d / .6) + 30 * (r1 - .5); y = y0 + (y1 - y0) * (d / .6) + 30 * (r2 - .5); op = cl(1 - b / .7) * f; }
        else { const b = a / .45; x = -200 + 1480 * b + 240 * (r1 - .5) - 400 * r2 + 200; y = 1920 * r2; sz = 50 + 90 * r3; op = cl(1.6 - Math.abs(b * 1480 - 200 - 1480 * r2 * .3 - (x + 200)) / 600); if (a > .45) op *= cl(1 - (a - .45) / .1); }
        h += star(x, y, sz, op * (.75 + .25 * Math.sin(T * 30 + i)), a * 200 + r1 * 90, i); } });
    for (const [t0, x0, y0, c] of D.fireworks) { const a = T - t0; if (a < 0 || a > 1.3) continue;
      for (let i = 0; i < 26; i++) { const ang = i / 26 * 6.283, f = 1 - Math.exp(-a * 5), r = 230 * f; h += `<div class="fw" style="left:${x0 + Math.cos(ang) * r}px;top:${y0 + Math.sin(ang) * r + 90 * a * a}px;background:${c};opacity:${cl(1 - a / 1.2)};box-shadow:0 0 18px ${c}"></div>`; } }
    const line = [...D.lines].reverse().find(l => T >= l.s - .05 && T < l.e + .3);
    if (line) h += `<div class="cap" style="font-size:${line.words.length > 8 ? 54 : 62}px">${line.words.map(w => `<span class="${T >= w.s && T < w.e + .05 ? 'on' : ''}">${w.w}</span>`).join(' ')}</div>`;
    const cv = document.querySelector('canvas'); if (cv) cv.style.filter = D.grade;
    ov.innerHTML = h;
  };
})();
