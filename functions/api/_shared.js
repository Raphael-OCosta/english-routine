import { LANGUAGES, MAX_PLAN_SIZE, PLAN_LOOKUP_KEYS, availableLanguages, cleanLanguages } from './_languages.js';

export const json = (data, status = 200) => new Response(JSON.stringify(data), {
  status,
  headers: {
    'Content-Type': 'application/json',
    'Cache-Control': 'private, no-store',
  },
});

export async function userFromRequest(request, env) {
  const token = (request.headers.get('Authorization') || '').replace(/^Bearer\s+/, '');
  if (!token) return null;

  const keys = [
    env.SUPABASE_PUBLISHABLE_KEY || env.SUPABASE_ANON_KEY,
    env.SUPABASE_SECRET_KEY || env.SUPABASE_SERVICE_ROLE_KEY,
  ].filter(Boolean);

  for (const key of [...new Set(keys)]) {
    const response = await fetch(`${env.SUPABASE_URL}/auth/v1/user`, {
      headers: { apikey: key, Authorization: `Bearer ${token}` },
    });
    if (response.ok) return response.json();
  }
  return null;
}

export async function adminRest(env, path, options = {}) {
  const key = env.SUPABASE_SECRET_KEY || env.SUPABASE_SERVICE_ROLE_KEY;
  const legacy = !String(key).startsWith('sb_secret_');
  const headers = {
    apikey: key,
    'Content-Type': 'application/json',
    Prefer: 'return=representation',
    ...(legacy ? { Authorization: `Bearer ${key}` } : {}),
    ...(options.headers || {}),
  };
  const response = await fetch(`${env.SUPABASE_URL}/rest/v1/${path}`, { ...options, headers });
  if (!response.ok) throw Error(await response.text());
  const text = await response.text();
  return text ? JSON.parse(text) : null;
}

export async function stripe(env, path, params) {
  const response = await fetch(`https://api.stripe.com/v1/${path}`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.STRIPE_SECRET_KEY}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams(params),
  });
  const data = await response.json();
  if (!response.ok) throw Error(data.error?.message || 'Stripe request failed');
  return data;
}


const ACTIVE_STATUSES = ['active', 'trialing'];

// Resolves whether a user may use the paid features and in which languages:
// administrator (all languages, to test unreleased ones), Stripe subscription
// (the languages chosen for the plan) or an unexpired complimentary grant.
export async function accessFor(env, user, profile) {
  if (profile?.role === 'admin') {
    return { active: true, source: 'admin', expires_at: null, languages: Object.keys(LANGUAGES), plan_size: MAX_PLAN_SIZE };
  }
  if (ACTIVE_STATUSES.includes(profile?.subscription_status)) {
    const planSize = Math.min(MAX_PLAN_SIZE, Math.max(1, Number(profile?.plan_size) || 1));
    const chosen = cleanLanguages(profile?.languages, { onlyAvailable: false, max: planSize });
    return { active: true, source: 'subscription', expires_at: null, languages: chosen.length ? chosen : ['en'], plan_size: planSize };
  }
  const email = String(user?.email || '').toLowerCase();
  if (email) {
    const grants = await adminRest(
      env,
      `complimentary_grants?email=eq.${encodeURIComponent(email)}&select=expires_at,languages`,
    );
    const grant = grants?.[0];
    if (grant && (!grant.expires_at || Date.parse(grant.expires_at) > Date.now())) {
      const languages = Array.isArray(grant.languages) && grant.languages.length
        ? cleanLanguages(grant.languages, { onlyAvailable: false })
        : availableLanguages();
      return { active: true, source: 'gift', expires_at: grant.expires_at, languages, plan_size: languages.length };
    }
  }
  return { active: false, source: 'none', expires_at: null, languages: [], plan_size: 0 };
}

export async function requireActive(env, user, language = 'en') {
  const rows = await adminRest(
    env,
    `profiles?id=eq.${encodeURIComponent(user.id)}&select=role,subscription_status,languages,plan_size`,
  );
  const access = await accessFor(env, user, rows?.[0]);
  return access.active && access.languages.includes(language);
}

// Resolves the subscription price by its Stripe lookup key, so a price change
// only needs a new Stripe price with the same key (no redeploy). The 1-language
// plan falls back to STRIPE_PRICE_ID for environments without the key.
export async function subscriptionPriceId(env, planSize = 1) {
  const lookupKey = planSize === 1
    ? env.STRIPE_PRICE_LOOKUP_KEY || PLAN_LOOKUP_KEYS[1]
    : PLAN_LOOKUP_KEYS[planSize];
  if (!lookupKey) throw Error('Pacote inválido.');
  const params = new URLSearchParams({ active: 'true', limit: '1' });
  params.append('lookup_keys[]', lookupKey);
  const response = await fetch(`https://api.stripe.com/v1/prices?${params}`, {
    headers: { Authorization: `Bearer ${env.STRIPE_SECRET_KEY}` },
  });
  const data = await response.json();
  if (!response.ok) throw Error(data.error?.message || 'Stripe request failed');
  const price = data.data?.[0]?.id || (planSize === 1 ? env.STRIPE_PRICE_ID : null);
  if (!price) throw Error('Preço da assinatura não configurado.');
  return price;
}
