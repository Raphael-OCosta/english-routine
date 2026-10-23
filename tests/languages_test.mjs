import assert from 'node:assert/strict';
import { onRequestPost as chooseLanguages } from '../functions/api/languages.js';
import { onRequestPost as checkout } from '../functions/api/create-checkout-session.js';
import { cleanLanguages, planSizeFromLookupKey, LANGUAGES } from '../functions/api/_languages.js';

const env = { SUPABASE_URL: 'https://example.supabase.co', SUPABASE_SECRET_KEY: 'sb_secret_test', STRIPE_SECRET_KEY: 'sk_test' };
const headers = { Authorization: 'Bearer t', 'Content-Type': 'application/json' };

assert.equal(planSizeFromLookupKey('routine_3_idiomas'), 3);
assert.equal(planSizeFromLookupKey('english_routine_mensal'), 1);
assert.equal(planSizeFromLookupKey('outra'), null);
assert.deepEqual(cleanLanguages(['EN', 'en', 'ko', 'xx']), ['en']);
assert.deepEqual(cleanLanguages(['en', 'ko'], { onlyAvailable: false }), ['en', 'ko']);

let profile;
let patched = null;
globalThis.fetch = async (url, options = {}) => {
  url = String(url);
  if (url.endsWith('/auth/v1/user')) return Response.json({ id: 'u1', email: 'a@b.com' });
  if (url.includes('/rest/v1/profiles')) {
    if (options.method === 'PATCH') {
      patched = JSON.parse(options.body);
      return Response.json([{ ...profile, ...patched }]);
    }
    return Response.json([profile]);
  }
  throw new Error(`Unexpected ${url}`);
};
const post = body => chooseLanguages({ request: new Request('https://app.test/api/languages', { method: 'POST', headers, body: JSON.stringify(body) }), env });

profile = { subscription_status: 'inactive', languages: ['en'], plan_size: 1 };
assert.equal((await post({ languages: ['en'] })).status, 403);

// Korean is not available yet, so it cannot be chosen.
profile = { subscription_status: 'active', languages: ['en'], plan_size: 2, languages_changed_at: null };
assert.equal((await post({ languages: ['ko'] })).status, 400);

// While Korean is unreleased, simulate a released catalogue to test the rules.
LANGUAGES.ko.available = true;
patched = null;
profile = { subscription_status: 'active', languages: ['en'], plan_size: 2, languages_changed_at: new Date().toISOString() };
assert.equal((await post({ languages: ['en', 'ko'] })).status, 200);
assert.deepEqual(patched.languages, ['en', 'ko']);
assert.equal(patched.languages_changed_at, undefined, 'filling a free slot does not count as a swap');

profile = { subscription_status: 'active', languages: ['en'], plan_size: 1, languages_changed_at: new Date().toISOString() };
assert.equal((await post({ languages: ['ko'] })).status, 409, 'swap blocked within 30 days');

profile = { subscription_status: 'active', languages: ['en'], plan_size: 1, languages_changed_at: null };
patched = null;
assert.equal((await post({ languages: ['ko'] })).status, 200);
assert.ok(patched.languages_changed_at, 'swap records the change date');

// Checkout picks the price by package size and stores the languages.
let checkoutParams = null;
let lookedUp = '';
globalThis.fetch = async (url, options = {}) => {
  url = String(url);
  if (url.endsWith('/auth/v1/user')) return Response.json({ id: 'u1', email: 'a@b.com' });
  if (url.includes('/rest/v1/profiles')) return Response.json([{ stripe_customer_id: 'cus_1', full_name: 'A' }]);
  if (url.startsWith('https://api.stripe.com/v1/prices')) {
    lookedUp = decodeURIComponent(url);
    return Response.json({ data: [{ id: 'price_x' }] });
  }
  if (url.startsWith('https://api.stripe.com/v1/checkout/sessions')) {
    checkoutParams = new URLSearchParams(options.body);
    return Response.json({ url: 'https://checkout.test' });
  }
  throw new Error(`Unexpected ${url}`);
};
const res = await checkout({ request: new Request('https://app.test/api/create-checkout-session', { method: 'POST', headers, body: JSON.stringify({ languages: ['en', 'ko'] }) }), env });
assert.equal(res.status, 200);
assert.match(lookedUp, /routine_2_idiomas/);
assert.equal(checkoutParams.get('subscription_data[metadata][languages]'), 'en,ko');
await checkout({ request: new Request('https://app.test/api/create-checkout-session', { method: 'POST', headers, body: '' }), env });
assert.match(lookedUp, /english_routine_mensal/);
assert.equal(checkoutParams.get('subscription_data[metadata][languages]'), 'en');
LANGUAGES.ko.available = false;
console.log('languages_test: ok');
