/* German Routine — configuração do idioma para practice/practice.js e skills/skills.js. */
(() => {
  'use strict';
  const CONNECTORS = ['und', 'aber', 'oder', 'denn', 'weil', 'deshalb', 'dann', 'danach', 'zuerst', 'auch', 'trotzdem', 'außerdem'];

  // Sons que mudam em relação ao português, com a palavra de exemplo falada.
  function alphabet({ $, esc, speak, data }) {
    $('sounds').innerHTML = data.sounds.map(([letter, sound, example, note]) =>
      `<button type="button" data-say="${esc(example)}" title="${esc(note)}"><b>${esc(letter)}</b><small>${esc(sound)}</small><small lang="de">${esc(example)}</small></button>`).join('');
    $('alphabet').addEventListener('click', event => {
      const b = event.target.closest('[data-say]');
      if (b) speak(b.dataset.say);
    });
  }

  // Erros típicos de quem fala português.
  const PT_HABITS = [
    [/\b(muito|não|você|uma|então|também|porque|com|eu)\b/i, 'Há palavras em português (muito, não, você…). Em alemão: sehr/viel, nicht/kein, du/Sie, eine, mit, ich.'],
    [/\bich habe (\d+|zwanzig|dreißig|zehn) jahre\b/i, 'Idade usa sein: Ich bin zwanzig (Jahre alt).'],
    [/\bich habe (gegangen|gefahren|gekommen|geflogen)\b/i, 'Verbos de movimento usam sein no Perfekt: ich bin gegangen.'],
    [/\b(heute|morgen|gestern|dann|jetzt) (ich|du|er|sie|wir|ihr) (\w+e|\w+st|\w+t|\w+en)\b/i, 'Depois de advérbio no início, o verbo vem antes do sujeito: Heute gehe ich…'],
    [/\bin dem\b/i, 'in + dem costuma virar im (im Park, im Kino).'],
    [/\bnicht (ein|eine|einen)\b/i, 'Para negar substantivo use kein: kein Auto, keine Zeit, keinen Hund.'],
  ];
  function writingChecks(text) {
    const notes = PT_HABITS.filter(([re]) => re.test(text)).map(([, tip]) => tip);
    const lowerNouns = text.match(/\b(der|die|das|den|dem|ein|eine|einen|kein|keine) [a-zäöü]{3,}\b/g);
    if (lowerNouns) notes.push(`Substantivos começam com maiúscula: confira “${lowerNouns[0]}”.`);
    if (!notes.length) notes.push('Nenhum hábito típico do português encontrado. Confira artigos (der/die/das), casos e a posição do verbo.');
    return notes;
  }

  const tutorPrompt = (p, text) => `Corrija meu texto em alemão com explicações em português (sou brasileiro). Nível de treino: ${p.level}. `
    + `Proposta: ${p.prompt} (${p.prompt_pt}). Meta: ${p.lines} linhas e ${p.units} palavras. `
    + 'Analise: cumprimento da proposta, conjugação e tempos (Präsens, Perfekt com haben/sein, Futur), posição do verbo (2ª posição e final), '
    + 'artigos e casos (nominativo, acusativo, dativo), maiúsculas dos substantivos, kein × nicht e interferências do português. Mostre cada erro com a correção e a regra; '
    + 'depois uma versão revisada que preserve minhas ideias. Termine com três prioridades para o próximo treino.\n\nMeu texto:\n' + text;

  window.ROUTINE_APP = {
    lang: {
      code: 'de', html: 'de', tts: 'de-DE', voice: /^de/i, rate: 0.9, name: 'alemão', nameCap: 'Alemão',
      brand: 'German Routine', cheer: 'Sehr gut!', praise: 'Super!', levelPrefix: 'A', levelNames: { 1: 'A1', 2: 'A2' },
      script: /[äöüß]|\b(der|die|das|und|ist|ich|nicht|ein|eine)\b/i,
    },
    skills: { unit: 'words', unitLabel: 'palavras', connectors: CONNECTORS, writePlaceholder: 'Schreib hier auf Deutsch…', rate: 0.9 },
    alphabet,
    writingChecks,
    tutorPrompt,
  };
})();
