import { json, userFromRequest, adminRest, stripe, subscriptionPriceId } from './_shared.js';
import { cleanLanguages } from './_languages.js';

// Body opcional: { languages: ['en', 'ko'] }. O tamanho da lista define o
// pacote (1, 2 ou 3 idiomas) e os idiomas vão nos metadados da assinatura,
// de onde o webhook os grava no perfil.
export async function onRequestPost({ request, env }) {
  try {
    const user = await userFromRequest(request, env);
    if (!user) return json({ error: 'Não autenticado.' }, 401);
    const body = await request.json().catch(() => ({}));
    const languages = cleanLanguages(body?.languages?.length ? body.languages : ['en']);
    if (!languages.length) return json({ error: 'Escolha ao menos um idioma disponível.' }, 400);

    const rows = await adminRest(env, `profiles?id=eq.${encodeURIComponent(user.id)}&select=stripe_customer_id,full_name`);
    const profile = rows?.[0];
    let customer = profile?.stripe_customer_id;
    if (!customer) {
      const created = await stripe(env, 'customers', {
        email: user.email,
        name: profile?.full_name || '',
        'metadata[user_id]': user.id,
      });
      customer = created.id;
      await adminRest(env, `profiles?id=eq.${encodeURIComponent(user.id)}`, {
        method: 'PATCH',
        body: JSON.stringify({ stripe_customer_id: customer }),
      });
    }
    const origin = new URL(request.url).origin;
    const session = await stripe(env, 'checkout/sessions', {
      mode: 'subscription',
      customer,
      client_reference_id: user.id,
      'line_items[0][price]': await subscriptionPriceId(env, languages.length),
      'line_items[0][quantity]': '1',
      success_url: `${origin}/dashboard.html?checkout=success`,
      cancel_url: `${origin}/dashboard.html?checkout=cancelled`,
      'metadata[languages]': languages.join(','),
      'subscription_data[metadata][user_id]': user.id,
      'subscription_data[metadata][languages]': languages.join(','),
      allow_promotion_codes: 'true',
    });
    return json({ url: session.url });
  } catch (error) {
    return json({ error: error.message }, 500);
  }
}
