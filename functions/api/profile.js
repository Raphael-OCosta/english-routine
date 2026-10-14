import { json, userFromRequest, adminRest, accessFor } from './_shared.js';

export async function onRequestGet({ request, env }) {
  try {
    const user = await userFromRequest(request, env);
    if (!user) return json({ error: 'Não autenticado.' }, 401);

    const select = 'full_name,role,subscription_status,stripe_customer_id';
    let rows = await adminRest(
      env,
      `profiles?id=eq.${encodeURIComponent(user.id)}&select=${select}`,
    );

    if (!rows?.length) {
      const email = String(user.email || '').toLowerCase();
      const profile = {
        id: user.id,
        email,
        full_name: user.user_metadata?.name || (email === 'rarphael@gmail.com' ? 'Raphael Costa' : ''),
        role: email === 'rarphael@gmail.com' ? 'admin' : 'student',
        subscription_status: 'inactive',
      };
      rows = await adminRest(env, 'profiles', {
        method: 'POST',
        body: JSON.stringify(profile),
      });
    }

    const profile = rows?.[0];
    if (!profile) throw new Error('O perfil não pôde ser criado.');
    return json({ profile: { ...profile, access: await accessFor(env, user, profile) } });
  } catch (error) {
    const raw = error.message || '';
    const permission = raw.includes('42501') || raw.toLowerCase().includes('permission denied');
    return json({
      error: permission
        ? 'O banco ainda precisa receber as permissões da migração 003.'
        : raw || 'Não foi possível carregar seu perfil.',
    }, 500);
  }
}

