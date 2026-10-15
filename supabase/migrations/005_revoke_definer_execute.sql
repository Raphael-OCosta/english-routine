-- handle_new_user() only runs as a trigger; is_admin() is used by RLS policies
-- evaluated as authenticated, so it stays executable for signed-in users.
revoke execute on function public.handle_new_user() from public, anon, authenticated;
revoke execute on function public.is_admin() from public, anon;
grant execute on function public.is_admin() to authenticated, service_role;
