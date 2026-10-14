-- Grants required in addition to Row Level Security policies.
-- Safe to run more than once. It does not read, update or delete user data.
grant usage on schema public to authenticated, service_role;

grant select on table public.profiles to authenticated;
grant select, insert, update on table public.progress_snapshots to authenticated;
grant select on table public.ai_daily_usage to authenticated;
grant select on table public.admin_user_overview to authenticated;

grant all privileges on table public.profiles to service_role;
grant all privileges on table public.subscriptions to service_role;
grant all privileges on table public.progress_snapshots to service_role;
grant all privileges on table public.ai_daily_usage to service_role;
grant select on table public.admin_user_overview to service_role;

