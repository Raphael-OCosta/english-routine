import { json, userFromRequest, adminRest } from './_shared.js';
import { LANGUAGE_CHANGE_DAYS, cleanLanguages } from './_languages.js';

const DAY_MS = 86_400_000;

// Escolha dos idiomas do pacote pelo assinante.
// - Ocupar vagas livres (ex.: depois de um upgrade) é sempre permitido.
// - Trocar um idioma já escolhido vale uma vez a cada LANGUAGE_CHANGE_DAYS dias.
export async function onRequestPost({ request, env }) {
  try {
    const user = await userFromRequest(request, env);
    if (!user) return json({ error: 'Não autenticado.' }, 401);
    const rows = await adminRest(
      env,
      `profiles?id=eq.${encodeURIComponent(user.id)}&select=subscription_status,languages,plan_size,languages_changed_at`,
    );
    const profile = rows?.[0];
    if (!['active', 'trialing'].includes(profile?.subscription_status)) {
      return json({ error: 'A escolha de idiomas é feita pelos assinantes.' }, 403);
    }
    const planSize = Math.max(1, Number(profile.plan_size) || 1);
    const body = await request.json().catch(() => ({}));
    const wanted = cleanLanguages(body?.languages, { max: planSize });
    if (!wanted.length) return json({ error: 'Escolha ao menos um idioma disponível.' }, 400);

    const current = Array.isArray(profile.languages) ? profile.languages : [];
    const removesSomething = current.some(code => !wanted.includes(code));
    if (removesSomething && profile.languages_changed_at) {
      const next = Date.parse(profile.languages_changed_at) + LANGUAGE_CHANGE_DAYS * DAY_MS;
      if (next > Date.now()) {
        const date = new Date(next).toLocaleDateString('pt-BR');
        return json({ error: `Você poderá trocar de idioma novamente a partir de ${date}.` }, 409);
      }
    }
    const patch = { languages: wanted };
    if (removesSomething) patch.languages_changed_at = new Date().toISOString();
    const saved = await adminRest(env, `profiles?id=eq.${encodeURIComponent(user.id)}`, {
      method: 'PATCH',
      body: JSON.stringify(patch),
    });
    return json({ languages: saved?.[0]?.languages || wanted });
  } catch (error) {
    return json({ error: error.message || 'Não foi possível salvar os idiomas.' }, 500);
  }
}
