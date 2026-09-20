(function () {
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var db = SCStore.get();
  var SK = "smilecare.admin.v1";

  function eg(n) { return Number(n || 0).toLocaleString("ar-EG"); }
  function money(n) { return eg(n) + " " + (db.settings.currency || ""); }
  function uid(p) { return p + Math.random().toString(36).slice(2, 8); }
  function save(fn) { db = SCStore.patch(fn); render(); }
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
  var TITLES = { home: "نظرة عامة", books: "الحجوزات", procs: "الخدمات والأسعار", pkgs: "الباقات",
    hours: "المواعيد", steps: "الرحلة والمميزات", fear: "قسم الخوف", revs: "آراء المرضى",
    faq: "الأسئلة", set: "الإعدادات" };
  $$(".tab").forEach(function (b) {
    b.onclick = function () {
      $$(".tab").forEach(function (x) { x.classList.remove("on"); });
      $$(".panel").forEach(function (x) { x.classList.remove("on"); });
      b.classList.add("on");
      var pane = $("#p-" + b.dataset.tab); if (pane) pane.classList.add("on");
      $("#topTitle").textContent = TITLES[b.dataset.tab] || "";
      $("#side").classList.remove("on");
    };
  });
  $("#mob").onclick = function () { $("#side").classList.toggle("on"); };
  $("#resetAll").onclick = function () {
    if (!confirm("هترجّع كل البيانات زي ما كانت في الأول وتمسح اللي عدّلته. متأكد؟")) return;
    SCStore.reset(); db = SCStore.get(); render(); toast("رجعت البيانات الأصلية");
  };

  /* ============ محرّر جداول عام ============ */
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
          if (c.type === "lines") return "<td><textarea data-k='" + esc(c.k) + "' data-lines='1'>" +
            esc((v || []).join("\n")) + "</textarea></td>";
          if (c.type === "chk") return "<td style='text-align:center'><input type='checkbox' data-k='" +
            esc(c.k) + "'" + (v ? " checked" : "") + "></td>";
          if (c.type === "sel") return "<td><select data-k='" + esc(c.k) + "'>" +
            (c.opts() || []).map(function (o) {
              return "<option value='" + esc(o.id) + "'" + (o.id === v ? " selected" : "") + ">" +
                esc(o.name) + "</option>"; }).join("") + "</select></td>";
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
        else if (el.dataset.lines) val = el.value.split("\n").map(function (x) { return x.trim(); }).filter(Boolean);
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
      { n: (db.packages || []).length, t: "باقة" },
      { n: (db.days || []).filter(function (d) { return !d.off; }).length, t: "يوم شغل" }
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

  function paintPkgs() {
    var opts = (db.procs || []).map(function (p) { return { id: p.id, name: p.name }; });
    $("#pkgList").innerHTML = (db.packages || []).map(function (p, i) {
      var was = (p.items || []).reduce(function (a, it) {
        var s = (db.procs || []).filter(function (x) { return x.id === it.id; })[0];
        return a + (s ? (Number(s.price) || 0) * (Number(it.q) || 1) : 0); }, 0);
      var sv = was - (Number(p.price) || 0);
      var warn = was === 0 ? "<div class='warn'>كل الخدمات اللي في الباقة دي سعرها صفر — السعر قبل العرض مش هيظهر.</div>" : "";
      return "<div class='card' data-p='" + i + "' style='background:#FBFAF7'>" + warn +
        "<div class='grid3'>" +
        "<div class='field'><label>اسم الباقة</label><input data-pk='name' value='" + esc(p.name || "") + "'></div>" +
        "<div class='field'><label>السعر بعد العرض</label><input data-pk='price' type='number' min='0' value='" + esc(p.price || 0) + "'></div>" +
        "<div class='field'><label>شارة (اختياري)</label><input data-pk='tag' value='" + esc(p.tag || "") + "'></div>" +
        "</div>" +
        "<div class='field'><label>وصف قصير</label><input data-pk='sub' value='" + esc(p.sub || "") + "'></div>" +
        "<div class='field'><label>الخدمات اللي في الباقة</label><div class='picklist'>" +
          (p.items || []).map(function (it, j) {
            return "<div class='pickrow'><select data-it='" + j + "'>" + opts.map(function (o) {
              return "<option value='" + esc(o.id) + "'" + (o.id === it.id ? " selected" : "") + ">" +
                esc(o.name) + "</option>"; }).join("") + "</select>" +
              "<input type='number' min='1' value='" + (Number(it.q) || 1) + "' data-itq='" + j + "'>" +
              "<button class='ib del' data-itdel='" + j + "'>✕</button></div>";
          }).join("") + "</div>" +
          "<button class='btn xs' data-additem>+ خدمة</button></div>" +
        "<p class='hint'>السعر قبل العرض المحسوب: <b>" + money(was) + "</b> · التوفير: <b>" + money(sv) + "</b></p>" +
        "<button class='btn danger xs' data-pdel>حذف الباقة</button></div>";
    }).join("") || "<p class='hint'>مفيش باقات.</p>";

    $$("#pkgList [data-p]").forEach(function (box) {
      var i = +box.dataset.p;
      $$("[data-pk]", box).forEach(function (el) {
        el.onchange = function () {
          var v = el.type === "number" ? Number(el.value) || 0 : el.value;
          save(function (d) { d.packages[i][el.dataset.pk] = v; }); toast("اتحفظ");
        };
      });
      $$("[data-it]", box).forEach(function (s) {
        s.onchange = function () { save(function (d) { d.packages[i].items[+s.dataset.it].id = s.value; }); };
      });
      $$("[data-itq]", box).forEach(function (s) {
        s.onchange = function () { save(function (d) { d.packages[i].items[+s.dataset.itq].q = Number(s.value) || 1; }); };
      });
      $$("[data-itdel]", box).forEach(function (s) {
        s.onclick = function () { save(function (d) { d.packages[i].items.splice(+s.dataset.itdel, 1); }); };
      });
      $("[data-additem]", box).onclick = function () {
        var first = (db.procs[0] || {}).id; if (!first) return;
        save(function (d) { d.packages[i].items.push({ id: first, q: 1 }); });
      };
      $("[data-pdel]", box).onclick = function () {
        if (!confirm("تمسح الباقة دي؟")) return;
        save(function (d) { d.packages.splice(i, 1); }); toast("اتمسحت");
      };
    });
  }

  function paintFear() {
    var f = db.fear || {};
    $("#fearW").innerHTML =
      "<div class='field'><label>العنوان</label><input data-w='title' value='" + esc(f.title || "") + "'></div>" +
      "<div class='field'><label>السطر الذهبي</label><input data-w='sub' value='" + esc(f.sub || "") + "'></div>" +
      "<div class='field'><label>الفقرة</label><textarea data-w='body'>" + esc(f.body || "") + "</textarea></div>" +
      "<div class='field'><label>النقط (كل نقطة في سطر)</label><textarea data-w='points' data-lines='1'>" +
        esc((f.points || []).join("\n")) + "</textarea></div>";
    $$("#fearW [data-w]").forEach(function (el) {
      el.onchange = function () {
        var k = el.dataset.w;
        var val = el.dataset.lines ? el.value.split("\n").map(function (x) { return x.trim(); }).filter(Boolean) : el.value;
        save(function (d) { d.fear[k] = val; }); toast("اتحفظ");
      };
    });
  }

  function paintSettings() {
    var s = db.settings;
    var F = [
      ["brand", "اسم المركز", "text"], ["drName", "اسم الدكتور", "text"], ["drTitle", "التخصص", "text"],
      ["heroLine1", "العنوان — سطر ١", "text"], ["heroLine2", "العنوان — الكلمة الملوّنة", "text"],
      ["heroSub", "الجملة تحت العنوان", "area"],
      ["phone", "رقم العيادة", "text"], ["whats", "واتساب بكود الدولة", "text"],
      ["email", "البريد", "text"], ["mapUrl", "لينك الخريطة", "text"], ["addr", "العنوان", "text"],
      ["bookNote", "جملة فوق فورم الحجز", "text"], ["apptOnly", "جملة المواعيد", "text"],
      ["currency", "العملة", "text"], ["priceNote", "بديل السعر", "text"],
      ["priceHint", "ملاحظة الأسعار", "area"], ["adminPass", "كلمة سر اللوحة", "text"]
    ];
    $("#setW").innerHTML = "<div class='grid2'>" + F.map(function (f) {
      var v = esc(s[f[0]] == null ? "" : s[f[0]]);
      return "<div class='field'><label>" + esc(f[1]) + "</label>" +
        (f[2] === "area" ? "<textarea data-s='" + f[0] + "'>" + v + "</textarea>"
                         : "<input data-s='" + f[0] + "' value='" + v + "'>") + "</div>";
    }).join("") + "</div>" +
    "<div class='field'><label><input type='checkbox' data-sb='showPrices'" + (s.showPrices ? " checked" : "") +
      "> إظهار الأسعار على الموقع</label>" +
      "<p class='hint'>لو شيلت العلامة، كل الأسعار هتختفي وتتبدل بجملة «" + esc(s.priceNote) + "».</p></div>";
    $$("#setW [data-s]").forEach(function (el) {
      el.onchange = function () { save(function (d) { d.settings[el.dataset.s] = el.value; }); toast("اتحفظ"); };
    });
    $("#setW [data-sb]").onchange = function () {
      var c = this.checked; save(function (d) { d.settings.showPrices = c; }); toast("اتحفظ");
    };
  }

  /* ============ رسم الكل ============ */
  function render() {
    db = SCStore.get();
    $("#gBrand").textContent = db.settings.brand;
    $("#sBrand").textContent = db.settings.brand;
    var n = { nBooks: "bookings", nProcs: "procs", nPkgs: "packages", nRevs: "reviews", nFaq: "faq" };
    Object.keys(n).forEach(function (k) {
      var el = $("#" + k); if (el) el.textContent = eg((db[n[k]] || []).length); });

    paintHome();
    bookTable("#tBooks", db.bookings || []);

    table("#tCats", "cats", [{ k: "name", t: "اسم القسم" }]);
    table("#tProcs", "procs", [
      { k: "name", t: "الخدمة" },
      { k: "sub", t: "السطر الصغير" },
      { k: "cat", t: "القسم", type: "sel", w: "150px", opts: function () { return db.cats; } },
      { k: "price", t: "السعر", type: "num", w: "110px" },
      { k: "icon", t: "أيقونة", w: "100px" },
      { k: "tag", t: "شارة", w: "90px" },
      { k: "desc", t: "الوصف", type: "area" }
    ]);
    table("#tDays", "days", [
      { k: "name", t: "اليوم", w: "120px" },
      { k: "from", t: "من", w: "120px" },
      { k: "to", t: "لـ", w: "120px" },
      { k: "off", t: "إجازة", type: "chk", w: "70px" }
    ], { noDel: true });
    table("#tSlots", "slots", [{ k: "__self", t: "الساعة", type: "plain" }]);
    table("#tSteps", "steps", [
      { k: "n", t: "الرقم", w: "70px" }, { k: "t", t: "العنوان" }, { k: "d", t: "الشرح", type: "area" }
    ]);
    table("#tWhy", "why", [{ k: "t", t: "الميزة" }, { k: "d", t: "الشرح", type: "area" }]);
    table("#tStats", "stats", [{ k: "n", t: "الرقم", w: "140px" }, { k: "t", t: "الوصف" }]);
    table("#tRevs", "reviews", [
      { k: "n", t: "الاسم", w: "130px" }, { k: "t", t: "الرأي", type: "area" },
      { k: "s", t: "نجوم", type: "num", w: "80px" }
    ]);
    table("#tFaq", "faq", [{ k: "q", t: "السؤال" }, { k: "a", t: "الإجابة", type: "area" }]);
    if ($("#pkgList")) paintPkgs();
    if ($("#fearW")) paintFear();
    paintSettings();
  }

  var ADD = {
    addCat:  ["cats",     function () { return { id: uid("c"), name: "قسم جديد" }; }],
    addProc: ["procs",    function () { return { id: uid("p"), name: "خدمة جديدة", sub: "", cat: (db.cats[0] || {}).id, price: 0, icon: "tooth", tag: "", desc: "" }; }],
    addPkg:  ["packages", function () { return { id: uid("k"), name: "باقة جديدة", sub: "", price: 0, items: [] }; }],
    addSlot: ["slots",    function () { return "٣:٠٠ م"; }],
    addStep: ["steps",    function () { return { n: String((db.steps || []).length + 1), t: "خطوة", d: "" }; }],
    addWhy:  ["why",      function () { return { t: "ميزة جديدة", d: "" }; }],
    addStat: ["stats",    function () { return { n: "", t: "" }; }],
    addRev:  ["reviews",  function () { return { n: "", t: "", s: 5 }; }],
    addFaq:  ["faq",      function () { return { q: "سؤال جديد", a: "" }; }]
  };
  Object.keys(ADD).forEach(function (id) {
    var el = $("#" + id); if (!el) return;
    el.onclick = function () {
      var spec = ADD[id];
      save(function (d) { d[spec[0]].push(spec[1]()); });
      toast("اتضاف — نزّل تحت وعدّله");
    };
  });

  window.addEventListener("smilecare:change:full", function () {
    alert("مساحة التخزين اتملت. امسح حجوزات قديمة من تبويب الحجوزات.");
  });

  if (unlocked()) unlock();
})();
