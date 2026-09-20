(function () {
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };

  var db = DStore.get();
  function eg(n)    { return Number(n || 0).toLocaleString("ar-EG"); }
  /* رقم من غير فاصلة آلاف — للسنين */
  function egp(n)   { return String(n).replace(/[0-9]/g, function (d) { return "٠١٢٣٤٥٦٧٨٩"[+d]; }); }
  function money(n) { return eg(n) + " " + (db.settings.currency || ""); }
  function price(p) { return db.settings.showPrices && Number(p) ? money(p) : db.settings.priceNote; }
  function wa(txt)  { return "https://wa.me/" + (db.settings.whats || "") + "?text=" + encodeURIComponent(txt); }
  function mapUrl(q){ return "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(q); }
  var HI = "السلام عليكم عيادة د. محمود سالم ✦";

  function dayByDow(d) { return (db.days || []).filter(function (x) { return Number(x.dow) === d; })[0]; }
  function isOpenDay(d) { var x = dayByDow(d); return !!x && !x.off; }

  /* ============ عام ============ */
  function paintMeta() {
    var s = db.settings;
    $("#drName").textContent = s.drName; $("#drName2").textContent = s.drName;
    $("#drTitle").textContent = s.drTitle; $("#drTitle2").textContent = s.drTitle;
    $("#hl1").textContent = s.heroLine1; $("#hl2").textContent = s.heroLine2;
    $("#hSub").textContent = s.heroSub; $("#fIntro").textContent = s.heroSub;
    $("#pHint").textContent = s.priceHint || "";
    $("#bookNote").textContent = s.bookNote || "";
    $("#closedNote").textContent = s.closedNote || "";
    $("#yr").textContent = new Date().getFullYear();

    var askWa = wa(HI + "\nحابب أستفسر عن حالتي.");
    $("#heroCall").href = "tel:" + s.phone;
    $("#callFab").href = "tel:" + s.phone;
    $("#waFab").href = askWa; $("#waDirect").href = askWa; $("#finalWa").href = askWa; $("#fWa").href = askWa;
    $("#fPhone").textContent = s.phone; $("#fPhone").href = "tel:" + s.phone;
    $("#fFb").href = s.fb || "#";
    var main = (db.branches || []).filter(function (b) { return b.main; })[0] || (db.branches || [])[0] || {};
    $("#fMap").href = mapUrl(main.mapq || main.addr || "");

    /* الشريط */
    var items = ["الفيمتو سمايل", "الفيمتوليزك", "الليزك السطحي", "زراعة عدسات ICL",
      "المياه البيضاء", "جراحات الشبكية", "حقن الشبكية", "الحول وعيون الأطفال",
      "تجميل الجفون", "الياج والأرجون ليزر", "النظارات والعدسات"];
    var one = items.map(function (t) { return "<span><i></i>" + esc(t) + "</span>"; }).join("");
    $("#marqW").innerHTML = one + one;

    /* مفتوح دلوقتي؟ */
    var now = new Date(), d = dayByDow(now.getDay());
    var open = d && !d.off;
    $("#liveKick").classList.toggle("off", !open);
    $("#liveTxt").textContent = open
      ? "العيادة شغالة النهاردة · " + d.from + " — " + d.to
      : "النهاردة إجازة · بنفتح " + nextOpenName();
    $("#hNote").textContent = open
      ? "العيادة شغالة النهاردة من " + d.from + " لـ " + d.to
      : (s.closedNote || "") + " — احجز لأقرب يوم شغّال";

    /* التواصل */
    $("#ctW").innerHTML = [
      { k: "wa",  t: "واتساب — الحجز والاستفسار", v: s.phone, h: askWa },
      { k: "tel", t: "اتصال مباشر", v: s.phone, h: "tel:" + s.phone },
      { k: "pin", t: "العيادة الرئيسية", v: main.city || "", h: mapUrl(main.mapq || main.addr || "") },
      { k: "fb",  t: "فيسبوك", v: "صفحة العيادة", h: s.fb }
    ].filter(function (c) { return c.v && c.h; }).map(function (c) {
      var ext = /^http/.test(c.h) ? ' target="_blank" rel="noopener"' : "";
      var ltr = (c.k === "tel" || c.k === "wa") ? ' dir="ltr"' : "";
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

  function paintProcs() {
    $("#procW").innerHTML = (db.procs || []).map(function (p) {
      return '<article class="proc">' +
        (p.tag ? '<span class="tg">' + esc(p.tag) + "</span>" : "") +
        '<span class="ic"><svg><use href="#i-' + esc(p.icon || "eye") + '"></use></svg></span>' +
        "<h3>" + esc(p.name) + "</h3>" +
        (p.sub ? '<div class="s">' + esc(p.sub) + "</div>" : "") +
        "<p>" + esc(p.desc) + "</p>" +
        '<a class="go" href="' + esc(wa(HI + "\nحابب أستفسر عن «" + p.name + "».")) +
        '" target="_blank" rel="noopener">اسأل عن الخدمة دي<svg><use href="#i-arrow"></use></svg></a></article>';
    }).join("");
  }

  function paintSteps() {
    $("#stepW").innerHTML = (db.steps || []).map(function (s) {
      return '<div class="step"><div class="n">' + esc(s.n) + "</div><h3>" + esc(s.t) +
        "</h3><p>" + esc(s.d) + "</p></div>";
    }).join("");
  }

  function paintWhy() {
    var ic = ["shield", "eye", "laser", "map"];
    $("#whyW").innerHTML = (db.why || []).map(function (w, i) {
      return '<div class="why"><span class="k"><svg><use href="#i-' + ic[i % ic.length] +
        '"></use></svg></span><b>' + esc(w.t) + "</b><p>" + esc(w.d) + "</p></div>";
    }).join("");
  }

  function paintVisits() {
    $("#visitW").innerHTML = (db.visits || []).map(function (v) {
      var show = db.settings.showPrices && Number(v.price);
      return '<article class="visit">' +
        (v.tag ? '<span class="tg">' + esc(v.tag) + "</span>" : "") +
        "<h3>" + esc(v.name) + "</h3>" +
        '<div class="nt">' + esc(v.note || "&nbsp;") + "</div>" +
        '<div class="pr">' + (show ? eg(v.price) + ' <small>' + esc(db.settings.currency) + "</small>"
          : '<span style="font-size:1.2rem">' + esc(db.settings.priceNote) + "</span>") + "</div>" +
        "<ul>" + (v.feat || []).map(function (f) {
          return '<li><svg><use href="#i-check"></use></svg><span>' + esc(f) + "</span></li>"; }).join("") + "</ul>" +
        '<a class="btn b-o" href="#book">احجز ميعاد</a></article>';
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

  function paintBranches() {
    $("#brW").innerHTML = (db.branches || []).map(function (b) {
      return '<article class="br">' +
        (b.main ? '<span class="tg">الفرع الرئيسي</span>' : '<span class="tg">فرع</span>') +
        "<h3>" + esc(b.name) + "</h3><p>" + esc(b.addr) + "</p>" +
        '<div class="lnks">' +
        '<a class="btn b-o" href="' + esc(mapUrl(b.mapq || b.addr)) +
          '" target="_blank" rel="noopener"><svg><use href="#i-pin"></use></svg>الخريطة</a>' +
        '<a class="btn b-o" href="' + esc(wa(HI + "\nحابب أستفسر عن مواعيد «" + b.name + "».")) +
          '" target="_blank" rel="noopener"><svg><use href="#i-wa"></use></svg>اسأل عنه</a>' +
        "</div></article>";
    }).join("");
  }

  function paintReviews() {
    $("#revW").innerHTML = (db.reviews || []).map(function (r) {
      var st = Number(r.s) || 5;
      return '<article class="rev"><div class="st">' + "★".repeat(st) + "☆".repeat(5 - st) + "</div>" +
        "<p>" + esc(r.t) + "</p>" +
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
  var MON = ["يناير","فبراير","مارس","أبريل","مايو","يونيو","يوليو","أغسطس","سبتمبر","أكتوبر","نوفمبر","ديسمبر"];

  function paintBook() {
    /* سبب الزيارة */
    $("#bFor").innerHTML = '<option value="">اختار السبب</option>' +
      '<option>كشف وفحص عام</option>' +
      (db.procs || []).map(function (p) { return "<option>" + esc(p.name) + "</option>"; }).join("") +
      "<option>إعادة كشف / متابعة</option><option>حاجة تانية</option>";

    /* أقرب ١٤ يوم شغّال */
    var out = [], d = new Date(); d.setHours(0, 0, 0, 0);
    for (var i = 0; i < 30 && out.length < 14; i++) {
      var n = new Date(d.getTime() + i * 864e5);
      if (!isOpenDay(n.getDay())) continue;
      out.push(n);
    }
    $("#dayW").innerHTML = out.map(function (n, i) {
      var nm = dayByDow(n.getDay()).name;
      var lbl = i === 0 ? "النهاردة" : (i === 1 && (n - d) / 864e5 === 1 ? "بكرة" : nm);
      return '<button type="button" class="day" data-d="' + n.toISOString().slice(0, 10) + '">' +
        "<b>" + esc(lbl) + "</b><small>" + eg(n.getDate()) + " " + MON[n.getMonth()] + "</small></button>";
    }).join("");
    $$("#dayW .day").forEach(function (b) {
      b.onclick = function () {
        pickedDate = b.dataset.d;
        $$("#dayW .day").forEach(function (x) { x.classList.toggle("on", x === b); });
      };
    });

    $("#slotW").innerHTML = (db.slots || []).map(function (s) {
      return '<button type="button" class="slot" data-s="' + esc(s) + '">' + esc(s) + "</button>";
    }).join("");
    $$("#slotW .slot").forEach(function (b) {
      b.onclick = function () {
        pickedSlot = b.dataset.s;
        $$("#slotW .slot").forEach(function (x) { x.classList.toggle("on", x === b); });
      };
    });
  }

  function dateTxt(iso) {
    var n = new Date(iso + "T00:00:00");
    var nm = (dayByDow(n.getDay()) || {}).name || "";
    return nm + "، " + eg(n.getDate()) + " " + MON[n.getMonth()] + " " + egp(n.getFullYear());
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

    var dTxt = dateTxt(pickedDate);
    DStore.patch(function (d2) {
      d2.bookings.unshift({ id: "bk" + Date.now(), name: name, phone: phone, reason: reason,
        date: pickedDate, dateTxt: dTxt, time: pickedSlot, note: note,
        at: new Date().toISOString(), status: "جديد" });
      if (d2.bookings.length > 300) d2.bookings.length = 300;
    });

    var msg = HI + "\nحابب أحجز ميعاد.\n\n" +
      "• الاسم: " + name + "\n" +
      "• الموبايل: " + phone + "\n" +
      "• سبب الزيارة: " + reason + "\n" +
      "• اليوم: " + dTxt + "\n" +
      "• الساعة: " + pickedSlot +
      (note ? "\n• ملاحظات: " + note : "") +
      "\n\nياريت تأكدولي الميعاد ده.";
    window.open(wa(msg), "_blank");
    ok.classList.add("on");
    $("#bookForm").reset();
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
    db = DStore.get();
    paintMeta(); paintStats(); paintProcs(); paintSteps(); paintWhy();
    paintVisits(); paintBook(); paintHours(); paintBranches(); paintReviews(); paintFaq();
  }
  render();
  motion();
  $("#bookForm").addEventListener("submit", bookSubmit);
  DStore.on(function () { render(); });
})();
