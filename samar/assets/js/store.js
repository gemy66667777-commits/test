/* طبقة التخزين المشتركة بين الموقع ولوحة التحكم */
(function (w) {
  const KEY = "samar.v1";

  const clone = (o) => JSON.parse(JSON.stringify(o));

  function read() {
    try {
      const raw = localStorage.getItem(KEY);
      if (!raw) return null;
      const d = JSON.parse(raw);
      return d && d.settings && Array.isArray(d.items) ? d : null;
    } catch (e) { return null; }
  }

  function write(d) {
    try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e) {}
    return d;
  }

  let db = read();
  if (!db) db = write(clone(w.SAMAR_SEED));

  /* دمج أي حقول جديدة اتضافت للبيانات الأساسية بعد آخر حفظ */
  for (const k in w.SAMAR_SEED.settings)
    if (!(k in db.settings)) db.settings[k] = w.SAMAR_SEED.settings[k];
  for (const k of ["services", "testimonials", "addons", "occasions"])
    if (!db[k] || !db[k].length) db[k] = clone(w.SAMAR_SEED[k]);
  if (!Array.isArray(db.bookings)) db.bookings = [];

  const Store = {
    get data() { return db; },
    get s() { return db.settings; },

    save() { write(db); document.dispatchEvent(new CustomEvent("samar:change")); return db; },

    reset() { db = write(clone(w.SAMAR_SEED)); document.dispatchEvent(new CustomEvent("samar:change")); return db; },

    imageFor(it) {
      if (it.img) return it.img;                       // صورة مرفوعة من لوحة التحكم
      return "assets/img/" + it.slug + ".jpg";
    },
    thumbFor(it) {
      if (it.img) return it.img;
      return "assets/img/" + it.slug + "-sm.jpg";
    },

    priceText(v) {
      const n = Number(v) || 0;
      if (!db.settings.showPrices || n <= 0) return db.settings.priceLabel;
      return n.toLocaleString("ar-EG") + " جنيه";
    },

    cats() {
      const seen = [];
      db.items.forEach((i) => { if (i.cat && !seen.includes(i.cat)) seen.push(i.cat); });
      return seen;
    },

    addBooking(b) {
      b.id = "bk-" + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
      b.status = "جديد";
      b.created = new Date().toISOString();
      db.bookings.unshift(b);
      this.save();
      return b;
    },

    uid(p) { return p + "-" + Date.now().toString(36) + Math.random().toString(36).slice(2, 5); },

    export() {
      return new Blob([JSON.stringify(db, null, 2)], { type: "application/json" });
    },

    import(json) {
      const d = JSON.parse(json);
      if (!d.settings || !Array.isArray(d.items)) throw new Error("الملف مش متوافق");
      db = write(d);
      document.dispatchEvent(new CustomEvent("samar:change"));
    },

    /* الجلسة — لوحة التحكم فقط */
    login(user, pass) {
      const u = String(user || "").replace(/\D/g, "");
      const ok = db.settings.adminPhones.some((p) => p.replace(/\D/g, "") === u)
              && String(pass) === String(db.settings.adminPass);
      if (ok) sessionStorage.setItem("samar.session", u);
      return ok;
    },
    session() { return sessionStorage.getItem("samar.session"); },
    logout() { sessionStorage.removeItem("samar.session"); }
  };

  w.Store = Store;
})(window);
