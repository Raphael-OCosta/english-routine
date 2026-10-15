"""Gera os templates de e-mail do Supabase Auth em português.

Rode: python supabase/email-templates/build.py
Cole cada arquivo .html em Supabase → Authentication → Emails → Templates,
com o assunto indicado em LEIA-ME.md.
"""
from pathlib import Path

BASE = '''<!doctype html>
<html lang="pt-BR">
<body style="margin:0;padding:0;background:#f1f5fa;font-family:Arial,Helvetica,sans-serif;color:#172b49">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f1f5fa;padding:32px 12px">
<tr><td align="center">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#ffffff;border:1px solid #dbe4f0;border-radius:16px">
<tr><td style="padding:28px 32px 8px;font-size:24px;font-weight:800;letter-spacing:-0.5px;color:#013473">english<span style="color:#2677e8">routine.</span></td></tr>
<tr><td style="padding:8px 32px 0">
<h1 style="margin:0 0 12px;font-size:22px;line-height:1.3;color:#071c38">{titulo}</h1>
{corpo}
</td></tr>
<tr><td style="padding:8px 32px 28px">
<p style="margin:20px 0 0;font-size:13px;line-height:1.6;color:#586b86">Se o botão não funcionar, copie e cole este endereço no navegador:<br><a href="{link}" style="color:#2677e8;word-break:break-all">{link}</a></p>
</td></tr>
</table>
<p style="margin:16px 0 0;font-size:12px;line-height:1.6;color:#586b86">English Routine · <a href="https://englishroutine.com.br" style="color:#586b86">englishroutine.com.br</a> · Dúvidas: <a href="mailto:suporte@englishroutine.com.br" style="color:#586b86">suporte@englishroutine.com.br</a></p>
</td></tr>
</table>
</body>
</html>
'''

BOTAO = ('<p style="margin:24px 0 8px"><a href="{link}" style="display:inline-block;background:#013473;color:#ffffff;'
         'text-decoration:none;font-weight:700;padding:13px 22px;border-radius:10px">{rotulo}</a></p>')


def paragrafo(texto):
    return f'<p style="margin:0 0 12px;font-size:15px;line-height:1.6">{texto}</p>'


LINK = '{{ .ConfirmationURL }}'

TEMPLATES = [
    ('confirmar-cadastro', 'Confirm signup', 'Confirme seu cadastro no English Routine',
     'Confirme seu e-mail', [
         paragrafo('Olá! Falta só um passo para começar sua rotina de inglês.'),
         paragrafo('Clique no botão abaixo para confirmar o endereço <b>{{ .Email }}</b>.'),
         BOTAO.format(link=LINK, rotulo='Confirmar e-mail'),
         paragrafo('Se você não criou uma conta no English Routine, ignore esta mensagem.'),
     ]),
    ('redefinir-senha', 'Reset password', 'Redefina sua senha do English Routine',
     'Redefinir senha', [
         paragrafo('Recebemos um pedido para redefinir a senha da conta <b>{{ .Email }}</b>.'),
         paragrafo('Clique no botão abaixo e escolha uma nova senha. O link vale por 1 hora e só pode ser usado uma vez.'),
         BOTAO.format(link=LINK, rotulo='Criar nova senha'),
         paragrafo('Se você não pediu a troca, ignore este e-mail: sua senha atual continua valendo.'),
     ]),
    ('link-magico', 'Magic link', 'Seu link de acesso ao English Routine',
     'Entrar no English Routine', [
         paragrafo('Use o botão abaixo para entrar na sua conta. O link vale por 1 hora e só pode ser usado uma vez.'),
         BOTAO.format(link=LINK, rotulo='Entrar agora'),
         paragrafo('Se você não pediu este acesso, ignore esta mensagem.'),
     ]),
    ('alterar-email', 'Change email address', 'Confirme a troca de e-mail no English Routine',
     'Confirmar novo e-mail', [
         paragrafo('Recebemos um pedido para trocar o e-mail da sua conta de <b>{{ .Email }}</b> para <b>{{ .NewEmail }}</b>.'),
         BOTAO.format(link=LINK, rotulo='Confirmar troca'),
         paragrafo('Se você não fez esse pedido, responda para suporte@englishroutine.com.br imediatamente.'),
     ]),
    ('convite', 'Invite user', 'Você foi convidado para o English Routine',
     'Seu acesso ao English Routine', [
         paragrafo('Você recebeu um convite para usar o English Routine, a plataforma de treino diário de inglês.'),
         paragrafo('Clique no botão abaixo para aceitar e criar sua senha.'),
         BOTAO.format(link=LINK, rotulo='Aceitar convite'),
     ]),
]

REAUTH = BASE.replace(
    '<tr><td style="padding:8px 32px 28px">\n<p style="margin:20px 0 0;font-size:13px;line-height:1.6;color:#586b86">'
    'Se o botão não funcionar, copie e cole este endereço no navegador:<br><a href="{link}" '
    'style="color:#2677e8;word-break:break-all">{link}</a></p>\n</td></tr>\n',
    '<tr><td style="padding:0 32px 28px"></td></tr>\n',
).format(
    titulo='Código de confirmação',
    link='',
    corpo=''.join([
        paragrafo('Use o código abaixo para confirmar esta ação na sua conta:'),
        '<p style="margin:16px 0;font-size:30px;font-weight:800;letter-spacing:6px;color:#013473">{{ .Token }}</p>',
        paragrafo('Se você não fez este pedido, ignore esta mensagem.'),
    ]),
)


def main():
    pasta = Path(__file__).resolve().parent
    linhas = [
        '# Templates de e-mail do Supabase (português)',
        '',
        'Supabase → **Authentication → Emails → Templates**. Para cada aba, cole o **assunto** e o conteúdo do arquivo `.html` '
        '(modo código/“Source”) e clique em **Save changes**.',
        '',
        '| Aba no Supabase | Assunto | Arquivo |',
        '|---|---|---|',
    ]
    for arquivo, aba, assunto, titulo, partes in TEMPLATES:
        html = BASE.format(titulo=titulo, corpo='\n'.join(partes), link=LINK)
        (pasta / f'{arquivo}.html').write_text(html, encoding='utf-8', newline='\n')
        linhas.append(f'| {aba} | {assunto} | `{arquivo}.html` |')
    (pasta / 'reautenticacao.html').write_text(REAUTH, encoding='utf-8', newline='\n')
    linhas.append('| Reauthentication | Seu código de confirmação do English Routine | `reautenticacao.html` |')
    linhas += ['', 'Variáveis usadas: `{{ .ConfirmationURL }}`, `{{ .Email }}`, `{{ .NewEmail }}`, `{{ .Token }}` (substituídas pelo Supabase).', '']
    (pasta / 'LEIA-ME.md').write_text('\n'.join(linhas), encoding='utf-8', newline='\n')
    print('Templates gerados em', pasta)


if __name__ == '__main__':
    main()
