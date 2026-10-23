import assert from 'node:assert/strict';
import { createHmac } from 'node:crypto';
import { onRequestPost } from '../functions/api/stripe-webhook.js';

const env = { SUPABASE_URL: 'https://example.supabase.co', SUPABASE_SECRET_KEY: 'sb_secret_test', STRIPE_WEBHOOK_SECRET: 'whsec_test' };
let profilePatch = null;
let currentLanguages = ['en', 'ko'];
globalThis.fetch = async (url, options = {}) => {
  url = String(url);
  if (url.includes('/rest/v1/subscriptions')) return Response.json([{}]);
  if (url.includes('/rest/v1/profiles')) {
    if (options.method === 'PATCH') { profilePatch = JSON.parse(options.body); return Response.json([profilePatch]); }
    return Response.json([{ id: 'u1', languages: currentLanguages }]);
  }
  throw new Error(`Unexpected ${url}`);
};

async function send(subscription) {
  const body = JSON.stringify({ type: 'customer.subscription.updated', data: { object: subscription } });
  const t = Math.floor(Date.now() / 1000);
  const sig = createHmac('sha256', env.STRIPE_WEBHOOK_SECRET).update(`${t}.${body}`).digest('hex');
  const request = new Request('https://app.test/api/stripe-webhook', { method: 'POST', headers: { 'Stripe-Signature': `t=${t},v1=${sig}` }, body });
  const response = await onRequestPost({ request, env });
  assert.equal(response.status, 200);
}
const sub = (lookup, metadata = {}) => ({ id: 'sub_1', customer: 'cus_1', status: 'active', metadata, items: { data: [{ price: { lookup_key: lookup }, current_period_end: 1 }] } });

await send(sub('routine_2_idiomas', { languages: 'en,ko' }));
assert.deepEqual(profilePatch, { subscription_status: 'active', plan_size: 2, languages: ['en', 'ko'] });

// Downgrade in the customer portal (no metadata): keep the first languages that fit.
await send(sub('english_routine_mensal'));
assert.deepEqual(profilePatch, { subscription_status: 'active', plan_size: 1, languages: ['en'] });

// Unknown price (e.g. the old archived one): only the status changes.
await send(sub(null));
assert.deepEqual(profilePatch, { subscription_status: 'active' });
console.log('webhook_languages_test: ok');
