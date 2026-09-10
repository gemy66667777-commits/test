/* =============================================================
   شذى المدينة للعطورات — منطق الموقع
   ============================================================= */
(function () {
  'use strict';

  const $  = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.from((c || document).querySelectorAll(s));
  const esc = s => String(s).replace(/[&<>"]/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));
  const waLink = (msg, num) => 'https://wa.me/' + (num || BRAND.whatsapp) + '?text=' + encodeURIComponent(msg);

  /* ختم البراند — دائرة بخط كوفي، مستوحى من شعار المتجر */
  const STAMP = `
<svg viewBox="0 0 96 96" fill="none" role="img">
  <circle cx="48" cy="48" r="45" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="48" cy="48" r="38" stroke="currentColor" stroke-opacity=".38" stroke-width=".9" stroke-dasharray="1.6 5"/>
  <text x="48" y="38" text-anchor="middle" font-family="Almarai, sans-serif" font-size="10"
        letter-spacing="2.6" fill="currentColor" opacity=".72">SH</text>
  <path d="M30 44h36" stroke="currentColor" stroke-opacity=".45" stroke-width="1"/>
  <text x="48" y="68" text-anchor="middle" font-family="'Reem Kufi', sans-serif" font-size="21" fill="currentColor">شذى</text>
</svg>`;

  const ICONS = {
    rose:'<path d="M12 21c-4.4 0-7.5-2.9-7.5-7 0-3.4 2.6-5.6 4.6-7.4C10.6 5.3 11.6 4.2 12 3c.4 1.2 1.4 2.3 2.9 3.6 2 1.8 4.6 4 4.6 7.4 0 4.1-3.1 7-7.5 7Z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/><path d="M12 17.5c-2 0-3.4-1.3-3.4-3.2 0-1.6 1.2-2.6 2.1-3.4.6-.5 1.1-1 1.3-1.5.2.5.7 1 1.3 1.5.9.8 2.1 1.8 2.1 3.4 0 1.9-1.4 3.2-3.4 3.2Z" fill="currentColor" opacity=".45"/>',
    leaf:'<path d="M4.5 19.5C3 15 5.5 6.5 19.5 4.5c1 9.5-4.5 15.5-11 15.5-1.6 0-3-.2-4-.5Z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/><path d="M4.5 19.5C7 15.5 11 11 16 8.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" fill="none"/>',
    shop:'<path d="M4 9.5V19a1.5 1.5 0 0 0 1.5 1.5h13A1.5 1.5 0 0 0 20 19V9.5" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M3 9.5 4.8 4.5h14.4L21 9.5a3 3 0 0 1-6 0 3 3 0 0 1-6 0 3 3 0 0 1-6 0Z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/><path d="M9.8 20.5V14h4.4v6.5" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    chat:'<path d="M20 12.3c0 3.8-3.6 6.9-8 6.9-1 0-2-.2-2.9-.5L4 20.3l1.6-3.5A6.6 6.6 0 0 1 4 12.3c0-3.8 3.6-6.9 8-6.9s8 3.1 8 6.9Z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/>',
    whatsapp:'<path fill="currentColor" d="M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.48 1.34 5L2 22l5.2-1.36a9.9 9.9 0 0 0 4.84 1.24h.01c5.5 0 9.96-4.46 9.96-9.96C22.01 6.46 17.54 2 12.04 2Zm5.8 14.06c-.24.68-1.4 1.32-1.94 1.36-.5.05-.96.23-3.24-.68-2.74-1.08-4.46-3.88-4.6-4.06-.13-.18-1.1-1.46-1.1-2.78 0-1.32.7-1.97.94-2.24.25-.27.54-.34.72-.34h.52c.16 0 .4-.06.62.48.24.58.8 2 .87 2.14.07.14.12.3.02.48-.1.18-.15.3-.29.46-.14.16-.3.36-.43.48-.14.14-.29.29-.12.57.17.28.75 1.24 1.6 2 1.11.98 2.04 1.29 2.32 1.43.28.14.45.12.62-.07.17-.2.72-.83.91-1.12.19-.29.38-.24.64-.14.26.09 1.66.78 1.94.93.28.14.47.21.54.33.07.12.07.68-.17 1.36Z"/>',
    phone:'<path d="M6.5 3.5h3l1.5 4-2 1.4a11 11 0 0 0 5.1 5.1l1.4-2 4 1.5v3c0 1.1-.9 2-2 2A15.5 15.5 0 0 1 4.5 5.5c0-1.1.9-2 2-2Z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/>',
    instagram:'<rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.6" fill="none"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.6" fill="none"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor"/>',
    link:'<path d="M10 13.5a3.6 3.6 0 0 0 5.2.3l2.6-2.6a3.6 3.6 0 1 0-5.1-5.1l-1.5 1.5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/><path d="M14 10.5a3.6 3.6 0 0 0-5.2-.3l-2.6 2.6a3.6 3.6 0 1 0 5.1 5.1l1.5-1.5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/>',
    pin:'<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11Z" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="12" cy="10" r="2.6" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    check:'<circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.4" fill="none"/><path d="m8.4 12.2 2.4 2.4 4.8-5" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
  };
  const ico = n => '<svg viewBox="0 0 24 24" aria-hidden="true">' + (ICONS[n] || '') + '</svg>';

  const deptLabel = id => (CATEGORIES.find(c => c.id === id) || {}).label || '';

  /* ------------------------------ الأقسام ------------------------------ */
  function renderDepts() {
    const box = $('#depts');
    box.innerHTML = CATEGORIES.map((c, i) => {
      const n = c.id === 'all' ? PRODUCTS.length : PRODUCTS.filter(p => p.cat === c.id).length;
      return `<button class="${i === 0 ? 'is-active' : ''}" data-cat="${c.id}" role="tab">
                ${esc(c.label)}<span class="count">${n}</span>
              </button>`;
    }).join('');

    box.addEventListener('click', e => {
      const b = e.target.closest('button');
      if (!b) return;
      $$('button', box).forEach(x => x.classList.toggle('is-active', x === b));
      renderItems(b.dataset.cat);
    });
  }

  /* ------------------------------ المنتجات ------------------------------ */
  function renderItems(cat) {
    const list = (!cat || cat === 'all') ? PRODUCTS : PRODUCTS.filter(p => p.cat === cat);
    $('#grid').innerHTML = list.map(p => {
      const msg = 'السلام عليكم، أرغب في الاستفسار عن: ' + p.name +
                  (p.price ? ' — السعر المعروض ' + p.price + ' ' + BRAND.currency : ' — كم السعر والتوفّر؟');
      const price = p.price
        ? `<span class="item__price">${esc(p.price)}<small>${esc(BRAND.currency)}</small></span>`
        : `<span class="item__ask">السعر عبر واتساب</span>`;
      return `
<article class="item rev">
  <div class="item__media">
    ${p.badge ? `<span class="item__tag">${esc(p.badge)}</span>` : ''}
    <img src="${esc(p.img)}" alt="${esc(p.name)}" loading="lazy" decoding="async">
  </div>
  <div class="item__body">
    <span class="item__dept">${esc(deptLabel(p.cat))}</span>
    <h3 class="item__name">${esc(p.name)}</h3>
    <p class="item__desc">${esc(p.desc)}</p>
    <div class="item__foot">
      <span class="item__size">${esc(p.size)}</span>
      ${price}
    </div>
    <a class="item__order" href="${waLink(msg)}" target="_blank" rel="noopener">${ico('whatsapp')} اسأل عن السعر</a>
  </div>
</article>`;
    }).join('');
    observe();
  }

  /* ------------------------------ بقية الأقسام ------------------------------ */
  function renderAbout() {
    const rows = [
      ['العود والعنبر', 'تشكيلة عود وعنبر ومنتجات مستكا خيوس'],
      ['الورد الطائفي', 'من مزارع الطائف في موسمه'],
      ['العطور العالمية', 'ماركات أصلية للرجال والنساء'],
      ['العناية والمكياج', 'مستحضرات بشرة وشعر ومكياج مختارة']
    ];
    $('#aboutList').innerHTML = rows.map(([t, d]) =>
      `<li>${ico('check')}<span><b>${esc(t)}</b>${esc(d)}</span></li>`).join('');
  }

  function renderFeats() {
    $('#feats').innerHTML = FEATURES.map(f => `
<div class="feat rev">
  <span class="feat__ico">${ico(f.icon)}</span>
  <h3>${esc(f.title)}</h3>
  <p>${esc(f.text)}</p>
</div>`).join('');
  }

  function renderSays() {
    const star = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="m12 3.6 2.6 5.3 5.9.9-4.3 4.1 1 5.8-5.2-2.7-5.2 2.7 1-5.8L3.5 9.8l5.9-.9L12 3.6Z"/></svg>';
    $('#says').innerHTML = QUOTES.map(q => `
<figure class="say rev">
  <div class="say__stars">${star.repeat(5)}</div>
  <p>${esc(q.text)}</p>
  <figcaption class="say__by">
    <span class="say__av">${esc(q.name.trim().charAt(0))}</span>
    <span><b>${esc(q.name)}</b><span>${esc(q.role)}</span></span>
  </figcaption>
</figure>`).join('');
  }

  function renderLines() {
    const rows = [
      { show: BRAND.phoneDisplay,  note: 'واتساب — للاستفسار والطلب', href: waLink('السلام عليكم، أود الاستفسار عن منتجاتكم.', BRAND.whatsapp), go: 'محادثة واتساب ←', icon: 'whatsapp' },
      { show: BRAND.phone2Display, note: 'رقم إضافي للطلبات',        href: waLink('السلام عليكم، أود الاستفسار عن منتجاتكم.', BRAND.phone2),   go: 'محادثة واتساب ←', icon: 'whatsapp' },
      { show: BRAND.landlineShow,  note: 'هاتف المحل',                href: 'tel:+' + BRAND.landline, go: 'اتصال ←', icon: 'phone' },
      { show: BRAND.city,          note: BRAND.address,               href: 'https://linktr.ee/shathaalmadina', go: 'الموقع ←', icon: 'pin' }
    ];
    $('#lines').innerHTML = rows.map(r => `
<a class="line" href="${r.href}" target="_blank" rel="noopener">
  <span class="line__ico">${ico(r.icon)}</span>
  <span><b>${esc(r.show)}</b><span>${esc(r.note)}</span></span>
  <span class="line__go">${esc(r.go)}</span>
</a>`).join('');
  }

  function renderSocial() {
    $('#social').innerHTML = BRAND.social.map(s =>
      `<a href="${s.url}" target="_blank" rel="noopener" aria-label="${esc(s.label)}" title="${esc(s.label)}">${ico(s.icon)}</a>`
    ).join('');
  }

  /* ------------------------------ التفاعل ------------------------------ */
  let io;
  function observe() {
    const items = $$('.rev:not(.is-in):not(.is-pending)');
    if (!('IntersectionObserver' in window)) { items.forEach(i => i.classList.add('is-in')); return; }
    if (!io) {
      io = new IntersectionObserver(en => en.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      }), { rootMargin: '0px 0px -6% 0px', threshold: .06 });
    }
    /* ما يبدأ مخفياً إلا ما هو تحت الشاشة — الصفحة تظهر كاملة عند التحميل */
    items.forEach((el, i) => {
      if (el.getBoundingClientRect().top < window.innerHeight * .95) { el.classList.add('is-in'); return; }
      el.classList.add('is-pending');
      el.style.transitionDelay = Math.min(i % 6, 5) * 60 + 'ms';
      io.observe(el);
    });
  }

  function wireNav() {
    const header = $('#header'), nav = $('#nav'), burger = $('#burger');
    burger.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', e => {
      if (e.target.tagName === 'A') { nav.classList.remove('is-open'); burger.setAttribute('aria-expanded', 'false'); }
    });
    const links = $$('#nav a');
    const onScroll = () => {
      header.classList.toggle('is-stuck', window.scrollY > 8);
      let cur = '';
      $$('main section[id]').forEach(s => { if (window.scrollY >= s.offsetTop - 130) cur = s.id; });
      links.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + cur));
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  function wireWa() {
    $$('[data-wa]').forEach(el => {
      el.setAttribute('href', waLink(el.dataset.wa));
      el.setAttribute('target', '_blank');
      el.setAttribute('rel', 'noopener');
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    ['#stampHeader', '#stampHero', '#stampFooter'].forEach(s => { const el = $(s); if (el) el.innerHTML = STAMP; });
    $('#year').textContent = new Date().getFullYear();
    renderDepts();
    renderItems('all');
    renderAbout();
    renderFeats();
    renderSays();
    renderLines();
    renderSocial();
    wireWa();
    wireNav();
    observe();
  });
})();
