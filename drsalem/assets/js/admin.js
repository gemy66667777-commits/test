(function () {
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var db = DStore.get();
  var SK = "drsalem.admin.v1";

  function eg(n) { return Number(n || 0).toLocaleString("ar-EG"); }
  function uid(p) { return p + Math.random().toString(36).slice(2, 8); }
  function save(fn) { db = DStore.patch(fn); render(); }
  var tT;
  function toast(m) {
    var t = $("#toast"); t.textContent = m; t.classList.add("on");
    clearTimeout(tT); tT = setTimeout(function () { t.classList.remove("on"); }, 2200);
  }

  /* ============ الدخول ============ */
  function unlocked() { try { return sessionStorage.getItem(SK) === "1"; } catch (e) { return false; } }
  function unlock() {
    try { sessionStorage.setItem(SK, "1"); } catch (e) {}
    $("#gate").style.display = "none"; $("#app").classList.add("on"); render();
  }
  $("#gForm").addEventListener("submit", function (e) {
    e.preventDefault();
    var u = $("#gUser").value.replace(/\s/g, ""), p = $("#gPass").value;
    var ok = (u === db.settings.phone || u === "admin") && p === db.settings.adminPass;
    if (!ok) { $("#gErr").textContent = "الرقم أو كلمة السر غلط."; $("#gErr").classList.add("on"); return; }
    $("#gErr").classList.remove("on"); unlock();
  });
  $("#logout").onclick = function () { try { sessionStorage.removeItem(SK); } catch (e) {} location.reload(); };

  /* ============ التبويبات ============ */
  var TITLES = { home: "نظرة عامة", books: "الحجوزات", procs: "الخدمات", visits: "الكشف والأسعار",
    hours: "المواعيد", brs: "الفروع", steps: "الرحلة والمميزات", revs: "آراء المرضى",
    faq: "الأسئلة", set: "الإعدادات" };
  $$(".tab").forEach(function (b) {
    b.onclick = function () {
      $$(".tab").forEach(function (x) { x.classList.remove("on"); });
      $$(".panel").forEach(function (x) { x.classList.remove("on"); });
      b.classList.add("on"); $("#p-" + b.dataset.tab).classList.add("on");
      $("#topTitle").textContent = TITLES[b.dataset.tab] || "";
      $("#side").classList.remove("on");
    };
  });
  $("#mob").onclick = function () { $("#side").classList.toggle("on"); };
  $("#resetAll").onclick = function () {
    if (!confirm("هترجّع كل البيانات زي ما كانت في الأول وتمسح اللي عدّلته. متأكد؟")) return;
    DStore.reset(); db = DStore.get(); render(); toast("رجعت البيانات الأصلية");
  };

  /* ============ محرّر جداول عام ============ */
  /* cols: [{k, t, type: text|num|area|chk|plain, w}] — plain يعني نص بسيط جوه مصفوفة نصوص */
  function table(host, listKey, cols, opts) {
    opts = opts || {};
    var rows = db[listKey] || [];
    if (!rows.length) { $(host).innerHTML = "<p class='hint'>مفيش بنود — دوس على زرار الإضافة.</p>"; return; }
    var plain = cols.length === 1 && cols[0].type === "plain";
    $(host).innerHTML = "<table><thead><tr>" + cols.map(function (c) {
      return "<th" + (c.w ? ' style="width:' + c.w + '"' : "") + ">" + esc(c.t) + "</th>"; }).join("") +
      (opts.noDel ? "" : "<th style=\"width:46px\"></th>") + "</tr></thead><tbody>" +
      rows.map(function (r, i) {
        return "<tr data-i='" + i + "'>" + cols.map(function (c) {
          var v = plain ? r : r[c.k];
          if (c.type === "area") return "<td><textarea data-k='" + esc(c.k) + "'>" + esc(v || "") + "</textarea></td>";
          if (c.type === "list") return "<td><textarea data-k='" + esc(c.k) + "' data-list='1' placeholder='كل سطر بند'>" +
            esc((v || []).join("\n")) + "</textarea></td>";
          if (c.type === "chk") return "<td style='text-align:center'><input type='checkbox' data-k='" +
            esc(c.k) + "'" + (v ? " checked" : "") + "></td>";
          return "<td><input data-k='" + (plain ? "__self" : esc(c.k)) + "'" +
            (c.type === "num" ? " type='number' min='0'" : "") +
            " value='" + esc(v == null ? "" : v) + "'></td>";
        }).join("") +
        (opts.noDel ? "" : "<td><button class='ib del' data-del='" + i + "' title='حذف'>✕</button></td>") + "</tr>";
      }).join("") + "</tbody></table>";

    $$(host + " [data-k]").forEach(function (el) {
      el.onchange = function () {
        var i = +el.closest("tr").dataset.i, k = el.dataset.k, val;
        if (el.type === "checkbox") val = el.checked;
        else if (el.dataset.list) val = el.value.split("\n").map(function (x) { return x.trim(); }).filter(Boolean);
        else if (el.type === "number") val = Number(el.value) || 0;
        else val = el.value;
        save(function (d) { if (k === "__self") d[listKey][i] = val; else d[listKey][i][k] = val; });
        toast("اتحفظ");
      };
    });
    $$(host + " [data-del]").forEach(function (b) {
      b.onclick = function () {
        if (!confirm("متأكد إنك عايز تمسح البند ده؟")) return;
        save(function (d) { d[listKey].splice(+b.dataset.del, 1); }); toast("اتمسح");
      };
    });
  }

  /* ============ اللوحات ============ */
  function paintHome() {
    var bk = db.bookings || [];
    var today = new Date().toISOString().slice(0, 10);
    $("#kpis").innerHTML = [
      { n: bk.length, t: "إجمالي الحجوزات" },
      { n: bk.filter(function (b) { return b.date === today; }).length, t: "حجوزات النهاردة" },
      { n: bk.filter(function (b) { return b.status === "جديد"; }).length, t: "لسه محتاجة تأكيد" },
      { n: (db.procs || []).length, t: "خدمة" },
      { n: (db.days || []).filter(function (d) { return !d.off; }).length, t: "يوم شغل" },
      { n: (db.branches || []).length, t: "فرع" }
    ].map(function (k) {
      return "<div class='kpi'><b>" + eg(k.n) + "</b><small>" + esc(k.t) + "</small></div>"; }).join("");
    bookTable("#homeBooks", bk.slice(0, 6));
  }

  function bookTable(host, rows) {
    if (!rows.length) { $(host).innerHTML = "<p class='hint'>لسه مفيش حجوزات.</p>"; return; }
    $(host).innerHTML = "<table><thead><tr><th>الاسم</th><th>الموبايل</th><th>سبب الزيارة</th>" +
      "<th>الميعاد</th><th>ملاحظات</th><th>الحالة</th><th></th></tr></thead><tbody>" +
      rows.map(function (b) {
        var idx = db.bookings.indexOf(b);
        return "<tr><td>" + esc(b.name) + "</td>" +
          "<td dir='ltr'><a href='tel:" + esc(b.phone) + "'>" + esc(b.phone) + "</a></td>" +
          "<td>" + esc(b.reason || "—") + "</td>" +
          "<td>" + esc(b.dateTxt || b.date) + " · " + esc(b.time) + "</td>" +
          "<td>" + esc(b.note || "—") + "</td>" +
          "<td><select data-st='" + idx + "'>" +
            ["جديد", "اتأكد", "اتلغى", "حضر"].map(function (s) {
              return "<option" + (s === b.status ? " selected" : "") + ">" + s + "</option>"; }).join("") +
          "</select></td>" +
          "<td><button class='ib del' data-bdel='" + idx + "'>✕</button></td></tr>";
      }).join("") + "</tbody></table>";
    $$(host + " [data-st]").forEach(function (s) {
      s.onchange = function () { save(function (d) { d.bookings[+s.dataset.st].status = s.value; }); toast("اتحدّث"); };
    });
    $$(host + " [data-bdel]").forEach(function (b) {
      b.onclick = function () {
        if (!confirm("تمسح الحجز ده؟")) return;
        save(function (d) { d.bookings.splice(+b.dataset.bdel, 1); }); toast("اتمسح");
      };
    });
  }

  function paintSettings() {
    var s = db.settings;
    var F = [
      ["drName", "اسم الدكتور", "text"], ["drTitle", "اللقب", "text"],
      ["heroLine1", "سطر العنوان الأول", "text"], ["heroLine2", "سطر العنوان التاني", "text"],
      ["heroSub", "الجملة تحت العنوان", "area"],
      ["phone", "رقم العيادة", "text"], ["whats", "واتساب بكود الدولة", "text"],
      ["fb", "لينك فيسبوك", "text"],
      ["bookNote", "جملة فوق فورم الحجز", "text"], ["closedNote", "جملة الإجازة", "text"],
      ["currency", "العملة", "text"], ["priceNote", "بديل السعر لما يتقفل", "text"],
      ["priceHint", "ملاحظة تحت الأسعار", "area"],
      ["adminPass", "كلمة سر اللوحة", "text"]
    ];
    $("#setW").innerHTML = "<div class='grid2'>" + F.map(function (f) {
      var v = esc(s[f[0]] == null ? "" : s[f[0]]);
      return "<div class='field'><label>" + esc(f[1]) + "</label>" +
        (f[2] === "area" ? "<textarea data-s='" + f[0] + "'>" + v + "</textarea>"
                         : "<input data-s='" + f[0] + "' value='" + v + "'>") + "</div>";
    }).join("") + "</div>" +
    "<div class='field'><label><input type='checkbox' data-sb='showPrices'" + (s.showPrices ? " checked" : "") +
      "> إظهار الأسعار على الموقع</label>" +
      "<p class='hint'>لو شيلت العلامة، الأسعار هتختفي وتتبدل بجملة «" + esc(s.priceNote) + "».</p></div>";

    $$("#setW [data-s]").forEach(function (el) {
      el.onchange = function () { save(function (d) { d.settings[el.dataset.s] = el.value; }); toast("اتحفظ"); };
    });
    $("#setW [data-sb]").onchange = function () {
      var c = this.checked; save(function (d) { d.settings.showPrices = c; }); toast("اتحفظ");
    };
  }

  /* ============ رسم الكل ============ */
  function render() {
    db = DStore.get();
    $("#gBrand").textContent = db.settings.drName;
    $("#sBrand").textContent = db.settings.drName;
    var n = { nBooks: "bookings", nProcs: "procs", nVisits: "visits", nBrs: "branches",
      nRevs: "reviews", nFaq: "faq" };
    Object.keys(n).forEach(function (k) {
      var el = $("#" + k); if (el) el.textContent = eg((db[n[k]] || []).length); });

    paintHome();
    bookTable("#tBooks", db.bookings || []);

    table("#tProcs", "procs", [
      { k: "name", t: "الخدمة" },
      { k: "sub", t: "السطر الصغير" },
      { k: "icon", t: "أيقونة", w: "110px" },
      { k: "tag", t: "شارة", w: "90px" },
      { k: "desc", t: "الوصف", type: "area" }
    ]);
    table("#tVisits", "visits", [
      { k: "name", t: "البند" },
      { k: "price", t: "السعر", type: "num", w: "110px" },
      { k: "note", t: "ملاحظة", w: "170px" },
      { k: "tag", t: "شارة", w: "90px" },
      { k: "feat", t: "المميزات (سطر لكل بند)", type: "list" }
    ]);
    table("#tDays", "days", [
      { k: "name", t: "اليوم", w: "120px" },
      { k: "from", t: "من", w: "120px" },
      { k: "to", t: "لـ", w: "120px" },
      { k: "off", t: "إجازة", type: "chk", w: "70px" }
    ], { noDel: true });
    table("#tSlots", "slots", [{ k: "__self", t: "الساعة", type: "plain" }]);
    table("#tBrs", "branches", [
      { k: "name", t: "الفرع" },
      { k: "city", t: "المدينة" },
      { k: "addr", t: "العنوان", type: "area" },
      { k: "mapq", t: "بحث الخريطة" },
      { k: "main", t: "رئيسي", type: "chk", w: "70px" }
    ]);
    table("#tSteps", "steps", [
      { k: "n", t: "الرقم", w: "70px" },
      { k: "t", t: "العنوان" },
      { k: "d", t: "الشرح", type: "area" }
    ]);
    table("#tWhy", "why", [
      { k: "t", t: "الميزة" },
      { k: "d", t: "الشرح", type: "area" }
    ]);
    table("#tStats", "stats", [
      { k: "n", t: "الرقم", w: "140px" },
      { k: "t", t: "الوصف" }
    ]);
    table("#tRevs", "reviews", [
      { k: "n", t: "الاسم", w: "150px" },
      { k: "t", t: "الرأي", type: "area" },
      { k: "s", t: "نجوم", type: "num", w: "80px" }
    ]);
    table("#tFaq", "faq", [{ k: "q", t: "السؤال" }, { k: "a", t: "الإجابة", type: "area" }]);
    paintSettings();
  }

  var ADD = {
    addProc:  ["procs",    function () { return { id: uid("p"), name: "خدمة جديدة", sub: "", icon: "eye", tag: "", desc: "", price: 0 }; }],
    addVisit: ["visits",   function () { return { id: uid("v"), name: "بند جديد", price: 0, note: "", feat: [] }; }],
    addSlot:  ["slots",    function () { return "٤:٠٠ م"; }],
    addBr:    ["branches", function () { return { id: uid("b"), name: "فرع جديد", city: "", addr: "", mapq: "", main: false }; }],
    addStep:  ["steps",    function () { return { n: String((db.steps || []).length + 1), t: "خطوة", d: "" }; }],
    addWhy:   ["why",      function () { return { t: "ميزة جديدة", d: "" }; }],
    addStat:  ["stats",    function () { return { n: "", t: "" }; }],
    addRev:   ["reviews",  function () { return { n: "", t: "", s: 5 }; }],
    addFaq:   ["faq",      function () { return { q: "سؤال جديد", a: "" }; }]
  };
  Object.keys(ADD).forEach(function (id) {
    var el = $("#" + id); if (!el) return;
    el.onclick = function () {
      var spec = ADD[id];
      save(function (d) { d[spec[0]].push(spec[1]()); });
      toast("اتضاف — نزّل تحت وعدّله");
    };
  });

  window.addEventListener("drsalem:change:full", function () {
    alert("مساحة التخزين اتملت. امسح حجوزات قديمة من تبويب الحجوزات.");
  });

  if (unlocked()) unlock();
})();
