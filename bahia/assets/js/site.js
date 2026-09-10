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

  /* ------------------------------ اللغة ------------------------------ */
  const LKEY = 'bahia_lang';
  let lang = 'ar';
  try { const v = localStorage.getItem(LKEY); if (v === 'ar' || v === 'en') lang = v; } catch (e) {}
  const t  = k => T[lang][k];                    // نص واجهة
  const tx = v => (v && typeof v === 'object') ? (v[lang] || v.ar) : v;   // حقل ثنائي اللغة
  const cur = () => tx(BRAND.currency);

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
    const active = $('#tabs .tab.is-on');
    const on = active ? active.dataset.cat : 'all';
    box.innerHTML = CATEGORIES.map(c =>
      `<button class="tab${c.id === on ? ' is-on' : ''}" data-cat="${c.id}" role="tab">${esc(tx(c.label))}</button>`
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
    ${p.badge ? `<span class="card__badge">${esc(tx(p.badge))}</span>` : ''}
    <img src="${esc(p.img)}" alt="${esc(tx(p.name))}" loading="lazy" decoding="async">
    <button class="card__add" data-add="${p.id}">${ico('plus')} ${esc(t('add'))}</button>
  </div>
  <div class="card__body">
    <span class="card__sub">${esc(lang === 'ar' ? p.name.en : p.name.ar)}</span>
    <h3 class="card__name">${esc(tx(p.name))}</h3>
    <p class="card__desc">${esc(tx(p.desc))}</p>
    <div class="card__foot">
      <span class="card__price"><span class="num">${money(p.price)}</span><small>${esc(cur())}</small></span>
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
  <h3>${esc(tx(p.title))}</h3>
  <p>${esc(tx(p.text))}</p>
</div>`).join('');
  }

  /* ------------------------------ السلة ------------------------------ */
  function renderCart() {
    const n = count(), sum = total();
    const badge = $('#cartCount');
    badge.textContent = n;
    badge.classList.toggle('is-on', n > 0);
    $('#cartSub').textContent = n ? n + ' ' + t('pieces') : t('cartEmptySub');

    const body = $('#cartBody'), foot = $('#cartFoot');
    if (!n) {
      body.innerHTML = `<div class="cart__empty">${ico('bag')}<p>${esc(t('cartEmpty'))}</p><p style="font-size:.85rem">${esc(t('cartEmptyHint'))}</p></div>`;
      foot.hidden = true;
      return;
    }

    body.innerHTML = Object.entries(cart).map(([id, q]) => {
      const p = byId(id);
      if (!p) return '';
      return `
<div class="li">
  <img src="${esc(p.img)}" alt="${esc(tx(p.name))}">
  <div>
    <div class="li__name">${esc(tx(p.name))}</div>
    <div class="li__unit"><span class="num">${money(p.price)}</span> ${esc(cur())} / ${esc(t('each'))}</div>
    <div class="li__row">
      <div class="qty">
        <button data-dec="${p.id}" aria-label="إنقاص الكمية">−</button>
        <span class="num">${q}</span>
        <button data-inc="${p.id}" aria-label="زيادة الكمية">+</button>
      </div>
      <span class="li__sum"><span class="num">${money(p.price * q)}</span> ${esc(cur())}</span>
    </div>
    <button class="li__del" data-del="${p.id}">${esc(t('remove'))}</button>
  </div>
</div>`;
    }).join('');

    foot.hidden = false;
    $('#cartTotal').textContent = money(sum);

    const ship = $('#ship'), left = BRAND.freeShipFrom - sum;
    if (!BRAND.freeShipFrom || left <= 0) {
      ship.className = 'ship is-free';
      ship.innerHTML = ico('check') + '<span>' + t('shipFree') + '</span>';
    } else {
      ship.className = 'ship';
      ship.innerHTML = ico('truck') + '<span>' + t('shipLeft')(money(left), esc(cur())) + '</span>';
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
    toast(t('addedToast'));
    if (btn) {
      btn.classList.add('is-added');
      btn.innerHTML = ico('check') + ' ' + t('added');
      setTimeout(() => {
        btn.classList.remove('is-added');
        btn.innerHTML = ico('plus') + ' ' + t('add');
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
    lines.push(t('orderHi'), '');
    let i = 1;
    for (const [id, q] of Object.entries(cart)) {
      const p = byId(id);
      if (!p) continue;
      lines.push(i++ + '. ' + tx(p.name));
      lines.push('   ' + q + ' × ' + money(p.price) + ' = ' + money(p.price * q) + ' ' + cur());
    }
    const sum = total();
    lines.push('', '— — — — —');
    lines.push(t('orderCount') + ': ' + count());
    lines.push(t('orderTotal') + ': ' + money(sum) + ' ' + cur());
    if (BRAND.freeShipFrom && sum >= BRAND.freeShipFrom) lines.push(t('orderShip') + ': ' + t('orderShipFree'));
    lines.push('', t('orderName'), t('orderCity'), t('orderAddr'));
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

  /* ------------------------------ تطبيق اللغة ------------------------------ */
  function applyLang() {
    const d = document.documentElement;
    d.setAttribute('lang', lang);
    d.setAttribute('dir', t('dir'));

    /* النصوص الثابتة */
    $$('[data-t]').forEach(el => {
      const v = t(el.dataset.t);
      if (typeof v !== 'string') return;
      if (el.hasAttribute('data-html')) el.innerHTML = v; else el.textContent = v;
    });

    /* روابط أقسام الفوتر */
    $$('[data-cat-label]').forEach(a => {
      const c = CATEGORIES.find(x => x.id === a.dataset.cat);
      if (c) a.textContent = tx(c.label);
    });

    /* تسميات الوصول والعملة وزر اللغة */
    $('#langTxt').textContent = t('other');
    $('#langBtn').setAttribute('aria-label', t('otherLabel'));
    $('#cartBtn').setAttribute('aria-label', t('cartAria'));
    $('#cartClose').setAttribute('aria-label', t('close'));
    $('#burger').setAttribute('aria-label', t('menu'));
    $('#cart').setAttribute('aria-label', t('cartAria'));
    $('#curLabel').textContent = cur();

    /* روابط واتساب */
    [['#ctaWa', 'ctaWa'], ['#waLink', 'askWa']].forEach(([sel, key]) => {
      const el = $(sel);
      if (!el) return;
      el.href = wa(t(key));
      el.target = '_blank';
      el.rel = 'noopener';
    });

    /* إعادة بناء كل ما يحمل نصاً */
    renderTabs();
    renderGrid(($('#tabs .tab.is-on') || {}).dataset ? $('#tabs .tab.is-on').dataset.cat : 'all');
    renderPerks();
    renderCart();
    reveal();
  }

  function toggleLang() {
    lang = lang === 'ar' ? 'en' : 'ar';
    try { localStorage.setItem(LKEY, lang); } catch (e) {}
    applyLang();
  }

  document.addEventListener('DOMContentLoaded', () => {
    $('#logo').innerHTML = LOGO;
    $('#logoFtr').innerHTML = LOGO;
    $('#year').textContent = new Date().getFullYear();
    $('#waShow').textContent = BRAND.whatsappShow;

    applyLang();
    wireNav();

    $('#langBtn').addEventListener('click', toggleLang);

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
