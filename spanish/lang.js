/* Spanish Routine — configuração do idioma para practice/practice.js e skills/skills.js. */
(() => {
  'use strict';
  const CONNECTORS = ['y', 'pero', 'porque', 'también', 'además', 'entonces', 'por eso', 'sin embargo', 'primero', 'después', 'al final'];

  // Sons que mudam em relação ao português, com a palavra de exemplo falada.
  function alphabet({ $, esc, speak, data }) {
    $('sounds').innerHTML = data.sounds.map(([letter, sound, example, note]) =>
      `<button type="button" data-say="${esc(example)}" title="${esc(note)}"><b>${esc(letter)}</b><small>${esc(sound)}</small><small lang="es">${esc(example)}</small></button>`).join('');
    $('alphabet').addEventListener('click', event => {
      const b = event.target.closest('[data-say]');
      if (b) speak(b.dataset.say);
    });
  }

  // Erros típicos de quem fala português.
  const PT_HABITS = [
    [/\b(muito|mais|também|não|com|uma|você|então|porque)\b/i, 'Há palavras em português (muito, não, você, uma…). Em espanhol: mucho/muy, no, tú/usted, una.'],
    [/\b(eu|ele|ela|nós)\b/i, 'Pronomes em português (eu, ele, nós). Em espanhol: yo, él/ella, nosotros.'],
    [/ção\b|ções\b/i, 'Palavras terminadas em -ção viram -ción (canción, información).'],
    [/\bmuy (gente|calor|frío|hambre|dinero|tiempo)\b/i, 'Antes de substantivo use mucho/mucha (mucho calor, mucha gente), não muy.'],
    [/\bme gusta (los|las)\b/i, 'Com plural: me gustan los/las…'],
    [/\b(a el|de el)\b/i, 'Contrações: a + el = al; de + el = del.'],
  ];
  function writingChecks(text) {
    const notes = PT_HABITS.filter(([re]) => re.test(text)).map(([, tip]) => tip);
    if (/[¿¡]/.test(text) === false && /[?!]/.test(text)) notes.push('Perguntas e exclamações abrem com ¿ e ¡ (¿Qué tal? ¡Hola!).');
    if (!notes.length) notes.push('Nenhum hábito típico do português encontrado. Confira acentos e concordância.');
    return notes;
  }

  const tutorPrompt = (p, text) => `Corrija meu texto em espanhol com explicações em português (sou brasileiro). Nível de treino: ${p.level}. `
    + `Proposta: ${p.prompt} (${p.prompt_pt}). Meta: ${p.lines} linhas e ${p.units} palavras. `
    + 'Analise: cumprimento da proposta, conjugação e tempos verbais, ser/estar, gustar, artigos e contrações, acentos, falsos amigos e interferências do português '
    + '(portunhol). Mostre cada erro com a correção e a regra; depois uma versão revisada que preserve minhas ideias. Termine com três prioridades para o próximo treino.\n\nMeu texto:\n' + text;

  window.ROUTINE_APP = {
    lang: {
      code: 'es', html: 'es', tts: 'es-ES', voice: /^es/i, rate: 0.9, name: 'espanhol', nameCap: 'Espanhol',
      brand: 'Spanish Routine', cheer: '¡Muy bien!', praise: '¡Genial!', levelPrefix: 'A', levelNames: { 1: 'A1', 2: 'A2' },
      script: /[áéíóúñ¿¡]|\b(el|la|los|las|es|está|soy|que|de|en|y)\b/i,
    },
    skills: { unit: 'words', unitLabel: 'palavras', connectors: CONNECTORS, writePlaceholder: 'Escribe aquí en español…', rate: 0.9 },
    alphabet,
    writingChecks,
    tutorPrompt,
  };
})();
