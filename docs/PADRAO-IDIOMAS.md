# Padrão para novos idiomas (Routine)

Cada idioma é um app próprio no mesmo site (`/app.html` inglês, `/korean.html` coreano, …), com login, assinatura, sincronização e histórico compartilhados. Este documento é o checklist para criar o próximo (ex.: mandarim `zh`, japonês `ja`).

## 1. Peças comuns (não copiar, reutilizar)

| Peça | Onde | O que faz |
|---|---|---|
| Catálogo | `functions/api/_languages.js` | `name`, `brand`, `app`, `available`, `speech: {transcribe, tokens}` |
| Acesso | `functions/api/_shared.js` → `requireActive(env, user, lang)` | assinatura/cortesia/admin por idioma |
| Progresso | `/api/progress?lang=xx` + `public/assets/cloud-sync.js` | `window.ROUTINE_LANGUAGE = "xx"`, chave `routine-xx-v1` |
| Fala | `/api/speaking/evaluate` com `language: "xx"` | transcrição no idioma; shadowing por palavras ou sílabas |
| Habilidades | `skills/skills.js`, `skills/skills.css`, `skills/build.py` | Reading, Writing, Listening (texto + “Ouça e escolha”) e Speaking |
| Painel | `public/assets/dashboard.js` | “Em breve”, botão **Testar** para admin, **Treinar** quando `available` |

O inglês tem implementação própria das habilidades (anterior ao módulo) e grava **o mesmo esquema de eventos**, então históricos e relatórios ficam comparáveis.

## 2. Estrutura de um idioma

```
<idioma>/
  content.py          # banco de questões (gramática, vocabulário, …)
  skills_content.py   # TEXTS, PROMPTS, ROLEPLAY
  build_<idioma>.py   # gera public/<idioma>.html
  src/template.html   # abas Treinar · Reading · Writing · Listening · Speaking · … · Meu progresso
  src/styles.css      # variáveis de cor: --card --ink --muted --line --brand --accent --soft --good --good-soft --bad --bad-soft
  src/app.js          # treino de questões + RoutineSkills.mount(...)
```

O template precisa de `<section id="reading|writing|listening|speaking" role="tabpanel">` vazias, de `<div id="skillsHistory">` em “Meu progresso” e dos marcadores `{{GUARD}} {{STYLES}} {{SKILLS}} {{DATA}} {{APP}}`.

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

1. `_languages.js`: entrada com `available: false` e `speech`.
2. Pasta do idioma com `content.py`, `skills_content.py`, `build_<idioma>.py`, `src/`.
3. Romanização/pronúncia (se não for alfabeto latino) com teste contra lista oficial.
4. Testes: conteúdo (`tests/<idioma>_content_test.py`), fala (`tests/speaking_language_test.mjs`).
5. Admin testa pelo botão **Testar** no painel.
6. Revisão por nativo/professor.
7. Lançar: `available: true`, landing/preços, portal Stripe com troca entre os pacotes.
