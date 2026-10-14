import { json, userFromRequest, adminRest } from '../_shared.js';

const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

async function requireAdmin(request, env) {
  const user = await userFromRequest(request, env);
  if (!user) return { response: json({ error: 'Não autenticado.' }, 401) };
  const rows = await adminRest(env, `profiles?id=eq.${encodeURIComponent(user.id)}&select=role`);
  if (rows?.[0]?.role !== 'admin') return { response: json({ error: 'Acesso restrito ao administrador.' }, 403) };
  return { user };
}

async function listGrants(env) {
  return await adminRest(
    env,
    'complimentary_grants?select=email,expires_at,note,created_at,updated_at&order=created_at.desc',
  ) || [];
}

export async function onRequestGet({ request, env }) {
  try {
    const { response } = await requireAdmin(request, env);
    if (response) return response;
    return json({ grants: await listGrants(env) });
  } catch (error) {
    return json({ error: error.message || 'Não foi possível listar as cortesias.' }, 500);
  }
}

export async function onRequestPost({ request, env }) {
  try {
    const { user, response } = await requireAdmin(request, env);
    if (response) return response;
    const body = await request.json().catch(() => ({}));
    const email = String(body?.email || '').trim().toLowerCase();
    if (!EMAIL_PATTERN.test(email) || email.length > 254) return json({ error: 'Informe um e-mail válido.' }, 400);

    let expiresAt = null;
    if (body?.expires_at) {
      const parsed = Date.parse(`${String(body.expires_at).slice(0, 10)}T23:59:59-03:00`);
      if (Number.isNaN(parsed)) return json({ error: 'Data de validade inválida.' }, 400);
      if (parsed <= Date.now()) return json({ error: 'A validade precisa ser uma data futura.' }, 400);
      expiresAt = new Date(parsed).toISOString();
    }

    await adminRest(env, 'complimentary_grants?on_conflict=email', {
      method: 'POST',
      headers: { Prefer: 'resolution=merge-duplicates,return=representation' },
      body: JSON.stringify({
        email,
        expires_at: expiresAt,
        note: String(body?.note || '').trim().slice(0, 200),
        granted_by: user.id,
        updated_at: new Date().toISOString(),
      }),
    });
    return json({ grants: await listGrants(env) });
  } catch (error) {
    return json({ error: error.message || 'Não foi possível salvar a cortesia.' }, 500);
  }
}

export async function onRequestDelete({ request, env }) {
  try {
    const { response } = await requireAdmin(request, env);
    if (response) return response;
    const email = String(new URL(request.url).searchParams.get('email') || '').trim().toLowerCase();
    if (!email) return json({ error: 'Informe o e-mail.' }, 400);
    await adminRest(env, `complimentary_grants?email=eq.${encodeURIComponent(email)}`, { method: 'DELETE' });
    return json({ grants: await listGrants(env) });
  } catch (error) {
    return json({ error: error.message || 'Não foi possível revogar a cortesia.' }, 500);
  }
}
