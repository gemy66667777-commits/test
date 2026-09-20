(function () {
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };

  var db = EStore.get();
  var LOGO = '<svg viewBox="0 0 64 64"><circle cx="32" cy="14" r="7.6" fill="#E0272C"/>' +
    '<path d="M30.2 56.5C21.6 52.8 15.2 44.6 14 34.6c-.5-4.2.4-7.7 2.6-9.2 2.4-1.7 5.1-.4 6.3 3 1.1 3.1 1.4 6 1.4 9.6 0 1.1 1.6 1.1 1.7 0 .3-5.6 1.3-9.9 3.1-12.6 1.6-2.4 4-2.4 5.2.2 1 2.2 1 5.3.2 9.2-.2 1.1 1.3 1.5 1.6.4 1.3-4.3 3-7.2 5-8.4 2.2-1.3 4.3.2 4.4 3 .1 2.3-.6 5-2 8-.5 1 .8 1.8 1.4.9 1.7-2.5 3.4-3.8 5-3.6 2 .3 3 2.3 2.4 5.3-1.6 8.3-7.7 15-15.5 18.1-2 .8-4.2.8-6.1 0Z" fill="#12459B"/></svg>';

  function eg(n)    { return Number(n || 0).toLocaleString("ar-EG"); }
  function money(n) { return eg(n) + " " + (db.settings.currency || ""); }
  function price(p) { return db.settings.showPrices && Number(p) ? money(p) : db.settings.priceNote; }
  function wa(txt)  { return "https://wa.me/" + (db.settings.whats || "") + "?text=" + encodeURIComponent(txt); }
  function lab(id)  { return db.labs.filter(function (l) { return l.id === id; })[0]; }
  var HI = "السلام عليكم مستشفى علاج ✦";

  /* ============ الترويسة والبيانات العامة ============ */
  function paintMeta() {
    var s = db.settings;
    $("#logoMk").innerHTML = LOGO; $("#logoMk2").innerHTML = LOGO;
    $("#brandAr").textContent = s.brandAr; $("#brandAr2").textContent = s.brandAr;
    $$(".js-tag").forEach(function (e) { e.textContent = s.tagline; });
    $("#hIntro").textContent = s.intro; $("#fIntro").textContent = s.intro;
    $("#clinHours").textContent = s.clinicHours;
    $("#priceHint").textContent = s.priceHint || "";
    $("#addrTxt").textContent = s.addr;
    $("#yr").textContent = new Date().getFullYear();

    $("#hdrCall").href = "tel:" + s.phone;
    $("#ctaCall").href = "tel:" + s.phone;
    $("#emgFab").href = "tel:" + s.phone;
    $("#waFab").href = wa(HI + "\nحابب أستفسر عن خدمة.");
    $("#fPhone").textContent = s.phone; $("#fPhone").href = "tel:" + s.phone;
    $("#fWa").href = wa(HI + "\nحابب أستفسر عن خدمة.");
    $("#fMail").textContent = s.email; $("#fMail").href = "mailto:" + s.email;
    var mu = s.mapUrl || ("https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(s.mapq || s.addr));
    $("#mapBtn").href = mu; $("#fMap").href = mu;

    /* الوصول السريع في الهيرو */
    $("#quickW").innerHTML = [
      { i: "emg",   s: "استقبال وطوارئ", b: "٢٤ ساعة", h: "tel:" + s.phone },
      { i: "clock", s: "العيادات الخارجية", b: "٦ م — ١١ م", h: "#clinics" },
      { i: "gamca", s: "فحص دول الخليج", b: "٩ ص — ٤ ع", h: "#services" },
      { i: "pin",   s: "مكرم عبيد", b: "مدينة نصر", h: mu }
    ].map(function (q) {
      var ext = /^http/.test(q.h) ? ' target="_blank" rel="noopener"' : "";
      return '<a class="qk" href="' + esc(q.h) + '"' + ext + '><span class="i"><svg><use href="#i-' + q.i +
        '"></use></svg></span><span><small>' + esc(q.s) + "</small><b>" + esc(q.b) + "</b></span></a>";
    }).join("");

    /* الشريط المتحرك — متكرر مرتين عشان اللف يبقى ناعم */
    var items = ["طوارئ واستقبال ٢٤ ساعة", "وحدة ولادة وحضانات", "معامل تحاليل داخل المستشفى",
      "أشعة إكس وسونار", "عيادات في كل التخصصات", "مركز معتمد لفحص العمالة الوافدة",
      "غرف إقامة وسويتات", "رعاية مركزة"];
    var one = items.map(function (t) {
      return '<span><svg><use href="#i-spark"></use></svg>' + esc(t) + "</span>"; }).join("");
    $("#marqW").innerHTML = one + one;

    /* التواصل */
    $("#ctW").innerHTML = [
      { k: "wa",   t: "واتساب — الحجز والاستفسار", v: s.phone, h: wa(HI + "\nحابب أستفسر عن خدمة.") },
      { k: "tel",  t: "الطوارئ والاستقبال", v: s.phone2 || s.phone, h: "tel:" + (s.phone2 || s.phone) },
      { k: "pin",  t: "العنوان", v: "مكرم عبيد — مدينة نصر", h: mu },
      { k: "mail", t: "البريد الإلكتروني", v: s.email, h: "mailto:" + s.email }
    ].filter(function (c) { return c.v; }).map(function (c) {
      var ext = /^http/.test(c.h) ? ' target="_blank" rel="noopener"' : "";
      var ltr = (c.k === "tel" || c.k === "wa") ? ' dir="ltr"' : "";
      return '<a class="ct" href="' + esc(c.h) + '"' + ext + '><span class="i ' + c.k +
        '"><svg><use href="#i-' + c.k + '"></use></svg></span><span><small>' + esc(c.t) +
        "</small><b" + ltr + ">" + esc(c.v) + "</b></span></a>";
    }).join("");

    $("#hrsW").innerHTML = [s.emergency, s.clinicHours, s.gamcaHours].filter(Boolean).map(function (h) {
      return '<div class="hr"><svg><use href="#i-clock"></use></svg><span>' + esc(h) + "</span></div>"; }).join("");

    /* مؤشر «مفتوح دلوقتي» */
    var now = new Date(), hh = now.getHours();
    $("#liveTxt").textContent = (hh >= 18 && hh < 23)
      ? "العيادات شغالة دلوقتي · الطوارئ ٢٤ ساعة"
      : (hh >= 9 && hh < 16 ? "فحص العمالة شغال دلوقتي · الطوارئ ٢٤ ساعة" : "الطوارئ مفتوحة دلوقتي");
  }

  function paintStats() {
    $("#statsW").innerHTML = db.stats.map(function (s) {
      return '<div class="stat"><div class="n">' + esc(s.n) + '</div><div class="t">' + esc(s.t) + "</div></div>";
    }).join("");
  }
  function paintWhy() {
    var ic = ["emg", "birth", "lab", "shield"];
    $("#whyW").innerHTML = db.why.map(function (w, i) {
      return '<div class="why"><span class="k"><svg><use href="#i-' + ic[i % ic.length] + '"></use></svg></span>' +
        "<b>" + esc(w.n) + "</b><p>" + esc(w.t) + "</p></div>";
    }).join("");
  }

  /* ============ الخدمات ============ */
  function paintServices() {
    $("#svcW").innerHTML = db.services.map(function (v) {
      return '<article class="svc">' +
        '<div class="ph">' +
          (v.img ? '<img src="' + esc(v.img) + '" alt="' + esc(v.name) + '" loading="lazy">' : "") +
          (v.tag ? '<span class="tg">' + esc(v.tag) + "</span>" : "") +
          '<span class="ic"><svg><use href="#i-' + esc(v.icon || "lab") + '"></use></svg></span>' +
        "</div>" +
        '<div class="bd"><h3>' + esc(v.name) + "</h3><p>" + esc(v.desc) + "</p>" +
        '<a class="go" href="' + esc(wa(HI + "\nحابب أستفسر عن «" + v.name + "».")) +
        '" target="_blank" rel="noopener">اسأل عن الخدمة دي<svg><use href="#i-arrow"></use></svg></a></div></article>';
    }).join("");
  }

  /* ============ العيادات والحجز ============ */
  var SLOTS = ["٦:٠٠ م", "٧:٠٠ م", "٨:٠٠ م", "٩:٠٠ م", "١٠:٠٠ م", "١١:٠٠ م"];
  var pickedClinic = null, pickedSlot = null;

  function paintClinics() {
    $("#clinW").innerHTML = db.clinics.map(function (c) {
      return '<button type="button" class="clin" data-id="' + esc(c.id) + '"><b>' + esc(c.name) +
        "</b><small>" + esc(c.note || "") + "</small></button>";
    }).join("");
    $("#bClinic").innerHTML = '<option value="">اختار التخصص</option>' + db.clinics.map(function (c) {
      return '<option value="' + esc(c.id) + '">' + esc(c.name) + "</option>"; }).join("");
    $("#slotW").innerHTML = SLOTS.map(function (s) {
      return '<button type="button" class="slot" data-s="' + esc(s) + '">' + esc(s) + "</button>"; }).join("");

    $$("#clinW .clin").forEach(function (b) {
      b.onclick = function () { selectClinic(b.dataset.id); $("#bookForm").scrollIntoView({ block: "center" }); };
    });
    $("#bClinic").onchange = function () { selectClinic(this.value, true); };
    $$("#slotW .slot").forEach(function (b) {
      b.onclick = function () {
        pickedSlot = b.dataset.s;
        $$("#slotW .slot").forEach(function (x) { x.classList.toggle("on", x === b); });
      };
    });

    /* التاريخ: من النهاردة لشهر قدام */
    var d = new Date(), max = new Date(Date.now() + 30 * 864e5);
    var f = function (x) { return x.toISOString().slice(0, 10); };
    $("#bDate").min = f(d); $("#bDate").max = f(max); $("#bDate").value = f(d);
  }
  function selectClinic(id, fromSelect) {
    pickedClinic = id || null;
    $$("#clinW .clin").forEach(function (x) { x.classList.toggle("on", x.dataset.id === id); });
    if (!fromSelect) $("#bClinic").value = id || "";
  }

  function bookSubmit(e) {
    e.preventDefault();
    var name = $("#bName").value.trim(), phone = $("#bPhone").value.trim();
    var cid = $("#bClinic").value, date = $("#bDate").value, note = $("#bNote").value.trim();
    var err = $("#bErr"), ok = $("#bOk");
    ok.classList.remove("on");
    function fail(m) { err.textContent = m; err.classList.add("on"); }

    if (name.length < 3) return fail("اكتب اسمك بالكامل من فضلك.");
    if (!/^01[0-9]{9}$/.test(phone.replace(/\s|-/g, ""))) return fail("اكتب رقم موبايل صحيح — ١١ رقم يبدأ بـ ٠١.");
    if (!cid) return fail("اختار العيادة اللي عايز تحجز فيها.");
    if (!date) return fail("اختار تاريخ الحجز.");
    if (!pickedSlot) return fail("اختار ساعة الحجز.");
    err.classList.remove("on");

    var cname = (db.clinics.filter(function (c) { return c.id === cid; })[0] || {}).name || "—";
    var dTxt = new Date(date + "T00:00:00").toLocaleDateString("ar-EG",
      { weekday: "long", day: "numeric", month: "long", year: "numeric" });

    EStore.patch(function (d2) {
      d2.bookings.unshift({ id: "bk" + Date.now(), name: name, phone: phone, clinic: cname,
        date: date, dateTxt: dTxt, time: pickedSlot, note: note, at: new Date().toISOString(), status: "جديد" });
      if (d2.bookings.length > 300) d2.bookings.length = 300;
    });

    var msg = HI + "\nحابب أحجز في العيادة.\n\n" +
      "• الاسم: " + name + "\n" +
      "• الموبايل: " + phone + "\n" +
      "• العيادة: " + cname + "\n" +
      "• التاريخ: " + dTxt + "\n" +
      "• الساعة: " + pickedSlot +
      (note ? "\n• ملاحظات: " + note : "") +
      "\n\nياريت تأكدولي الميعاد ده.";
    window.open(wa(msg), "_blank");
    ok.classList.add("on");
    $("#bookForm").reset();
    pickedSlot = null;
    $$("#slotW .slot").forEach(function (x) { x.classList.remove("on"); });
    $("#bDate").value = new Date().toISOString().slice(0, 10);
  }

  /* ============ الباقات ============ */
  function calcPkg(p) {
    var was = 0, its = [];
    (p.items || []).forEach(function (it) {
      var l = lab(it.id); if (!l) return;
      var q = Number(it.q) || 1;
      was += (Number(l.price) || 0) * q;
      its.push({ l: l, q: q });
    });
    return { its: its, sum: was, was: Number(p.was) || was };
  }
  function paintPackages() {
    $("#pkgW").innerHTML = db.packages.map(function (p) {
      var c = calcPkg(p), save = c.was - Number(p.price || 0);
      var show = db.settings.showPrices && Number(p.price);
      var pct = c.was > 0 ? Math.round(save / c.was * 100) : 0;
      return '<article class="pkg">' +
        (p.tag ? '<span class="tg">' + esc(p.tag) + "</span>" : "") +
        "<h3>" + esc(p.name) + '</h3><p class="sub">' + esc(p.sub || "") + "</p>" +
        '<div class="prc">' + (show
          ? '<span class="now">' + money(p.price) + "</span>" +
            (save > 0 ? '<span class="was">' + money(c.was) + "</span>" : "")
          : '<span class="now" style="font-size:1.1rem">' + esc(db.settings.priceNote) + "</span>") +
        "</div>" +
        (show && save > 0 ? '<span class="save">توفير ' + money(save) + "</span>" +
          '<span class="save pct">خصم ' + eg(pct) + "٪</span>" : "") +
        "<ul>" + c.its.map(function (x) {
          return "<li><svg><use href=\"#i-check\"></use></svg><span>" + esc(x.l.name) +
            (x.q > 1 ? " × " + eg(x.q) : "") + "</span></li>"; }).join("") + "</ul>" +
        '<a class="btn btn-b" href="' + esc(wa(HI + "\nحابب أحجز «" + p.name + "»" +
          (show ? " بسعر " + money(p.price) : "") + ".\nياريت تقولولي المواعيد المتاحة.")) +
        '" target="_blank" rel="noopener"><svg><use href="#i-wa"></use></svg>احجز الباقة</a></article>';
    }).join("");
  }

  /* ============ التحاليل ============ */
  var filter = "all", q = "";
  function paintTabs() {
    var cats = [{ id: "all", name: "الكل" }].concat(db.labcats);
    $("#tabW").innerHTML = cats.map(function (c) {
      return '<button type="button" class="tab' + (c.id === filter ? " on" : "") +
        '" data-c="' + esc(c.id) + '">' + esc(c.name) + "</button>"; }).join("");
    $$("#tabW .tab").forEach(function (b) {
      b.onclick = function () { filter = b.dataset.c; paintTabs(); paintLabs(); };
    });
  }
  function paintLabs() {
    var rows = db.labs.filter(function (l) {
      var okc = filter === "all" || l.cat === filter;
      var okq = !q || (l.name || "").toLowerCase().indexOf(q) > -1;
      return okc && okq;
    });
    $("#labEmpty").style.display = rows.length ? "none" : "block";
    $("#labW").innerHTML = rows.map(function (l) {
      return '<div class="lab"><span class="nm">' + esc(l.name) + "</span>" +
        '<span class="pr">' + esc(price(l.price)) + "</span></div>";
    }).join("");
  }

  /* ============ الغرف والولادة ============ */
  function card(r) {
    var show = db.settings.showPrices && Number(r.price);
    return '<article class="room">' +
      (r.img ? '<div class="ph"><img src="' + esc(r.img) + '" alt="' + esc(r.name) + '" loading="lazy">' +
        (r.tag ? '<span class="tg">' + esc(r.tag) + "</span>" : "") + "</div>" : "") +
      '<div class="bd"><h3>' + esc(r.name) + "</h3>" +
      '<div class="pr">' + (show
        ? "<b>" + money(r.price) + "</b>" + (r.per ? "<small>/ " + esc(r.per) + "</small>" : "")
        : '<b style="font-size:1.05rem">' + esc(db.settings.priceNote) + "</b>") + "</div>" +
      "<ul>" + (r.feat || []).map(function (f) {
        return '<li><svg><use href="#i-check"></use></svg><span>' + esc(f) + "</span></li>"; }).join("") + "</ul>" +
      '<a class="btn btn-o" href="' + esc(wa(HI + "\nحابب أستفسر عن «" + r.name + "»" +
        (show ? " بسعر " + money(r.price) + (r.per ? " / " + r.per : "") : "") + ".")) +
      '" target="_blank" rel="noopener"><svg><use href="#i-wa"></use></svg>استفسر واحجز</a></div></article>';
  }
  function paintRooms() {
    $("#roomW").innerHTML = db.rooms.map(card).join("");
    $("#birthW").innerHTML = db.births.map(card).join("");
  }

  /* ============ المعرض واللايت بوكس ============ */
  var gi = 0;
  function paintGallery() {
    $("#galW").innerHTML = db.gallery.map(function (g, i) {
      return '<figure class="gi" data-i="' + i + '"><img src="' + esc(g.img) + '" alt="' + esc(g.cap || "") +
        '" loading="lazy"><figcaption class="cap">' + esc(g.cap || "") + "</figcaption></figure>";
    }).join("");
    $$("#galW .gi").forEach(function (f) { f.onclick = function () { openLb(+f.dataset.i); }; });
  }
  function openLb(i) {
    if (!db.gallery.length) return;
    gi = (i + db.gallery.length) % db.gallery.length;
    $("#lbI").src = db.gallery[gi].img;
    $("#lbC").textContent = db.gallery[gi].cap || "";
    $("#lb").classList.add("on");
    document.body.style.overflow = "hidden";
  }
  function closeLb() { $("#lb").classList.remove("on"); document.body.style.overflow = ""; }

  /* ============ آراء وأسئلة ============ */
  function paintReviews() {
    $("#revW").innerHTML = db.reviews.map(function (r) {
      var st = Number(r.s) || 5;
      return '<article class="rev"><span class="qt">”</span>' +
        '<div class="st">' + "★".repeat(st) + "☆".repeat(5 - st) + "</div>" +
        "<p>" + esc(r.t) + "</p>" +
        '<div class="who"><span class="av">' + esc((r.n || "؟").trim().charAt(0)) + "</span>" +
        "<b>" + esc(r.n) + "</b></div></article>";
    }).join("");
  }
  function paintFaq() {
    $("#faqW").innerHTML = db.faq.map(function (f) {
      return '<div class="fq"><button type="button" class="q">' + esc(f.q) +
        '<span class="ch"><svg><use href="#i-chev"></use></svg></span></button>' +
        '<div class="a"><p>' + esc(f.a) + "</p></div></div>";
    }).join("");
    $$("#faqW .fq").forEach(function (fq) {
      fq.querySelector(".q").onclick = function () {
        var open = fq.classList.contains("on");
        $$("#faqW .fq").forEach(function (o) { o.classList.remove("on"); o.querySelector(".a").style.maxHeight = 0; });
        if (!open) { fq.classList.add("on"); fq.querySelector(".a").style.maxHeight = fq.querySelector(".a").scrollHeight + "px"; }
      };
    });
  }

  /* ============ حركات ============ */
  function motion() {
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    /* الهيدر + شريط التقدّم */
    var hdr = $("#hdr"), prog = $("#prog");
    function onScroll() {
      hdr.classList.toggle("sc", window.scrollY > 40);
      var h = document.documentElement.scrollHeight - window.innerHeight;
      prog.style.transform = "scaleX(" + (h > 0 ? window.scrollY / h : 0) + ")";
    }
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

    /* الظهور التدريجي */
    if ("IntersectionObserver" in window && !reduce) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
      }, { threshold: .08, rootMargin: "0px 0px -60px 0px" });
      $$(".rv").forEach(function (e) { io.observe(e); });
      /* احتياطي: لو المراقب ما اشتغلش لأي سبب، نظهّر كل حاجة بعد ثانيتين */
      setTimeout(function () {
        if (!document.querySelector(".rv.in")) $$(".rv").forEach(function (e) { e.classList.add("in"); });
      }, 2000);
    } else { $$(".rv").forEach(function (e) { e.classList.add("in"); }); }

    /* الدرج */
    var dr = $("#drawer"), sc = $("#scrim");
    function close() { dr.classList.remove("on"); sc.classList.remove("on"); document.body.style.overflow = ""; }
    $("#burger").onclick = function () { dr.classList.add("on"); sc.classList.add("on"); document.body.style.overflow = "hidden"; };
    $("#dx").onclick = close; sc.onclick = close;
    $$("#drawer a").forEach(function (a) { a.onclick = close; });

    /* اللايت بوكس */
    $("#lbX").onclick = closeLb;
    $("#lbP").onclick = function (e) { e.stopPropagation(); openLb(gi - 1); };
    $("#lbN").onclick = function (e) { e.stopPropagation(); openLb(gi + 1); };
    $("#lb").onclick = function (e) { if (e.target.id === "lb") closeLb(); };
    document.addEventListener("keydown", function (e) {
      if (!$("#lb").classList.contains("on")) { if (e.key === "Escape") close(); return; }
      if (e.key === "Escape") closeLb();
      if (e.key === "ArrowLeft") openLb(gi + 1);
      if (e.key === "ArrowRight") openLb(gi - 1);
    });
  }

  /* ============ تشغيل ============ */
  function render() {
    db = EStore.get();
    paintMeta(); paintStats(); paintWhy(); paintServices();
    paintClinics(); paintPackages(); paintTabs(); paintLabs();
    paintRooms(); paintGallery(); paintReviews(); paintFaq();
  }
  render();
  motion();
  $("#bookForm").addEventListener("submit", bookSubmit);
  $("#q").addEventListener("input", function () { q = this.value.trim().toLowerCase(); paintLabs(); });
  EStore.on(function () { render(); });
})();
