import assert from 'node:assert/strict';
import { subscriptionPriceId } from '../functions/api/_shared.js';

let requested = '';
let answer = { data: [{ id: 'price_lookup' }] };
globalThis.fetch = async url => {
  requested = String(url);
  return Response.json(answer);
};

const env = { STRIPE_SECRET_KEY: 'sk_test', STRIPE_PRICE_ID: 'price_env' };
assert.equal(await subscriptionPriceId(env), 'price_lookup');
assert.match(decodeURIComponent(requested), /lookup_keys\[\]=english_routine_mensal/);
answer = { data: [] };
assert.equal(await subscriptionPriceId(env), 'price_env');
await assert.rejects(subscriptionPriceId({ STRIPE_SECRET_KEY: 'sk_test' }), /não configurado/);
console.log('price_test: ok');
