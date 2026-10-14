import { json, userFromRequest, adminRest } from './_shared.js';

const MAX_STATE_BYTES = 4_900_000;

async function readState(env, userId) {
  const rows = await adminRest(
    env,
    `progress_snapshots?user_id=eq.${encodeURIComponent(userId)}&select=state`,
  );
  return rows?.[0]?.state || null;
}

export async function onRequestGet({ request, env }) {
  try {
    const user = await userFromRequest(request, env);
    if (!user) return json({ error: 'Não autenticado.' }, 401);
    return json({ state: await readState(env, user.id) });
  } catch (error) {
    return json({ error: error.message || 'Não foi possível carregar o progresso.' }, 500);
  }
}

export async function onRequestPut({ request, env }) {
  try {
    const user = await userFromRequest(request, env);
    if (!user) return json({ error: 'Não autenticado.' }, 401);
    const body = await request.json();
    const state = body?.state;
    if (!state || typeof state !== 'object' || !Array.isArray(state.attempts)) {
      return json({ error: 'Progresso inválido.' }, 400);
    }
    if (new TextEncoder().encode(JSON.stringify(state)).length > MAX_STATE_BYTES) {
      return json({ error: 'O histórico excede o limite permitido.' }, 413);
    }
    const rows = await adminRest(env, 'progress_snapshots?on_conflict=user_id', {
      method: 'POST',
      headers: { Prefer: 'resolution=merge-duplicates,return=representation' },
      body: JSON.stringify({
        user_id: user.id,
        state,
        updated_at: new Date().toISOString(),
      }),
    });
    return json({ state: rows?.[0]?.state || state });
  } catch (error) {
    return json({ error: error.message || 'Não foi possível salvar o progresso.' }, 500);
  }
}

