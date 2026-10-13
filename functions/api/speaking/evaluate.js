import{json,userFromRequest,adminRest}from'../_shared.js';
const MIME_EXT={'audio/webm':'webm','audio/mp4':'m4a','audio/ogg':'ogg','audio/wav':'wav','audio/x-wav':'wav','audio/mpeg':'mp3'};
const words=s=>(s.toLowerCase().match(/[a-z]+(?:['’-][a-z]+)*/g)||[]);
function similarity(expected,actual){const a=words(expected),b=words(actual),m=a.length,n=b.length,row=Array.from({length:n+1},(_,i)=>i);for(let i=1;i<=m;i++){let prev=row[0];row[0]=i;for(let j=1;j<=n;j++){const old=row[j];row[j]=Math.min(row[j]+1,row[j-1]+1,prev+(a[i-1]===b[j-1]?0:1));prev=old}}const score=Math.round(100*(1-row[n]/Math.max(1,m,n))),missing=a.filter((w,i)=>b[i]!==w);return{score:Math.max(0,score),review:[...new Set(missing)].slice(0,10)}}
async function activeProfile(user,env){const rows=await adminRest(env,`profiles?id=eq.${encodeURIComponent(user.id)}&select=role,subscription_status`);return rows?.[0]}
async function consume(user,env){const today=new Date().toISOString().slice(0,10),rows=await adminRest(env,`ai_daily_usage?user_id=eq.${encodeURIComponent(user.id)}&usage_date=eq.${today}&select=calls`),calls=rows?.[0]?.calls||0,limit=Math.max(1,Math.min(100,Number(env.AI_DAILY_LIMIT)||10));if(calls>=limit)return{ok:false,limit};await adminRest(env,'ai_daily_usage?on_conflict=user_id,usage_date',{method:'POST',headers:{Prefer:'resolution=merge-duplicates,return=representation'},body:JSON.stringify({user_id:user.id,usage_date:today,calls:calls+1})});return{ok:true,limit}}
export async function onRequestPost({request,env}){
 const user=await userFromRequest(request,env);if(!user)return json({error:'Sessão inválida. Entre novamente.'},401);
 const profile=await activeProfile(user,env);if(profile?.role!=='admin'&&!['active','trialing'].includes(profile?.subscription_status))return json({error:'Assinatura inativa.'},403);
 if(!env.OPENAI_API_KEY)return json({error:'A avaliação por IA ainda não foi ativada pelo administrador.'},503);
 let data;try{data=await request.json()}catch{return json({error:'Gravação inválida.'},400)}
 const mime=String(data?.mimeType||'').split(';')[0].toLowerCase(),audio=String(data?.audio||''),mode=data?.mode,reference=String(data?.reference||'');
 if(!MIME_EXT[mime]||!['monologue','roleplay','shadow'].includes(mode)||!reference||reference.length>12000||audio.length<500||audio.length>22000000)return json({error:'Dados da gravação inválidos ou grandes demais.'},400);
 const usage=await consume(user,env);if(!usage.ok)return json({error:`Limite diário de ${usage.limit} avaliações por IA atingido.`},429);
 let bytes;try{bytes=Uint8Array.from(atob(audio),c=>c.charCodeAt(0))}catch{return json({error:'Não foi possível ler a gravação.'},400)}if(bytes.length>15000000)return json({error:'A gravação excede 15 MB.'},413);
 const form=new FormData();form.set('model',env.OPENAI_TRANSCRIBE_MODEL||'gpt-4o-mini-transcribe');form.set('language','en');form.set('response_format','json');form.append('file',new Blob([bytes],{type:mime}),`speaking.${MIME_EXT[mime]}`);
 const response=await fetch('https://api.openai.com/v1/audio/transcriptions',{method:'POST',headers:{Authorization:`Bearer ${env.OPENAI_API_KEY}`},body:form}),raw=await response.json();
 if(!response.ok)return json({error:raw?.error?.message||'A transcrição não pôde ser concluída.'},502);const transcript=String(raw.text||'').trim();if(!transcript)return json({error:'Não foi possível reconhecer fala em inglês.'},422);
 const match=mode==='shadow'?similarity(reference,transcript):null;return json({transcript:transcript.slice(0,20000),confidence:null,match:match?.score??null,score:match?.score??null,weakWords:[],reviewWords:match?.review||[]});
}
