-- 1 Percent Club: no prop-firm track. Stage 04 is now "1% Trader", the top of the path.
-- Run once in Supabase: SQL Editor → New query → paste this file → Run. Safe to run again.
update public.milestones set title = 'Risk 1% or less on 50 trades in a row' where id = 's4-prop';
insert into public.milestones (id, stage, title, xp, sort) values
  ('s4-review', 4, 'Review your journal every week for 3 months', 150, 3)
on conflict (id) do update set title = excluded.title, stage = excluded.stage, sort = excluded.sort;
