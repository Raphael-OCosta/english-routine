export function onRequestGet({env}){
 const config={supabaseUrl:env.SUPABASE_URL,supabaseAnonKey:env.SUPABASE_ANON_KEY};
 return new Response(`window.ENGLISH_DAILY_CONFIG=${JSON.stringify(config)};`,{headers:{'Content-Type':'application/javascript; charset=utf-8','Cache-Control':'public, max-age=300'}});
}
