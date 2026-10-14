// Compatibility route for pages that load `/config.js`.
// Cloudflare Pages strips only the final extension, so this file maps to
// `/config.js` while `functions/config.js` continues to map to `/config`.
export function onRequestGet({ env }) {
  const config = {
    supabaseUrl: env.SUPABASE_URL,
    supabaseAnonKey: env.SUPABASE_PUBLISHABLE_KEY || env.SUPABASE_ANON_KEY,
  };

  return new Response(
    `window.ENGLISH_DAILY_CONFIG=${JSON.stringify(config)};`,
    {
      headers: {
        'Content-Type': 'application/javascript; charset=utf-8',
        'Cache-Control': 'public, max-age=300',
      },
    },
  );
}

