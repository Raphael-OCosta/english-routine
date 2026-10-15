"""Gera as páginas legais e de suporte em public/.

Edite os dados em IDENTIDADE e rode: python build-legal.py
Documento e endereço são opcionais: vazios, são omitidos do texto. Valores
entre colchetes com PENDENTE aparecem destacados em amarelo no site.
"""
from pathlib import Path

PENDENTE = '<span class="pendente">[{}]</span>'

IDENTIDADE = {
    'nome': 'Raphael Costa',
    'documento': '',  # CPF ou CNPJ
    'endereco': '',  # endereço completo para correspondência
    'email': 'suporte@englishroutine.com.br',
    'site': 'englishroutine.com.br',
    'preco': 'R$ 39,90',
    'atualizado': '15/10/2026',
}

FOOTER = (
    '<footer class="footer"><div class="wrap footer-grid">'
    '<div>© 2026 English Routine · {nome}{doc_sufixo}<br>'
    '<a href="mailto:{email}">{email}</a></div>'
    '<nav class="footer-links" aria-label="Informações legais">'
    '<a href="/termos.html">Termos de Uso</a>'
    '<a href="/privacidade.html">Privacidade</a>'
    '<a href="/cancelamento.html">Cancelamento e reembolso</a>'
    '<a href="/suporte.html">Suporte</a>'
    '</nav></div></footer>'
)

PAGE = '''<!doctype html>
<html lang="pt-BR">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{titulo} · English Routine</title><link rel="canonical" href="https://{site}/{arquivo}"><link rel="stylesheet" href="/assets/site.css"></head>
<body>
<header class="wrap topbar"><a class="brand" href="/">english<span>routine.</span></a><nav><a href="/#planos">Planos</a><a class="button secondary" href="/login.html">Entrar</a></nav></header>
<main class="wrap legal">
<div class="eyebrow">English Routine</div>
<h1>{titulo}</h1>
<p class="updated">Última atualização: {atualizado}</p>
{corpo}
</main>
{footer}
</body></html>
'''

TERMOS = '''
<p>Estes Termos regulam o uso da plataforma English Routine, disponível em {site}, oferecida por {responsavel} (“nós”). Ao criar uma conta você declara que leu e concorda com estes Termos e com a <a href="/privacidade.html">Política de Privacidade</a>.</p>

<h2>1. O serviço</h2>
<p>A English Routine é uma plataforma on-line de prática de inglês com exercícios de gramática, leitura, escrita, escuta e fala, meta diária configurável e histórico de progresso salvo na conta do aluno. O conteúdo é de apoio ao estudo e não substitui cursos certificados nem confere certificação de nível.</p>

<h2>2. Cadastro</h2>
<ul>
<li>A conta é pessoal e intransferível. Você é responsável por manter sua senha em sigilo e pelas atividades realizadas na sua conta.</li>
<li>O cadastro é destinado a maiores de 18 anos. Menores podem usar a plataforma apenas com cadastro e acompanhamento de um responsável legal.</li>
<li>As informações fornecidas devem ser verdadeiras e mantidas atualizadas.</li>
</ul>

<h2>3. Assinatura, preço e renovação</h2>
<ul>
<li>O acesso completo é oferecido pelo plano mensal de <b>{preco} por mês</b>, cobrado antecipadamente no cartão informado no pagamento.</li>
<li>A assinatura é <b>renovada automaticamente</b> a cada mês, na mesma data da contratação, até que seja cancelada.</li>
<li>O pagamento é processado pela Stripe. Não armazenamos os dados do seu cartão.</li>
<li>Eventual alteração de preço será comunicada por e-mail com pelo menos 30 dias de antecedência e valerá a partir do ciclo seguinte; você poderá cancelar antes disso.</li>
<li>Podemos conceder acessos de cortesia a nosso critério, sem cobrança e com validade informada no painel da conta.</li>
</ul>

<h2>4. Cancelamento e reembolso</h2>
<p>Você pode cancelar a qualquer momento, sem multa, conforme a <a href="/cancelamento.html">Política de Cancelamento e Reembolso</a>, que inclui o direito de arrependimento de 7 dias previsto no Código de Defesa do Consumidor.</p>

<h2>5. Recursos com inteligência artificial</h2>
<p>A avaliação de fala usa um serviço de transcrição automática. Os resultados são orientativos, podem conter imprecisões e não representam avaliação oficial de proficiência. Há um limite diário de avaliações por aluno para garantir a disponibilidade do serviço.</p>

<h2>6. Uso permitido</h2>
<p>Não é permitido: compartilhar a conta; copiar, revender ou extrair em massa o conteúdo; tentar burlar limites, pagamentos ou mecanismos de segurança; enviar conteúdo ilícito ou ofensivo nas áreas de escrita e fala. O descumprimento pode levar à suspensão da conta, após comunicação ao aluno.</p>

<h2>7. Propriedade intelectual</h2>
<p>Os exercícios, textos, marca, layout e software da English Routine são protegidos por lei. A assinatura concede uma licença pessoal, não exclusiva e intransferível de uso enquanto estiver ativa. Os textos que você escreve continuam sendo seus.</p>

<h2>8. Disponibilidade e responsabilidade</h2>
<p>Trabalhamos para manter a plataforma disponível e seus dados seguros, mas podem ocorrer interrupções para manutenção ou por falhas de terceiros. Em caso de indisponibilidade prolongada por nossa responsabilidade, você pode solicitar compensação proporcional pelo <a href="/suporte.html">Suporte</a>. Nada nestes Termos limita direitos garantidos pelo Código de Defesa do Consumidor.</p>

<h2>9. Alterações</h2>
<p>Podemos atualizar estes Termos. Mudanças relevantes serão avisadas por e-mail ou na plataforma com antecedência razoável. A versão vigente fica sempre nesta página.</p>

<h2>10. Lei aplicável e contato</h2>
<p>Aplica-se a legislação brasileira. Fica eleito o foro do domicílio do consumidor. Dúvidas e solicitações: <a href="mailto:{email}">{email}</a>.</p>
'''

PRIVACIDADE = '''
<p>Esta Política explica como a English Routine trata dados pessoais, em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018 — LGPD).</p>

<h2>1. Controlador e contato</h2>
<p>Controlador: {responsavel}. Encarregado pelo tratamento de dados e canal do titular: <a href="mailto:{email}">{email}</a>.</p>

<h2>2. Dados que tratamos</h2>
<table>
<thead><tr><th>Dado</th><th>Finalidade</th><th>Base legal (LGPD)</th></tr></thead>
<tbody>
<tr><td>Nome, e-mail e senha (guardada de forma criptografada)</td><td>Criar e proteger sua conta, comunicar sobre o serviço</td><td>Execução de contrato (art. 7º, V)</td></tr>
<tr><td>Histórico de estudo: respostas, metas, textos escritos, resultados de exercícios</td><td>Salvar e sincronizar seu progresso entre dispositivos</td><td>Execução de contrato (art. 7º, V)</td></tr>
<tr><td>Gravação de voz nos exercícios de fala</td><td>Transcrever e avaliar a pronúncia. O áudio é enviado para transcrição e <b>não é armazenado</b> por nós; guardamos apenas o resultado</td><td>Execução de contrato (art. 7º, V)</td></tr>
<tr><td>Status da assinatura e identificador de cliente na Stripe</td><td>Liberar o acesso e gerenciar cobranças</td><td>Execução de contrato e obrigação legal (art. 7º, II e V)</td></tr>
<tr><td>Registros técnicos de acesso (IP, data e hora)</td><td>Segurança, prevenção a fraudes e cumprimento do Marco Civil da Internet</td><td>Obrigação legal e legítimo interesse (art. 7º, II e IX)</td></tr>
</tbody>
</table>
<p>Não coletamos dados de cartão: o pagamento é feito diretamente na Stripe. Não vendemos dados pessoais nem os usamos para publicidade de terceiros.</p>

<h2>3. Com quem compartilhamos</h2>
<p>Usamos fornecedores (operadores) que tratam dados apenas para prestar o serviço:</p>
<ul>
<li><b>Supabase</b> — autenticação e banco de dados, hospedados em São Paulo (Brasil).</li>
<li><b>Cloudflare</b> — hospedagem do site e entrega segura das páginas.</li>
<li><b>Stripe</b> — processamento de pagamentos e assinaturas.</li>
<li><b>OpenAI</b> — transcrição do áudio dos exercícios de fala.</li>
<li><b>Provedor de e-mail transacional</b> — envio de confirmação de cadastro e redefinição de senha.</li>
</ul>
<p>Alguns desses fornecedores processam dados fora do Brasil (por exemplo, nos Estados Unidos). Essas transferências internacionais ocorrem para a execução do contrato com você e com fornecedores que adotam cláusulas contratuais e medidas de segurança compatíveis com a LGPD (art. 33).</p>

<h2>4. Armazenamento no navegador</h2>
<p>Usamos o armazenamento local do navegador para manter sua sessão de login e uma cópia do progresso, permitindo estudar mesmo com conexão instável. Não usamos cookies de publicidade nem de rastreamento.</p>

<h2>5. Por quanto tempo guardamos</h2>
<ul>
<li>Dados da conta e histórico: enquanto a conta existir. Após pedido de exclusão, são apagados em até 30 dias.</li>
<li>Registros de acesso: 6 meses, conforme o Marco Civil da Internet.</li>
<li>Dados de cobrança: pelo prazo exigido pela legislação fiscal (em geral, 5 anos), mantidos pela Stripe e por nós apenas no necessário.</li>
</ul>

<h2>6. Seus direitos</h2>
<p>Você pode solicitar a qualquer momento: confirmação e acesso aos dados; correção; exportação (portabilidade); anonimização ou eliminação de dados desnecessários; informação sobre compartilhamentos; e revogação de consentimento quando aplicável (art. 18 da LGPD). Envie o pedido para <a href="mailto:{email}">{email}</a> a partir do e-mail cadastrado. Respondemos em até 15 dias. Você também pode reclamar à Autoridade Nacional de Proteção de Dados (ANPD).</p>

<h2>7. Segurança</h2>
<p>Usamos conexão criptografada (HTTPS), controle de acesso por usuário no banco de dados, senhas protegidas por hash e chaves de serviço guardadas apenas nos servidores. Em caso de incidente relevante, comunicaremos os titulares afetados e a ANPD.</p>

<h2>8. Crianças e adolescentes</h2>
<p>O cadastro de menores de 18 anos deve ser feito por um responsável legal, que pode exercer os direitos acima em nome do menor.</p>

<h2>9. Alterações</h2>
<p>Esta Política pode ser atualizada. Mudanças relevantes serão comunicadas por e-mail ou na plataforma.</p>
'''

CANCELAMENTO = '''
<h2>Como cancelar</h2>
<ol>
<li>Entre na sua conta e abra <b>Minha conta</b>.</li>
<li>Clique em <b>Gerenciar cobrança</b> e escolha <b>Cancelar plano</b>.</li>
<li>Se preferir, envie um e-mail para <a href="mailto:{email}">{email}</a> pedindo o cancelamento; respondemos em até 2 dias úteis.</li>
</ol>
<p>Não há multa nem fidelidade. Após o cancelamento, a renovação automática é interrompida e o acesso continua até o fim do período já pago. Seu histórico permanece salvo caso queira voltar, a menos que você peça a exclusão dos dados.</p>

<h2>Direito de arrependimento (7 dias)</h2>
<p>Na primeira contratação, você pode desistir em até <b>7 dias corridos</b> a partir do pagamento, sem precisar justificar, e recebe o <b>reembolso integral</b> (art. 49 do Código de Defesa do Consumidor). Basta cancelar pelo portal e enviar um e-mail para <a href="mailto:{email}">{email}</a> pedindo o reembolso, ou pedir ambos pelo e-mail.</p>

<h2>Depois dos 7 dias</h2>
<p>Mensalidades já iniciadas não são reembolsadas proporcionalmente; o cancelamento vale para as cobranças seguintes. Cobranças indevidas, em duplicidade ou feitas após um cancelamento confirmado são sempre devolvidas integralmente.</p>

<h2>Como o reembolso é feito</h2>
<p>O estorno é feito no mesmo cartão usado na compra, pela Stripe, em até 7 dias após a confirmação. O prazo para o valor aparecer na fatura depende do emissor do cartão, normalmente de 1 a 2 faturas.</p>

<h2>Renovação</h2>
<p>O plano de {preco} por mês renova automaticamente na mesma data de cada mês. Você recebe o recibo por e-mail a cada cobrança e pode acompanhar as faturas em <b>Gerenciar cobrança</b>.</p>
'''

SUPORTE = '''
<p>Fale com a gente pelo e-mail <a href="mailto:{email}"><b>{email}</b></a>. Respondemos em até <b>2 dias úteis</b>.</p>

<h2>Para agilizar o atendimento</h2>
<ul>
<li>Escreva a partir do e-mail cadastrado na sua conta.</li>
<li>Descreva o que aconteceu e, se possível, envie um print da tela.</li>
<li>Informe o navegador e o dispositivo usados.</li>
</ul>

<h2>Assuntos mais comuns</h2>
<ul>
<li><b>Cancelamento e reembolso:</b> veja a <a href="/cancelamento.html">Política de Cancelamento e Reembolso</a>.</li>
<li><b>Esqueci minha senha:</b> use “Esqueci minha senha” na <a href="/login.html">tela de entrada</a>.</li>
<li><b>Progresso não aparece em outro dispositivo:</b> aguarde a mensagem “Salvo na nuvem” no topo do treino antes de fechar a página e entre com o mesmo e-mail no outro dispositivo.</li>
<li><b>Acesso, correção, exportação ou exclusão dos seus dados:</b> peça por e-mail; respondemos em até 15 dias, conforme a <a href="/privacidade.html">Política de Privacidade</a>.</li>
</ul>

<h2>Dados do responsável</h2>
<p>{nome}{doc_sufixo}{endereco_linha}</p>
'''

PAGES = [
    ('termos.html', 'Termos de Uso', TERMOS),
    ('privacidade.html', 'Política de Privacidade', PRIVACIDADE),
    ('cancelamento.html', 'Cancelamento e reembolso', CANCELAMENTO),
    ('suporte.html', 'Suporte', SUPORTE),
]


def campos():
    ident = dict(IDENTIDADE)
    doc, endereco = ident['documento'], ident['endereco']
    ident['doc_sufixo'] = f' · {doc}' if doc else ''
    ident['endereco_linha'] = f'<br>{endereco}' if endereco else ''
    ident['responsavel'] = ', '.join(
        [ident['nome']] + ([doc] if doc else []) + ([f'com endereço em {endereco}'] if endereco else [])
    )
    return ident


def main():
    public = Path(__file__).resolve().parent / 'public'
    ident = campos()
    footer = FOOTER.format(**ident)
    for arquivo, titulo, corpo in PAGES:
        html = PAGE.format(
            titulo=titulo, arquivo=arquivo, corpo=corpo.format(**ident).strip(),
            footer=footer, **ident,
        )
        (public / arquivo).write_text(html, encoding='utf-8', newline='\n')
    # The same footer is used by the landing page between the markers below.
    for name in ('index.html', 'dashboard.html'):
        path = public / name
        text = path.read_text(encoding='utf-8')
        start, end = '<!-- legal-footer -->', '<!-- /legal-footer -->'
        if start in text:
            before, rest = text.split(start, 1)
            after = rest.split(end, 1)[1]
            path.write_text(f'{before}{start}{footer}{end}{after}', encoding='utf-8', newline='\n')
    pendentes = sum(p.read_text(encoding='utf-8').count('class="pendente"') for p in public.glob('*.html'))
    print(f'Páginas geradas. Campos pendentes no site: {pendentes}')


if __name__ == '__main__':
    main()
