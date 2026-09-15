/* لاشيرا ستور — لوحة التحكم */
(function () {
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  const ar = (n) => Number(n || 0).toLocaleString("ar-EG");
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const SK = "lashera.admin";
  let db = LStore.get();

  const sv = (d) => `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
    stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">${d}</svg>`;
  const I = {
    grid:  sv('<rect x="3" y="3" width="7.5" height="7.5" rx="2"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="2"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="2"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="2"/>'),
    image: sv('<rect x="3" y="4.5" width="18" height="15" rx="2.5"/><circle cx="8.5" cy="10" r="1.6"/><path d="m4 17 5-4.5 4 3.3 3.5-2.8L20 17"/>'),
    box:   sv('<path d="M20.5 7.8 12 3.2 3.5 7.8v8.4L12 20.8l8.5-4.6z"/><path d="m3.6 7.9 8.4 4.5 8.4-4.5M12 12.4v8.4"/>'),
    cal:   sv('<rect x="3.2" y="5" width="17.6" height="16" rx="2.5"/><path d="M3.2 10h17.6M8 3v4M16 3v4"/>'),
    gear:  sv('<circle cx="12" cy="12" r="3.1"/><path d="M19.6 14.4a1.6 1.6 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.6 1.6 0 0 0-2.7 1.1v.3a2 2 0 1 1-4 0v-.2a1.6 1.6 0 0 0-2.8-1.1l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.6 1.6 0 0 0-1.1-2.7h-.3a2 2 0 1 1 0-4h.2a1.6 1.6 0 0 0 1.1-2.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.6 1.6 0 0 0 2.7-1.1v-.3a2 2 0 1 1 4 0v.2a1.6 1.6 0 0 0 2.8 1.1l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.6 1.6 0 0 0 1.1 2.7h.3a2 2 0 1 1 0 4h-.2a1.6 1.6 0 0 0-1.4.9z"/>'),
    edit:  sv('<path d="M16.4 3.9a2 2 0 0 1 2.8 2.8L7.6 18.3l-3.8 1 1-3.8z"/>'),
    trash: sv('<path d="M4.5 6.5h15M9.5 6.5V4.6h5v1.9M6.6 6.5l.8 13a1.6 1.6 0 0 0 1.6 1.5h6a1.6 1.6 0 0 0 1.6-1.5l.8-13"/>'),
    up:    sv('<path d="M12 19V5M5.5 11.5 12 5l6.5 6.5"/>'),
    down:  sv('<path d="M12 5v14M18.5 12.5 12 19l-6.5-6.5"/>'),
    star:  sv('<path d="m12 3.4 2.6 5.4 5.9.8-4.3 4.2 1 5.9L12 17l-5.2 2.7 1-5.9-4.3-4.2 5.9-.8z"/>'),
    wa:    sv('<path d="M20.5 11.6a8.4 8.4 0 0 1-12.4 7.4L3.5 20.5l1.6-4.5A8.4 8.4 0 1 1 20.5 11.6z"/>')
  };
  $$("[data-icon]").forEach((el) => (el.innerHTML = I[el.dataset.icon] || ""));

  let tT;
  function toast(msg) {
    const t = $("#toast"); t.textContent = msg; t.classList.add("on");
    clearTimeout(tT); tT = setTimeout(() => t.classList.remove("on"), 2600);
  }
  const modal = $("#modal"), mbox = $("#modalBox");
  function openModal(html) { mbox.innerHTML = html; modal.classList.add("on"); document.body.style.overflow = "hidden"; }
  function closeModal() { modal.classList.remove("on"); document.body.style.overflow = ""; }
  modal.addEventListener("click", (e) => { if (e.target === modal) closeModal(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeModal(); });

  const digits = (s) => String(s || "").replace(/\D/g, "");
  function priceText(p) {
    const s = db.settings;
    if (!s.showPrices || !Number(p)) return s.priceNote;
    return ar(p) + " " + (s.currency || "");
  }

  /* ---------- الدخول ---------- */
  $("#gBrand").textContent = db.settings.brandAr;
  $("#sBrand").textContent = db.settings.brandAr;
  $("#gForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const u = digits($("#gUser").value), p = $("#gPass").value;
    const ok = u && digits(db.settings.phone).endsWith(u.slice(-9)) && p === db.settings.adminPass;
    if (ok) { try { sessionStorage.setItem(SK, $("#gUser").value); } catch (err) {} enter(); }
    else {
      const er = $("#gErr");
      er.textContent = "الرقم أو كلمة السر غلط. جرّب تاني.";
      er.classList.add("on"); $("#gPass").value = "";
    }
  });
  function session() { try { return sessionStorage.getItem(SK); } catch (e) { return null; } }
  function enter() {
    $("#gate").style.display = "none";
    $("#app").classList.add("on");
    $("#whoami").textContent = "داخل برقم " + session();
    renderAll();
  }
  $("#logout").onclick = () => { try { sessionStorage.removeItem(SK); } catch (e) {} location.reload(); };
  if (session()) enter();

  /* ---------- التبويبات ---------- */
  $$(".tab").forEach((t) => t.addEventListener("click", () => {
    $$(".tab").forEach((x) => x.classList.toggle("on", x === t));
    $$(".panel").forEach((p) => p.classList.toggle("on", p.id === "p-" + t.dataset.tab));
    document.body.classList.remove("nav");
    scrollTo({ top: 0 });
  }));
  $$(".mob").forEach((b) => (b.onclick = () => document.body.classList.toggle("nav")));

  /* ---------- رفع صورة ---------- */
  function pickImg(cb) {
    const f = document.createElement("input");
    f.type = "file"; f.accept = "image/*";
    f.onchange = () => {
      const file = f.files && f.files[0]; if (!file) return;
      const rd = new FileReader();
      rd.onload = () => cb(rd.result);
      rd.readAsDataURL(file);
    };
    f.click();
  }

  /* ================= نظرة عامة ================= */
  function renderHome() {
    const o = db.orders;
    const kpi = (ic, n, lbl) => `<div class="kpi"><span class="ic">${I[ic]}</span><b>${n}</b><small>${lbl}</small></div>`;
    $("#kpis").innerHTML =
      kpi("box",   ar(db.products.length), "منتج معروض") +
      kpi("image", ar(db.gallery.length),  "صورة في المعرض") +
      kpi("cal",   ar(o.length),           "إجمالي الطلبات") +
      kpi("star",  ar(o.filter((x) => x.src === "form").length), "طلب من الفورم");

    const last = o.slice(0, 7);
    $("#lastOrds").innerHTML = last.length ? `<table><thead><tr>
        <th>العميل</th><th>المنتج</th><th>المدينة</th><th>التاريخ</th></tr></thead><tbody>` +
      last.map((x) => `<tr>
        <td><span class="nm">${esc(x.name)}</span><small dir="ltr">${esc(x.phone)}</small></td>
        <td>${esc(x.item)}</td><td>${esc(x.city || "—")}</td>
        <td>${esc(fmt(x.at))}</td></tr>`).join("") + "</tbody></table>"
      : `<div class="blank"><b>لسه مفيش طلبات</b>أول طلب يجي من الموقع هيظهر هنا.</div>`;

    const by = {};
    o.forEach((x) => (by[x.item || "—"] = (by[x.item || "—"] || 0) + 1));
    const keys = Object.keys(by).sort((a, c) => by[c] - by[a]).slice(0, 8);
    const max = Math.max(1, ...keys.map((k) => by[k]));
    $("#chart").innerHTML = keys.length ? keys.map((k) =>
      `<div class="bar"><span>${esc(k)}</span><span class="t"><i style="width:${(by[k] / max) * 100}%"></i></span><span class="v">${ar(by[k])}</span></div>`
    ).join("") : `<div class="blank" style="padding:30px"><b>مفيش بيانات لسه</b></div>`;
  }
  function fmt(iso) {
    try { const d = new Date(iso);
      return d.toLocaleDateString("ar-EG", { day: "numeric", month: "short" }) + " · " +
             d.toLocaleTimeString("ar-EG", { hour: "2-digit", minute: "2-digit" });
    } catch (e) { return "—"; }
  }

  /* ================= المنتجات ================= */
  function renderProds() {
    const ps = db.products;
    $("#nProds").textContent = ar(ps.length);
    $("#pgrid").innerHTML = ps.length ? ps.map((p, i) => `
      <article class="mcard">
        <div class="ph">${p.badge ? `<span class="fav">${esc(p.badge)}</span>` : ""}
          <img src="${esc(p.img)}" alt="${esc(p.name)}" loading="lazy"></div>
        <div class="bd"><b>${esc(p.name)}</b><small>${esc((p.sizes || []).join(" · "))}</small>
          <span class="pr">${esc(priceText(p.price))}</span></div>
        <div class="bar2">
          <button class="ib" data-ed="${i}" title="تعديل">${I.edit}</button>
          <button class="ib" data-mv="${i}" data-d="-1" title="تقديم">${I.up}</button>
          <button class="ib" data-mv="${i}" data-d="1" title="تأخير">${I.down}</button>
          <button class="ib del" data-del="${i}" title="حذف" style="margin-inline-start:auto">${I.trash}</button>
        </div>
      </article>`).join("")
      : `<div class="blank" style="grid-column:1/-1"><b>مفيش منتجات</b>ابدأ بإضافة أول منتج.</div>`;

    $$("#pgrid [data-ed]").forEach((b) => (b.onclick = () => prodForm(+b.dataset.ed)));
    $$("#pgrid [data-mv]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.mv, j = i + +b.dataset.d;
      if (j < 0 || j >= db.products.length) return;
      db = LStore.patch((d) => { const t = d.products[i]; d.products[i] = d.products[j]; d.products[j] = t; });
    }));
    $$("#pgrid [data-del]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.del;
      if (!confirm("تحذف «" + db.products[i].name + "»؟")) return;
      db = LStore.patch((d) => d.products.splice(i, 1)); toast("اتحذف");
    }));
  }
  $("#addProd").onclick = () => prodForm(-1);

  function prodForm(i) {
    const p = i < 0
      ? { id: "p" + Date.now(), name: "", img: "assets/img/p-moss.jpg", price: 0, sizes: ["عبوة"], badge: "", desc: "" }
      : JSON.parse(JSON.stringify(db.products[i]));
    openModal(`
      <h3>${i < 0 ? "منتج جديد" : "تعديل منتج"}</h3>
      <p class="sub">الاسم والصورة دول اللي بيظهروا في صفحة المنتجات.</p>
      <div class="field"><label>صورة المنتج</label>
        <div class="drop" id="mPick"><img id="mImg" src="${esc(p.img)}" alt="">
          <div>اضغط لاختيار صورة من جهازك</div></div></div>
      <div class="field"><label>اسم المنتج</label><input id="mName" value="${esc(p.name)}" placeholder="مثال: زيت الشعر واللحية 60 مل"></div>
      <div class="field"><label>الوصف</label><textarea id="mDesc" style="min-height:70px">${esc(p.desc)}</textarea></div>
      <div class="grid2">
        <div class="field"><label>المقاسات (افصلهم بفاصلة)</label><input id="mSizes" value="${esc((p.sizes || []).join("، "))}"></div>
        <div class="field"><label>الشارة (اختياري)</label><input id="mBadge" value="${esc(p.badge || "")}" placeholder="الأكثر طلبًا"></div>
      </div>
      <div class="field"><label>السعر</label><input id="mPrice" type="number" min="0" value="${Number(p.price) || 0}">
        <div class="hint">السعر مش بيظهر في الموقع غير لو فعّلت «إظهار الأسعار» من الإعدادات</div></div>
      <div class="modal-acts"><button class="btn ghost" id="mC">إلغاء</button><button class="btn" id="mS">حفظ</button></div>`);
    let img = p.img;
    $("#mPick").onclick = () => pickImg((d) => { img = d; $("#mImg").src = d; });
    $("#mC").onclick = closeModal;
    $("#mS").onclick = () => {
      const n = $("#mName").value.trim();
      if (!n) { $("#mName").focus(); return; }
      const rec = { id: p.id, name: n, img: img, price: Number($("#mPrice").value) || 0,
        sizes: $("#mSizes").value.split(/[،,]/).map((x) => x.trim()).filter(Boolean),
        badge: $("#mBadge").value.trim(), desc: $("#mDesc").value.trim() };
      if (!rec.sizes.length) rec.sizes = ["عبوة"];
      db = LStore.patch((d) => { i < 0 ? d.products.push(rec) : (d.products[i] = rec); });
      closeModal(); toast("اتحفظ ✅");
    };
  }

  /* ================= المعرض ================= */
  function renderItems() {
    const g = db.gallery;
    $("#nItems").textContent = ar(g.length);
    $("#mgrid").innerHTML = g.length ? g.map((it, i) => `
      <article class="mcard">
        <div class="ph"><img src="${esc(it.img)}" alt="${esc(it.cap)}" loading="lazy"></div>
        <div class="bd"><b>${esc(it.cap)}</b></div>
        <div class="bar2">
          <button class="ib" data-ed="${i}" title="تعديل">${I.edit}</button>
          <button class="ib" data-mv="${i}" data-d="-1" title="تقديم">${I.up}</button>
          <button class="ib" data-mv="${i}" data-d="1" title="تأخير">${I.down}</button>
          <button class="ib del" data-del="${i}" title="حذف" style="margin-inline-start:auto">${I.trash}</button>
        </div>
      </article>`).join("")
      : `<div class="blank" style="grid-column:1/-1"><b>المعرض فاضي</b>ابدأ بإضافة أول صورة.</div>`;

    $$("#mgrid [data-ed]").forEach((b) => (b.onclick = () => itemForm(+b.dataset.ed)));
    $$("#mgrid [data-mv]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.mv, j = i + +b.dataset.d;
      if (j < 0 || j >= db.gallery.length) return;
      db = LStore.patch((d) => { const t = d.gallery[i]; d.gallery[i] = d.gallery[j]; d.gallery[j] = t; });
    }));
    $$("#mgrid [data-del]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.del;
      if (!confirm("تحذف الصورة دي؟")) return;
      db = LStore.patch((d) => d.gallery.splice(i, 1)); toast("اتحذفت");
    }));
  }
  $("#addItem").onclick = () => itemForm(-1);

  function itemForm(i) {
    const it = i < 0 ? { img: "assets/img/p-moss.jpg", cap: "" } : Object.assign({}, db.gallery[i]);
    openModal(`
      <h3>${i < 0 ? "صورة جديدة" : "تعديل الصورة"}</h3>
      <p class="sub">اكتب اللي شايفه في الصورة بالظبط.</p>
      <div class="field"><label>الصورة</label>
        <div class="drop" id="mPick"><img id="mImg" src="${esc(it.img)}" alt="">
          <div>اضغط لاختيار صورة من جهازك</div></div></div>
      <div class="field"><label>الوصف اللي تحت الصورة</label><input id="mCap" value="${esc(it.cap)}" placeholder="مثال: عبوة 60 مل على طحلب أخضر">
        <div class="hint">من غير أقواس ولا أسماء تسويقية — اللي في الصورة بس</div></div>
      <div class="modal-acts"><button class="btn ghost" id="mC">إلغاء</button><button class="btn" id="mS">حفظ</button></div>`);
    let img = it.img;
    $("#mPick").onclick = () => pickImg((d) => { img = d; $("#mImg").src = d; });
    $("#mC").onclick = closeModal;
    $("#mS").onclick = () => {
      const rec = { img: img, cap: $("#mCap").value.trim() || "صورة" };
      db = LStore.patch((d) => { i < 0 ? d.gallery.push(rec) : (d.gallery[i] = rec); });
      closeModal(); toast("اتحفظ ✅");
    };
  }

  /* ================= الطلبات ================= */
  function renderOrds() {
    const o = db.orders;
    $("#nOrds").textContent = ar(o.length);
    $("#ordsTbl").innerHTML = o.length ? `<table><thead><tr>
        <th>التاريخ</th><th>العميل</th><th>المنتج</th><th>المدينة</th><th>ملاحظات</th><th></th></tr></thead><tbody>` +
      o.map((x, i) => `<tr>
        <td>${esc(fmt(x.at))}</td>
        <td><span class="nm">${esc(x.name)}</span><small dir="ltr">${esc(x.phone)}</small></td>
        <td>${esc(x.item)}</td><td>${esc(x.city || "—")}</td><td>${esc(x.note || "—")}</td>
        <td><button class="ib del" data-del="${i}">${I.trash}</button></td></tr>`).join("") + "</tbody></table>"
      : `<div class="blank"><b>لسه مفيش طلبات</b>أول طلب من الموقع هيظهر هنا.</div>`;
    $$("#ordsTbl [data-del]").forEach((b) => (b.onclick = () => {
      db = LStore.patch((d) => d.orders.splice(+b.dataset.del, 1)); toast("اتحذف");
    }));
  }
  $("#clrOrds").onclick = () => {
    if (!db.orders.length) return;
    if (!confirm("تمسح كل الطلبات؟")) return;
    db = LStore.patch((d) => (d.orders = [])); toast("اتمسحت");
  };
  $("#expCsv").onclick = () => {
    const rows = [["التاريخ", "الاسم", "الموبايل", "المدينة", "المنتج", "ملاحظات"]]
      .concat(db.orders.map((x) => [x.at, x.name, x.phone, x.city, x.item, x.note]));
    const csv = "﻿" + rows.map((r) => r.map((c) =>
      '"' + String(c == null ? "" : c).replace(/"/g, '""') + '"').join(",")).join("\r\n");
    dl(new Blob([csv], { type: "text/csv;charset=utf-8" }), "lashera-orders.csv");
  };
  function dl(blob, name) {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 900);
  }

  /* ================= الإعدادات ================= */
  const F = $("#setForm");
  function renderSet() {
    const s = db.settings;
    ["brandAr","brand","tagline","taglineAr","intro","phone","phoneShow","whats",
     "instagram","city","hours","ship","priceNote","currency","adminPass"].forEach((k) => {
      if (F.elements[k]) F.elements[k].value = s[k] == null ? "" : s[k];
    });
    F.elements.showPrices.checked = !!s.showPrices;
  }
  F.addEventListener("submit", (e) => {
    e.preventDefault();
    const el = e.target.elements;
    db = LStore.patch((d) => {
      ["brandAr","brand","tagline","taglineAr","intro","phone","phoneShow","whats",
       "instagram","city","hours","ship","priceNote","currency","adminPass"].forEach((k) => {
        if (el[k]) d.settings[k] = el[k].value.trim();
      });
      d.settings.whats = digits(d.settings.whats);
      d.settings.showPrices = el.showPrices.checked;
      if (!d.settings.adminPass) d.settings.adminPass = "123456";
    });
    $("#gBrand").textContent = $("#sBrand").textContent = db.settings.brandAr;
    toast("الإعدادات اتحفظت ✅");
  });
  $("#expJson").onclick = () =>
    dl(new Blob([JSON.stringify(db, null, 2)], { type: "application/json" }), "lashera-backup.json");
  $("#impJson").onclick = () => $("#impFile").click();
  $("#impFile").onchange = (e) => {
    const f = e.target.files && e.target.files[0]; if (!f) return;
    const rd = new FileReader();
    rd.onload = () => {
      try {
        const o = JSON.parse(rd.result);
        if (!o || typeof o !== "object") throw 0;
        db = LStore.set(o); toast("النسخة اترجّعت ✅");
      } catch (err) { toast("الملف مش مظبوط"); }
    };
    rd.readAsText(f);
    e.target.value = "";
  };
  $("#resetAll").onclick = () => {
    if (!confirm("هترجّع كل حاجة زي ما كانت من الأول؟")) return;
    LStore.reset(); db = LStore.get(); toast("رجع للأصل");
  };

  /* ---------- تشغيل ---------- */
  function renderAll() { renderHome(); renderProds(); renderItems(); renderOrds(); renderSet(); }
  LStore.on(() => { db = LStore.get(); if ($("#app").classList.contains("on")) renderAll(); });
})();
