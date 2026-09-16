(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var db = MStore.get();
  var CK = "mazaya.list.v1";
  var list = [];
  try { list = JSON.parse(localStorage.getItem(CK)) || []; } catch (e) { list = []; }
  var filter = "all";

  function saveList() { try { localStorage.setItem(CK, JSON.stringify(list)); } catch (e) {} }
  function eg(n) { return Number(n || 0).toLocaleString("ar-EG"); }
  function money(n) { return eg(n) + " " + (db.settings.currency || ""); }
  function price(p) { return db.settings.showPrices && Number(p) ? money(p) : db.settings.priceNote; }
  function wa(txt) { return "https://wa.me/" + (db.settings.whats || "") + "?text=" + encodeURIComponent(txt); }
  function prod(id) { return db.products.filter(function (p) { return p.id === id; })[0]; }
  function catName(id) { return (db.cats.filter(function (c) { return c.id === id; })[0] || {}).name || "—"; }

  function paintMeta() {
    var s = db.settings;
    $("#hIntro").textContent = s.intro;
    $("#fIntro").textContent = s.intro;
    $("#hAddr").textContent = s.addr; $("#tAddr").textContent = s.addr;
    $("#sAddr").textContent = s.addr; $("#fAddr").textContent = s.addr;
    $("#tHours").textContent = s.hours; $("#sHours").textContent = s.hours; $("#fHours").textContent = s.hours;
    $("#sShip").textContent = s.ship;
    $("#pHint").textContent = s.priceHint || ""; $("#sPrice").textContent = s.priceHint || "";
    $("#sPhone").textContent = s.phone; $("#sPhone").href = "tel:" + s.phone;
    $("#fPhoneA").textContent = s.phone; $("#fPhoneA").href = "tel:" + s.phone;
    $("#sMap").href = "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(s.mapq);
    $("#waFab").href = wa("السلام عليكم، جاية من موقع مزايا ✦");
    $("#yr").textContent = new Date().getFullYear();
  }
  function paintStats() {
    $("#statsW").innerHTML = db.stats.map(function (s) {
      return '<div class="it"><div class="n">' + esc(s.n) + '</div><div class="t">' + esc(s.t) + "</div></div>"; }).join("");
  }
  function paintWhy() {
    $("#whyW").innerHTML = db.why.map(function (w) {
      return '<div class="why"><b>' + esc(w.n) + "</b><p>" + esc(w.t) + "</p></div>"; }).join("");
  }

  /* ---------- العروض ---------- */
  function paintOffers() {
    $("#offerW").innerHTML = db.offers.map(function (o) {
      var its = o.items.map(prod).filter(Boolean);
      var was = its.reduce(function (a, p) { return a + (Number(p.price) || 0); }, 0);
      var save = was - Number(o.price || 0);
      return '<article class="offer" data-id="' + esc(o.id) + '">' +
        (o.tag ? '<span class="tg">' + esc(o.tag) + "</span>" : "") +
        "<h3>" + esc(o.name) + '</h3><p class="sub">' + esc(o.sub) + "</p>" +
        '<div class="thumbs">' + its.map(function (p) {
          return '<img src="' + esc(p.img) + '" alt="' + esc(p.name) + '">'; }).join("") + "</div>" +
        "<ul>" + its.map(function (p) { return "<li>" + esc(p.name) + "</li>"; }).join("") + "</ul>" +
        '<div class="prc">' +
        (was > Number(o.price || 0) ? '<span class="was">' + esc(money(was)) + "</span>" : "") +
        '<span class="now">' + eg(o.price) + ' <small>' + esc(db.settings.currency) + "</small></span>" +
        (save > 0 ? '<span class="save">توفير ' + esc(money(save)) + "</span>" : "") + "</div>" +
        '<button class="btn btn-w" type="button" style="width:100%">اطلبي العرض على واتساب</button></article>';
    }).join("");
    $$("#offerW .offer").forEach(function (el) {
      var o = db.offers.filter(function (x) { return x.id === el.dataset.id; })[0];
      $("button.btn", el).addEventListener("click", function () {
        var its = o.items.map(prod).filter(Boolean);
        var t = "طلب عرض من موقع مزايا ✦\n\n" + o.name + "\n" +
          its.map(function (p, i) { return (i + 1) + ") " + p.name; }).join("\n") +
          "\n\nسعر العرض: " + money(o.price) + "\n\nياريت تأكدولي التفاصيل.";
        log({ item: o.name, note: "عرض" });
        window.open(wa(t), "_blank");
      });
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
    var ps = db.products.filter(function (p) { return filter === "all" || p.cat === filter; });
    $("#prodW").innerHTML = ps.map(function (p) {
      var inList = list.some(function (l) { return l.id === p.id; });
      return '<article class="card" data-id="' + esc(p.id) + '">' +
        '<div class="ph"><img src="' + esc(p.img) + '" alt="' + esc(p.name) + '" loading="lazy">' +
        '<span class="tag">' + esc(catName(p.cat)) + "</span></div>" +
        '<div class="bd"><h3>' + esc(p.name) + "</h3>" +
        '<p class="ds">' + esc(p.note) + "</p>" +
        '<div class="ft"><span class="pr">' + esc(price(p.price)) + "</span>" +
        '<button class="add' + (inList ? " in" : "") + '" type="button">' +
        (inList ? "في القايمة ✓" : "ضيفي") + "</button></div></div></article>";
    }).join("");
    $$("#prodW .card").forEach(function (card) {
      var p = prod(card.dataset.id);
      $(".add", card).addEventListener("click", function () { addItem(p); });
      $(".ph", card).addEventListener("click", function () { openLb(p.img, p.name); });
    });
  }
  function paintSelect() {
    $("#fItem").innerHTML = '<option value="">لسه مش محددة</option>' +
      '<optgroup label="العروض">' + db.offers.map(function (o) {
        return "<option>" + esc(o.name) + "</option>"; }).join("") + "</optgroup>" +
      '<optgroup label="المنتجات">' + db.products.map(function (p) {
        return "<option>" + esc(p.name) + "</option>"; }).join("") + "</optgroup>";
  }

  /* ---------- المعرض ---------- */
  var gi = 0, single = null;
  function paintGal() {
    $("#galW").innerHTML = db.gallery.map(function (g, i) {
      return '<figure data-i="' + i + '"><img src="' + esc(g.img) + '" alt="' + esc(g.cap) +
        '" loading="lazy"><figcaption>' + esc(g.cap) + "</figcaption></figure>"; }).join("");
    $$("#galW figure").forEach(function (f) {
      f.addEventListener("click", function () { single = null; gi = +f.dataset.i; showLb(); });
    });
  }
  function openLb(img, cap) { single = { img: img, cap: cap }; showLb(); }
  function showLb() {
    var g = single || db.gallery[gi]; if (!g) return;
    $("#lbI").src = g.img; $("#lbI").alt = g.cap; $("#lbC").textContent = g.cap;
    $("#lbP").hidden = $("#lbN").hidden = !!single;
    $("#lb").classList.add("on");
  }
  function step(d) { if (single) return; gi = (gi + d + db.gallery.length) % db.gallery.length; showLb(); }
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
  function addItem(p) {
    var f = list.filter(function (l) { return l.id === p.id; })[0];
    if (f) f.q++; else list.push({ id: p.id, q: 1 });
    saveList(); paintList(); paintProds(); openDrw();
  }
  function paintList() {
    var n = list.reduce(function (a, c) { return a + c.q; }, 0);
    $("#cnt").textContent = n;
    if (!list.length) {
      $("#drwB").innerHTML = '<div class="empty">القايمة فاضية.<br>ضيفي اللي عايزاه من المنتجات.</div>';
      $("#drwTot").textContent = "—"; return;
    }
    var tot = 0;
    $("#drwB").innerHTML = list.map(function (l) {
      var p = prod(l.id); if (!p) return "";
      tot += (Number(p.price) || 0) * l.q;
      return '<div class="li" data-id="' + esc(p.id) + '"><img src="' + esc(p.img) + '" alt="">' +
        '<div class="in"><div class="nm">' + esc(p.name) + "</div>" +
        '<div class="pp">' + esc(price(p.price)) + "</div>" +
        '<div class="qt"><button data-d="-1">−</button><span>' + l.q + '</span><button data-d="1">+</button></div></div>' +
        '<button class="rm">حذف</button></div>'; }).join("");
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
  function openDrw() { $("#drw").classList.add("on"); $("#ov").classList.add("on"); }
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
        (db.settings.showPrices && p.price ? " — " + money(p.price) : "");
    }).filter(Boolean);
    var t = "طلب من موقع مزايا ✦\n\n" + lines.join("\n") +
      (db.settings.showPrices && tot ? "\n\nالإجمالي: " + money(tot) : "") +
      "\n\nياريت تأكدولي التوفر والسعر.";
    log({ item: list.map(function (l) { var p = prod(l.id); return p ? p.name + " ×" + l.q : ""; })
      .filter(Boolean).join(" + "), note: "من القايمة" });
    window.open(wa(t), "_blank");
  });

  function log(o) {
    MStore.patch(function (d) {
      d.orders.unshift({ at: new Date().toISOString(), name: o.name || "—", phone: o.phone || "—",
        area: o.area || "—", item: o.item, note: o.note || "", status: "جديد" });
    });
  }

  /* ---------- فورم ---------- */
  $("#oForm").addEventListener("submit", function (e) {
    e.preventDefault();
    var el = e.target.elements;
    var name = el.name.value.trim(), phone = el.phone.value.trim();
    if (!name || !phone) { el[!name ? "name" : "phone"].focus(); return; }
    var rec = { name: name, phone: phone, area: el.area.value.trim(),
      item: el.item.value || "—", note: el.note.value.trim() };
    log(rec);
    var t = "طلب جديد من موقع مزايا ✦\n\n" +
      "الاسم: " + rec.name + "\nالموبايل: " + rec.phone +
      (rec.area ? "\nالمنطقة: " + rec.area : "") +
      "\nالمطلوب: " + rec.item + (rec.note ? "\nملاحظات: " + rec.note : "");
    window.open(wa(t), "_blank");
    var m = $("#okMsg");
    m.textContent = "تمام يا " + name + " ✦ طلبك اتسجّل وفتحنا لك واتساب. لو ما اتفتحش، كلّمينا على " + db.settings.phone;
    m.classList.add("on");
    e.target.reset();
  });

  $("#burger").addEventListener("click", function () { $("#links").classList.toggle("on"); });
  $$("#links a").forEach(function (a) {
    a.addEventListener("click", function () { $("#links").classList.remove("on"); });
  });

  function all() { paintMeta(); paintStats(); paintWhy(); paintOffers(); paintChips();
    paintProds(); paintSelect(); paintGal(); paintFaq(); paintList(); }
  all();
  MStore.on(function () { db = MStore.get(); all(); });
})();
