-- Plataforma multi-idioma (English Routine + Korean Routine).
-- Aplicar em duas etapas em produção para não quebrar a versão publicada:
--   Etapa A (antes do deploy): colunas novas + índice único (user_id, language).
--   Etapa B (depois do deploy): chave primária passa a ser (user_id, language).

-- ---------------------------------------------------------------- Etapa A
alter table public.progress_snapshots
  add column if not exists language text not null default 'en'
  check (language ~ '^[a-z]{2}$');

create unique index if not exists progress_snapshots_user_language
  on public.progress_snapshots (user_id, language);

alter table public.profiles
  add column if not exists languages text[] not null default '{en}',
  add column if not exists plan_size integer not null default 1 check (plan_size between 1 and 3),
  add column if not exists languages_changed_at timestamptz;

-- Cortesia por idioma: null = todos os idiomas disponíveis.
alter table public.complimentary_grants
  add column if not exists languages text[];

-- ---------------------------------------------------------------- Etapa B
alter table public.progress_snapshots drop constraint if exists progress_snapshots_pkey;
alter table public.progress_snapshots
  add constraint progress_snapshots_pkey primary key using index progress_snapshots_user_language;
