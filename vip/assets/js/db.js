/* =============================================================
   V.I.P SILVER — طبقة قاعدة البيانات (Supabase)
   -------------------------------------------------------------
   تعمل فقط إذا مُلئت القيمتان في supabase-config.js.
   وإن لم تُملأ، يبقى الموقع يعمل من data.js كما هو تماماً.
   ============================================================= */
window.VIPDB = (function () {
  'use strict';

  const URL = (typeof SUPABASE_URL === 'string' ? SUPABASE_URL : '').trim();
  const KEY = (typeof SUPABASE_ANON_KEY === 'string' ? SUPABASE_ANON_KEY : '').trim();
  const configured = !!(URL && KEY && window.supabase && window.supabase.createClient);

  const sb = configured ? window.supabase.createClient(URL, KEY) : null;

  /* رقم الموبايل يُستخدم كهوية الدخول، ويُخزَّن داخلياً كبريد
     حتى نستغني عن رسائل SMS المدفوعة. */
  const toEmail = phone => String(phone).replace(/[^\d]/g, '') + '@vip.local';
  const toPhone = email => String(email || '').split('@')[0];

  /* تحويل صف قاعدة البيانات إلى شكل المنتج المستخدم في الموقع */
  const rowToProduct = r => ({
    id: r.id, cat: r.cat, price: Number(r.price), img: r.img,
    name:  { ar: r.name_ar  || '', en: r.name_en  || '' },
    desc:  { ar: r.desc_ar  || '', en: r.desc_en  || '' },
    badge: { ar: r.badge_ar || '', en: r.badge_en || '' },
    sort: r.sort
  });

  const productToRow = (p, sort) => ({
    id: p.id, cat: p.cat, price: Number(p.price) || 0, img: p.img,
    name_ar:  (p.name  && p.name.ar)  || '', name_en:  (p.name  && p.name.en)  || '',
    desc_ar:  (p.desc  && p.desc.ar)  || '', desc_en:  (p.desc  && p.desc.en)  || '',
    badge_ar: (p.badge && p.badge.ar) || '', badge_en: (p.badge && p.badge.en) || '',
    sort: sort == null ? (p.sort || 0) : sort,
    updated_at: new Date().toISOString()
  });

  let admin = false;

  return {
    get on() { return configured; },
    get admin() { return admin; },

    /* ---------------- الجلسة ---------------- */
    async session() {
      if (!configured) return null;
      const { data } = await sb.auth.getSession();
      if (!data.session) { admin = false; return null; }
      await this.refreshAdmin();
      return toPhone(data.session.user.email);
    },

    async refreshAdmin() {
      if (!configured) { admin = false; return false; }
      const { data, error } = await sb.rpc('is_admin');
      admin = !error && data === true;
      return admin;
    },

    async signUp(phone, password) {
      const { error } = await sb.auth.signUp({ email: toEmail(phone), password });
      if (error) return { error: error.message };
      /* بعض المشاريع تعيد جلسة مباشرة، وبعضها يتطلب دخولاً صريحاً */
      const s = await sb.auth.getSession();
      if (!s.data.session) {
        const r = await sb.auth.signInWithPassword({ email: toEmail(phone), password });
        if (r.error) return { error: r.error.message };
      }
      await this.refreshAdmin();
      return { ok: true };
    },

    async signIn(phone, password) {
      const { error } = await sb.auth.signInWithPassword({ email: toEmail(phone), password });
      if (error) return { error: error.message };
      await this.refreshAdmin();
      return { ok: true };
    },

    async signOut() {
      if (configured) await sb.auth.signOut();
      admin = false;
    },

    async exists(phone) {
      /* لا توجد طريقة آمنة لمعرفة ذلك من المتصفح، فنجرّب الدخول لاحقاً */
      return null;
    },

    /* ---------------- المنتجات ---------------- */
    async loadProducts() {
      const { data, error } = await sb.from('products').select('*').order('sort').order('created_at');
      if (error) return { error: error.message };
      return { products: (data || []).map(rowToProduct) };
    },

    async seedProducts(list) {
      const rows = list.map((p, i) => productToRow(p, i));
      const { error } = await sb.from('products').upsert(rows);
      return error ? { error: error.message } : { ok: true };
    },

    async saveProduct(p, sort) {
      const { error } = await sb.from('products').upsert(productToRow(p, sort));
      return error ? { error: error.message } : { ok: true };
    },

    async deleteProduct(id) {
      const { error } = await sb.from('products').delete().eq('id', id);
      return error ? { error: error.message } : { ok: true };
    },

    /* ---------------- الصور ---------------- */
    async uploadImage(blob, ext) {
      const path = 'p_' + Date.now().toString(36) + '_' + Math.random().toString(36).slice(2, 7) + '.' + (ext || 'jpg');
      const { error } = await sb.storage.from('products').upload(path, blob, {
        contentType: 'image/jpeg', upsert: false
      });
      if (error) return { error: error.message };
      const { data } = sb.storage.from('products').getPublicUrl(path);
      return { url: data.publicUrl };
    },

    /* ---------------- الطلبات ---------------- */
    async saveOrder(info, items, total, lang) {
      const { error } = await sb.from('orders').insert({
        name: info.name, phone: info.phone, gov: info.gov,
        address: info.addr, note: info.note || '',
        items, total, lang: lang || 'ar'
      });
      return error ? { error: error.message } : { ok: true };
    }
  };
})();
