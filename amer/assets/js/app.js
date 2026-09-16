(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var db = AStore.get();
  var CK = "amer.list.v1";
  var list = [];
  try { list = JSON.parse(localStorage.getItem(CK)) || []; } catch (e) { list = []; }
  var filter = "all";

  function saveList() { try { localStorage.setItem(CK, JSON.stringify(list)); } catch (e) {} }
  function eg(n) { return Number(n || 0).toLocaleString("ar-EG"); }
  function money(n) { return eg(n) + " " + (db.settings.currency || ""); }
  function price(p) { return db.settings.showPrices && Number(p) ? money(p) : db.settings.priceNote; }
  function wa(num, txt) {
    var d = String(num || "").replace(/\D/g, "");
    if (d.indexOf("0") === 0) d = "2" + d;
    return "https://wa.me/" + d + "?text=" + encodeURIComponent(txt);
  }
  function dept(id) { return db.depts.filter(function (d) { return d.id === id; })[0] || db.depts[0]; }
  function prod(id) { return db.products.filter(function (p) { return p.id === id; })[0]; }

  /* ---------- نصوص عامة ---------- */
  function paintMeta() {
    var s = db.settings;
    $("#hIntro").textContent = s.intro;
    $("#fIntro").textContent = s.intro;
    $("#hAddr").textContent = s.addr;
    $("#wAddr").textContent = s.addr;
    $("#oAddr").textContent = s.addr + " — " + s.hours;
    $("#tHours").textContent = s.hours;
    $("#wHours").textContent = s.hours;
    $("#wFb").textContent = s.facebook;
    $("#pHint").textContent = s.priceHint || "";
    $("#oPrice").textContent = s.priceHint || "";
    $("#wPhone").textContent = s.phone; $("#wPhone").href = "tel:" + s.phone;
    $("#wMap").href = "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(s.mapq);
    $("#wWa").href = wa(s.phone, "السلام عليكم، حابب أستفسر عن المعروض عندكم 👑");
    $("#waFab").href = wa(s.phone, "السلام عليكم، جاي من موقع سنتر الأمير والأميرة 👑");
    $("#oNums").innerHTML = db.depts.map(function (d) {
      return esc(d.name) + ": " + d.phones.map(function (n) {
        return '<a class="num-l" href="tel:' + esc(n) + '">' + esc(n) + "</a>"; }).join(" — ");
    }).join("<br>");
    $("#fNums").innerHTML = db.depts.map(function (d) {
      return "<li>" + esc(d.name) + '<br><a class="num-l" href="tel:' + esc(d.phones[0]) + '">' +
        esc(d.phones[0]) + "</a></li>"; }).join("");
    $("#yr").textContent = new Date().getFullYear();
  }

  function paintStats() {
    $("#statsW").innerHTML = db.stats.map(function (s) {
      return '<div class="it"><div class="n">' + esc(s.n) + '</div><div class="t">' + esc(s.t) + "</div></div>";
    }).join("");
  }

  /* ---------- الأقسام ---------- */
  function paintDepts() {
    $("#deptW").innerHTML = db.depts.map(function (d) {
      return '<article class="dept"><div class="ic"><svg><use href="#i-' + esc(d.icon) + '"></use></svg></div>' +
        "<h3>" + esc(d.name) + "</h3><p>" + esc(d.note) + "</p>" +
        '<div class="nums">' + d.phones.map(function (n) {
          return '<div class="num"><b>' + esc(n) + "</b>" +
            '<a class="go" href="' + esc(wa(n, "السلام عليكم، حابب أستفسر عن " + d.name + " 👑")) +
            '" target="_blank" rel="noopener"><svg><use href="#i-wa"></use></svg> واتساب</a></div>';
        }).join("") + "</div></article>";
    }).join("");
  }

  /* ---------- المنتجات ---------- */
  function paintChips() {
    var used = {}; db.products.forEach(function (p) { used[p.dept] = 1; });
    var ds = db.depts.filter(function (d) { return used[d.id]; });
    $("#chipW").innerHTML = '<button type="button" data-f="all" aria-pressed="' + (filter === "all") + '">الكل</button>' +
      ds.map(function (d) {
        return '<button type="button" data-f="' + esc(d.id) + '" aria-pressed="' + (filter === d.id) + '">' +
          esc(d.name) + "</button>"; }).join("");
    $$("#chipW button").forEach(function (b) {
      b.addEventListener("click", function () { filter = b.dataset.f; paintChips(); paintProds(); });
    });
  }
  function paintProds() {
    var ps = db.products.filter(function (p) { return filter === "all" || p.dept === filter; });
    $("#prodW").innerHTML = ps.map(function (p) {
      var inList = list.some(function (l) { return l.id === p.id; });
      return '<article class="card" data-id="' + esc(p.id) + '">' +
        '<div class="ph" data-img="' + esc(p.img) + '" data-cap="' + esc(p.name) + '">' +
        '<img src="' + esc(p.img) + '" alt="' + esc(p.name) + '" loading="lazy">' +
        '<span class="tag">' + esc(dept(p.dept).name) + "</span></div>" +
        '<div class="bd"><h3>' + esc(p.name) + "</h3>" +
        '<p class="ds">' + esc(p.note) + "</p>" +
        '<div class="ft"><span class="pr">' + esc(price(p.price)) + "</span>" +
        '<button class="add' + (inList ? " in" : "") + '" type="button">' +
        (inList ? "في القايمة ✓" : "ضيف للقايمة") + "</button></div></div></article>";
    }).join("");
    $$("#prodW .card").forEach(function (card) {
      var p = prod(card.dataset.id);
      $(".add", card).addEventListener("click", function () { addItem(p); });
      $(".ph", card).addEventListener("click", function () { openLbFor(p.img, p.name); });
    });
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
        (was > 0 ? '<span class="was">' + esc(money(was)) + "</span>" : "") +
        '<span class="now">' + eg(o.price) + ' <small>' + esc(db.settings.currency) + "</small></span>" +
        (save > 0 ? '<span class="save">توفير ' + esc(money(save)) + "</span>" : "") + "</div>" +
        '<button class="btn btn-a" type="button" style="width:100%">اطلب العرض على واتساب</button></article>';
    }).join("");
    $$("#offerW .offer").forEach(function (el) {
      var o = db.offers.filter(function (x) { return x.id === el.dataset.id; })[0];
      $("button.btn", el).addEventListener("click", function () {
        var its = o.items.map(prod).filter(Boolean);
        var t = "طلب عرض من موقع سنتر الأمير والأميرة 👑\n\n" + o.name + "\n" +
          its.map(function (p, i) { return (i + 1) + ") " + p.name; }).join("\n") +
          "\n\nسعر العرض: " + money(o.price) + "\n\nياريت تأكدولي التفاصيل.";
        logOrder({ item: o.name, note: "عرض", src: "offer" });
        window.open(wa(db.settings.phone, t), "_blank");
      });
    });
  }

  /* ---------- المعرض واللايت بوكس ---------- */
  var gi = 0, lbSingle = null;
  function paintGal() {
    $("#galW").innerHTML = db.gallery.map(function (g, i) {
      return '<figure data-i="' + i + '"><img src="' + esc(g.img) + '" alt="' + esc(g.cap) +
        '" loading="lazy"><figcaption>' + esc(g.cap) + "</figcaption></figure>"; }).join("");
    $$("#galW figure").forEach(function (f) {
      f.addEventListener("click", function () { lbSingle = null; gi = +f.dataset.i; showLb(); });
    });
  }
  function openLbFor(img, cap) { lbSingle = { img: img, cap: cap }; showLb(); }
  function showLb() {
    var g = lbSingle || db.gallery[gi]; if (!g) return;
    $("#lbI").src = g.img; $("#lbI").alt = g.cap; $("#lbC").textContent = g.cap;
    $("#lbP").hidden = $("#lbN").hidden = !!lbSingle;
    $("#lb").classList.add("on");
  }
  function step(d) { if (lbSingle) return; gi = (gi + d + db.gallery.length) % db.gallery.length; showLb(); }
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
      $("#drwB").innerHTML = '<div class="empty">القايمة فاضية.<br>ضيف اللي عايزه من المنتجات.</div>';
      $("#drwTot").textContent = "—";
      return;
    }
    var groups = {};
    list.forEach(function (l) {
      var p = prod(l.id); if (!p) return;
      (groups[p.dept] = groups[p.dept] || []).push({ l: l, p: p });
    });
    var tot = 0;
    $("#drwB").innerHTML = Object.keys(groups).map(function (did) {
      var d = dept(did), rows = groups[did], sub = 0;
      rows.forEach(function (r) { sub += (Number(r.p.price) || 0) * r.l.q; });
      tot += sub;
      return '<div class="grp" data-d="' + esc(did) + '">' +
        '<div class="gh"><span style="font-weight:500;color:var(--ink)">' + esc(d.name) + "</span>" +
        "<span>" + esc(d.phones[0]) + "</span></div>" +
        rows.map(function (r) {
          return '<div class="li" data-id="' + esc(r.p.id) + '">' +
            '<img src="' + esc(r.p.img) + '" alt="">' +
            '<div class="in"><div class="nm">' + esc(r.p.name) + "</div>" +
            '<div style="font-size:12.5px;color:var(--muted)">' + esc(price(r.p.price)) + "</div>" +
            '<div class="qt"><button data-d="-1">−</button><span>' + r.l.q + '</span><button data-d="1">+</button></div></div>' +
            '<button class="rm">حذف</button></div>';
        }).join("") +
        '<div class="gs"><button class="btn btn-w" type="button">ابعت القسم ده على واتساب</button></div></div>';
    }).join("");
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
    $$("#drwB .grp").forEach(function (g) {
      $(".gs button", g).addEventListener("click", function () { sendGroup(g.dataset.d); });
    });
  }
  function sendGroup(did) {
    var d = dept(did);
    var rows = list.map(function (l) { return { l: l, p: prod(l.id) }; })
      .filter(function (r) { return r.p && r.p.dept === did; });
    if (!rows.length) return;
    var sub = 0;
    var lines = rows.map(function (r, i) {
      sub += (Number(r.p.price) || 0) * r.l.q;
      return (i + 1) + ") " + r.p.name + " × " + r.l.q +
        (db.settings.showPrices && r.p.price ? " — " + money(r.p.price) : "");
    });
    var t = "طلب من موقع سنتر الأمير والأميرة 👑\n" + d.name + "\n\n" + lines.join("\n") +
      (db.settings.showPrices && sub ? "\n\nالإجمالي التقديري: " + money(sub) : "") +
      "\n\nياريت تأكدولي التوفر والسعر.";
    logOrder({ item: rows.map(function (r) { return r.p.name + " ×" + r.l.q; }).join(" + "),
      note: d.name, src: "list" });
    window.open(wa(d.phones[0], t), "_blank");
  }
  function openDrw() { $("#drw").classList.add("on"); $("#ov").classList.add("on"); }
  function closeDrw() { $("#drw").classList.remove("on"); $("#ov").classList.remove("on"); }
  $("#listOpen").addEventListener("click", openDrw);
  $("#drwX").addEventListener("click", closeDrw);
  $("#ov").addEventListener("click", closeDrw);
  $("#drwClr").addEventListener("click", function () { list = []; saveList(); paintList(); paintProds(); });

  function logOrder(o) {
    AStore.patch(function (d) {
      d.orders.unshift({ at: new Date().toISOString(), name: o.name || "—", phone: o.phone || "—",
        area: o.area || "—", item: o.item, note: o.note || "", src: o.src });
    });
  }

  /* ---------- فورم الطلب ---------- */
  function paintSelects() {
    $("#fDept").innerHTML = db.depts.map(function (d) {
      return '<option value="' + esc(d.id) + '">' + esc(d.name) + "</option>"; }).join("");
    var sel = $("#fItem");
    sel.innerHTML = '<option value="">اختار المنتج (اختياري)</option>' +
      db.products.map(function (p) { return "<option>" + esc(p.name) + "</option>"; }).join("") +
      "<option>حاجة تانية / مش موجودة في الموقع</option>";
  }
  $("#oForm").addEventListener("submit", function (e) {
    e.preventDefault();
    var el = e.target.elements;
    var name = el.name.value.trim(), phone = el.phone.value.trim();
    if (!name || !phone) { el[!name ? "name" : "phone"].focus(); return; }
    var d = dept(el.dept.value);
    var rec = { name: name, phone: phone, area: el.area.value.trim(),
      item: el.item.value || "—", note: el.note.value.trim(), src: "form" };
    logOrder({ item: rec.item, note: d.name + (rec.note ? " · " + rec.note : ""), src: "form",
      name: name, phone: phone, area: rec.area });
    var t = "طلب جديد من موقع سنتر الأمير والأميرة 👑\n\n" +
      "الاسم: " + rec.name + "\nالموبايل: " + rec.phone +
      (rec.area ? "\nالمنطقة: " + rec.area : "") +
      "\nالقسم: " + d.name + "\nالمنتج: " + rec.item +
      (rec.note ? "\nملاحظات: " + rec.note : "");
    window.open(wa(d.phones[0], t), "_blank");
    var m = $("#okMsg");
    m.textContent = "تمام يا " + name + " ✅ طلبك اتسجّل وفتحنا لك واتساب " + d.name +
      ". لو ما اتفتحش، كلّمنا على " + d.phones[0];
    m.classList.add("on");
    e.target.reset();
  });

  /* ---------- الهيدر ---------- */
  $("#burger").addEventListener("click", function () { $("#links").classList.toggle("on"); });
  $$("#links a").forEach(function (a) {
    a.addEventListener("click", function () { $("#links").classList.remove("on"); });
  });

  function all() {
    paintMeta(); paintStats(); paintDepts(); paintChips(); paintProds();
    paintOffers(); paintGal(); paintFaq(); paintSelects(); paintList();
  }
  all();
  AStore.on(function () { db = AStore.get(); all(); });
})();
