-- 1 Percent Club: what the public home page may read from the members database.
-- Run once in Supabase: SQL Editor → New query → paste this file → Run. Safe to run again.
-- Only counts, the next live session's title and time, and published lesson titles are exposed:
-- never video or file links, join links, or anything about individual members.

create or replace function public.public_stats() returns json
language sql stable security definer set search_path = public as $$
  select json_build_object(
    'members',  (select count(*) from public.profiles),
    'videos',   (select count(*) from public.lessons where published and kind = 'video'),
    'ebooks',   (select count(*) from public.lessons where published and kind = 'ebook'),
    'by_stage', (select coalesce(json_object_agg(stage, json_build_object('videos', v, 'ebooks', e)), '{}'::json)
                   from (select stage, count(*) filter (where kind = 'video') v, count(*) filter (where kind = 'ebook') e
                           from public.lessons where published and stage is not null group by stage) s),
    'live_30d', (select count(*) from public.live_sessions where starts_at >= now() and starts_at < now() + interval '30 days'),
    'next_live', (select json_build_object('title', title, 'kind', kind, 'starts_at', starts_at, 'duration_mins', duration_mins)
                    from public.live_sessions where starts_at + make_interval(mins => duration_mins) > now()
                    order by starts_at limit 1)
  );
$$;

create or replace function public.public_library()
returns table (id uuid, kind text, title text, description text, category text, level text, stage smallint,
               duration_secs integer, pages integer, cover_url text, required_plan text)
language sql stable security definer set search_path = public as $$
  select id, kind, title, description, category, level, stage, duration_secs, pages, cover_url, required_plan
    from public.lessons where published order by sort, created_at;
$$;

grant execute on function public.public_stats() to anon, authenticated;
grant execute on function public.public_library() to anon, authenticated;

-- your starter ebook, so the home page shelf starts with the real cover (edit or unpublish it in admin)
insert into public.lessons (kind, title, description, category, level, stage, cover_url, required_plan, published, sort)
select 'ebook', 'Headline and Storyline', 'The free starter ebook from 1 Percent Club.', 'Foundations', 'Beginner', 1,
       'https://1-percentclub.com/ebook-01.webp', 'starter', true, 0
 where not exists (select 1 from public.lessons where title = 'Headline and Storyline');
