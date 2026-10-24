/* Chinese Routine — configuração do idioma para practice/practice.js e skills/skills.js. */
(() => {
  'use strict';
  const CONNECTORS = ['因为', '所以', '但是', '可是', '然后', '而且', '如果', '还有', '最后', '先'];

  // Tons, iniciais e finais do pinyin, com o exemplo falado em caracteres.
  function alphabet({ $, esc, speak, data }) {
    const button = (say, big, top, bottom) =>
      `<button type="button" data-say="${esc(say)}"><b>${esc(big)}</b><small>${esc(top)}</small>${bottom ? `<small lang="zh-CN">${esc(bottom)}</small>` : ''}</button>`;
    $('tones').innerHTML = data.tones.map(([py, hz, pt]) => button(hz, py, pt, hz)).join('');
    $('initials').innerHTML = data.initials.map(([letter, hz, py]) => button(hz, letter, py, hz)).join('');
    $('finals').innerHTML = data.finals.map(([letter, hz, py]) => button(hz, letter, py, hz)).join('');
    $('alphabet').addEventListener('click', event => {
      const b = event.target.closest('[data-say]');
      if (b) speak(b.dataset.say);
    });
  }

  function writingChecks(text) {
    const notes = [];
    const hanzi = (text.match(/[一-鿿]/g) || []).length;
    const latin = (text.match(/[A-Za-z]/g) || []).length;
    if (latin > hanzi * 0.3) notes.push('Há bastante alfabeto latino. Tente escrever em caracteres (o teclado pinyin converte o que você digita).');
    if (/是(很|太|非常)?(忙|好|大|小|热|冷|贵|便宜|漂亮|高兴|累|难|容易)/.test(text)) notes.push('Parece haver 是 antes de adjetivo (ex.: 我是忙). Com adjetivos use 很: 我很忙.');
    if (/没(是|喜欢)/.test(text)) notes.push('是 e 喜欢 são negados com 不 (不是, 不喜欢), não com 没.');
    if (/[二](个|本|杯|件|张|双|条|只|瓶|碗)/.test(text)) notes.push('Antes de classificador, “dois” é 两 (两个, 两本), não 二.');
    if (/[,.?!]/.test(text.replace(/[A-Za-z0-9][,.?!]/g, ''))) notes.push('Use a pontuação chinesa: ，。？！');
    const sentences = text.split(/[。！？\n]+/).filter(x => /[一-鿿]/.test(x)).length;
    if (sentences) notes.push(`${sentences} frase(s) em chinês.`);
    return notes;
  }

  const tutorPrompt = (p, text) => `Corrija meu texto em chinês (mandarim, caracteres simplificados) com explicações em português. Nível de treino: ${p.level}. `
    + `Proposta: ${p.prompt} (${p.prompt_pt}). Meta: ${p.lines} linhas e ${p.units} caracteres. `
    + 'Analise: cumprimento da proposta, ordem da frase (tempo e lugar antes do verbo), classificadores, 不 × 没, 了/过, 的/得, uso de 是 com adjetivos, '
    + 'escolha de palavras e caracteres. Mostre cada erro com a correção, o pinyin e a regra; depois uma versão revisada que preserve minhas ideias, '
    + 'com pinyin. Termine com três prioridades para o próximo treino.\n\nMeu texto:\n' + text;

  window.ROUTINE_APP = {
    lang: {
      code: 'zh', html: 'zh-CN', tts: 'zh-CN', voice: /^(zh|cmn)/i, rate: 0.8, name: 'chinês', nameCap: 'Chinês (mandarim)',
      brand: 'Chinese Routine', cheer: '对了！', praise: '很好！', levelPrefix: 'HSK', script: /[一-鿿]/,
    },
    skills: { unit: 'syllables', unitLabel: 'caracteres', connectors: CONNECTORS, writePlaceholder: '请在这里用中文写…', rate: 0.8 },
    alphabet,
    writingChecks,
    tutorPrompt,
  };
})();
