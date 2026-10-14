import{json,userFromRequest,requireActive}from'../_shared.js';
export async function onRequestGet({request,env}){
 const user=await userFromRequest(request,env);if(!user)return json({error:'Sessão inválida.'},401);
 if(!await requireActive(env,user))return json({error:'Assinatura inativa.'},403);
 return json({service:'english-daily-homework',appVersion:'2026.10.06.2',configured:!!env.OPENAI_API_KEY,model:'gpt-4o-mini',transcribeModel:env.OPENAI_TRANSCRIBE_MODEL||'gpt-4o-mini-transcribe'});
}
