import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const source = readFileSync(new URL('../public/assets/cloud-sync.js', import.meta.url), 'utf8');
const start = source.indexOf('  function mergeStates(');
const end = source.indexOf('\n\n  async function remoteState', start);
assert.ok(start >= 0 && end > start, 'mergeStates must remain extractable for this test');

const mergeStates = Function(`${source.slice(start, end)}; return mergeStates;`)();
const remoteAttempt = { qid: 'q1', time: '2026-10-14T10:00:00.000Z' };
const localAttempt = { qid: 'q2', time: '2026-10-14T10:01:00.000Z' };

const merged = mergeStates(
  { version: 1, attempts: [remoteAttempt], skills: { events: [], drafts: {}, accepted: [] } },
  { version: 1, attempts: [localAttempt], skills: { events: [], drafts: {}, accepted: [] } },
);
assert.deepEqual(merged.attempts, [remoteAttempt, localAttempt]);

const localWinsOverEmptyCloud = mergeStates(
  { version: 1, attempts: [], skills: { events: [], drafts: {}, accepted: [] } },
  { version: 1, attempts: [localAttempt], skills: { events: [], drafts: {}, accepted: [] } },
);
assert.equal(localWinsOverEmptyCloud.attempts.length, 1);
assert.equal(localWinsOverEmptyCloud.attempts[0].qid, 'q2');

assert.match(source, /setInterval\(\(\) =>/);
assert.match(source, /english-daily:state-saved/);
assert.match(readFileSync(new URL('../public/app.html', import.meta.url), 'utf8'), /cloud-sync\.js\?v=20261014-3/);

console.log('cloud_sync_test: ok');

// pagehide in app.html persists the pre-hydration in-memory state; it must not
// overwrite the cloud state written right before the hydration reload.
assert.match(source, /if \(hydrating && this === localStorage && key === KEY\) return;/);
assert.match(source, /function reloadAfterHydration\(\) \{\n    hydrating = true;/);
console.log('cloud_sync_test (hydration guard): ok');
