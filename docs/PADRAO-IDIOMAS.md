# Padrão para novos idiomas (Routine)

Cada idioma é um app próprio no mesmo site (`/app.html` inglês, `/korean.html` coreano, …), com login, assinatura, sincronização e histórico compartilhados. Este documento é o checklist para criar o próximo (ex.: mandarim `zh`, japonês `ja`).

## 1. Peças comuns (não copiar, reutilizar)

| Peça | Onde | O que faz |
|---|---|---|
| Catálogo | `functions/api/_languages.js` | `name`, `brand`, `app`, `available`, `speech: {transcribe, tokens}` |
| Acesso | `functions/api/_shared.js` → `requireActive(env, user, lang)` | assinatura/cortesia/admin por idioma |
| Progresso | `/api/progress?lang=xx` + `public/assets/cloud-sync.js` | `window.ROUTINE_LANGUAGE = "xx"`, chave `routine-xx-v1` |
| Fala | `/api/speaking/evaluate` com `language: "xx"` | transcrição no idioma; shadowing por palavras ou sílabas |
| Treino de questões | `practice/practice.js`, `practice/template.html`, `practice/styles.css`, `practice/build.py` | filtros, rodadas, múltipla escolha × digitar, várias lacunas, pronúncia nas opções, guia, progresso |
| Habilidades | `skills/skills.js`, `skills/skills.css`, `skills/build.py` | Reading, Writing, Listening (texto + “Ouça e escolha”) e Speaking |
| Teste de nível | `placement/placement.js`, `placement/template.html`, `placement/build_placement.py`, `placement/bank_<lang>.py` | teste adaptativo (EAP, 3PL), resultado por nível e plano de treino |
| Painel | `public/assets/dashboard.js` | “Em breve”, botão **Testar** para admin, **Treinar** quando `available` |

O inglês tem implementação própria das habilidades (anterior ao módulo) e grava **o mesmo esquema de eventos**, então históricos e relatórios ficam comparáveis.

## 2. Estrutura de um idioma

```
<idioma>/
  content.py          # banco de questões (gramática, vocabulário, …)
  skills_content.py   # TEXTS, PROMPTS, ROLEPLAY
  lang.js             # window.ROUTINE_APP: lang (code, tts, voice, script, brand, levelPrefix, cheer…), alphabet(), writingChecks(), tutorPrompt()
  alphabet.html       # conteúdo da aba do alfabeto/sons (Hangul, Pinyin e tons, …)
  <romanização>.py    # pronúncia escrita (romanize.py no coreano, pinyin.py no chinês)
  build_<idioma>.py   # gera public/<idioma>.html com practice.build.build_app(PAGE, data, out)
```

`PAGE` traz os textos da interface: `code, html_lang, brand, brand_word, name, alphabet_tab, eyebrow, headline, intro, level_prefix, typing_label, typing_hint, lang_js, alphabet_html`. `data` traz `questions, modules, guide, roman, skills` e o que o `alphabet()` do idioma usar.

Questão: `{id, module, level (1|2), theme, prompt, text (com ___), answers[0] = exibida (as demais são aceitas ao digitar), distractors, explanation, audio, roman, slots?}`. Com várias lacunas, `slots = [{answers, distractors, label}]`.

## 3. Esquema de conteúdo das habilidades

```python
TEXTS = [{
  "id": "zr001", "level": "HSK 1", "topic": "apresentação", "title": "Título em português",
  "text": "Parágrafo 1\n\nParágrafo 2",          # no idioma
  "translation": "Tradução\n\nmesmos parágrafos",  # opcional, mesma contagem de parágrafos
  "questions": [{"question": "…?", "options": ["certa", "…", "…", "…"], "answer": 0, "why": "trecho que justifica"}],
}]
PROMPTS = [{"id": "zw01", "level": "HSK 1", "topic": "…", "prompt": "no idioma", "prompt_pt": "em português",
            "units": 80, "lines": 4}]   # units = mínimo de palavras ou sílabas (conforme lang.unit)
ROLEPLAY = "1. … 2. … 3. …"             # perguntas da entrevista no idioma
```

`skills.build.skills_bundle(TEXTS, PROMPTS, ROLEPLAY, listen_choice, romanize)` valida tudo (IDs únicos, respostas válidas, parágrafos da tradução) e acrescenta a pronúncia (`roman`) por parágrafo quando o idioma tem função de romanização.

`listen_choice` = lista de `{"answer", "options", "explanation"}`: frases completas que diferem só num ponto (partícula, tempo, tom). Gere a partir do próprio banco de questões de uma lacuna.

## 4. Montagem no app

```js
const skills = RoutineSkills.mount({
  lang: { code: 'zh', name: 'mandarim', html: 'zh', tts: 'zh-CN', voice: /^zh/i, rate: 0.85,
          unit: 'syllables', unitLabel: 'caracteres', connectors: ['因为', '所以', '但是'] },
  data: KDATA.skills, roman: KDATA.roman,
  skills: () => (state.skills ??= { events: [] }), save, day: today,
  writingChecks: text => [/* dicas locais em HTML seguro */],
  tutorPrompt: (prompt, text) => '…pedido de correção em português para colar no chat…',
});
// nas abas: skills.pause(); em "Meu progresso": skills.renderHistory();
```

`unit`: `words` (alfabetos com espaço) ou `syllables` (hangul, kana, hanzi). A velocidade de leitura é gravada em `wpm` com `unit` ao lado.

## 5. Eventos gravados (`state.skills.events`)

- reading `{kind, ref, level, seconds, wpm, unit, score, total, reread}`
- writing `{kind, ref, level, text, words, lines, unique, unit}`
- listening `{kind, ref, level, score, total, transcript, title?}` (`ref: "ouca-e-escolha"` no treino rápido)
- speaking `{kind, ref, level, seconds, mode, notes, checks, intelligibility?, speechText?}`

Todos com `id`, `time`, `day`. O `cloud-sync` mescla por `id` entre aparelhos e respeita `resetAt`.

## 6. Checklist de um idioma novo

1. `_languages.js`: entrada com `available: false` e `speech` (o painel mostra “Em breve” e o botão **Testar** para o admin).
2. Pasta do idioma com `content.py`, `skills_content.py`, `lang.js`, `alphabet.html`, `build_<idioma>.py`.
3. Romanização/pronúncia (se não for alfabeto latino) com teste contra lista oficial.
4. Testes: conteúdo (`tests/<idioma>_content_test.py`), fala (`tests/speaking_language_test.mjs`).
5. Admin testa pelo botão **Testar** no painel.
6. Revisão por nativo/professor.
7. Lançar: `available: true`, landing/preços, portal Stripe com troca entre os pacotes.

## 7. Exemplos prontos

- Coreano: `korean/` (hangul, partículas pelo batchim, romanização revisada).
- Chinês: `chinese/` (tons, pinyin por dicionário, classificadores; ao digitar aceita caracteres ou pinyin com/sem tons).
- Espanhol: `spanish/` (alfabeto latino: questões marcam `typeable`; conjugação por regra + irregulares; falsos amigos para brasileiros; `levelNames` A1/A2).
- Japonês: `japanese/` (hiragana/katakana, leituras de kanji por dicionário, romaji Hepburn com partículas wa/e/o; ao digitar aceita kana ou romaji; `levelNames` N5/N4).

Dicas gerais:
- Idiomas de alfabeto latino não conseguem decidir pelo `script` o que é digitável: marque `typeable: true/false` em cada questão.
- `lang.levelNames` dá nome aos níveis (A1/A2, N5/N4); sem ele usa `levelPrefix + número` (TOPIK 1, HSK 2).
- `lang.cheer` e `lang.praise` são as frases de acerto/elogio no idioma.
- Teste de nível: `placement/bank_en.py` (inglês, CEFR). Para outro idioma, crie `bank_<lang>.py` e uma entrada em `PAGES` com os níveis (TOPIK, HSK…).
