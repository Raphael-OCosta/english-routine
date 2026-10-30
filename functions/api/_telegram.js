import { LANGUAGES } from './_languages.js';

// Aviso de vendas no Telegram do dono do site. Sem as variáveis, não faz nada.
// Uma falha aqui nunca derruba o webhook do Stripe, e a mensagem não leva dados pessoais do aluno.
export async function notifyTelegram(env, text) {
  if (!env.TELEGRAM_BOT_TOKEN || !env.TELEGRAM_CHAT_ID) return false;
  try {
    const response = await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ chat_id: env.TELEGRAM_CHAT_ID, text }),
      signal: AbortSignal.timeout(5000),
    });
    return response.ok;
  } catch (_) {
    return false;
  }
}

const money = cents => `R$ ${(Number(cents || 0) / 100).toFixed(2).replace('.', ',')}`;
const date = seconds => new Date(seconds * 1000).toLocaleDateString('pt-BR', { timeZone: 'America/Sao_Paulo' });

function planLine(languages) {
  const names = String(languages || '').split(',').filter(Boolean).map(code => LANGUAGES[code]?.name || code);
  if (!names.length) return null;
  return `Plano: ${names.length} ${names.length === 1 ? 'idioma' : 'idiomas'} (${names.join(', ')})`;
}

// Texto do aviso para um evento do Stripe; null quando o evento não merece mensagem.
export function saleMessage(event) {
  const object = event.data.object;
  const lines = [];
  if (event.type === 'checkout.session.completed' && object.mode === 'subscription') {
    lines.push('Nova assinatura!', planLine(object.metadata?.languages), `Valor: ${money(object.amount_total)}`);
  } else if (event.type === 'customer.subscription.updated'
    && object.cancel_at_period_end && event.data.previous_attributes?.cancel_at_period_end === false) {
    const end = object.items?.data?.[0]?.current_period_end;
    lines.push('Cancelamento agendado', planLine(object.metadata?.languages), end ? `Acesso até ${date(end)}` : null);
  } else if (event.type === 'customer.subscription.deleted') {
    lines.push('Assinatura encerrada', planLine(object.metadata?.languages));
  } else if (event.type === 'invoice.payment_failed') {
    lines.push('Pagamento recusado', `Valor: ${money(object.amount_due)}`);
  } else {
    return null;
  }
  const text = lines.filter(Boolean).join('\n');
  return event.livemode === false ? `[TESTE] ${text}` : text;
}
