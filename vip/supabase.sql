-- =============================================================
-- V.I.P SILVER — إعداد قاعدة البيانات على Supabase
-- افتح SQL Editor في مشروعك والصق هذا الملف كاملاً ثم اضغط Run.
-- آمن للتشغيل أكثر من مرة.
-- =============================================================

-- ------------------------------------------------------------
-- 1) جدول الأدمن: من يملك صلاحية التعديل
--    الدخول يتم برقم الموبايل، ويُخزَّن داخلياً كبريد على الشكل
--    01XXXXXXXXX@vip.local حتى نستغني عن رسائل SMS المدفوعة.
-- ------------------------------------------------------------
create table if not exists public.admins (
  email text primary key,
  phone text not null,
  added_at timestamptz default now()
);

insert into public.admins (email, phone) values
  ('01156442660@vip.local', '01156442660'),
  ('01065434420@vip.local', '01065434420')
on conflict (email) do nothing;

-- دالة مساعدة: هل المستخدم الحالي أدمن؟
create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.admins a where a.email = auth.jwt() ->> 'email');
$$;

-- ------------------------------------------------------------
-- 2) جدول المنتجات
-- ------------------------------------------------------------
create table if not exists public.products (
  id         text primary key,
  cat        text not null default 'silver',
  price      numeric not null default 0,
  name_ar    text not null default '',
  name_en    text not null default '',
  desc_ar    text not null default '',
  desc_en    text not null default '',
  badge_ar   text not null default '',
  badge_en   text not null default '',
  img        text not null default '',
  sort       int  not null default 0,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create index if not exists products_sort_idx on public.products (sort, created_at);

-- ------------------------------------------------------------
-- 3) جدول الطلبات — سجلّ لكل طلب يُرسَل عبر واتساب
-- ------------------------------------------------------------
create table if not exists public.orders (
  id          bigserial primary key,
  name        text not null,
  phone       text not null,
  gov         text not null,
  address     text not null,
  note        text default '',
  items       jsonb not null,
  total       numeric not null,
  lang        text default 'ar',
  created_at  timestamptz default now()
);

create index if not exists orders_created_idx on public.orders (created_at desc);

-- ------------------------------------------------------------
-- 4) قواعد الصلاحيات (Row Level Security)
--    هنا الحماية الحقيقية: الفحص يتم على السيرفر لا في المتصفح.
-- ------------------------------------------------------------
alter table public.products enable row level security;
alter table public.orders   enable row level security;
alter table public.admins   enable row level security;

-- المنتجات: الجميع يقرأ، الأدمن وحده يكتب
drop policy if exists products_read   on public.products;
drop policy if exists products_insert on public.products;
drop policy if exists products_update on public.products;
drop policy if exists products_delete on public.products;

create policy products_read   on public.products for select using (true);
create policy products_insert on public.products for insert with check (public.is_admin());
create policy products_update on public.products for update using (public.is_admin()) with check (public.is_admin());
create policy products_delete on public.products for delete using (public.is_admin());

-- الطلبات: أي زائر يستطيع تسجيل طلبه، والأدمن وحده يقرأها
drop policy if exists orders_insert on public.orders;
drop policy if exists orders_read   on public.orders;

create policy orders_insert on public.orders for insert with check (true);
create policy orders_read   on public.orders for select using (public.is_admin());

-- جدول الأدمن: يقرأه الأدمن فقط، ولا يُعدَّل إلا من لوحة Supabase
drop policy if exists admins_read on public.admins;
create policy admins_read on public.admins for select using (public.is_admin());

-- ------------------------------------------------------------
-- 5) مخزن صور المنتجات
-- ------------------------------------------------------------
insert into storage.buckets (id, name, public)
values ('products', 'products', true)
on conflict (id) do nothing;

drop policy if exists product_images_read   on storage.objects;
drop policy if exists product_images_write  on storage.objects;
drop policy if exists product_images_update on storage.objects;
drop policy if exists product_images_delete on storage.objects;

create policy product_images_read   on storage.objects for select
  using (bucket_id = 'products');
create policy product_images_write  on storage.objects for insert
  with check (bucket_id = 'products' and public.is_admin());
create policy product_images_update on storage.objects for update
  using (bucket_id = 'products' and public.is_admin());
create policy product_images_delete on storage.objects for delete
  using (bucket_id = 'products' and public.is_admin());

-- ------------------------------------------------------------
-- تم. الخطوة التالية في README: إنشاء حسابي الأدمن من الموقع نفسه.
-- ------------------------------------------------------------
