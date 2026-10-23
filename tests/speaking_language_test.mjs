import assert from 'node:assert/strict';
import { onRequestPost } from '../functions/api/speaking/evaluate.js';

// A avaliação de fala usa o idioma pedido: transcrição em coreano e shadowing
// comparado por sílabas (o coreano não separa palavras como o inglês).
const env = {
  SUPABASE_URL: 'https://example.supabase.co',
  SUPABASE_PUBLISHABLE_KEY: 'sb_publishable_test',
  SUPABASE_SECRET_KEY: 'sb_secret_test',
  OPENAI_API_KEY: 'test-key',
};
let transcribeLanguage = null;
let spoken = '';
globalThis.fetch = async (url, options = {}) => {
  url = String(url);
  if (url.endsWith('/auth/v1/user')) return Response.json({ id: 'u1', email: 'admin@example.com' });
  if (url.includes('/rest/v1/profiles')) return Response.json([{ role: 'admin', subscription_status: 'inactive', languages: [], plan_size: 0 }]);
  if (url.includes('/rest/v1/complimentary_grants')) return Response.json([]);
  if (url.includes('/rest/v1/ai_daily_usage')) return Response.json((options.method || 'GET') === 'POST' ? [{ calls: 1 }] : []);
  if (url.includes('api.openai.com')) {
    transcribeLanguage = options.body.get('language');
    return Response.json({ text: spoken });
  }
  throw new Error(`Unexpected URL: ${url}`);
};

const audio = Buffer.from('x'.repeat(2000)).toString('base64');
const call = body => onRequestPost({
  request: new Request('https://app.test/api/speaking/evaluate', {
    method: 'POST', headers: { Authorization: 'Bearer t', 'Content-Type': 'application/json' },
    body: JSON.stringify({ audio, mimeType: 'audio/webm', mode: 'shadow', ...body }),
  }),
  env,
});

spoken = '저는 매일 커피를 마셔요';
let res = await call({ reference: '저는 매일 커피를 마셔요.', language: 'ko' });
let data = await res.json();
assert.equal(res.status, 200, JSON.stringify(data));
assert.equal(transcribeLanguage, 'ko');
assert.equal(data.score, 100);

spoken = '저는 매일 커피 마셔요';
res = await call({ reference: '저는 매일 커피를 마셔요.', language: 'ko' });
data = await res.json();
assert.ok(data.score >= 80 && data.score < 100, data.score);

spoken = 'I work from home';
res = await call({ reference: 'I work from home.' });
data = await res.json();
assert.equal(transcribeLanguage, 'en');
assert.equal(data.score, 100);

res = await call({ reference: 'x', language: 'xx' });
assert.equal(res.status, 400);

console.log('speaking_language_test: ok');
