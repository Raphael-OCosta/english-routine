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

