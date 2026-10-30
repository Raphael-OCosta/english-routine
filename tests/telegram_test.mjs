// Checks do aviso de vendas no Telegram: node tests/telegram_test.mjs
import assert from 'node:assert/strict';
import { createHmac } from 'node:crypto';
import { onRequestPost } from '../functions/api/stripe-webhook.js';
import { saleMessage } from '../functions/api/_telegram.js';

const env = { SUPABASE_URL: 'https://example.supabase.co', SUPABASE_SECRET_KEY: 'sb_secret_test', STRIPE_WEBHOOK_SECRET: 'whsec_test', TELEGRAM_BOT_TOKEN: '123:abc', TELEGRAM_CHAT_ID: '42' };
const sent = [];
let dbFails = false;
let telegramFails = false;
globalThis.fetch = async (url, options = {}) => {
  url = String(url);
  if (url.startsWith('https://api.telegram.org/')) {
    if (telegramFails) throw new Error('offline');
    sent.push({ url, ...JSON.parse(options.body) });
    return Response.json({ ok: true });
  }
  if (dbFails) return new Response('{}', { status: 500 });
  return Response.json([{ id: 'u1', languages: ['en'] }]);
};

async function send(event, config = env) {
  const body = JSON.stringify(event);
  const t = Math.floor(Date.now() / 1000);
  const sig = createHmac('sha256', config.STRIPE_WEBHOOK_SECRET).update(`${t}.${body}`).digest('hex');
  const request = new Request('https://app.test/api/stripe-webhook', { method: 'POST', headers: { 'Stripe-Signature': `t=${t},v1=${sig}` }, body });
  return onRequestPost({ request, env: config });
}
const userId = '11111111-1111-4111-8111-111111111111';
const checkout = { type: 'checkout.session.completed', livemode: true, data: { object: { mode: 'subscription', client_reference_id: userId, customer: 'cus_1', amount_total: 7490, metadata: { languages: 'en,ko' }, customer_details: { email: 'aluno@example.com', name: 'Aluno' } } } };

// compra real: plano, idiomas e valor, sem dados pessoais
assert.equal((await send(checkout)).status, 200);
assert.equal(sent.length, 1);
assert.equal(sent[0].chat_id, '42');
assert.ok(sent[0].url.endsWith('/bot123:abc/sendMessage'));
assert.equal(sent[0].text, 'Nova assinatura!\nPlano: 2 idiomas (Inglês, Coreano)\nValor: R$ 74,90');
assert.ok(!sent[0].text.includes('aluno@example.com'));

// modo de teste é identificado
assert.ok(saleMessage({ ...checkout, livemode: false }).startsWith('[TESTE] Nova assinatura!'));

// cancelamento só avisa quando o agendamento acontece, não em toda atualização
const updated = { type: 'customer.subscription.updated', livemode: true, data: { object: { cancel_at_period_end: true, metadata: { languages: 'en' }, items: { data: [{ current_period_end: 1798761600 }] } }, previous_attributes: { cancel_at_period_end: false } } };
assert.match(saleMessage(updated), /^Cancelamento agendado\nPlano: 1 idioma \(Inglês\)\nAcesso até \d\d\/\d\d\/\d{4}$/);
assert.equal(saleMessage({ ...updated, data: { ...updated.data, previous_attributes: { status: 'active' } } }), null);
assert.equal(saleMessage({ type: 'customer.subscription.deleted', livemode: true, data: { object: {} } }), 'Assinatura encerrada');
assert.equal(saleMessage({ type: 'invoice.payment_failed', livemode: true, data: { object: { amount_due: 4490 } } }), 'Pagamento recusado\nValor: R$ 44,90');
assert.equal(saleMessage({ type: 'invoice.paid', data: { object: {} } }), null);

// falha no Telegram não derruba o webhook
telegramFails = true;
assert.equal((await send(checkout)).status, 200);
telegramFails = false;

// sem as variáveis, nada é enviado
sent.length = 0;
const { TELEGRAM_BOT_TOKEN, ...noBot } = env;
assert.equal((await send(checkout, noBot)).status, 200);
assert.equal(sent.length, 0);

// banco fora do ar: o Stripe vai reenviar, então o aviso espera
dbFails = true;
assert.equal((await send(checkout)).status, 500);
assert.equal(sent.length, 0);
console.log('telegram_test: ok');
