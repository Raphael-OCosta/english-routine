/* Japanese Routine — configuração do idioma para practice/practice.js e skills/skills.js. */
(() => {
  'use strict';
  const CONNECTORS = ['そして', 'でも', 'だから', 'それから', 'それに', 'しかし', 'ので', 'から', 'まず', '最後に'];

  // Tabelas de hiragana e katakana; o katakana é o hiragana deslocado no Unicode.
  function alphabet({ $, esc, speak, data }) {
    const kata = s => s.replace(/[ぁ-ゖ]/g, c => String.fromCharCode(c.charCodeAt(0) + 0x60));
    const button = (ch, r) => `<button type="button" data-say="${esc(ch)}"><b lang="ja">${esc(ch)}</b><small>${esc(r)}</small></button>`;
    $('hiragana').innerHTML = data.hiragana.map(([k, r]) => button(k, r)).join('');
    $('katakana').innerHTML = data.hiragana.map(([k, r]) => button(kata(k), r)).join('');
    $('alphabet').addEventListener('click', event => {
      const b = event.target.closest('[data-say]');
      if (b) speak(b.dataset.say);
    });
  }

  function writingChecks(text) {
    const notes = [];
    const jp = (text.match(/[぀-ヿ一-鿿]/g) || []).length;
    const latin = (text.match(/[A-Za-z]/g) || []).length;
    if (latin > jp * 0.3) notes.push('Há bastante romaji. Tente escrever em kana e kanji (o teclado japonês converte o que você digita).');
    const sentences = text.split(/[。！？\n]+/).map(x => x.trim()).filter(x => /[぀-ヿ一-鿿]/.test(x));
    const polite = sentences.filter(x => /(です|ます|ました|ません|でした|ましょう)$/.test(x)).length;
    const plain = sentences.length - polite;
    if (polite && plain) notes.push(`Você misturou estilo educado (-です/-ます, ${polite} frase(s)) e estilo simples (${plain}). Em um mesmo texto, escolha um.`);
    else if (polite) notes.push('Estilo educado (-です/-ます) consistente.');
    if (/[,.]/.test(text.replace(/[A-Za-z0-9][,.]/g, ''))) notes.push('Use a pontuação japonesa: 、 e 。');
    if (/私は.*私は/.test(text)) notes.push('私は aparece várias vezes. Em japonês o sujeito óbvio costuma ser omitido.');
    return notes;
  }

  const tutorPrompt = (p, text) => `Corrija meu texto em japonês com explicações em português. Nível de treino: ${p.level}. `
    + `Proposta: ${p.prompt} (${p.prompt_pt}). Meta: ${p.lines} linhas e ${p.units} caracteres. `
    + 'Analise: cumprimento da proposta, partículas (は/が, を, に/で, へ, の, と, も), conjugação dos verbos (-masu, -te, passado), adjetivos い/な, '
    + 'consistência do estilo educado, escolha de kana e kanji e naturalidade. Mostre cada erro com a correção, a leitura em kana/romaji e a regra; '
    + 'depois uma versão revisada que preserve minhas ideias. Termine com três prioridades para o próximo treino.\n\nMeu texto:\n' + text;

  window.ROUTINE_APP = {
    lang: {
      code: 'ja', html: 'ja', tts: 'ja-JP', voice: /^ja/i, rate: 0.85, name: 'japonês', nameCap: 'Japonês',
      brand: 'Japanese Routine', cheer: 'せいかい！', praise: 'すごい！', levelPrefix: 'N', levelNames: { 1: 'N5', 2: 'N4' },
      script: /[぀-ヿ一-鿿]/,
    },
    skills: { unit: 'syllables', unitLabel: 'caracteres', connectors: CONNECTORS, writePlaceholder: 'ここに日本語で書いてください…', rate: 0.85 },
    alphabet,
    writingChecks,
    tutorPrompt,
  };
})();
