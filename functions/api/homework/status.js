import{json,userFromRequest,adminRest}from'../_shared.js';
export async function onRequestGet({request,env}){
 const user=await userFromRequest(request,env);if(!user)return json({error:'Sessão inválida.'},401);
 const profiles=await adminRest(env,`profiles?id=eq.${encodeURIComponent(user.id)}&select=role,subscription_status`),profile=profiles?.[0];
 if(profile?.role!=='admin'&&!['active','trialing'].includes(profile?.subscription_status))return json({error:'Assinatura inativa.'},403);
 return json({service:'english-daily-homework',appVersion:'2026.10.06.2',configured:!!env.OPENAI_API_KEY,model:'gpt-4o-mini',transcribeModel:env.OPENAI_TRANSCRIBE_MODEL||'gpt-4o-mini-transcribe'});
}
