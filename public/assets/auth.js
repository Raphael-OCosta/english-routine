(() => {
  const cfg = window.ENGLISH_DAILY_CONFIG;
  const status = document.querySelector('#status');
  if (!cfg?.supabaseUrl || !cfg?.supabaseAnonKey) {
    status.textContent = 'Ambiente ainda não configurado.';
    return;
  }

  const client = window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey);
  const form = document.querySelector('#authForm');
  const toggle = document.querySelector('#toggle');
  const forgot = document.querySelector('#forgot');
  const nameField = document.querySelector('#nameField');
  const email = document.querySelector('#email');
  const password = document.querySelector('#password');
  const emailField = email.closest('.field');
  const passwordLabel = document.querySelector('label[for="password"]');

  let signup = new URLSearchParams(location.search).get('mode') === 'signup';
  // The reset link returns with type=recovery; the session it creates must
  // only be used to set a new password, never to skip straight to the app.
  let recovery = /type=recovery/.test(location.hash) || /type=recovery/.test(location.search);

  function paint() {
    const mode = recovery ? 'recovery' : signup ? 'signup' : 'login';
    document.querySelector('#title').textContent = { recovery: 'Nova senha', signup: 'Criar conta', login: 'Entrar' }[mode];
    document.querySelector('#subtitle').textContent = {
      recovery: 'Escolha uma nova senha com pelo menos 8 caracteres.',
      signup: 'Comece sua rotina de inglês.',
      login: 'Continue sua evolução.',
    }[mode];
    document.querySelector('#submit').textContent = { recovery: 'Salvar nova senha', signup: 'Criar conta', login: 'Entrar' }[mode];
    toggle.textContent = signup ? 'Já tenho uma conta' : 'Ainda não tenho conta';
    nameField.hidden = mode !== 'signup';
    emailField.hidden = recovery;
    email.required = !recovery;
    toggle.hidden = recovery;
    forgot.hidden = recovery;
    if (passwordLabel) passwordLabel.textContent = recovery ? 'Nova senha' : 'Senha';
    password.autocomplete = mode === 'login' ? 'current-password' : 'new-password';
  }
  paint();

  toggle.onclick = event => {
    event.preventDefault();
    signup = !signup;
    status.textContent = '';
    paint();
  };

  client.auth.onAuthStateChange(event => {
    if (event === 'PASSWORD_RECOVERY') {
      recovery = true;
      status.textContent = '';
      paint();
    }
  });

  form.onsubmit = async event => {
    event.preventDefault();
    status.textContent = 'Aguarde…';

    if (recovery) {
      if (password.value.length < 8) {
        status.textContent = 'A senha precisa ter pelo menos 8 caracteres.';
        return;
      }
      const { error } = await client.auth.updateUser({ password: password.value });
      if (error) {
        status.textContent = error.message;
        return;
      }
      status.textContent = 'Senha atualizada. Entrando…';
      history.replaceState(null, '', '/login.html');
      location.href = '/dashboard.html';
      return;
    }

    const address = email.value.trim();
    const name = document.querySelector('#name').value.trim();
    const result = signup
      ? await client.auth.signUp({
        email: address,
        password: password.value,
        options: { data: { name }, emailRedirectTo: `${location.origin}/login.html` },
      })
      : await client.auth.signInWithPassword({ email: address, password: password.value });
    if (result.error) {
      status.textContent = result.error.message;
      return;
    }
    status.textContent = signup && !result.data.session
      ? 'Confira seu e-mail para confirmar o cadastro.'
      : 'Login realizado.';
    if (result.data.session) location.href = '/dashboard.html';
  };

  forgot.onclick = async event => {
    event.preventDefault();
    const address = email.value.trim();
    if (!address) {
      status.textContent = 'Informe seu e-mail primeiro.';
      return;
    }
    const { error } = await client.auth.resetPasswordForEmail(address, { redirectTo: `${location.origin}/login.html` });
    status.textContent = error ? error.message : 'Enviamos as instruções para redefinir sua senha.';
  };

  client.auth.getSession().then(({ data }) => {
    if (data.session && !recovery) location.href = '/dashboard.html';
  });
})();
