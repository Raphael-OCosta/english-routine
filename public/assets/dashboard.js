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
      const { data: currentRow, error: readError } = await client
        .from('progress_snapshots')
        .select('state')
        .maybeSingle();
      if (readError) throw readError;

      const current = currentRow?.state && typeof currentRow.state === 'object'
        ? currentRow.state
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

      const { error } = await client.from('progress_snapshots').upsert({
        user_id: session.user.id,
        state: merged,
        updated_at: new Date().toISOString(),
      });
      if (error) throw error;
      sessionStorage.removeItem('english-daily-cloud-loaded');
      historyStatus.textContent = `Histórico combinado com sucesso: ${attempts.length} respostas disponíveis. Abra o treino para conferir.`;
      document.querySelector('#study').hidden = false;
    } catch (error) {
      historyStatus.textContent = error.message || 'Não foi possível importar o histórico.';
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
    return result.profile;
  }

  let profile;
  try {
    profile = await loadProfile();
  } catch (error) {
    document.querySelector('#subscription').textContent = 'Indisponível';
    document.querySelector('#accessMessage').textContent = error.message;
    return;
  }

  document.querySelector('#studentName').textContent = profile.full_name || session.user.email.split('@')[0];
  const active = ['active', 'trialing'].includes(profile.subscription_status) || profile.role === 'admin';
  document.querySelector('#subscription').textContent = profile.role === 'admin' ? 'Administrador' : active ? 'Ativa' : 'Inativa';
  document.querySelector('#accessMessage').textContent = active
    ? 'Seu acesso está liberado. Continue de onde parou.'
    : 'Assine para liberar todos os treinos e salvar o progresso na nuvem.';
  document.querySelector('#study').hidden = !active;
  document.querySelector('#subscribe').hidden = active;
  document.querySelector('#portal').hidden = !profile.stripe_customer_id;
  document.querySelector('#admin').hidden = profile.role !== 'admin';

  async function call(path) {
    const response = await fetch(path, {
      method: 'POST',
      headers: { Authorization: `Bearer ${session.access_token}` },
    });
    const data = await response.json();
    if (!response.ok) throw Error(data.error || 'Não foi possível continuar.');
    location.href = data.url;
  }
  document.querySelector('#subscribe').onclick = () => call('/api/create-checkout-session');
  document.querySelector('#portal').onclick = () => call('/api/customer-portal');
})();

