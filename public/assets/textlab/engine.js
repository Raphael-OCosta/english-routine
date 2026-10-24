/* TextLab — textos em inglês construídos a partir de estruturas gramaticais escolhidas.
 *
 * Cada tema é uma história curta (personagens + eventos). Cada evento é renderizado na
 * estrutura pedida (tempo verbal, modal, voz passiva, condicional…) e na forma escolhida
 * (afirmativa, negativa, pergunta). O resultado é uma lista de frases em segmentos:
 *   { t: 'texto' }                       texto comum
 *   { t: 'is taking', g: 'pc', id: 3 }   trecho-alvo (destaque, lacuna e gabarito)
 * Funciona no navegador (window.TextLab) e no Node (module.exports) para testes.
 */
(function (root) {
  'use strict';

  // ------------------------------------------------------------ morfologia
  const IRREGULAR = {
    be: ['was', 'been'], bring: ['brought', 'brought'], build: ['built', 'built'], buy: ['bought', 'bought'], catch: ['caught', 'caught'],
    choose: ['chose', 'chosen'], come: ['came', 'come'], cut: ['cut', 'cut'], do: ['did', 'done'], draw: ['drew', 'drawn'], drink: ['drank', 'drunk'],
    drive: ['drove', 'driven'], eat: ['ate', 'eaten'], feel: ['felt', 'felt'], find: ['found', 'found'], fly: ['flew', 'flown'], forget: ['forgot', 'forgotten'],
    give: ['gave', 'given'], go: ['went', 'gone'], grow: ['grew', 'grown'], have: ['had', 'had'], hear: ['heard', 'heard'], keep: ['kept', 'kept'],
    know: ['knew', 'known'], leave: ['left', 'left'], lend: ['lent', 'lent'], lose: ['lost', 'lost'], make: ['made', 'made'], meet: ['met', 'met'],
    pay: ['paid', 'paid'], put: ['put', 'put'], read: ['read', 'read'], ride: ['rode', 'ridden'], run: ['ran', 'run'], say: ['said', 'said'],
    see: ['saw', 'seen'], sell: ['sold', 'sold'], send: ['sent', 'sent'], set: ['set', 'set'], sing: ['sang', 'sung'], sit: ['sat', 'sat'],
    sleep: ['slept', 'slept'], speak: ['spoke', 'spoken'], spend: ['spent', 'spent'], stand: ['stood', 'stood'], swim: ['swam', 'swum'],
    take: ['took', 'taken'], teach: ['taught', 'taught'], tell: ['told', 'told'], think: ['thought', 'thought'], throw: ['threw', 'thrown'],
    understand: ['understood', 'understood'], wake: ['woke', 'woken'], wear: ['wore', 'worn'], win: ['won', 'won'], write: ['wrote', 'written'],
    hang: ['hung', 'hung'], feed: ['fed', 'fed'], blow: ['blew', 'blown'], get: ['got', 'gotten'], fall: ['fell', 'fallen'], break: ['broke', 'broken'], hide: ['hid', 'hidden'],
  };
  const DOUBLE = new Set(['stop', 'plan', 'shop', 'run', 'swim', 'sit', 'chat', 'jog', 'drop', 'begin', 'put', 'cut', 'set', 'get', 'prefer', 'admit', 'win', 'plug', 'hug', 'clap']);
  const VOWEL = /[aeiou]/;

  function split(lemma) {
    const [head, ...rest] = lemma.split(' ');
    return { head, tail: rest.length ? ' ' + rest.join(' ') : '' };
  }
  function third(v) {
    if (v === 'have') return 'has';
    if (v === 'be') return 'is';
    if (v === 'do' || v === 'go') return v + 'es';
    if (/[^aeiou]y$/.test(v)) return v.slice(0, -1) + 'ies';
    if (/(s|x|z|ch|sh|o)$/.test(v)) return v + 'es';
    return v + 's';
  }
  function ing(v) {
    if (v === 'be') return 'being';
    if (v.endsWith('ie')) return v.slice(0, -2) + 'ying';
    if (v.endsWith('e') && !/(ee|ye|oe)$/.test(v)) return v.slice(0, -1) + 'ing';
    if (DOUBLE.has(v)) return v + v.at(-1) + 'ing';
    return v + 'ing';
  }
  function regularPast(v) {
    if (v.endsWith('e')) return v + 'd';
    if (/[^aeiou]y$/.test(v)) return v.slice(0, -1) + 'ied';
    if (DOUBLE.has(v)) return v + v.at(-1) + 'ed';
    return v + 'ed';
  }
  const past = v => (IRREGULAR[v] ? IRREGULAR[v][0] : regularPast(v));
  const participle = v => (IRREGULAR[v] ? IRREGULAR[v][1] : regularPast(v));

  // Formas de um lema com partícula ("wake up" → "wakes up").
  const form = (lemma, fn) => { const { head, tail } = split(lemma); return fn(head) + tail; };

  // ------------------------------------------------------------ sujeito
  // person: '1s' (I), '3s' (he/she/it, nomes), 'pl' (they, we, grupos)
  const BE = { present: { '1s': 'am', '3s': 'is', pl: 'are' }, past: { '1s': 'was', '3s': 'was', pl: 'were' } };
  const NEG_BE = { am: "am not", is: "isn't", are: "aren't", was: "wasn't", were: "weren't" };
  const doAux = p => (p === '3s' ? 'does' : 'do');
  const haveAux = p => (p === '3s' ? 'has' : 'have');
  const cap = s => s.charAt(0).toUpperCase() + s.slice(1);

  // ------------------------------------------------------------ estruturas
  // label: nome mostrado; group: agrupamento na interface; lead: marcadores de tempo opcionais.
  const GRAMMAR = {
    ps: { label: 'Simple present', group: 'Tempos verbais', lead: ['Every morning,', 'On weekdays,', 'Most days,', 'Every week,'] },
    pc: { label: 'Present continuous', group: 'Tempos verbais', lead: ['Right now,', 'At the moment,', 'Today,', 'This week,'] },
    past: { label: 'Simple past', group: 'Tempos verbais', lead: ['Yesterday,', 'Last Monday,', 'Last week,', 'Two days ago,'] },
    pastc: { label: 'Past continuous', group: 'Tempos verbais', lead: ['At eight o\'clock yesterday,', 'At that moment,', 'While it was raining,', 'All afternoon,'] },
    pp: { label: 'Present perfect', group: 'Tempos verbais', lead: ['This year,', 'So far,', 'This week,', ''] },
    pastp: { label: 'Past perfect', group: 'Tempos verbais', lead: ['By ten o\'clock,', 'Before lunch,', 'By then,', 'By the end of the day,'] },
    will: { label: 'Future · will', group: 'Tempos verbais', lead: ['Tomorrow,', 'Next week,', 'Soon,', 'Later,'] },
    going: { label: 'Future · going to', group: 'Tempos verbais', lead: ['This weekend,', 'Next month,', 'Tonight,', 'On Friday,'] },
    usedto: { label: 'Used to', group: 'Tempos verbais', lead: ['Years ago,', 'In the past,', 'Back then,', 'A long time ago,'] },
    can: { label: 'Modais · can / could (habilidade)', group: 'Verbos modais', lead: ['Now', '', '', ''] },
    should: { label: 'Modais · should / must / have to', group: 'Verbos modais', lead: ['', '', '', ''] },
    might: { label: 'Modais · may / might (possibilidade)', group: 'Verbos modais', lead: ['Tomorrow,', 'Later,', 'Next week,', ''] },
    passive: { label: 'Voz passiva', group: 'Estruturas', lead: ['Every day,', 'Yesterday,', 'Usually,', 'Last week,'] },
    cond1: { label: 'First conditional', group: 'Estruturas', lead: [] },
    cond2: { label: 'Second conditional', group: 'Estruturas', lead: [] },
  };
  const FORMS = { aff: 'Afirmativas', neg: 'Negativas', q: 'Perguntas' };
  // Estruturas que não ficam naturais em negativa/pergunta no gerador.
  const ONLY_AFF = new Set(['cond1', 'cond2']);

  function maker() {
    let id = 0;
    return g => (t => ({ t, g, id: ++id }));
  }

  // Renderiza um evento. ctx: { who, rng, gid, connector }
  function render(ev, g, f, ctx) {
    const S = ctx.who(ev.s);
    const p = S.person;
    const v = ev.v;
    const obj = ev.o ? ' ' + ev.o : '';
    const rest = ev.r ? ' ' + ev.r : '';
    const seg = [];
    const plain = t => seg.push({ t });
    // Todas as partes da estrutura numa frase (ex.: "Does … take") formam uma só resposta.
    let gid = null;
    const target = (...parts) => { gid ??= ctx.nextId(); parts.forEach(t => seg.push({ t, g, id: gid, base: ev.v })); };
    const lead = () => {
      const options = (GRAMMAR[g].lead || []).filter(Boolean);
      if (!options.length || ctx.rng() < 0.45) return '';
      return options[Math.floor(ctx.rng() * options.length)] + ' ';
    };
    const ans = aux => ` Yes, ${S.pron} ${aux}.`;

    if (g === 'passive') {
      if (!ev.pass) return null;
      const pastTense = ctx.rng() < 0.5;
      const subj = ev.pass;
      const sp = ev.passPl ? 'pl' : '3s';
      const be = BE[pastTense ? 'past' : 'present'][sp];
      const ld = pastTense ? ['Yesterday, ', 'Last week, ', ''][Math.floor(ctx.rng() * 3)] : ['Every day, ', 'Usually, ', ''][Math.floor(ctx.rng() * 3)];
      const by = ` by ${S.full}`;
      if (f === 'q') { plain(''); target(cap(be)); plain(` ${subj} `); target(form(v, participle)); plain(`${by}${rest}?${` Yes, ${sp === 'pl' ? 'they' : 'it'} ${be}.`}`); }
      else if (f === 'neg') { plain(ld ? ld + subj + ' ' : cap(subj) + ' '); target(NEG_BE[be] + ' ' + form(v, participle)); plain(`${by}${rest}.`); }
      else { plain(ld ? ld + subj + ' ' : cap(subj) + ' '); target(be + ' ' + form(v, participle)); plain(`${by}${rest}.`); }
      return seg;
    }

    if (g === 'cond1' || g === 'cond2') {
      const next = ev.next;
      if (!next) return null;
      const S2 = ctx.who(next.s, true, ev.s);
      const ifVerb = g === 'cond1'
        ? (p === '3s' ? form(v, third) : v === 'be' ? BE.present[p] : v)
        : (v === 'be' ? 'were' : form(v, past));
      const main = (g === 'cond1' ? 'will ' : 'would ') + next.v;
      plain(`If ${S.subj} `); target(ifVerb); plain(`${obj}${rest}, ${S2.subj} `);
      { const nid = ctx.nextId(); seg.push({ t: main, g, id: nid, base: next.v }); }
      plain(`${next.o ? ' ' + next.o : ''}${next.r ? ' ' + next.r : ''}.`);
      return seg;
    }

    const L = f === 'aff' || f === 'neg' ? lead() : '';
    const subjFirst = L ? `${L}${S.subj}` : cap(S.subj);
    const qLead = f === 'q' && g === 'pastp' ? (GRAMMAR.pastp.lead[Math.floor(ctx.rng() * 4)] + ' ') : '';
    const say = (aux, verbForm, negAux) => {
      if (f === 'q') {
        plain(qLead); target(qLead ? aux : cap(aux)); plain(` ${S.full} `); target(verbForm); plain(`${obj}${rest}?${ans(aux.split(' ')[0])}`);
      } else if (f === 'neg') {
        plain(subjFirst + ' '); target(`${negAux} ${verbForm}`); plain(`${obj}${rest}.`);
      } else {
        plain(subjFirst + ' '); target(aux ? `${aux} ${verbForm}` : verbForm); plain(`${obj}${rest}.`);
      }
    };

    switch (g) {
      case 'ps': {
        if (f === 'aff') {
          const adv = L ? '' : ['usually ', 'often ', 'always ', 'sometimes ', ''][Math.floor(ctx.rng() * 5)];
          const vf = p === '3s' ? form(v, third) : v;
          plain(subjFirst + ' ' + adv); target(vf); plain(`${obj}${rest}.`);
          return seg;
        }
        const aux = doAux(p);
        say(aux, v, aux === 'does' ? "doesn't" : "don't");
        return seg;
      }
      case 'pc': { const be = BE.present[p]; say(be, form(v, ing), NEG_BE[be]); return seg; }
      case 'past': {
        if (f === 'aff') { plain(subjFirst + ' '); target(form(v, past)); plain(`${obj}${rest}.`); return seg; }
        say('did', v, "didn't");
        return seg;
      }
      case 'pastc': { const be = BE.past[p]; say(be, form(v, ing), NEG_BE[be]); return seg; }
      case 'pp': {
        const have = haveAux(p);
        if (f === 'aff') { const adv = ['already ', 'just ', ''][Math.floor(ctx.rng() * 3)]; plain(subjFirst + ' '); target(`${have} ${adv}${form(v, participle)}`); plain(`${obj}${rest}.`); return seg; }
        if (f === 'neg') { plain(subjFirst + ' '); target(`${have === 'has' ? "hasn't" : "haven't"} ${form(v, participle)}`); plain(`${obj}${rest} yet.`); return seg; }
        plain(''); target(cap(have)); plain(` ${S.full} `); target(form(v, participle)); plain(`${obj}${rest} yet?${ans(have)}`);
        return seg;
      }
      case 'pastp': { say('had', form(v, participle), "hadn't"); return seg; }
      case 'will': { say('will', v, "won't"); return seg; }
      case 'going': {
        const be = BE.present[p];
        if (f === 'q') { plain(''); target(cap(be)); plain(` ${S.full} `); target(`going to ${v}`); plain(`${obj}${rest}?${ans(be)}`); return seg; }
        plain(subjFirst + ' '); target(`${f === 'neg' ? NEG_BE[be] : be} going to ${v}`); plain(`${obj}${rest}.`);
        return seg;
      }
      case 'usedto': {
        if (f === 'q') { plain(''); target('Did'); plain(` ${S.full} `); target(`use to ${v}`); plain(`${obj}${rest}?${ans('did')}`); return seg; }
        plain(subjFirst + ' '); target(f === 'neg' ? `didn't use to ${v}` : `used to ${v}`); plain(`${obj}${rest}.`);
        return seg;
      }
      case 'can': {
        const could = ctx.rng() < 0.35;
        if (could && f !== 'q') {
          plain(`When ${S.full} ${p === 'pl' ? 'were' : 'was'} younger, ${S.pron} `);
          target(f === 'neg' ? `couldn't ${v}` : `could ${v}`); plain(`${obj}${rest}.`);
          return seg;
        }
        say('can', v, "can't");
        return seg;
      }
      case 'should': {
        const pick = Math.floor(ctx.rng() * 3);
        if (pick === 0) { say('should', v, "shouldn't"); return seg; }
        if (pick === 1 && f !== 'q') { plain(subjFirst + ' '); target(f === 'neg' ? `mustn't ${v}` : `must ${v}`); plain(`${obj}${rest}.`); return seg; }
        const has = p === '3s' ? 'has' : 'have';
        if (f === 'q') { plain(''); target(cap(doAux(p))); plain(` ${S.full} `); target(`have to ${v}`); plain(`${obj}${rest}?${ans(doAux(p))}`); return seg; }
        plain(subjFirst + ' '); target(f === 'neg' ? `${doAux(p) === 'does' ? "doesn't" : "don't"} have to ${v}` : `${has} to ${v}`); plain(`${obj}${rest}.`);
        return seg;
      }
      case 'might': {
        const m = ctx.rng() < 0.5 ? 'might' : 'may';
        if (f === 'q') { plain(''); target('Could'); plain(` ${S.full} `); target(v); plain(`${obj}${rest}?${ans('could')}`); return seg; }
        plain(subjFirst + ' '); target(f === 'neg' ? `${m} not ${v}` : `${m} ${v}`); plain(`${obj}${rest}.`);
        return seg;
      }
      default: return null;
    }
  }

  // ------------------------------------------------------------ gerador
  function rng(seed) {
    let a = seed >>> 0;
    return () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  }

  /* opts: { story, grammar: ['ps','might'], forms: ['aff','neg'], sentences: 12, seed, connectors: bool } */
  function generate(story, opts) {
    const R = rng(opts.seed || 1);
    const grammar = opts.grammar.length ? opts.grammar : ['ps'];
    const forms = opts.forms?.length ? opts.forms : ['aff'];
    const people = story.people;
    const mentioned = new Set();
    let lastSubject = null;
    let id = 0;
    let events = [...story.events];
    // Começa em um ponto aleatório da história e segue em ordem (circular).
    const start = Math.floor(R() * events.length);
    events = [...events.slice(start), ...events.slice(0, start)];
    let i = 0;

    function who(key, inResult = false, prevKey = null) {
      const person = people[key];
      const usePron = (inResult && prevKey === key) || (mentioned.has(key) && lastSubject === key);
      mentioned.add(key);
      lastSubject = key;
      return { subj: usePron ? person.pron : person.name, pron: person.pron, full: person.name, person: person.person };
    }
    const ctx = { rng: R, who, nextId: () => ++id };
    // Condicionais usam pares causa → consequência escritos para cada tema.
    const pairs = (story.pairs || []).map(([a, b]) => ({ ...a, next: b }));
    let pi = 0;
    // Formas em rodízio por estrutura (a partir de um ponto sorteado): equilibra afirmativas, negativas e perguntas.
    const formTurn = {};

    const sentences = [];
    let guard = 0;
    let gi = 0;
    while (sentences.length < opts.sentences && i < events.length && guard++ < opts.sentences * 6) {
      const ev = events[i];
      // Distribui as estruturas em rodízio; se uma não serve para o evento, tenta as outras.
      let out = null;
      let used = null;
      let usedEvent = false;
      for (let k = 0; k < grammar.length && !out; k++) {
        const g = grammar[(gi + k) % grammar.length];
        const cond = ONLY_AFF.has(g);
        if (cond && pi >= pairs.length) continue;
        formTurn[g] ??= Math.floor(R() * forms.length);
        const f = cond ? 'aff' : forms[formTurn[g] % forms.length];
        const before = id;
        out = render(cond ? pairs[pi] : ev, g, f, ctx);
        if (!out) { id = before; continue; }
        used = { g, f };
        if (cond) pi++;
        else { usedEvent = true; formTurn[g]++; }
      }
      if (usedEvent || !out) i++;
      if (!out) continue;
      gi++;
      sentences.push({ seg: out, g: used.g, f: used.f });
    }
    // lc: a frase abre com um grupo ou objeto que só ganhou maiúscula por estar no início ("The kids…").
    const lowerStarts = [...Object.values(people).map(x => x.name), ...story.events.map(e => e.o)]
      .filter(x => x && x[0] !== x[0].toUpperCase()).map(x => x[0].toUpperCase() + x.slice(1));
    sentences.forEach(s => { const t = s.seg[0]?.t || ''; s.lc = lowerStarts.some(x => t.startsWith(x)); });
    if (opts.connectors) addConnectors(sentences, R);
    return { title: story.title, sentences, paragraphs: paragraphs(sentences) };
  }

  const LINKS = ['Then', 'After that,', 'Later,', 'Also,', 'Meanwhile,'];
  function addConnectors(sentences, R) {
    sentences.forEach((s, n) => {
      if (n === 0 || n % 3 !== 1 || s.f === 'q' || /^(If|When)/.test(s.seg[0].t)) return;
      const first = s.seg[0];
      if (!first.t || first.g) return;
      if (/^(Every|On|Most|Right|At|Today|This|Yesterday|Last|Two|While|All|So|By|Before|Tomorrow|Next|Soon|Later|Tonight|Years|In|Back|A long|Now|Usually)\b/.test(first.t)) return;
      const link = LINKS[Math.floor(R() * LINKS.length)];
      const lower = s.lc;
      first.t = `${link} ${lower ? first.t.charAt(0).toLowerCase() + first.t.slice(1) : first.t}`;
    });
  }

  function paragraphs(sentences) {
    const out = [];
    for (let n = 0; n < sentences.length; n += 4) out.push(sentences.slice(n, n + 4));
    return out;
  }

  // Texto puro de uma frase (para copiar).
  const plainText = s => s.seg.map(x => x.t).join('');

  // Lacunas: cada trecho-alvo vira uma lacuna; a dica mostra o verbo base (e o modal, quando há).
  function gaps(result) {
    const key = [];
    const groups = new Map();
    result.sentences.forEach(s => s.seg.forEach(x => {
      if (!x.g) return;
      if (!groups.has(x.id)) { groups.set(x.id, { n: groups.size + 1, parts: [], g: x.g }); key.push(groups.get(x.id)); }
      groups.get(x.id).parts.push(x.t);
    }));
    return { key, groups };
  }

  const api = { GRAMMAR, FORMS, generate, gaps, plainText, third, ing, past, participle, render, rng };
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.TextLab = api;
})(typeof window !== 'undefined' ? window : globalThis);
