/* ليالي بارتي — لوحة التحكم */
(function () {
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  const ar = (n) => Number(n || 0).toLocaleString("ar-EG");
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const S = Store;

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
    phone: sv('<path d="M6.6 3.5h3l1.5 3.8-2 1.4a12 12 0 0 0 6.2 6.2l1.4-2 3.8 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.6 5.7a2 2 0 0 1 2-2.2z"/>'),
    wa:    sv('<path d="M20.5 11.6a8.4 8.4 0 0 1-12.4 7.4L3.5 20.5l1.6-4.5A8.4 8.4 0 1 1 20.5 11.6z"/>'),
    star:  sv('<path d="m12 3.4 2.6 5.4 5.9.8-4.3 4.2 1 5.9L12 17l-5.2 2.7 1-5.9-4.3-4.2 5.9-.8z"/>'),
    users: sv('<circle cx="9" cy="8.2" r="3.4"/><path d="M2.8 20.2a6.2 6.2 0 0 1 12.4 0"/><path d="M16.2 5.2a3.4 3.4 0 0 1 0 6.6M17.6 14.6a6.2 6.2 0 0 1 3.6 5.6"/>'),
    money: sv('<rect x="2.8" y="5.6" width="18.4" height="12.8" rx="2.5"/><circle cx="12" cy="12" r="2.8"/><path d="M6.2 9.4v5.2M17.8 9.4v5.2"/>')
  };
  $$("[data-icon]").forEach((el) => (el.innerHTML = I[el.dataset.icon] || ""));

  /* ---------- توست ---------- */
  let tT;
  function toast(msg) {
    const t = $("#toast"); t.textContent = msg; t.classList.add("on");
    clearTimeout(tT); tT = setTimeout(() => t.classList.remove("on"), 2600);
  }

  /* ---------- نافذة ---------- */
  const modal = $("#modal"), mbox = $("#modalBox");
  function openModal(html) { mbox.innerHTML = html; modal.classList.add("on"); document.body.style.overflow = "hidden"; }
  function closeModal() { modal.classList.remove("on"); document.body.style.overflow = ""; }
  modal.addEventListener("click", (e) => { if (e.target === modal) closeModal(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeModal(); });

  /* ---------- الدخول ---------- */
  $("#gBrand").textContent = S.s.brand;
  $("#sBrand").textContent = S.s.brand;
  $("#gForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const err = $("#gErr");
    if (S.login($("#gUser").value, $("#gPass").value)) { enter(); }
    else { err.textContent = "الرقم أو كلمة السر غلط. جرّب تاني."; err.classList.add("on"); $("#gPass").value = ""; }
  });
  function enter() {
    $("#gate").style.display = "none";
    $("#app").classList.add("on");
    $("#whoami").textContent = "داخلة برقم " + S.session();
    renderAll();
  }
  $("#logout").onclick = () => { S.logout(); location.reload(); };
  if (S.session()) enter();

  /* ---------- التبويبات ---------- */
  $$(".tab").forEach((t) => t.addEventListener("click", () => {
    $$(".tab").forEach((x) => x.classList.toggle("on", x === t));
    $$(".panel").forEach((p) => p.classList.toggle("on", p.id === "p-" + t.dataset.tab));
    document.body.classList.remove("nav");
    scrollTo({ top: 0 });
  }));
  $$(".mob").forEach((b) => (b.onclick = () => document.body.classList.toggle("nav")));

  /* ================= نظرة عامة ================= */
  function renderHome() {
    const b = S.data.bookings;
    const neu = b.filter((x) => x.status === "جديد").length;
    const kpi = (ic, n, lbl) => `<div class="kpi"><span class="ic">${I[ic]}</span><b>${n}</b><small>${lbl}</small></div>`;
    $("#kpis").innerHTML =
      kpi("image", ar(S.data.items.length), "عمل في المعرض") +
      kpi("box",   ar(S.data.packages.length), "عرض معروض") +
      kpi("cal",   ar(b.length), "إجمالي الحجوزات") +
      kpi("star",  ar(neu), "طلب جديد محتاج رد");

    const last = b.slice(0, 6);
    $("#lastBooks").innerHTML = last.length ? `<table><thead><tr>
        <th>العميلة</th><th>المناسبة</th><th>التاريخ</th><th>الحالة</th></tr></thead><tbody>` +
      last.map((x) => `<tr>
        <td><span class="nm">${esc(x.name)}</span><small dir="ltr">${esc(x.phone)}</small></td>
        <td>${esc(x.type)}<small>${esc(x.pkg || "—")}</small></td>
        <td>${esc(x.date || "—")}</td>
        <td>${chip(x.status)}</td></tr>`).join("") + "</tbody></table>"
      : `<div class="blank"><b>لسه مفيش حجوزات</b>أول طلب يجي من الموقع هيظهر هنا.</div>`;

    const by = {};
    b.forEach((x) => (by[x.type] = (by[x.type] || 0) + 1));
    const keys = Object.keys(by).sort((a, c) => by[c] - by[a]);
    const max = Math.max(1, ...keys.map((k) => by[k]));
    $("#chart").innerHTML = keys.length ? keys.map((k) =>
      `<div class="bar"><span>${esc(k)}</span><span class="t"><i style="width:${(by[k] / max) * 100}%"></i></span><span class="v">${ar(by[k])}</span></div>`
    ).join("") : `<div class="blank" style="padding:30px"><b>مفيش بيانات لسه</b></div>`;
  }
  const chip = (s) => `<span class="chip ${{ "جديد": "c-new", "مؤكد": "c-ok", "تم": "c-done", "ملغي": "c-no" }[s] || "c-new"}">${esc(s)}</span>`;

  /* ================= المعرض ================= */
  function renderItems() {
    const its = S.data.items;
    $("#nItems").textContent = ar(its.length);
    $("#mgrid").innerHTML = its.length ? its.map((it, i) => `
      <article class="mcard">
        <div class="ph">${it.featured ? `<span class="fav">مميز</span>` : ""}
          <img src="${esc(S.thumbFor(it))}" alt="${esc(it.name)}" loading="lazy"></div>
        <div class="bd"><b>${esc(it.name)}</b><small>${esc(it.cat)}</small>
          <span class="pr">${esc(S.priceText(it.price))}</span></div>
        <div class="bar2">
          <button class="ib" data-ed="${i}" title="تعديل">${I.edit}</button>
          <button class="ib" data-mv="${i}" data-d="-1" title="تقديم">${I.up}</button>
          <button class="ib" data-mv="${i}" data-d="1" title="تأخير">${I.down}</button>
          <button class="ib del" data-del="${i}" title="حذف" style="margin-inline-start:auto">${I.trash}</button>
        </div>
      </article>`).join("")
      : `<div class="blank" style="grid-column:1/-1"><b>المعرض فاضي</b>ابدأ بإضافة أول عمل.</div>`;

    $$("#mgrid [data-ed]").forEach((b) => (b.onclick = () => itemModal(+b.dataset.ed)));
    $$("#mgrid [data-mv]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.mv, j = i + +b.dataset.d;
      if (j < 0 || j >= its.length) return;
      [its[i], its[j]] = [its[j], its[i]]; S.save(); toast("اتغير الترتيب");
    }));
    $$("#mgrid [data-del]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.del;
      if (!confirm(`تحذف «${its[i].name}» من المعرض؟`)) return;
      its.splice(i, 1); S.save(); toast("اتحذف");
    }));
  }

  function itemModal(i) {
    const isNew = i == null;
    const it = isNew ? { id: S.uid("g"), name: "", cat: S.cats()[0] || "كتب كتاب", desc: "", price: 0, featured: false, slug: "", img: "" } : S.data.items[i];
    openModal(`
      <h3>${isNew ? "إضافة عمل" : "تعديل العمل"}</h3>
      <p class="sub">الاسم والسعر دول اللي بيظهروا تحت الصورة في الموقع.</p>
      <div class="field"><label>صورة العمل</label>
        <div class="drop" id="drop">${it.img || it.slug ? `<img src="${esc(S.thumbFor(it))}" alt="">` : ""}
          <div>اضغط لاختيار صورة من جهازك</div></div>
        <input type="file" id="pick" accept="image/*" hidden></div>
      <div class="field"><label>اسم المنتج</label><input id="fName" value="${esc(it.name)}" placeholder="مثال: كوشة دايرة بنيون آية"></div>
      <div class="grid2">
        <div class="field"><label>القسم</label><input id="fCat" value="${esc(it.cat)}" list="cats">
          <datalist id="cats">${S.cats().map((c) => `<option>${esc(c)}</option>`).join("")}</datalist></div>
        <div class="field"><label>السعر</label><input id="fPrice" type="number" min="0" value="${Number(it.price) || 0}">
          <div class="hint">سيبه ٠ عشان يظهر «${esc(S.s.priceLabel)}»</div></div>
      </div>
      <div class="field"><label>وصف مختصر</label><textarea id="fDesc" style="min-height:70px">${esc(it.desc)}</textarea></div>
      <label class="sw"><input type="checkbox" id="fFav" ${it.featured ? "checked" : ""}>
        <span><b>عمل مميز</b><small>يتعلّم عليه بعلامة في اللوحة</small></span></label>
      <div class="modal-acts">
        <button class="btn ghost" id="mCancel">إلغاء</button>
        <button class="btn" id="mSave">حفظ</button>
      </div>`);

    let img = it.img || "";
    $("#drop").onclick = () => $("#pick").click();
    $("#pick").onchange = (e) => {
      const f = e.target.files[0]; if (!f) return;
      if (f.size > 2.6e6) return toast("الصورة كبيرة — خليها أقل من ٢.٥ ميجا");
      const r = new FileReader();
      r.onload = () => { img = r.result; $("#drop").innerHTML = `<img src="${img}" alt=""><div>اضغط لتغيير الصورة</div>`; };
      r.readAsDataURL(f);
    };
    $("#mCancel").onclick = closeModal;
    $("#mSave").onclick = () => {
      const name = $("#fName").value.trim();
      if (!name) return toast("اكتب اسم المنتج الأول");
      if (!it.slug && !img && !it.img) return toast("اختار صورة للعمل");
      Object.assign(it, {
        name, cat: $("#fCat").value.trim() || "متنوع",
        desc: $("#fDesc").value.trim(), price: Math.max(0, +$("#fPrice").value || 0),
        featured: $("#fFav").checked, img: img || it.img || ""
      });
      if (isNew) S.data.items.push(it);
      S.save(); closeModal(); toast(isNew ? "اتضاف للمعرض" : "اتحفظ");
    };
  }
  $("#addItem").onclick = () => itemModal(null);

  /* ================= الباقات ================= */
  function renderPkgs() {
    const ps = S.data.packages;
    $("#nPkgs").textContent = ar(ps.length);
    $("#pgrid").innerHTML = ps.length ? ps.map((p, i) => `
      <article class="mcard">
        <div class="bd" style="padding:20px">
          ${p.badge ? `<span class="chip c-done" style="align-self:flex-start;margin-bottom:8px">${esc(p.badge)}</span>` : ""}
          <b style="font-size:1.5rem">${esc(p.name)}</b>
          <small>${esc(p.sub)}</small>
          <span class="pr">${esc(S.priceText(p.price))} · ${esc(p.guests || "")}</span>
          <small style="margin-top:8px">${ar((p.features || []).length)} مميزات</small>
        </div>
        <div class="bar2">
          <button class="ib" data-ed="${i}" title="تعديل">${I.edit}</button>
          <button class="ib" data-mv="${i}" data-d="-1">${I.up}</button>
          <button class="ib" data-mv="${i}" data-d="1">${I.down}</button>
          <button class="ib del" data-del="${i}" style="margin-inline-start:auto">${I.trash}</button>
        </div>
      </article>`).join("")
      : `<div class="blank" style="grid-column:1/-1"><b>مفيش باقات</b>ضيف أول باقة.</div>`;

    $$("#pgrid [data-ed]").forEach((b) => (b.onclick = () => pkgModal(+b.dataset.ed)));
    $$("#pgrid [data-mv]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.mv, j = i + +b.dataset.d;
      if (j < 0 || j >= ps.length) return;
      [ps[i], ps[j]] = [ps[j], ps[i]]; S.save(); toast("اتغير الترتيب");
    }));
    $$("#pgrid [data-del]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.del;
      if (!confirm(`تحذف عرض «${ps[i].name}»؟`)) return;
      ps.splice(i, 1); S.save(); toast("اتحذفت");
    }));
  }

  function pkgModal(i) {
    const isNew = i == null;
    const p = isNew ? { id: S.uid("pkg"), name: "", sub: "", desc: "", price: 0, guests: "", badge: "", features: [] } : S.data.packages[i];
    openModal(`
      <h3>${isNew ? "عرض جديد" : "تعديل العرض"}</h3>
      <p class="sub">سمّيها اسم يتفكر — ده اللي بيفضل في دماغ العميل.</p>
      <div class="grid2">
        <div class="field"><label>اسم العرض</label><input id="pName" value="${esc(p.name)}" placeholder="مثال: العرض الرابع"></div>
        <div class="field"><label>الجملة تحت الاسم</label><input id="pSub" value="${esc(p.sub)}"></div>
      </div>
      <div class="field"><label>وصف مختصر</label><textarea id="pDesc" style="min-height:66px">${esc(p.desc)}</textarea></div>
      <div class="grid3">
        <div class="field"><label>السعر</label><input id="pPrice" type="number" min="0" value="${Number(p.price) || 0}"></div>
        <div class="field"><label>عدد الضيوف</label><input id="pGuests" value="${esc(p.guests)}"></div>
        <div class="field"><label>ملصق مميز</label><input id="pBadge" value="${esc(p.badge)}" placeholder="اختياري"></div>
      </div>
      <div class="field"><label>المميزات — كل ميزة في سطر</label>
        <textarea id="pFeat" style="min-height:150px">${esc((p.features || []).join("\n"))}</textarea></div>
      <div class="modal-acts">
        <button class="btn ghost" id="mCancel">إلغاء</button>
        <button class="btn" id="mSave">حفظ</button>
      </div>`);
    $("#mCancel").onclick = closeModal;
    $("#mSave").onclick = () => {
      const name = $("#pName").value.trim();
      if (!name) return toast("العرض محتاج اسم");
      Object.assign(p, {
        name, sub: $("#pSub").value.trim(), desc: $("#pDesc").value.trim(),
        price: Math.max(0, +$("#pPrice").value || 0), guests: $("#pGuests").value.trim(),
        badge: $("#pBadge").value.trim(),
        features: $("#pFeat").value.split("\n").map((s) => s.trim()).filter(Boolean)
      });
      if (isNew) S.data.packages.push(p);
      S.save(); closeModal(); toast(isNew ? "اتضاف العرض" : "اتحفظت");
    };
  }
  $("#addPkg").onclick = () => pkgModal(null);

  /* ================= الحجوزات ================= */
  function renderBooks() {
    const all = S.data.bookings;
    const f = $("#fStatus").value;
    const rows = f ? all.filter((b) => b.status === f) : all;
    $("#nBooks").textContent = ar(all.filter((b) => b.status === "جديد").length);

    $("#bookTbl").innerHTML = rows.length ? `<table><thead><tr>
      <th>العميلة</th><th>المناسبة</th><th>الميعاد</th><th>المكان</th><th>الباقة</th><th>الحالة</th><th>وصل</th><th></th>
      </tr></thead><tbody>` + rows.map((b) => {
        const k = all.indexOf(b);
        const wa = String(b.phone).replace(/\D/g, "").replace(/^0/, "20");
        return `<tr>
        <td><span class="nm">${esc(b.name)}</span><small dir="ltr">${esc(b.phone)}</small></td>
        <td>${esc(b.type)}${b.note ? `<small title="${esc(b.note)}">${esc(b.note.slice(0, 34))}${b.note.length > 34 ? "…" : ""}</small>` : ""}</td>
        <td>${esc(b.date || "—")}</td>
        <td>${esc(b.place || "—")}</td>
        <td>${esc(b.pkg || "—")}</td>
        <td><select data-st="${k}">
          ${["جديد", "مؤكد", "تم", "ملغي"].map((s) => `<option${s === b.status ? " selected" : ""}>${s}</option>`).join("")}
        </select></td>
        <td><small>${new Date(b.created).toLocaleDateString("ar-EG")}</small></td>
        <td><div class="acts">
          <a class="ib" href="tel:${esc(b.phone)}" title="اتصال">${I.phone}</a>
          <a class="ib" href="https://wa.me/${wa}" target="_blank" rel="noopener" title="واتساب">${I.wa}</a>
          <button class="ib del" data-del="${k}" title="حذف">${I.trash}</button>
        </div></td></tr>`; }).join("") + "</tbody></table>"
      : `<div class="blank"><b>مفيش حجوزات ${f ? "بالحالة دي" : "لسه"}</b>الطلبات اللي بتيجي من الموقع بتظهر هنا فورًا.</div>`;

    $$("#bookTbl [data-st]").forEach((s) => (s.onchange = () => {
      all[+s.dataset.st].status = s.value; S.save(); toast("اتحدثت الحالة");
    }));
    $$("#bookTbl [data-del]").forEach((b) => (b.onclick = () => {
      if (!confirm("تحذف الطلب ده؟")) return;
      all.splice(+b.dataset.del, 1); S.save(); toast("اتحذف");
    }));
  }
  $("#fStatus").onchange = renderBooks;

  function dl(blob, name) {
    const u = URL.createObjectURL(blob), a = document.createElement("a");
    a.href = u; a.download = name; a.click(); setTimeout(() => URL.revokeObjectURL(u), 1500);
  }
  $("#expCsv").onclick = () => {
    const H = ["الاسم", "الموبايل", "المناسبة", "التاريخ", "المكان", "الباقة", "الحالة", "ملاحظات", "وصل في"];
    const q = (v) => `"${String(v == null ? "" : v).replace(/"/g, '""')}"`;
    const csv = "﻿" + [H.map(q).join(",")].concat(
      S.data.bookings.map((b) => [b.name, b.phone, b.type, b.date, b.place, b.pkg, b.status, b.note, new Date(b.created).toLocaleString("ar-EG")].map(q).join(","))
    ).join("\n");
    dl(new Blob([csv], { type: "text/csv;charset=utf-8" }), "laialy-bookings.csv");
    toast("اتنزل الملف");
  };

  /* ================= الإعدادات ================= */
  function renderSet() {
    const s = S.s, f = $("#setForm").elements;
    f.brand.value = s.brand; f.latin.value = s.latin; f.tagline.value = s.tagline; f.intro.value = s.intro;
    f.p0.value = s.phones[0] || ""; f.p1.value = s.phones[1] || ""; f.p2.value = s.phones[2] || "";
    f.whatsapp.value = s.whatsapp; f.hours.value = s.hours; f.address.value = s.address;
    f.showPrices.checked = !!s.showPrices; f.priceLabel.value = s.priceLabel; f.adminPass.value = s.adminPass;
  }
  $("#setForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const f = e.target.elements, s = S.s;
    const phones = [f.p0.value, f.p1.value, f.p2.value].map((x) => x.trim()).filter(Boolean);
    if (!phones.length) return toast("لازم رقم واحد على الأقل");
    if (!f.adminPass.value.trim()) return toast("كلمة السر مينفعش تبقى فاضية");
    Object.assign(s, {
      brand: f.brand.value.trim() || s.brand, latin: f.latin.value.trim(),
      tagline: f.tagline.value.trim(), intro: f.intro.value.trim(),
      phones, adminPhones: phones, whatsapp: f.whatsapp.value.trim(),
      hours: f.hours.value.trim(), address: f.address.value.trim(),
      showPrices: f.showPrices.checked, priceLabel: f.priceLabel.value.trim() || "السعر عند الطلب",
      adminPass: f.adminPass.value.trim()
    });
    S.save();
    $("#sBrand").textContent = s.brand;
    toast("اتحفظت الإعدادات ✦ الموقع اتحدّث");
  });

  $("#expJson").onclick = () => { dl(S.export(), "laialy-backup.json"); toast("اتنزلت النسخة"); };
  $("#impJson").onclick = () => $("#impFile").click();
  $("#impFile").onchange = (e) => {
    const f = e.target.files[0]; if (!f) return;
    const r = new FileReader();
    r.onload = () => { try { S.import(r.result); toast("اترجعت النسخة"); } catch (x) { toast("الملف مش متوافق"); } };
    r.readAsText(f); e.target.value = "";
  };
  $("#resetAll").onclick = () => {
    if (!confirm("هيترجع كل حاجة لأصلها وتتمسح كل التعديلات والحجوزات. متأكد؟")) return;
    S.reset(); renderSet(); toast("رجع الوضع الأصلي");
  };

  /* ---------- تشغيل ---------- */
  function renderAll() { renderHome(); renderItems(); renderPkgs(); renderBooks(); renderSet(); }
  document.addEventListener("laialy:change", () => { renderHome(); renderItems(); renderPkgs(); renderBooks(); });
})();
