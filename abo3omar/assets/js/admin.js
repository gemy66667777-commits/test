/* مول السعدني — لوحة التحكم */
(function () {
  const $  = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  const ar = (n) => Number(n || 0).toLocaleString("ar-EG");
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const SK = "abo3omar.admin";
  let db = AStore.get();

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
    pin:   sv('<path d="M12 21.5s7-6 7-11a7 7 0 1 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10.4" r="2.6"/>'),
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
  const cur = () => db.settings.currency || "";
  function priceText(p) {
    const s = db.settings;
    if (!s.showPrices || !Number(p)) return s.priceNote;
    return ar(p) + " " + cur();
  }
  const prod = (id) => db.products.filter((p) => p.id === id)[0];
  const thumb = (src, alt) => src
    ? `<img src="${esc(src)}" alt="${esc(alt || "")}" loading="lazy">`
    : `<span class="noimg">صورة قريبًا</span>`;

  /* حساب العرض */
  function calcOffer(o) {
    let sum = 0, pcs = 0, n = 0;
    (o.items || []).forEach((it) => {
      const p = prod(it.id); if (!p) return;
      const q = Number(it.q) || 1;
      sum += (Number(p.price) || 0) * q; pcs += q; n++;
    });
    return { sum, pcs, n, was: Number(o.was) || sum, pieces: Number(o.pieces) || pcs };
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
      if (file.size > 1.6 * 1024 * 1024) toast("الصورة كبيرة — يفضّل أقل من ١٫٥ ميجا");
      const rd = new FileReader();
      rd.onload = () => cb(rd.result);
      rd.readAsDataURL(file);
    };
    f.click();
  }
  function fmt(iso) {
    try { const d = new Date(iso);
      return d.toLocaleDateString("ar-EG", { day: "numeric", month: "short" }) + " · " +
             d.toLocaleTimeString("ar-EG", { hour: "2-digit", minute: "2-digit" });
    } catch (e) { return "—"; }
  }
  const rowBar = (i, key) => `<div class="bar2">
      <button class="ib" data-ed="${i}" title="تعديل">${I.edit}</button>
      <button class="ib" data-mv="${i}" data-d="-1" title="تقديم">${I.up}</button>
      <button class="ib" data-mv="${i}" data-d="1" title="تأخير">${I.down}</button>
      <button class="ib del" data-del="${i}" title="حذف" style="margin-inline-start:auto">${I.trash}</button>
    </div>`;
  function wire(root, key, form, label) {
    $$(root + " [data-ed]").forEach((b) => (b.onclick = () => form(+b.dataset.ed)));
    $$(root + " [data-mv]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.mv, j = i + +b.dataset.d;
      if (j < 0 || j >= db[key].length) return;
      db = AStore.patch((d) => { const t = d[key][i]; d[key][i] = d[key][j]; d[key][j] = t; });
    }));
    $$(root + " [data-del]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.del;
      if (!confirm("تحذف " + label(db[key][i]) + "؟")) return;
      db = AStore.patch((d) => d[key].splice(i, 1)); toast("اتحذف");
    }));
  }

  /* ================= نظرة عامة ================= */
  function renderHome() {
    const o = db.orders;
    const noImg = db.products.filter((p) => !p.img).length;
    const kpi = (ic, n, lbl) => `<div class="kpi"><span class="ic">${I[ic]}</span><b>${n}</b><small>${lbl}</small></div>`;
    $("#kpis").innerHTML =
      kpi("box",   ar(db.products.length), "منتج معروض") +
      kpi("star",  ar(db.offers.length),   "عرض شغال") +
      kpi("cal",   ar(o.length),           "إجمالي الطلبات") +
      kpi("image", ar(noImg),              "صنف لسه من غير صورة");

    const last = o.slice(0, 7);
    $("#lastOrds").innerHTML = last.length ? `<table><thead><tr>
        <th>العميل</th><th>المطلوب</th><th>المنطقة</th><th>التاريخ</th></tr></thead><tbody>` +
      last.map((x) => `<tr>
        <td><span class="nm">${esc(x.name)}</span><small dir="ltr">${esc(x.phone)}</small></td>
        <td>${esc(x.item)}</td><td>${esc(x.area || "—")}</td>
        <td>${esc(fmt(x.at))}</td></tr>`).join("") + "</tbody></table>"
      : `<div class="blank"><b>لسه مفيش طلبات</b>أول طلب يجي من الموقع هيظهر هنا.</div>`;

    const by = {};
    o.forEach((x) => { const k = x.note || "—"; by[k] = (by[k] || 0) + 1; });
    const keys = Object.keys(by).sort((a, c) => by[c] - by[a]).slice(0, 8);
    const max = Math.max(1, ...keys.map((k) => by[k]));
    $("#chart").innerHTML = keys.length ? keys.map((k) =>
      `<div class="bar"><span>${esc(k)}</span><span class="t"><i style="width:${(by[k] / max) * 100}%"></i></span><span class="v">${ar(by[k])}</span></div>`
    ).join("") : `<div class="blank" style="padding:30px"><b>مفيش بيانات لسه</b></div>`;
  }

  /* ================= المنتجات ================= */
  const catName = (id) => (db.cats.filter((d) => d.id === id)[0] || {}).name || "—";
  function renderProds() {
    const ps = db.products;
    $("#nProds").textContent = ar(ps.length);
    $("#pgrid").innerHTML = ps.length ? ps.map((p, i) => `
      <article class="mcard">
        <div class="ph">${thumb(p.img, p.name)}</div>
        <div class="bd"><b>${esc(p.name)}</b><small>${esc(catName(p.cat))}</small>
          <span class="pr">${esc(priceText(p.price))}</span></div>
        ${rowBar(i)}
      </article>`).join("")
      : `<div class="blank" style="grid-column:1/-1"><b>مفيش منتجات</b>ابدأ بإضافة أول منتج.</div>`;
    wire("#pgrid", "products", prodForm, (x) => "«" + x.name + "»");
  }
  $("#addProd").onclick = () => prodForm(-1);

  function prodForm(i) {
    const p = i < 0
      ? { id: "p" + Date.now(), name: "", img: "", price: 0, cat: (db.cats[0] || {}).id, note: "" }
      : JSON.parse(JSON.stringify(db.products[i]));
    openModal(`
      <h3>${i < 0 ? "منتج جديد" : "تعديل منتج"}</h3>
      <p class="sub">سيب الصورة فاضية لو الصنف لسه مش متصوّر — هيظهر برسمة بديلة مكتوب عليها «الصورة قريبًا».</p>
      <div class="field"><label>صورة المنتج</label>
        <div class="drop" id="mPick">
          <div id="mImgW">${p.img ? `<img id="mImg" src="${esc(p.img)}" alt="">` : `<div class="noimg">من غير صورة</div>`}</div>
          <div>اضغط لاختيار صورة من جهازك</div></div>
        <div class="rowacts"><button type="button" class="btn ghost" id="mNoImg">شيل الصورة</button></div></div>
      <div class="field"><label>اسم المنتج</label><input id="mName" value="${esc(p.name)}" placeholder="مثال: دفاية تركي كبيرة"></div>
      <div class="field"><label>الوصف</label><textarea id="mNote" style="min-height:64px">${esc(p.note || "")}</textarea></div>
      <div class="grid2">
        <div class="field"><label>القسم</label><select id="mCat">${
          db.cats.map((d) => `<option value="${esc(d.id)}" ${d.id === p.cat ? "selected" : ""}>${esc(d.name)}</option>`).join("")
        }</select></div>
        <div class="field"><label>السعر</label><input id="mPrice" type="number" min="0" value="${Number(p.price) || 0}"></div>
      </div>
      <div class="modal-acts"><button class="btn ghost" id="mC">إلغاء</button><button class="btn" id="mS">حفظ</button></div>`);
    let img = p.img;
    const paintImg = () => {
      $("#mImgW").innerHTML = img ? `<img id="mImg" src="${esc(img)}" alt="">` : `<div class="noimg">من غير صورة</div>`;
    };
    $("#mPick").onclick = () => pickImg((d) => { img = d; paintImg(); });
    $("#mNoImg").onclick = (e) => { e.stopPropagation(); img = ""; paintImg(); };
    $("#mC").onclick = closeModal;
    $("#mS").onclick = () => {
      const n = $("#mName").value.trim();
      if (!n) { $("#mName").focus(); return; }
      const rec = { id: p.id, name: n, img: img, price: Number($("#mPrice").value) || 0,
        cat: $("#mCat").value, note: $("#mNote").value.trim() };
      db = AStore.patch((d) => { i < 0 ? d.products.push(rec) : (d.products[i] = rec); });
      closeModal(); toast("اتحفظ ✅");
    };
  }

  /* ================= العروض (بالكميات) ================= */
  function renderOffers() {
    const os = db.offers;
    $("#nOffers").textContent = ar(os.length);
    $("#ogrid").innerHTML = os.length ? os.map((o, i) => {
      const c = calcOffer(o);
      const save = c.was - Number(o.price || 0);
      const first = (o.items || []).map((it) => prod(it.id)).filter((p) => p && p.img)[0];
      return `<article class="mcard">
        <div class="ph">${o.feat ? `<span class="fav">مميّز</span>` : o.tag ? `<span class="fav">${esc(o.tag)}</span>` : ""}
          ${thumb(o.img || (first && first.img), o.name)}</div>
        <div class="bd"><b>${esc(o.name)}</b>
          <small>${ar(c.pieces)} جهاز · ${ar(c.n)} صنف · قبل ${ar(c.was)}</small>
          <span class="pr">${ar(o.price)} ${esc(cur())}${save > 0 ? ` — توفير ${ar(save)}` : ""}</span></div>
        ${rowBar(i)}</article>`; }).join("")
      : `<div class="blank" style="grid-column:1/-1"><b>مفيش عروض</b>ابدأ بإضافة أول عرض.</div>`;
    wire("#ogrid", "offers", offerForm, (x) => "«" + x.name + "»");
  }
  $("#addOffer").onclick = () => offerForm(-1);

  function offerForm(i) {
    const o = i < 0
      ? { id: "o" + Date.now(), name: "", sub: "", items: [], price: 0, tag: "", img: "", was: 0, pieces: 0, feat: false }
      : JSON.parse(JSON.stringify(db.offers[i]));
    const qOf = (id) => { const f = (o.items || []).filter((x) => x.id === id)[0]; return f ? f.q : 1; };
    const has  = (id) => (o.items || []).some((x) => x.id === id);

    openModal(`
      <h3>${i < 0 ? "عرض جديد" : "تعديل عرض"}</h3>
      <p class="sub">علّم على منتجات العرض واكتب كمية كل صنف — عدد القطع والسعر قبل العرض بيتحسبوا لوحدهم.</p>
      <div class="grid2">
        <div class="field"><label>اسم العرض</label><input id="oName" value="${esc(o.name)}" placeholder="مثال: عرض المولد ٢"></div>
        <div class="field"><label>الشارة (اختياري)</label><input id="oTag" value="${esc(o.tag || "")}" placeholder="العرض الرسمي"></div>
      </div>
      <div class="field"><label>الجملة تحت الاسم</label><input id="oSub" value="${esc(o.sub || "")}"></div>

      <label class="sw" style="margin-bottom:14px">
        <input type="checkbox" id="oFeat" ${o.feat ? "checked" : ""}>
        <span><b>العرض المميّز</b><small>بيظهر كبير فوق باقي العروض — واحد بس</small></span>
      </label>

      <div class="field"><label>بوستر العرض (اختياري)</label>
        <div class="drop" id="oPick">
          <div id="oImgW">${o.img ? `<img src="${esc(o.img)}" alt="">` : `<div class="noimg">من غير بوستر</div>`}</div>
          <div>اضغط لاختيار صورة من جهازك</div></div>
        <div class="rowacts"><button type="button" class="btn ghost" id="oNoImg">شيل البوستر</button></div></div>

      <div class="field"><label>منتجات العرض وكمياتها</label>
        <div id="oItems" class="picklist">${
          db.products.map((p) => `<label>
            <input type="checkbox" value="${esc(p.id)}" ${has(p.id) ? "checked" : ""}>
            ${p.img ? `<img src="${esc(p.img)}" alt="">` : `<span class="noimg">لا صورة</span>`}
            <b>${esc(p.name)}</b>
            <input class="qn" type="number" min="1" value="${qOf(p.id)}" ${has(p.id) ? "" : "disabled"}>
            <em>${ar(p.price)} ${esc(cur())}</em></label>`).join("")
        }</div></div>

      <div class="calc" id="oCalc"></div>

      <div class="grid2">
        <div class="field"><label>سعر العرض</label><input id="oPrice" type="number" min="0" value="${Number(o.price) || 0}"></div>
        <div class="field"><label>السعر قبل العرض</label><input id="oWas" type="number" min="0" value="${Number(o.was) || 0}">
          <div class="hint">سيبه صفر عشان يتحسب لوحده من أسعار المنتجات</div></div>
      </div>
      <div class="field"><label>عدد الأجهزة المكتوب</label><input id="oPieces" type="number" min="0" value="${Number(o.pieces) || 0}">
        <div class="hint">سيبه صفر عشان يتحسب لوحده من الكميات</div></div>

      <div class="modal-acts"><button class="btn ghost" id="mC">إلغاء</button><button class="btn" id="mS">حفظ</button></div>`);

    function read() {
      return $$("#oItems label").filter((l) => $("input[type=checkbox]", l).checked).map((l) => ({
        id: $("input[type=checkbox]", l).value,
        q: Math.max(1, Number($(".qn", l).value) || 1)
      }));
    }
    function recalc() {
      const items = read();
      const c = calcOffer({ items });
      const manualWas = Number($("#oWas").value) || 0;
      const manualPcs = Number($("#oPieces").value) || 0;
      let html = `<span>المحسوب:</span> <b>${ar(c.pcs)} جهاز</b> <span>·</span> <b>${ar(c.sum)} ${esc(cur())}</b>`;
      if (manualWas && Math.abs(manualWas - c.sum) > 0)
        html += ` <span class="warn">⚠ السعر المكتوب ${ar(manualWas)} مختلف عن المحسوب</span>`;
      if (manualPcs && manualPcs !== c.pcs)
        html += ` <span class="warn">⚠ عدد الأجهزة المكتوب ${ar(manualPcs)} مختلف عن المحسوب ${ar(c.pcs)}</span>`;
      $("#oCalc").innerHTML = html;
    }
    $$("#oItems label").forEach((l) => {
      const cb = $("input[type=checkbox]", l), qn = $(".qn", l);
      cb.onchange = () => { qn.disabled = !cb.checked; recalc(); };
      qn.oninput = recalc;
      qn.onclick = (e) => e.preventDefault();
    });
    $("#oWas").oninput = recalc; $("#oPieces").oninput = recalc;
    recalc();

    let img = o.img || "";
    const paintImg = () => {
      $("#oImgW").innerHTML = img ? `<img src="${esc(img)}" alt="">` : `<div class="noimg">من غير بوستر</div>`;
    };
    $("#oPick").onclick = () => pickImg((d) => { img = d; paintImg(); });
    $("#oNoImg").onclick = (e) => { e.stopPropagation(); img = ""; paintImg(); };

    $("#mC").onclick = closeModal;
    $("#mS").onclick = () => {
      const n = $("#oName").value.trim();
      if (!n) { $("#oName").focus(); return; }
      const feat = $("#oFeat").checked;
      const rec = { id: o.id, name: n, sub: $("#oSub").value.trim(), tag: $("#oTag").value.trim(),
        img: img, items: read(), price: Number($("#oPrice").value) || 0,
        was: Number($("#oWas").value) || 0, pieces: Number($("#oPieces").value) || 0, feat: feat };
      db = AStore.patch((d) => {
        if (feat) d.offers.forEach((x) => { x.feat = false; });
        i < 0 ? d.offers.push(rec) : (d.offers[i] = rec);
      });
      closeModal(); toast("اتحفظ ✅");
    };
  }

  /* ================= الأقسام ================= */
  function renderCats() {
    const cs = db.cats;
    $("#nCats").textContent = ar(cs.length);
    $("#catsTbl").innerHTML = cs.length ? `<table><thead><tr>
        <th>القسم</th><th>الكود</th><th>عدد المنتجات</th><th></th></tr></thead><tbody>` +
      cs.map((c, i) => {
        const n = db.products.filter((p) => p.cat === c.id).length;
        return `<tr><td><span class="nm">${esc(c.name)}</span></td>
          <td><small dir="ltr">${esc(c.id)}</small></td><td>${ar(n)}</td>
          <td style="display:flex;gap:6px">
            <button class="ib" data-ed="${i}">${I.edit}</button>
            <button class="ib" data-mv="${i}" data-d="-1">${I.up}</button>
            <button class="ib" data-mv="${i}" data-d="1">${I.down}</button>
            <button class="ib del" data-del="${i}">${I.trash}</button></td></tr>`; }).join("") + "</tbody></table>"
      : `<div class="blank"><b>مفيش أقسام</b>ضيف أول قسم.</div>`;
    $$("#catsTbl [data-ed]").forEach((b) => (b.onclick = () => catForm(+b.dataset.ed)));
    $$("#catsTbl [data-mv]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.mv, j = i + +b.dataset.d;
      if (j < 0 || j >= db.cats.length) return;
      db = AStore.patch((d) => { const t = d.cats[i]; d.cats[i] = d.cats[j]; d.cats[j] = t; });
    }));
    $$("#catsTbl [data-del]").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.del, c = db.cats[i];
      const n = db.products.filter((p) => p.cat === c.id).length;
      if (n) { alert("مينفعش تحذف «" + c.name + "» وفيه " + n + " منتج. انقلهم لقسم تاني الأول."); return; }
      if (!confirm("تحذف قسم «" + c.name + "»؟")) return;
      db = AStore.patch((d) => d.cats.splice(i, 1)); toast("اتحذف");
    }));
  }
  $("#addCat").onclick = () => catForm(-1);
  function catForm(i) {
    const c = i < 0 ? { id: "c" + Date.now(), name: "" } : Object.assign({}, db.cats[i]);
    openModal(`
      <h3>${i < 0 ? "قسم جديد" : "تعديل قسم"}</h3>
      <div class="field"><label>اسم القسم</label><input id="cName" value="${esc(c.name)}" placeholder="مثال: سجاد وكليم"></div>
      <div class="modal-acts"><button class="btn ghost" id="mC">إلغاء</button><button class="btn" id="mS">حفظ</button></div>`);
    $("#mC").onclick = closeModal;
    $("#mS").onclick = () => {
      const n = $("#cName").value.trim();
      if (!n) { $("#cName").focus(); return; }
      db = AStore.patch((d) => { i < 0 ? d.cats.push({ id: c.id, name: n }) : (d.cats[i].name = n); });
      closeModal(); toast("اتحفظ ✅");
    };
  }

  /* ================= المعرض والآراء ================= */
  function picGrid(key, node, counter, form, empty) {
    const g = db[key] || [];
    $(counter).textContent = ar(g.length);
    $(node).innerHTML = g.length ? g.map((it, i) => `
      <article class="mcard">
        <div class="ph">${thumb(it.img, it.cap)}</div>
        <div class="bd"><b>${esc(it.cap || "—")}</b></div>
        ${rowBar(i)}</article>`).join("")
      : `<div class="blank" style="grid-column:1/-1"><b>${empty}</b>ابدأ بإضافة أول صورة.</div>`;
    wire(node, key, form, () => "الصورة دي");
  }
  function picForm(key, i, title, ph) {
    const list = db[key] || [];
    const it = i < 0 ? { img: "", cap: "" } : Object.assign({}, list[i]);
    openModal(`
      <h3>${i < 0 ? title + " جديد" : "تعديل " + title}</h3>
      <div class="field"><label>الصورة</label>
        <div class="drop" id="mPick">
          <div id="mImgW">${it.img ? `<img src="${esc(it.img)}" alt="">` : `<div class="noimg">اختار صورة</div>`}</div>
          <div>اضغط لاختيار صورة من جهازك</div></div></div>
      <div class="field"><label>الوصف</label><input id="mCap" value="${esc(it.cap || "")}" placeholder="${esc(ph)}"></div>
      <div class="modal-acts"><button class="btn ghost" id="mC">إلغاء</button><button class="btn" id="mS">حفظ</button></div>`);
    let img = it.img;
    $("#mPick").onclick = () => pickImg((d) => {
      img = d; $("#mImgW").innerHTML = `<img src="${esc(d)}" alt="">`; });
    $("#mC").onclick = closeModal;
    $("#mS").onclick = () => {
      if (!img) { toast("اختار صورة الأول"); return; }
      const rec = { img: img, cap: $("#mCap").value.trim() };
      db = AStore.patch((d) => { i < 0 ? d[key].push(rec) : (d[key][i] = rec); });
      closeModal(); toast("اتحفظ ✅");
    };
  }
  const renderItems = () => picGrid("gallery", "#mgrid", "#nItems",
    (i) => picForm("gallery", i, "صورة", "مثال: مفرش مرفا دريم هاوس"), "المعرض فاضي");
  const renderRevs  = () => picGrid("reviews", "#rgrid", "#nRevs",
    (i) => picForm("reviews", i, "رأي", "مثال: الأوردر وصل وكل حاجة تحفة"), "مفيش آراء");
  $("#addItem").onclick = () => picForm("gallery", -1, "صورة", "مثال: مفرش مرفا دريم هاوس");
  $("#addRev").onclick  = () => picForm("reviews", -1, "رأي", "مثال: الأوردر وصل وكل حاجة تحفة");

  /* ================= الفروع ================= */
  function renderBrs() {
    const bs = db.branches || [];
    $("#nBrs").textContent = ar(bs.length);
    $("#brsTbl").innerHTML = bs.length ? `<table><thead><tr>
        <th>الفرع</th><th>العنوان</th><th>بحث الخريطة</th><th></th></tr></thead><tbody>` +
      bs.map((b, i) => `<tr>
        <td><span class="nm">${esc(b.name)}</span></td>
        <td>${esc(b.addr)}</td><td><small>${esc(b.mapq || "—")}</small></td>
        <td style="display:flex;gap:6px">
          <button class="ib" data-ed="${i}">${I.edit}</button>
          <button class="ib" data-mv="${i}" data-d="-1">${I.up}</button>
          <button class="ib" data-mv="${i}" data-d="1">${I.down}</button>
          <button class="ib del" data-del="${i}">${I.trash}</button></td></tr>`).join("") + "</tbody></table>"
      : `<div class="blank"><b>مفيش فروع</b>ضيف أول فرع.</div>`;
    wire("#brsTbl", "branches", brForm, (x) => "«" + x.name + "»");
  }
  $("#addBr").onclick = () => brForm(-1);
  function brForm(i) {
    const bs = db.branches || [];
    const b = i < 0 ? { id: "b" + Date.now(), name: "", addr: "", mapq: "" } : Object.assign({}, bs[i]);
    openModal(`
      <h3>${i < 0 ? "فرع جديد" : "تعديل فرع"}</h3>
      <div class="field"><label>اسم الفرع</label><input id="bName" value="${esc(b.name)}" placeholder="مثال: الفرع الثالث"></div>
      <div class="field"><label>العنوان</label><input id="bAddr" value="${esc(b.addr)}" placeholder="الشارع والعلامة المميزة"></div>
      <div class="field"><label>نص البحث في جوجل مابس</label><input id="bMap" value="${esc(b.mapq || "")}" placeholder="اسم المكان زي ما بتدوّر عليه"></div>
      <div class="modal-acts"><button class="btn ghost" id="mC">إلغاء</button><button class="btn" id="mS">حفظ</button></div>`);
    $("#mC").onclick = closeModal;
    $("#mS").onclick = () => {
      const n = $("#bName").value.trim();
      if (!n) { $("#bName").focus(); return; }
      const rec = { id: b.id, name: n, addr: $("#bAddr").value.trim(), mapq: $("#bMap").value.trim() };
      db = AStore.patch((d) => { i < 0 ? d.branches.push(rec) : (d.branches[i] = rec); });
      closeModal(); toast("اتحفظ ✅");
    };
  }

  /* ================= الطلبات ================= */
  function renderOrds() {
    const flt = $("#fStatus") ? $("#fStatus").value : "";
    const rows = db.orders.map((b, i) => ({ b, i })).filter(({ b }) => !flt || b.status === flt);
    $("#nOrds").textContent = ar(db.orders.length);
    $("#ordsTbl").innerHTML = rows.length ? `<table><thead><tr>
        <th>التاريخ</th><th>العميل</th><th>المطلوب</th><th>المنطقة</th><th>النوع</th><th>الحالة</th><th></th></tr></thead><tbody>` +
      rows.map(({ b, i }) => `<tr>
        <td>${esc(fmt(b.at))}</td>
        <td><span class="nm">${esc(b.name)}</span><small dir="ltr">${esc(b.phone)}</small></td>
        <td>${esc(b.item)}</td><td>${esc(b.area || "—")}</td><td>${esc(b.note || "—")}</td>
        <td><select data-st="${i}">${["جديد","مؤكد","تم","ملغي"].map((s) =>
          `<option ${s === b.status ? "selected" : ""}>${s}</option>`).join("")}</select></td>
        <td><button class="ib del" data-del="${i}">${I.trash}</button></td></tr>`).join("") + "</tbody></table>"
      : `<div class="blank"><b>مفيش طلبات هنا</b>أول طلب من الموقع هيظهر في الجدول.</div>`;
    $$("#ordsTbl [data-st]").forEach((s) => (s.onchange = () => {
      db = AStore.patch((d) => (d.orders[+s.dataset.st].status = s.value)); toast("الحالة اتغيّرت");
    }));
    $$("#ordsTbl [data-del]").forEach((b) => (b.onclick = () => {
      db = AStore.patch((d) => d.orders.splice(+b.dataset.del, 1)); toast("اتحذف");
    }));
  }
  if ($("#fStatus")) $("#fStatus").onchange = renderOrds;
  $("#expCsv").onclick = () => {
    const rows = [["التاريخ", "الاسم", "الموبايل", "المنطقة", "المطلوب", "النوع", "الحالة"]]
      .concat(db.orders.map((x) => [x.at, x.name, x.phone, x.area, x.item, x.note, x.status]));
    const csv = "﻿" + rows.map((r) => r.map((c) =>
      '"' + String(c == null ? "" : c).replace(/"/g, '""') + '"').join(",")).join("\r\n");
    dl(new Blob([csv], { type: "text/csv;charset=utf-8" }), "abo3omar-orders.csv");
  };
  function dl(blob, name) {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 900);
  }

  /* ================= الإعدادات ================= */
  const KEYS = ["brandAr","brand","tagline","slogan","intro","ship","phone","whats","whats2",
                "hours","priceNote","priceHint","photoNote","currency","adminPass"];
  const F = $("#setForm");
  function renderSet() {
    const s = db.settings;
    KEYS.forEach((k) => { if (F.elements[k]) F.elements[k].value = s[k] == null ? "" : s[k]; });
    F.elements.showPrices.checked = !!s.showPrices;
  }
  F.addEventListener("submit", (e) => {
    e.preventDefault();
    const el = e.target.elements;
    db = AStore.patch((d) => {
      KEYS.forEach((k) => { if (el[k]) d.settings[k] = el[k].value.trim(); });
      d.settings.whats  = digits(d.settings.whats);
      d.settings.whats2 = digits(d.settings.whats2);
      d.settings.showPrices = el.showPrices.checked;
      if (!d.settings.adminPass) d.settings.adminPass = "123456";
    });
    $("#gBrand").textContent = $("#sBrand").textContent = db.settings.brandAr;
    toast("الإعدادات اتحفظت ✅");
  });
  $("#expJson").onclick = () =>
    dl(new Blob([JSON.stringify(db, null, 2)], { type: "application/json" }), "abo3omar-backup.json");
  $("#impJson").onclick = () => $("#impFile").click();
  $("#impFile").onchange = (e) => {
    const f = e.target.files && e.target.files[0]; if (!f) return;
    const rd = new FileReader();
    rd.onload = () => {
      try {
        const o = JSON.parse(rd.result);
        if (!o || typeof o !== "object") throw 0;
        db = AStore.set(o); toast("النسخة اترجّعت ✅");
      } catch (err) { toast("الملف مش مظبوط"); }
    };
    rd.readAsText(f);
    e.target.value = "";
  };
  $("#resetAll").onclick = () => {
    if (!confirm("هترجّع كل حاجة زي ما كانت من الأول؟")) return;
    AStore.reset(); db = AStore.get(); toast("رجع للأصل");
  };

  /* ---------- تشغيل ---------- */
  function renderAll() {
    renderHome(); renderProds(); renderOffers(); renderCats();
    renderItems(); renderRevs(); renderBrs(); renderOrds(); renderSet();
  }
  window.addEventListener("abo3omar:change:full", () =>
    toast("مساحة التخزين اتملت — امسح صور قديمة أو صغّر الصور"));
  AStore.on(() => { db = AStore.get(); if ($("#app").classList.contains("on")) renderAll(); });
})();
