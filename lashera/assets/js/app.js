(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var db = LStore.get();
  var CK = "lashera.cart.v1";
  var cart = [];
  try { cart = JSON.parse(localStorage.getItem(CK)) || []; } catch (e) { cart = []; }
  var picked = {};

  function saveCart() { try { localStorage.setItem(CK, JSON.stringify(cart)); } catch (e) {} }
  function waLink(txt) { return "https://wa.me/" + (db.settings.whats || "") + "?text=" + encodeURIComponent(txt); }
  function priceText(p) {
    var s = db.settings;
    if (!s.showPrices || !Number(p)) return s.priceNote;
    return Number(p).toLocaleString("ar-EG") + " " + (s.currency || "");
  }

  /* ---------- نصوص عامة ---------- */
  function paintMeta() {
    var s = db.settings;
    $("#hIntro").textContent = s.intro;
    $("#fIntro").textContent = s.intro;
    $("#bTag").textContent = s.tagline;
    $("#tShip").textContent = s.ship;
    $("#sShip").textContent = s.ship;
    $("#sHours").textContent = s.hours;
    $("#sPhone").textContent = s.phoneShow; $("#sPhone").href = "tel:" + s.phone;
    $("#fPhoneA").textContent = s.phoneShow; $("#fPhoneA").href = "tel:" + s.phone;
    $("#sIg").textContent = "@" + s.instagram; $("#sIg").href = "https://instagram.com/" + s.instagram;
    $("#fIgA").textContent = "@" + s.instagram; $("#fIgA").href = "https://instagram.com/" + s.instagram;
    $("#fCityS").textContent = s.city;
    $("#waFab").href = waLink("السلام عليكم، حابب أستفسر عن منتجات لاشيرا 🌿");
    $("#yr").textContent = new Date().getFullYear();
  }

  function paintStats() {
    $("#statsW").innerHTML = db.stats.map(function (s) {
      return '<div class="it"><div class="n">' + esc(s.n) + '</div><div class="t">' + esc(s.t) + "</div></div>";
    }).join("");
  }

  /* ---------- المنتجات ---------- */
  function paintProds() {
    $("#prodW").innerHTML = db.products.map(function (p, i) {
      var szs = (p.sizes && p.sizes.length ? p.sizes : ["عبوة"]);
      if (!picked[p.id]) picked[p.id] = szs[0];
      return '<article class="card" data-i="' + i + '">' +
        '<div class="ph"><img src="' + esc(p.img) + '" alt="' + esc(p.name) + '" loading="lazy">' +
        (p.badge ? '<span class="badge">' + esc(p.badge) + "</span>" : "") + "</div>" +
        '<div class="bd"><h3>' + esc(p.name) + "</h3>" +
        '<p class="ds">' + esc(p.desc) + "</p>" +
        '<div class="szs">' + szs.map(function (z) {
          return '<button type="button" data-sz="' + esc(z) + '" aria-pressed="' +
            (picked[p.id] === z) + '">' + esc(z) + "</button>"; }).join("") + "</div>" +
        '<div class="pr"><span class="p">' + esc(priceText(p.price)) + "</span>" +
        '<button class="add" type="button">أضف للسلة</button></div></div></article>';
    }).join("");

    $$("#prodW .card").forEach(function (card) {
      var p = db.products[+card.dataset.i];
      $$(".szs button", card).forEach(function (b) {
        b.addEventListener("click", function () {
          picked[p.id] = b.dataset.sz;
          $$(".szs button", card).forEach(function (x) { x.setAttribute("aria-pressed", x === b); });
        });
      });
      $(".add", card).addEventListener("click", function () { addToCart(p, picked[p.id]); });
    });
  }

  function paintSelect() {
    var sel = $("#fItem");
    sel.innerHTML = '<option value="">اختار المنتج</option>' + db.products.map(function (p) {
      return "<option>" + esc(p.name) + "</option>"; }).join("") +
      "<option>حاجة تانية / مش متأكد</option>";
  }

  /* ---------- أقسام تانية ---------- */
  function paintOils() {
    $("#oilW").innerHTML = db.oils.map(function (o, i) {
      return '<div class="oil"><div class="dot">' + (i + 1) + "</div><h3>" + esc(o.n) +
        "</h3><p>" + esc(o.t) + "</p></div>"; }).join("");
  }
  function paintBens() {
    $("#benW").innerHTML = db.benefits.map(function (b) {
      return '<div class="ben"><i>✓</i><span>' + esc(b) + "</span></div>"; }).join("");
  }
  function paintHow() {
    $("#howW").innerHTML = db.howto.map(function (h) {
      return '<div class="step"><span class="no">' + esc(h.s) + "</span><h3>" + esc(h.n) +
        "</h3><p>" + esc(h.t) + "</p></div>"; }).join("");
  }
  function paintFaq() {
    $("#faqW").innerHTML = db.faq.map(function (f) {
      return "<details><summary>" + esc(f.q) + "</summary><p>" + esc(f.a) + "</p></details>"; }).join("");
  }

  /* ---------- المعرض واللايت بوكس ---------- */
  var gi = 0;
  function paintGal() {
    $("#galW").innerHTML = db.gallery.map(function (g, i) {
      return '<figure data-i="' + i + '"><img src="' + esc(g.img) + '" alt="' + esc(g.cap) +
        '" loading="lazy"><figcaption>' + esc(g.cap) + "</figcaption></figure>"; }).join("");
    $$("#galW figure").forEach(function (f) {
      f.addEventListener("click", function () { gi = +f.dataset.i; showLb(); });
    });
  }
  function showLb() {
    var g = db.gallery[gi]; if (!g) return;
    $("#lbI").src = g.img; $("#lbI").alt = g.cap; $("#lbC").textContent = g.cap;
    $("#lb").classList.add("on");
  }
  function step(d) { gi = (gi + d + db.gallery.length) % db.gallery.length; showLb(); }
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

  /* ---------- السلة ---------- */
  function addToCart(p, sz) {
    var f = cart.filter(function (c) { return c.id === p.id && c.sz === sz; })[0];
    if (f) f.q++; else cart.push({ id: p.id, name: p.name, img: p.img, sz: sz, q: 1 });
    saveCart(); paintCart(); openCart();
  }
  function paintCart() {
    var n = cart.reduce(function (a, c) { return a + c.q; }, 0);
    $("#cnt").textContent = n;
    if (db.settings.showPrices) {
      var tot = cart.reduce(function (a, c) {
        var p = db.products.filter(function (x) { return x.id === c.id; })[0];
        return a + (p ? Number(p.price) || 0 : 0) * c.q; }, 0);
      $("#cartTot").textContent = tot
        ? tot.toLocaleString("ar-EG") + " " + (db.settings.currency || "")
        : db.settings.priceNote;
    } else { $("#cartTot").textContent = db.settings.priceNote; }
    if (!cart.length) { $("#cartB").innerHTML = '<div class="empty">السلة فاضية لسه.<br>اختار منتج وضيفه.</div>'; return; }
    $("#cartB").innerHTML = cart.map(function (c, i) {
      return '<div class="ci" data-i="' + i + '"><img src="' + esc(c.img) + '" alt="' + esc(c.name) + '">' +
        '<div class="in"><div class="nm">' + esc(c.name) + '</div><div class="sz">' + esc(c.sz) + "</div>" +
        '<div class="qt"><button data-d="-1">−</button><span>' + c.q + '</span><button data-d="1">+</button></div></div>' +
        '<button class="rm">حذف</button></div>'; }).join("");
    $$("#cartB .ci").forEach(function (el) {
      var i = +el.dataset.i;
      $$(".qt button", el).forEach(function (b) {
        b.addEventListener("click", function () {
          cart[i].q += +b.dataset.d;
          if (cart[i].q < 1) cart.splice(i, 1);
          saveCart(); paintCart();
        });
      });
      $(".rm", el).addEventListener("click", function () { cart.splice(i, 1); saveCart(); paintCart(); });
    });
  }
  function openCart() { $("#cart").classList.add("on"); $("#ov").classList.add("on"); }
  function closeCart() { $("#cart").classList.remove("on"); $("#ov").classList.remove("on"); }
  $("#cartOpen").addEventListener("click", openCart);
  $("#cartX").addEventListener("click", closeCart);
  $("#ov").addEventListener("click", closeCart);
  $("#cartClr").addEventListener("click", function () { cart = []; saveCart(); paintCart(); });
  $("#cartSend").addEventListener("click", function () {
    if (!cart.length) { openCart(); return; }
    var t = "طلب من موقع لاشيرا ستور 🌿\n\n" + cart.map(function (c, i) {
      return (i + 1) + ") " + c.name + " — " + c.sz + " × " + c.q; }).join("\n") +
      "\n\nياريت تبعتولي السعر وطريقة التوصيل.";
    LStore.patch(function (d) {
      d.orders.unshift({ at: new Date().toISOString(), name: "—", phone: "—", city: "—",
        item: cart.map(function (c) { return c.name + " (" + c.sz + ") ×" + c.q; }).join(" + "),
        note: "من السلة", src: "cart" });
    });
    window.open(waLink(t), "_blank");
  });

  /* ---------- فورم الطلب ---------- */
  $("#oForm").addEventListener("submit", function (e) {
    e.preventDefault();
    var el = e.target.elements;
    var name = el.name.value.trim(), phone = el.phone.value.trim();
    if (!name || !phone) { el[!name ? "name" : "phone"].focus(); return; }
    var rec = { at: new Date().toISOString(), name: name, phone: phone,
      city: el.city.value.trim(), item: el.item.value || "—", note: el.note.value.trim(), src: "form" };
    LStore.patch(function (d) { d.orders.unshift(rec); });
    var t = "طلب جديد من موقع لاشيرا ستور 🌿\n\n" +
      "الاسم: " + rec.name + "\nالموبايل: " + rec.phone +
      (rec.city ? "\nالمدينة: " + rec.city : "") +
      "\nالمنتج: " + rec.item + (rec.note ? "\nملاحظات: " + rec.note : "");
    window.open(waLink(t), "_blank");
    var m = $("#okMsg");
    m.textContent = "تمام يا " + name + " ✅ طلبك اتسجّل وفتحنا لك واتساب. لو ما اتفتحش، كلّمنا على " + db.settings.phoneShow;
    m.classList.add("on");
    e.target.reset();
  });

  /* ---------- الهيدر ---------- */
  $("#burger").addEventListener("click", function () { $("#links").classList.toggle("on"); });
  $$("#links a").forEach(function (a) {
    a.addEventListener("click", function () { $("#links").classList.remove("on"); });
  });

  function all() { paintMeta(); paintStats(); paintProds(); paintSelect(); paintOils();
    paintBens(); paintHow(); paintGal(); paintFaq(); paintCart(); }
  all();
  LStore.on(function () { db = LStore.get(); all(); });
})();
