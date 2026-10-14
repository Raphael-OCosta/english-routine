import { json, adminRest } from './_shared.js';

const enc = new TextEncoder();
const UUID_PATTERN = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

function hex(bytes) {
  return [...new Uint8Array(bytes)].map((byte) => byte.toString(16).padStart(2, '0')).join('');
}

function safeEqual(a, b) {
  if (a.length !== b.length) return false;
  let difference = 0;
  for (let index = 0; index < a.length; index += 1) {
    difference |= a.charCodeAt(index) ^ b.charCodeAt(index);
  }
  return difference === 0;
}

async function verify(body, header, secret) {
  const values = header.split(',').map((item) => item.split('='));
  const timestamp = values.find(([key]) => key === 't')?.[1];
  const signatures = values.filter(([key]) => key === 'v1').map(([, value]) => value);
  if (!timestamp || !signatures.length || !secret) return false;

  const signed = `${timestamp}.${body}`;
  const key = await crypto.subtle.importKey(
    'raw',
    enc.encode(secret),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign'],
  );
  const signature = hex(await crypto.subtle.sign('HMAC', key, enc.encode(signed)));
  return Math.abs(Date.now() / 1000 - Number(timestamp)) < 300
    && signatures.some((candidate) => safeEqual(signature, candidate));
}

export async function onRequestPost({ request, env }) {
  const body = await request.text();
  const signature = request.headers.get('Stripe-Signature') || '';
  if (!await verify(body, signature, env.STRIPE_WEBHOOK_SECRET)) {
    return json({ error: 'Assinatura inválida.' }, 400);
  }

  const event = JSON.parse(body);
  const object = event.data.object;

  try {
    if (event.type === 'checkout.session.completed') {
      const userId = object.client_reference_id || object.metadata?.user_id || '';
      if (UUID_PATTERN.test(userId)) {
        await adminRest(env, `profiles?id=eq.${encodeURIComponent(userId)}`, {
          method: 'PATCH',
          body: JSON.stringify({ stripe_customer_id: object.customer }),
        });
      }
    }

    if (event.type.startsWith('customer.subscription.')) {
      const customer = object.customer;
      const status = object.status;
      const currentPeriodEnd = object.items?.data?.[0]?.current_period_end
        ? new Date(object.items.data[0].current_period_end * 1000).toISOString()
        : null;
      await adminRest(env, 'subscriptions?on_conflict=stripe_subscription_id', {
        method: 'POST',
        headers: { Prefer: 'resolution=merge-duplicates,return=representation' },
        body: JSON.stringify({
          stripe_subscription_id: object.id,
          stripe_customer_id: customer,
          status,
          current_period_end: currentPeriodEnd,
          cancel_at_period_end: !!object.cancel_at_period_end,
        }),
      });
      await adminRest(env, `profiles?stripe_customer_id=eq.${encodeURIComponent(customer)}`, {
        method: 'PATCH',
        body: JSON.stringify({ subscription_status: status }),
      });
    }

    return json({ received: true });
  } catch (error) {
    return json({ error: error.message }, 500);
  }
}

