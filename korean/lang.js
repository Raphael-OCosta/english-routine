/* Korean Routine — configuração do idioma para practice/practice.js e skills/skills.js. */
(() => {
  'use strict';
  const CONNECTORS = ['그리고', '그래서', '하지만', '그런데', '그러면', '왜냐하면', '그러니까', '또', '먼저', '마지막으로'];

  // Tabela do hangul: letras, sílabas e o nome da letra no áudio.
  function alphabet({ $, esc, speak, data }) {
    const letterButton = (char, top, bottom) =>
      `<button type="button" data-say="${esc(char)}"><b lang="ko">${esc(char)}</b><small>${esc(top)}</small>${bottom ? `<small>${esc(bottom)}</small>` : ''}</button>`;
    $('consonants').innerHTML = data.consonants.map(([c, rr, name]) => letterButton(c, rr, name)).join('');
    $('vowels').innerHTML = data.vowels.map(([v, rr]) => letterButton(v, rr)).join('');
    const INITIALS = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ';
    const MEDIALS = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ';
    const RR = Object.fromEntries(data.consonants.map(([c, rr]) => [c, rr.split('/')[0]]));
    RR['ㅇ'] = '';
    RR['ㄹ'] = 'r';
    const VRR = Object.fromEntries(data.vowels);
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
  }

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

  window.ROUTINE_APP = {
    lang: {
      code: 'ko', html: 'ko', tts: 'ko-KR', voice: /^ko/i, rate: 0.85, name: 'coreano', nameCap: 'Coreano',
      brand: 'Korean Routine', cheer: '맞아요!', praise: '잘했어요!', levelPrefix: 'TOPIK', script: /[ᄀ-ᇿ㄰-㆏가-힣]/,
    },
    skills: { unit: 'syllables', unitLabel: 'sílabas', connectors: CONNECTORS, writePlaceholder: '여기에 한국어로 써 보세요…', rate: 0.85 },
    alphabet,
    writingChecks,
    tutorPrompt,
  };
})();
