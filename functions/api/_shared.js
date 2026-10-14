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

// Resolves whether a user may use the paid features: administrator, Stripe
// subscription or an unexpired complimentary grant for the account e-mail.
export async function accessFor(env, user, profile) {
  if (profile?.role === 'admin') return { active: true, source: 'admin', expires_at: null };
  if (ACTIVE_STATUSES.includes(profile?.subscription_status)) {
    return { active: true, source: 'subscription', expires_at: null };
  }
  const email = String(user?.email || '').toLowerCase();
  if (email) {
    const grants = await adminRest(
      env,
      `complimentary_grants?email=eq.${encodeURIComponent(email)}&select=expires_at`,
    );
    const grant = grants?.[0];
    if (grant && (!grant.expires_at || Date.parse(grant.expires_at) > Date.now())) {
      return { active: true, source: 'gift', expires_at: grant.expires_at };
    }
  }
  return { active: false, source: 'none', expires_at: null };
}

export async function requireActive(env, user) {
  const rows = await adminRest(
    env,
    `profiles?id=eq.${encodeURIComponent(user.id)}&select=role,subscription_status`,
  );
  return (await accessFor(env, user, rows?.[0])).active;
}
