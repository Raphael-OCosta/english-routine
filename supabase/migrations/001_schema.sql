create extension if not exists pgcrypto;
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  full_name text not null default '',
  role text not null default 'student' check (role in ('student','admin')),
  subscription_status text not null default 'inactive',
  stripe_customer_id text unique,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create table if not exists public.subscriptions (
  stripe_subscription_id text primary key,
  stripe_customer_id text not null,
  status text not null,
  current_period_end timestamptz,
  cancel_at_period_end boolean not null default false,
  updated_at timestamptz not null default now()
);
create table if not exists public.progress_snapshots (
  user_id uuid primary key references auth.users(id) on delete cascade,
  state jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now(),
  constraint progress_size check (octet_length(state::text) <= 5000000)
);
create table if not exists public.ai_daily_usage (
  user_id uuid not null references auth.users(id) on delete cascade,
  usage_date date not null default current_date,
  calls integer not null default 0 check (calls >= 0),
  primary key(user_id, usage_date)
);
create or replace function public.handle_new_user() returns trigger language plpgsql security definer set search_path=public as $$begin insert into public.profiles(id,email,full_name,role) values(new.id,new.email,coalesce(new.raw_user_meta_data->>'name',''),case when lower(new.email)='rarphael@gmail.com' then 'admin' else 'student' end);return new;end$$;
drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users for each row execute procedure public.handle_new_user();
create or replace function public.is_admin() returns boolean language sql stable security definer set search_path=public as $$select exists(select 1 from public.profiles where id=auth.uid() and role='admin')$$;
alter table public.profiles enable row level security;
alter table public.subscriptions enable row level security;
alter table public.progress_snapshots enable row level security;
alter table public.ai_daily_usage enable row level security;
create policy "profile own read" on public.profiles for select using(id=auth.uid() or public.is_admin());
create policy "progress own read" on public.progress_snapshots for select using(user_id=auth.uid() or public.is_admin());
create policy "progress own insert" on public.progress_snapshots for insert with check(user_id=auth.uid());
create policy "progress own update" on public.progress_snapshots for update using(user_id=auth.uid()) with check(user_id=auth.uid());
create policy "subscriptions admin read" on public.subscriptions for select using(public.is_admin());
create policy "ai usage own read" on public.ai_daily_usage for select using(user_id=auth.uid() or public.is_admin());
create or replace view public.admin_user_overview with(security_invoker=true) as select p.id,p.full_name,p.email,p.subscription_status,p.created_at from public.profiles p;
grant select on public.admin_user_overview to authenticated;
