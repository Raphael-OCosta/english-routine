/* Italian Routine — configuração do idioma para practice/practice.js e skills/skills.js. */
(() => {
  'use strict';
  const CONNECTORS = ['e', 'ma', 'perché', 'quindi', 'allora', 'anche', 'poi', 'infine', 'prima', 'però', 'invece', 'inoltre'];

  // Sons que mudam em relação ao português, com a palavra de exemplo falada.
  function alphabet({ $, esc, speak, data }) {
    $('sounds').innerHTML = data.sounds.map(([letter, sound, example, note]) =>
      `<button type="button" data-say="${esc(example)}" title="${esc(note)}"><b>${esc(letter)}</b><small>${esc(sound)}</small><small lang="it">${esc(example)}</small></button>`).join('');
    $('alphabet').addEventListener('click', event => {
      const b = event.target.closest('[data-say]');
      if (b) speak(b.dataset.say);
    });
  }

  // Erros típicos de quem fala português.
  const PT_HABITS = [
    [/\b(muito|não|você|uma|então|também|porque|com|eu)\b/i, 'Há palavras em português (muito, não, você…). Em italiano: molto, non, tu/Lei, una, con, io.'],
    [/\b(a il|a lo|a la|in il|in la|di il|di la|su il)\b/i, 'Preposição + artigo se juntam: al, allo, alla, nel, nella, del, della, sul.'],
    [/\bsono (\d+|venti|trenta|dieci) anni\b/i, 'Idade usa avere: ho vent\'anni (não sono).'],
    [/\b(la mia|il mio) (madre|padre|sorella|fratello|moglie|marito)\b/i, 'Com parentes no singular o possessivo vai sem artigo: mia madre, mio fratello.'],
    [/\bmi piace (i|gli|le)\b/i, 'Com plural use mi piacciono: mi piacciono i gatti.'],
    [/\bho (andato|venuto|uscito|tornato|partito)\b/i, 'Verbos de movimento usam essere: sono andato/a.'],
  ];
  function writingChecks(text) {
    const notes = PT_HABITS.filter(([re]) => re.test(text)).map(([, tip]) => tip);
    if (!notes.length) notes.push('Nenhum hábito típico do português encontrado. Confira acentos (è × e), artigos e concordância.');
    return notes;
  }

  const tutorPrompt = (p, text) => `Corrija meu texto em italiano com explicações em português (sou brasileiro). Nível de treino: ${p.level}. `
    + `Proposta: ${p.prompt} (${p.prompt_pt}). Meta: ${p.lines} linhas e ${p.units} palavras. `
    + 'Analise: cumprimento da proposta, conjugação e tempos (presente, passato prossimo com avere/essere, imperfetto, futuro), artigos (il/lo/la/l\'), '
    + 'preposições articuladas (al, nel, del), concordância, acentos e falsos amigos/interferências do português. Mostre cada erro com a correção e a regra; '
    + 'depois uma versão revisada que preserve minhas ideias. Termine com três prioridades para o próximo treino.\n\nMeu texto:\n' + text;

  window.ROUTINE_APP = {
    lang: {
      code: 'it', html: 'it', tts: 'it-IT', voice: /^it/i, rate: 0.9, name: 'italiano', nameCap: 'Italiano',
      brand: 'Italian Routine', cheer: 'Bravissimo!', praise: 'Perfetto!', levelPrefix: 'A', levelNames: { 1: 'A1', 2: 'A2' },
      script: /[àèéìòù]|\b(il|lo|gli|sono|che|non|una|della|perché)\b/i,
    },
    skills: { unit: 'words', unitLabel: 'parole', connectors: CONNECTORS, writePlaceholder: 'Scrivi qui in italiano…', rate: 0.9 },
    alphabet,
    writingChecks,
    tutorPrompt,
  };
})();
