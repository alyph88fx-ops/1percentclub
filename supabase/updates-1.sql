-- 1 Percent Club update 1: remember when each lesson went live, so member desks can flag new videos.
-- Run once in Supabase: SQL Editor → New query → paste this file → Run. Safe to run again.

alter table public.lessons add column if not exists published_at timestamptz;
update public.lessons set published_at = created_at where published and published_at is null;

create or replace function public.stamp_published() returns trigger
language plpgsql as $$
begin
  if new.published and (tg_op = 'INSERT' or not old.published) then new.published_at := now(); end if;
  if not new.published then new.published_at := null; end if;
  return new;
end $$;
drop trigger if exists on_lesson_publish on public.lessons;
create trigger on_lesson_publish before insert or update of published on public.lessons for each row execute function public.stamp_published();
