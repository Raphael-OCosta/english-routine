-- Repairs profiles for users created before the trigger was installed.
-- This migration does not modify progress_snapshots or subscription records.
insert into public.profiles (id, email, full_name, role, subscription_status)
select
  u.id,
  coalesce(u.email, ''),
  coalesce(u.raw_user_meta_data ->> 'name', case when lower(u.email) = 'rarphael@gmail.com' then 'Raphael Costa' else '' end),
  case when lower(u.email) = 'rarphael@gmail.com' then 'admin' else 'student' end,
  'inactive'
from auth.users u
on conflict (id) do update
set
  email = excluded.email,
  full_name = case
    when public.profiles.full_name = '' then excluded.full_name
    else public.profiles.full_name
  end,
  role = case
    when lower(excluded.email) = 'rarphael@gmail.com' then 'admin'
    else public.profiles.role
  end,
  updated_at = now();

