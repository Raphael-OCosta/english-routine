// Checks do TextLab (textos por gramática): node tests/textlab_test.mjs
import { createRequire } from 'node:module';
import assert from 'node:assert/strict';

const require = createRequire(import.meta.url);
const T = require('../textlab/engine.js');
const STORIES = require('../textlab/stories_en.js');

// morfologia
assert.equal(T.third('watch'), 'watches');
assert.equal(T.third('study'), 'studies');
assert.equal(T.third('play'), 'plays');
assert.equal(T.third('have'), 'has');
assert.equal(T.ing('make'), 'making');
assert.equal(T.ing('run'), 'running');
assert.equal(T.ing('see'), 'seeing');
assert.equal(T.past('plan'), 'planned');
assert.equal(T.past('carry'), 'carried');
assert.equal(T.past('take'), 'took');
assert.equal(T.participle('write'), 'written');
assert.equal(T.participle('feed'), 'fed');

const ALL = Object.keys(T.GRAMMAR);
const FORMS = ['aff', 'neg', 'q'];
let total = 0;
for (const story of STORIES) {
  assert.ok(story.events.length >= 10, story.id);
  assert.ok(story.pairs.length >= 4, story.id);
  for (const g of ALL) {
    for (let seed = 1; seed <= 6; seed++) {
      const r = T.generate(story, { grammar: [g], forms: FORMS, sentences: 12, seed, connectors: seed % 2 === 0 });
      assert.ok(r.sentences.length >= 3, `${story.id}/${g}: poucas frases`);
      for (const s of r.sentences) {
        const text = T.plainText(s);
        total++;
        assert.equal(s.g, g, `${story.id}/${g}: estrutura trocada`);
        assert.ok(/^[A-Z"]/.test(text), `${story.id}/${g}: começa minúscula: ${text}`);
        assert.ok(/[.?]$/.test(text), `${story.id}/${g}: sem pontuação final: ${text}`);
        assert.ok(!/undefined|null|\s{2,}| ,| \./.test(text), `${story.id}/${g}: texto quebrado: ${text}`);
        assert.ok(s.seg.some(x => x.g), `${story.id}/${g}: sem trecho-alvo: ${text}`);
        if (s.f === 'q') assert.ok(text.includes('?'), text);
        // cada resposta (id) fica numa frase só e todas as partes têm o verbo base
        const ids = new Set(s.seg.filter(x => x.g).map(x => x.id));
        assert.ok(ids.size <= 2, text);
        s.seg.filter(x => x.g).forEach(x => assert.ok(x.base, text));
      }
    }
  }
}
// combinações: todas as estruturas marcadas aparecem (com tema suficiente)
const mix = T.generate(STORIES[0], { grammar: ['pp', 'should', 'passive', 'cond1'], forms: FORMS, sentences: 12, seed: 7, connectors: true });
assert.deepEqual(new Set(mix.sentences.map(s => s.g)), new Set(['pp', 'should', 'passive', 'cond1']));
// mesma semente → mesmo texto (o link compartilhado reabre o mesmo texto)
const a = T.generate(STORIES[3], { grammar: ['past', 'might'], forms: FORMS, sentences: 9, seed: 99, connectors: true });
const b = T.generate(STORIES[3], { grammar: ['past', 'might'], forms: FORMS, sentences: 9, seed: 99, connectors: true });
assert.equal(a.sentences.map(T.plainText).join(' '), b.sentences.map(T.plainText).join(' '));
// formas equilibradas por estrutura
const forms = T.generate(STORIES[1], { grammar: ['ps', 'pc'], forms: ['aff', 'neg'], sentences: 12, seed: 3 });
for (const g of ['ps', 'pc']) assert.equal(new Set(forms.sentences.filter(s => s.g === g).map(s => s.f)).size, 2, g);

console.log(`textlab ok: ${total} frases verificadas`);
