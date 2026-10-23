(async () => {
  const cfg = window.ENGLISH_DAILY_CONFIG;
  if (!cfg?.supabaseUrl || !cfg?.supabaseAnonKey) {
    location.href = '/login.html';
    return;
  }

  const client = window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey);
  const logout = document.querySelector('#logout');
  logout.onclick = async () => {
    logout.disabled = true;
    await client.auth.signOut({ scope: 'local' });
    Object.keys(localStorage)
      .filter(key => key.startsWith('english-daily-v1') || key.startsWith('routine-'))
      .forEach(key => localStorage.removeItem(key));
    location.replace('/login.html');
  };

  let { data: { session } } = await client.auth.getSession();
  if (!session) {
    location.replace('/login.html');
    return;
  }

  const { error: userError } = await client.auth.getUser();
  if (userError) {
    const refreshed = await client.auth.refreshSession();
    session = refreshed.data.session;
  } else {
    session = (await client.auth.getSession()).data.session;
  }
  if (!session) {
    await client.auth.signOut({ scope: 'local' });
    location.replace('/login.html');
    return;
  }

  const historyFile = document.querySelector('#historyFile');
  const historyPaste = document.querySelector('#historyPaste');
  const historyStatus = document.querySelector('#historyStatus');
  document.querySelector('#importHistory').onclick = async () => {
    try {
      historyStatus.textContent = 'Lendo o backup…';
      const raw = historyFile.files[0]
        ? await historyFile.files[0].text()
        : historyPaste.value.trim();
      if (!raw) throw new Error('Selecione o arquivo ou cole o conteúdo do backup.');
      const state = JSON.parse(raw);
      if (!state || typeof state !== 'object' || !Array.isArray(state.attempts)) {
        throw new Error('O arquivo não parece ser um backup válido do English Routine.');
      }
      const progressResponse = await fetch('/api/progress', {
        headers: { Authorization: `Bearer ${session.access_token}` },
      });
      const progressResult = await progressResponse.json();
      if (!progressResponse.ok) throw new Error(progressResult.error || 'Não foi possível carregar o progresso atual.');

      const current = progressResult.state && typeof progressResult.state === 'object'
        ? progressResult.state
        : {};
      const attempts = [...(Array.isArray(current.attempts) ? current.attempts : [])];
      const attemptKeys = new Set(attempts.map(item => `${item.time}|${item.qid}`));
      for (const item of state.attempts) {
        const key = `${item.time}|${item.qid}`;
        if (!attemptKeys.has(key)) {
          attempts.push(item);
          attemptKeys.add(key);
        }
      }
      attempts.sort((a, b) => String(a.time).localeCompare(String(b.time)));

      const currentSkills = current.skills || {};
      const incomingSkills = state.skills || {};
      const events = [...(Array.isArray(currentSkills.events) ? currentSkills.events : [])];
      const eventKeys = new Set(events.map(item => item.id || `${item.time}|${item.skill || item.type || ''}`));
      for (const item of Array.isArray(incomingSkills.events) ? incomingSkills.events : []) {
        const key = item.id || `${item.time}|${item.skill || item.type || ''}`;
        if (!eventKeys.has(key)) {
          events.push(item);
          eventKeys.add(key);
        }
      }
      events.sort((a, b) => String(a.time).localeCompare(String(b.time)));

      const goalHistory = { ...(state.goalHistory || {}), ...(current.goalHistory || {}) };
      for (const [day, value] of Object.entries(state.goalHistory || {})) {
        goalHistory[day] = Math.max(Number(goalHistory[day] || 0), Number(value || 0));
      }
      const merged = {
        ...state,
        ...current,
        version: 1,
        // An explicit import restores old answers on purpose, so it clears
        // the reset cut-off that would otherwise filter them out again.
        resetAt: undefined,
        attempts,
        session: null,
        goalHistory,
        skills: {
          ...incomingSkills,
          ...currentSkills,
          events,
          drafts: { ...(incomingSkills.drafts || {}), ...(currentSkills.drafts || {}) },
          accepted: [...new Set([
            ...(Array.isArray(currentSkills.accepted) ? currentSkills.accepted : []),
            ...(Array.isArray(incomingSkills.accepted) ? incomingSkills.accepted : []),
          ])],
        },
      };

      const saveResponse = await fetch('/api/progress', {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${session.access_token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ state: merged }),
      });
      const saveResult = await saveResponse.json();
      if (!saveResponse.ok) throw new Error(saveResult.error || 'Não foi possível salvar o histórico.');
      sessionStorage.removeItem('english-daily-cloud-loaded');
      historyStatus.textContent = `Histórico combinado com sucesso: ${attempts.length} respostas disponíveis. Abra o treino para conferir.`;
      document.querySelector('#study').hidden = false;
    } catch (error) {
      const message = error.message || '';
      historyStatus.textContent = message.toLowerCase().includes('permission denied')
        ? 'O banco ainda precisa receber as permissões da migração 003. Nenhum dado foi alterado.'
        : message || 'Não foi possível importar o histórico.';
    }
  };

  async function loadProfile(retry = true) {
    const response = await fetch('/api/profile', {
      headers: { Authorization: `Bearer ${session.access_token}` },
    });
    const result = await response.json();
    if (response.status === 401 && retry) {
      const refreshed = await client.auth.refreshSession();
      if (refreshed.data.session) {
        session = refreshed.data.session;
        return loadProfile(false);
      }
    }
    if (!response.ok || !result.profile) throw new Error(result.error || 'Não foi possível carregar seu perfil.');
    catalog = result.languages || { en: { name: 'Inglês', brand: 'English Routine', app: '/app.html', available: true } };
    return result.profile;
  }
  let catalog = {};

  let profile;
  try {
    profile = await loadProfile();
  } catch (error) {
    document.querySelector('#subscription').textContent = 'Indisponível';
    document.querySelector('#accessMessage').textContent = error.message;
    return;
  }

  document.querySelector('#studentName').textContent = profile.full_name || session.user.email.split('@')[0];
  document.querySelector('#accountEmail').textContent = session.user.email;
  const access = profile.access || { active: false, source: 'none' };
  const active = Boolean(access.active);
  const giftUntil = access.expires_at ? new Date(access.expires_at).toLocaleDateString('pt-BR') : '';
  document.querySelector('#subscription').textContent = {
    admin: 'Administrador',
    subscription: 'Ativa',
    gift: giftUntil ? `Cortesia até ${giftUntil}` : 'Cortesia',
  }[access.source] || 'Inativa';
  document.querySelector('#accessMessage').textContent = access.source === 'gift'
    ? 'Você recebeu acesso de cortesia. Bons estudos!'
    : active
      ? 'Seu acesso está liberado. Continue de onde parou.'
      : 'Assine para liberar todos os treinos e salvar o progresso na nuvem.';
  document.querySelector('#study').hidden = !active;
  document.querySelector('#subscribe').hidden = active;
  document.querySelector('#portal').hidden = !profile.stripe_customer_id;
  document.querySelector('#admin').hidden = profile.role !== 'admin';

  try {
    const progressResponse = await fetch('/api/progress', {
      cache: 'no-store',
      headers: { Authorization: `Bearer ${session.access_token}` },
    });
    const progressResult = await progressResponse.json();
    if (!progressResponse.ok) throw new Error(progressResult.error || 'Não foi possível consultar o progresso.');
    const attempts = Array.isArray(progressResult.state?.attempts) ? progressResult.state.attempts.length : 0;
    const skills = Array.isArray(progressResult.state?.skills?.events) ? progressResult.state.skills.events.length : 0;
    document.querySelector('#cloudProgress').textContent = `${attempts} ${attempts === 1 ? 'resposta salva' : 'respostas salvas'} na nuvem${skills ? ` · ${skills} treinos de habilidades` : ''}.`;
  } catch (error) {
    document.querySelector('#cloudProgress').textContent = `Não foi possível conferir o progresso salvo: ${error.message}`;
  }

  async function call(path, button, loadingMessage) {
    const originalLabel = button.textContent;
    button.disabled = true;
    document.querySelector('#accessMessage').textContent = loadingMessage;
    try {
      const response = await fetch(path, {
        method: 'POST',
        headers: { Authorization: `Bearer ${session.access_token}`, 'Content-Type': 'application/json' },
        body: JSON.stringify(path.includes('checkout') ? { languages: checked() } : {}),
      });
      const data = await response.json();
      if (!response.ok) throw Error(data.error || 'Não foi possível continuar.');
      if (!data.url) throw Error('O Stripe não devolveu o endereço de pagamento.');
      location.href = data.url;
    } catch (error) {
      button.disabled = false;
      button.textContent = originalLabel;
      document.querySelector('#accessMessage').textContent = `Não foi possível abrir o Stripe: ${error.message}`;
    }
  }
  const subscribe = document.querySelector('#subscribe');
  const portal = document.querySelector('#portal');

  // ------------------------------------------------------------ idiomas
  const PLAN_PRICES = { 1: 'R$ 44,90/mês', 2: 'R$ 74,90/mês', 3: 'R$ 99,90/mês' };
  const subscriber = access.source === 'subscription';
  const planSize = subscriber ? Math.max(1, Number(access.plan_size) || 1) : 3;
  const entitled = Array.isArray(access.languages) ? access.languages : [];
  const languageList = document.querySelector('#languageList');
  const languagesStatus = document.querySelector('#languagesStatus');
  const saveLanguages = document.querySelector('#saveLanguages');
  const planPrice = document.querySelector('#planPrice');
  const selectable = !active || subscriber;
  document.querySelector('#languagesBox').hidden = false;
  document.querySelector('#languagesSummary').textContent = subscriber
    ? `Seu pacote inclui ${planSize} ${planSize === 1 ? 'idioma' : 'idiomas'}. Para incluir mais idiomas, altere o plano em Gerenciar cobrança.`
    : active
      ? 'Idiomas liberados no seu acesso.'
      : 'Escolha os idiomas da sua assinatura: 1 idioma R$ 44,90, 2 idiomas R$ 74,90, 3 idiomas R$ 99,90 por mês.';

  const escapeHtml = value => String(value ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  languageList.innerHTML = Object.entries(catalog).map(([code, lang]) => {
    const has = entitled.includes(code);
    const status = has ? 'Liberado' : lang.available ? 'Disponível' : 'Em breve';
    const box = selectable && lang.available
      ? `<input type="checkbox" data-language="${code}" ${has || (!active && code === 'en') ? 'checked' : ''}>`
      : '';
    const action = has && lang.available ? `<a class="button" href="${escapeHtml(lang.app)}">Treinar</a>` : `<span class="badge">${status}</span>`;
    return `<div class="language-item"><label>${box}<span>${escapeHtml(lang.brand)}<small>${escapeHtml(lang.name)} · ${status}</small></span></label>${action}</div>`;
  }).join('');

  const checked = () => [...languageList.querySelectorAll('input[data-language]:checked')].map(input => input.dataset.language);
  function refreshChoice() {
    const count = checked().length;
    if (!active) {
      planPrice.hidden = count === 0;
      planPrice.textContent = count ? `${count} ${count === 1 ? 'idioma' : 'idiomas'} · ${PLAN_PRICES[count]}` : '';
      subscribe.disabled = count === 0;
    }
    if (subscriber) {
      saveLanguages.hidden = false;
      saveLanguages.disabled = count === 0 || count > planSize
        || (count === entitled.length && checked().every(code => entitled.includes(code)));
      languagesStatus.textContent = count > planSize ? `Seu pacote permite até ${planSize} ${planSize === 1 ? 'idioma' : 'idiomas'}.` : '';
    }
  }
  languageList.addEventListener('change', refreshChoice);
  refreshChoice();

  saveLanguages.onclick = async () => {
    saveLanguages.disabled = true;
    languagesStatus.textContent = 'Salvando…';
    try {
      const response = await fetch('/api/languages', {
        method: 'POST',
        headers: { Authorization: `Bearer ${session.access_token}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({ languages: checked() }),
      });
      const data = await response.json();
      if (!response.ok) throw Error(data.error || 'Não foi possível salvar.');
      location.reload();
    } catch (error) {
      languagesStatus.textContent = error.message;
      saveLanguages.disabled = false;
    }
  };
  subscribe.onclick = () => call('/api/create-checkout-session', subscribe, 'Abrindo o pagamento seguro do Stripe…');
  portal.onclick = () => call('/api/customer-portal', portal, 'Abrindo o portal de cobrança…');
})();

