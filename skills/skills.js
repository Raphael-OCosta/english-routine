/* Routine Skills — Reading, Writing, Listening e Speaking comuns a todos os idiomas.
 *
 * Cada idioma chama RoutineSkills.mount(config) depois de ter, na página, os painéis
 * #reading, #writing, #listening, #speaking e o contêiner #skillsHistory.
 * Os eventos gravados seguem o mesmo esquema do English Routine (state.skills.events):
 *   reading   {kind, ref, level, seconds, wpm, unit, score, total, reread}
 *   writing   {kind, ref, level, text, words, lines, unique, unit}
 *   listening {kind, ref, level, score, total, transcript, title?}
 *   speaking  {kind, ref, level, seconds, mode, notes, checks, intelligibility?, speechText?}
 * Contrato completo em docs/PADRAO-IDIOMAS.md.
 */
(() => {
  'use strict';
  const MAX_EVENTS = 1500;
  const MAX_RECORD_MS = 120000;
  const MAX_AUDIO_BYTES = 15000000;
  const LISTEN_CHOICE_ROUND = 10;

  const $ = id => document.getElementById(id);
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const shuffle = list => {
    const a = [...list];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  };
  const timeLabel = ms => {
    const n = Math.floor(ms / 1000);
    return `${String(Math.floor(n / 60)).padStart(2, '0')}:${String(n % 60).padStart(2, '0')}`;
  };
  const newClock = () => ({ ms: 0, start: null });
  const elapsed = c => c.ms + (c.start ? Date.now() - c.start : 0);
  const pauseClock = c => { c.ms = elapsed(c); c.start = null; };

  // Contagem por idioma: palavras (alfabeto latino) ou sílabas (hangul, kana, hanzi).
  const COUNTERS = {
    words: text => (String(text).match(/[\p{L}\p{N}]+(?:['’-][\p{L}\p{N}]+)*/gu) || []),
    syllables: text => (String(text).match(/[가-힣぀-ヿ一-鿿]/g) || []),
  };

  function mount(cfg) {
    const L = cfg.lang;
    const texts = cfg.data.texts;
    const prompts = cfg.data.prompts;
    const units = COUNTERS[L.unit] || COUNTERS.words;
    const unitLabel = L.unitLabel || 'palavras';
    const S = () => cfg.skills();
    let lastSaved = true;
    const tag = L.code;

    function addSkill(event) {
      if (S().events.length >= MAX_EVENTS) return false;
      S().events.push({ id: Date.now().toString(36) + '-' + Math.random().toString(36).slice(2), time: new Date().toISOString(), day: cfg.day(), ...event });
      lastSaved = cfg.save() !== false;
      renderHistory();
      readingAvailability();
      return true;
    }
    const saveMessage = () => (lastSaved ? 'Registro salvo no seu histórico.' : 'Não foi possível salvar neste navegador.');
    const options = items => items.map(p => `<option value="${p.id}">${esc(`${p.level} · ${p.topic} · ${p.title || p.prompt_pt || p.prompt}`)}</option>`).join('');
    const paragraphs = (text, lang) => String(text).split('\n\n').map(p => `<p${lang ? ` lang="${lang}"` : ''}>${esc(p)}</p>`).join('');
    const levels = [...new Set([...texts, ...prompts].map(p => p.level))];
    const levelOptions = '<option value="">Todos</option>' + levels.map(l => `<option>${esc(l)}</option>`).join('');

    // ---------------------------------------------------------------- voz
    let voices = [];
    let speech = null;
    let watchdog = null;
    function loadVoices() {
      voices = 'speechSynthesis' in window ? speechSynthesis.getVoices().filter(v => L.voice.test(v.lang)) : [];
      for (const id of [`${tag}ListenVoice`]) {
        const select = $(id);
        if (!select) continue;
        select.innerHTML = voices.length
          ? voices.map((v, i) => `<option value="${i}">${esc(v.name + ' · ' + v.lang)}</option>`).join('')
          : `<option value="">Voz padrão em ${esc(L.name)} (se disponível)</option>`;
      }
    }
    function stopSpeech() {
      clearTimeout(watchdog);
      watchdog = null;
      if ('speechSynthesis' in window) speechSynthesis.cancel();
      speech = null;
    }
    function say(text, statusId, onDone, rate) {
      stopSpeech();
      const status = $(statusId);
      if (!('speechSynthesis' in window)) { if (status) status.textContent = 'Este navegador não oferece narração.'; return; }
      const u = new SpeechSynthesisUtterance(text);
      speech = u;
      u.lang = L.tts;
      u.rate = rate || Number($(`${tag}ListenRate`)?.value) || L.rate || 0.9;
      const voice = voices[Number($(`${tag}ListenVoice`)?.value)] || voices[0];
      if (voice) u.voice = voice;
      u.onstart = () => { clearTimeout(watchdog); if (status) status.textContent = 'Reproduzindo…'; };
      u.onend = () => { clearTimeout(watchdog); if (status) status.textContent = 'Áudio concluído.'; onDone?.(); };
      u.onerror = e => { if (!['canceled', 'interrupted'].includes(e.error) && status) status.textContent = 'Não foi possível reproduzir esta voz. Escolha outra voz.'; };
      if (status) status.textContent = 'Carregando voz…';
      watchdog = setTimeout(() => { if (speech === u) { stopSpeech(); if (status) status.textContent = `A voz não iniciou. Instale a voz em ${L.name} no sistema ou troque de navegador.`; } }, 8000);
      speechSynthesis.speak(u);
    }

    // ---------------------------------------------------------------- quiz
    // Opções embaralhadas a cada exibição; o valor guarda o índice original.
    function quiz(target, p, prefix) {
      $(target).innerHTML = '<h3>Confira sua compreensão</h3>' + p.questions.map((question, i) => {
        const order = shuffle(question.options.map((_, n) => n));
        return `<label for="${prefix}${i}">${esc(question.question)}</label><select id="${prefix}${i}"><option value="">Escolha uma resposta</option>${order.map(n => `<option value="${n}">${esc(question.options[n])}</option>`).join('')}</select>`;
      }).join('');
    }
    function quizResult(p, prefix) {
      if (p.questions.some((_, i) => $(prefix + i).value === '')) return null;
      const right = (question, i) => Number($(prefix + i).value) === question.answer;
      const score = p.questions.filter(right).length;
      return {
        score, total: p.questions.length,
        html: `<h3>${score} / ${p.questions.length} na compreensão</h3>` + p.questions.map((question, i) =>
          `<p><b>${right(question, i) ? '✓' : '✗'} ${esc(question.options[question.answer])}</b> · <span lang="${L.html}">${esc(question.why)}</span></p>`).join(''),
      };
    }
    const lockQuiz = (p, prefix) => p.questions.forEach((_, i) => { $(prefix + i).disabled = true; });
    const supportBlock = p => `${p.roman ? `<details><summary>Mostrar pronúncia (romanização)</summary>${paragraphs(p.roman)}</details>` : ''}`
      + `${p.translation ? `<details><summary>Mostrar tradução</summary>${paragraphs(p.translation)}</details>` : ''}`;

    // ---------------------------------------------------------------- reading
    $('reading').innerHTML = `
      <div class="skill-heading"><span class="eyebrow">01 · Reading</span><h2>Leia no seu ritmo. Depois confira.</h2>
      <p class="muted">Textos originais por nível. O cronômetro mede ${esc(unitLabel)} por minuto; pausas não contam. Depois da leitura, responda às perguntas e, se quiser, veja a pronúncia e a tradução.</p></div>
      <div class="card">
        <div class="skill-filters"><div><label for="${tag}ReadLevel">Nível</label><select id="${tag}ReadLevel">${levelOptions}</select></div>
        <div><label for="${tag}ReadTopic">Tema</label><select id="${tag}ReadTopic"></select></div>
        <div><label for="${tag}ReadPick">Texto</label><select id="${tag}ReadPick"></select></div></div>
        <button id="${tag}ReadRandom">Sortear texto · priorizar não lidos</button>
        <p id="${tag}ReadAvailability" class="small muted" role="status"></p>
        <h3 id="${tag}ReadTitle"></h3><p id="${tag}ReadMeta" class="small muted"></p>
        <div class="timer-row"><output id="${tag}ReadClock" class="clock">00:00</output><button id="${tag}ReadStart" class="primary">Iniciar leitura</button><button id="${tag}ReadPause" disabled>Pausar</button><button id="${tag}ReadFinish" disabled>Terminei de ler</button></div>
        <article id="${tag}ReadPassage" class="passage" lang="${L.html}" hidden></article>
        <div id="${tag}ReadSupport" hidden></div>
        <div id="${tag}ReadQuestions" class="quiz" hidden></div>
        <button id="${tag}ReadSave" class="primary" hidden>Corrigir compreensão e registrar</button>
        <div id="${tag}ReadResult" role="status"></div>
      </div>`;
    let readClock = newClock();
    let readStage = 'idle';
    let readMs = 0;
    const readItem = () => texts.find(p => p.id === $(`${tag}ReadPick`).value) || texts[0];
    $(`${tag}ReadTopic`).innerHTML = '<option value="">Todos</option>' + [...new Set(texts.map(p => p.topic))].map(t => `<option>${esc(t)}</option>`).join('');
    const readingPool = () => texts.filter(p => (!$(`${tag}ReadLevel`).value || p.level === $(`${tag}ReadLevel`).value) && (!$(`${tag}ReadTopic`).value || p.topic === $(`${tag}ReadTopic`).value));
    const readIds = () => new Set(S().events.filter(e => e.kind === 'reading').map(e => e.ref));
    function readingAvailability() {
      const items = readingPool();
      const read = readIds();
      $(`${tag}ReadAvailability`).textContent = `${items.length} textos nesta seleção · ${items.filter(p => read.has(p.id)).length} já lidos · ${items.filter(p => !read.has(p.id)).length} ainda não lidos.`;
    }
    function readChoices() {
      const items = readingPool();
      $(`${tag}ReadPick`).innerHTML = options(items);
      $(`${tag}ReadPick`).value = items[0]?.id || '';
      resetReading();
      readingAvailability();
    }
    function resetReading() {
      readClock = newClock();
      readStage = 'idle';
      readMs = 0;
      const has = !!$(`${tag}ReadPick`).value;
      const p = readItem();
      $(`${tag}ReadTitle`).textContent = has ? p.title : 'Nenhum texto nesta combinação';
      $(`${tag}ReadMeta`).textContent = has ? `${p.level} · ${p.topic} · ${units(p.text).length} ${unitLabel}` : 'Escolha outro tema ou nível.';
      $(`${tag}ReadPassage`).innerHTML = has ? paragraphs(p.text) : '';
      $(`${tag}ReadPassage`).hidden = true;
      $(`${tag}ReadSupport`).hidden = true;
      $(`${tag}ReadQuestions`).hidden = true;
      $(`${tag}ReadSave`).hidden = true;
      $(`${tag}ReadResult`).innerHTML = '';
      $(`${tag}ReadStart`).disabled = !has;
      $(`${tag}ReadStart`).textContent = 'Iniciar leitura';
      $(`${tag}ReadPause`).disabled = true;
      $(`${tag}ReadFinish`).disabled = true;
      $(`${tag}ReadClock`).textContent = '00:00';
    }
    function pauseReading() {
      if (readStage !== 'running') return;
      pauseClock(readClock);
      readStage = 'paused';
      $(`${tag}ReadPause`).textContent = 'Retomar';
      $(`${tag}ReadPassage`).hidden = true;
    }
    $(`${tag}ReadLevel`).onchange = readChoices;
    $(`${tag}ReadTopic`).onchange = readChoices;
    $(`${tag}ReadPick`).onchange = resetReading;
    $(`${tag}ReadRandom`).onclick = () => {
      const read = readIds();
      const pool = readingPool();
      const unread = pool.filter(p => !read.has(p.id) && p.id !== $(`${tag}ReadPick`).value);
      const items = unread.length ? unread : pool.filter(p => p.id !== $(`${tag}ReadPick`).value);
      if (!items.length) return;
      $(`${tag}ReadPick`).value = items[Math.floor(Math.random() * items.length)].id;
      resetReading();
    };
    $(`${tag}ReadStart`).onclick = () => {
      resetReading();
      readClock.start = Date.now();
      readStage = 'running';
      $(`${tag}ReadStart`).disabled = true;
      $(`${tag}ReadPassage`).hidden = false;
      $(`${tag}ReadPause`).disabled = false;
      $(`${tag}ReadPause`).textContent = 'Pausar';
      $(`${tag}ReadFinish`).disabled = false;
    };
    $(`${tag}ReadPause`).onclick = () => {
      if (readStage === 'running') pauseReading();
      else if (readStage === 'paused') {
        readClock.start = Date.now();
        readStage = 'running';
        $(`${tag}ReadPause`).textContent = 'Pausar';
        $(`${tag}ReadPassage`).hidden = false;
      }
    };
    $(`${tag}ReadFinish`).onclick = () => {
      if (!['running', 'paused'].includes(readStage)) return;
      pauseClock(readClock);
      readMs = readClock.ms;
      if (readMs < 1000) { $(`${tag}ReadResult`).textContent = 'Leia o texto antes de concluir.'; readStage = 'paused'; $(`${tag}ReadPause`).textContent = 'Retomar'; return; }
      readStage = 'finished';
      $(`${tag}ReadClock`).textContent = timeLabel(readMs);
      $(`${tag}ReadPause`).disabled = true;
      $(`${tag}ReadFinish`).disabled = true;
      $(`${tag}ReadPassage`).hidden = true;
      quiz(`${tag}ReadQuestions`, readItem(), `${tag}rq`);
      $(`${tag}ReadQuestions`).hidden = false;
      $(`${tag}ReadSave`).hidden = false;
      $(`${tag}ReadSave`).disabled = false;
      $(`${tag}ReadResult`).textContent = `Leitura concluída em ${timeLabel(readMs)}. Responda às perguntas para registrar.`;
    };
    $(`${tag}ReadSave`).onclick = () => {
      if (readStage !== 'finished') return;
      const p = readItem();
      const r = quizResult(p, `${tag}rq`);
      if (!r) { $(`${tag}ReadResult`).textContent = 'Responda a todas as perguntas antes de registrar.'; return; }
      const count = units(p.text).length;
      const rate = readMs >= 10000 ? Math.round(count * 60000 / readMs) : null;
      if (rate === null) { $(`${tag}ReadResult`).textContent = 'Tempo de leitura curto demais para calcular a velocidade. Refaça a leitura.'; return; }
      const reread = S().events.some(e => e.kind === 'reading' && e.ref === p.id);
      if (!addSkill({ kind: 'reading', ref: p.id, level: p.level, seconds: readMs / 1000, wpm: rate, unit: L.unit, score: r.score, total: r.total, reread })) return;
      readStage = 'saved';
      $(`${tag}ReadSave`).disabled = true;
      lockQuiz(p, `${tag}rq`);
      $(`${tag}ReadPassage`).hidden = false;
      $(`${tag}ReadSupport`).innerHTML = supportBlock(p);
      $(`${tag}ReadSupport`).hidden = false;
      $(`${tag}ReadResult`).innerHTML = `<div class="feedback"><h3>${rate} ${esc(unitLabel)} por minuto · ${timeLabel(readMs)}</h3>${r.html}<p>${reread ? 'Releitura registrada.' : 'Primeira leitura deste texto.'} ${saveMessage()}</p></div>`;
      $(`${tag}ReadStart`).disabled = false;
      $(`${tag}ReadStart`).textContent = 'Ler novamente';
    };

    // ---------------------------------------------------------------- writing
    $('writing').innerHTML = `
      <div class="skill-heading"><span class="eyebrow">02 · Writing</span><h2>Escreva em ${esc(L.name)}.</h2>
      <p class="muted">Rascunho salvo automaticamente. A revisão local dá pistas objetivas; para uma correção completa, use o pedido pronto para o chat.</p></div>
      <div class="card">
        <label for="${tag}WritePick">Proposta de escrita · nível e tema</label><select id="${tag}WritePick">${options(prompts)}</select>
        <h3 id="${tag}WritePrompt" lang="${L.html}"></h3><p id="${tag}WritePromptPt" class="muted"></p><p id="${tag}WriteGoal" class="notice"></p>
        <label for="${tag}WriteText">Seu texto em ${esc(L.name)}</label>
        <textarea id="${tag}WriteText" class="writing-area" lang="${L.html}" maxlength="20000" placeholder="${esc(L.writePlaceholder || '')}"></textarea>
        <p id="${tag}WriteCounts" class="small" role="status"></p>
        <div class="row"><button id="${tag}WriteCheck" class="primary">Revisar meu texto</button><button id="${tag}WriteSave" disabled>Registrar versão revisada</button><button id="${tag}WriteTutor">Preparar correção no chat</button></div>
        <div id="${tag}WriteResult" aria-live="polite"></div>
        <div id="${tag}TutorBox" hidden><label for="${tag}TutorText">Copie e cole este pedido no chat</label><textarea id="${tag}TutorText" readonly></textarea><button id="${tag}TutorCopy">Copiar pedido</button></div>
        <p id="${tag}WriteStatus" role="status"></p>
      </div>`;
    const writeItem = () => prompts.find(p => p.id === $(`${tag}WritePick`).value) || prompts[0];
    const drafts = () => (S().drafts ??= {});
    let writeEvaluation = null;
    function writingMetrics(text) {
      const list = units(text);
      const words = COUNTERS.words(text);
      return {
        units: list.length, words: words.length, unique: new Set(words.map(w => w.toLowerCase())).size,
        lines: text.split(/\r?\n/).filter(l => l.trim()).length,
        sentences: text.split(/[.!?。？！]+/).filter(x => x.trim()).length,
        paragraphs: text.trim() ? text.trim().split(/\n\s*\n/).length : 0,
      };
    }
    function writingChanged() {
      const p = writeItem();
      const text = $(`${tag}WriteText`).value;
      const m = writingMetrics(text);
      drafts()[p.id] = text;
      cfg.save();
      $(`${tag}WriteCounts`).textContent = `${m.units} / ${p.units} ${unitLabel} · ${m.lines} / ${p.lines} linhas · ${m.words} palavras`;
      writeEvaluation = null;
      $(`${tag}WriteSave`).disabled = true;
      $(`${tag}WriteResult`).innerHTML = '';
      $(`${tag}TutorBox`).hidden = true;
    }
    function chooseWriting() {
      const p = writeItem();
      $(`${tag}WritePrompt`).textContent = p.prompt;
      $(`${tag}WritePromptPt`).textContent = p.prompt_pt || '';
      $(`${tag}WriteGoal`).textContent = `${p.level} · mínimo de ${p.lines} linhas e ${p.units} ${unitLabel}. Use Enter para criar uma linha.`;
      $(`${tag}WriteText`).value = drafts()[p.id] || '';
      writingChanged();
    }
    $(`${tag}WritePick`).onchange = chooseWriting;
    $(`${tag}WriteText`).oninput = writingChanged;
    $(`${tag}WriteCheck`).onclick = () => {
      const text = $(`${tag}WriteText`).value;
      const p = writeItem();
      const m = writingMetrics(text);
      if (!m.units) { $(`${tag}WriteStatus`).textContent = 'Escreva algumas frases primeiro.'; return; }
      const enough = m.units >= p.units && m.lines >= p.lines;
      // Em idiomas com espaço, conector só conta como palavra inteira (o “y” de “Yo” não vale).
      const hasWord = c => ` ${text.toLowerCase().replace(/[^\p{L}\s]/gu, ' ').replace(/\s+/g, ' ')} `.includes(` ${c.toLowerCase()} `);
      const connectors = (L.connectors || []).filter(c => (L.unit === 'words' ? hasWord(c) : text.includes(c)));
      const notes = (cfg.writingChecks?.(text, p) || []).map(n => `<li>${n}</li>`).join('');
      writeEvaluation = { text, ...m };
      $(`${tag}WriteSave`).disabled = false;
      $(`${tag}WriteResult`).innerHTML = `<div class="feedback"><h3>Revisão orientativa · ${enough ? 'extensão atingida' : 'continue desenvolvendo'}</h3>`
        + `<p><b>Estrutura:</b> ${m.sentences} frase(s), ${m.paragraphs} parágrafo(s), ${m.units} ${esc(unitLabel)}.</p>`
        + `<p><b>Conectores:</b> ${connectors.length ? connectors.map(c => `<span lang="${L.html}">${esc(c)}</span>`).join(', ') : `nenhum ainda — experimente ${(L.connectors || []).slice(0, 3).map(esc).join(', ')}`}.</p>`
        + (notes ? `<ul>${notes}</ul>` : '')
        + '<p class="small">A revisão local não corrige gramática nem sentido. Para isso, use “Preparar correção no chat”.</p></div>';
      $(`${tag}WriteStatus`).textContent = 'Revisão pronta. Você pode registrar esta versão ou ajustá-la antes.';
    };
    $(`${tag}WriteSave`).onclick = () => {
      if (!writeEvaluation || writeEvaluation.text !== $(`${tag}WriteText`).value) return;
      const p = writeItem();
      const e = writeEvaluation;
      if (S().events.some(x => x.kind === 'writing' && x.ref === p.id && x.text === e.text)) { $(`${tag}WriteStatus`).textContent = 'Esta versão já está no histórico.'; return; }
      if (!addSkill({ kind: 'writing', ref: p.id, level: p.level, text: e.text, words: e.units, lines: e.lines, unique: e.unique, unit: L.unit })) return;
      $(`${tag}WriteSave`).disabled = true;
      $(`${tag}WriteStatus`).textContent = saveMessage();
    };
    $(`${tag}WriteTutor`).onclick = () => {
      const p = writeItem();
      $(`${tag}TutorText`).value = cfg.tutorPrompt(p, $(`${tag}WriteText`).value);
      $(`${tag}TutorBox`).hidden = false;
    };
    $(`${tag}TutorCopy`).onclick = async () => {
      $(`${tag}TutorText`).select();
      try { await navigator.clipboard.writeText($(`${tag}TutorText`).value); $(`${tag}WriteStatus`).textContent = 'Pedido copiado.'; } catch (_) { $(`${tag}WriteStatus`).textContent = 'Selecionado: use Ctrl+C para copiar.'; }
    };

    // ---------------------------------------------------------------- listening
    $('listening').innerHTML = `
      <div class="skill-heading"><span class="eyebrow">03 · Listening</span><h2>Primeiro escute. Depois confira.</h2>
      <p class="muted">Áudio narrado pela voz em ${esc(L.name)} do seu aparelho. Ao compartilhar a tela, inclua o som do computador para os outros ouvirem.</p></div>
      <div class="card">
        <div class="skill-filters"><div><label for="${tag}ListenVoice">Voz em ${esc(L.name)}</label><select id="${tag}ListenVoice"></select></div>
        <div><label for="${tag}ListenRate">Velocidade</label><select id="${tag}ListenRate"><option value="0.7">0,7 ×</option><option value="0.85" selected>0,85 ×</option><option value="1">1 ×</option></select></div></div>
      </div>
      <div class="card" id="${tag}ChoiceCard"><h3>Ouça e escolha · treino rápido</h3>
        <p class="small muted">Ouça a frase e escolha exatamente o que foi dito. As opções mudam só num ponto: partícula, tempo verbal ou terminação. Rodadas de ${LISTEN_CHOICE_ROUND}; o resultado entra no histórico.</p>
        <div class="row"><button id="${tag}LcPlay" class="primary">🔊 Ouvir frase</button><button id="${tag}LcSlow">Ouvir devagar</button><span id="${tag}LcCount" class="small muted"></span></div>
        <p id="${tag}LcStatus" class="small muted" role="status"></p>
        <div id="${tag}LcOptions" class="lc-options" lang="${L.html}"></div><div id="${tag}LcFeedback"></div>
        <div class="row"><button id="${tag}LcNext" class="primary" hidden>Próxima frase →</button></div>
      </div>
      <div class="card"><h3>Escute um texto</h3>
        <label for="${tag}ListenPick">Escolha seu áudio de prática</label><select id="${tag}ListenPick">${options(texts)}</select>
        <div class="row"><button id="${tag}ListenPlay" class="primary">Ouvir do início</button><button id="${tag}ListenStop">Parar áudio</button></div>
        <p id="${tag}ListenStatus" role="status"></p>
        <details id="${tag}ListenTranscript"><summary>Mostrar transcrição · apoio opcional</summary><div id="${tag}ListenText" class="passage" lang="${L.html}"></div><div id="${tag}ListenSupport"></div></details>
        <div id="${tag}ListenQuestions" class="quiz"></div>
        <button id="${tag}ListenCheck" class="primary">Corrigir e registrar listening</button>
        <div id="${tag}ListenResult" role="status"></div>
      </div>`;
    let listenPlayed = false;
    let listenSaved = false;
    let transcriptUsed = false;
    const listenItem = () => texts.find(p => p.id === $(`${tag}ListenPick`).value) || texts[0];
    function chooseListening() {
      stopSpeech();
      listenPlayed = false;
      listenSaved = false;
      transcriptUsed = false;
      const p = listenItem();
      $(`${tag}ListenText`).innerHTML = paragraphs(p.text);
      $(`${tag}ListenSupport`).innerHTML = supportBlock(p);
      $(`${tag}ListenTranscript`).open = false;
      quiz(`${tag}ListenQuestions`, p, `${tag}lq`);
      $(`${tag}ListenResult`).innerHTML = '';
      $(`${tag}ListenStatus`).textContent = 'Escute o áudio completo antes de responder.';
      $(`${tag}ListenCheck`).disabled = false;
    }
    $(`${tag}ListenPick`).onchange = chooseListening;
    $(`${tag}ListenPlay`).onclick = () => say(listenItem().text.replace(/\n\n/g, ' '), `${tag}ListenStatus`, () => { listenPlayed = true; });
    $(`${tag}ListenStop`).onclick = () => { stopSpeech(); $(`${tag}ListenStatus`).textContent = 'Áudio interrompido.'; };
    $(`${tag}ListenTranscript`).ontoggle = () => { if ($(`${tag}ListenTranscript`).open) transcriptUsed = true; };
    $(`${tag}ListenCheck`).onclick = () => {
      if (listenSaved) return;
      if (!listenPlayed) { $(`${tag}ListenResult`).textContent = 'Escute o áudio completo antes de registrar.'; return; }
      const p = listenItem();
      const r = quizResult(p, `${tag}lq`);
      if (!r) { $(`${tag}ListenResult`).textContent = 'Responda a todas as perguntas.'; return; }
      if (!addSkill({ kind: 'listening', ref: p.id, level: p.level, score: r.score, total: r.total, transcript: transcriptUsed })) return;
      listenSaved = true;
      lockQuiz(p, `${tag}lq`);
      $(`${tag}ListenCheck`).disabled = true;
      $(`${tag}ListenResult`).innerHTML = `<div class="feedback">${r.html}<p>${transcriptUsed ? 'Com apoio de transcrição.' : 'Sem abrir a transcrição.'} ${saveMessage()}</p></div>`;
    };

    // Ouça e escolha
    const choiceBank = cfg.data.listenChoice || [];
    let lc = null;
    function lcRender() {
      const item = lc.items[lc.i];
      item.order = item.order || shuffle(item.options);
      $(`${tag}LcCount`).textContent = `Frase ${lc.i + 1} de ${lc.items.length} · acertos ${lc.score}`;
      $(`${tag}LcOptions`).innerHTML = item.order.map((o, j) => `<button type="button" data-lc="${j}">${esc(o)}${cfg.roman?.[o] ? `<small>${esc(cfg.roman[o])}</small>` : ''}</button>`).join('');
      $(`${tag}LcFeedback`).innerHTML = '';
      $(`${tag}LcNext`).hidden = true;
      $(`${tag}LcStatus`).textContent = 'Ouça e escolha a frase que você ouviu.';
    }
    function lcStart() {
      lc = { items: shuffle(choiceBank).slice(0, LISTEN_CHOICE_ROUND).map(x => ({ ...x })), i: 0, score: 0, saved: false };
      if (lc.items.length) lcRender();
      else $(`${tag}ChoiceCard`).hidden = true;
    }
    const lcPlay = rate => { if (lc?.items.length) say(lc.items[lc.i].answer, `${tag}LcStatus`, null, rate); };
    $(`${tag}LcPlay`).onclick = () => lcPlay();
    $(`${tag}LcSlow`).onclick = () => lcPlay(0.6);
    $(`${tag}LcOptions`).onclick = e => {
      const b = e.target.closest('button');
      if (!b || !lc) return;
      const item = lc.items[lc.i];
      if (item.done) return;
      item.done = true;
      const chosen = item.order[Number(b.dataset.lc)];
      const ok = chosen === item.answer;
      if (ok) lc.score++;
      $(`${tag}LcOptions`).querySelectorAll('button').forEach(x => {
        x.disabled = true;
        const text = item.order[Number(x.dataset.lc)];
        if (text === item.answer) x.classList.add('correct');
        else if (x === b) x.classList.add('wrong');
      });
      $(`${tag}LcFeedback`).innerHTML = `<div class="feedback ${ok ? 'ok' : 'wrong'}"><h3>${ok ? '✓ Você ouviu certo!' : 'Era esta frase:'}</h3><p lang="${L.html}">${esc(item.answer)}</p><p>${esc(item.explanation || '')}</p></div>`;
      $(`${tag}LcCount`).textContent = `Frase ${lc.i + 1} de ${lc.items.length} · acertos ${lc.score}`;
      const last = lc.i + 1 >= lc.items.length;
      $(`${tag}LcNext`).textContent = last ? 'Nova rodada' : 'Próxima frase →';
      $(`${tag}LcNext`).hidden = false;
      if (last && !lc.saved) {
        lc.saved = true;
        if (addSkill({ kind: 'listening', ref: 'ouca-e-escolha', title: `Ouça e escolha · ${lc.items.length} frases`, level: 'Misto', score: lc.score, total: lc.items.length, transcript: false })) {
          $(`${tag}LcStatus`).textContent = `Rodada concluída: ${lc.score}/${lc.items.length}. ${saveMessage()}`;
        }
      }
    };
    $(`${tag}LcNext`).onclick = () => {
      if (lc.i + 1 >= lc.items.length) lcStart();
      else { lc.i++; lcRender(); }
      lcPlay();
    };

    // ---------------------------------------------------------------- speaking
    $('speaking').innerHTML = `
      <div class="skill-heading"><span class="eyebrow">04 · Speaking</span><h2>Uma ideia. Sua voz. Mais confiança.</h2>
      <p class="muted">Prepare palavras-chave por 30 segundos. Fale por 1 a 2 minutos, escute sua gravação e escolha um ponto para melhorar.</p></div>
      <div class="card">
        <label for="${tag}SpeakPick">Tema para falar</label><select id="${tag}SpeakPick">${options(prompts)}</select>
        <label for="${tag}SpeakMode">Formato do treino</label><select id="${tag}SpeakMode"><option value="monologue">Monólogo · apresente sua ideia</option><option value="roleplay">Entrevista · responda a três perguntas</option><option value="shadow">Shadowing · escute e repita um trecho</option></select>
        <div id="${tag}SpeakPrompt" class="notice" lang="${L.html}"></div><p id="${tag}SpeakPromptPt" class="small muted"></p>
        <button id="${tag}SpeakModel" hidden>Ouvir trecho de referência</button>
        <div class="timer-row"><output id="${tag}SpeakClock" class="clock">00:00</output><button id="${tag}SpeakPrepare">Preparar · 30 segundos</button><button id="${tag}SpeakStart" class="primary">Iniciar fala sem gravação</button><button id="${tag}SpeakRecord">Gravar minha voz</button><button id="${tag}SpeakStop" disabled>Encerrar fala</button><button id="${tag}SpeakEvaluate" disabled>Avaliar inteligibilidade com IA</button></div>
        <p id="${tag}SpeakStatus" role="status"></p>
        <audio id="${tag}SpeakAudio" controls hidden></audio><a id="${tag}SpeakDownload" hidden>Baixar minha gravação</a>
        <div id="${tag}SpeakResult" aria-live="polite"></div>
        <p class="small muted">O microfone só liga ao clicar em Gravar. O áudio fica nesta aba e só é enviado para avaliação quando você clicar em Avaliar; ele não entra no histórico.</p>
        <fieldset class="self-check"><legend>Depois de se ouvir, faça sua autoavaliação</legend>
          <label><input id="${tag}SpeakClear" type="checkbox"> Consegui transmitir minha ideia com clareza.</label>
          <label><input id="${tag}SpeakFlow" type="checkbox"> Continuei mesmo quando faltou uma palavra.</label>
          <label><input id="${tag}SpeakWords" type="checkbox"> Usei vocabulário relacionado ao tema.</label></fieldset>
        <label for="${tag}SpeakNotes">O que funcionou e o que vou melhorar?</label><textarea id="${tag}SpeakNotes" maxlength="2000"></textarea>
        <button id="${tag}SpeakSave" class="primary" disabled>Registrar treino de fala</button>
      </div>`;
    let speakClock = newClock();
    let speakStage = 'idle';
    let prepTimer = null;
    let recorder = null;
    let stream = null;
    let recordURL = null;
    let recordBlob = null;
    let evaluation = null;
    let evaluating = false;
    let tick = null;
    const speakItem = () => prompts.find(p => p.id === $(`${tag}SpeakPick`).value) || prompts[0];
    function shadowText() {
      const p = speakItem();
      const t = texts.find(x => x.level === p.level && x.topic === p.topic) || texts.find(x => x.level === p.level) || texts[0];
      return t.text.split('\n\n')[0];
    }
    function speakingPrompt() {
      const p = speakItem();
      const mode = $(`${tag}SpeakMode`).value;
      $(`${tag}SpeakPrompt`).textContent = mode === 'shadow' ? shadowText() : mode === 'roleplay' ? `${p.prompt}\n${cfg.data.roleplay || ''}` : p.prompt;
      $(`${tag}SpeakPromptPt`).textContent = mode === 'shadow' ? 'Ouça o trecho e repita em voz alta, imitando ritmo e entonação.' : (p.prompt_pt || '');
      $(`${tag}SpeakModel`).hidden = mode !== 'shadow';
    }
    function controls(active) {
      for (const id of ['SpeakPick', 'SpeakMode', 'SpeakStart', 'SpeakRecord', 'SpeakPrepare']) $(tag + id).disabled = active || evaluating;
      $(`${tag}SpeakStop`).disabled = !active;
      $(`${tag}SpeakEvaluate`).disabled = active || evaluating || !recordBlob || speakStage !== 'finished';
    }
    function clearRecording() {
      if (recordURL) URL.revokeObjectURL(recordURL);
      recordURL = null;
      recordBlob = null;
      evaluation = null;
      $(`${tag}SpeakAudio`).hidden = true;
      $(`${tag}SpeakDownload`).hidden = true;
      $(`${tag}SpeakResult`).innerHTML = '';
    }
    const releaseMic = () => { stream?.getTracks().forEach(t => t.stop()); stream = null; };
    function startTick() {
      clearInterval(tick);
      tick = setInterval(() => { $(`${tag}SpeakClock`).textContent = timeLabel(elapsed(speakClock)); }, 250);
    }
    function startSpeaking() {
      stopSpeech();
      clearTimeout(prepTimer);
      speakClock = newClock();
      speakClock.start = Date.now();
      speakStage = 'running';
      controls(true);
      $(`${tag}SpeakSave`).disabled = true;
      startTick();
      $(`${tag}SpeakStatus`).textContent = 'Fale com calma. O cronômetro está contando.';
    }
    function finishSpeaking() {
      clearTimeout(prepTimer);
      clearInterval(tick);
      if (speakStage === 'preparing') { speakStage = 'idle'; controls(false); $(`${tag}SpeakStatus`).textContent = 'Preparação encerrada.'; return; }
      if (speakStage !== 'running') return;
      pauseClock(speakClock);
      speakStage = 'finished';
      if (recorder && recorder.state !== 'inactive') recorder.stop();
      else controls(false);
      releaseMic();
      $(`${tag}SpeakClock`).textContent = timeLabel(speakClock.ms);
      $(`${tag}SpeakSave`).disabled = speakClock.ms < 1000;
      $(`${tag}SpeakStatus`).textContent = `Fala encerrada em ${timeLabel(speakClock.ms)}. Escute-se e faça sua autoavaliação.`;
    }
    $(`${tag}SpeakPick`).onchange = () => { speakStage = 'idle'; $(`${tag}SpeakSave`).disabled = true; clearRecording(); speakingPrompt(); };
    $(`${tag}SpeakMode`).onchange = $(`${tag}SpeakPick`).onchange;
    $(`${tag}SpeakModel`).onclick = () => say(shadowText(), `${tag}SpeakStatus`);
    $(`${tag}SpeakStart`).onclick = () => { clearRecording(); startSpeaking(); };
    $(`${tag}SpeakStop`).onclick = finishSpeaking;
    $(`${tag}SpeakPrepare`).onclick = () => {
      stopSpeech();
      speakStage = 'preparing';
      controls(true);
      $(`${tag}SpeakStatus`).textContent = 'Prepare três palavras-chave. A fala não começa automaticamente.';
      prepTimer = setTimeout(() => { speakStage = 'idle'; controls(false); $(`${tag}SpeakStatus`).textContent = 'Tempo de preparo encerrado. Comece quando quiser.'; }, 30000);
    };
    $(`${tag}SpeakRecord`).onclick = async () => {
      if (!navigator.mediaDevices?.getUserMedia || typeof MediaRecorder === 'undefined') { $(`${tag}SpeakStatus`).textContent = 'Gravação indisponível neste navegador. Use Iniciar fala sem gravação.'; return; }
      clearRecording();
      try {
        stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      } catch (_) {
        $(`${tag}SpeakStatus`).textContent = 'Não foi possível acessar o microfone. Confira a permissão do navegador.';
        return;
      }
      const chunks = [];
      const current = new MediaRecorder(stream);
      recorder = current;
      current.ondataavailable = e => { if (e.data.size) chunks.push(e.data); };
      current.onstop = () => {
        recordBlob = new Blob(chunks, { type: current.mimeType || 'audio/webm' });
        recordURL = URL.createObjectURL(recordBlob);
        $(`${tag}SpeakAudio`).src = recordURL;
        $(`${tag}SpeakAudio`).hidden = false;
        $(`${tag}SpeakDownload`).href = recordURL;
        $(`${tag}SpeakDownload`).download = `${tag}-speaking-${cfg.day()}${recordBlob.type.includes('mp4') ? '.m4a' : '.webm'}`;
        $(`${tag}SpeakDownload`).hidden = false;
        controls(false);
      };
      startSpeaking();
      current.start(1000);
      setTimeout(() => { if (recorder === current && current.state !== 'inactive') finishSpeaking(); }, MAX_RECORD_MS);
      $(`${tag}SpeakStatus`).textContent = 'Gravando sua voz… limite de 2 minutos.';
    };
    const toBase64 = blob => new Promise((resolve, reject) => {
      if (blob.size > MAX_AUDIO_BYTES) { reject(Error('A gravação passou de 15 MB. Grave por menos tempo.')); return; }
      const reader = new FileReader();
      reader.onload = () => resolve(String(reader.result).split(',', 2)[1] || '');
      reader.onerror = () => reject(Error('Não foi possível ler a gravação.'));
      reader.readAsDataURL(blob);
    });
    $(`${tag}SpeakEvaluate`).onclick = async () => {
      if (!recordBlob || evaluating || speakStage !== 'finished') return;
      evaluating = true;
      controls(false);
      $(`${tag}SpeakStatus`).textContent = 'Avaliando inteligibilidade…';
      try {
        const mode = $(`${tag}SpeakMode`).value;
        const reference = mode === 'shadow' ? shadowText() : $(`${tag}SpeakPrompt`).textContent;
        const response = await fetch('/api/speaking/evaluate', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ audio: await toBase64(recordBlob), mimeType: recordBlob.type, mode, reference, language: L.code }),
          signal: AbortSignal.timeout(150000),
        });
        const data = await response.json();
        if (!response.ok) throw Error(data.error || 'Não foi possível avaliar agora.');
        evaluation = data;
        const review = data.reviewWords?.length ? `<p><b>Trechos para repetir:</b> <span lang="${L.html}">${data.reviewWords.map(esc).join(', ')}</span></p>` : '';
        $(`${tag}SpeakResult`).innerHTML = `<div class="feedback"><h3>Inteligibilidade · ${data.score ?? '—'}${data.score === null ? '' : '%'}</h3>`
          + `<p><b>O que foi reconhecido:</b> <span lang="${L.html}">${esc(data.transcript)}</span></p>${review}`
          + '<p class="small">Resultado orientativo: ruído, microfone e sotaque afetam o reconhecimento. Não substitui um professor.</p></div>';
        $(`${tag}SpeakStatus`).textContent = 'Avaliação concluída.';
      } catch (e) {
        $(`${tag}SpeakStatus`).textContent = e.name === 'TimeoutError' ? 'A avaliação demorou demais. Tente novamente.' : e.message;
      } finally {
        evaluating = false;
        controls(false);
      }
    };
    $(`${tag}SpeakSave`).onclick = () => {
      if (speakStage !== 'finished' || speakClock.ms < 1000) return;
      const p = speakItem();
      const extra = evaluation && Number.isFinite(evaluation.score) ? { intelligibility: evaluation.score, speechText: evaluation.transcript } : {};
      if (!addSkill({
        kind: 'speaking', ref: p.id, level: p.level, seconds: speakClock.ms / 1000, mode: $(`${tag}SpeakMode`).value,
        notes: $(`${tag}SpeakNotes`).value, checks: ['SpeakClear', 'SpeakFlow', 'SpeakWords'].map(id => $(tag + id).checked), ...extra,
      })) return;
      speakStage = 'saved';
      $(`${tag}SpeakSave`).disabled = true;
      $(`${tag}SpeakStatus`).textContent = saveMessage();
    };

    // ---------------------------------------------------------------- histórico
    function renderHistory() {
      const box = $('skillsHistory');
      if (!box) return;
      const events = S().events;
      const kinds = ['reading', 'writing', 'listening', 'speaking'];
      const reads = events.filter(e => e.kind === 'reading').slice(-5);
      const avg = reads.length ? Math.round(reads.reduce((n, e) => n + e.wpm, 0) / reads.length) : 0;
      const detail = e => e.kind === 'reading' ? `${e.wpm} ${unitLabel}/min · ${timeLabel(e.seconds * 1000)} · compreensão ${e.score}/${e.total}${e.reread ? ' · releitura' : ''}`
        : e.kind === 'writing' ? `${e.words} ${unitLabel} · ${e.lines} linhas`
          : e.kind === 'listening' ? `${e.score}/${e.total}${e.transcript ? ' · com transcrição' : ''}`
            : `${timeLabel(e.seconds * 1000)} · autoavaliação ${(e.checks || []).filter(Boolean).length}/3 · ${e.mode}${Number.isFinite(e.intelligibility) ? ` · inteligibilidade ${e.intelligibility}%` : ''}`;
      const title = e => [...texts, ...prompts].find(p => p.id === e.ref)?.title || prompts.find(p => p.id === e.ref)?.prompt_pt || e.title || e.ref;
      box.innerHTML = `<div class="skill-summary">${kinds.map(k => `<div><span>${k[0].toUpperCase() + k.slice(1)}</span><strong>${events.filter(e => e.kind === k).length}</strong><small>treinos</small></div>`).join('')}</div>`
        + `<p class="small muted">${reads.length ? `Reading: média das últimas ${reads.length} leituras = ${avg} ${unitLabel}/min.` : 'Registre leituras para acompanhar sua velocidade e compreensão.'}</p>`
        + (events.slice(-30).reverse().map(e => `<details><summary>${esc(e.day)} · ${esc(e.kind)} · ${esc(e.level)} · ${esc(detail(e))}</summary><p>${esc(title(e))}</p>${e.text ? `<pre class="saved-writing" lang="${L.html}">${esc(e.text)}</pre>` : ''}${e.speechText ? `<p lang="${L.html}">${esc(e.speechText)}</p>` : ''}${e.notes ? `<p>${esc(e.notes)}</p>` : ''}</details>`).join('')
          || '<p class="muted">Nenhum treino de habilidades registrado ainda.</p>');
    }

    // ---------------------------------------------------------------- início
    if ('speechSynthesis' in window) {
      loadVoices();
      speechSynthesis.addEventListener?.('voiceschanged', loadVoices);
    }
    readChoices();
    chooseWriting();
    chooseListening();
    speakingPrompt();
    lcStart();
    renderHistory();
    document.addEventListener('visibilitychange', () => { if (document.hidden) pause(); });

    function pause() {
      pauseReading();
      stopSpeech();
      if (speakStage === 'running' || speakStage === 'preparing') finishSpeaking();
    }
    return { pause, renderHistory, say };
  }

  window.RoutineSkills = { mount, COUNTERS };
})();
