import assert from 'node:assert/strict';
import { accessFor } from '../functions/api/_shared.js';
import { onRequestPost, onRequestGet } from '../functions/api/admin/grants.js';

const env = { SUPABASE_URL: 'https://example.supabase.co', SUPABASE_SECRET_KEY: 'sb_secret_test' };
const future = new Date(Date.now() + 86400000).toISOString();
const past = new Date(Date.now() - 86400000).toISOString();
let grantRows = [];
let role = 'student';
let posted = null;

globalThis.fetch = async (url, options = {}) => {
  url = String(url);
  if (url.endsWith('/auth/v1/user')) return Response.json({ id: 'u1', email: 'Amigo@Example.com' });
  if (url.includes('/rest/v1/profiles')) return Response.json([{ role }]);
  if (url.includes('/rest/v1/complimentary_grants')) {
    if (options.method === 'POST') {
      posted = JSON.parse(options.body);
      return Response.json([posted]);
    }
    return Response.json(grantRows);
  }
  throw new Error(`Unexpected URL: ${url}`);
};

const user = { id: 'u1', email: 'Amigo@Example.com' };
assert.deepEqual(await accessFor(env, user, { role: 'admin' }), { active: true, source: 'admin', expires_at: null, languages: ['en', 'ko'], plan_size: 3 });
const sub = await accessFor(env, user, { subscription_status: 'active', plan_size: 2, languages: ['en', 'ko', 'xx'] });
assert.deepEqual(sub.languages, ['en', 'ko']);
assert.equal(sub.plan_size, 2);
assert.deepEqual((await accessFor(env, user, { subscription_status: 'active', plan_size: 1, languages: ['ko', 'en'] })).languages, ['ko']);
assert.equal((await accessFor(env, user, { subscription_status: 'active' })).source, 'subscription');
assert.equal((await accessFor(env, user, { subscription_status: 'inactive' })).active, false);
grantRows = [{ expires_at: null }];
assert.equal((await accessFor(env, user, { subscription_status: 'inactive' })).source, 'gift');
grantRows = [{ expires_at: future }];
assert.equal((await accessFor(env, user, { subscription_status: 'canceled' })).active, true);
grantRows = [{ expires_at: past }];
assert.equal((await accessFor(env, user, { subscription_status: 'canceled' })).active, false);

const headers = { Authorization: 'Bearer t', 'Content-Type': 'application/json' };
const body = JSON.stringify({ email: ' Novo@Example.com ', note: 'presente' });
role = 'student';
assert.equal((await onRequestPost({ request: new Request('https://app.test/api/admin/grants', { method: 'POST', headers, body }), env })).status, 403);
assert.equal((await onRequestGet({ request: new Request('https://app.test/api/admin/grants', { headers }), env })).status, 403);
role = 'admin';
grantRows = [];
const ok = await onRequestPost({ request: new Request('https://app.test/api/admin/grants', { method: 'POST', headers, body }), env });
assert.equal(ok.status, 200);
assert.equal(posted.email, 'novo@example.com');
assert.equal(posted.expires_at, null);
assert.equal(posted.granted_by, 'u1');
const bad = await onRequestPost({ request: new Request('https://app.test/api/admin/grants', { method: 'POST', headers, body: JSON.stringify({ email: 'x@y.com', expires_at: '2020-01-01' }) }), env });
assert.equal(bad.status, 400);

console.log('access_test: ok');
