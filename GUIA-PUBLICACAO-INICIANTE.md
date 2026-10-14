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

### 4.1 Criar a organização

Se sua conta é nova, o Supabase mostra primeiro **Create a new organization**. A organização é a pasta administrativa que agrupa projetos, membros e cobrança; ela não é o banco de dados.

Preencha assim:

| Campo | Valor recomendado |
|---|---|
| **Name** | `English Routine` |
| **Type** | `Personal` |
| **Plan** | `Free — $0/month` |

Use `English Routine` na organização e reserve `english-routine-producao` para o projeto da próxima tela. Se já escreveu `english-routine-producao` como nome da organização, isso não causa erro técnico, mas vale corrigir agora para os dois níveis ficarem fáceis de identificar.

Clique em **Create organization**. O plano Free não solicita cobrança mensal nessa etapa. A assinatura do Supabase é definida por organização, por isso todos os projetos criados dentro dela usarão inicialmente esse plano.

### 4.2 Criar o projeto

Depois de criar a organização, o Supabase mostrará a criação do primeiro projeto. Se isso não acontecer automaticamente, abra a organização **English Routine** e clique em **New project**.

1. Em **Organization**, escolha `English Routine`.
2. Em **GitHub (optional)**, não clique em **Connect GitHub** agora. O repositório será conectado ao Cloudflare na Fase 6; esta integração opcional do Supabase não é necessária para nossa migração manual.
3. Em **Project name**, apague o nome automático e escreva `english-routine-producao`.
4. Em **Database password**, clique em **Generate a password**, copie a senha e guarde-a imediatamente no gerenciador de senhas. Não envie essa senha pelo chat, não tire captura dela e não coloque no GitHub.
5. Em **Region**, abra `Americas` e escolha **South America / São Paulo** se estiver disponível; caso contrário, escolha a região geograficamente mais próxima do público brasileiro.
6. Em **Security**, deixe **Enable Data API** marcado.
7. Deixe **Automatically expose new tables** desmarcado. O script do projeto controla explicitamente as permissões.
8. Deixe **Enable automatic RLS** desmarcado nesta tela. A migração `001_schema.sql` habilita RLS individualmente nas quatro tabelas e cria as políticas necessárias.
9. Deixe **Advanced configuration** fechado e mantenha os valores padrão.
10. Não ative **High availability**, add-ons pagos ou recursos experimentais.
11. Clique em **Create new project**.
12. Aguarde o status indicar que o projeto está pronto. A criação do banco pode levar alguns minutos.

Resumo da tela:

| Campo | Configuração |
|---|---|
| Organization | `English Routine` |
| GitHub | Não conectar agora |
| Project name | `english-routine-producao` |
| Database password | Gerar e guardar com segurança |
| Region | São Paulo, se disponível |
| Enable Data API | Marcado |
| Automatically expose new tables | Desmarcado |
| Enable automatic RLS | Desmarcado; será configurado pelo SQL |
| Advanced configuration | Não alterar |

O topo do painel deverá mostrar algo semelhante a `English Routine / english-routine-producao`.

### 4.3 Criar tabelas e regras de segurança

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

### 4.4 Copiar as três informações do projeto

O Supabase atual usa chaves **Publishable** e **Secret**. Não use a aba **Legacy anon, service_role API keys**; essas chaves antigas estão sendo descontinuadas.

#### 4.4.1 Copiar a Publishable key

1. Abra **Settings → API Keys**.
2. Mantenha selecionada a aba **Publishable and secret API keys**.
3. Na seção **Publishable key**, localize a linha `default`.
4. Clique no ícone de copiar, à direita da chave que começa com `sb_publishable_`.
5. Guarde com o nome `SUPABASE_PUBLISHABLE_KEY`.

Essa chave é feita para uso no navegador. Ela só é segura porque o banco terá RLS e políticas; mesmo assim, não há necessidade de colá-la em conversas ou capturas.

#### 4.4.2 Copiar a Secret key

1. Na mesma página, desça até **Secret keys**.
2. Na linha `default`, clique diretamente no ícone de copiar. Não é necessário revelar a chave na tela.
3. Guarde com o nome `SUPABASE_SECRET_KEY`.

A Secret key começa com `sb_secret_`, concede acesso privilegiado e deve ficar somente nos segredos do Cloudflare. Nunca coloque essa chave no HTML, no GitHub, em capturas de tela ou em mensagens.

#### 4.4.3 Copiar a URL do projeto

1. No menu esquerdo, em **Integrations**, clique em **Data API**.
2. Localize **Project URL** ou **API URL**. Ela tem o formato `https://xxxxxxxx.supabase.co`.
3. Copie somente a URL base, sem acrescentar `/rest/v1`.
4. Guarde com o nome `SUPABASE_URL`.

Outra opção é clicar no botão verde **Connect**, no topo do painel; ele também mostra a URL e a Publishable key. Para conferir todas as chaves, continue usando **Settings → API Keys**.

Ao terminar, você terá três valores guardados localmente:

| Variável futura no Cloudflare | Começa ou se parece com | Pode ir ao navegador? |
|---|---|---|
| `SUPABASE_URL` | `https://...supabase.co` | Sim |
| `SUPABASE_PUBLISHABLE_KEY` | `sb_publishable_...` | Sim |
| `SUPABASE_SECRET_KEY` | `sb_secret_...` | Não, segredo do servidor |

Não crie chaves adicionais agora e não desative as chaves `default`.

### 4.5 Configurar login por e-mail

Na interface atual do Supabase, você começa exatamente na tela mostrada na imagem: **Authentication → Users**. A mensagem **No users in your project** é normal; ela apenas informa que ninguém se cadastrou ainda.

#### 4.5.1 Ativar o acesso por e-mail e senha

1. No menu esquerdo, localize o grupo **Configuration**.
2. Clique em **Sign In / Providers**.
3. Na lista de provedores, localize **Email** e abra o cartão.
4. Deixe **Enable Email provider** ativado.
5. Deixe **Allow new users to sign up** ativado, caso essa opção apareça no cartão.
6. Deixe **Confirm Email** ativado. Assim, o aluno precisa confirmar o endereço recebido por e-mail antes de entrar.
7. Mantenha as demais opções de e-mail nos valores padrão por enquanto.
8. Clique em **Save**.

Não habilite telefone, login anônimo, Google ou outros provedores nesta etapa. Eles poderão ser adicionados depois, sem impedir o funcionamento do login por e-mail.

#### 4.5.2 Configurar os endereços de retorno

No mesmo menu esquerdo, existe a opção **URL Configuration**. Como o endereço público do Cloudflare Pages ainda será criado na fase 6, não invente uma URL e não use `127.0.0.1:8765`: esse endereço pertence somente ao servidor local do seu computador.

Por enquanto, deixe essa tela como está e prossiga para o passo 4.6. Depois do primeiro deploy no Cloudflare Pages, volte aqui e preencha:

1. **Site URL:** `https://english-routine-760.pages.dev`.
2. **Redirect URLs:** adicione `https://english-routine-760.pages.dev/login.html`.
3. Clique em **Save**.

Quando o domínio definitivo estiver conectado, o guia voltará a esta configuração para cadastrar `https://englishroutine.com.br` e `https://englishroutine.com.br/login.html`.

### 4.6 Criar o administrador

Você pode criar sua conta administrativa agora, diretamente pelo painel do Supabase. Não é necessário esperar a publicação do site.

1. No menu esquerdo, abra **Authentication → Users**.
2. No canto superior direito, clique em **Add user**.
3. Escolha **Create new user**. Não selecione **Send invitation** nesta etapa.
4. No campo de e-mail, informe:

```text
rarphael@gmail.com
```

5. Crie uma senha forte e exclusiva. Guarde-a no seu gerenciador de senhas e não a envie pelo chat.
6. Se aparecer **Auto Confirm User**, deixe essa opção ativada. Como a conta está sendo criada por você no painel administrativo, ela poderá entrar sem aguardar o e-mail de confirmação.
7. Clique em **Create user**.
8. Aguarde a nova linha aparecer em **Authentication → Users**.

O arquivo `001_schema.sql`, executado no passo 4.3, contém um gatilho que reconhece esse endereço de e-mail e atribui automaticamente o papel `admin`.

#### 4.6.1 Conferir o perfil administrativo

1. No menu principal esquerdo do Supabase, abra **Table Editor**.
2. Selecione a tabela **profiles**.
3. Localize a linha cujo campo `email` é `rarphael@gmail.com`.
4. Confirme que a coluna `role` contém `admin`.
5. Se `full_name` estiver vazio, edite somente essa coluna e informe `Raphael Costa`.
6. Salve a alteração.

O resultado correto é:

| Coluna | Valor esperado |
|---|---|
| `email` | `rarphael@gmail.com` |
| `full_name` | `Raphael Costa` |
| `role` | `admin` |
| `subscription_status` | `inactive` |

O status `inactive` é normal para o administrador. O código do site libera o acesso administrativo pela coluna `role`, sem exigir que o administrador compre uma assinatura.

Se o usuário aparecer em **Authentication → Users**, mas não existir uma linha correspondente em **Table Editor → profiles**, não crie a linha manualmente. Isso indica que o esquema ou o gatilho do passo 4.3 não foi instalado corretamente e precisa ser verificado antes de continuar.

### 4.7 E-mail de produção

O e-mail padrão do Supabase serve apenas para testes limitados. O English Routine usará o **Resend** como provedor SMTP para enviar confirmação de cadastro, recuperação de senha e outras mensagens de autenticação.

#### 4.7.1 O que fazer agora

1. Acesse o Resend e crie sua conta.
2. Você pode usar **Continue with Google**. Isso serve somente para entrar no painel administrativo do Resend e não ativa login com Google para os alunos do English Routine.
3. Se o Resend pedir o nome da equipe, use `English Routine`.
4. Permaneça no plano gratuito durante a implantação e os testes.
5. Pare esta configuração quando chegar à tela inicial do Resend.

Não adicione os registros DNS no Registro.br agora. O domínio será conectado ao Cloudflare nas fases seguintes; inserir os registros antes dessa mudança faria você repetir a configuração.

Pode prosseguir para a fase 5. Retorne aos passos abaixo depois que o domínio `englishroutine.com.br` estiver ativo no Cloudflare.

#### 4.7.2 Verificar o domínio no Resend — executar depois da configuração do Cloudflare

1. No Resend, abra **Domains**.
2. Clique em **Add Domain**.
3. Informe `englishroutine.com.br`.
4. Mantenha habilitada a capacidade de envio de e-mails.
5. O Resend mostrará registros DNS, normalmente DKIM, SPF e MX. Não copie valores de exemplos do guia: use exatamente os nomes, tipos e valores exibidos na sua conta.
6. Abra o painel do Cloudflare em **DNS → Records** para `englishroutine.com.br`.
7. Crie cada registro mostrado pelo Resend. Nos registros usados para e-mail, mantenha **Proxy status** como **DNS only**, quando essa opção existir.
8. Volte ao Resend e clique em **Verify** ou **I've added the records**.
9. Aguarde todos os itens de envio ficarem como **Verified**. A propagação pode levar alguns minutos ou mais.

#### 4.7.3 Criar a credencial SMTP — executar após o domínio ficar Verified

1. No Resend, abra **API Keys**.
2. Clique em **Create API Key**.
3. Use o nome `Supabase Auth - English Routine`.
4. Conceda apenas permissão de envio, se o painel oferecer níveis de permissão.
5. Copie a chave exibida uma única vez e guarde-a no gerenciador de senhas. Não a envie pelo chat nem a salve no GitHub.

No Supabase, abra a configuração de SMTP do projeto dentro de **Authentication**. Na interface atual, ela pode aparecer dentro de **Emails** ou como **SMTP Settings**. Ative o SMTP personalizado e preencha:

| Campo | Valor |
|---|---|
| **Sender email** | `conta@englishroutine.com.br` |
| **Sender name** | `English Routine` |
| **Host** | `smtp.resend.com` |
| **Port** | `465` |
| **Username** | `resend` |
| **Password** | a API Key criada no Resend |

Salve a configuração. A senha SMTP é a chave do Resend e deve permanecer somente no painel protegido do Supabase.

O remetente usado nas mensagens será:

```text
conta@englishroutine.com.br
```

Depois, faça um cadastro de teste com outro endereço e confirme se a mensagem aparece em **Emails** no Resend. Configure DMARC antes de abrir o cadastro ao público; o próprio Resend indicará o registro recomendado para o domínio.

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

Você está na **Área restrita**, que é o ambiente de teste correto. A faixa azul informa que nenhuma alteração dessa área afeta clientes ou pagamentos reais.

Na interface atual do Stripe, use qualquer um destes caminhos:

**Caminho principal pela tela mostrada:**

1. Na seção **Configurações do produto**, clique em **Faturamento**.
2. Procure **Portal do cliente** ou **Customer portal**.
3. Abra a configuração do portal.

**Caminho pelo menu esquerdo:**

1. Clique na seta ao lado de **Billing** para expandir o menu.
2. Procure **Portal do cliente** ou **Customer portal**.

**Atalho direto no ambiente de teste:**

```text
https://dashboard.stripe.com/test/settings/billing/portal
```

Quando a página do portal abrir, configure assim:

| Opção | Configuração recomendada |
|---|---|
| Atualização de formas de pagamento | Ativada |
| Histórico de faturas | Ativado |
| Cancelamento de assinatura | Ativado |
| Momento do cancelamento | Ao final do período de cobrança |
| Motivo do cancelamento | Ativado |
| Troca de plano | Desativada por enquanto |
| Alteração de quantidade | Desativada |
| Códigos promocionais | Desativados por enquanto |

O English Routine possui apenas um plano mensal, então troca de plano e quantidade não são necessárias.

Se a tela exigir um **link de retorno padrão**, deixe-o vazio por enquanto. Depois do primeiro deploy, use:

```text
https://english-routine-760.pages.dev/dashboard.html
```

Quando o domínio definitivo estiver ativo, esse endereço será substituído por:

```text
https://englishroutine.com.br/dashboard.html
```

Clique em **Salvar alterações**. Continue trabalhando na Área restrita; não clique em **Alternar para a conta de produção** nesta fase.

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

Na tela **Configurar compilações e implantações**, preencha exatamente assim:

| Campo mostrado pelo Cloudflare | Valor |
|---|---|
| **Nome do projeto** | `english-routine` |
| **Ramificação de produção** | `main` |
| **Predefinição da estrutura** | `Nenhum` |
| **Comando da build** | deixe completamente vazio |
| **Diretório de saída da build** | `public` |
| **Diretório raiz (avançado) → Caminho** | deixe completamente vazio |

No campo de saída, digite somente `public`, sem barra inicial e sem usar `saas/public`. O caminho raiz fica vazio porque as pastas `functions`, `public` e `supabase` já estão diretamente na raiz do repositório GitHub.

Não adicione variáveis de ambiente nessa tela ainda. Elas serão cadastradas com os tipos corretos no passo 6.3, depois que o projeto Pages existir.

Revise os campos e clique em **Salvar e implantar** ou no botão equivalente exibido no final da página.

Para este projeto, o Cloudflare reservou o endereço:

```text
https://english-routine-760.pages.dev
```

A pasta `functions` precisa ficar ao lado de `public`, na raiz do projeto Pages.

### 6.3 Variáveis e segredos

A tela **Configurações** mostrada na imagem é a configuração geral da conta Cloudflare. As variáveis ficam dentro do projeto Pages, não nessa tela.

Para chegar ao lugar correto:

1. Clique em **Página inicial da conta** no menu esquerdo.
2. Abra **Computação**.
3. Entre em **Workers & Pages**.
4. Selecione o projeto **english-routine**.
5. Abra a guia **Configurações** do projeto.
6. Entre em **Variáveis e segredos**.
7. Clique em **Adicionar**.

Cadastre uma entrada por vez. Use **Texto simples/Variable** para os valores públicos de configuração e marque **Criptografar/Encrypt/Secret** para chaves privadas:

| Nome | Tipo | Origem |
|---|---|---|
| `SUPABASE_URL` | variável | Project URL do Supabase |
| `SUPABASE_PUBLISHABLE_KEY` | variável | Publishable key `sb_publishable_...` do Supabase |
| `SUPABASE_SECRET_KEY` | segredo | Secret key `sb_secret_...` do Supabase |
| `STRIPE_SECRET_KEY` | segredo | `sk_test_...` do Stripe |
| `STRIPE_PRICE_ID` | variável | `price_...` do produto de teste |
| `OPENAI_API_KEY` | segredo | chave do projeto OpenAI para produção |
| `OPENAI_TRANSCRIBE_MODEL` | variável | `gpt-4o-mini-transcribe` |
| `AI_DAILY_LIMIT` | variável | comece com `10` |

O `STRIPE_WEBHOOK_SECRET` será incluído depois que o webhook for criado.

Para cada item:

1. informe exatamente o nome da primeira coluna;
2. cole o valor correspondente sem aspas e sem espaços extras;
3. selecione **Produção** e, se houver essa escolha, também **Visualizações/Preview**;
4. marque **Criptografar** nos itens classificados como segredo;
5. clique em **Salvar**.

Não envie os valores secretos pelo chat e não os coloque no GitHub. Se precisar interromper a configuração, pode sair do painel: o projeto e a primeira implantação permanecem salvos. Ao retornar, recomece pelo caminho **Computação → Workers & Pages → english-routine → Configurações → Variáveis e segredos**.

Faça um novo deploy após salvar as variáveis.

### 6.4 Primeira verificação

O Cloudflare fornecerá um endereço semelhante a:

```text
https://english-routine-760.pages.dev
```

Teste:

1. Landing page abre.
2. Botão Entrar abre o login.
3. Cadastro cria usuário.
4. E-mail de confirmação chega.
5. Login mostra o nome do aluno.
6. Conta sem pagamento permanece no dashboard, sem liberar o treino.

Se a tela de login mostrar **Ambiente ainda não configurado**, o arquivo de configuração pública não foi carregado. Verifique nesta ordem:

1. confirme no projeto Cloudflare que `SUPABASE_URL` e `SUPABASE_PUBLISHABLE_KEY` estão salvas em **Variáveis e segredos**;
2. faça uma nova implantação depois de salvar as variáveis;
3. abra `https://english-routine-760.pages.dev/login` em uma nova aba e recarregue;
4. se a mensagem continuar, confirme que o repositório contém `functions/config.js.js`, compatibilidade necessária para a rota `/config.js` usada pela primeira versão publicada.

Em 14/10/2026, essa rota de compatibilidade foi adicionada ao repositório e a tela publicada foi validada sem a mensagem de ambiente não configurado.

Se o login funcionar, mas o painel mostrar **Não foi possível carregar seu perfil**, isso não significa que o histórico foi apagado. A autenticação existe, porém a linha da tabela `profiles` está ausente ou inacessível. A versão atual tenta reparar automaticamente o perfil autenticado pela rota protegida `/api/profile`. Depois da nova implantação, saia, entre novamente e pressione `Ctrl + F5`. Como conferência manual, execute `supabase/migrations/002_repair_existing_profiles.sql` no **SQL Editor** do Supabase; a migração é idempotente e não altera `progress_snapshots`.

O painel também possui **Importar histórico antigo**. Selecione o arquivo JSON exportado na versão local ou cole o conteúdo do backup. A plataforma lê primeiro o histórico já salvo na nuvem e combina respostas e treinos sem duplicar registros; ela não substitui silenciosamente o progresso online. Depois da confirmação, abra **Começar treino** para conferir os totais.

Dentro do treino, a barra superior mostra o estado da nuvem: **Alterações pendentes**, **Salvando…**, **Salvo na nuvem** ou **Pendente de sincronização**. Cada gravação lê primeiro o snapshot online e combina respostas e habilidades antes de enviar. Se a internet cair ou a aba for fechada durante o envio, um marcador local mantém a pendência e o sistema tenta novamente na próxima abertura, sem substituir respostas existentes na nuvem.

Se aparecer `permission denied for table profiles` ou `permission denied for table progress_snapshots`, abra o **SQL Editor** do Supabase, cole todo o conteúdo de `supabase/migrations/003_grant_application_permissions.sql` e clique em **Run**. RLS e privilégios SQL são camadas diferentes: a migração 001 já restringe cada aluno ao próprio registro, enquanto a migração 003 autoriza os papéis da aplicação a acessar essas tabelas sob essas regras. O script não apaga nem modifica histórico e pode ser executado novamente sem risco.

---

## Fase 7 — conectar o webhook Stripe

Na interface atual, o Stripe chama o webhook de **destino de eventos**. Continue na **Área restrita**, pois esta fase ainda usa pagamentos de teste.

### 7.1 Escolher escopo e formato

Na tela **Configure o destino dos seus eventos**, selecione:

| Campo | Escolha |
|---|---|
| **Escopo do destino de eventos** | **Sua conta** |
| **Estilo do conteúdo** | **Instantâneo** |
| **Versão da API** | mantenha a versão já selecionada pelo Stripe |

Não escolha **Contas conectadas**: o English Routine não usa Stripe Connect. Não escolha **Mínimo**: o webhook atual lê `event.data.object`, que está presente no payload instantâneo. Eventos v1 de snapshot incluem uma representação versionada do objeto; eventos thin/mínimos exigiriam buscar o objeto separadamente. [Documentação oficial do Stripe sobre versionamento e eventos](https://docs.stripe.com/api/versioning).

### 7.2 Selecionar somente quatro eventos

Não percorra todas as categorias mostradas nas imagens e não use **Selecionar tudo**. Use a caixa **Encontre o evento por nome ou descrição** e pesquise um nome por vez. Marque exatamente:

```text
checkout.session.completed
customer.subscription.created
customer.subscription.updated
customer.subscription.deleted
```

Procedimento:

1. Pesquise `checkout.session.completed` e marque a caixa desse evento.
2. Apague a pesquisa.
3. Pesquise `customer.subscription.created` e marque.
4. Repita para `customer.subscription.updated`.
5. Repita para `customer.subscription.deleted`.
6. Abra a guia **Eventos selecionados** e confirme que o contador mostra **4**.
7. Clique em **Continuar**.

O evento de Checkout confirma a conclusão da sessão de pagamento; os três eventos de assinatura mantêm o acesso atualizado quando a assinatura é criada, alterada ou cancelada. [Tipos de eventos do Stripe](https://docs.stripe.com/api/events/types) · [Checkout e `checkout.session.completed`](https://docs.stripe.com/payments/existing-customers?platform=web&ui=stripe-hosted).

### 7.3 Escolher o destino

Na etapa **Escolher tipo de destino**:

1. Escolha **Endpoint de webhook** ou **Webhook endpoint**.
2. Não escolha Amazon EventBridge.
3. Clique em **Continuar**.

### 7.4 Configurar o endpoint

Na etapa **Configure o destino**, informe a URL completa:

```text
https://english-routine-760.pages.dev/api/stripe-webhook
```

Se houver os campos opcionais:

| Campo | Valor sugerido |
|---|---|
| **Nome** | `English Routine - teste` |
| **Descrição** | `Assinaturas de teste do English Routine` |

Revise o resumo: **Sua conta**, **Instantâneo**, quatro eventos e a URL terminada em `/api/stripe-webhook`. Depois clique em **Criar destino**.

### 7.5 Guardar o segredo de assinatura

Depois de criar o destino:

1. Abra os detalhes do destino.
2. Localize **Signing secret** ou **Segredo de assinatura**.
3. Clique em **Reveal** apenas no seu computador.
4. Copie o valor que começa com `whsec_`.
5. Não envie esse valor pelo chat e não o coloque no GitHub.

### 7.6 Cadastrar o segredo no Cloudflare

1. Abra **Cloudflare → Computação → Workers & Pages → english-routine**.
2. Entre em **Configurações → Variáveis e segredos**.
3. Adicione:

```text
Nome: STRIPE_WEBHOOK_SECRET
Valor: whsec_... copiado do Stripe
Tipo: segredo / criptografado
Ambiente: Produção
```

4. Salve.
5. Faça uma nova implantação do projeto Pages para garantir que a função receba o segredo.

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


