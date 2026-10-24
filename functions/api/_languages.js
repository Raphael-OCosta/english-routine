// Catálogo de idiomas e pacotes. `available` controla o que pode ser vendido:
// um idioma só entra no checkout quando o conteúdo dele estiver publicado.
// `speech`: código ISO-639-1 da transcrição e como comparar a fala no shadowing
// (palavras para alfabetos com espaço; sílabas para hangul, kana e hanzi).
export const LANGUAGES = {
  en: { name: 'Inglês', brand: 'English Routine', app: '/app.html', available: true, speech: { transcribe: 'en', tokens: 'words' } },
  ko: { name: 'Coreano', brand: 'Korean Routine', app: '/korean.html', available: false, speech: { transcribe: 'ko', tokens: 'syllables' } },
  zh: { name: 'Chinês', brand: 'Chinese Routine', app: '/chinese.html', available: false, speech: { transcribe: 'zh', tokens: 'syllables' } },
};

// Lookup keys dos preços no Stripe por quantidade de idiomas.
export const PLAN_LOOKUP_KEYS = {
  1: 'english_routine_mensal',
  2: 'routine_2_idiomas',
  3: 'routine_3_idiomas',
};

export const MAX_PLAN_SIZE = 3;
// Trocar idiomas já escolhidos é permitido uma vez a cada 30 dias;
// ocupar vagas vazias do pacote (após upgrade) é livre.
export const LANGUAGE_CHANGE_DAYS = 30;

export const availableLanguages = () => Object.keys(LANGUAGES).filter(code => LANGUAGES[code].available);

export function isLanguage(code) {
  return Object.hasOwn(LANGUAGES, code);
}

export function planSizeFromLookupKey(lookupKey) {
  const entry = Object.entries(PLAN_LOOKUP_KEYS).find(([, key]) => key === lookupKey);
  return entry ? Number(entry[0]) : null;
}

// Normaliza uma lista de idiomas pedida pelo cliente: só códigos conhecidos,
// sem repetição e dentro do limite do pacote.
export function cleanLanguages(list, { onlyAvailable = true, max = MAX_PLAN_SIZE } = {}) {
  if (!Array.isArray(list)) return [];
  const allowed = onlyAvailable ? availableLanguages() : Object.keys(LANGUAGES);
  return [...new Set(list.map(code => String(code).toLowerCase()))]
    .filter(code => allowed.includes(code))
    .slice(0, max);
}
