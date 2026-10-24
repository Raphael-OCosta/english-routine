// Guarda leve para páginas exclusivas de assinantes que não sincronizam progresso
// (ex.: teste de nível). Sem sessão → login; sem acesso ao idioma → painel.
// Uso: <script src="/assets/require-access.js" data-lang="en"></script> depois do
// supabase-js e do /config.js, com html[data-cloud-auth="pending"] escondendo a página.
(() => {
  const LANGUAGE = document.currentScript?.dataset.lang || 'en';
  addEventListener('DOMContentLoaded', async () => {
    const cfg = window.ENGLISH_DAILY_CONFIG;
    if (!cfg?.supabaseUrl || !cfg?.supabaseAnonKey) { location.href = '/login.html'; return; }
    const client = window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey);
    let { data: { session } } = await client.auth.getSession();
    if (session && (await client.auth.getUser()).error) session = (await client.auth.refreshSession()).data.session;
    if (!session) { location.href = '/login.html'; return; }
    try {
      const response = await fetch('/api/profile', { headers: { Authorization: `Bearer ${session.access_token}` } });
      const { profile } = await response.json();
      const languages = profile?.access?.languages;
      const active = response.ok && Boolean(profile?.access?.active) && (!Array.isArray(languages) || languages.includes(LANGUAGE));
      if (!active) { location.href = '/dashboard.html'; return; }
    } catch (_) {
      location.href = '/dashboard.html';
      return;
    }
    delete document.documentElement.dataset.cloudAuth;
  });
})();
