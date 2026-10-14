import assert from 'node:assert/strict';
import { onRequestGet, onRequestPut } from '../functions/api/progress.js';

const userId = '11111111-1111-4111-8111-111111111111';
const env = {
  SUPABASE_URL: 'https://example.supabase.co',
  SUPABASE_PUBLISHABLE_KEY: 'sb_publishable_test',
  SUPABASE_SECRET_KEY: 'sb_secret_test',
};
const saved = { version: 1, attempts: [{ qid: 'q1', time: '2026-10-14T10:00:00.000Z' }] };
let writtenBody = null;

globalThis.fetch = async (url, options = {}) => {
  if (String(url).endsWith('/auth/v1/user')) {
    return Response.json({ id: userId, email: 'teste@example.com' });
  }
  if (String(url).includes('/rest/v1/progress_snapshots')) {
    if ((options.method || 'GET') === 'POST') {
      writtenBody = JSON.parse(options.body);
      return Response.json([{ state: writtenBody.state }]);
    }
    return Response.json([{ state: saved }]);
  }
  throw new Error(`Unexpected URL: ${url}`);
};

const headers = { Authorization: 'Bearer access-token' };
const getResponse = await onRequestGet({ request: new Request('https://app.test/api/progress', { headers }), env });
assert.equal(getResponse.status, 200);
assert.equal(getResponse.headers.get('Cache-Control'), 'private, no-store');
assert.deepEqual((await getResponse.json()).state, saved);

const putResponse = await onRequestPut({
  request: new Request('https://app.test/api/progress', {
    method: 'PUT',
    headers: { ...headers, 'Content-Type': 'application/json' },
    body: JSON.stringify({ state: saved }),
  }),
  env,
});
assert.equal(putResponse.status, 200);
assert.equal(writtenBody.user_id, userId);
assert.deepEqual((await putResponse.json()).state, saved);

console.log('progress_api_test: ok');
