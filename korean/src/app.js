(() => {
  'use strict';
  const KEY = 'routine-ko-v1';
  const ROUND_SIZE = 20;
  const $ = id => document.getElementById(id);
  const byId = new Map(KDATA.questions.map(q => [q.id, q]));

  // ------------------------------------------------------------ state
  function emptyState() {
    return { version: 1, attempts: [], session: null, goal: 20, goalHistory: {}, skills: { events: [] } };
  }
  function loadState() {
    try {
      const saved = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (saved && typeof saved === 'object') {
        return { ...emptyState(), ...saved, attempts: Array.isArray(saved.attempts) ? saved.attempts : [] };
      }
    } catch (_) { /* estado corrompido: recomeça */ }
    return emptyState();
  }
  let state = loadState();

  function save() {
    const raw = JSON.stringify(state);
    localStorage.setItem(KEY, raw);
    dispatchEvent(new CustomEvent('english-daily:state-saved', { detail: { raw } }));
  }
  const today = () => {
    const d = new Date();
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  };

  // ------------------------------------------------------------ voz
  let koVoice = null;
  function pickVoice() {
    if (!('speechSynthesis' in window)) return;
    koVoice = speechSynthesis.getVoices().find(v => /^ko/i.test(v.lang)) || null;
    const notice = $('voiceNotice');
    if (!koVoice && speechSynthesis.getVoices().length) {
      notice.textContent = 'Seu aparelho não tem voz em coreano instalada. O áudio pode soar estranho: instale a voz “Coreano” nas configurações de idioma/fala do sistema.';
      notice.hidden = false;
    } else {
      notice.hidden = true;
    }
  }
  function speak(text) {
    if (!('speechSynthesis' in window) || !text) return;
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'ko-KR';
    if (koVoice) u.voice = koVoice;
    u.rate = 0.85;
    speechSynthesis.speak(u);
  }
  if ('speechSynthesis' in window) {
    pickVoice();
    speechSynthesis.addEventListener?.('voiceschanged', pickVoice);
  }

  // ------------------------------------------------------------ util
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const hasHangul = s => /[ᄀ-ᇿ㄰-㆏가-힣]/.test(s);
  function shuffle(list) {
    const a = [...list];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  let skills = null;

  // ------------------------------------------------------------ abas
  document.querySelectorAll('[role=tab]').forEach(tab => tab.addEventListener('click', () => {
    document.querySelectorAll('[role=tab]').forEach(t => t.setAttribute('aria-selected', String(t === tab)));
    document.querySelectorAll('[role=tabpanel]').forEach(p => { p.hidden = p.id !== tab.dataset.tab; });
    skills?.pause();
    if (tab.dataset.tab === 'progress') { renderProgress(); skills?.renderHistory(); }
  }));

  // ------------------------------------------------------------ treino
  const filters = $('moduleFilters');
  filters.innerHTML = Object.entries(KDATA.modules).map(([key, label]) => {
    const n = KDATA.questions.filter(q => q.module === key).length;
    return `<label><input type="checkbox" value="${key}" checked> ${esc(label)} <span class="muted small">(${n})</span></label>`;
  }).join('');

  let round = [];
  let index = 0;
  let answered = false;
  let roundCorrect = 0;
  let reviewMode = false;
  let picks = [];

  const mode = () => (document.querySelector('input[name=mode]:checked')?.value === 'typing' ? 'typing' : 'choice');
  const slotsOf = q => q.slots || [{ answers: q.answers, distractors: q.distractors, label: '' }];
  // Digitação só onde a resposta é hangul (significados em português ficam na múltipla escolha).
  const typeable = q => slotsOf(q).every(s => s.answers.every(hasHangul));
  const norm = s => String(s).normalize('NFC').replace(/[\s.?!,·~]/g, '').toLowerCase();
  const romanOf = text => (state.showRoman !== false && KDATA.roman[text]) || '';
  const optionLabel = o => {
    const roman = romanOf(o);
    return `<span${hasHangul(o) ? ' lang="ko"' : ''}>${esc(o)}</span>${roman ? `<small>${esc(roman)}</small>` : ''}`;
  };

  function pool() {
    const modules = new Set([...filters.querySelectorAll('input:checked')].map(i => i.value));
    const levels = new Set([$('level1').checked && 1, $('level2').checked && 2].filter(Boolean));
    return KDATA.questions.filter(q => modules.has(q.module) && levels.has(q.level) && (mode() === 'choice' || typeable(q)));
  }

  function wrongIds() {
    // Questão "para revisar" = a última tentativa dela foi errada.
    const last = new Map();
    for (const a of state.attempts) last.set(a.qid, a.correct);
    return [...last].filter(([qid, ok]) => !ok && byId.has(qid)).map(([qid]) => qid);
  }

  function newRound(review = false) {
    reviewMode = review;
    let list;
    if (review) {
      list = wrongIds().map(id => byId.get(id)).filter(q => mode() === 'choice' || typeable(q));
      if (!list.length) {
        showEmpty('Nenhum erro para revisar neste formato. 잘했어요! (Muito bem!)');
        return;
      }
    } else {
      list = pool();
      if (!list.length) {
        showEmpty(mode() === 'typing'
          ? 'Nenhuma questão para digitar nesta seleção. Inclua partículas, verbos, completar frases ou vocabulário.'
          : 'Escolha ao menos um conteúdo e um nível.');
        return;
      }
      // Prioriza questões nunca vistas, depois as menos recentes.
      const seen = new Set(state.attempts.map(a => a.qid));
      const fresh = shuffle(list.filter(q => !seen.has(q.id)));
      const old = shuffle(list.filter(q => seen.has(q.id)));
      list = [...fresh, ...old];
    }
    round = shuffle(list.slice(0, ROUND_SIZE));
    index = 0;
    roundCorrect = 0;
    renderQuestion();
  }

  function showEmpty(message) {
    round = [];
    $('qMeta').textContent = '';
    $('qCount').textContent = '';
    $('qPrompt').textContent = message;
    $('qText').textContent = '';
    for (const id of ['options', 'slots']) $(id).innerHTML = '';
    for (const id of ['feedback', 'next', 'speak', 'check', 'typing', 'typingHint']) $(id).hidden = true;
    $('roundInfo').textContent = '';
  }

  function renderQuestion() {
    const q = round[index];
    const slots = slotsOf(q);
    const typing = mode() === 'typing';
    const multi = slots.length > 1;
    answered = false;
    picks = slots.map(() => null);
    $('qMeta').textContent = `${KDATA.modules[q.module]} · TOPIK ${q.level}${reviewMode ? ' · revisão' : ''}`;
    $('qCount').textContent = `${index + 1} de ${round.length}`;
    $('qPrompt').textContent = q.prompt;
    const qText = $('qText');
    qText.innerHTML = esc(q.text).replace(/___/g, '<span class="blank"></span>');
    qText.lang = hasHangul(q.text) ? 'ko' : 'pt-BR';
    // Em frases com lacunas o áudio entregaria a resposta: só toca depois de corrigir.
    $('speak').hidden = !q.audio || q.module === 'completar';
    $('typingHint').hidden = !typing;
    $('options').innerHTML = '';
    $('slots').innerHTML = '';
    $('typing').hidden = !(typing && !multi);
    $('check').hidden = !(typing || multi);
    if (typing && !multi) {
      $('typed').value = '';
      $('typed').className = '';
      $('typed').disabled = false;
      setTimeout(() => $('typed').focus(), 0);
    } else if (typing) {
      $('slots').innerHTML = slots.map((s, i) =>
        `<div class="slot"><h3>Lacuna ${i + 1} · ${esc(s.label)}</h3><input data-slot="${i}" lang="ko" autocomplete="off" autocapitalize="off" spellcheck="false"></div>`).join('');
    } else if (multi) {
      $('slots').innerHTML = slots.map((s, i) => {
        const options = shuffle([s.answers[0], ...s.distractors.slice(0, 3)]);
        return `<div class="slot"><h3>Lacuna ${i + 1} · ${esc(s.label)}</h3><div class="slot-options">${options.map(o =>
          `<button type="button" data-slot="${i}" data-value="${esc(o)}">${optionLabel(o)}</button>`).join('')}</div></div>`;
      }).join('');
    } else {
      const options = shuffle([q.answers[0], ...q.distractors.slice(0, 3)]);
      $('options').innerHTML = options.map(o => `<button type="button" data-value="${esc(o)}">${optionLabel(o)}</button>`).join('');
    }
    $('feedback').hidden = true;
    $('next').hidden = true;
    $('roundInfo').textContent = `Acertos na rodada: ${roundCorrect}`;
    if (q.module === 'escuta') setTimeout(() => speak(q.audio), 250);
  }

  function finish(values) {
    if (answered || !round.length) return;
    const q = round[index];
    const slots = slotsOf(q);
    if (values.some(v => !String(v || '').trim())) {
      $('roundInfo').textContent = slots.length > 1 ? 'Preencha todas as lacunas.' : 'Digite sua resposta.';
      return;
    }
    answered = true;
    const results = slots.map((s, i) => s.answers.some(a => norm(a) === norm(values[i])));
    const correct = results.every(Boolean);
    if (correct) roundCorrect++;

    // Marca certo/errado em cada controle.
    $('options').querySelectorAll('button').forEach(b => {
      b.disabled = true;
      if (q.answers.includes(b.dataset.value)) b.classList.add('correct');
      else if (b.dataset.value === values[0]) b.classList.add('wrong');
    });
    $('slots').querySelectorAll('button').forEach(b => {
      b.disabled = true;
      const s = slots[Number(b.dataset.slot)];
      if (s.answers.includes(b.dataset.value)) b.classList.add('correct');
      else if (b.classList.contains('picked')) b.classList.add('wrong');
    });
    $('slots').querySelectorAll('input').forEach(input => {
      input.disabled = true;
      input.classList.add(results[Number(input.dataset.slot)] ? 'correct' : 'wrong');
    });
    if (!$('typing').hidden) {
      $('typed').disabled = true;
      $('typed').classList.add(correct ? 'correct' : 'wrong');
    }
    $('check').hidden = true;

    const day = today();
    state.attempts.push({
      qid: q.id, answer: values.join(' · '), correct, day, review: reviewMode, mode: mode(), time: new Date().toISOString(),
    });
    state.goalHistory = { ...(state.goalHistory || {}), [day]: Number(state.goal) || 20 };
    save();

    const fb = $('feedback');
    fb.className = 'feedback' + (correct ? ' ok' : '');
    const expected = slots.map(s => s.answers[0]);
    let complete = q.text;
    if (q.text.includes('___')) expected.forEach(v => { complete = complete.replace('___', v); });
    else complete = expected.join(' · ');
    const roman = q.roman ? ` <span class="muted">(${esc(q.roman)})</span>` : '';
    fb.innerHTML = `<strong>${correct ? 'Correto! 맞아요!' : 'Resposta certa:'}</strong>${roman}<br>`
      + `<span${hasHangul(complete) ? ' lang="ko"' : ''}>${esc(complete)}</span><br>${esc(q.explanation)}`;
    fb.hidden = false;
    if (q.audio && q.module !== 'escuta') speak(q.audio);
    $('speak').hidden = !q.audio;
    $('next').textContent = index + 1 < round.length ? 'Próxima →' : 'Nova rodada';
    $('next').hidden = false;
    $('roundInfo').textContent = `Acertos na rodada: ${roundCorrect}`;
    renderGoal();
  }

  $('options').addEventListener('click', event => {
    const button = event.target.closest('button');
    if (button) finish([button.dataset.value]);
  });
  $('slots').addEventListener('click', event => {
    const button = event.target.closest('button');
    if (!button || answered) return;
    const i = Number(button.dataset.slot);
    picks[i] = button.dataset.value;
    $('slots').querySelectorAll(`button[data-slot="${i}"]`).forEach(b => b.classList.toggle('picked', b === button));
  });
  $('check').addEventListener('click', () => {
    if (mode() === 'typing') {
      const inputs = [...$('slots').querySelectorAll('input')];
      finish(inputs.length ? inputs.map(i => i.value) : [$('typed').value]);
    } else {
      finish(picks);
    }
  });
  addEventListener('keydown', event => {
    // isComposing: o Enter que fecha a sílaba no teclado coreano não corrige.
    if (event.key !== 'Enter' || event.isComposing) return;
    if (!$('check').hidden && event.target.closest?.('#questionCard')) { event.preventDefault(); $('check').click(); }
    else if (!$('next').hidden && !event.target.closest?.('button')) { event.preventDefault(); $('next').click(); }
  });

  $('next').addEventListener('click', () => {
    if (index + 1 < round.length) {
      index++;
      renderQuestion();
    } else {
      newRound(reviewMode);
    }
  });
  $('speak').addEventListener('click', () => { const q = round[index]; if (q) speak(q.audio); });
  $('newRound').addEventListener('click', () => newRound(false));
  $('reviewRound').addEventListener('click', () => newRound(true));
  document.querySelectorAll('input[name=mode]').forEach(input => {
    input.checked = input.value === (state.mode === 'typing' ? 'typing' : 'choice');
    input.addEventListener('change', () => { state.mode = mode(); save(); newRound(false); });
  });
  $('showRoman').checked = state.showRoman !== false;
  $('showRoman').addEventListener('change', () => {
    state.showRoman = $('showRoman').checked;
    save();
    document.querySelectorAll('#options button, .slot-options button').forEach(b => {
      b.querySelector('small')?.remove();
      const roman = romanOf(b.dataset.value);
      if (roman) b.insertAdjacentHTML('beforeend', `<small>${esc(roman)}</small>`);
    });
  });

  const goalInput = $('goal');
  goalInput.value = state.goal || 20;
  goalInput.addEventListener('change', () => {
    const n = Math.min(200, Math.max(5, Math.round(Number(goalInput.value) || 20)));
    goalInput.value = n;
    state.goal = n;
    state.goalHistory = { ...(state.goalHistory || {}), [today()]: n };
    save();
    renderGoal();
  });
  function renderGoal() {
    const done = state.attempts.filter(a => a.day === today()).length;
    const goal = Number(state.goal) || 20;
    $('goalStatus').textContent = done >= goal ? `Meta de hoje cumprida: ${done}/${goal} ✓` : `Hoje: ${done}/${goal}`;
  }

  // ------------------------------------------------------------ hangul
  function letterButton(char, top, bottom) {
    return `<button type="button" data-say="${esc(char)}"><b lang="ko">${esc(char)}</b><small>${esc(top)}</small>${bottom ? `<small>${esc(bottom)}</small>` : ''}</button>`;
  }
  $('consonants').innerHTML = KDATA.consonants.map(([c, rr, name]) => letterButton(c, rr, name)).join('');
  $('vowels').innerHTML = KDATA.vowels.map(([v, rr]) => letterButton(v, rr)).join('');
  const INITIALS = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ';
  const MEDIALS = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ';
  const RR = Object.fromEntries(KDATA.consonants.map(([c, rr]) => [c, rr.split('/')[0]]));
  RR['ㅇ'] = '';
  RR['ㄹ'] = 'r';
  const VRR = Object.fromEntries(KDATA.vowels);
  const syllables = [];
  for (const c of 'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅎ') {
    for (const v of 'ㅏㅓㅗㅜㅣ') {
      const syl = String.fromCharCode(0xac00 + (INITIALS.indexOf(c) * 21 + MEDIALS.indexOf(v)) * 28);
      syllables.push(letterButton(syl, RR[c] + VRR[v]));
    }
  }
  $('syllables').innerHTML = syllables.join('');
  // Nome da letra soa melhor que a letra solta no TTS.
  const NAMES = { ㄱ: '기역', ㄴ: '니은', ㄷ: '디귿', ㄹ: '리을', ㅁ: '미음', ㅂ: '비읍', ㅅ: '시옷', ㅇ: '이응', ㅈ: '지읒', ㅊ: '치읓', ㅋ: '키읔', ㅌ: '티읕', ㅍ: '피읖', ㅎ: '히읗', ㄲ: '쌍기역', ㄸ: '쌍디귿', ㅃ: '쌍비읍', ㅆ: '쌍시옷', ㅉ: '쌍지읒' };
  $('alphabet').addEventListener('click', event => {
    const button = event.target.closest('[data-say]');
    if (!button) return;
    const ch = button.dataset.say;
    const vowelIndex = MEDIALS.indexOf(ch);
    speak(NAMES[ch] || (vowelIndex >= 0 ? String.fromCharCode(0xac00 + (11 * 21 + vowelIndex) * 28) : ch));
  });

  // ------------------------------------------------------------ guia
  $('guideList').innerHTML = KDATA.guide.map(([title, body], i) =>
    `<details${i < 2 ? ' open' : ''}><summary>${esc(title)}</summary><p>${esc(body)}</p></details>`).join('');

  // ------------------------------------------------------------ progresso
  function renderProgress() {
    const attempts = state.attempts.filter(a => byId.has(a.qid));
    const total = attempts.length;
    const right = attempts.filter(a => a.correct).length;
    $('sTotal').textContent = total;
    $('sRate').textContent = total ? `${Math.round((right / total) * 100)}%` : '0%';
    $('sToday').textContent = attempts.filter(a => a.day === today()).length;
    const wrong = wrongIds();
    $('sWrong').textContent = wrong.length;
    $('byModule').innerHTML = Object.entries(KDATA.modules).map(([key, label]) => {
      const list = attempts.filter(a => byId.get(a.qid).module === key);
      const ok = list.filter(a => a.correct).length;
      return `<tr><td>${esc(label)}</td><td>${list.length}</td><td>${list.length ? Math.round((ok / list.length) * 100) + '%' : '—'}</td></tr>`;
    }).join('');
    const recent = attempts.filter(a => !a.correct).slice(-8).reverse();
    $('lastWrong').innerHTML = recent.length ? recent.map(a => {
      const q = byId.get(a.qid);
      return `<p><span lang="${hasHangul(q.text) ? 'ko' : 'pt-BR'}">${esc(q.text)}</span> → <strong lang="ko">${esc(q.answers[0])}</strong> <span class="muted small">(você marcou ${esc(a.answer)})</span></p>`;
    }).join('') : '<p class="muted">Nenhum erro ainda.</p>';
  }

  $('reset').addEventListener('click', () => {
    if (!confirm('Apagar todo o histórico do Korean Routine? O English Routine não é afetado.')) return;
    state = { ...emptyState(), goal: state.goal };
    save();
    renderProgress();
    skills?.renderHistory();
    renderGoal();
    newRound(false);
  });

  // ------------------------------------------------------------ habilidades (módulo comum skills/)
  const CONNECTORS = ['그리고', '그래서', '하지만', '그런데', '그러면', '왜냐하면', '그러니까', '또', '먼저', '마지막으로'];
  function writingChecks(text) {
    const notes = [];
    const sentences = text.split(/[.!?\n]+/).map(x => x.trim()).filter(x => /[가-힣]/.test(x));
    const polite = sentences.filter(x => /요$/.test(x)).length;
    const formal = sentences.filter(x => /니다$/.test(x)).length;
    const plain = sentences.filter(x => /[^니]다$/.test(x)).length;
    const styles = [polite && '-요 (educado)', formal && '-ㅂ니다 (formal)', plain && '-다 (escrito/diário)'].filter(Boolean);
    if (styles.length > 1) notes.push(`Você misturou estilos de terminação: ${styles.join(', ')}. Em um mesmo texto, escolha um.`);
    else if (styles.length === 1) notes.push(`Terminação consistente: ${styles[0]}.`);
    const latin = (text.match(/[A-Za-z]/g) || []).length;
    const hangul = (text.match(/[가-힣]/g) || []).length;
    if (latin > hangul * 0.2) notes.push('Há bastante alfabeto latino. Tente escrever tudo em hangul (nomes estrangeiros também podem ser escritos em hangul).');
    const repeated = Object.entries((text.match(/[가-힣]+/g) || []).reduce((m, w) => ({ ...m, [w]: (m[w] || 0) + 1 }), {}))
      .filter(([w, n]) => n >= 3 && w.length >= 2).map(([w]) => w);
    if (repeated.length) notes.push(`Palavras repetidas 3+ vezes: <span lang="ko">${repeated.slice(0, 5).join(', ')}</span>. Varie com sinônimos ou junte frases com conectores.`);
    if (/(은는|이가|을를)/.test(text)) notes.push('Parece haver duas partículas seguidas (ex.: 은는). Confira.');
    return notes;
  }
  const tutorPrompt = (p, text) => `Corrija meu texto em coreano com explicações em português. Nível de treino: ${p.level}. `
    + `Proposta: ${p.prompt} (${p.prompt_pt}). Meta: ${p.lines} linhas e ${p.units} sílabas. `
    + 'Analise: cumprimento da proposta, partículas (은/는, 이/가, 을/를, 에/에서), conjugação e tempo verbal, consistência do nível de formalidade (-요, -ㅂ니다, -다), '
    + 'espaçamento (띄어쓰기), ortografia e vocabulário. Mostre cada erro com a correção e a regra, depois uma versão revisada que preserve minhas ideias, '
    + 'com romanização de frases difíceis. Termine com três prioridades para o próximo treino.\n\nMeu texto:\n' + text;

  skills = RoutineSkills.mount({
    lang: {
      code: 'ko', name: 'coreano', html: 'ko', tts: 'ko-KR', voice: /^ko/i, rate: 0.85,
      unit: 'syllables', unitLabel: 'sílabas', connectors: CONNECTORS, writePlaceholder: '여기에 한국어로 써 보세요…',
    },
    data: KDATA.skills,
    roman: KDATA.roman,
    skills: () => (state.skills ??= { events: [] }),
    save,
    day: today,
    writingChecks,
    tutorPrompt,
  });

  renderGoal();
  newRound(false);
})();
