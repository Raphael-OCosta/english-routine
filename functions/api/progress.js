import { json, userFromRequest, adminRest } from './_shared.js';
import { isLanguage } from './_languages.js';

const MAX_STATE_BYTES = 4_900_000;

// Each language keeps its own snapshot; requests without ?lang= are English,
// which keeps older app versions working.
function languageOf(request) {
  const lang = new URL(request.url).searchParams.get('lang') || 'en';
  return isLanguage(lang) ? lang : null;
}

async function readState(env, userId, language) {
  const rows = await adminRest(
    env,
    `progress_snapshots?user_id=eq.${encodeURIComponent(userId)}&language=eq.${language}&select=state`,
  );
  return rows?.[0]?.state || null;
}

export async function onRequestGet({ request, env }) {
  try {
    const user = await userFromRequest(request, env);
    if (!user) return json({ error: 'Não autenticado.' }, 401);
    const language = languageOf(request);
    if (!language) return json({ error: 'Idioma inválido.' }, 400);
    return json({ state: await readState(env, user.id, language), language });
  } catch (error) {
    return json({ error: error.message || 'Não foi possível carregar o progresso.' }, 500);
  }
}

export async function onRequestPut({ request, env }) {
  try {
    const user = await userFromRequest(request, env);
    if (!user) return json({ error: 'Não autenticado.' }, 401);
    const language = languageOf(request);
    if (!language) return json({ error: 'Idioma inválido.' }, 400);
    const body = await request.json();
    const state = body?.state;
    if (!state || typeof state !== 'object' || !Array.isArray(state.attempts)) {
      return json({ error: 'Progresso inválido.' }, 400);
    }
    if (new TextEncoder().encode(JSON.stringify(state)).length > MAX_STATE_BYTES) {
      return json({ error: 'O histórico excede o limite permitido.' }, 413);
    }
    const rows = await adminRest(env, 'progress_snapshots?on_conflict=user_id,language', {
      method: 'POST',
      headers: { Prefer: 'resolution=merge-duplicates,return=representation' },
      body: JSON.stringify({
        user_id: user.id,
        language,
        state,
        updated_at: new Date().toISOString(),
      }),
    });
    return json({ state: rows?.[0]?.state || state, language });
  } catch (error) {
    return json({ error: error.message || 'Não foi possível salvar o progresso.' }, 500);
  }
}
