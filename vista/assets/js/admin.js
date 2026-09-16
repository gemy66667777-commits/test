/* فيستا إيفينت — لوحة التحكم */
(function () {
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  const ar = (n) => Number(n || 0).toLocaleString("ar-EG");
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const SK = "vista.admin";
  let db = VStore.get();

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
    star:  sv('<path d="m12 3.4 2.6 5.4 5.9.8-4.3 4.2 1 5.9L12 17l-5.2 2.7 1-5.9-4.3-4.2 5.9-.8z"/>')
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
  function pickImg(cb) {
    const f = document.createElement("input");
    f.type = "file"; f.accept = "image/*";
    f.onchange = () => {
      const file = f.files && f.files[0]; if (!file) return;
      const rd = new FileReader(); rd.onload = () => cb(rd.result); rd.readAsDataURL(file);
    };
    f.click();
  }
  function fmt(iso) {
    try { const d = new Date(iso);
      return d.toLocaleDateString("ar-EG", { day: "numeric", month: "short" }) + " · " +
             d.toLocaleTimeString("ar-EG", { hour: "2-digit", minute: "2-digit" });
    } catch (e) { return "—"; }
  }
  const nameOf = (arr, id) => (arr.filter((x) => x.id === id)[0] || {}).name || "—";

  /* ---------- الدخول ---------- */
  $("#gBrand").textContent = db.settings.brandAr;
  $("#sBrand").textContent = db.settings.brandAr;
  $("#gForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const u = digits($("#gUser").value), p = $("#gPass").value;
    const ok = u && digits(db.settings.phone).endsWith(u.slice(-9)) && p === db.settings.adminPass;
    if (ok) { try { sessionStorage.setItem(SK, $("#gUser").value); } catch (err) {} enter(); }
    else {
      const er = $("#gErr"); er.textContent = "الرقم أو كلمة السر غلط. جرّب تاني.";
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

  $$(".tab").forEach((t) => t.addEventListener("click", () => {
    $$(".tab").forEach((x) => x.classList.toggle("on", x === t));
    $$(".panel").forEach((p) => p.classList.toggle("on", p.id === "p-" + t.dataset.tab));
    document.body.classList.remove("nav"); scrollTo({ top: 0 });
  }));
  $$(".mob").forEach((b) => (b.onclick = () => document.body.classList.toggle("nav")));

  /* ================= نظرة عامة ================= */
  const chip = (s) => `<span class="chip ${{ "جديد": "c-new", "مؤكد": "c-ok", "تم": "c-done", "ملغي": "c-no" }[s] || "c-new"}">${esc(s)}</span>`;
  function renderHome() {
    const b = db.bookings;
    const kpi = (ic, n, lbl) => `<div class="kpi"><span class="ic">${I[ic]}</span><b>${n}</b><small>${lbl}</small></div>`;
    $("#kpis").innerHTML =
      kpi("image", ar(db.gallery.length), "صورة في المعرض") +
      kpi("box",   ar(db.packages.length), "كوشة معروضة") +
      kpi("cal",   ar(b.length), "إجمالي الحجوزات") +
      kpi("star",  ar(b.filter((x) => x.status === "جديد").length), "طلب جديد محتاج رد");

    const last = b.slice(0, 6);
    $("#lastBooks").innerHTML = last.length ? `<table><thead><tr>
        <th>العميلة</th><th>المناسبة</th><th>التاريخ</th><th>الحالة</th></tr></thead><tbody>` +
      last.map((x) => `<tr>
        <td><span class="nm">${esc(x.name)}</span><small dir="ltr">${esc(x.phone)}</small></td>
        <td>${esc(x.type)}<small>${esc(x.pkg || "—")}</small></td>
        <td>${esc(x.date || fmt(x.at))}</td><td>${chip(x.status)}</td></tr>`).join("") + "</tbody></table>"
      : `<div class="blank"><b>لسه مفيش حجوزات</b>أول طلب من الموقع هيظهر هنا.</div>`;

    const by = {};
    b.forEach((x) => (by[x.type] = (by[x.type] || 0) + 1));
    const keys = Object.keys(by).sort((a, c) => by[c] - by[a]);
    const max = Math.max(1, ...keys.map((k) => by[k]));
    $("#chart").innerHTML = keys.length ? keys.map((k) =>
      `<div class="bar"><span>${esc(k)}</span><span class="t"><i style="width:${(by[k] / max) * 100}%"></i></span><span class="v">${ar(by[k])}</span></div>`
    ).join("") : `<div class="blank" style="padding:30px"><b>مفيش بيانات لسه</b></div>`;
  }

  /* ================= المعرض ================= */
  function renderItems() {
    const g = db.gallery;
    $("#nItems").textContent = ar(g.length);
    $("#mgrid").innerHTML = g.length ? g.map((it, i) => `
      <article class="mcard">
        <div class="ph"><img src="${esc(it.img)}" alt="${esc(it.cap)}" loading="lazy"></div>
        <div class="bd"><b>${esc(it.cap)}</b>
          <small>${esc(nameOf(db.shapes, it.shape))} · ${esc(nameOf(db.lights, it.light))} · ${esc(nameOf(db.flowers, it.fl))}</small></div>
        <div class="bar2">
          <button class="ib" data-ed="${i}" title="تعديل">${I.edit}</button>
          <button class="ib" data-mv="${i}" data-d="-1" title="تقديم">${I.up}</button>
          <button class="ib" data-mv="${i}" data-d="1" title="تأخير">${I.down}</button>
          <button class="ib del" data-del="${i}" title="حذف" style="margin-inline-start:auto">${I.trash}</button>
        </div></article>`).join("")
      : `<div class="blank" style="grid-column:1/-1"><b>المعرض فاضي</b>ابدأ بإضافة أول صورة.</div>`;
    $$("#mgrid [data-ed]").forEach((b) => (b.onclick = () => itemForm(+b.dataset.ed)));
    $$("#mgrid [data-mv]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.mv, j = i + +b.dataset.d;
      if (j < 0 || j >= db.gallery.length) return;
      db = VStore.patch((d) => { const t = d.gallery[i]; d.gallery[i] = d.gallery[j]; d.gallery[j] = t; });
    }));
    $$("#mgrid [data-del]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.del;
      if (!confirm("تحذف الصورة دي؟")) return;
      db = VStore.patch((d) => d.gallery.splice(i, 1)); toast("اتحذفت");
    }));
  }
  $("#addItem").onclick = () => itemForm(-1);
  function itemForm(i) {
    const it = i < 0 ? { img: "assets/img/g-arch-blue.jpg", cap: "", shape: db.shapes[0].id, light: db.lights[0].id, fl: db.flowers[0].id }
                     : Object.assign({}, db.gallery[i]);
    const sel = (arr, cur) => arr.map((o) => `<option value="${esc(o.id)}" ${o.id === cur ? "selected" : ""}>${esc(o.name)}</option>`).join("");
    openModal(`
      <h3>${i < 0 ? "صورة جديدة" : "تعديل الصورة"}</h3>
      <p class="sub">التصنيف ده اللي «صمّم كوشتك» بيدوّر بيه، فخليه مظبوط.</p>
      <div class="field"><label>الصورة</label>
        <div class="drop" id="mPick"><img id="mImg" src="${esc(it.img)}" alt="">
          <div>اضغط لاختيار صورة من جهازك</div></div></div>
      <div class="field"><label>الوصف اللي تحت الصورة</label><input id="mCap" value="${esc(it.cap)}" placeholder="مثال: كوشة دائرية بورد أبيض وإضاءة زرقا">
        <div class="hint">اكتب اللي شايفه في الصورة بالظبط</div></div>
      <div class="grid3">
        <div class="field"><label>الشكل</label><select id="mShape">${sel(db.shapes, it.shape)}</select></div>
        <div class="field"><label>الإضاءة</label><select id="mLight">${sel(db.lights, it.light)}</select></div>
        <div class="field"><label>الورد</label><select id="mFl">${sel(db.flowers, it.fl)}</select></div>
      </div>
      <div class="modal-acts"><button class="btn ghost" id="mC">إلغاء</button><button class="btn" id="mS">حفظ</button></div>`);
    let img = it.img;
    $("#mPick").onclick = () => pickImg((d) => { img = d; $("#mImg").src = d; });
    $("#mC").onclick = closeModal;
    $("#mS").onclick = () => {
      const rec = { img: img, cap: $("#mCap").value.trim() || "صورة",
        shape: $("#mShape").value, light: $("#mLight").value, fl: $("#mFl").value };
      db = VStore.patch((d) => { i < 0 ? d.gallery.push(rec) : (d.gallery[i] = rec); });
      closeModal(); toast("اتحفظ ✅");
    };
  }

  /* ================= الكوش ================= */
  function renderPkgs() {
    const ps = db.packages;
    $("#nPkgs").textContent = ar(ps.length);
    $("#pgrid").innerHTML = ps.length ? ps.map((p, i) => `
      <article class="mcard">
        <div class="ph"><img src="${esc(p.img)}" alt="${esc(p.name)}" loading="lazy"></div>
        <div class="bd"><b>${esc(p.name)}</b><small>${p.items.length} مكوّنات</small>
          <span class="pr">${esc(priceText(p.price))}</span></div>
        <div class="bar2">
          <button class="ib" data-ed="${i}" title="تعديل">${I.edit}</button>
          <button class="ib" data-mv="${i}" data-d="-1" title="تقديم">${I.up}</button>
          <button class="ib" data-mv="${i}" data-d="1" title="تأخير">${I.down}</button>
          <button class="ib del" data-del="${i}" title="حذف" style="margin-inline-start:auto">${I.trash}</button>
        </div></article>`).join("")
      : `<div class="blank" style="grid-column:1/-1"><b>مفيش كوش</b>ابدأ بإضافة أول كوشة.</div>`;
    $$("#pgrid [data-ed]").forEach((b) => (b.onclick = () => pkgForm(+b.dataset.ed)));
    $$("#pgrid [data-mv]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.mv, j = i + +b.dataset.d;
      if (j < 0 || j >= db.packages.length) return;
      db = VStore.patch((d) => { const t = d.packages[i]; d.packages[i] = d.packages[j]; d.packages[j] = t; });
    }));
    $$("#pgrid [data-del]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.del;
      if (!confirm("تحذف «" + db.packages[i].name + "»؟")) return;
      db = VStore.patch((d) => d.packages.splice(i, 1)); toast("اتحذفت");
    }));
  }
  $("#addPkg").onclick = () => pkgForm(-1);
  function pkgForm(i) {
    const p = i < 0 ? { id: "p" + Date.now(), name: "", img: "assets/img/g-arch-blue.jpg", price: 0, items: [] }
                    : JSON.parse(JSON.stringify(db.packages[i]));
    openModal(`
      <h3>${i < 0 ? "كوشة جديدة" : "تعديل كوشة"}</h3>
      <p class="sub">المكوّنات دي اللي بتظهر كنقط تحت اسم الكوشة.</p>
      <div class="field"><label>صورة الكوشة</label>
        <div class="drop" id="mPick"><img id="mImg" src="${esc(p.img)}" alt="">
          <div>اضغط لاختيار صورة من جهازك</div></div></div>
      <div class="field"><label>اسم الكوشة</label><input id="mName" value="${esc(p.name)}" placeholder="مثال: كوشة دائرية"></div>
      <div class="field"><label>المكوّنات (كل واحدة في سطر)</label>
        <textarea id="mItems" style="min-height:120px">${esc(p.items.join("\n"))}</textarea></div>
      <div class="field"><label>السعر</label><input id="mPrice" type="number" min="0" value="${Number(p.price) || 0}">
        <div class="hint">مش بيظهر غير لو فعّلت «إظهار الأسعار» من الإعدادات</div></div>
      <div class="modal-acts"><button class="btn ghost" id="mC">إلغاء</button><button class="btn" id="mS">حفظ</button></div>`);
    let img = p.img;
    $("#mPick").onclick = () => pickImg((d) => { img = d; $("#mImg").src = d; });
    $("#mC").onclick = closeModal;
    $("#mS").onclick = () => {
      const n = $("#mName").value.trim();
      if (!n) { $("#mName").focus(); return; }
      const rec = { id: p.id, name: n, img: img, price: Number($("#mPrice").value) || 0,
        items: $("#mItems").value.split("\n").map((x) => x.trim()).filter(Boolean) };
      db = VStore.patch((d) => { i < 0 ? d.packages.push(rec) : (d.packages[i] = rec); });
      closeModal(); toast("اتحفظ ✅");
    };
  }

  /* ================= الخدمات ================= */
  const ICONS = [["arch","كوشة"],["bulb","إضاءة"],["neon","نيون"],["flower","ورد"],["tree","حديقة"],["seat","كنبة"]];
  function renderSvcs() {
    $("#nSvcs").textContent = ar(db.services.length);
    $("#sgrid").innerHTML = db.services.map((s, i) => `
      <article class="mcard">
        <div class="bd" style="padding-top:18px"><b>${esc(s.n)}</b><small>${esc(s.t)}</small></div>
        <div class="bar2">
          <button class="ib" data-ed="${i}" title="تعديل">${I.edit}</button>
          <button class="ib" data-mv="${i}" data-d="-1" title="تقديم">${I.up}</button>
          <button class="ib" data-mv="${i}" data-d="1" title="تأخير">${I.down}</button>
          <button class="ib del" data-del="${i}" title="حذف" style="margin-inline-start:auto">${I.trash}</button>
        </div></article>`).join("");
    $$("#sgrid [data-ed]").forEach((b) => (b.onclick = () => svcForm(+b.dataset.ed)));
    $$("#sgrid [data-mv]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.mv, j = i + +b.dataset.d;
      if (j < 0 || j >= db.services.length) return;
      db = VStore.patch((d) => { const t = d.services[i]; d.services[i] = d.services[j]; d.services[j] = t; });
    }));
    $$("#sgrid [data-del]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.del;
      if (!confirm("تحذف «" + db.services[i].n + "»؟")) return;
      db = VStore.patch((d) => d.services.splice(i, 1)); toast("اتحذفت");
    }));
  }
  $("#addSvc").onclick = () => svcForm(-1);
  function svcForm(i) {
    const s = i < 0 ? { ic: "arch", n: "", t: "" } : Object.assign({}, db.services[i]);
    openModal(`
      <h3>${i < 0 ? "خدمة جديدة" : "تعديل خدمة"}</h3>
      <div class="grid2">
        <div class="field"><label>الاسم</label><input id="mN" value="${esc(s.n)}"></div>
        <div class="field"><label>الأيقونة</label><select id="mIc">${
          ICONS.map(([v, l]) => `<option value="${v}" ${v === s.ic ? "selected" : ""}>${l}</option>`).join("")
        }</select></div>
      </div>
      <div class="field"><label>الشرح</label><textarea id="mT" style="min-height:72px">${esc(s.t)}</textarea></div>
      <div class="modal-acts"><button class="btn ghost" id="mC">إلغاء</button><button class="btn" id="mS">حفظ</button></div>`);
    $("#mC").onclick = closeModal;
    $("#mS").onclick = () => {
      const n = $("#mN").value.trim();
      if (!n) { $("#mN").focus(); return; }
      const rec = { ic: $("#mIc").value, n: n, t: $("#mT").value.trim() };
      db = VStore.patch((d) => { i < 0 ? d.services.push(rec) : (d.services[i] = rec); });
      closeModal(); toast("اتحفظ ✅");
    };
  }

  /* ================= الحجوزات ================= */
  function renderBooks() {
    const flt = $("#fStatus").value;
    const rows = db.bookings.map((b, i) => ({ b, i })).filter(({ b }) => !flt || b.status === flt);
    $("#nBooks").textContent = ar(db.bookings.length);
    $("#bookTbl").innerHTML = rows.length ? `<table><thead><tr>
        <th>وصل</th><th>العميلة</th><th>المناسبة</th><th>المكان</th><th>الكوشة</th><th>ملاحظات</th><th>الحالة</th><th></th>
      </tr></thead><tbody>` + rows.map(({ b, i }) => `<tr>
        <td>${esc(fmt(b.at))}</td>
        <td><span class="nm">${esc(b.name)}</span><small dir="ltr">${esc(b.phone)}</small></td>
        <td>${esc(b.type)}<small>${esc(b.date || "—")}</small></td>
        <td>${esc(b.place)}</td><td>${esc(b.pkg)}</td><td>${esc(b.note || "—")}</td>
        <td><select data-st="${i}" class="stsel">${
          ["جديد","مؤكد","تم","ملغي"].map((s) => `<option ${s === b.status ? "selected" : ""}>${s}</option>`).join("")
        }</select></td>
        <td><button class="ib del" data-del="${i}">${I.trash}</button></td></tr>`).join("") + "</tbody></table>"
      : `<div class="blank"><b>مفيش حجوزات هنا</b>أول طلب من الموقع هيظهر في الجدول.</div>`;
    $$("#bookTbl [data-st]").forEach((s) => (s.onchange = () => {
      const i = +s.dataset.st;
      db = VStore.patch((d) => (d.bookings[i].status = s.value)); toast("الحالة اتغيّرت");
    }));
    $$("#bookTbl [data-del]").forEach((b) => (b.onclick = () => {
      db = VStore.patch((d) => d.bookings.splice(+b.dataset.del, 1)); toast("اتحذف");
    }));
  }
  $("#fStatus").onchange = renderBooks;
  $("#expCsv").onclick = () => {
    const rows = [["وصل", "الاسم", "الموبايل", "التاريخ", "المناسبة", "المكان", "الكوشة", "ملاحظات", "الحالة"]]
      .concat(db.bookings.map((x) => [x.at, x.name, x.phone, x.date, x.type, x.place, x.pkg, x.note, x.status]));
    const csv = "﻿" + rows.map((r) => r.map((c) =>
      '"' + String(c == null ? "" : c).replace(/"/g, '""') + '"').join(",")).join("\r\n");
    dl(new Blob([csv], { type: "text/csv;charset=utf-8" }), "vista-bookings.csv");
  };
  function dl(blob, name) {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 900);
  }

  /* ================= الإعدادات ================= */
  const KEYS = ["brandAr","brand","intro","area","hours","phone","whats","priceNote","priceHint","currency","adminPass"];
  const F = $("#setForm");
  function renderSet() {
    const s = db.settings;
    KEYS.forEach((k) => { if (F.elements[k]) F.elements[k].value = s[k] == null ? "" : s[k]; });
    F.elements.showPrices.checked = !!s.showPrices;
  }
  F.addEventListener("submit", (e) => {
    e.preventDefault();
    const el = e.target.elements;
    db = VStore.patch((d) => {
      KEYS.forEach((k) => { if (el[k]) d.settings[k] = el[k].value.trim(); });
      d.settings.whats = digits(d.settings.whats);
      d.settings.showPrices = el.showPrices.checked;
      if (!d.settings.adminPass) d.settings.adminPass = "123456";
    });
    $("#gBrand").textContent = $("#sBrand").textContent = db.settings.brandAr;
    toast("الإعدادات اتحفظت ✅");
  });
  $("#expJson").onclick = () =>
    dl(new Blob([JSON.stringify(db, null, 2)], { type: "application/json" }), "vista-backup.json");
  $("#impJson").onclick = () => $("#impFile").click();
  $("#impFile").onchange = (e) => {
    const f = e.target.files && e.target.files[0]; if (!f) return;
    const rd = new FileReader();
    rd.onload = () => {
      try {
        const o = JSON.parse(rd.result);
        if (!o || typeof o !== "object") throw 0;
        db = VStore.set(o); toast("النسخة اترجّعت ✅");
      } catch (err) { toast("الملف مش مظبوط"); }
    };
    rd.readAsText(f); e.target.value = "";
  };
  $("#resetAll").onclick = () => {
    if (!confirm("هترجّع كل حاجة زي ما كانت من الأول؟")) return;
    VStore.reset(); db = VStore.get(); toast("رجع للأصل");
  };

  function renderAll() { renderHome(); renderItems(); renderPkgs(); renderSvcs(); renderBooks(); renderSet(); }
  VStore.on(() => { db = VStore.get(); if ($("#app").classList.contains("on")) renderAll(); });
})();
