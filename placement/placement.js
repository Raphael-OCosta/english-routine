/* Routine Placement — teste de nivelamento adaptativo, comum a todos os idiomas.
 *
 * Modelo: cada item tem dificuldade b pela sua faixa (A1 … C2). A cada resposta a
 * habilidade θ é reestimada por EAP (média a posteriori numa grade) com o modelo
 * logístico de 3 parâmetros (chute c = 1/opções). O próximo item é o mais informativo
 * perto de θ, respeitando a cota de cada tipo (gramática/vocabulário, leitura, escuta).
 * Resultado aproximado, sem valor de certificação. Contrato em docs/PADRAO-IDIOMAS.md.
 */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const shuffle = a => { a = [...a]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const GRID = Array.from({ length: 161 }, (_, i) => -4 + i * 0.05);
  const D = 1.7;

  // Sessão sem tela: usada pela página e pelos testes de simulação.
  function createSession(cfg) {
    const levels = cfg.levels;                // [{code:'A1', b:-2.5, min, title, description, plan}]
    const bOf = Object.fromEntries(levels.map(l => [l.code, l.b]));
    const bank = cfg.bank.map((q, i) => ({ ...q, id: i, b: bOf[q.level] + (((i * 37) % 7) - 3) * 0.06 }));
    const quota = { ...cfg.quota };           // {grammar: 18, reading: 6, listening: 6}
    const total = Object.values(quota).reduce((a, b) => a + b, 0);
    const typeOf = q => (q.type === 'vocab' ? 'grammar' : q.type);
    const prior = GRID.map(t => Math.exp(-(t * t) / (2 * 1.6 * 1.6)));
    const answers = [];
    const p = (theta, q) => { const c = 1 / q.options.length; return c + (1 - c) / (1 + Math.exp(-D * (theta - q.b))); };
    function estimate() {
      const post = GRID.map((t, k) => answers.reduce((acc, a) => acc * (a.correct ? p(t, a.q) : 1 - p(t, a.q)), prior[k]));
      const sum = post.reduce((a, b) => a + b, 0);
      const mean = GRID.reduce((acc, t, k) => acc + t * post[k], 0) / sum;
      const sd = Math.sqrt(GRID.reduce((acc, t, k) => acc + (t - mean) ** 2 * post[k], 0) / sum);
      return { theta: mean, sd };
    }
    const info = (theta, q) => { const c = 1 / q.options.length; const pr = p(theta, q); return (D * D * ((pr - c) ** 2) * (1 - pr)) / (((1 - c) ** 2) * pr); };
    function next() {
      const used = new Set(answers.map(a => a.q.id));
      const done = type => answers.filter(a => typeOf(a.q) === type).length;
      const types = Object.keys(quota).filter(t => done(t) < quota[t]);
      if (!types.length) return null;
      // Começa por gramática; depois o tipo mais atrasado na sua cota.
      const type = answers.length < 4 && types.includes('grammar') ? 'grammar'
        : types.sort((a, b) => (done(a) / quota[a]) - (done(b) / quota[b]))[0];
      const { theta } = estimate();
      const pool = bank.filter(q => !used.has(q.id) && typeOf(q) === type);
      if (!pool.length) { quota[type] = done(type); return next(); }
      const ranked = pool.map(q => [q, info(theta, q)]).sort((a, b) => b[1] - a[1]).slice(0, 3);
      return ranked[Math.floor(Math.random() * ranked.length)][0];
    }
    const answer = (q, chosen) => { answers.push({ q, chosen, correct: chosen === 0 }); };
    const levelFor = theta => [...levels].reverse().find(l => theta >= l.min) || levels[0];
    const score = theta => Math.max(0, Math.min(100, Math.round((theta + 3.5) / 7 * 100)));
    return { next, answer, estimate, levelFor, score, answers, total, p };
  }

  function start(cfg) {
    const levels = cfg.levels;
    let session = createSession(cfg);
    let current = null;
    let plays = 0;
    let t0 = 0;
    const total = session.total;

    // ------------------------------------------------------------ telas
    function show(id) { for (const s of ['intro', 'test', 'result']) $(s).hidden = s !== id; window.scrollTo({ top: 0, behavior: 'smooth' }); }
    function say(text) {
      if (!('speechSynthesis' in window)) { $('pAudioStatus').textContent = 'Seu navegador não tem narração. Pule para a próxima.'; return; }
      speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = cfg.tts;
      const v = speechSynthesis.getVoices().find(x => cfg.voice.test(x.lang));
      if (v) u.voice = v;
      u.rate = 0.95;
      speechSynthesis.speak(u);
    }
    function render() {
      current = session.next();
      if (!current) { finish(); return; }
      plays = 0;
      const n = session.answers.length + 1;
      $('pProgress').style.width = `${(session.answers.length / total) * 100}%`;
      $('pCount').textContent = `Questão ${n} de ${total}`;
      $('pType').textContent = cfg.typeLabels[current.type];
      $('pPassage').hidden = !current.passage;
      $('pPassage').innerHTML = current.passage ? esc(current.passage).replace(/\n/g, '<br>') : '';
      $('pAudio').hidden = !current.audio;
      $('pAudioStatus').textContent = current.audio ? 'Você pode ouvir até 2 vezes.' : '';
      $('pPlay').disabled = false;
      $('pStem').innerHTML = esc(current.stem).replace('___', '<span class="blank"></span>');
      current.order = shuffle(current.options.map((_, i) => i));
      $('pOptions').innerHTML = current.order.map(i => `<button type="button" data-i="${i}" lang="${cfg.lang}">${esc(current.options[i])}</button>`).join('');
      $('pOptions').classList.remove('locked');
      $('test').classList.remove('anim');
      void $('test').offsetWidth;
      $('test').classList.add('anim');
    }
    $('pPlay').onclick = () => {
      if (!current?.audio || plays >= 2) return;
      plays++;
      say(current.audio);
      $('pAudioStatus').textContent = plays >= 2 ? 'Última vez ouvida.' : 'Você pode ouvir mais 1 vez.';
      if (plays >= 2) $('pPlay').disabled = true;
    };
    $('pOptions').onclick = e => {
      const b = e.target.closest('button');
      if (!b || $('pOptions').classList.contains('locked')) return;
      $('pOptions').classList.add('locked');
      b.classList.add('picked');
      session.answer(current, Number(b.dataset.i));
      setTimeout(render, 260);
    };
    $('pSkip').onclick = () => {
      if (!current) return;
      session.answer(current, -1);
      render();
    };
    function finish() {
      if ('speechSynthesis' in window) speechSynthesis.cancel();
      const { theta, sd } = session.estimate();
      const { levelFor, score, answers } = session;
      const level = levelFor(theta);
      const result = {
        lang: cfg.lang, level: level.code, score: score(theta), theta: Math.round(theta * 100) / 100, sd: Math.round(sd * 100) / 100,
        date: new Date().toISOString(), minutes: Math.round((Date.now() - t0) / 60000),
        bySkill: Object.fromEntries(Object.keys(cfg.typeLabels).map(t => {
          const list = answers.filter(a => a.q.type === t);
          return [t, { right: list.filter(a => a.correct).length, total: list.length }];
        })),
      };
      try {
        const key = `routine-placement-${cfg.lang}`;
        const history = JSON.parse(localStorage.getItem(key) || '[]');
        history.push(result);
        localStorage.setItem(key, JSON.stringify(history.slice(-20)));
      } catch (_) { /* navegador sem armazenamento: o resultado só aparece na tela */ }
      $('pProgress').style.width = '100%';
      $('rLevel').textContent = level.code;
      $('rTitle').textContent = level.title;
      $('rDesc').textContent = level.description;
      $('rScore').textContent = `${result.score}/100`;
      $('rRange').textContent = `Faixa provável: ${levelFor(theta - sd).code}–${levelFor(theta + sd).code}`;
      $('rPlan').innerHTML = level.plan.map(x => `<li>${esc(x)}</li>`).join('');
      $('rSkills').innerHTML = Object.entries(result.bySkill).filter(([, s]) => s.total).map(([t, s]) =>
        `<div class="bar"><span>${esc(cfg.typeLabels[t])}</span><div><i style="--w:${Math.round(s.right / s.total * 100)}%"></i></div><b>${s.right}/${s.total}</b></div>`).join('');
      $('rLevels').innerHTML = levels.map(l => `<span class="${l.code === level.code ? 'on' : ''}">${l.code}</span>`).join('');
      $('rReview').innerHTML = answers.map((a, i) => `<details><summary>${a.correct ? '✓' : '✗'} ${i + 1}. ${esc(a.q.stem)} <small>${a.q.level}</small></summary>`
        + `${a.q.passage ? `<p class="small">${esc(a.q.passage).replace(/\n/g, '<br>')}</p>` : ''}${a.q.audio ? `<p class="small"><b>Áudio:</b> ${esc(a.q.audio)}</p>` : ''}`
        + `<p><b>Resposta:</b> ${esc(a.q.options[0])}${a.correct ? '' : a.chosen < 0 ? ' · você pulou' : ` · você marcou: ${esc(a.q.options[a.chosen])}`}</p><p class="small">${esc(a.q.why)}</p></details>`).join('');
      show('result');
      cfg.onResult?.(result);
    }
    $('pStart').onclick = () => { session = createSession(cfg); t0 = Date.now(); show('test'); render(); };
    $('rAgain').onclick = () => show('intro');
    if ('speechSynthesis' in window) speechSynthesis.getVoices();

    // Último resultado salvo, se houver.
    try {
      const last = JSON.parse(localStorage.getItem(`routine-placement-${cfg.lang}`) || '[]').pop();
      if (last) $('pLast').textContent = `Seu último resultado: ${last.level} (${last.score}/100) em ${new Date(last.date).toLocaleDateString('pt-BR')}.`;
    } catch (_) { /* sem histórico */ }
    return session;
  }

  window.RoutinePlacement = { start, createSession };
})();
