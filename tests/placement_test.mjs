import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

// Simula alunos de cada nível respondendo ao teste adaptativo e confere se o
// nível estimado cai no lugar certo (ou no vizinho) na grande maioria das vezes.
globalThis.window = globalThis;
const html = readFileSync(new URL('../public/nivelamento.html', import.meta.url), 'utf8');
eval(readFileSync(new URL('../placement/placement.js', import.meta.url), 'utf8'));
const config = JSON.parse(html.match(/const PLACEMENT = (\{.*\});/)[1]);

const codes = config.levels.map(l => l.code);
let exact = 0;
let near = 0;
let runs = 0;
for (const level of config.levels) {
  for (let r = 0; r < 60; r++) {
    const s = window.RoutinePlacement.createSession(config);
    const trueTheta = level.b + (Math.random() - 0.5) * 0.8;
    let q;
    let asked = 0;
    while ((q = s.next())) {
      asked++;
      s.answer(q, Math.random() < s.p(trueTheta, q) ? 0 : 1);
    }
    assert.equal(asked, 30);
    const got = s.levelFor(s.estimate().theta).code;
    const diff = Math.abs(codes.indexOf(got) - codes.indexOf(level.code));
    exact += diff === 0;
    near += diff <= 1;
    runs++;
  }
}
const types = (() => {
  const s = window.RoutinePlacement.createSession(config);
  let q;
  while ((q = s.next())) s.answer(q, 0);
  return s.answers.reduce((m, a) => ({ ...m, [a.q.type === 'vocab' ? 'grammar' : a.q.type]: (m[a.q.type === 'vocab' ? 'grammar' : a.q.type] || 0) + 1 }), {});
})();
assert.deepEqual(types, config.quota);
assert.ok(near / runs >= 0.9, `nível vizinho só em ${Math.round(near / runs * 100)}%`);
assert.ok(exact / runs >= 0.5, `nível exato só em ${Math.round(exact / runs * 100)}%`);
console.log(`placement_test: ok · exato ${Math.round(exact / runs * 100)}% · ±1 nível ${Math.round(near / runs * 100)}%`);
