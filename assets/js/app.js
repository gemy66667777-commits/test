/* ريتشي — واجهة الموقع */
(function () {
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  const ar = (n) => Number(n).toLocaleString("ar-EG");
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  /* ---------- أيقونات ---------- */
  const sv = (d, extra) => `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
    stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" ${extra || ""}>${d}</svg>`;
  const ICON = {
    hall:   sv('<path d="M3 21h18M5 21V8l7-5 7 5v13"/><path d="M9 21v-6h6v6"/>'),
    flower: sv('<circle cx="12" cy="9" r="2.6"/><path d="M12 6.4C12 4 10.5 2.6 9 2.6S6.4 4 7.6 6.4c1 2 2.4 2.6 4.4 2.6"/><path d="M12 6.4C12 4 13.5 2.6 15 2.6S17.6 4 16.4 6.4c-1 2-2.4 2.6-4.4 2.6"/><path d="M9.4 10.4C7.3 9.2 5.4 9.7 4.7 11s.4 3 3 2.9c2.2-.1 3.4-1.1 4.3-2.8"/><path d="M14.6 10.4c2.1-1.2 4-.7 4.7.6s-.4 3-3 2.9c-2.2-.1-3.4-1.1-4.3-2.8"/><path d="M12 11.6V21"/>'),
    coffee: sv('<path d="M4 8h13v6a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5V8z"/><path d="M17 9h1.8a2.7 2.7 0 0 1 0 5.4H17"/><path d="M7 4.5V3M10.5 4.5V3M14 4.5V3"/>'),
    camera: sv('<path d="M3 8.5A2.5 2.5 0 0 1 5.5 6h1.7l1.2-2h6.2l1.2 2h1.7A2.5 2.5 0 0 1 20 8.5v9A2.5 2.5 0 0 1 17.5 20h-11A2.5 2.5 0 0 1 4 17.5z"/><circle cx="11.8" cy="12.6" r="3.6"/>'),
    music:  sv('<path d="M9 18V5.5l10-2V16"/><circle cx="6.5" cy="18" r="2.6"/><circle cx="16.5" cy="16" r="2.6"/>'),
    light:  sv('<path d="M9 17h6M10 21h4"/><path d="M12 2a6.4 6.4 0 0 0-3.6 11.7c.5.4.8 1 .8 1.6V17h5.6v-1.7c0-.6.3-1.2.8-1.6A6.4 6.4 0 0 0 12 2z"/>'),
    ring:   sv('<circle cx="12" cy="14.5" r="5.5"/><path d="m8.8 9.6 1.4-4.1h3.6l1.4 4.1"/><path d="m10.2 5.5 1.8 2.2 1.8-2.2"/>'),
    star:   sv('<path d="m12 3.2 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17.2l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" fill="currentColor" stroke="none"/>'),
    check:  sv('<path d="m4.5 12.5 5 5 10-11"/>'),
    phone:  sv('<path d="M6.6 3.5h3l1.5 3.8-2 1.4a12 12 0 0 0 6.2 6.2l1.4-2 3.8 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.6 5.7a2 2 0 0 1 2-2.2z"/>'),
    pin:    sv('<path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11z"/><circle cx="12" cy="10" r="2.7"/>'),
    clock:  sv('<circle cx="12" cy="12" r="9"/><path d="M12 7v5.3l3.3 2"/>'),
    zoom:   sv('<circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.4-4.4M11 8.6v4.8M8.6 11h4.8"/>'),
    x:      sv('<path d="m6 6 12 12M18 6 6 18"/>'),
    prev:   sv('<path d="m14.5 5-7 7 7 7"/>'),
    next:   sv('<path d="m9.5 5 7 7-7 7"/>'),
    up:     sv('<path d="M12 19V5M5.5 11.5 12 5l6.5 6.5"/>'),
    wa:     sv('<path d="M20.5 11.6a8.4 8.4 0 0 1-12.4 7.4L3.5 20.5l1.6-4.5A8.4 8.4 0 1 1 20.5 11.6z"/><path d="M9 9.2c.3-.8.6-.8 1-.8h.6c.2 0 .4 0 .6.5l.7 1.7c0 .2 0 .3-.1.5l-.4.5c-.2.2-.3.3-.1.6a7 7 0 0 0 3.1 2.6c.3.1.5.1.7-.1l.6-.7c.2-.2.3-.2.6-.1l1.7.8c.3.1.4.2.4.4a2 2 0 0 1-1.3 1.7c-.5.2-1.2.2-3.4-.7a9.6 9.6 0 0 1-4.3-4c-.5-.9-.7-1.7-.7-2.3 0-.3.1-.6.3-.9z"/>')
  };
  $$("[data-icon]").forEach((el) => (el.innerHTML = ICON[el.dataset.icon] || ""));

  const S = Store;

  /* ---------- الإعدادات في كل مكان ---------- */
  function paintSettings() {
    const s = S.s;
    $$("[data-s]").forEach((el) => { if (s[el.dataset.s] != null) el.textContent = s[el.dataset.s]; });
    document.title = `${s.brand} | ${s.tagline} — تنظيم وتجهيز الأفراح والمناسبات`;

    $("#heroTags").innerHTML = S.data.services.map((x) => `<span>${esc(x.name)}</span>`).join("");

    $("#ftrPhones").innerHTML =
      s.phones.map((p) => `<li><a href="tel:${esc(p)}" dir="ltr">${esc(p)}</a></li>`).join("") +
      `<li><a href="#book">طلب معاينة</a></li>`;

    const wa = $("#wa");
    wa.href = `https://wa.me/${String(s.whatsapp).replace(/\D/g, "")}?text=` +
      encodeURIComponent(`السلام عليكم، حابب أستفسر عن تجهيز مناسبة مع ${s.brand} 🌿`);
    wa.innerHTML = ICON.wa;

    $("#conGrid").innerHTML = `
      <div class="con"><span class="ic">${ICON.phone}</span><h3>للتواصل والحجز</h3>
        ${s.phones.map((p) => `<a href="tel:${esc(p)}" dir="ltr">${esc(p)}</a>`).join("")}</div>
      <div class="con"><span class="ic">${ICON.pin}</span><h3>العنوان</h3>
        <p>${esc(s.address)}</p>
        <a href="https://www.google.com/maps/search/${encodeURIComponent(s.address)}" target="_blank" rel="noopener">افتح على الخريطة</a></div>
      <div class="con"><span class="ic">${ICON.clock}</span><h3>مواعيد العمل</h3><p>${esc(s.hours)}</p>
        <p>المعاينة بميعاد مسبق</p></div>
      <div class="con"><span class="ic">${ICON.wa}</span><h3>واتساب</h3>
        <p>أسرع طريقة للرد</p><a href="${wa.href}" target="_blank" rel="noopener">ابعتلنا رسالة</a></div>`;
  }

  /* ---------- الخدمات ---------- */
  function paintServices() {
    $("#svcGrid").innerHTML = S.data.services.map((x) => `
      <article class="svc rv"><span class="ic">${ICON[x.icon] || ICON.star}</span>
        <h3>${esc(x.name)}</h3><p>${esc(x.desc)}</p></article>`).join("");
  }

  /* ---------- الباقات ---------- */
  function paintPackages() {
    $("#pkgGrid").innerHTML = S.data.packages.map((p) => `
      <article class="pkg rv${p.badge ? " hot" : ""}">
        ${p.badge ? `<span class="tag">${esc(p.badge)}</span>` : ""}
        <h3>${esc(p.name)}</h3>
        <div class="sub">${esc(p.sub)}</div>
        <p class="desc">${esc(p.desc)}</p>
        <div class="price">${esc(S.priceText(p.price))}<small>${esc(p.guests || "")}</small></div>
        <ul>${(p.features || []).map((f) => `<li>${ICON.check}<span>${esc(f)}</span></li>`).join("")}</ul>
        <button class="btn ${p.badge ? "" : "ghost"}" data-pick="${esc(p.name)}">اطلب الباقة</button>
      </article>`).join("");

    const sel = $("#bPkg");
    sel.innerHTML = `<option value="">مش محدد / حابب أستشير</option>` +
      S.data.packages.map((p) => `<option>${esc(p.name)}</option>`).join("");

    $$("[data-pick]").forEach((b) => b.addEventListener("click", () => {
      sel.value = b.dataset.pick;
      $("#book").scrollIntoView({ behavior: "smooth" });
      setTimeout(() => $("#bName").focus({ preventScroll: true }), 600);
    }));
  }

  /* ---------- المعرض ---------- */
  let view = [];
  function paintGallery(cat) {
    const cats = ["الكل", ...S.cats()];
    const active = cat && cats.includes(cat) ? cat : "الكل";
    $("#filters").innerHTML = cats.map((c) =>
      `<button data-cat="${esc(c)}" class="${c === active ? "on" : ""}">${esc(c)}</button>`).join("");

    view = active === "الكل" ? S.data.items : S.data.items.filter((i) => i.cat === active);

    $("#galGrid").innerHTML = view.length ? view.map((it, i) => `
      <article class="card" data-i="${i}" style="animation-delay:${Math.min(i, 11) * 45}ms">
        <div class="ph">
          <span class="cat">${esc(it.cat)}</span>
          <img src="${esc(S.thumbFor(it))}" alt="${esc(it.name)}" loading="lazy" decoding="async">
          <span class="zoom">${ICON.zoom}</span>
        </div>
        <div class="meta">
          <h3>${esc(it.name)}</h3>
          <p>${esc(it.desc || "")}</p>
          <div class="price"><b>${esc(S.priceText(it.price))}</b><span>شامل التنفيذ والتركيب</span></div>
        </div>
      </article>`).join("") : `<p class="empty">مفيش أعمال في القسم ده لسه.</p>`;

    $$("#filters button").forEach((b) =>
      b.addEventListener("click", () => paintGallery(b.dataset.cat)));
    $$("#galGrid .card").forEach((c) =>
      c.addEventListener("click", () => openLB(+c.dataset.i)));
    reveal();
  }

  /* ---------- لايت بوكس ---------- */
  let lbi = 0;
  const lb = $("#lb");
  $("#lbX").innerHTML = ICON.x;
  /* في RTL: السابق سهمه لليمين والتالي لليسار */
  $("#lbP").innerHTML = ICON.next; $("#lbNx").innerHTML = ICON.prev;

  function openLB(i) { lbi = i; showLB(); lb.classList.add("on"); document.body.style.overflow = "hidden"; }
  function closeLB() { lb.classList.remove("on"); document.body.style.overflow = ""; }
  function stepLB(d) { lbi = (lbi + d + view.length) % view.length; showLB(); }
  function showLB() {
    const it = view[lbi]; if (!it) return;
    const img = $("#lbImg");
    img.style.animation = "none"; void img.offsetWidth; img.style.animation = "";
    img.src = S.imageFor(it); img.alt = it.name;
    $("#lbT").textContent = it.name;
    $("#lbD").textContent = it.desc || "";
    $("#lbPr").textContent = S.priceText(it.price);
    $("#lbN").textContent = `${ar(lbi + 1)} / ${ar(view.length)}`;
  }
  $("#lbX").onclick = closeLB;
  $("#lbP").onclick = () => stepLB(-1);
  $("#lbNx").onclick = () => stepLB(1);
  lb.addEventListener("click", (e) => { if (e.target === lb || e.target.classList.contains("lb-body")) closeLB(); });
  document.addEventListener("keydown", (e) => {
    if (!lb.classList.contains("on")) return;
    if (e.key === "Escape") closeLB();
    if (e.key === "ArrowLeft") stepLB(1);
    if (e.key === "ArrowRight") stepLB(-1);
  });
  let tx = 0;
  lb.addEventListener("touchstart", (e) => (tx = e.changedTouches[0].clientX), { passive: true });
  lb.addEventListener("touchend", (e) => {
    const d = e.changedTouches[0].clientX - tx;
    if (Math.abs(d) > 55) stepLB(d > 0 ? -1 : 1);
  }, { passive: true });

  /* ---------- آراء ---------- */
  function paintSays() {
    $("#sayGrid").innerHTML = S.data.testimonials.map((t) => `
      <article class="say rv">
        <div class="stars">★★★★★</div>
        <p>${esc(t.text)}</p>
        <div class="who"><span class="av">${esc(t.name.trim()[0] || "ر")}</span>
          <span><b>${esc(t.name)}</b><small>${esc(t.event)}</small></span></div>
      </article>`).join("");
  }

  /* ---------- الحجز ---------- */
  $("#bookForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const el = e.target.elements;
    const name = el.name.value.trim();
    const phone = el.phone.value.trim();
    const ok = $("#bookOk");
    if (name.length < 3 || phone.replace(/\D/g, "").length < 10) {
      ok.textContent = "اكتب اسمك ورقم موبايل صحيح عشان نقدر نرجعلك.";
      ok.classList.add("on"); return;
    }
    S.addBooking({
      name, phone, type: el.type.value, date: el.date.value,
      guests: el.guests.value, pkg: el.pkg.value, note: el.note.value.trim()
    });
    ok.innerHTML = `تمام يا ${esc(name.split(" ")[0])} — وصلنا طلبك ✦ هنكلمك على <b dir="ltr">${esc(phone)}</b> خلال ٢٤ ساعة.`;
    ok.classList.add("on");
    e.target.reset();
    ok.scrollIntoView({ behavior: "smooth", block: "center" });
  });

  /* ---------- الهيدر والقائمة ---------- */
  const hdr = $("#hdr"), up = $("#up");
  up.innerHTML = ICON.up;
  up.onclick = () => window.scrollTo({ top: 0, behavior: "smooth" });
  const onScroll = () => {
    hdr.classList.toggle("on", scrollY > 30);
    up.classList.toggle("on", scrollY > 600);
    let cur = "";
    $$("main section[id]").forEach((s) => { if (scrollY >= s.offsetTop - 140) cur = s.id; });
    $$("#nav a[href^='#']").forEach((a) => a.classList.toggle("active", a.getAttribute("href") === "#" + cur));
  };
  addEventListener("scroll", onScroll, { passive: true }); onScroll();

  const burger = $("#burger");
  const closeMenu = () => { document.body.classList.remove("menu"); burger.setAttribute("aria-expanded", "false"); };
  burger.onclick = () => {
    const open = document.body.classList.toggle("menu");
    burger.setAttribute("aria-expanded", String(open));
  };
  $$("#nav a").forEach((a) => a.addEventListener("click", closeMenu));
  $("[data-close-menu]").onclick = closeMenu;

  /* ---------- ظهور تدريجي + عدادات ---------- */
  const io = "IntersectionObserver" in window
    ? new IntersectionObserver((es) => es.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.classList.add("in");
        io.unobserve(e.target);
        $$("[data-count]", e.target).forEach(count);
      }), { threshold: .12, rootMargin: "0px 0px -40px" })
    : null;
  function reveal() {
    $$(".rv:not(.in)").forEach((el, i) => {
      el.style.transitionDelay = Math.min(i, 6) * 70 + "ms";
      io ? io.observe(el) : el.classList.add("in");
    });
  }
  function count(el) {
    const to = +el.dataset.count, t0 = performance.now(), dur = 1500;
    (function tick(t) {
      const p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
      el.textContent = ar(Math.round(to * e)) + (p === 1 ? "+" : "");
      if (p < 1) requestAnimationFrame(tick);
    })(t0);
  }

  /* ---------- إقلاع ---------- */
  function render() { paintSettings(); paintServices(); paintPackages(); paintSays(); paintGallery(); reveal(); }
  document.addEventListener("richy:change", render);
  addEventListener("storage", (e) => { if (e.key === "richy.v1") location.reload(); });
  $("#yr").textContent = ar(new Date().getFullYear());
  render();
})();
