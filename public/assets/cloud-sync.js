(() => {
  window.ENGLISH_DAILY_CLOUD = true;
  const KEY = 'english-daily-v1';
  const PENDING_KEY = `${KEY}-cloud-pending`;
  const HYDRATED_PARAM = 'cloud_hydrated';
  let client;
  let user;
  let ready = false;
  let timer;
  let syncStatus;
  let lastQueuedValue = null;
  const nativeFetch = window.fetch.bind(window);
  const originalSetItem = Storage.prototype.setItem;
  const originalRemoveItem = Storage.prototype.removeItem;

  window.fetch = async (input, init = {}) => {
    const url = typeof input === 'string' ? input : input.url;
    if (url.startsWith('/api/')) {
      const token = (await client?.auth.getSession())?.data?.session?.access_token;
      const headers = new Headers(init.headers || {});
      if (token) headers.set('Authorization', `Bearer ${token}`);
      init = { ...init, headers };
    }
    return nativeFetch(input, init);
  };

  function showSync(message, state = '') {
    if (!syncStatus) return;
    syncStatus.textContent = message;
    syncStatus.dataset.state = state;
  }

  function stableJson(value) {
    if (Array.isArray(value)) return `[${value.map(stableJson).join(',')}]`;
    if (value && typeof value === 'object') {
      return `{${Object.keys(value).sort().map(key => `${JSON.stringify(key)}:${stableJson(value[key])}`).join(',')}}`;
    }
    return JSON.stringify(value);
  }

  function durableJson(value) {
    if (!value || typeof value !== 'object') return stableJson(value);
    return stableJson({ ...value, session: null });
  }

  function hydrationMarked() {
    return new URL(location.href).searchParams.get(HYDRATED_PARAM) === '1';
  }

  function clearHydrationMark() {
    const url = new URL(location.href);
    if (!url.searchParams.has(HYDRATED_PARAM)) return;
    url.searchParams.delete(HYDRATED_PARAM);
    history.replaceState(null, '', `${url.pathname}${url.search}${url.hash}`);
  }

  function reloadAfterHydration() {
    const url = new URL(location.href);
    url.searchParams.set(HYDRATED_PARAM, '1');
    location.replace(`${url.pathname}${url.search}${url.hash}`);
  }

  function mergeStates(remote = {}, local = {}) {
    const attempts = [...(Array.isArray(remote.attempts) ? remote.attempts : [])];
    const attemptKeys = new Set(attempts.map(item => `${item.time}|${item.qid}`));
    for (const item of Array.isArray(local.attempts) ? local.attempts : []) {
      const key = `${item.time}|${item.qid}`;
      if (!attemptKeys.has(key)) {
        attempts.push(item);
        attemptKeys.add(key);
      }
    }
    attempts.sort((a, b) => String(a.time).localeCompare(String(b.time)));

    const remoteSkills = remote.skills || {};
    const localSkills = local.skills || {};
    const events = [...(Array.isArray(remoteSkills.events) ? remoteSkills.events : [])];
    const eventKeys = new Set(events.map(item => item.id || `${item.time}|${item.skill || item.type || ''}`));
    for (const item of Array.isArray(localSkills.events) ? localSkills.events : []) {
      const key = item.id || `${item.time}|${item.skill || item.type || ''}`;
      if (!eventKeys.has(key)) {
        events.push(item);
        eventKeys.add(key);
      }
    }
    events.sort((a, b) => String(a.time).localeCompare(String(b.time)));

    const goalHistory = { ...(remote.goalHistory || {}), ...(local.goalHistory || {}) };
    for (const day of new Set([
      ...Object.keys(remote.goalHistory || {}),
      ...Object.keys(local.goalHistory || {}),
    ])) {
      goalHistory[day] = Math.max(
        Number(remote.goalHistory?.[day] || 0),
        Number(local.goalHistory?.[day] || 0),
      );
    }

    return {
      ...remote,
      ...local,
      version: 1,
      attempts,
      session: null,
      goalHistory,
      skills: {
        ...remoteSkills,
        ...localSkills,
        events,
        drafts: { ...(remoteSkills.drafts || {}), ...(localSkills.drafts || {}) },
        accepted: [...new Set([
          ...(Array.isArray(remoteSkills.accepted) ? remoteSkills.accepted : []),
          ...(Array.isArray(localSkills.accepted) ? localSkills.accepted : []),
        ])],
      },
    };
  }

  async function remoteState() {
    const response = await fetch('/api/progress');
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || 'Não foi possível carregar o progresso.');
    return result.state || null;
  }

  async function saveRemoteState(state) {
    const response = await fetch('/api/progress', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ state }),
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || 'Não foi possível salvar o progresso.');
    return result.state || state;
  }

  async function flushToCloud(raw = lastQueuedValue || localStorage.getItem(KEY)) {
    if (!ready || !raw || !user) return false;
    clearTimeout(timer);
    showSync('Salvando…', 'saving');
    try {
      const localState = JSON.parse(raw);
      const state = mergeStates(await remoteState() || {}, localState);
      const savedState = await saveRemoteState(state);
      originalSetItem.call(localStorage, KEY, JSON.stringify(savedState));
      lastQueuedValue = null;
      originalRemoveItem.call(localStorage, PENDING_KEY);
      showSync('Salvo na nuvem', 'saved');
      return true;
    } catch (error) {
      originalSetItem.call(localStorage, PENDING_KEY, new Date().toISOString());
      showSync('Pendente de sincronização', 'error');
      return false;
    }
  }

  function queueSync(raw) {
    lastQueuedValue = raw;
    originalSetItem.call(localStorage, PENDING_KEY, new Date().toISOString());
    showSync('Alterações pendentes', 'pending');
    clearTimeout(timer);
    timer = setTimeout(() => flushToCloud(raw), 250);
  }

  Storage.prototype.setItem = function setItem(key, value) {
    originalSetItem.call(this, key, value);
    if (this === localStorage && key === KEY && ready) queueSync(value);
  };

  addEventListener('online', () => flushToCloud());
  addEventListener('visibilitychange', () => {
    if (localStorage.getItem(PENDING_KEY)) flushToCloud();
  });

  addEventListener('DOMContentLoaded', async () => {
    const cfg = window.ENGLISH_DAILY_CONFIG;
    if (!cfg?.supabaseUrl || !cfg?.supabaseAnonKey) {
      location.href = '/login.html';
      return;
    }

    client = window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey);
    let { data: { session } } = await client.auth.getSession();
    if (!session) {
      location.href = '/login.html';
      return;
    }
    const checked = await client.auth.getUser();
    if (checked.error) session = (await client.auth.refreshSession()).data.session;
    if (!session) {
      location.href = '/login.html';
      return;
    }
    user = session.user;

    let profile;
    try {
      const profileResponse = await fetch('/api/profile');
      const profileResult = await profileResponse.json();
      if (!profileResponse.ok || !profileResult.profile) {
        throw new Error(profileResult.error || 'Não foi possível carregar o perfil.');
      }
      profile = profileResult.profile;
    } catch (profileError) {
      location.href = '/dashboard.html';
      return;
    }
    const active = profile?.role === 'admin' || ['active', 'trialing'].includes(profile?.subscription_status);
    if (!active) {
      location.href = '/dashboard.html';
      return;
    }

    const localRaw = localStorage.getItem(KEY);
    const hasPendingLocal = Boolean(localStorage.getItem(PENDING_KEY));
    let cloudState;
    try {
      cloudState = await remoteState();
    } catch (error) {
      location.href = '/dashboard.html';
      return;
    }

    let canonicalState = null;
    if (hasPendingLocal && localRaw) {
      canonicalState = mergeStates(cloudState || {}, JSON.parse(localRaw));
      let uploaded = false;
      try {
        canonicalState = await saveRemoteState(canonicalState);
        uploaded = true;
      } catch (uploadError) {
        originalSetItem.call(localStorage, PENDING_KEY, new Date().toISOString());
      }
      if (uploaded) originalRemoveItem.call(localStorage, PENDING_KEY);
    } else if (cloudState && Object.keys(cloudState).length) {
      canonicalState = cloudState;
    } else if (localRaw) {
      canonicalState = JSON.parse(localRaw);
      try {
        canonicalState = await saveRemoteState(canonicalState);
      } catch (uploadError) {
        originalSetItem.call(localStorage, PENDING_KEY, new Date().toISOString());
      }
    }

    if (canonicalState) {
      const canonicalRaw = JSON.stringify(canonicalState);
      let localState = null;
      try {
        localState = localRaw ? JSON.parse(localRaw) : null;
      } catch (error) {
        localState = null;
      }
      if (durableJson(canonicalState) !== durableJson(localState)) {
        originalSetItem.call(localStorage, KEY, canonicalRaw);
        if (!hydrationMarked()) {
          reloadAfterHydration();
          return;
        }
      }
    }
    clearHydrationMark();

    const style = document.createElement('style');
    style.textContent = `
      .cloud-accountbar{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:12px max(22px,calc((100vw - 1320px)/2));background:var(--card);color:var(--ink);border-bottom:1px solid var(--line);box-shadow:0 4px 18px rgba(1,52,115,.06)}
      .cloud-accountbar__user{display:flex;align-items:center;gap:9px;min-width:0}
      .cloud-accountbar__avatar{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--brand);color:#fff;font-weight:800}
      .cloud-accountbar__name{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
      .cloud-accountbar__actions{display:flex;align-items:center;justify-content:flex-end;gap:12px}
      .cloud-accountbar__status{font-size:12px;color:var(--muted);white-space:nowrap}
      .cloud-accountbar__status[data-state="error"]{color:var(--bad)}
      .cloud-accountbar__link{display:inline-flex;align-items:center;justify-content:center;padding:8px 14px;border-radius:10px;background:var(--brand);color:#fff;text-decoration:none;font-weight:700;border:1px solid var(--brand)}
      .cloud-accountbar__link:hover{background:#084991;color:#fff}
      @media(max-width:600px){.cloud-accountbar{align-items:flex-start;padding:10px 14px}.cloud-accountbar__actions{flex-direction:column;align-items:flex-end;gap:5px}.cloud-accountbar__status{font-size:10px}.cloud-accountbar__link{padding:7px 11px;font-size:13px}}
    `;
    document.head.append(style);

    const bar = document.createElement('div');
    bar.className = 'cloud-accountbar';
    bar.innerHTML = `
      <div class="cloud-accountbar__user">
        <span class="cloud-accountbar__avatar" aria-hidden="true"></span>
        <span class="cloud-accountbar__name">Olá, <b></b></span>
      </div>
      <div class="cloud-accountbar__actions">
        <span class="cloud-accountbar__status" role="status">Sincronizado</span>
        <a class="cloud-accountbar__link" href="/dashboard.html">Minha conta</a>
      </div>`;
    const name = profile.full_name || user.email.split('@')[0];
    bar.querySelector('b').textContent = name;
    bar.querySelector('.cloud-accountbar__avatar').textContent = name.trim().charAt(0).toUpperCase();
    syncStatus = bar.querySelector('.cloud-accountbar__status');
    document.body.prepend(bar);

    ready = true;
    document.documentElement.dataset.cloudAuth = 'ready';
    if (localStorage.getItem(PENDING_KEY)) flushToCloud();
  });
})();

