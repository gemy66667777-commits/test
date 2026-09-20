(function () {
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };

  var db = SCStore.get();
  function eg(n)  { return Number(n || 0).toLocaleString("ar-EG"); }
  function egp(n) { return String(n).replace(/[0-9]/g, function (d) { return "٠١٢٣٤٥٦٧٨٩"[+d]; }); }
  function money(n) { return eg(n) + " " + (db.settings.currency || ""); }
  function wa(txt){ return "https://wa.me/" + (db.settings.whats || "") + "?text=" + encodeURIComponent(txt); }
  function proc(id) { return (db.procs || []).filter(function (p) { return p.id === id; })[0]; }
  var HI = "السلام عليكم Smile Care Center ✦";
  var MON = ["يناير","فبراير","مارس","أبريل","مايو","يونيو","يوليو","أغسطس","سبتمبر","أكتوبر","نوفمبر","ديسمبر"];

  function dayByDow(d) { return (db.days || []).filter(function (x) { return Number(x.dow) === d; })[0]; }
  function isOpenDay(d) { var x = dayByDow(d); return !!x && !x.off; }

  /* ============ عام ============ */
  function paintMeta() {
    var s = db.settings;
    $("#brandEn").textContent = s.brand; $("#brandEn2").textContent = s.brand;
    $("#drName").textContent = s.drName + " — " + s.drTitle;
    $("#drName2").textContent = s.drName + " — " + s.drTitle;
    $("#hl1").textContent = s.heroLine1; $("#hl2").textContent = s.heroLine2;
    $("#hSub").textContent = s.heroSub; $("#fIntro").textContent = s.heroSub;
    $("#pHint").textContent = s.priceHint || "";
    $("#bookNote").textContent = s.bookNote || "";
    $("#apptNote").textContent = s.apptOnly || "";
    $("#yr").textContent = new Date().getFullYear();

    var askWa = wa(HI + "\nحابب أستفسر عن حالة سناني.");
    $("#heroWa").href = askWa; $("#waFab").href = askWa; $("#waDirect").href = askWa;
    $("#finalWa").href = askWa; $("#fWa").href = askWa;
    $("#callFab").href = "tel:" + s.phone;
    $("#fPhone").textContent = s.phone; $("#fPhone").href = "tel:" + s.phone;
    $("#fMail").textContent = s.email; $("#fMail").href = "mailto:" + s.email;
    $("#fMap").href = s.mapUrl || "#";

    /* شارات الهيرو */
    var d = dayByDow(new Date().getDay());
    $("#badgeW").innerHTML = [
      { b: "زراعة وتجميل", s: "التخصص" },
      { b: d && !d.off ? d.from + " — " + d.to : "الجمعة إجازة", s: d && !d.off ? "مفتوح النهاردة" : "بنفتح " + nextOpenName() },
      { b: "الشيخ زايد", s: "الجيزة" },
      { b: "بالحجز", s: "من غير انتظار" }
    ].map(function (x) {
      return '<span class="hb"><svg><use href="#i-star"></use></svg><span><b>' + esc(x.b) +
        "</b> " + esc(x.s) + "</span></span>";
    }).join("");

    var items = ["زراعة الأسنان", "ابتسامة هوليود", "الفينير واللومينير", "تيجان الزيركون",
      "تبييض بالليزر", "علاج العصب", "الحشو التجميلي", "تنظيف الجير", "تقويم الأسنان",
      "ضرس العقل", "أسنان الأطفال"];
    var one = items.map(function (t) { return "<span><i></i>" + esc(t) + "</span>"; }).join("");
    $("#marqW").innerHTML = one + one;

    var f = db.fear || {};
    $("#fTitle").textContent = f.title || ""; $("#fSub").textContent = f.sub || "";
    $("#fBody").textContent = f.body || "";
    $("#fList").innerHTML = (f.points || []).map(function (p) {
      return '<li><svg><use href="#i-check"></use></svg><span>' + esc(p) + "</span></li>"; }).join("");

    $("#ctW").innerHTML = [
      { k: "wa",   t: "واتساب — الحجز والاستفسار", v: s.phone, h: askWa },
      { k: "tel",  t: "اتصال مباشر", v: s.phone, h: "tel:" + s.phone },
      { k: "pin",  t: "العنوان", v: s.addr, h: s.mapUrl },
      { k: "mail", t: "البريد الإلكتروني", v: s.email, h: "mailto:" + s.email }
    ].filter(function (c) { return c.v && c.h; }).map(function (c) {
      var ext = /^http/.test(c.h) ? ' target="_blank" rel="noopener"' : "";
      var ltr = (c.k === "tel" || c.k === "wa" || c.k === "mail") ? ' dir="ltr"' : "";
      return '<a class="ct" href="' + esc(c.h) + '"' + ext + '><span class="i i-' + c.k +
        '"><svg><use href="#i-' + c.k + '"></use></svg></span><span><small>' + esc(c.t) +
        "</small><b" + ltr + ">" + esc(c.v) + "</b></span></a>";
    }).join("");
  }

  function nextOpenName() {
    var d = new Date();
    for (var i = 1; i <= 7; i++) {
      var n = new Date(d.getTime() + i * 864e5);
      if (isOpenDay(n.getDay())) return dayByDow(n.getDay()).name;
    }
    return "";
  }

  function paintStats() {
    $("#statsW").innerHTML = (db.stats || []).map(function (s) {
      return '<div class="stat"><div class="n">' + esc(s.n) + '</div><div class="t">' + esc(s.t) + "</div></div>";
    }).join("");
  }

  /* ============ الخدمات + الفلاتر ============ */
  var filter = "all";
  function paintTabs() {
    var cats = [{ id: "all", name: "الكل" }].concat(db.cats || []);
    $("#tabW").innerHTML = cats.map(function (c) {
      return '<button type="button" class="tab' + (c.id === filter ? " on" : "") +
        '" data-c="' + esc(c.id) + '">' + esc(c.name) + "</button>"; }).join("");
    $$("#tabW .tab").forEach(function (b) {
      b.onclick = function () { filter = b.dataset.c; paintTabs(); paintProcs(); };
    });
  }
  function paintProcs() {
    var rows = (db.procs || []).filter(function (p) { return filter === "all" || p.cat === filter; });
    $("#procW").innerHTML = rows.map(function (p) {
      var show = db.settings.showPrices && Number(p.price);
      return '<article class="proc">' +
        (p.tag ? '<span class="tg">' + esc(p.tag) + "</span>" : "") +
        '<span class="ic"><svg><use href="#i-' + esc(p.icon || "tooth") + '"></use></svg></span>' +
        "<h3>" + esc(p.name) + "</h3>" +
        (p.sub ? '<div class="s">' + esc(p.sub) + "</div>" : "") +
        "<p>" + esc(p.desc) + "</p>" +
        '<div class="pr' + (show ? "" : " soft") + '">' +
          (show ? money(p.price) : esc(db.settings.priceNote)) + "</div>" +
        '<a class="go" href="' + esc(wa(HI + "\nحابب أستفسر عن «" + p.name + "».")) +
        '" target="_blank" rel="noopener">اسأل عن الخدمة دي<svg><use href="#i-arrow"></use></svg></a></article>';
    }).join("");
  }

  /* ============ الباقات ============ */
  function calcPkg(p) {
    var was = 0, its = [];
    (p.items || []).forEach(function (it) {
      var s = proc(it.id); if (!s) return;
      var q = Number(it.q) || 1;
      was += (Number(s.price) || 0) * q;
      its.push({ s: s, q: q });
    });
    return { its: its, was: Number(p.was) || was };
  }
  function paintPkgs() {
    $("#pkgW").innerHTML = (db.packages || []).map(function (p) {
      var c = calcPkg(p), save = c.was - Number(p.price || 0);
      var show = db.settings.showPrices && Number(p.price);
      var pct = c.was > 0 ? Math.round(save / c.was * 100) : 0;
      return '<article class="pkg">' +
        (p.tag ? '<span class="tg">' + esc(p.tag) + "</span>" : "") +
        "<h3>" + esc(p.name) + '</h3><p class="sub">' + esc(p.sub || "") + "</p>" +
        '<div class="prc">' + (show
          ? '<span class="now">' + money(p.price) + "</span>" +
            (save > 0 ? '<span class="was">' + money(c.was) + "</span>" : "")
          : '<span class="now" style="font-size:1.1rem">' + esc(db.settings.priceNote) + "</span>") + "</div>" +
        (show && save > 0 ? '<span class="save">توفير ' + money(save) + "</span>" +
          '<span class="save pct">خصم ' + eg(pct) + "٪</span>" : "") +
        "<ul>" + c.its.map(function (x) {
          return '<li><svg><use href="#i-check"></use></svg><span>' + esc(x.s.name) +
            (x.q > 1 ? " × " + eg(x.q) : "") + "</span></li>"; }).join("") + "</ul>" +
        '<a class="btn b-d" href="' + esc(wa(HI + "\nحابب أحجز «" + p.name + "»" +
          (show ? " بسعر " + money(p.price) : "") + ".")) +
        '" target="_blank" rel="noopener"><svg><use href="#i-wa"></use></svg>احجز الباقة</a></article>';
    }).join("");
  }

  function paintSteps() {
    $("#stepW").innerHTML = (db.steps || []).map(function (s) {
      return '<div class="step"><div class="n">' + esc(s.n) + "</div><h3>" + esc(s.t) +
        "</h3><p>" + esc(s.d) + "</p></div>";
    }).join("");
  }
  function paintWhy() {
    var ic = ["doc", "smile", "clock", "star"];
    $("#whyW").innerHTML = (db.why || []).map(function (w, i) {
      return '<div class="why"><span class="k"><svg><use href="#i-' + ic[i % ic.length] +
        '"></use></svg></span><b>' + esc(w.t) + "</b><p>" + esc(w.d) + "</p></div>";
    }).join("");
  }
  function paintHours() {
    var today = new Date().getDay();
    $("#hoursW").innerHTML = (db.days || []).map(function (d) {
      var off = !!d.off;
      return '<div class="hrow' + (off ? " off" : "") + (Number(d.dow) === today ? " now" : "") + '">' +
        "<b>" + esc(d.name) + "</b>" +
        '<span class="t">' + (off ? "إجازة" : esc(d.from) + " — " + esc(d.to)) + "</span></div>";
    }).join("");
  }
  function paintReviews() {
    $("#revW").innerHTML = (db.reviews || []).map(function (r) {
      var st = Number(r.s) || 5;
      return '<article class="rev"><span class="qt">”</span><div class="st">' +
        "★".repeat(st) + "☆".repeat(5 - st) + "</div><p>" + esc(r.t) + "</p>" +
        '<div class="who"><span class="av">' + esc((r.n || "؟").trim().charAt(0)) + "</span><b>" +
        esc(r.n) + "</b></div></article>";
    }).join("");
  }
  function paintFaq() {
    $("#faqW").innerHTML = (db.faq || []).map(function (f) {
      return '<div class="fq"><button type="button" class="q">' + esc(f.q) +
        '<span class="ch"><svg><use href="#i-chev"></use></svg></span></button>' +
        '<div class="a"><p>' + esc(f.a) + "</p></div></div>";
    }).join("");
    $$("#faqW .fq").forEach(function (fq) {
      fq.querySelector(".q").onclick = function () {
        var open = fq.classList.contains("on");
        $$("#faqW .fq").forEach(function (o) { o.classList.remove("on"); o.querySelector(".a").style.maxHeight = 0; });
        if (!open) {
          fq.classList.add("on");
          fq.querySelector(".a").style.maxHeight = fq.querySelector(".a").scrollHeight + "px";
        }
      };
    });
  }

  /* ============ الحجز ============ */
  var pickedDate = null, pickedSlot = null;

  function paintBook() {
    $("#bFor").innerHTML = '<option value="">اختار السبب</option>' +
      '<option>كشف وفحص عام</option>' +
      (db.procs || []).map(function (p) { return "<option>" + esc(p.name) + "</option>"; }).join("") +
      "<option>متابعة علاج</option><option>حالة مستعجلة (ألم)</option>";

    var out = [], d = new Date(); d.setHours(0, 0, 0, 0);
    for (var i = 0; i < 40 && out.length < 12; i++) {
      var n = new Date(d.getTime() + i * 864e5);
      if (!isOpenDay(n.getDay())) continue;
      out.push(n);
    }
    if (!out.length) { $("#dayW").innerHTML = "<p class='nt'>مفيش مواعيد متاحة — كلّمنا على واتساب.</p>"; return; }
    $("#dayW").innerHTML = out.map(function (n) {
      var diff = Math.round((n - d) / 864e5);
      var lbl = diff === 0 ? "النهاردة" : (diff === 1 ? "بكرة" : dayByDow(n.getDay()).name);
      return '<button type="button" class="day" data-d="' + n.toISOString().slice(0, 10) + '">' +
        "<b>" + esc(lbl) + "</b><small>" + eg(n.getDate()) + " " + MON[n.getMonth()] + "</small></button>";
    }).join("");
    $$("#dayW .day").forEach(function (x) {
      x.onclick = function () {
        pickedDate = x.dataset.d;
        $$("#dayW .day").forEach(function (y) { y.classList.toggle("on", y === x); });
      };
    });

    $("#slotW").innerHTML = (db.slots || []).map(function (s) {
      return '<button type="button" class="slot" data-s="' + esc(s) + '">' + esc(s) + "</button>";
    }).join("");
    $$("#slotW .slot").forEach(function (x) {
      x.onclick = function () {
        pickedSlot = x.dataset.s;
        $$("#slotW .slot").forEach(function (y) { y.classList.toggle("on", y === x); });
      };
    });
  }

  function dateTxt(iso) {
    var n = new Date(iso + "T00:00:00");
    return (dayByDow(n.getDay()) || {}).name + "، " + eg(n.getDate()) + " " + MON[n.getMonth()] +
      " " + egp(n.getFullYear());
  }

  function bookSubmit(e) {
    e.preventDefault();
    var name = $("#bName").value.trim(), phone = $("#bPhone").value.trim();
    var reason = $("#bFor").value, note = $("#bNote").value.trim();
    var err = $("#bErr"), ok = $("#bOk");
    ok.classList.remove("on");
    function fail(m) { err.textContent = m; err.classList.add("on"); }

    if (name.length < 3) return fail("اكتب اسمك بالكامل من فضلك.");
    if (!/^01[0-9]{9}$/.test(phone.replace(/[\s-]/g, ""))) return fail("اكتب رقم موبايل صحيح — ١١ رقم يبدأ بـ ٠١.");
    if (!reason) return fail("اختار سبب الزيارة.");
    if (!pickedDate) return fail("اختار يوم الحجز.");
    if (!pickedSlot) return fail("اختار ساعة الحجز.");
    if (!isOpenDay(new Date(pickedDate + "T00:00:00").getDay()))
      return fail("اليوم ده إجازة في العيادة — اختار يوم تاني.");
    err.classList.remove("on");

    /* نمسك القيم قبل الحفظ — الحفظ بيعيد الرسم وبيصفّر الاختيارات */
    var theDate = pickedDate, theSlot = pickedSlot;
    var dTxt = dateTxt(theDate);
    SCStore.patch(function (d2) {
      d2.bookings.unshift({ id: "bk" + Date.now(), name: name, phone: phone, reason: reason,
        date: theDate, dateTxt: dTxt, time: theSlot, note: note,
        at: new Date().toISOString(), status: "جديد" });
      if (d2.bookings.length > 300) d2.bookings.length = 300;
    });

    var msg = HI + "\nحابب أحجز ميعاد.\n\n" +
      "• الاسم: " + name + "\n" +
      "• الموبايل: " + phone + "\n" +
      "• سبب الزيارة: " + reason + "\n" +
      "• اليوم: " + dTxt + "\n" +
      "• الساعة: " + theSlot +
      (note ? "\n• ملاحظات: " + note : "") +
      "\n\nياريت تأكدولي الميعاد ده.";
    window.open(wa(msg), "_blank");
    ok.classList.add("on");
    $("#bName").value = ""; $("#bPhone").value = ""; $("#bNote").value = ""; $("#bFor").value = "";
    pickedDate = null; pickedSlot = null;
    $$("#dayW .day").forEach(function (x) { x.classList.remove("on"); });
    $$("#slotW .slot").forEach(function (x) { x.classList.remove("on"); });
  }

  /* ============ حركة ============ */
  function motion() {
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var hdr = $("#hdr");
    function onScroll() { hdr.classList.toggle("sc", window.scrollY > 30); }
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

    if ("IntersectionObserver" in window && !reduce) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
      }, { threshold: .06, rootMargin: "0px 0px -70px 0px" });
      $$(".rv").forEach(function (e) { io.observe(e); });
      setTimeout(function () {
        if (!document.querySelector(".rv.in")) $$(".rv").forEach(function (e) { e.classList.add("in"); });
      }, 2200);
    } else { $$(".rv").forEach(function (e) { e.classList.add("in"); }); }

    var dr = $("#drawer"), sc = $("#scrim");
    function close() { dr.classList.remove("on"); sc.classList.remove("on"); document.body.style.overflow = ""; }
    $("#burger").onclick = function () {
      dr.classList.add("on"); sc.classList.add("on"); document.body.style.overflow = "hidden"; };
    $("#dx").onclick = close; sc.onclick = close;
    $$("#drawer a").forEach(function (a) { a.onclick = close; });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
  }

  /* ============ تشغيل ============ */
  function render() {
    db = SCStore.get();
    paintMeta(); paintStats(); paintTabs(); paintProcs(); paintPkgs();
    paintSteps(); paintWhy(); paintBook(); paintHours(); paintReviews(); paintFaq();
  }
  render();
  motion();
  $("#bookForm").addEventListener("submit", bookSubmit);
  SCStore.on(function () { render(); });
})();
