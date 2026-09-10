/* =============================================================
   باهية | BAHIA — منطق المتجر والسلة
   ============================================================= */
(function () {
  'use strict';

  const $  = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.from((c || document).querySelectorAll(s));
  const esc = s => String(s).replace(/[&<>"]/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));
  const byId = id => PRODUCTS.find(p => p.id === id);
  const money = n => n.toLocaleString('en-US');

  const wa = msg => 'https://wa.me/' + BRAND.whatsapp + '?text=' + encodeURIComponent(msg);

  /* ------------------------------ الشعار ------------------------------ */
  const LOGO = `
<svg viewBox="0 0 252 58" style="direction:ltr" role="img" aria-label="باهية BAHIA">
  <path d="M229 7c14.5 14.5 14.5 27 0 43-14.5-16-14.5-28.5 0-43Z" fill="currentColor"/>
  <path d="M229 20c6.8 7.8 6.8 15.2 0 23-6.8-7.8-6.8-15.2 0-23Z" fill="#c9ac7c"/>
  <text x="206" y="30" text-anchor="end" font-family="'Playfair Display',Georgia,serif"
        font-size="26" font-weight="500" letter-spacing="8" fill="currentColor">BAHIA</text>
  <text x="199" y="50" text-anchor="end" font-family="'El Messiri',serif"
        font-size="17" fill="currentColor" opacity=".76">باهية</text>
</svg>`;

  const ICONS = {
    truck:'<rect x="2.5" y="6.5" width="11" height="9" rx="2" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M13.5 9.5h3.6l2.9 3v3h-6.5Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" fill="none"/><circle cx="7" cy="17.5" r="1.9" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="16.5" cy="17.5" r="1.9" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    shield:'<path d="M12 3l7 3v5.6c0 4.3-2.9 7.6-7 9.4-4.1-1.8-7-5.1-7-9.4V6l7-3Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" fill="none"/><path d="m9 12 2.2 2.2L15.5 10" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/>',
    gift:'<rect x="3.5" y="9" width="17" height="11.5" rx="2" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M2.5 9h19M12 9v11.5" stroke="currentColor" stroke-width="1.5"/><path d="M12 9c-1-3-2.5-4.5-4-4.5S5.5 6 7 9m5 0c1-3 2.5-4.5 4-4.5S18.5 6 17 9" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    chat:'<path d="M20 12.3c0 3.8-3.6 6.9-8 6.9-1 0-2-.2-2.9-.5L4 20.3l1.6-3.5A6.6 6.6 0 0 1 4 12.3c0-3.8 3.6-6.9 8-6.9s8 3.1 8 6.9Z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/>',
    bag:'<path d="M4 7h16l-1.3 12.1a2 2 0 0 1-2 1.9H7.3a2 2 0 0 1-2-1.9Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round" fill="none"/><path d="M8.6 7V5.9a3.4 3.4 0 0 1 6.8 0V7" stroke="currentColor" stroke-width="1.4" fill="none"/>',
    plus:'<path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>',
    check:'<path d="m5 13 4 4L19 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
  };
  const ico = n => '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">' + (ICONS[n] || '') + '</svg>';

  /* ------------------------------ حالة السلة ------------------------------ */
  const KEY = 'bahia_cart_v1';
  let cart = {};
  try { cart = JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { cart = {}; }

  const save  = () => { try { localStorage.setItem(KEY, JSON.stringify(cart)); } catch (e) {} };
  const count = () => Object.values(cart).reduce((a, b) => a + b, 0);
  const total = () => Object.entries(cart).reduce((sum, [id, q]) => {
    const p = byId(id); return p ? sum + p.price * q : sum;
  }, 0);

  /* ------------------------------ المنتجات ------------------------------ */
  function renderTabs() {
    const box = $('#tabs');
    box.innerHTML = CATEGORIES.map((c, i) =>
      `<button class="tab${i === 0 ? ' is-on' : ''}" data-cat="${c.id}" role="tab">${esc(c.label)}</button>`
    ).join('');
    box.addEventListener('click', e => {
      const b = e.target.closest('.tab');
      if (b) selectCat(b.dataset.cat);
    });
  }

  function selectCat(cat) {
    $$('#tabs .tab').forEach(t => t.classList.toggle('is-on', t.dataset.cat === cat));
    renderGrid(cat);
  }

  function renderGrid(cat) {
    const list = (!cat || cat === 'all') ? PRODUCTS : PRODUCTS.filter(p => p.cat === cat);
    $('#grid').innerHTML = list.map(p => `
<article class="card rev">
  <div class="card__shot">
    ${p.badge ? `<span class="card__badge">${esc(p.badge)}</span>` : ''}
    <img src="${esc(p.img)}" alt="${esc(p.name)}" loading="lazy" decoding="async">
    <button class="card__add" data-add="${p.id}">${ico('plus')} أضيفي للسلة</button>
  </div>
  <div class="card__body">
    <span class="card__sub">${esc(p.sub)}</span>
    <h3 class="card__name">${esc(p.name)}</h3>
    <p class="card__desc">${esc(p.desc)}</p>
    <div class="card__foot">
      <span class="card__price"><span class="num">${money(p.price)}</span><small>${esc(BRAND.currency)}</small></span>
      ${p.was ? `<span class="card__was num">${money(p.was)}</span>` : ''}
    </div>
  </div>
</article>`).join('');
    reveal();
  }

  function renderPerks() {
    $('#perks').innerHTML = PERKS.map(p => `
<div class="perk rev">
  <span class="perk__ic">${ico(p.icon)}</span>
  <h3>${esc(p.title)}</h3>
  <p>${esc(p.text)}</p>
</div>`).join('');
  }

  /* ------------------------------ السلة ------------------------------ */
  function renderCart() {
    const n = count(), sum = total();
    const badge = $('#cartCount');
    badge.textContent = n;
    badge.classList.toggle('is-on', n > 0);
    $('#cartSub').textContent = n ? n + ' قطعة في السلة' : 'لا توجد منتجات بعد';

    const body = $('#cartBody'), foot = $('#cartFoot');
    if (!n) {
      body.innerHTML = `<div class="cart__empty">${ico('bag')}<p>سلتك فارغة.</p><p style="font-size:.85rem">أضيفي منتجاتك المفضلة وابدئي الطلب.</p></div>`;
      foot.hidden = true;
      return;
    }

    body.innerHTML = Object.entries(cart).map(([id, q]) => {
      const p = byId(id);
      if (!p) return '';
      return `
<div class="li">
  <img src="${esc(p.img)}" alt="${esc(p.name)}">
  <div>
    <div class="li__name">${esc(p.name)}</div>
    <div class="li__unit"><span class="num">${money(p.price)}</span> ${esc(BRAND.currency)} للقطعة</div>
    <div class="li__row">
      <div class="qty">
        <button data-dec="${p.id}" aria-label="إنقاص الكمية">−</button>
        <span class="num">${q}</span>
        <button data-inc="${p.id}" aria-label="زيادة الكمية">+</button>
      </div>
      <span class="li__sum"><span class="num">${money(p.price * q)}</span> ${esc(BRAND.currency)}</span>
    </div>
    <button class="li__del" data-del="${p.id}">إزالة</button>
  </div>
</div>`;
    }).join('');

    foot.hidden = false;
    $('#cartTotal').textContent = money(sum);

    const ship = $('#ship'), left = BRAND.freeShipFrom - sum;
    if (!BRAND.freeShipFrom || left <= 0) {
      ship.className = 'ship is-free';
      ship.innerHTML = ico('check') + '<span>مبروك! الشحن مجاني على هذا الطلب.</span>';
    } else {
      ship.className = 'ship';
      ship.innerHTML = ico('truck') + `<span>أضيفي بـ <b class="num">${money(left)}</b> ${esc(BRAND.currency)} واحصلي على شحن مجاني.</span>`;
    }
  }

  let toastTimer;
  function toast(msg) {
    const t = $('#toast');
    t.innerHTML = ico('check') + '<span>' + esc(msg) + '</span>';
    t.classList.add('is-on');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => t.classList.remove('is-on'), 2400);
  }

  function add(id, btn) {
    cart[id] = (cart[id] || 0) + 1;
    save(); renderCart();
    toast('تمت الإضافة إلى السلة');
    if (btn) {
      btn.classList.add('is-added');
      btn.innerHTML = ico('check') + ' تمت الإضافة';
      setTimeout(() => {
        btn.classList.remove('is-added');
        btn.innerHTML = ico('plus') + ' أضيفي للسلة';
      }, 1400);
    }
  }

  function openCart(open) {
    $('#cart').classList.toggle('is-on', open);
    $('#scrim').classList.toggle('is-on', open);
    $('#cart').setAttribute('aria-hidden', String(!open));
    document.body.classList.toggle('is-locked', open);
    if (open) $('#cartClose').focus();
  }

  /* رسالة الطلب التي تُرسل إلى واتساب */
  function orderMessage() {
    const lines = [];
    lines.push('مرحباً ' + BRAND.ar + '، أرغب في تأكيد الطلب التالي:', '');
    let i = 1;
    for (const [id, q] of Object.entries(cart)) {
      const p = byId(id);
      if (!p) continue;
      lines.push(i++ + '. ' + p.name);
      lines.push('   ' + q + ' × ' + money(p.price) + ' = ' + money(p.price * q) + ' ' + BRAND.currency);
    }
    const sum = total();
    lines.push('', '— — — — —');
    lines.push('عدد القطع: ' + count());
    lines.push('الإجمالي: ' + money(sum) + ' ' + BRAND.currency);
    if (BRAND.freeShipFrom && sum >= BRAND.freeShipFrom) lines.push('الشحن: مجاني');
    lines.push('', 'الاسم:', 'المدينة:', 'العنوان:');
    return lines.join('\n');
  }

  function checkout() {
    if (!count()) return;
    window.open(wa(orderMessage()), '_blank', 'noopener');
  }

  /* ------------------------------ التفاعل ------------------------------ */
  let io;
  function reveal() {
    const items = $$('.rev:not(.is-in):not(.is-wait)');
    if (!('IntersectionObserver' in window)) { items.forEach(i => i.classList.add('is-in')); return; }
    if (!io) {
      io = new IntersectionObserver(en => en.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      }), { rootMargin: '0px 0px -6% 0px', threshold: .05 });
    }
    /* ما يبدأ مخفياً إلا ما هو تحت الشاشة، فالصفحة تظهر كاملة عند التحميل */
    items.forEach((el, i) => {
      if (el.getBoundingClientRect().top < window.innerHeight * .95) { el.classList.add('is-in'); return; }
      el.classList.add('is-wait');
      el.style.transitionDelay = Math.min(i % 8, 6) * 55 + 'ms';
      io.observe(el);
    });
  }

  function wireNav() {
    const hdr = $('#hdr'), nav = $('#nav'), burger = $('#burger');
    burger.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', e => {
      if (e.target.tagName === 'A') { nav.classList.remove('is-open'); burger.setAttribute('aria-expanded', 'false'); }
    });
    const links = $$('#nav a');
    const onScroll = () => {
      hdr.classList.toggle('is-stuck', window.scrollY > 8);
      let cur = '';
      $$('main section[id]').forEach(s => { if (window.scrollY >= s.offsetTop - 140) cur = s.id; });
      links.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + cur));
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  document.addEventListener('DOMContentLoaded', () => {
    $('#logo').innerHTML = LOGO;
    $('#logoFtr').innerHTML = LOGO;
    $('#year').textContent = new Date().getFullYear();
    $('#waShow').textContent = BRAND.whatsappShow;

    renderTabs();
    renderGrid('all');
    renderPerks();
    renderCart();
    wireNav();
    reveal();

    $$('[data-wa]').forEach(el => {
      el.setAttribute('href', wa(el.dataset.wa));
      el.setAttribute('target', '_blank');
      el.setAttribute('rel', 'noopener');
    });

    /* أزرار الإضافة داخل الشبكة */
    $('#grid').addEventListener('click', e => {
      const b = e.target.closest('[data-add]');
      if (b) add(b.dataset.add, b);
    });

    /* أزرار السلة */
    $('#cartBody').addEventListener('click', e => {
      const inc = e.target.closest('[data-inc]'), dec = e.target.closest('[data-dec]'), del = e.target.closest('[data-del]');
      if (inc) { cart[inc.dataset.inc]++; }
      else if (dec) { const id = dec.dataset.dec; cart[id]--; if (cart[id] <= 0) delete cart[id]; }
      else if (del) { delete cart[del.dataset.del]; }
      else return;
      save(); renderCart();
    });

    $('#cartBtn').addEventListener('click', () => openCart(true));
    $('#cartClose').addEventListener('click', () => openCart(false));
    $('#scrim').addEventListener('click', () => openCart(false));
    $('#checkout').addEventListener('click', checkout);
    document.addEventListener('keydown', e => { if (e.key === 'Escape') openCart(false); });

    /* روابط الأقسام في الفوتر */
    $$('.ftr__nav [data-cat]').forEach(a => a.addEventListener('click', () => selectCat(a.dataset.cat)));
  });
})();
