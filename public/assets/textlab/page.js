/* Página "Textos por gramática" (public/textos.html): controles, texto destacado, lacunas e gabarito.
 * As escolhas ficam no endereço (#g=…&s=…&seed=…): o mesmo link reabre o mesmo texto.
 */
(() => {
  'use strict';
  const { GRAMMAR, FORMS, generate } = window.TextLab;
  const STORIES = window.TEXTLAB_STORIES;
  const $ = id => document.getElementById(id);
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const COLORS = {
    ps: '#2563eb', pc: '#0ea5e9', past: '#7c3aed', pastc: '#a855f7', pp: '#db2777', pastp: '#be123c', will: '#059669', going: '#10b981',
    usedto: '#b45309', can: '#ea580c', should: '#dc2626', might: '#d97706', passive: '#0f766e', cond1: '#4f46e5', cond2: '#6d28d9',
  };
  const PT = {
    ps: 'hábitos e fatos', pc: 'ação acontecendo agora', past: 'ação terminada no passado', pastc: 'ação em andamento no passado',
    pp: 'passado ligado ao presente', pastp: 'passado antes de outro passado', will: 'previsões e decisões', going: 'planos e intenções',
    usedto: 'hábitos antigos', can: 'habilidade', should: 'conselho e obrigação', might: 'possibilidade', passive: 'foco em quem recebe a ação',
    cond1: 'condição real no futuro', cond2: 'condição imaginária',
  };

  // ------------------------------------------------------------ controles
  const groups = {};
  Object.entries(GRAMMAR).forEach(([key, g]) => { (groups[g.group] ??= []).push(key); });
  $('grammar').innerHTML = Object.entries(groups).map(([name, keys]) => `<div class="group">${esc(name)}</div><div class="chips">${keys.map(k =>
    `<label class="chip" title="${esc(PT[k])}" style="--c:${COLORS[k]}"><input type="checkbox" value="${k}"><span><i></i>${esc(GRAMMAR[k].label)}</span></label>`).join('')}</div>`).join('');
  $('story').innerHTML = STORIES.map(s => `<option value="${s.id}">${esc(s.label)} · ${esc(s.title)}</option>`).join('');
  $('forms').innerHTML = Object.entries(FORMS).map(([k, label]) => `<label><input type="checkbox" value="${k}"${k !== 'q' ? ' checked' : ''}> ${label}</label>`).join('');

  const picked = box => [...$(box).querySelectorAll('input:checked')].map(i => i.value);
  let seed = 0;
  let result = null;
  let tab = 'text';

  function readHash() {
    const h = new URLSearchParams(location.hash.slice(1));
    if (!h.get('g')) return false;
    const g = h.get('g').split(',');
    $('grammar').querySelectorAll('input').forEach(i => { i.checked = g.includes(i.value); });
    if (h.get('s')) $('story').value = h.get('s');
    const f = (h.get('f') || 'aff').split(',');
    $('forms').querySelectorAll('input').forEach(i => { i.checked = f.includes(i.value); });
    if (h.get('n')) $('size').value = h.get('n');
    $('connectors').checked = h.get('c') !== '0';
    seed = Number(h.get('seed')) || 1;
    return true;
  }
  function writeHash() {
    const h = new URLSearchParams({ g: picked('grammar').join(','), s: $('story').value, f: picked('forms').join(','), n: $('size').value, c: $('connectors').checked ? '1' : '0', seed });
    history.replaceState(null, '', '#' + h);
  }

  function run(newSeed) {
    const grammar = picked('grammar');
    if (!grammar.length) { $('status').textContent = 'Marque ao menos uma estrutura.'; return; }
    const forms = picked('forms');
    if (newSeed || !seed) seed = Math.floor(Math.random() * 1e9) + 1;
    const story = STORIES.find(s => s.id === $('story').value) || STORIES[0];
    result = generate(story, { grammar, forms: forms.length ? forms : ['aff'], sentences: Number($('size').value), seed, connectors: $('connectors').checked });
    writeHash();
    const counts = {};
    result.sentences.forEach(s => { counts[s.g] = (counts[s.g] || 0) + 1; });
    const missing = grammar.filter(g => !counts[g]);
    $('status').textContent = result.sentences.length < Number($('size').value)
      ? `Este tema rendeu ${result.sentences.length} frases com essa combinação.` : '';
    if (missing.length) $('status').textContent += ` ${missing.map(g => GRAMMAR[g].label).join(', ')} não coube neste tema.`;
    render();
  }

  // ------------------------------------------------------------ saída
  function legend() {
    const counts = {};
    result.sentences.forEach(s => { counts[s.g] = (counts[s.g] || 0) + 1; });
    return `<div class="legend">${Object.entries(counts).map(([g, n]) => `<span style="--c:${COLORS[g]}" title="${esc(PT[g])}"><i></i>${esc(GRAMMAR[g].label)} · ${n}</span>`).join('')}</div>`;
  }
  function header(kind) {
    const total = result.sentences.length;
    const forms = [...new Set(result.sentences.map(s => FORMS[s.f]))].join(', ').toLowerCase();
    return `<span class="eyebrow">${kind}</span><h3 lang="en">${esc(result.title)}</h3><p class="meta">${total} frases · ${forms}</p>`;
  }
  const sentenceHtml = (s, mode, hint) => s.seg.map((x, i) => {
    if (!x.g) return esc(x.t);
    if (mode === 'text') return `<span class="t" style="--c:${COLORS[x.g]}">${esc(x.t)}</span>`;
    const group = groupsOf.get(x.id);
    const last = group.lastIndex === i && group.sentence === s;
    const label = group.first === x ? `<span class="gap">${group.n}</span>` : '<span class="gap">&nbsp;</span>';
    const h = !last || hint === 'none' ? '' : ` <span class="hint">(${esc(hint === 'both' ? `${x.base} · ${GRAMMAR[x.g].label}` : x.base)})</span>`;
    return label + h;
  }).join('');

  let groupsOf = new Map();
  function indexGroups() {
    groupsOf = new Map();
    let n = 0;
    result.sentences.forEach(s => s.seg.forEach((x, i) => {
      if (!x.g) return;
      if (!groupsOf.has(x.id)) groupsOf.set(x.id, { n: ++n, first: x, parts: [], sentence: s, lastIndex: i, g: x.g, base: x.base });
      const g = groupsOf.get(x.id);
      g.parts.push(x.t);
      g.lastIndex = i;
    }));
  }

  function render() {
    if (!result) return;
    indexGroups();
    const paragraphs = mode => result.paragraphs.map(p => `<p class="par" lang="en">${p.map(s => sentenceHtml(s, mode, $('hint').value)).join(' ')}</p>`).join('');
    const key = [...groupsOf.values()].map(g => `<li><b>${esc(g.parts.join(' … '))}</b> <span class="muted small">· ${esc(GRAMMAR[g.g].label)}</span></li>`).join('');
    $('out').innerHTML = `
      <div data-panel="text"${tab === 'text' ? '' : ' hidden'} class="${$('highlight').checked ? 'hl' : ''}">${header('Texto')}${legend()}${paragraphs('text')}</div>
      <div data-panel="exercise"${tab === 'exercise' ? '' : ' hidden'}>${header('Exercício · complete as lacunas')}
        <p class="small muted">Complete cada lacuna com a forma correta do verbo entre parênteses. Lacunas com o mesmo número formam uma única resposta (por exemplo, auxiliar e verbo principal numa pergunta).</p>${paragraphs('gap')}</div>
      <div data-panel="key"${tab === 'key' ? '' : ' hidden'}>${header('Gabarito')}<ol class="key" lang="en">${key}</ol></div>`;
    $('hlWrap').style.display = tab === 'text' ? '' : 'none';
    $('hint').style.display = tab === 'exercise' ? '' : 'none';
  }

  function plain() {
    const panel = $('out').querySelector(`[data-panel="${tab}"]`);
    if (!panel) return '';
    const clone = panel.cloneNode(true);
    clone.querySelectorAll('.gap').forEach(g => { g.textContent = g.textContent.trim() ? `____(${g.textContent.trim()})` : '____'; });
    clone.querySelectorAll('.legend').forEach(l => l.remove());
    let n = 0;
    return [...clone.querySelectorAll('h3, .meta, p, li')].map(el => (el.tagName === 'LI' ? `${++n}. ` : '') + el.textContent.trim()).join('\n\n');
  }

  // ------------------------------------------------------------ eventos
  document.querySelectorAll('[role=tab]').forEach(b => b.addEventListener('click', () => {
    tab = b.dataset.tab;
    document.querySelectorAll('[role=tab]').forEach(x => x.setAttribute('aria-selected', String(x === b)));
    render();
  }));
  $('generate').onclick = () => run(true);
  $('another').onclick = () => run(true);
  $('highlight').onchange = render;
  $('hint').onchange = render;
  $('print').onclick = () => print();
  $('copy').onclick = async () => {
    const text = plain();
    try { await navigator.clipboard.writeText(text); $('status').textContent = 'Copiado. Cole no seu documento.'; } catch (_) { $('status').textContent = 'Não foi possível copiar automaticamente.'; }
  };

  if (readHash()) run(false);
  else {
    ['pp', 'should'].forEach(k => { $('grammar').querySelector(`input[value="${k}"]`).checked = true; });
    run(true);
  }
})();
