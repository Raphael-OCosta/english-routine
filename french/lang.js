/* French Routine — configuração do idioma para practice/practice.js e skills/skills.js. */
(() => {
  'use strict';
  const CONNECTORS = ['et', 'mais', 'parce que', 'donc', 'alors', 'aussi', 'ensuite', 'puis', 'enfin', "d'abord", 'cependant', 'pourtant'];

  // Sons que mudam em relação ao português, com a palavra de exemplo falada.
  function alphabet({ $, esc, speak, data }) {
    $('sounds').innerHTML = data.sounds.map(([letter, sound, example, note]) =>
      `<button type="button" data-say="${esc(example)}" title="${esc(note)}"><b>${esc(letter)}</b><small>${esc(sound)}</small><small lang="fr">${esc(example)}</small></button>`).join('');
    $('alphabet').addEventListener('click', event => {
      const b = event.target.closest('[data-say]');
      if (b) speak(b.dataset.say);
    });
  }

  // Erros típicos de quem fala português.
  const PT_HABITS = [
    [/\b(muito|não|você|uma|então|também|porque|com)\b/i, 'Há palavras em português (muito, não, você…). Em francês: très/beaucoup, ne…pas, tu/vous, une.'],
    [/\b(eu|ele|ela|nós)\b/i, 'Pronomes em português. Em francês: je, il/elle, nous.'],
    [/\bje (ai|aime|habite|étudie|écoute|écris|achète|attends)\b/i, 'Antes de vogal, je vira j\' (j\'ai, j\'aime, j\'habite).'],
    [/\bne (a|ai|est|aime|habite)\b/i, 'Antes de vogal, ne vira n\' (je n\'aime pas, il n\'est pas).'],
    [/\b(à le|à les|de le|de les)\b/i, 'Contrações: à + le = au, à + les = aux, de + le = du, de + les = des.'],
    [/\bje suis (\d+|vingt|trente|dix) ans\b/i, 'Idade usa avoir: j\'ai vingt ans (não je suis).'],
  ];
  function writingChecks(text) {
    const notes = PT_HABITS.filter(([re]) => re.test(text)).map(([, tip]) => tip);
    if (/\bne\b/i.test(text) && !/\b(pas|jamais|rien|plus|personne)\b/i.test(text)) notes.push('Você usou ne sem pas (ne … pas).');
    if (!notes.length) notes.push('Nenhum hábito típico do português encontrado. Confira acentos, artigos e concordância.');
    return notes;
  }

  const tutorPrompt = (p, text) => `Corrija meu texto em francês com explicações em português (sou brasileiro). Nível de treino: ${p.level}. `
    + `Proposta: ${p.prompt} (${p.prompt_pt}). Meta: ${p.lines} linhas e ${p.units} palavras. `
    + 'Analise: cumprimento da proposta, conjugação e tempos (présent, passé composé com avoir/être, imparfait, futur proche), artigos e partitivos, '
    + 'contrações (au, du), elisão, acentos, concordância e falsos amigos/interferências do português. Mostre cada erro com a correção e a regra; '
    + 'depois uma versão revisada que preserve minhas ideias. Termine com três prioridades para o próximo treino.\n\nMeu texto:\n' + text;

  window.ROUTINE_APP = {
    lang: {
      code: 'fr', html: 'fr', tts: 'fr-FR', voice: /^fr/i, rate: 0.9, name: 'francês', nameCap: 'Francês',
      brand: 'French Routine', cheer: 'Très bien !', praise: 'Bravo !', levelPrefix: 'A', levelNames: { 1: 'A1', 2: 'A2' },
      script: /[àâçéèêëîïôûùœ]|\b(le|la|les|est|je|une|des|du|et|que)\b/i,
    },
    skills: { unit: 'words', unitLabel: 'palavras', connectors: CONNECTORS, writePlaceholder: 'Écrivez ici en français…', rate: 0.9 },
    alphabet,
    writingChecks,
    tutorPrompt,
  };
})();
