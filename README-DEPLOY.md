# English Routine SaaS — implantação

> Primeira publicação? Siga antes o roteiro detalhado em `GUIA-PUBLICACAO-INICIANTE.md`.

Arquitetura escolhida para o MVP comercial:

- **Cloudflare Pages + Functions**: landing page, app e endpoints de pagamento.
- **Supabase**: login por e-mail/senha, PostgreSQL, progresso por usuário e RLS.
- **Stripe Checkout + Billing Portal**: assinatura mensal e cancelamento.
- **OpenAI**: manter apenas onde houver recurso de IA; a chave deve ficar no servidor.

## O que já está pronto

- Landing page responsiva.
- Cadastro, login, confirmação de e-mail e recuperação de senha.
- Dashboard com nome do aluno e status da assinatura.
- Acesso do administrador para `rarphael@gmail.com`.
- Checkout recorrente, portal de cobrança e webhook da Stripe.
- Banco com perfis, assinaturas e progresso sincronizado por usuário.
- Row Level Security: cada aluno lê e altera somente o próprio progresso.
- Build que incorpora o treino atual em `public/app.html`.

## Contas que Raphael precisa criar

1. Cloudflare: https://dash.cloudflare.com/sign-up
2. Supabase: https://supabase.com/dashboard
3. Stripe Brasil: https://dashboard.stripe.com/register
4. Domínio registrado: `englishroutine.com.br`.

Não envie senhas, chaves secretas ou códigos de recuperação pelo chat. Use convites de equipe ou configure os segredos diretamente nos painéis.

## 1. Supabase

1. Crie um projeto na região mais próxima dos alunos.
2. Abra **SQL Editor**, cole e execute `supabase/migrations/001_schema.sql`.
3. Em **Authentication → URL Configuration**, informe a URL pública do site e os redirects de login.
4. Em **Authentication → Email**, mantenha confirmação de e-mail habilitada.
5. Antes do lançamento, configure SMTP próprio; o serviço de teste do Supabase tem limite baixo.
6. Copie `Project URL` e a chave pública `anon`. A `service_role` é segredo exclusivo do servidor.
7. Crie primeiro a conta `rarphael@gmail.com`; o trigger atribui `role=admin` automaticamente.

## 2. Stripe

1. Complete o cadastro empresarial, bancário e fiscal.
2. Crie o produto **English Routine** e um preço mensal recorrente de **R$ 39,90**.
3. Copie o `price_...` criado.
4. Ative o **Customer Portal** com cancelamento e atualização do cartão.
5. Quando conectar o domínio ao Cloudflare, crie um webhook para `https://englishroutine.com.br/api/stripe-webhook`.
6. Assine os eventos:
   - `checkout.session.completed`
   - `customer.subscription.created`
   - `customer.subscription.updated`
   - `customer.subscription.deleted`
7. Copie o segredo `whsec_...`.
8. Faça tudo primeiro no modo de teste. Mude para chaves live apenas depois do teste completo.

## 3. Gerar a aplicação

Na pasta `english-practice`:

```powershell
python build.py
python saas\build-saas.py
```

O diretório publicável será `saas/public` e as Functions ficam em `saas/functions`.

## 4. Cloudflare Pages

1. Crie um projeto Pages ligado ao repositório Git.
2. Root directory: `english-practice/saas`.
3. Build command: `python ../build.py && python build-saas.py`.
4. Output directory: `public`.
5. Cadastre estas variáveis e segredos:
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`
   - `SUPABASE_SERVICE_ROLE_KEY` — segredo
   - `STRIPE_SECRET_KEY` — segredo
   - `STRIPE_PRICE_ID`
   - `STRIPE_WEBHOOK_SECRET` — segredo
   - `OPENAI_API_KEY` — segredo, usado apenas no servidor
   - `OPENAI_TRANSCRIBE_MODEL` — `gpt-4o-mini-transcribe`
   - `AI_DAILY_LIMIT` — limite por aluno/dia; sugestão inicial: `10`
6. Faça o primeiro deploy usando o subdomínio `pages.dev`.
7. Teste cadastro, confirmação de e-mail, compra com cartão de teste, webhook, acesso, sincronização e cancelamento.
8. Só então conecte o domínio próprio e altere Supabase/Stripe para a URL definitiva.

## 5. Checklist obrigatório antes de cobrar

- Definir nome comercial, domínio e preço final.
- Publicar Termos de Uso, Política de Privacidade e Política de Cancelamento.
- Informar finalidade e retenção dos dados conforme a LGPD.
- Definir canal de suporte e prazo de resposta.
- Consultar contador sobre CNPJ, CNAE, emissão fiscal e tributação.
- Fazer backup e teste de restauração do banco.
- Ativar MFA nas contas Cloudflare, Supabase, Stripe e OpenAI.
- Limitar consumo de IA por plano e por usuário antes de disponibilizar Speaking com IA.
- Não usar a chave pessoal local da OpenAI no site público.

## Custos de referência em 13/10/2026

- Cloudflare Pages: arquivos estáticos gratuitos e ilimitados; Functions compartilham a cota gratuita de 100.000 requisições/dia.
- Supabase Free: adequado para desenvolvimento, mas pausa após uma semana sem atividade. Para produção: Pro a partir de US$ 25/mês, com backup diário.
- Stripe Brasil: sem mensalidade de configuração no preço padrão; cobra por transação. Billing acrescenta percentual sobre o volume recorrente.
- Domínio: valor anual variável conforme extensão e disponibilidade.

Valores mudam. Confirme nos painéis antes da contratação.
