(function () {
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };

  var db = MaiStore.get();
  function eg(n)  { return Number(n || 0).toLocaleString("ar-EG"); }
  function egp(n) { return String(n).replace(/[0-9]/g, function (d) { return "٠١٢٣٤٥٦٧٨٩"[+d]; }); }
  function wa(txt){ return "https://wa.me/" + (db.settings.whats || "") + "?text=" + encodeURIComponent(txt); }
  var HI = "السلام عليكم عيادة د. مي السادات ✦";
  var DAYNAMES = ["الأحد", "الاتنين", "التلات", "الأربع", "الخميس", "الجمعة", "السبت"];
  var MON = ["يناير","فبراير","مارس","أبريل","مايو","يونيو","يوليو","أغسطس","سبتمبر","أكتوبر","نوفمبر","ديسمبر"];

  /* ============ عام ============ */
  function paintMeta() {
    var s = db.settings;
    $("#drName").textContent = s.drName; $("#drName2").textContent = s.drName;
    $("#drTitle").textContent = s.drTitle; $("#drTitle2").textContent = s.drTitle;
    $("#hl1").textContent = s.heroLine1; $("#hl2").textContent = s.heroLine2; $("#hl3").textContent = s.heroLine3;
    $("#hSub").textContent = s.heroSub; $("#fIntro").textContent = s.heroSub;
    $("#bookNote").textContent = s.bookNote || "";
    $("#revNote").textContent = s.reviewsNote || "";
    $("#kickTxt").textContent = s.reviewsNote || "";
    $("#yr").textContent = new Date().getFullYear();

    var askWa = wa(HI + "\nحابب أستفسر عن حالتي.");
    $("#heroWa").href = askWa; $("#waFab").href = askWa; $("#waDirect").href = askWa;
    $("#finalWa").href = askWa; $("#fWa").href = askWa;
    $("#callFab").href = "tel:" + s.phone;
    $("#fPhone").textContent = "الحجز " + s.phone; $("#fPhone").href = "tel:" + s.phone;
    $("#fEmg").textContent = "الطوارئ " + s.phoneEmg; $("#fEmg").href = "tel:" + s.phoneEmg;
    $("#fFb").href = s.fb || "#";

    $("#credW").innerHTML = (db.creds || []).map(function (c) {
      return '<span class="cred"><svg><use href="#i-badge"></use></svg><span><b>' + esc(c.t) +
        "</b> <small>" + esc(c.s) + "</small></span></span>";
    }).join("");

    var items = ["جراحات الثدي", "أورام الثدي", "البواسير والشرخ بالليزر", "الناسور الشرجي والعصعصي",
      "الفتاق بالمنظار", "تكميم المعدة", "تحويل المسار", "استئصال المرارة", "الزائدة الدودية",
      "الغدة الدرقية", "الجراحات الصغرى"];
    var one = items.map(function (t) { return "<span><i></i>" + esc(t) + "</span>"; }).join("");
    $("#marqW").innerHTML = one + one;

    var w = db.women || {};
    $("#wTitle").textContent = w.title || ""; $("#wSub").textContent = w.sub || "";
    $("#wBody").textContent = w.body || "";
    $("#wList").innerHTML = (w.points || []).map(function (p) {
      return '<li><svg><use href="#i-check"></use></svg><span>' + esc(p) + "</span></li>"; }).join("");

    var main = (db.branches || []).filter(function (b) { return b.main; })[0] || (db.branches || [])[0] || {};
    $("#ctW").innerHTML = [
      { k: "wa",  t: "واتساب — الحجز والاستفسار", v: s.phone, h: askWa },
      { k: "tel", t: "الحجز", v: s.phone, h: "tel:" + s.phone },
      { k: "emg", t: "الطوارئ", v: s.phoneEmg, h: "tel:" + s.phoneEmg },
      { k: "fb",  t: "فيسبوك", v: "صفحة الدكتورة", h: s.fb }
    ].filter(function (c) { return c.v && c.h; }).map(function (c) {
      var ext = /^http/.test(c.h) ? ' target="_blank" rel="noopener"' : "";
      var ltr = (c.k === "tel" || c.k === "wa" || c.k === "emg") ? ' dir="ltr"' : "";
      return '<a class="ct" href="' + esc(c.h) + '"' + ext + '><span class="i i-' + c.k +
        '"><svg><use href="#i-' + (c.k === "emg" ? "tel" : c.k) + '"></use></svg></span><span><small>' +
        esc(c.t) + "</small><b" + ltr + ">" + esc(c.v) + "</b></span></a>";
    }).join("");
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
        '<span class="ic"><svg><use href="#i-' + esc(p.icon || "plus") + '"></use></svg></span>' +
        "<h3>" + esc(p.name) + "</h3>" +
        (p.sub ? '<div class="s">' + esc(p.sub) + "</div>" : "") +
        "<p>" + esc(p.desc) + "</p>" +
        '<a class="go" href="' + esc(wa(HI + "\nحابب أستفسر عن «" + p.name + "».")) +
        '" target="_blank" rel="noopener">اسألي عن الجراحة دي<svg><use href="#i-arrow"></use></svg></a></article>';
    }).join("");
  }
  function paintSteps() {
    $("#stepW").innerHTML = (db.steps || []).map(function (s) {
      return '<div class="step"><div class="n">' + esc(s.n) + "</div><h3>" + esc(s.t) +
        "</h3><p>" + esc(s.d) + "</p></div>";
    }).join("");
  }
  function paintWhy() {
    var ic = ["badge", "chat", "heart", "shield"];
    $("#whyW").innerHTML = (db.why || []).map(function (w, i) {
      return '<div class="why"><span class="k"><svg><use href="#i-' + ic[i % ic.length] +
        '"></use></svg></span><b>' + esc(w.t) + "</b><p>" + esc(w.d) + "</p></div>";
    }).join("");
  }
  function paintBranches() {
    $("#brW").innerHTML = (db.branches || []).map(function (b) {
      return '<article class="br">' +
        '<span class="tg">' + (b.main ? "العيادة الرئيسية" : "فرع") + "</span>" +
        "<h3>" + esc(b.name) + "</h3>" +
        '<div class="hr"><svg><use href="#i-clock"></use></svg><span>' + esc(b.hoursTxt || "") + "</span></div>" +
        "<p>" + esc(b.addr) + "</p>" +
        '<div class="lnks">' +
        '<a class="btn b-o" href="' + esc(b.mapUrl || "#") + '" target="_blank" rel="noopener">' +
          '<svg><use href="#i-pin"></use></svg>الخريطة</a>' +
        '<a class="btn b-o" href="#book" data-goclin="' + esc(b.id) + '">' +
          '<svg><use href="#i-clock"></use></svg>احجزي هنا</a>' +
        "</div></article>";
    }).join("");
    $$("#brW [data-goclin]").forEach(function (a) {
      a.onclick = function () { pickClinic(a.dataset.goclin); };
    });
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

  /* ============ الحجز — المواعيد بتتغيّر حسب الفرع ============ */
  var pickedClinic = null, pickedDate = null, pickedSlot = null;
  function branch(id) { return (db.branches || []).filter(function (b) { return b.id === id; })[0]; }

  function paintBook() {
    $("#bFor").innerHTML = '<option value="">اختاري السبب</option>' +
      '<option>كشف واستشارة</option>' +
      (db.procs || []).map(function (p) { return "<option>" + esc(p.name) + "</option>"; }).join("") +
      "<option>متابعة بعد عملية</option><option>حاجة تانية</option>";

    $("#clinW").innerHTML = (db.branches || []).map(function (b) {
      return '<button type="button" class="clin" data-c="' + esc(b.id) + '"><b>' + esc(b.name) +
        "</b><small>" + esc(b.hoursTxt || "") + "</small></button>";
    }).join("");
    $$("#clinW .clin").forEach(function (b) {
      b.onclick = function () { pickClinic(b.dataset.c); };
    });

    if (!pickedClinic) {
      var m = (db.branches || []).filter(function (b) { return b.main; })[0] || (db.branches || [])[0];
      if (m) pickedClinic = m.id;
    }
    pickClinic(pickedClinic, true);
  }

  function pickClinic(id, quiet) {
    var b = branch(id); if (!b) return;
    pickedClinic = id; pickedDate = null; pickedSlot = null;
    $$("#clinW .clin").forEach(function (x) { x.classList.toggle("on", x.dataset.c === id); });
    paintDays(b); paintSlots(b);
    if (!quiet) $("#bookForm").scrollIntoView({ block: "center" });
  }

  function paintDays(b) {
    var out = [], d = new Date(); d.setHours(0, 0, 0, 0);
    var allowed = b.days || [];
    for (var i = 0; i < 60 && out.length < 10; i++) {
      var n = new Date(d.getTime() + i * 864e5);
      if (allowed.indexOf(n.getDay()) === -1) continue;
      out.push(n);
    }
    if (!out.length) { $("#dayW").innerHTML = "<p class='nt'>مفيش مواعيد متاحة — كلّمينا على واتساب.</p>"; return; }
    $("#dayW").innerHTML = out.map(function (n, i) {
      var diff = Math.round((n - d) / 864e5);
      var lbl = diff === 0 ? "النهاردة" : (diff === 1 ? "بكرة" : DAYNAMES[n.getDay()]);
      return '<button type="button" class="day" data-d="' + n.toISOString().slice(0, 10) + '">' +
        "<b>" + esc(lbl) + "</b><small>" + eg(n.getDate()) + " " + MON[n.getMonth()] + "</small></button>";
    }).join("");
    $$("#dayW .day").forEach(function (x) {
      x.onclick = function () {
        pickedDate = x.dataset.d;
        $$("#dayW .day").forEach(function (y) { y.classList.toggle("on", y === x); });
      };
    });
  }

  function paintSlots(b) {
    $("#slotW").innerHTML = (b.slots || []).map(function (s) {
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
    return DAYNAMES[n.getDay()] + "، " + eg(n.getDate()) + " " + MON[n.getMonth()] + " " + egp(n.getFullYear());
  }

  function bookSubmit(e) {
    e.preventDefault();
    var name = $("#bName").value.trim(), phone = $("#bPhone").value.trim();
    var reason = $("#bFor").value, note = $("#bNote").value.trim();
    var err = $("#bErr"), ok = $("#bOk");
    ok.classList.remove("on");
    function fail(m) { err.textContent = m; err.classList.add("on"); }

    var b = branch(pickedClinic);
    if (!b) return fail("اختاري العيادة الأول.");
    if (name.length < 3) return fail("اكتبي اسمك بالكامل من فضلك.");
    if (!/^01[0-9]{9}$/.test(phone.replace(/[\s-]/g, ""))) return fail("اكتبي رقم موبايل صحيح — ١١ رقم يبدأ بـ ٠١.");
    if (!reason) return fail("اختاري سبب الزيارة.");
    if (!pickedDate) return fail("اختاري يوم الحجز.");
    if (!pickedSlot) return fail("اختاري ساعة الحجز.");
    if ((b.days || []).indexOf(new Date(pickedDate + "T00:00:00").getDay()) === -1)
      return fail("اليوم ده مش من مواعيد «" + b.name + "» — اختاري يوم تاني.");
    err.classList.remove("on");

    /* نمسك القيم قبل الحفظ — لأن الحفظ بيعيد الرسم وبيصفّر الاختيارات */
    var theDate = pickedDate, theSlot = pickedSlot, theClinic = b.name;
    var dTxt = dateTxt(theDate);
    MaiStore.patch(function (d2) {
      d2.bookings.unshift({ id: "bk" + Date.now(), name: name, phone: phone, reason: reason,
        clinic: theClinic, date: theDate, dateTxt: dTxt, time: theSlot, note: note,
        at: new Date().toISOString(), status: "جديد" });
      if (d2.bookings.length > 300) d2.bookings.length = 300;
    });

    var msg = HI + "\nحابب أحجز ميعاد.\n\n" +
      "• الاسم: " + name + "\n" +
      "• الموبايل: " + phone + "\n" +
      "• العيادة: " + theClinic + "\n" +
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
    db = MaiStore.get();
    paintMeta(); paintStats(); paintProcs(); paintSteps(); paintWhy();
    paintBook(); paintBranches(); paintReviews(); paintFaq();
  }
  render();
  motion();
  $("#bookForm").addEventListener("submit", bookSubmit);
  MaiStore.on(function () { render(); });
})();
