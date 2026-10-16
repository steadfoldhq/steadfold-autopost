// Steadfold motion kit: deterministic runtime. window.seek(t) puts every element in its state for time t (seconds).
// The Python side (kit.py) renders frame by frame with Playwright, adds sub-frame motion blur and post effects.
(function () {
  const W = 1080, H = 1920;
  const cl = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const E = {
    lin: p => p,
    inC: p => p * p * p,
    outC: p => 1 - Math.pow(1 - p, 3),
    outQ: p => 1 - (1 - p) * (1 - p),
    io: p => (p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2),
    expo: p => (p <= 0 ? 0 : p >= 1 ? 1 : p < .5 ? Math.pow(2, 20 * p - 10) / 2 : (2 - Math.pow(2, -20 * p + 10)) / 2),
    back: p => { const c1 = 2.2, c3 = c1 + 1; return 1 + c3 * Math.pow(p - 1, 3) + c1 * Math.pow(p - 1, 2); },
    el: p => (p <= 0 ? 0 : p >= 1 ? 1 : Math.pow(2, -10 * p) * Math.sin((p * 10 - .75) * (2 * Math.PI) / 3) + 1),
  };
  const rnd = s => { const x = Math.sin(s * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };
  const FAST = new Set(['whipL', 'whipR', 'whipU', 'whipD', 'zoom', 'spin', 'stripes', 'slam', 'push']);
  let TL, scenes, ov, stage;

  function init(tl) {
    TL = tl;
    stage = document.getElementById('stage');
    ov = document.getElementById('ov');
    scenes = [...document.querySelectorAll('.scene')];
    autofit();
    document.querySelectorAll('[data-a=type]').forEach(el => { el.dataset.full = el.textContent; });
    document.querySelectorAll('[data-a=draw]').forEach(p => {
      const L = p.getTotalLength ? p.getTotalLength() : 1000; p.dataset.len = L;
      p.style.strokeDasharray = L; p.style.strokeDashoffset = L;
    });
  }

  // Shrink any text block whose lines would leave the safe width (x 80-1000) once the camera pushes in.
  function autofit() {
    scenes.forEach(sc => {
      sc.style.display = 'block';
      sc.querySelectorAll('.el').forEach(el => {
        if (!el.textContent.trim() || el.querySelector('.el') || el.tagName === 'svg') return;
        if (!(el.dataset.a === 'words' || el.style.width === '1080px')) return;  // text blocks only, never cards
        for (let k = 0; k < 6; k++) {
          const rg = document.createRange(); rg.selectNodeContents(el);
          let lo = 1e9, hi = -1e9;
          for (const r of rg.getClientRects()) { if (r.width < 1) continue; lo = Math.min(lo, r.left); hi = Math.max(hi, r.right); }
          const wdt = hi - lo;
          if (!(wdt > 920)) break;
          const fs = parseFloat(getComputedStyle(el).fontSize);
          el.style.fontSize = (fs * 915 / wdt) + 'px';
        }
      });
      sc.style.display = 'none';
    });
  }

  // ---------------------------------------------------------------- element animations
  function fmt(v, el) {
    const dec = +(el.dataset.dec || 0), pre = el.dataset.pre || '', suf = el.dataset.suf || '', pad = +(el.dataset.pad || 0);
    if (el.dataset.mmss) { const T = Math.max(0, Math.round(v)); return pre + String(Math.floor(T / 60)).padStart(2, '0') + ':' + String(T % 60).padStart(2, '0') + suf; }
    let s = v.toFixed(dec);
    if (el.dataset.comma) s = (+s).toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec });
    if (pad) s = s.padStart(pad, '0');
    return pre + s + suf;
  }
  function animEl(el, u, t) {
    const a = el.dataset.a, d = +(el.dataset.d || .4), r0 = +(el.dataset.r || 0);
    const p = cl(u / d);
    let tf = '', op = 1;
    switch (a) {
      case 'none': break;
      case 'fade': op = E.outQ(p); break;
      case 'pop': { const s = u < 0 ? 0 : .25 + .75 * E.back(p); tf = `scale(${s})`; op = cl(u / (d * .25)); break; }
      case 'stamp': { const s = 1 + 1.1 * (1 - E.outC(p)); tf = `scale(${s}) rotate(${r0 * (1 - E.outC(p)) * 2}deg)`; op = cl(u / (d * .3)); break; }
      case 'up': tf = `translateY(${(1 - E.outC(p)) * 110}px)`; op = cl(u / (d * .5)); break;
      case 'down': tf = `translateY(${-(1 - E.outC(p)) * 110}px)`; op = cl(u / (d * .5)); break;
      case 'left': tf = `translateX(${(1 - E.outC(p)) * 260}px)`; op = cl(u / (d * .4)); break;
      case 'right': tf = `translateX(${-(1 - E.outC(p)) * 260}px)`; op = cl(u / (d * .4)); break;
      case 'fly': { // object flies in from below-right with spin and lands with overshoot
        const q = E.back(p); tf = `translate(${(1 - q) * 500}px,${(1 - q) * 900}px) rotate(${(1 - q) * 70}deg)`; op = u < 0 ? 0 : 1; break; }
      case 'drop': { const q = E.el(p); tf = `translateY(${(1 - q) * -700}px)`; op = u < 0 ? 0 : 1; break; }
      case 'scroll': tf = `translateY(${-E.io(p) * +(el.dataset.to || 600)}px)`; op = 1; break;
      case 'wipe': el.style.clipPath = `inset(-20% ${(1 - E.io(p)) * 100}% -20% 0)`; break;
      case 'wipeD': el.style.clipPath = `inset(0 0 ${(1 - E.io(p)) * 100}% 0)`; break;
      case 'hl': el.style.backgroundSize = `${E.io(p) * 100}% 100%`; break;
      case 'strike': { const sk = el.querySelector('.sk'); if (sk) sk.style.width = `${E.io(p) * 100}%`; break; }
      case 'bar': el.style.width = `${E.io(p) * +(el.dataset.to || 100)}%`; break;
      case 'draw': el.style.strokeDashoffset = (+el.dataset.len) * (1 - E.io(p)); break;
      case 'type': { const f = el.dataset.full; const n = Math.round(cl(u / d) * f.length); el.textContent = f.slice(0, n); break; }
      case 'count': { const from = +(el.dataset.from || 0), to = +el.dataset.to; el.textContent = fmt(from + (to - from) * E.outC(p), el); break; }
      case 'tick': { const from = +(el.dataset.from || 0), to = +el.dataset.to; el.textContent = fmt(from + (to - from) * p, el); break; }
      case 'words': {
        const gap = +(el.dataset.gap || .12);
        [...el.querySelectorAll('.w')].forEach((w, k) => {
          const uk = u - k * gap, q = cl(uk / d);
          const s = uk < 0 ? .4 : .55 + .45 * E.back(q);
          w.style.transform = `translateY(${(1 - E.outC(q)) * 50}px) scale(${s})`;
          w.style.opacity = cl(uk / (d * .3));
        });
        break;
      }
      case 'stack': { // children drop in one by one (notifications)
        const gap = +(el.dataset.gap || .15);
        [...el.children].forEach((c, k) => {
          const uk = u - k * gap, q = cl(uk / d);
          c.style.transform = `translateY(${(1 - E.back(q)) * -120}px) scale(${.8 + .2 * E.outC(q)})`;
          c.style.opacity = cl(uk / (d * .3));
        });
        break;
      }
    }
    // continuous loops after the entrance
    const lp = el.dataset.loop;
    if (lp && u > 0) {
      const tt = u, amp = +(el.dataset.amp || 1);
      if (lp === 'float') tf += ` translateY(${Math.sin(tt * 2.6) * 12 * amp}px) rotate(${Math.sin(tt * 1.9) * 2 * amp}deg)`;
      if (lp === 'wobble') tf += ` rotate(${Math.sin(tt * 9) * 5 * amp}deg)`;
      if (lp === 'pulse') tf += ` scale(${1 + Math.sin(tt * 7.2) * .035 * amp})`;
      if (lp === 'shake') { const k = Math.floor(t * 30); const dmp = Math.max(0, 1 - tt / 0.6); tf += ` translate(${(rnd(k) - .5) * 26 * amp * dmp}px,${(rnd(k + 9) - .5) * 26 * amp * dmp}px)`; }
      if (lp === 'buzz') { const k = Math.floor(t * 30); tf += ` translate(${(rnd(k) - .5) * 10 * amp}px,${(rnd(k + 3) - .5) * 6 * amp}px) rotate(${(rnd(k + 5) - .5) * 4 * amp}deg)`; }
      if (lp === 'spin') tf += ` rotate(${tt * 40 * amp}deg)`;
    }
    if (r0 && a !== 'stamp') tf += ` rotate(${r0}deg)`;
    el.style.transform = tf;
    if (!['wipe', 'hl', 'strike', 'bar', 'draw', 'type', 'count', 'tick', 'words', 'stack', 'wipeD'].includes(a)) el.style.opacity = op;
  }

  function animScene(i, local, t) {
    const sc = scenes[i];
    sc.querySelectorAll('[data-a]').forEach(el => animEl(el, local - +(el.dataset.t || 0), t));
    const cam = sc.querySelector('.cam');
    const s = TL.scenes[i], q = cl(local / Math.max(.3, s.dur));
    const mode = s.cam || 'push';
    let tf = '';
    if (mode === 'push') tf = `scale(${1 + .07 * q})`;
    if (mode === 'pull') tf = `scale(${1.08 - .07 * q})`;
    if (mode === 'left') tf = `scale(1.06) translateX(${(.5 - q) * 50}px)`;
    if (mode === 'right') tf = `scale(1.06) translateX(${(q - .5) * 50}px)`;
    if (mode === 'rise') tf = `scale(1.05) translateY(${(.5 - q) * 60}px)`;
    if (mode === 'tilt') tf = `scale(${1.04 + .04 * q}) rotate(${(q - .5) * 2.4}deg)`;
    // parallax: .bg layer inside cam moves less (counter-scale)
    if (cam) cam.style.transform = tf;
    const bgl = sc.querySelector('.par');
    if (bgl) bgl.style.transform = `scale(${1.12 + .05 * q}) translateY(${(q - .5) * -40}px)`;
  }

  function resetScene(sc) {
    sc.style.display = 'none'; sc.style.transform = ''; sc.style.clipPath = ''; sc.style.opacity = 1; sc.style.zIndex = 1;
    sc.style.filter = ''; sc.style.transformOrigin = '50% 50%';
  }

  // ---------------------------------------------------------------- transitions between scenes
  function trans(tr, A, B, p) {
    const fx = (tr.focus || [540, 960])[0], fy = (tr.focus || [540, 960])[1];
    const c = tr.color || '#FFC94D', c2 = tr.color2 || '#FFFFFF', c3 = tr.color3 || '#141414';
    let post = null;
    A.style.zIndex = 1; B.style.zIndex = 3; ov.style.zIndex = 2; ov.innerHTML = ''; ov.style.cssText = '';
    const show = (a, b) => { A.style.display = a ? 'block' : 'none'; B.style.display = b ? 'block' : 'none'; };
    const e = E.expo(p);
    switch (tr.type) {
      case 'cut': show(p < .5, p >= .5); break;
      case 'whipL': case 'whipR': {
        const s = tr.type === 'whipL' ? -1 : 1; show(true, true);
        A.style.transform = `translateX(${s * W * e}px)`; B.style.transform = `translateX(${-s * W * (1 - e)}px)`; break; }
      case 'whipU': case 'whipD': {
        const s = tr.type === 'whipU' ? -1 : 1; show(true, true);
        A.style.transform = `translateY(${s * H * e}px)`; B.style.transform = `translateY(${-s * H * (1 - e)}px)`; break; }
      case 'push': { // parallax push: A drifts and darkens, B slides over it with a shadow
        show(true, true);
        A.style.transform = `translateX(${-W * .35 * e}px) scale(${1 - .08 * e})`; A.style.filter = `brightness(${1 - .45 * e})`;
        B.style.transform = `translateX(${W * (1 - e)}px)`; B.style.boxShadow = '-40px 0 80px rgba(0,0,0,.35)'; break; }
      case 'zoom': { // punch through a focus point: A rushes in, B lands from big to 1
        A.style.transformOrigin = `${fx}px ${fy}px`; B.style.transformOrigin = `${fx}px ${fy}px`;
        if (p < .5) { const q = E.inC(p * 2); show(true, false); A.style.transform = `scale(${1 + 2.6 * q})`; }
        else { const q = E.outC((p - .5) * 2); show(false, true); B.style.transform = `scale(${2.2 - 1.2 * q})`; }
        break; }
      case 'pull': { // zoom out: A shrinks away into a card, B arrives from small
        if (p < .5) { const q = E.inC(p * 2); show(true, false); A.style.transform = `scale(${1 - .75 * q}) rotate(${-8 * q}deg)`; A.style.borderRadius = '60px'; }
        else { const q = E.outC((p - .5) * 2); show(false, true); B.style.transform = `scale(${.35 + .65 * q})`; }
        break; }
      case 'iris': { // two-tone shape wipe: a brand-colour circle leads, the next scene follows inside it
        show(true, true);
        const r1 = E.io(cl(p / .8)) * 2300, r2 = E.io(cl((p - .2) / .8)) * 2300;
        ov.style.cssText = `position:absolute;inset:0;clip-path:circle(${r1}px at ${fx}px ${fy}px);background:${c};z-index:2`;
        B.style.clipPath = `circle(${r2}px at ${fx}px ${fy}px)`; break; }
      case 'blob': { // soft rounded blob wipe (Littlefold): rounded rect grows from a point
        show(true, true);
        const q1 = E.io(cl(p / .8)), q2 = E.io(cl((p - .2) / .8));
        const rr = (q) => `inset(${(1 - q) * fy}px ${(1 - q) * (W - fx)}px ${(1 - q) * (H - fy)}px ${(1 - q) * fx}px round ${200 * (1 - q) + 60}px)`;
        ov.style.cssText = `position:absolute;inset:0;clip-path:${rr(q1)};background:${c};z-index:2`;
        B.style.clipPath = rr(q2); break; }
      case 'stripes': { // three diagonal highlighter bars sweep the frame; the scene swaps under them
        show(p < .5, p >= .5);
        const cols = [c, c2, c3];
        ov.style.cssText = 'position:absolute;inset:0;overflow:hidden;z-index:4';
        ov.innerHTML = cols.map((col, k) => {
          const q = E.io(cl((p - k * .08) / .84));
          const off = (q * 2 - 1) * 2600;
          return `<div style="position:absolute;left:-800px;top:${k * 640 - 300}px;width:2700px;height:${760}px;background:${col};transform:rotate(-24deg) translateX(${-off}px)"></div>`;
        }).join('');
        break; }
      case 'slit': { // the next scene opens from a horizontal slit, with accent edges
        show(true, true);
        const q = E.expo(p), half = (1 - q) * 50;
        B.style.clipPath = `inset(${half}% 0 ${half}% 0)`;
        const y1 = H * half / 100, y2 = H - y1;
        ov.style.cssText = 'position:absolute;inset:0;z-index:4;pointer-events:none';
        if (p < .98) ov.innerHTML = `<div style="position:absolute;left:0;width:${W}px;top:${y1 - 14}px;height:28px;background:${c}"></div><div style="position:absolute;left:0;width:${W}px;top:${y2 - 14}px;height:28px;background:${c}"></div>`;
        break; }
      case 'spin': {
        if (p < .5) { const q = E.inC(p * 2); show(true, false); A.style.transform = `rotate(${-140 * q}deg) scale(${1 - .7 * q})`; }
        else { const q = E.outC((p - .5) * 2); show(false, true); B.style.transform = `rotate(${140 * (1 - q)}deg) scale(${.3 + .7 * q})`; }
        break; }
      case 'slam': { // B rises like a card, A recedes slower (parallax), hero lands with the scene's own pop
        show(true, true);
        A.style.transform = `translateY(${-H * .3 * e}px) scale(${1 - .1 * e})`; A.style.filter = `brightness(${1 - .5 * e})`;
        B.style.transform = `translateY(${H * (1 - e)}px)`; B.style.borderRadius = `${60 * (1 - e)}px`; break; }
      case 'flash': { // warm light-leak bloom hides the swap
        show(p < .5, p >= .5);
        const k = Math.pow(Math.sin(Math.PI * p), .8);
        ov.style.cssText = `position:absolute;inset:0;z-index:4;pointer-events:none;opacity:${k};` +
          `background:radial-gradient(120% 80% at ${30 + 40 * p}% ${40 + 20 * p}%, #FFFFFF 0%, ${c} 38%, ${c2} 72%, rgba(255,255,255,0) 100%);mix-blend-mode:screen`;
        if (p >= .5) B.style.transform = `scale(${1.08 - .08 * E.outC((p - .5) * 2)})`;
        break; }
      case 'glitch': {
        show(p < .5, p >= .5);
        post = { glitch: Math.sin(Math.PI * p), seed: Math.floor(p * 20) }; break; }
      case 'pixel': {
        show(p < .5, p >= .5);
        post = { pixel: Math.round(4 + 70 * Math.sin(Math.PI * p)) }; break; }
      default: show(p < .5, p >= .5);
    }
    return post;
  }

  // ---------------------------------------------------------------- seek
  window.seek = function (t) {
    scenes.forEach(resetScene);
    ov.innerHTML = ''; ov.style.cssText = 'display:none';
    const S = TL.scenes;
    let i = 0;
    for (let k = 0; k < S.length; k++) if (t >= S[k].start) i = k;
    let post = null, blur = 1;
    // inside a transition window?
    let inWin = -1;
    for (let k = 1; k < S.length; k++) {
      const tr = S[k].tin, b = S[k].start;
      if (!tr || tr.type === 'none') continue;
      if (t >= b - tr.d / 2 && t < b + tr.d / 2) { inWin = k; break; }
    }
    if (inWin > 0) {
      const tr = S[inWin].tin, b = S[inWin].start, p = (t - (b - tr.d / 2)) / tr.d;
      animScene(inWin - 1, t - S[inWin - 1].start, t);
      animScene(inWin, t - S[inWin].start, t);
      post = trans(tr, scenes[inWin - 1], scenes[inWin], p);
      if (FAST.has(tr.type)) blur = ['zoom', 'whipL', 'whipR', 'whipU', 'whipD'].includes(tr.type) ? 6 : 4;
    } else {
      scenes[i].style.display = 'block';
      animScene(i, t - S[i].start, t);
    }
    // stage shakes (impacts)
    let st = '';
    (TL.shakes || []).forEach(([t0, d, amp]) => {
      if (t >= t0 && t < t0 + d) { const k = Math.floor(t * 30), dm = 1 - (t - t0) / d; st = `translate(${(rnd(k) - .5) * amp * dm}px,${(rnd(k + 7) - .5) * amp * dm}px)`; }
    });
    stage.style.transform = st;
    (TL.blurSpans || []).forEach(([a, b]) => { if (t >= a && t < b) blur = Math.max(blur, 3); });
    return { blur, post };
  };
  window.motionInit = init;
})();
