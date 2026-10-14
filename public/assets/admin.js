(async () => {
  const cfg = window.ENGLISH_DAILY_CONFIG;
  const client = window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey);
  const { data: { session } } = await client.auth.getSession();
  if (!session) {
    location.href = '/login.html';
    return;
  }

  const $ = selector => document.querySelector(selector);
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const date = value => new Date(value).toLocaleDateString('pt-BR');
  let users = [];
  let grants = [];

  async function api(path, options = {}) {
    const token = (await client.auth.getSession()).data.session?.access_token;
    const response = await fetch(path, {
      ...options,
      headers: { ...(options.headers || {}), Authorization: `Bearer ${token}` },
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || 'Falha na requisição.');
    return result;
  }

  function grantActive(grant) {
    return !grant.expires_at || Date.parse(grant.expires_at) > Date.now();
  }

  function render() {
    const byEmail = new Map(grants.map(grant => [grant.email, grant]));
    const emails = new Set(users.map(user => String(user.email).toLowerCase()));
    $('#grants').innerHTML = grants.length
      ? grants.map(grant => `<tr>
          <td>${esc(grant.email)}</td>
          <td>${grant.expires_at ? `${grantActive(grant) ? 'até' : 'expirou em'} ${date(grant.expires_at)}` : 'Sem prazo'}</td>
          <td>${esc(grant.note)}</td>
          <td>${emails.has(grant.email) ? 'Criada' : 'Aguardando cadastro'}</td>
          <td><button class="link-button" data-revoke="${esc(grant.email)}">Revogar</button></td>
        </tr>`).join('')
      : '<tr><td colspan="5" class="muted">Nenhuma cortesia concedida.</td></tr>';
    $('#users').innerHTML = users.map(user => {
      const grant = byEmail.get(String(user.email).toLowerCase());
      const status = grant && grantActive(grant) && !['active', 'trialing'].includes(user.subscription_status)
        ? 'cortesia'
        : user.subscription_status;
      return `<tr><td>${esc(user.full_name)}</td><td>${esc(user.email)}</td><td>${esc(status)}</td><td>${date(user.created_at)}</td></tr>`;
    }).join('');
  }

  $('#grants').onclick = async event => {
    const email = event.target.dataset?.revoke;
    if (!email || !confirm(`Revogar o acesso de cortesia de ${email}?`)) return;
    try {
      grants = (await api(`/api/admin/grants?email=${encodeURIComponent(email)}`, { method: 'DELETE' })).grants;
      $('#grantStatus').textContent = `Cortesia de ${email} revogada.`;
      render();
    } catch (error) {
      $('#grantStatus').textContent = error.message;
    }
  };

  $('#grantForm').onsubmit = async event => {
    event.preventDefault();
    const button = $('#grantSubmit');
    button.disabled = true;
    try {
      const email = $('#grantEmail').value.trim().toLowerCase();
      grants = (await api('/api/admin/grants', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, expires_at: $('#grantExpires').value || null, note: $('#grantNote').value }),
      })).grants;
      $('#grantStatus').textContent = `Cortesia concedida a ${email}.`;
      event.target.reset();
      render();
    } catch (error) {
      $('#grantStatus').textContent = error.message;
    } finally {
      button.disabled = false;
    }
  };

  const { data, error } = await client.from('admin_user_overview').select('*').order('created_at', { ascending: false });
  if (error) {
    $('#status').textContent = 'Acesso negado ou falha ao carregar.';
    return;
  }
  users = data;
  try {
    grants = (await api('/api/admin/grants')).grants;
  } catch (grantError) {
    $('#grantStatus').textContent = grantError.message;
  }
  render();
})();
