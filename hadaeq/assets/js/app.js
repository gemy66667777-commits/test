(function () {
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };

  var db = HStore.get();
  var CK = "hadaeq.list.v1";
  var list = []; try { list = JSON.parse(localStorage.getItem(CK)) || []; } catch (e) { list = []; }
  var filter = "all", q = "";

  function saveList() { try { localStorage.setItem(CK, JSON.stringify(list)); } catch (e) {} }
  function eg(n)    { return Number(n || 0).toLocaleString("ar-EG"); }
  function money(n) { return eg(n) + " " + (db.settings.currency || ""); }
  function price(p) { return db.settings.showPrices && Number(p) ? money(p) : db.settings.priceNote; }
  function wa(txt, num) { return "https://wa.me/" + (num || db.settings.whats || "") + "?text=" + encodeURIComponent(txt); }
  function prod(id) { return db.products.filter(function (p) { return p.id === id; })[0]; }
  function catName(id) { return (db.cats.filter(function (c) { return c.id === id; })[0] || {}).name || "—"; }
  function mapUrl(s) { return "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(s); }
  var HI = "السلام عليكم، من موقع حدائق الزهور ✦";

  /* رسمة بديلة للمنتج غير المصوّر */
  var ART = {
    niche:'<path d="M9.5 3h5v3h-5z"/><path d="M8 9.5A3.5 3.5 0 0 1 11.5 6h1A3.5 3.5 0 0 1 16 9.5V19a2 2 0 0 1-2 2h-4a2 2 0 0 1-2-2z"/><path d="M9.8 12.5h4.4"/>',
    classic:'<path d="M10 3h4v2.6h-4z"/><path d="M7.5 10.5c0-2.5 2-4.5 4.5-4.5s4.5 2 4.5 4.5V19a2 2 0 0 1-2 2H9.5a2 2 0 0 1-2-2z"/><circle cx="12" cy="13" r="2.4"/>',
    women:'<path d="M10.2 3.2h3.6v3h-3.6z"/><path d="M8.6 9.8c0-1.9 1.5-3.4 3.4-3.4s3.4 1.5 3.4 3.4v8.8a2 2 0 0 1-2 2h-2.8a2 2 0 0 1-2-2z"/><path d="M17 5.5c1.4.6 2 2.2 1.5 3.5"/>',
    care:'<ellipse cx="12" cy="9.5" rx="7" ry="3"/><path d="M5 9.5v4.2c0 1.7 3.1 3 7 3s7-1.3 7-3V9.5"/>'
  };
  function media(p, cls) {
    if (p.img) return '<img src="' + esc(p.img) + '" alt="' + esc(p.name) + '" loading="lazy">';
    return '<span class="art">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.15" stroke-linecap="round" stroke-linejoin="round">' +
      (ART[p.cat] || ART.beds) + "</svg></span>" +
      '<span class="soon">الصورة قريبًا</span>';
  }

  /* ---------- الترويسة والبيانات العامة ---------- */
  function paintMeta() {
    var s = db.settings;
    $("#brandAr").textContent = s.brandAr; $("#brandAr2").textContent = s.brandAr;
    $("#brandAr3").textContent = s.brandAr;
    $$(".js-tag").forEach(function (e) { e.textContent = s.tagline; });
    $("#slogan").textContent = s.slogan;
    $("#hIntro").textContent = s.intro; $("#fIntro").textContent = s.intro;
    $("#tHours").textContent = s.hours; $("#sHours").textContent = s.hours; $("#fHours").textContent = s.hours;
    $("#sShip").textContent = s.ship;
    $("#pHint").textContent = s.priceHint || ""; $("#sPrice").textContent = s.priceHint || "";
    $("#photoNote").textContent = s.photoNote || "";
    $("#fPhoneA").textContent = s.phone; $("#fPhoneA").href = "tel:" + s.phone;
    $("#waFab").href = wa(HI + "\nودّي أستفسر عن العطور المتوفرة.");
    $("#askPhoto").href = wa(HI + "\nممكن ترسلون لي صور العطور المتوفرة حالياً؟");
    $("#yr").textContent = new Date().getFullYear();

    var b0 = (db.branches || [])[0] || { addr: "", mapq: "" };
    $("#tAddr").textContent = b0.addr;
    $("#hAddr").textContent = b0.addr;

    /* أرقام التواصل */
    var nums = [
      { k: "wa",  t: "واتساب — الطلبات", v: s.whats,  d: s.whats },
      { k: "wa",  t: "واتساب ٢",          v: s.whats2, d: s.whats2 },
      { k: "tel",  t: "للاتصال المباشر",  v: s.phone, d: s.phone },
      { k: "snap", t: "سناب شات",          v: s.snap,  d: s.snap }
    ].filter(function (n) { return n.v; });
    $("#numsW").innerHTML = nums.map(function (n) {
      var href, label = n.v, ext = true;
      if (n.k === "wa") { href = wa(HI + "\nودّي أستفسر عن العطور المتوفرة.", n.v); label = "0" + String(n.v).replace(/^966/, ""); }
      else if (n.k === "snap") { href = "https://www.snapchat.com/add/" + n.v; label = "@" + n.v; }
      else { href = "tel:" + n.v; ext = false; }
      return '<a class="numbox" href="' + esc(href) + '"' + (ext ? ' target="_blank" rel="noopener"' : "") + '>' +
        '<span class="ic ' + n.k + '"><svg><use href="#i-' + n.k + '"></use></svg></span>' +
        "<span><small>" + esc(n.t) + "</small><b dir=\"ltr\">" + esc(label) + "</b></span></a>";
    }).join("");

    /* الفروع */
    $("#brW").innerHTML = (db.branches || []).map(function (b) {
      return '<div class="branch"><span class="ic"><svg><use href="#i-pin"></use></svg></span>' +
        "<div><b>" + esc(b.name) + "</b><p>" + esc(b.addr) + "</p>" +
        '<a href="' + esc(mapUrl(b.mapq || b.addr)) + '" target="_blank" rel="noopener">افتح على الخريطة ↗</a></div></div>';
    }).join("");
  }

  function paintStats() {
    $("#statsW").innerHTML = db.stats.map(function (s) {
      return '<div class="it"><div class="n">' + esc(s.n) + '</div><div class="t">' + esc(s.t) + "</div></div>"; }).join("");
  }
  function paintWhy() {
    $("#whyW").innerHTML = db.why.map(function (w) {
      return '<div class="why"><b>' + esc(w.n) + "</b><p>" + esc(w.t) + "</p></div>"; }).join("");
  }

  /* ---------- العروض (بالكميات) ---------- */
  function calc(o) {
    var was = 0, pcs = 0, its = [];
    (o.items || []).forEach(function (it) {
      var p = prod(it.id); if (!p) return;
      var qn = Number(it.q) || 1;
      was += (Number(p.price) || 0) * qn; pcs += qn;
      its.push({ p: p, q: qn });
    });
    return { its: its, sum: was, was: Number(o.was) || was, pcs: Number(o.pieces) || pcs };
  }
  function offerText(o) {
    var c = calc(o);
    return HI + "\nودّي أحجز «" + o.name + "»\n\n" +
      c.its.map(function (x) { return "• " + x.p.name + " × " + x.q; }).join("\n") +
      "\n\nعدد العطور: " + c.pcs +
      "\nسعر الباقة: " + money(o.price) +
      "\n\nياليت تأكدون لي التفاصيل والمتوفر.";
  }
  function offerCard(o, big) {
    var c = calc(o), save = c.was - Number(o.price || 0);
    var thumbs = c.its.filter(function (x) { return x.p.img; }).slice(0, 5);
    return '<article class="offer' + (big ? " big" : "") + '" data-id="' + esc(o.id) + '">' +
      (big && o.img ? '<div class="poster"><img src="' + esc(o.img) + '" alt="' + esc(o.name) + '" loading="lazy"></div>' : "") +
      '<div class="ob">' +
      (o.tag ? '<span class="tg">' + esc(o.tag) + "</span>" : "") +
      "<h3>" + esc(o.name) + '</h3><p class="sub">' + esc(o.sub || "") + "</p>" +
      '<div class="prc">' +
        '<span class="now">' + eg(o.price) + " <small>" + esc(db.settings.currency) + "</small></span>" +
        (c.was > Number(o.price || 0) ? '<span class="was">' + esc(money(c.was)) + "</span>" : "") +
        (save > 0 ? '<span class="save">وفّر ' + esc(money(save)) + "</span>" : "") +
      "</div>" +
      '<div class="pcs">' + esc(eg(c.pcs)) + " عطر في الباقة</div>" +
      (thumbs.length && c.its.length > 1 ? '<div class="thumbs">' + thumbs.map(function (x) {
        return '<img src="' + esc(x.p.img) + '" alt="' + esc(x.p.name) + '" loading="lazy">'; }).join("") + "</div>" : "") +
      (c.its.length > 1 ? "<ul>" + c.its.map(function (x) {
        return "<li><b>" + esc(eg(x.q)) + "×</b> " + esc(x.p.name) + "</li>"; }).join("") + "</ul>"
        : '<p class="onenote">' + esc((c.its[0] || {}).p ? c.its[0].p.note || "" : "") + "</p>") +
      '<button class="btn btn-w js-order" type="button">احجز العرض على واتساب</button>' +
      "</div></article>";
  }
  function paintOffers() {
    var feat = db.offers.filter(function (o) { return o.feat; })[0];
    var rest = db.offers.filter(function (o) { return o !== feat; });
    $("#featW").innerHTML = feat ? offerCard(feat, true) : "";
    $("#offerW").innerHTML = rest.map(function (o) { return offerCard(o, false); }).join("");
    $$(".offer").forEach(function (el) {
      var o = db.offers.filter(function (x) { return x.id === el.dataset.id; })[0];
      if (!o) return;
      $(".js-order", el).addEventListener("click", function () {
        log({ item: o.name, note: "عرض" });
        window.open(wa(offerText(o)), "_blank");
      });
      var ps = $(".poster img", el);
      if (ps) ps.addEventListener("click", function () { openLb(o.img, o.name); });
    });
  }

  /* ---------- المنتجات ---------- */
  function paintChips() {
    var used = {}; db.products.forEach(function (p) { used[p.cat] = 1; });
    var cs = db.cats.filter(function (c) { return used[c.id]; });
    $("#chipW").innerHTML = '<button type="button" data-f="all" aria-pressed="' + (filter === "all") + '">الكل</button>' +
      cs.map(function (c) {
        return '<button type="button" data-f="' + esc(c.id) + '" aria-pressed="' + (filter === c.id) + '">' +
          esc(c.name) + "</button>"; }).join("");
    $$("#chipW button").forEach(function (b) {
      b.addEventListener("click", function () { filter = b.dataset.f; paintChips(); paintProds(); });
    });
  }
  function paintProds() {
    var ps = db.products.filter(function (p) {
      var okc = filter === "all" || p.cat === filter;
      var okq = !q || (p.name + " " + (p.note || "")).toLowerCase().indexOf(q) > -1;
      return okc && okq;
    });
    if (!ps.length) {
      $("#prodW").innerHTML = '<div class="blank">مفيش نتيجة للبحث ده.<br><span>جرّب كلمة تانية أو اسألنا على واتساب.</span></div>';
      return;
    }
    $("#prodW").innerHTML = ps.map(function (p) {
      var inList = list.some(function (l) { return l.id === p.id; });
      return '<article class="card' + (p.img ? "" : " noimg") + '" data-id="' + esc(p.id) + '">' +
        '<div class="ph">' + media(p) + '<span class="tag">' + esc(catName(p.cat)) + "</span></div>" +
        '<div class="bd"><h3>' + esc(p.name) + "</h3>" +
        '<p class="ds">' + esc(p.note || "") + "</p>" +
        '<div class="ft"><span class="pr">' + esc(price(p.price)) + "</span>" +
        '<button class="add' + (inList ? " in" : "") + '" type="button">' +
        (inList ? "في القايمة ✓" : "ضيف") + "</button></div></div></article>";
    }).join("");
    $$("#prodW .card").forEach(function (card) {
      var p = prod(card.dataset.id);
      $(".add", card).addEventListener("click", function () { addItem(p); });
      if (p.img) $(".ph", card).addEventListener("click", function () { openLb(p.img, p.name); });
    });
  }
  function paintSelect() {
    $("#fItem").innerHTML = '<option value="">لسه مش محدد</option>' +
      '<optgroup label="العروض">' + db.offers.map(function (o) {
        return "<option>" + esc(o.name) + "</option>"; }).join("") + "</optgroup>" +
      '<optgroup label="المنتجات">' + db.products.map(function (p) {
        return "<option>" + esc(p.name) + "</option>"; }).join("") + "</optgroup>";
  }

  /* ---------- المعرض والآراء ---------- */
  var gi = 0, single = null, src = "gallery";
  function paintGal() {
    $("#galW").innerHTML = db.gallery.map(function (g, i) {
      return '<figure data-i="' + i + '"><img src="' + esc(g.img) + '" alt="' + esc(g.cap) +
        '" loading="lazy"><figcaption>' + esc(g.cap) + "</figcaption></figure>"; }).join("");
    $$("#galW figure").forEach(function (f) {
      f.addEventListener("click", function () { single = null; src = "gallery"; gi = +f.dataset.i; showLb(); });
    });
  }
  function paintReviews() {
    $("#revW").innerHTML = (db.reviews || []).map(function (r, i) {
      return '<figure data-i="' + i + '"><img src="' + esc(r.img) + '" alt="' + esc(r.cap) + '" loading="lazy"></figure>';
    }).join("");
    $$("#revW figure").forEach(function (f) {
      f.addEventListener("click", function () { single = null; src = "reviews"; gi = +f.dataset.i; showLb(); });
    });
  }
  function bank() { return src === "reviews" ? (db.reviews || []) : db.gallery; }
  function openLb(img, cap) { single = { img: img, cap: cap }; showLb(); }
  function showLb() {
    var g = single || bank()[gi]; if (!g) return;
    $("#lbI").src = g.img; $("#lbI").alt = g.cap || ""; $("#lbC").textContent = g.cap || "";
    $("#lbP").hidden = $("#lbN").hidden = !!single;
    $("#lb").classList.add("on");
  }
  function step(d) { if (single) return; var b = bank(); gi = (gi + d + b.length) % b.length; showLb(); }
  $("#lbX").addEventListener("click", function () { $("#lb").classList.remove("on"); });
  $("#lbP").addEventListener("click", function () { step(-1); });
  $("#lbN").addEventListener("click", function () { step(1); });
  $("#lb").addEventListener("click", function (e) { if (e.target.id === "lb") $("#lb").classList.remove("on"); });
  document.addEventListener("keydown", function (e) {
    if (!$("#lb").classList.contains("on")) return;
    if (e.key === "Escape") $("#lb").classList.remove("on");
    if (e.key === "ArrowLeft") step(1);
    if (e.key === "ArrowRight") step(-1);
  });

  function paintFaq() {
    $("#faqW").innerHTML = db.faq.map(function (f) {
      return "<details><summary>" + esc(f.q) + "</summary><p>" + esc(f.a) + "</p></details>"; }).join("");
  }

  /* ---------- قايمة الطلب ---------- */
  var toastT;
  function toast(msg) {
    var t = $("#toast");
    t.textContent = msg; t.classList.add("on");
    clearTimeout(toastT); toastT = setTimeout(function () { t.classList.remove("on"); }, 2000);
  }
  function addItem(p) {
    var f = list.filter(function (l) { return l.id === p.id; })[0];
    if (f) f.q++; else list.push({ id: p.id, q: 1 });
    saveList(); paintList(); paintProds();
    toast("اتضاف للقايمة — " + list.reduce(function (a, c) { return a + c.q; }, 0) + " عطر");
  }
  function paintList() {
    var n = list.reduce(function (a, c) { return a + c.q; }, 0);
    $("#cnt").textContent = n;
    $("#cnt").classList.toggle("on", n > 0);
    if (!list.length) {
      $("#drwB").innerHTML = '<div class="empty">القايمة فاضية.<br>ضيف اللي عايزه من المنتجات.</div>';
      $("#drwTot").textContent = "—"; return;
    }
    var tot = 0;
    $("#drwB").innerHTML = list.map(function (l) {
      var p = prod(l.id); if (!p) return "";
      tot += (Number(p.price) || 0) * l.q;
      return '<div class="li" data-id="' + esc(p.id) + '">' +
        '<div class="liph">' + (p.img ? '<img src="' + esc(p.img) + '" alt="">' : '<span class="mini">صورة<br>قريبًا</span>') + "</div>" +
        '<div class="in"><div class="nm">' + esc(p.name) + "</div>" +
        '<div class="pp">' + esc(price(p.price)) + "</div>" +
        '<div class="qt"><button data-d="-1" aria-label="تقليل">−</button><span>' + l.q +
        '</span><button data-d="1" aria-label="زيادة">+</button></div></div>' +
        '<button class="rm" aria-label="حذف">حذف</button></div>'; }).join("");
    $("#drwTot").textContent = db.settings.showPrices && tot ? money(tot) : db.settings.priceNote;
    $$("#drwB .li").forEach(function (el) {
      var id = el.dataset.id;
      $$(".qt button", el).forEach(function (b) {
        b.addEventListener("click", function () {
          var it = list.filter(function (l) { return l.id === id; })[0]; if (!it) return;
          it.q += +b.dataset.d;
          if (it.q < 1) list = list.filter(function (l) { return l.id !== id; });
          saveList(); paintList(); paintProds();
        });
      });
      $(".rm", el).addEventListener("click", function () {
        list = list.filter(function (l) { return l.id !== id; });
        saveList(); paintList(); paintProds();
      });
    });
  }
  function openDrw()  { $("#drw").classList.add("on");    $("#ov").classList.add("on"); }
  function closeDrw() { $("#drw").classList.remove("on"); $("#ov").classList.remove("on"); }
  $("#listOpen").addEventListener("click", openDrw);
  $("#drwX").addEventListener("click", closeDrw);
  $("#ov").addEventListener("click", closeDrw);
  $("#drwClr").addEventListener("click", function () { list = []; saveList(); paintList(); paintProds(); });
  $("#drwSend").addEventListener("click", function () {
    if (!list.length) { openDrw(); return; }
    var tot = 0;
    var lines = list.map(function (l, i) {
      var p = prod(l.id); if (!p) return "";
      tot += (Number(p.price) || 0) * l.q;
      return (i + 1) + ") " + p.name + " × " + l.q +
        (db.settings.showPrices && p.price ? " — " + money(p.price * l.q) : "");
    }).filter(Boolean);
    var t = HI + "\nودّي أأكد هذا الطلب:\n\n" + lines.join("\n") +
      (db.settings.showPrices && tot ? "\n\nالإجمالي: " + money(tot) : "") +
      "\n\nالاسم:\nالمدينة:\nالعنوان:";
    log({ item: list.map(function (l) { var p = prod(l.id); return p ? p.name + " ×" + l.q : ""; })
      .filter(Boolean).join(" + "), note: "من القايمة" });
    window.open(wa(t), "_blank");
  });

  function log(o) {
    HStore.patch(function (d) {
      d.orders.unshift({ at: new Date().toISOString(), name: o.name || "—", phone: o.phone || "—",
        area: o.area || "—", item: o.item, note: o.note || "", status: "جديد" });
      if (d.orders.length > 300) d.orders.length = 300;
    });
  }

  /* ---------- فورم الطلب ---------- */
  $("#oForm").addEventListener("submit", function (e) {
    e.preventDefault();
    var el = e.target.elements;
    var name = el.name.value.trim(), phone = el.phone.value.trim();
    if (!name || !phone) { el[!name ? "name" : "phone"].focus(); return; }
    var rec = { name: name, phone: phone, area: el.area.value.trim(),
      item: el.item.value || "—", note: el.note.value.trim() };
    log(rec);
    var t = HI + "\nطلب جديد من الموقع:\n\n" +
      "الاسم: " + rec.name + "\nالموبايل: " + rec.phone +
      (rec.area ? "\nالمدينة/المنطقة: " + rec.area : "") +
      "\nالمطلوب: " + rec.item + (rec.note ? "\nملاحظات: " + rec.note : "");
    window.open(wa(t), "_blank");
    var m = $("#okMsg");
    m.textContent = "تم يا " + name + " ✦ سجّلنا طلبك وفتحنا لك الواتساب. لو ما فتح، كلّمنا على " + db.settings.phone;
    m.classList.add("on");
    e.target.reset();
  });

  /* ---------- البحث والقائمة ---------- */
  var sIn = $("#search");
  sIn.addEventListener("input", function () { q = sIn.value.trim().toLowerCase(); paintProds(); });
  $("#searchX").addEventListener("click", function () { sIn.value = ""; q = ""; paintProds(); sIn.focus(); });
  $("#burger").addEventListener("click", function () { $("#links").classList.toggle("on"); });
  $$("#links a").forEach(function (a) {
    a.addEventListener("click", function () { $("#links").classList.remove("on"); });
  });

  function all() {
    paintMeta(); paintStats(); paintWhy(); paintOffers(); paintChips();
    paintProds(); paintSelect(); paintGal(); paintReviews(); paintFaq(); paintList();
  }
  all();
  HStore.on(function () { db = HStore.get(); all(); });
})();
