// Checks do public/assets/tts-fix.js com uma voz simulada: node tests/tts_fix_test.mjs
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const source = readFileSync(new URL('../public/assets/tts-fix.js', import.meta.url), 'utf8');

function setup() {
  const spoken = [];
  const listeners = {};
  const body = { children: [], append(el) { this.children.push(el); } };
  class Utterance {
    constructor(text) { this.text = text; this.volume = 1; this.events = {}; }
    addEventListener(type, fn) { (this.events[type] ??= []).push(fn); }
    fire(type, extra = {}) { (this.events[type] || []).forEach(fn => fn({ type, ...extra })); }
  }
  const synth = { paused: false, speaking: false, speak(u) { spoken.push(u); }, cancel() { spoken.push('cancel'); }, resume() { this.paused = false; } };
  const timers = [];
  const ctx = {
    window: { speechSynthesis: synth }, SpeechSynthesisUtterance: Utterance,
    addEventListener: (type, fn) => { (listeners[type] ??= []).push(fn); },
    setTimeout: (fn, ms) => timers.push({ fn, ms }),
    Date, WeakSet, String,
    document: { body, createElement: () => ({ style: {}, setAttribute() {}, set innerHTML(v) { this.html = v; }, querySelector: () => ({}), remove() {} }) },
  };
  vm.runInNewContext(source, ctx);
  const runTimers = () => { while (timers.length) timers.shift().fn(); };
  return { synth, spoken, listeners, Utterance, body, runTimers, timers };
}

// 1) primeiro toque destrava a voz com uma fala muda (iPhone)
{
  const t = setup();
  t.listeners.pointerdown[0]();
  assert.equal(t.spoken.length, 1);
  assert.equal(t.spoken[0].volume, 0);
  t.listeners.click[0]();
  assert.equal(t.spoken.length, 1, 'destrava uma vez só');
}
// 2) speak logo depois de cancel espera um instante (Android)
{
  const t = setup();
  const u = new t.Utterance('안녕하세요');
  t.synth.cancel();
  t.synth.speak(u);
  assert.deepEqual(t.spoken, ['cancel'], 'não fala no mesmo instante do cancel');
  assert.equal(t.timers.find(x => x.ms === 150) !== undefined, true);
  t.timers.filter(x => x.ms === 150).forEach(x => x.fn());
  assert.equal(t.spoken.at(-1), u);
}
// 3) sem cancel recente, fala na hora
{
  const t = setup();
  const u = new t.Utterance('Hello');
  t.synth.speak(u);
  assert.equal(t.spoken[0], u);
}
// 4) voz que não começa mostra o aviso; fala cancelada não mostra
{
  const t = setup();
  t.synth.speak(new t.Utterance('Hallo'));
  t.runTimers();
  assert.equal(t.body.children.length, 1, 'aviso mostrado');
  const t2 = setup();
  const u = new t2.Utterance('Ciao');
  t2.synth.speak(u);
  u.fire('start');
  t2.runTimers();
  assert.equal(t2.body.children.length, 0, 'tocou: sem aviso');
  const t3 = setup();
  t3.synth.speak(new t3.Utterance('Bonjour'));
  t3.synth.cancel();
  t3.runTimers();
  assert.equal(t3.body.children.length, 0, 'cancelada: sem aviso');
}
console.log('tts-fix ok');
