// Day 9 overlay (from day-8-dogs/overlay.js): opens on Day 8's sepia freeze + "TO BE CONTINUED" arrow, a red PART 2 stamp slams in, colour snaps back.
// Movie bars, badge, big beat text, word-by-word captions (the general's words light up red, Mango's yellow), a sunrise countdown clock,
// then the new cliffhanger: freeze + sepia + "TO BE CONTINUED", and the Day 10 end card.
(() => {
  const css = `#brand,#count,#title,#end,#sub,#cm,#tags{display:none!important}
  #ov{position:absolute;inset:0;pointer-events:none;font-family:Nunito,sans-serif;z-index:5}
  #ov .bar{position:absolute;left:0;right:0;height:130px;background:#000}
  #ov .brand{position:absolute;top:226px;left:0;right:0;text-align:center}
  #ov .brand span{display:inline-block;background:rgba(255,255,255,.95);color:#2F5FE0;font-weight:900;font-size:32px;letter-spacing:.08em;padding:10px 26px;border-radius:999px;box-shadow:0 8px 24px rgba(20,40,90,.18)}
  #ov .big{position:absolute;left:50px;right:50px;top:470px;text-align:center;font-weight:900;font-size:96px;line-height:1.04;color:#fff;-webkit-text-stroke:14px #1B2333;paint-order:stroke fill;text-shadow:0 12px 0 rgba(27,35,51,.3)}
  #ov .big y{color:#FFD23F} #ov .big r{color:#FF4B4B}
  #ov .small{position:absolute;left:60px;right:60px;top:712px;text-align:center;font-weight:900;font-size:56px;color:#FFD23F;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cap{position:absolute;left:60px;right:60px;top:1500px;text-align:center;font-weight:900;font-size:64px;line-height:1.15}
  #ov .cap span{display:inline-block;margin:0 8px;color:#fff;-webkit-text-stroke:11px #1B2333;paint-order:stroke fill}
  #ov .cap span.on{color:#FFD23F} #ov .cap.dog span.on{color:#FF5A5A} #ov .cap.dog span{font-size:70px}
  #ov .clock{position:absolute;top:330px;left:0;right:0;text-align:center}
  #ov .clock span{display:inline-block;background:rgba(20,16,30,.82);color:#FFB36B;font-weight:900;font-size:40px;padding:10px 26px;border-radius:18px;border:4px solid #FF8A3C;font-variant-numeric:tabular-nums;letter-spacing:.03em}
  #ov .stamp{position:absolute;left:0;right:0;top:820px;text-align:center}
  #ov .stamp span{display:inline-block;font-weight:900;font-size:150px;color:#FF3B3B;border:14px solid #FF3B3B;border-radius:28px;padding:0 44px;transform:rotate(-8deg);background:rgba(255,255,255,.12);letter-spacing:.04em}
  #ov .tbc{position:absolute;left:46px;top:1260px;display:flex;align-items:center}
  #ov .tbc .ar{width:0;height:0;border-top:62px solid transparent;border-bottom:62px solid transparent;border-right:84px solid #3A2A1A}
  #ov .tbc .tx{background:#3A2A1A;color:#F3E2C0;font-weight:900;font-size:58px;letter-spacing:.04em;height:124px;line-height:124px;padding:0 40px 0 14px;border-radius:0 18px 18px 0;font-style:italic}
  #ov .flash{position:absolute;inset:0;background:#fff}
  #ov .endc{position:absolute;left:60px;right:60px;top:290px;text-align:center}
  #ov .endc .t1{font-weight:900;font-size:50px;color:#F3E2C0;letter-spacing:.12em;margin-bottom:34px}
  #ov .endc .t2{font-weight:900;font-size:112px;line-height:1.02;color:#fff;-webkit-text-stroke:14px #1B2333;paint-order:stroke fill}
  #ov .endc .t2 y{color:#FFD23F}
  #ov .chip{display:inline-block;font-weight:900;font-size:46px;color:#1B2333;background:#FFD23F;padding:14px 34px;border-radius:999px;border:6px solid #1B2333;margin-top:30px}
  #ov .chip.w{background:#fff} #ov .chip.o{background:#FF8A3C}
`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  const ov = document.createElement('div'); ov.id = 'ov'; document.body.appendChild(ov);
  const cv = document.querySelector('canvas');
  const back = x => { x = Math.min(1, Math.max(0, x)); const c = 1.70158; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
  const ease = x => { x = Math.min(1, Math.max(0, x)); return 1 - Math.pow(1 - x, 3); };
  const OPEN = 1.2;   // Day 8's freeze until here, then colour snaps back
  window.ovDraw = (T, D) => {
    let h = '';
    const F = D.freeze, END = F + 1.8;
    cv.style.filter = T < OPEN ? 'sepia(.85) contrast(1.08) brightness(.92)' : T < F ? 'none' : T < END ? `sepia(${.85 * ease((T - F) / .15)}) contrast(1.08) brightness(.92)` : `sepia(.85) brightness(${.92 - .62 * ease((T - END) / .4)}) blur(${6 * ease((T - END) / .4)}px)`;
    if (T < END) h += `<div class="bar" style="top:0"></div><div class="bar" style="bottom:0"></div>`;
    if (T < F && T >= OPEN) h += `<div class="brand"><span>🐾 PETME2 CAT TOWN</span></div>`;
    if (T < OPEN) { h += `<div class="tbc" style="transform:translateX(${-700 * ease((T - .75) / .4)}px)"><div class="ar"></div><div class="tx">TO BE CONTINUED</div></div>`;
      if (T >= .35) h += `<div class="stamp"><span style="transform:rotate(-8deg) scale(${1 + 1.4 * (1 - ease((T - .35) / .16))});opacity:${Math.min(1, (T - .35) / .08)}">PART 2</span></div>`; }
    if (T >= OPEN && T < OPEN + .25) h += `<div class="flash" style="opacity:${.85 * (1 - (T - OPEN) / .25)}"></div>`;
    const beat = D.beats.find(x => T >= x.s && T < x.e);
    if (beat && !beat.tbc) { const kk = beat.still ? 1 : back((T - beat.s) / (beat.pop ? .18 : .3)); h += `<div class="big" style="transform:scale(${.6 + .4 * kk});opacity:${beat.still ? 1 : Math.min(1, (T - beat.s) / .1)}">${beat.html}</div>`;
      if (beat.small && T >= beat.ss) h += `<div class="small" style="transform:scale(${back((T - beat.ss) / .3)})">${beat.small}</div>`; }
    if (D.clock && T >= D.clock[0] && T < F) {   // the sunrise countdown: 10 hours run down fast through the night
      const k = (T - D.clock[0]) / (D.clock[1] - D.clock[0]), s = Math.max(0, Math.round(36000 - 26000 * k)), hh = Math.floor(s / 3600), mm = Math.floor(s / 60) % 60, ss = s % 60;
      h += `<div class="clock" style="transform:scale(${back((T - D.clock[0]) / .35)})"><span>🌅 ATTACK IN ${hh}:${String(mm).padStart(2, '0')}:${String(ss).padStart(2, '0')}</span></div>`; }
    if (T >= F && T < END) { const k = ease((T - F - .25) / .35); h += `<div class="tbc" style="transform:translateX(${-700 * (1 - k)}px)"><div class="ar"></div><div class="tx">TO BE CONTINUED</div></div>`; }
    if (T >= END) { const k = (T - END) / .45;
      h += `<div class="endc" style="opacity:${ease(k)}"><div class="t1">TO BE CONTINUED...</div>
        <div class="t2" style="transform:scale(${.7 + .3 * back(k)})">DAY 10:<br>WHAT DID THE<br><y>SPY SEE?</y> 👀</div>
        <div style="transform:scale(${back((T - END - .6) / .35)})"><span class="chip">💬 GUESS IN THE COMMENTS</span></div>
        <div style="transform:scale(${back((T - END - 1.0) / .35)})"><span class="chip o">🌅 THE DOGS ATTACK AT SUNRISE</span></div>
        <div style="transform:scale(${back((T - END - 1.4) / .35)})"><span class="chip w">🐱 FOLLOW = 1 MORE CAT<br>IN THE ARMY ⚔️</span></div></div>`; }
    const line = D.lines.find(l => T >= l.s - .05 && T < l.e + .3);
    if (line && T < END) h += `<div class="cap ${line.who}">${line.words.map(w => `<span class="${T >= w.s && T < w.e + .05 ? 'on' : ''}">${w.w}</span>`).join(' ')}</div>`;
    ov.innerHTML = h;
  };
})();
