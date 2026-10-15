# Templates de e-mail do Supabase (português)

Supabase → **Authentication → Emails → Templates**. Para cada aba, cole o **assunto** e o conteúdo do arquivo `.html` (modo código/“Source”) e clique em **Save changes**.

| Aba no Supabase | Assunto | Arquivo |
|---|---|---|
| Confirm signup | Confirme seu cadastro no English Routine | `confirmar-cadastro.html` |
| Reset password | Redefina sua senha do English Routine | `redefinir-senha.html` |
| Magic link | Seu link de acesso ao English Routine | `link-magico.html` |
| Change email address | Confirme a troca de e-mail no English Routine | `alterar-email.html` |
| Invite user | Você foi convidado para o English Routine | `convite.html` |
| Reauthentication | Seu código de confirmação do English Routine | `reautenticacao.html` |

Variáveis usadas: `{{ .ConfirmationURL }}`, `{{ .Email }}`, `{{ .NewEmail }}`, `{{ .Token }}` (substituídas pelo Supabase).
