# English Routine — guia de publicação para iniciantes

Este roteiro leva o projeto local até um pequeno lançamento comercial. Faça uma fase por vez. Não ative cobranças reais antes de concluir o teste final.

## Visão geral

Você terá cinco peças:

1. **Nome e domínio** — a identidade pública do produto.
2. **GitHub** — a cópia privada do código que alimenta a hospedagem.
3. **Cloudflare Pages** — onde o site e as funções serão hospedados.
4. **Supabase** — cadastro, login, banco e progresso dos alunos.
5. **Stripe** — assinatura mensal, cartão, recibos e cancelamento.

O aluno acessará o domínio, criará uma conta, confirmará o e-mail, pagará no Stripe e voltará ao painel. O progresso será salvo no Supabase. A chave OpenAI ficará somente nas variáveis secretas do Cloudflare.

---

## Fase 1 — validar a marca escolhida

### Nome e domínio escolhidos

O nome definido é **English Routine** e o domínio `englishroutine.com.br` já foi registrado. A busca inicial feita no INPI não encontrou marca idêntica. O domínio e a marca são registros diferentes: o domínio garante o endereço na internet, enquanto o pedido no INPI busca proteger o nome no segmento escolhido.

O pedido de marca pode ser feito depois, mas é recomendável protocolá-lo antes de cobrar assinaturas, investir em anúncios ou produzir grande volume de material. Comece avaliando a marca nominativa **English Routine** nas classes 41 (educação) e 42 (plataforma SaaS); a classe 9 pode ser relevante se houver aplicativo ou software baixável. Até a concessão, não use o símbolo `®`.

Existe também um site estrangeiro ativo chamado **My English Routine**. Isso não decide sozinho a registrabilidade da sua marca no Brasil, mas merece entrar na análise de risco, especialmente se você planejar vender fora do país. Guarde a busca do INPI e, para reduzir o risco comercial, consulte um profissional de propriedade intelectual antes do lançamento pago.

### Verificações finais

Escolha um nome que:

- seja curto e fácil de falar em português;
- possa ser escrito sem hífen, acento ou explicação;
- não limite o produto apenas à gramática;
- tenha usuário parecido disponível nas redes sociais;
- tenha domínio `.com.br` disponível;
- não seja semelhante a marca de educação já depositada no INPI.

Para validar **English Routine**, faça estas verificações:

1. Pesquise o nome exato entre aspas no Google.
2. Pesquise no Instagram, YouTube, TikTok e LinkedIn.
3. Consulte a busca de marcas do INPI, principalmente serviços de educação e software.
4. Consulte o domínio no Registro.br.
5. Guarde os resultados, comprovante do domínio e evidências das primeiras publicações.

Não conclua que um nome está juridicamente livre apenas porque o domínio está disponível. A busca do INPI e, antes de um investimento maior, uma avaliação profissional são etapas separadas.

### Estrutura recomendada do domínio

Se o público inicial é brasileiro, prefira:

```text
nomedamarca.com.br
```

Evite números, hífens, grafias difíceis e domínios que imitam concorrentes. Compre primeiro o domínio principal. Variações podem ser adicionadas depois.

### Resultado esperado

Ao terminar esta fase, você terá:

- nome **English Routine** confirmado para o projeto;
- domínio `englishroutine.com.br` registrado;
- pesquisa inicial do INPI arquivada;
- decisão tomada sobre quando protocolar a marca.

---

## Fase 2 — registrar o domínio

O domínio `englishroutine.com.br` já foi registrado no Registro.br. Nesta fase, faça apenas a conferência e proteção da conta.

Depois do registro:

1. Confirme que `englishroutine.com.br` aparece na sua conta do Registro.br.
2. Não altere o DNS imediatamente.
3. Ative autenticação em dois fatores na conta.
4. Guarde os dados de recuperação em um gerenciador de senhas.
5. Anote a data de renovação.

O DNS será apontado para o Cloudflare somente depois que a primeira versão estiver funcionando no endereço gratuito `pages.dev`.

### Resultado esperado

O domínio aparece como registrado em sua conta. Ainda é normal ele não abrir um site.

---

## Fase 3 — preparar o GitHub

Nesta fase você criará uma cópia separada do pacote SaaS. Ela será o projeto conectado ao GitHub e, posteriormente, ao Cloudflare. A versão local usada para estudar continuará em `C:\fabric-core-mcp-remote\english-practice`.

### 3.1 Confirmar o Git no computador

Abra o **PowerShell** e execute:

```powershell
git --version
```

Neste computador já foi encontrada a versão `2.51.2.windows.1`. Se o comando mostrar uma versão, continue. O GitHub CLI (`gh`) não está instalado e não será necessário neste roteiro.

### 3.2 Criar um repositório vazio no GitHub

1. Entre em [github.com](https://github.com/) com a sua conta.
2. No canto superior direito, clique no sinal **+**.
3. Clique em **New repository**.
4. Em **Owner**, mantenha sua conta pessoal.
5. Em **Repository name**, escreva exatamente `english-routine`.
6. Em **Description**, escreva `Plataforma de estudos de inglês por assinatura`.
7. Marque **Private**.
8. Não marque **Add a README file**.
9. Em **Add .gitignore**, deixe **None**.
10. Em **Choose a license**, deixe **None**.
11. Clique em **Create repository**.

O GitHub mostrará a página **Quick setup**. Não feche essa página: você copiará o endereço HTTPS dela no passo 3.6.

> O repositório deve ser criado vazio. Adicionar README, licença ou `.gitignore` nessa tela cria um histórico separado e dificulta o primeiro envio.

### 3.3 Extrair uma cópia limpa do pacote SaaS

No PowerShell, copie e execute todo o bloco abaixo:

```powershell
$pacote = 'C:\fabric-core-mcp-remote\english-practice\English-Routine-SaaS-pronto-para-publicar.zip'
$pastaPublicacao = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'English-Routine-SaaS'
Test-Path -LiteralPath $pacote
Test-Path -LiteralPath $pastaPublicacao
```

O primeiro resultado deve ser `True`. O segundo deve ser `False`. Se o segundo for `True`, já existe uma pasta com esse nome: use `English-Routine-SaaS-2` no comando abaixo para não sobrescrever nada.

Se o segundo resultado foi `False`, execute:

```powershell
Expand-Archive -LiteralPath $pacote -DestinationPath $pastaPublicacao
Set-Location -LiteralPath $pastaPublicacao
Get-ChildItem -Force
```

Você deverá ver diretamente, sem outra pasta intermediária:

```text
functions/
public/
supabase/
.dev.vars.example
.gitignore
build-saas.py
GUIA-PUBLICACAO-INICIANTE.md
README-DEPLOY.md
```

### 3.4 Confirmar que nenhum segredo será enviado

Execute dentro de `English-Routine-SaaS`:

```powershell
Get-ChildItem -Recurse -Force -File -Include '.dev.vars','.env'
```

O resultado esperado é vazio. O arquivo `.dev.vars.example` pode existir porque contém apenas nomes ilustrativos. Nunca coloque nesse arquivo chaves verdadeiras da OpenAI, Supabase ou Stripe.

Confira também as regras de proteção:

```powershell
Get-Content -LiteralPath '.gitignore'
```

Elas devem incluir `.dev.vars`, `.env`, `node_modules/` e `.wrangler/`.

### 3.5 Criar o primeiro histórico do projeto

Ainda na mesma janela do PowerShell, execute um comando por vez:

```powershell
git init
git branch -M main
git config user.name 'Raphael Costa'
git config user.email 'rarphael@gmail.com'
git add .
git status
```

No resultado de `git status`, os arquivos deverão aparecer em **Changes to be committed**. Confirme que `.dev.vars` e `.env` não aparecem. Em seguida, faça o primeiro commit:

```powershell
git commit -m 'Publica estrutura inicial do English Routine'
```

O resultado esperado contém algo parecido com `root-commit` e informa quantos arquivos foram criados.

### 3.6 Conectar a pasta ao repositório do GitHub

Na página **Quick setup** do GitHub, selecione **HTTPS** e copie o endereço. Ele terá este formato:

```text
https://github.com/SEU-USUARIO/english-routine.git
```

Substitua o endereço do exemplo abaixo pelo endereço copiado e execute:

```powershell
git remote add origin https://github.com/SEU-USUARIO/english-routine.git
git remote -v
git push -u origin main
```

No primeiro `push`, o Windows poderá abrir uma janela do navegador para autorizar o Git Credential Manager. Entre na conta correta e autorize. A senha comum da conta não funciona como senha do Git; use a autorização pelo navegador quando ela aparecer.

### 3.7 Conferir o resultado no GitHub

Atualize a página do repositório e confirme:

- o selo **Private** aparece próximo ao nome;
- as pastas `functions`, `public` e `supabase` aparecem na raiz;
- `.dev.vars.example`, `.gitignore` e os dois guias aparecem;
- não existe `.dev.vars`, `.env` nem qualquer arquivo contendo suas chaves;
- o commit `Publica estrutura inicial do English Routine` aparece no histórico.

### 3.8 Como enviar atualizações futuras

Quando os arquivos do projeto forem atualizados, substitua a cópia na pasta de publicação e então execute, dentro dela:

```powershell
git status
git add .
git commit -m 'Atualiza English Routine'
git push
```

Leia o `git status` antes de cada commit. Ele permite conferir exatamente o que será enviado.

### Erros comuns nesta fase

**`Author identity unknown`**  
Execute novamente os dois comandos `git config user.name` e `git config user.email`, depois repita o commit.

**`remote origin already exists`**  
Verifique primeiro o endereço salvo:

```powershell
git remote -v
```

Se ele já aponta para o repositório correto, pule `git remote add origin` e execute somente `git push -u origin main`.

**`Repository not found`**  
Confirme se o endereço copiado está correto, se o repositório existe na conta atual e se a janela de autorização foi concluída.

**`rejected` ou `fetch first` no primeiro push**  
Provavelmente o repositório não foi criado vazio. Como ainda é a primeira publicação, crie outro repositório privado vazio, sem README, `.gitignore` ou licença, e conecte a pasta a ele.

### Resultado esperado

Ao terminar a Fase 3, haverá um repositório privado `english-routine` com o código SaaS, nenhum segredo versionado e a branch local `main` conectada ao GitHub. A partir daí, siga para a configuração do Supabase.

---

## Fase 4 — configurar o Supabase

### 4.1 Criar o projeto

1. Entre no Supabase Dashboard.
2. Clique em **New project**.
3. Escolha a organização criada na sua conta.
4. Nome sugerido: `english-routine-producao`.
5. Crie uma senha de banco forte e guarde-a no gerenciador de senhas.
6. Escolha a região mais próxima do público brasileiro disponível no painel.
7. No desenvolvimento, o plano gratuito é suficiente. Para lançamento pago, programe a mudança para Pro.
8. Aguarde o projeto ficar disponível.

### 4.2 Criar tabelas e regras de segurança

1. No menu lateral, abra **SQL Editor**.
2. Clique em **New query**.
3. Abra localmente `supabase/migrations/001_schema.sql`.
4. Copie todo o conteúdo e cole no editor.
5. Clique em **Run**.
6. A execução deve terminar sem erro.

Confira em **Table Editor** se aparecem:

- `profiles`;
- `subscriptions`;
- `progress_snapshots`;
- `ai_daily_usage`.

### 4.3 Copiar as três informações do projeto

Abra **Project Settings → API** e localize:

- Project URL → será `SUPABASE_URL`;
- chave pública/anon → será `SUPABASE_ANON_KEY`;
- `service_role` → será `SUPABASE_SERVICE_ROLE_KEY`.

A chave pública pode ser usada pelo navegador. A `service_role` é secreta e nunca pode entrar no HTML, GitHub ou conversa.

### 4.4 Configurar login por e-mail

1. Abra **Authentication → Providers**.
2. Mantenha Email habilitado.
3. Mantenha confirmação de e-mail habilitada.
4. Quando existir uma URL `pages.dev`, abra **Authentication → URL Configuration**.
5. Em **Site URL**, informe essa URL.
6. Inclua a mesma origem nas URLs de redirecionamento permitidas.

### 4.5 Criar o administrador

Depois que o site estiver conectado ao Supabase, faça seu cadastro usando:

```text
rarphael@gmail.com
```

O banco atribuirá automaticamente o papel `admin`. Confirme em **Table Editor → profiles** se a coluna `role` mostra `admin`.

### 4.6 E-mail de produção

O e-mail padrão do Supabase é somente para testes. Antes de convidar clientes, crie uma conta em um provedor SMTP, como Resend, Brevo ou Postmark, e configure em **Authentication → Email/SMTP Settings**. Use um remetente como:

```text
conta@englishroutine.com.br
```

Configure SPF, DKIM e DMARC conforme as instruções do provedor de e-mail.

---

## Fase 5 — configurar o Stripe em modo de teste

Não ative cobranças reais nesta fase.

### 5.1 Completar o cadastro

1. Entre no Stripe Dashboard.
2. Preencha os dados do responsável, atividade e conta bancária solicitados.
3. Mantenha o painel em **modo de teste**.

### 5.2 Criar o produto

1. Abra **Product catalog → Products**.
2. Clique em **Add product**.
3. Use o nome **English Routine**.
4. Escolha preço recorrente mensal em BRL.
5. Defina o preço recorrente como **R$ 39,90 por mês**, conforme a decisão comercial do projeto.
6. Salve e copie o identificador que começa com `price_`.

Esse valor será `STRIPE_PRICE_ID`.

### 5.3 Configurar o portal do cliente

Abra as configurações do **Customer portal** e permita:

- atualizar cartão;
- consultar cobranças;
- cancelar assinatura.

### 5.4 Chaves de teste

Abra **Developers → API keys** e localize a chave secreta de teste que começa com `sk_test_`. Ela será `STRIPE_SECRET_KEY` e ficará somente no Cloudflare.

---

## Fase 6 — hospedar no Cloudflare Pages

### 6.1 Criar o projeto

1. Entre no Cloudflare Dashboard.
2. Abra **Workers & Pages**.
3. Clique em **Create application** e escolha **Pages** ou a opção de importar repositório Git.
4. Conecte o GitHub.
5. Autorize acesso apenas ao repositório privado da plataforma.
6. Selecione o repositório.

### 6.2 Configuração do build

Se o conteúdo da pasta `saas` estiver na raiz do repositório, use:

```text
Framework preset: None
Build command: deixar vazio
Build output directory: public
Root directory: /
Production branch: main
```

A pasta `functions` precisa ficar ao lado de `public`, na raiz do projeto Pages.

### 6.3 Variáveis e segredos

Antes ou logo após o primeiro deploy, abra **Settings → Variables and Secrets**. Cadastre:

| Nome | Tipo | Origem |
|---|---|---|
| `SUPABASE_URL` | variável | Project URL do Supabase |
| `SUPABASE_ANON_KEY` | variável | chave pública do Supabase |
| `SUPABASE_SERVICE_ROLE_KEY` | segredo | service role do Supabase |
| `STRIPE_SECRET_KEY` | segredo | `sk_test_...` do Stripe |
| `STRIPE_PRICE_ID` | variável | `price_...` do produto de teste |
| `OPENAI_API_KEY` | segredo | chave do projeto OpenAI para produção |
| `OPENAI_TRANSCRIBE_MODEL` | variável | `gpt-4o-mini-transcribe` |
| `AI_DAILY_LIMIT` | variável | comece com `10` |

O `STRIPE_WEBHOOK_SECRET` será incluído depois que o webhook for criado.

Faça um novo deploy após salvar as variáveis.

### 6.4 Primeira verificação

O Cloudflare fornecerá um endereço semelhante a:

```text
https://nome-do-projeto.pages.dev
```

Teste:

1. Landing page abre.
2. Botão Entrar abre o login.
3. Cadastro cria usuário.
4. E-mail de confirmação chega.
5. Login mostra o nome do aluno.
6. Conta sem pagamento permanece no dashboard, sem liberar o treino.

---

## Fase 7 — conectar o webhook Stripe

1. No Stripe, abra **Developers → Webhooks**.
2. Clique em **Add endpoint**.
3. Informe:

```text
https://SEU-PROJETO.pages.dev/api/stripe-webhook
```

4. Marque estes eventos:

```text
checkout.session.completed
customer.subscription.created
customer.subscription.updated
customer.subscription.deleted
```

5. Salve.
6. Revele e copie o segredo que começa com `whsec_`.
7. No Cloudflare, crie o segredo `STRIPE_WEBHOOK_SECRET`.
8. Faça novo deploy.

### Resultado esperado

Depois de uma compra de teste, o Stripe mostra o webhook com resposta HTTP 200 e a tabela `profiles` muda `subscription_status` para `active` ou `trialing`.

---

## Fase 8 — teste completo sem dinheiro real

Crie uma segunda conta de aluno usando outro e-mail. Faça o fluxo completo:

1. Cadastro.
2. Confirmação do e-mail.
3. Login.
4. Compra com cartão de teste indicado pelo Stripe.
5. Retorno ao dashboard.
6. Acesso ao treino.
7. Responder algumas questões.
8. Sair e entrar novamente.
9. Abrir em outro navegador e verificar o progresso.
10. Testar Speaking e conferir o limite diário.
11. Abrir o portal do cliente.
12. Cancelar a assinatura.
13. Confirmar a atualização do status.

Não avance se algum item falhar.

---

## Fase 9 — conectar o domínio

Faça isso somente depois do teste no `pages.dev`.

1. No Cloudflare Pages, abra o projeto.
2. Abra **Custom domains**.
3. Clique em **Set up a domain**.
4. Informe o domínio registrado.
5. Se o domínio está no Registro.br, siga as instruções do Cloudflare para trocar os servidores DNS.
6. Aguarde a validação e o certificado HTTPS.
7. Teste o domínio com `https://`.

Depois, atualize para `https://englishroutine.com.br`:

- **Supabase → Authentication → URL Configuration**;
- URL do webhook no Stripe;
- links públicos e e-mails;
- domínio permitido no provedor SMTP.

Mantenha temporariamente a URL `pages.dev` autorizada enquanto testa a transição.

---

## Fase 10 — identidade e páginas obrigatórias

Antes de cobrar, o rodapé precisa apresentar:

- nome empresarial ou nome do responsável;
- canal de suporte;
- Termos de Uso;
- Política de Privacidade;
- Política de Cancelamento e Reembolso;
- descrição clara do plano, valor, periodicidade e renovação.

Defina como o aluno solicita acesso, correção ou exclusão dos dados. Consulte contador sobre formalização, atividade, tributação e emissão fiscal. Faça revisão jurídica dos documentos antes do lançamento público.

---

## Fase 11 — ativar produção

Somente depois de todos os testes:

1. Ative a conta Stripe para pagamentos reais.
2. Crie no modo real o produto e preço.
3. Troque `STRIPE_SECRET_KEY` por `sk_live_...`.
4. Troque `STRIPE_PRICE_ID` pelo preço real.
5. Crie outro webhook no modo real e troque `STRIPE_WEBHOOK_SECRET`.
6. Faça uma assinatura real de baixo risco com uma conta de teste controlada por você.
7. Confira cobrança, acesso, cancelamento e eventual estorno.
8. Convide inicialmente de 5 a 10 alunos conhecidos.
9. Monitore erros e custos por uma semana antes de anunciar amplamente.

---

## Checklist de segurança

- MFA ativado em GitHub, Cloudflare, Supabase, Stripe e OpenAI.
- Repositório privado.
- Nenhum segredo dentro do GitHub ou HTML.
- `service_role` somente no Cloudflare.
- RLS habilitado nas tabelas Supabase.
- SMTP próprio antes de aceitar clientes.
- Limite diário da IA configurado.
- Alertas de gasto na OpenAI e Stripe revisados.
- Backup do banco e procedimento de restauração definidos.
- Canal para direitos do titular e suporte publicado.

## Ordem prática recomendada

Para evitar gastos e retrabalho, siga exatamente esta ordem:

```text
Domínio registrado → guardar pesquisa INPI → GitHub → Supabase → Stripe teste
→ Cloudflare pages.dev → webhook → teste completo → documentos
→ conectar englishroutine.com.br → pedido de marca antes da divulgação comercial
→ Stripe real → grupo piloto → lançamento
```

