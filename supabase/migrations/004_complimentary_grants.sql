-- Gift (complimentary) access granted by an administrator, keyed by e-mail so it
-- can be granted before the person creates an account.
-- expires_at null means access without an end date.
-- Only the service role (Cloudflare functions) reads or writes this table.
create table if not exists public.complimentary_grants (
  email text primary key check (email = lower(email) and position('@' in email) > 1),
  expires_at timestamptz,
  note text not null default '' check (char_length(note) <= 200),
  granted_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

alter table public.complimentary_grants enable row level security;

revoke all on table public.complimentary_grants from anon, authenticated;
grant all privileges on table public.complimentary_grants to service_role;
