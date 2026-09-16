(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var db = VStore.get();

  function wa(txt) { return "https://wa.me/" + (db.settings.whats || "") + "?text=" + encodeURIComponent(txt); }
  function price(p) {
    var s = db.settings;
    if (!s.showPrices || !Number(p)) return s.priceNote;
    return Number(p).toLocaleString("ar-EG") + " " + (s.currency || "");
  }
  var byId = function (arr, id) { return arr.filter(function (x) { return x.id === id; })[0]; };

  /* ---------- نصوص عامة ---------- */
  function paintMeta() {
    var s = db.settings;
    $("#hIntro").textContent = s.intro;
    $("#fIntro").textContent = s.intro;
    $("#hArea").textContent = s.area;  $("#tArea").textContent = s.area;
    $("#sArea").textContent = s.area;  $("#fArea").textContent = s.area;
    $("#hHours").textContent = s.hours; $("#tHours").textContent = s.hours;
    $("#sHours").textContent = s.hours; $("#fHours").textContent = s.hours;
    $("#pHint").textContent = s.priceHint || "";
    $("#sPrice").textContent = s.priceHint || "";
    $("#sPhone").textContent = s.phone; $("#sPhone").href = "tel:" + s.phone;
    $("#fPhoneA").textContent = s.phone; $("#fPhoneA").href = "tel:" + s.phone;
    $("#waFab").href = wa("السلام عليكم، جاية من موقع فيستا إيفينت ✦");
    $("#yr").textContent = new Date().getFullYear();
  }
  function paintStats() {
    $("#statsW").innerHTML = db.stats.map(function (s) {
      return '<div class="it"><div class="n">' + esc(s.n) + '</div><div class="t">' + esc(s.t) + "</div></div>";
    }).join("");
  }
  function paintSvcs() {
    $("#svcW").innerHTML = db.services.map(function (s) {
      return '<article class="svc"><div class="ic"><svg><use href="#i-' + esc(s.ic) + '"></use></svg></div>' +
        "<h3>" + esc(s.n) + "</h3><p>" + esc(s.t) + "</p></article>";
    }).join("");
  }
  function paintPkgs() {
    $("#pkgW").innerHTML = db.packages.map(function (p) {
      return '<article class="pkg" data-id="' + esc(p.id) + '">' +
        '<div class="ph"><img src="' + esc(p.img) + '" alt="' + esc(p.name) + '" loading="lazy"></div>' +
        '<div class="bd"><h3>' + esc(p.name) + "</h3><ul>" +
        p.items.map(function (i) { return "<li>" + esc(i) + "</li>"; }).join("") + "</ul>" +
        '<div class="ft"><span class="pr">' + esc(price(p.price)) + "</span>" +
        '<button class="btn btn-k" type="button" style="padding:9px 18px;font-size:13.5px">اسألي عنها</button>' +
        "</div></div></article>"; }).join("");
    $$("#pkgW .pkg").forEach(function (el) {
      var p = byId(db.packages, el.dataset.id);
      $("button", el).addEventListener("click", function () {
        log({ type: "استفسار", pkg: p.name, note: "من كارت الكوشة" });
        window.open(wa("السلام عليكم ✦\nحابة أسأل عن: " + p.name + "\n\n" +
          p.items.map(function (i) { return "• " + i; }).join("\n")), "_blank");
      });
      $(".ph", el).addEventListener("click", function () { openLb(p.img, p.name); });
    });
    var sel = $("#fPkg");
    sel.innerHTML = '<option value="">لسه مش محددة</option>' +
      db.packages.map(function (p) { return "<option>" + esc(p.name) + "</option>"; }).join("");
  }

  /* ---------- صمّم كوشتك ---------- */
  var pick = { shape: "round", light: "blue", fl: "white" }, mi = 0, matches = [], exact = true;
  function paintOpts() {
    $("#optShape").innerHTML = db.shapes.map(function (s) {
      return '<button type="button" data-v="' + esc(s.id) + '" aria-pressed="' + (pick.shape === s.id) + '">' +
        esc(s.name) + "</button>"; }).join("");
    $("#optLight").innerHTML = db.lights.map(function (l) {
      return '<button type="button" data-v="' + esc(l.id) + '" aria-pressed="' + (pick.light === l.id) + '">' +
        '<i class="sw" style="background:' + esc(l.css) + ';color:' + esc(l.css) + '"></i>' + esc(l.name) + "</button>"; }).join("");
    $("#optFl").innerHTML = db.flowers.map(function (f) {
      return '<button type="button" data-v="' + esc(f.id) + '" aria-pressed="' + (pick.fl === f.id) + '">' +
        esc(f.name) + "</button>"; }).join("");
    bind("#optShape", "shape"); bind("#optLight", "light"); bind("#optFl", "fl");
  }
  function bind(sel, key) {
    $$(sel + " button").forEach(function (b) {
      b.addEventListener("click", function () { pick[key] = b.dataset.v; mi = 0; paintOpts(); match(); });
    });
  }
  function match() {
    var g = db.gallery;
    var f3 = g.filter(function (x) { return x.shape === pick.shape && x.light === pick.light && x.fl === pick.fl; });
    var f2 = g.filter(function (x) { return x.shape === pick.shape && x.light === pick.light; });
    var f1 = g.filter(function (x) { return x.shape === pick.shape; });
    exact = f3.length > 0;
    matches = f3.length ? f3 : (f2.length ? f2 : (f1.length ? f1 : g));
    if (mi >= matches.length) mi = 0;
    show();
  }
  function show() {
    var m = matches[mi]; if (!m) return;
    $("#mkImg").src = m.img; $("#mkImg").alt = m.cap;
    $("#mkCap").textContent = m.cap;
    $("#mkStage").classList.toggle("near-on", !exact);
    var word = exact ? "بنفس الاختيار" : "قريبة من اختيارك";
    $("#mkCount").textContent = matches.length > 1
      ? (mi + 1) + " من " + matches.length + " صور " + word
      : (exact ? "صورة واحدة بالاختيار ده" : "أقرب صورة لاختيارك");
    var sh = byId(db.shapes, pick.shape), li = byId(db.lights, pick.light), fl = byId(db.flowers, pick.fl);
    $("#mkNote").textContent = exact
      ? "كوشة " + sh.name + " بإضاءة " + li.name + " و" + fl.name + " — " + sh.note + "."
      : "مفيش صورة بنفس التوليفة بالظبط، ودي أقرب حاجة ليها. ابعتيلنا اختيارك وهننفّذه.";
  }
  $("#mkPrev").addEventListener("click", function () { mi = (mi - 1 + matches.length) % matches.length; show(); });
  $("#mkNext").addEventListener("click", function () { mi = (mi + 1) % matches.length; show(); });
  $("#mkImg").addEventListener("click", function () {
    var m = matches[mi]; if (m) openLb(m.img, m.cap);
  });
  $("#mkSend").addEventListener("click", function () {
    var sh = byId(db.shapes, pick.shape), li = byId(db.lights, pick.light), fl = byId(db.flowers, pick.fl);
    var t = "السلام عليكم ✦ صمّمت كوشتي من الموقع:\n\n" +
      "• الشكل: " + sh.name + "\n• الإضاءة: " + li.name + "\n• الورد: " + fl.name +
      "\n\nياريت تبعتولي السعر والمتاح.";
    log({ type: "صمّم كوشتك", pkg: sh.name + " · " + li.name + " · " + fl.name, note: "من المصمّم" });
    window.open(wa(t), "_blank");
  });

  /* ---------- المعرض واللايت بوكس ---------- */
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

  /* ---------- الحجز ---------- */
  function log(o) {
    VStore.patch(function (d) {
      d.bookings.unshift({ at: new Date().toISOString(), name: o.name || "—", phone: o.phone || "—",
        date: o.date || "", type: o.type || "—", place: o.place || "—", pkg: o.pkg || "—",
        note: o.note || "", status: "جديد" });
    });
  }
  $("#bForm").addEventListener("submit", function (e) {
    e.preventDefault();
    var el = e.target.elements;
    var name = el.name.value.trim(), phone = el.phone.value.trim();
    if (!name || !phone) { el[!name ? "name" : "phone"].focus(); return; }
    var rec = { name: name, phone: phone, date: el.date.value, type: el.type.value,
      place: el.place.value, pkg: el.pkg.value || "—", note: el.note.value.trim() };
    log(rec);
    var t = "حجز جديد من موقع فيستا إيفينت ✦\n\n" +
      "الاسم: " + rec.name + "\nالموبايل: " + rec.phone +
      (rec.date ? "\nالتاريخ: " + rec.date : "") +
      "\nالمناسبة: " + rec.type + "\nالمكان: " + rec.place +
      "\nالكوشة: " + rec.pkg + (rec.note ? "\nملاحظات: " + rec.note : "");
    window.open(wa(t), "_blank");
    var m = $("#okMsg");
    m.textContent = "تمام يا " + name + " ✦ حجزك اتسجّل وفتحنا لك واتساب. لو ما اتفتحش، كلّمينا على " + db.settings.phone;
    m.classList.add("on");
    e.target.reset();
  });

  $("#burger").addEventListener("click", function () { $("#links").classList.toggle("on"); });
  $$("#links a").forEach(function (a) {
    a.addEventListener("click", function () { $("#links").classList.remove("on"); });
  });

  function all() { paintMeta(); paintStats(); paintOpts(); match(); paintSvcs(); paintPkgs(); paintGal(); paintFaq(); }
  all();
  VStore.on(function () { db = VStore.get(); all(); });
})();
