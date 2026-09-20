(function () {
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var db = EStore.get();
  var SK = "elaj.admin.v1";

  function eg(n) { return Number(n || 0).toLocaleString("ar-EG"); }
  function money(n) { return eg(n) + " " + (db.settings.currency || ""); }
  function uid(p) { return p + Math.random().toString(36).slice(2, 8); }
  function save(fn) { db = EStore.patch(fn); render(); }
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
    var ok = (u === db.settings.phone || u === db.settings.phone2 || u === "admin") && p === db.settings.adminPass;
    if (!ok) { $("#gErr").textContent = "الرقم أو كلمة السر غلط."; $("#gErr").classList.add("on"); return; }
    $("#gErr").classList.remove("on"); unlock();
  });
  $("#logout").onclick = function () { try { sessionStorage.removeItem(SK); } catch (e) {} location.reload(); };

  /* ============ التبويبات ============ */
  var TITLES = { home: "نظرة عامة", books: "الحجوزات", svcs: "الخدمات", clins: "العيادات",
    labs: "التحاليل والأشعة", pkgs: "الباقات", rooms: "الغرف والولادة", gal: "المعرض",
    revs: "آراء المرضى", faq: "الأسئلة", set: "الإعدادات" };
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
    EStore.reset(); db = EStore.get(); render(); toast("رجعت البيانات الأصلية");
  };

  /* ============ محرّر جداول عام ============ */
  /* cols: [{k:مفتاح, t:عنوان, type:text|num|area|img|sel|list, opts, w}] */
  function table(host, listKey, cols, opts) {
    opts = opts || {};
    var rows = db[listKey] || [];
    var html = "<table><thead><tr>" + cols.map(function (c) {
      return "<th" + (c.w ? ' style="width:' + c.w + '"' : "") + ">" + esc(c.t) + "</th>"; }).join("") +
      "<th style=\"width:46px\"></th></tr></thead><tbody>" +
      rows.map(function (r, i) {
        return "<tr data-i='" + i + "'>" + cols.map(function (c) {
          var v = r[c.k];
          if (c.type === "img") {
            return "<td><img class='thumb' src='" + esc(v || "") + "' alt='' onerror=\"this.style.visibility='hidden'\">" +
              "<input type='file' accept='image/*' data-f='" + esc(c.k) + "' style='margin-top:5px;font-size:.72rem'></td>";
          }
          if (c.type === "area") {
            return "<td><textarea data-k='" + esc(c.k) + "'>" + esc(v || "") + "</textarea></td>";
          }
          if (c.type === "list") {
            return "<td><textarea data-k='" + esc(c.k) + "' data-list='1' placeholder='كل سطر بند'>" +
              esc((v || []).join("\n")) + "</textarea></td>";
          }
          if (c.type === "sel") {
            return "<td><select data-k='" + esc(c.k) + "'>" + (c.opts() || []).map(function (o) {
              return "<option value='" + esc(o.id) + "'" + (o.id === v ? " selected" : "") + ">" +
                esc(o.name) + "</option>"; }).join("") + "</select></td>";
          }
          return "<td><input data-k='" + esc(c.k) + "'" + (c.type === "num" ? " type='number' min='0'" : "") +
            " value='" + esc(v == null ? "" : v) + "'></td>";
        }).join("") + "<td><button class='ib del' data-del='" + i + "' title='حذف'>✕</button></td></tr>";
      }).join("") + "</tbody></table>";
    $(host).innerHTML = rows.length ? html : "<p class='hint'>مفيش بنود — دوس على زرار الإضافة.</p>";

    $$(host + " [data-k]").forEach(function (el) {
      el.onchange = function () {
        var i = +el.closest("tr").dataset.i, k = el.dataset.k;
        var val = el.value;
        if (el.dataset.list) val = val.split("\n").map(function (x) { return x.trim(); }).filter(Boolean);
        else if (el.type === "number") val = Number(val) || 0;
        save(function (d) { d[listKey][i][k] = val; });
        toast("اتحفظ");
      };
    });
    $$(host + " [data-f]").forEach(function (el) {
      el.onchange = function () {
        var f = el.files && el.files[0]; if (!f) return;
        var i = +el.closest("tr").dataset.i, k = el.dataset.f;
        readImg(f, function (url) { save(function (d) { d[listKey][i][k] = url; }); toast("الصورة اتحفظت"); });
      };
    });
    $$(host + " [data-del]").forEach(function (b) {
      b.onclick = function () {
        if (!confirm("متأكد إنك عايز تمسح البند ده؟")) return;
        save(function (d) { d[listKey].splice(+b.dataset.del, 1); }); toast("اتمسح");
      };
    });
  }

  /* ضغط الصورة قبل التخزين عشان localStorage ما يتملاش */
  function readImg(file, cb) {
    var fr = new FileReader();
    fr.onload = function () {
      var im = new Image();
      im.onload = function () {
        var MAX = 1100, w = im.width, h = im.height;
        if (w > MAX) { h = Math.round(h * MAX / w); w = MAX; }
        var c = document.createElement("canvas"); c.width = w; c.height = h;
        c.getContext("2d").drawImage(im, 0, 0, w, h);
        cb(c.toDataURL("image/jpeg", .82));
      };
      im.onerror = function () { cb(fr.result); };
      im.src = fr.result;
    };
    fr.readAsDataURL(file);
  }

  /* ============ اللوحات ============ */
  function paintHome() {
    var bk = db.bookings || [];
    var today = new Date().toISOString().slice(0, 10);
    $("#kpis").innerHTML = [
      { n: bk.length, t: "إجمالي الحجوزات" },
      { n: bk.filter(function (b) { return b.date === today; }).length, t: "حجوزات النهاردة" },
      { n: (db.clinics || []).length, t: "عيادة" },
      { n: (db.labs || []).length, t: "تحليل وأشعة" },
      { n: (db.packages || []).length, t: "باقة عروض" },
      { n: (db.services || []).length, t: "خدمة طبية" }
    ].map(function (k) {
      return "<div class='kpi'><b>" + eg(k.n) + "</b><small>" + esc(k.t) + "</small></div>"; }).join("");
    bookTable("#homeBooks", bk.slice(0, 6));
  }

  function bookTable(host, rows) {
    if (!rows.length) { $(host).innerHTML = "<p class='hint'>لسه مفيش حجوزات.</p>"; return; }
    $(host).innerHTML = "<table><thead><tr><th>الاسم</th><th>الموبايل</th><th>العيادة</th>" +
      "<th>الميعاد</th><th>ملاحظات</th><th>الحالة</th><th></th></tr></thead><tbody>" +
      rows.map(function (b) {
        var idx = db.bookings.indexOf(b);
        return "<tr><td>" + esc(b.name) + "</td>" +
          "<td dir='ltr'><a href='tel:" + esc(b.phone) + "'>" + esc(b.phone) + "</a></td>" +
          "<td>" + esc(b.clinic) + "</td>" +
          "<td>" + esc(b.dateTxt || b.date) + " · " + esc(b.time) + "</td>" +
          "<td>" + esc(b.note || "—") + "</td>" +
          "<td><select data-st='" + idx + "'>" +
            ["جديد", "اتأكد", "اتلغى", "خلص"].map(function (s) {
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
    var labOpts = (db.labs || []).map(function (l) { return { id: l.id, name: l.name }; });
    $("#pkgList").innerHTML = (db.packages || []).map(function (p, i) {
      var was = (p.items || []).reduce(function (a, it) {
        var l = (db.labs || []).filter(function (x) { return x.id === it.id; })[0];
        return a + (l ? (Number(l.price) || 0) * (Number(it.q) || 1) : 0); }, 0);
      var save2 = was - (Number(p.price) || 0);
      var warn = Number(p.was) && Number(p.was) !== was
        ? "<div class='warn'>السعر اللي كاتبه يدوي (" + eg(p.was) + ") مختلف عن المحسوب (" + eg(was) + ").</div>" : "";
      return "<div class='card' data-p='" + i + "' style='background:#F8FBFF'>" + warn +
        "<div class='grid3'>" +
        "<div class='field'><label>اسم الباقة</label><input data-pk='name' value='" + esc(p.name || "") + "'></div>" +
        "<div class='field'><label>السعر بعد العرض</label><input data-pk='price' type='number' min='0' value='" + esc(p.price || 0) + "'></div>" +
        "<div class='field'><label>شارة (اختياري)</label><input data-pk='tag' value='" + esc(p.tag || "") + "'></div>" +
        "</div>" +
        "<div class='field'><label>وصف قصير</label><input data-pk='sub' value='" + esc(p.sub || "") + "'></div>" +
        "<div class='field'><label>التحاليل اللي في الباقة</label><div class='picklist' data-items>" +
          (p.items || []).map(function (it, j) {
            return "<div class='pickrow'><select data-it='" + j + "'>" + labOpts.map(function (o) {
              return "<option value='" + esc(o.id) + "'" + (o.id === it.id ? " selected" : "") + ">" +
                esc(o.name) + "</option>"; }).join("") + "</select>" +
              "<input type='number' min='1' value='" + (Number(it.q) || 1) + "' data-itq='" + j + "'>" +
              "<button class='ib del' data-itdel='" + j + "'>✕</button></div>";
          }).join("") + "</div>" +
          "<button class='btn xs' data-additem>+ تحليل</button></div>" +
        "<p class='hint'>السعر قبل العرض المحسوب: <b>" + money(was) + "</b> · التوفير: <b>" + money(save2) + "</b></p>" +
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
        var first = (db.labs[0] || {}).id; if (!first) return;
        save(function (d) { d.packages[i].items.push({ id: first, q: 1 }); });
      };
      $("[data-pdel]", box).onclick = function () {
        if (!confirm("تمسح الباقة دي؟")) return;
        save(function (d) { d.packages.splice(i, 1); }); toast("اتمسحت");
      };
    });
  }

  function paintSettings() {
    var s = db.settings;
    var F = [
      ["brandAr", "اسم المستشفى", "text"], ["tagline", "الشعار الجانبي", "text"],
      ["intro", "النبذة", "area"],
      ["phone", "رقم الواتساب/الموبايل", "text"], ["phone2", "رقم تاني", "text"],
      ["land", "الأرضي", "text"], ["email", "البريد", "text"],
      ["whats", "رقم الواتساب بكود الدولة", "text"],
      ["emergency", "مواعيد الطوارئ", "text"], ["clinicHours", "مواعيد العيادات", "text"],
      ["gamcaHours", "مواعيد فحص العمالة", "text"],
      ["addr", "العنوان", "area"], ["mapUrl", "لينك الخريطة", "text"],
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
    db = EStore.get();
    $("#gBrand").textContent = db.settings.brandAr;
    $("#sBrand").textContent = db.settings.brandAr;
    var n = { nBooks: "bookings", nSvcs: "services", nClins: "clinics", nLabs: "labs",
      nPkgs: "packages", nGal: "gallery", nRevs: "reviews", nFaq: "faq" };
    Object.keys(n).forEach(function (k) { $("#" + k).textContent = eg((db[n[k]] || []).length); });
    $("#nRooms").textContent = eg((db.rooms || []).length + (db.births || []).length);

    paintHome();
    bookTable("#tBooks", db.bookings || []);

    table("#tSvcs", "services", [
      { k: "img", t: "صورة", type: "img", w: "90px" },
      { k: "name", t: "الخدمة" },
      { k: "tag", t: "شارة", w: "110px" },
      { k: "desc", t: "الوصف", type: "area" },
      { k: "icon", t: "أيقونة", w: "110px" }
    ]);
    table("#tClins", "clinics", [{ k: "name", t: "العيادة" }, { k: "note", t: "التفاصيل" }]);
    table("#tCats", "labcats", [{ k: "name", t: "اسم القسم" }]);
    table("#tLabs", "labs", [
      { k: "name", t: "التحليل / الأشعة" },
      { k: "cat", t: "القسم", type: "sel", w: "170px", opts: function () { return db.labcats; } },
      { k: "price", t: "السعر", type: "num", w: "110px" }
    ]);
    table("#tRooms", "rooms", [
      { k: "img", t: "صورة", type: "img", w: "90px" },
      { k: "name", t: "الغرفة" },
      { k: "price", t: "السعر", type: "num", w: "110px" },
      { k: "per", t: "لكل", w: "90px" },
      { k: "tag", t: "شارة", w: "90px" },
      { k: "feat", t: "المميزات (سطر لكل بند)", type: "list" }
    ]);
    table("#tBirths", "births", [
      { k: "name", t: "البند" },
      { k: "price", t: "السعر", type: "num", w: "110px" },
      { k: "tag", t: "شارة", w: "90px" },
      { k: "feat", t: "المميزات (سطر لكل بند)", type: "list" }
    ]);
    table("#tGal", "gallery", [
      { k: "img", t: "صورة", type: "img", w: "90px" },
      { k: "cap", t: "الوصف" }
    ]);
    table("#tRevs", "reviews", [
      { k: "n", t: "الاسم", w: "150px" },
      { k: "t", t: "الرأي", type: "area" },
      { k: "s", t: "نجوم", type: "num", w: "80px" }
    ]);
    table("#tFaq", "faq", [{ k: "q", t: "السؤال" }, { k: "a", t: "الإجابة", type: "area" }]);
    paintPkgs();
    paintSettings();
  }

  /* أزرار الإضافة */
  var ADD = {
    addSvc:  ["services", function () { return { id: uid("s"), name: "خدمة جديدة", icon: "lab", img: "", tag: "", desc: "" }; }],
    addClin: ["clinics",  function () { return { id: uid("c"), name: "عيادة جديدة", note: "" }; }],
    addCat:  ["labcats",  function () { return { id: uid("g"), name: "قسم جديد" }; }],
    addLab:  ["labs",     function () { return { id: uid("l"), name: "تحليل جديد", cat: (db.labcats[0] || {}).id, price: 0 }; }],
    addRoom: ["rooms",    function () { return { id: uid("r"), name: "غرفة جديدة", price: 0, per: "اللّيلة", img: "", feat: [] }; }],
    addBirth:["births",   function () { return { id: uid("b"), name: "بند جديد", price: 0, feat: [] }; }],
    addGal:  ["gallery",  function () { return { img: "", cap: "" }; }],
    addRev:  ["reviews",  function () { return { n: "", t: "", s: 5 }; }],
    addFaq:  ["faq",      function () { return { q: "سؤال جديد", a: "" }; }],
    addPkg:  ["packages", function () { return { id: uid("p"), name: "باقة جديدة", sub: "", price: 0, items: [] }; }]
  };
  Object.keys(ADD).forEach(function (id) {
    var el = $("#" + id); if (!el) return;
    el.onclick = function () {
      var spec = ADD[id];
      save(function (d) { d[spec[0]].push(spec[1]()); });
      toast("اتضاف — نزّل تحت وعدّله");
    };
  });

  window.addEventListener("elaj:change:full", function () {
    alert("مساحة التخزين اتملت. امسح صور قديمة من المعرض أو استخدم صور أصغر.");
  });

  if (unlocked()) unlock();
})();
