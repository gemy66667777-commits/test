/* =============================================================
   الروقي للعطور — منطق الموقع والرسومات
   ============================================================= */
(function () {
  'use strict';

  const $  = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.from((c || document).querySelectorAll(s));
  const esc = s => String(s).replace(/[&<>"]/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));

  const waLink = (msg, num) =>
    'https://wa.me/' + (num || BRAND.whatsapp) + '?text=' + encodeURIComponent(msg);

  /* ============================================================
     1) مكتبة الرسومات (SVG) — بديل احترافي للصور
     ============================================================ */
  const frame = (id, tone, body) => `
<svg viewBox="0 0 400 400" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="bg${id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fbf9f5"/><stop offset="1" stop-color="#ece6d9"/>
    </linearGradient>
    <linearGradient id="ob${id}" x1=".1" y1="0" x2=".9" y2="1">
      <stop offset="0" stop-color="${tone[0]}"/><stop offset="1" stop-color="${tone[1]}"/>
    </linearGradient>
    <linearGradient id="gd${id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#eddcae"/><stop offset=".45" stop-color="#c2a15a"/><stop offset="1" stop-color="#8d7135"/>
    </linearGradient>
    <radialGradient id="gl${id}" cx=".5" cy=".4" r=".62">
      <stop offset="0" stop-color="#c2a15a" stop-opacity=".26"/><stop offset="1" stop-color="#c2a15a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="400" height="400" fill="url(#bg${id})"/>
  <circle cx="200" cy="172" r="134" fill="url(#gl${id})"/>
  <circle cx="200" cy="172" r="120" fill="none" stroke="#c2a15a" stroke-opacity=".3" stroke-width="1.2" stroke-dasharray="1.5 9" stroke-linecap="round"/>
  <ellipse cx="200" cy="334" rx="104" ry="15" fill="#16241d" opacity=".10"/>
  ${body}
</svg>`;

  const mono = (x, y, s, fill) =>
    `<text x="${x}" y="${y}" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-size="${s}" fill="${fill}">R</text>`;

  const ART = {
    /* برطمان المعمول */
    jar: id => `
      <rect x="140" y="198" width="120" height="122" rx="18" fill="url(#ob${id})"/>
      <rect x="140" y="198" width="32" height="122" rx="16" fill="#fff" opacity=".14"/>
      <rect x="130" y="164" width="140" height="42" rx="14" fill="url(#gd${id})"/>
      <rect x="130" y="164" width="140" height="11" rx="5" fill="#fff" opacity=".3"/>
      <rect x="160" y="234" width="80" height="56" rx="10" fill="#fdfbf6" opacity=".92"/>
      ${mono(200, 272, 30, '#9a7c3c')}
      <rect x="172" y="243" width="56" height="1.4" fill="#c2a15a" opacity=".6"/>`,

    /* قارورة دهن العود */
    dropper: id => `
      <rect x="164" y="202" width="72" height="116" rx="20" fill="url(#ob${id})"/>
      <rect x="164" y="202" width="22" height="116" rx="11" fill="#fff" opacity=".17"/>
      <rect x="184" y="170" width="32" height="36" fill="${'url(#ob' + id + ')'}"/>
      <rect x="176" y="106" width="48" height="68" rx="12" fill="url(#gd${id})"/>
      <rect x="176" y="140" width="48" height="7" fill="#fff" opacity=".28"/>
      <circle cx="200" cy="102" r="11" fill="url(#gd${id})"/>
      <rect x="176" y="256" width="48" height="40" rx="8" fill="#fdfbf6" opacity=".9"/>
      ${mono(200, 285, 22, '#9a7c3c')}`,

    /* قطع العود / البخور */
    chips: (id, tone) => `
      <g>
        <rect x="146" y="284" width="130" height="28" rx="13" fill="${tone[1]}" opacity=".85" transform="rotate(4 211 298)"/>
        <rect x="110" y="250" width="122" height="34" rx="15" fill="url(#ob${id})" transform="rotate(-9 171 267)"/>
        <rect x="178" y="238" width="112" height="30" rx="14" fill="url(#ob${id})" opacity=".92" transform="rotate(8 234 253)"/>
        <rect x="136" y="210" width="96" height="27" rx="13" fill="${tone[1]}" opacity=".7" transform="rotate(-17 184 224)"/>
        <rect x="196" y="192" width="80" height="24" rx="11" fill="url(#ob${id})" opacity=".85" transform="rotate(15 236 204)"/>
        <rect x="164" y="168" width="62" height="20" rx="9" fill="${tone[1]}" opacity=".6" transform="rotate(-6 195 178)"/>
      </g>`,

    /* المبخرة */
    burner: id => `
      <path d="M148 320h104l-16-64h-72Z" fill="url(#ob${id})"/>
      <rect x="140" y="238" width="120" height="26" rx="11" fill="url(#gd${id})"/>
      <path d="M164 238l12-44h48l12 44Z" fill="url(#ob${id})" opacity=".95"/>
      <rect x="160" y="182" width="80" height="15" rx="7" fill="url(#gd${id})"/>
      <path d="M200 176c-18-18 18-28 0-46s16-26 6-38" fill="none" stroke="#c2a15a" stroke-opacity=".55" stroke-width="3.2" stroke-linecap="round"/>
      <path d="M232 178c-13-14 13-21 0-35" fill="none" stroke="#c2a15a" stroke-opacity=".32" stroke-width="2.6" stroke-linecap="round"/>
      <path d="M168 180c-11-12 11-18 0-30" fill="none" stroke="#c2a15a" stroke-opacity=".28" stroke-width="2.4" stroke-linecap="round"/>
      <rect x="176" y="286" width="48" height="1.6" fill="#fff" opacity=".22"/>`,

    /* زجاجة العطر */
    flacon: id => `
      <path d="M150 216c0-15 11-26 26-26h48c15 0 26 11 26 26v76c0 16-13 28-29 28h-42c-16 0-29-12-29-28Z" fill="url(#ob${id})"/>
      <rect x="158" y="206" width="20" height="112" rx="10" fill="#fff" opacity=".16"/>
      <rect x="186" y="162" width="28" height="34" fill="url(#ob${id})"/>
      <rect x="174" y="128" width="52" height="38" rx="9" fill="url(#gd${id})"/>
      <rect x="182" y="116" width="36" height="14" rx="6" fill="url(#gd${id})"/>
      <rect x="172" y="240" width="56" height="46" rx="9" fill="#fdfbf6" opacity=".9"/>
      ${mono(200, 274, 26, '#9a7c3c')}`,

    /* المسك */
    pearls: id => `
      <rect x="146" y="216" width="108" height="98" rx="22" fill="url(#ob${id})"/>
      <rect x="146" y="216" width="30" height="98" rx="15" fill="#fff" opacity=".4"/>
      <rect x="138" y="186" width="124" height="36" rx="13" fill="url(#gd${id})"/>
      <rect x="138" y="186" width="124" height="10" rx="5" fill="#fff" opacity=".3"/>
      <circle cx="286" cy="300" r="17" fill="#f6efe2" stroke="#c2a15a" stroke-opacity=".35"/>
      <circle cx="312" cy="318" r="12" fill="#f0e6d4" stroke="#c2a15a" stroke-opacity=".3"/>
      <circle cx="106" cy="310" r="14" fill="#f6efe2" stroke="#c2a15a" stroke-opacity=".3"/>
      ${mono(200, 282, 26, '#9a7c3c')}`,

    /* بوكس الهدية */
    box: id => `
      <rect x="116" y="222" width="168" height="96" rx="12" fill="url(#ob${id})"/>
      <rect x="188" y="222" width="24" height="96" fill="url(#gd${id})" opacity=".92"/>
      <rect x="104" y="180" width="192" height="48" rx="12" fill="${'url(#ob' + id + ')'}"/>
      <rect x="104" y="180" width="192" height="10" rx="5" fill="#fff" opacity=".14"/>
      <rect x="188" y="180" width="24" height="48" fill="url(#gd${id})"/>
      <circle cx="200" cy="150" r="26" fill="none" stroke="url(#gd${id})" stroke-width="2.4"/>
      ${mono(200, 160, 26, '#c2a15a')}
      <path d="M200 176c-14-8-34-6-34 4h68c0-10-20-12-34-4Z" fill="url(#gd${id})" opacity=".9"/>`,

    /* التوزيعات */
    gift: id => `
      <rect x="106" y="242" width="86" height="76" rx="11" fill="url(#ob${id})"/>
      <rect x="106" y="242" width="86" height="12" rx="6" fill="url(#gd${id})"/>
      <path d="M212 318V214c0-8 6-14 14-14h48c8 0 14 6 14 14v104Z" fill="url(#ob${id})" opacity=".95"/>
      <rect x="212" y="236" width="76" height="14" fill="url(#gd${id})" opacity=".9"/>
      <path d="M232 200c0-14 8-24 18-24s18 10 18 24" fill="none" stroke="url(#gd${id})" stroke-width="3.4" stroke-linecap="round"/>
      <rect x="176" y="272" width="58" height="46" rx="10" fill="${'url(#ob' + id + ')'}" opacity=".8"/>
      <rect x="176" y="272" width="58" height="10" rx="5" fill="url(#gd${id})" opacity=".85"/>
      ${mono(149, 292, 24, '#c2a15a')}`
  };

  const artFor = (p) => frame(p.id, p.tone, (ART[p.art] || ART.jar)(p.id, p.tone));

  /* شعار الروقي */
  const MARK = `
<svg viewBox="0 0 48 48" fill="none">
  <circle cx="24" cy="24" r="21" stroke="currentColor" stroke-width="1.3"/>
  <circle cx="24" cy="24" r="17" stroke="currentColor" stroke-opacity=".45" stroke-width=".9" stroke-dasharray="1.4 4.5"/>
  <text x="24" y="31.5" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-size="20" fill="currentColor">R</text>
</svg>`;

  /* أيقونات */
  const ICONS = {
    shield:'<path d="M12 3l7 3v5.6c0 4.3-2.9 7.6-7 9.4-4.1-1.8-7-5.1-7-9.4V6l7-3Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" fill="none"/><path d="m9 12 2.2 2.2L15.5 10" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/>',
    box:'<path d="M3 8.5 12 3l9 5.5v7L12 21l-9-5.5v-7Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" fill="none"/><path d="M12 12v9M3 8.5 12 12l9-3.5" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    truck:'<rect x="2.5" y="6.5" width="11" height="9" rx="2" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M13.5 9.5h3.6l2.9 3v3h-6.5Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" fill="none"/><circle cx="7" cy="17.5" r="1.9" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="16.5" cy="17.5" r="1.9" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    star:'<path d="m12 3.6 2.6 5.3 5.9.9-4.3 4.1 1 5.8-5.2-2.7-5.2 2.7 1-5.8L3.5 9.8l5.9-.9L12 3.6Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" fill="none"/>',
    camera:'<rect x="3" y="7" width="18" height="13" rx="3" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="12" cy="13.5" r="3.4" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M8.5 7l1.3-2.4h4.4L15.5 7" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    chat:'<path d="M20 12.5c0 3.9-3.6 7-8 7-1 0-2-.2-2.9-.5L4 20.5l1.6-3.6A6.7 6.7 0 0 1 4 12.5c0-3.9 3.6-7 8-7s8 3.1 8 7Z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/>',
    flame:'<path d="M12 3c3.4 4 5.5 6.3 5.5 9.5a5.5 5.5 0 1 1-11 0C6.5 9.3 8.6 7 12 3Z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/><path d="M12 11.5c1.6 2 2.4 2.9 2.4 4.2a2.4 2.4 0 1 1-4.8 0c0-1.3.8-2.2 2.4-4.2Z" fill="currentColor" opacity=".55"/>',
    gift:'<rect x="3.5" y="9" width="17" height="11.5" rx="2" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M2.5 9h19M12 9v11.5" stroke="currentColor" stroke-width="1.5"/><path d="M12 9c-1-3-2.5-4.5-4-4.5S5.5 6 7 9m5 0c1-3 2.5-4.5 4-4.5S18.5 6 17 9" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    heart:'<path d="M12 20s-7-4.4-7-9.3A4 4 0 0 1 12 8a4 4 0 0 1 7 2.7C19 15.6 12 20 12 20Z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/>',
    instagram:'<rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.6" fill="none"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.6" fill="none"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor"/>',
    whatsapp:'<path fill="currentColor" d="M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.48 1.34 5L2 22l5.2-1.36a9.9 9.9 0 0 0 4.84 1.24h.01c5.5 0 9.96-4.46 9.96-9.96C22.01 6.46 17.54 2 12.04 2Zm5.8 14.06c-.24.68-1.4 1.32-1.94 1.36-.5.05-.96.23-3.24-.68-2.74-1.08-4.46-3.88-4.6-4.06-.13-.18-1.1-1.46-1.1-2.78 0-1.32.7-1.97.94-2.24.25-.27.54-.34.72-.34h.52c.16 0 .4-.06.62.48.24.58.8 2 .87 2.14.07.14.12.3.02.48-.1.18-.15.3-.29.46-.14.16-.3.36-.43.48-.14.14-.29.29-.12.57.17.28.75 1.24 1.6 2 1.11.98 2.04 1.29 2.32 1.43.28.14.45.12.62-.07.17-.2.72-.83.91-1.12.19-.29.38-.24.64-.14.26.09 1.66.78 1.94.93.28.14.47.21.54.33.07.12.07.68-.17 1.36Z"/>',
    phone:'<path d="M6.5 3.5h3l1.5 4-2 1.4a11 11 0 0 0 5.1 5.1l1.4-2 4 1.5v3c0 1.1-.9 2-2 2A15.5 15.5 0 0 1 4.5 5.5c0-1.1.9-2 2-2Z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/>'
  };
  const ico = (n, cls) => '<svg class="' + (cls || '') + '" viewBox="0 0 24 24" aria-hidden="true">' + (ICONS[n] || '') + '</svg>';

  /* ============================================================
     2) رسم الواجهة الكبيرة وواجهة القصة
     ============================================================ */
  function heroArt() {
    return `
<svg viewBox="0 0 520 580" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="hArch" x1=".2" y1="0" x2=".9" y2="1">
      <stop offset="0" stop-color="#255c48"/><stop offset="1" stop-color="#0e2419"/>
    </linearGradient>
    <linearGradient id="hGold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f0e0b4"/><stop offset=".45" stop-color="#c2a15a"/><stop offset="1" stop-color="#8d7135"/>
    </linearGradient>
    <linearGradient id="hBottle" x1=".1" y1="0" x2=".9" y2="1">
      <stop offset="0" stop-color="#d8b878"/><stop offset="1" stop-color="#6b4a20"/>
    </linearGradient>
    <radialGradient id="hGlow" cx=".5" cy=".34" r=".55">
      <stop offset="0" stop-color="#c2a15a" stop-opacity=".4"/><stop offset="1" stop-color="#c2a15a" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <path d="M56 560V226C56 113 147 22 260 22s204 91 204 204v306a28 28 0 0 1-28 28H84a28 28 0 0 1-28-28Z" fill="url(#hArch)"/>
  <path d="M56 532V226C56 113 147 22 260 22s204 91 204 204v306a28 28 0 0 1-28 28H84a28 28 0 0 1-28-28Z" fill="none" stroke="url(#hGold)" stroke-width="2" opacity=".65"/>
  <path d="M86 560V230c0-96 78-174 174-174s174 78 174 174v330" fill="none" stroke="#c2a15a" stroke-opacity=".3" stroke-width="1" stroke-dasharray="2 10" stroke-linecap="round"/>
  <ellipse cx="260" cy="330" rx="180" ry="180" fill="url(#hGlow)"/>

  <circle cx="260" cy="118" r="32" fill="none" stroke="url(#hGold)" stroke-width="1.8"/>
  <text x="260" y="130" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-size="30" fill="#c2a15a">R</text>
  <text x="260" y="170" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-size="13" letter-spacing="6" fill="#c2a15a" opacity=".8">AL ROGI</text>

  <path d="M260 232c-22-22 22-34 0-56" fill="none" stroke="#c2a15a" stroke-opacity=".45" stroke-width="3" stroke-linecap="round"/>
  <path d="M318 244c-16-16 16-25 0-40" fill="none" stroke="#c2a15a" stroke-opacity=".26" stroke-width="2.6" stroke-linecap="round"/>
  <path d="M204 246c-14-14 14-22 0-34" fill="none" stroke="#c2a15a" stroke-opacity=".26" stroke-width="2.4" stroke-linecap="round"/>

  <ellipse cx="260" cy="520" rx="150" ry="22" fill="#000" opacity=".2"/>

  <rect x="150" y="392" width="96" height="118" rx="18" fill="#123024"/>
  <rect x="138" y="356" width="120" height="42" rx="13" fill="url(#hGold)"/>
  <rect x="138" y="356" width="120" height="11" rx="5" fill="#fff" opacity=".3"/>
  <rect x="166" y="424" width="64" height="52" rx="9" fill="#fbf7ee" opacity=".92"/>
  <text x="198" y="459" text-anchor="middle" font-family="Georgia,serif" font-size="26" fill="#9a7c3c">R</text>

  <rect x="286" y="330" width="80" height="180" rx="24" fill="url(#hBottle)"/>
  <rect x="286" y="330" width="24" height="180" rx="12" fill="#fff" opacity=".18"/>
  <rect x="310" y="288" width="34" height="46" fill="#8a6229"/>
  <rect x="300" y="222" width="54" height="72" rx="13" fill="url(#hGold)"/>
  <rect x="300" y="258" width="54" height="8" fill="#fff" opacity=".28"/>
  <circle cx="327" cy="218" r="12" fill="url(#hGold)"/>
  <rect x="298" y="404" width="56" height="46" rx="9" fill="#fbf7ee" opacity=".9"/>
  <text x="326" y="437" text-anchor="middle" font-family="Georgia,serif" font-size="24" fill="#9a7c3c">R</text>
</svg>`;
  }

  function storyArt() {
    return `
<svg viewBox="0 0 440 450" preserveAspectRatio="xMidYMid slice">
  <defs>
    <linearGradient id="sBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#245847"/><stop offset="1" stop-color="#0d2118"/>
    </linearGradient>
    <linearGradient id="sGold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f0e0b4"/><stop offset=".5" stop-color="#c2a15a"/><stop offset="1" stop-color="#8d7135"/>
    </linearGradient>
    <pattern id="sPat" width="60" height="60" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <path d="M30 4 46 30 30 56 14 30Z" fill="none" stroke="#c2a15a" stroke-opacity=".22" stroke-width="1"/>
      <circle cx="30" cy="30" r="3" fill="#c2a15a" fill-opacity=".18"/>
    </pattern>
  </defs>
  <rect width="440" height="450" fill="url(#sBg)"/>
  <rect width="440" height="450" fill="url(#sPat)"/>
  <circle cx="220" cy="200" r="120" fill="none" stroke="#c2a15a" stroke-opacity=".35" stroke-width="1.4"/>
  <circle cx="220" cy="200" r="104" fill="none" stroke="#c2a15a" stroke-opacity=".22" stroke-width="1" stroke-dasharray="2 9"/>
  <circle cx="220" cy="200" r="62" fill="none" stroke="url(#sGold)" stroke-width="2.2"/>
  <text x="220" y="222" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-size="62" fill="#c2a15a">R</text>
  <text x="220" y="316" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-size="17" letter-spacing="9" fill="#c2a15a" opacity=".85">AL ROGI</text>
  <text x="220" y="350" text-anchor="middle" font-family="Tajawal,sans-serif" font-size="15" letter-spacing="2" fill="#e8e3d5" opacity=".62">الروقي للعطور</text>
  <path d="M120 380h200" stroke="#c2a15a" stroke-opacity=".4" stroke-width="1"/>
</svg>`;
  }

  /* ============================================================
     3) البناء
     ============================================================ */
  function renderFilters() {
    const box = $('#filters');
    box.innerHTML = CATEGORIES.map((c, i) =>
      `<button class="chip${i === 0 ? ' is-active' : ''}" data-cat="${c.id}" role="tab">${esc(c.label)}</button>`
    ).join('');

    box.addEventListener('click', e => {
      const b = e.target.closest('.chip');
      if (!b) return;
      $$('.chip', box).forEach(c => c.classList.toggle('is-active', c === b));
      renderProducts(b.dataset.cat);
    });
  }

  function catLabel(id) {
    const c = CATEGORIES.find(x => x.id === id);
    return c ? c.label : '';
  }

  function renderProducts(cat) {
    const list = (!cat || cat === 'all') ? PRODUCTS : PRODUCTS.filter(p => p.cat === cat);
    $('#grid').innerHTML = list.map(p => {
      const msg = 'مرحباً، أرغب في طلب: ' + p.name + ' (' + p.size + ')' +
                  (p.price ? ' — السعر ' + p.price + ' ' + BRAND.currency : ' — أرجو إفادتي بالسعر');
      const priceHtml = p.price
        ? esc(p.price) + '<span>' + esc(BRAND.currency) + '</span>'
        : '<span class="card__ask">السعر عبر واتساب</span>';
      return `
<article class="card reveal${p.img ? ' card--photo' : ''}">
  <div class="card__media">
    ${p.badge ? `<span class="card__badge">${esc(p.badge)}</span>` : ''}
    <span class="card__cat">${esc(catLabel(p.cat))}</span>
    ${p.img ? `<img class="card__img" src="${esc(p.img)}" alt="${esc(p.name)}" loading="lazy" decoding="async">` : artFor(p)}
  </div>
  <div class="card__body">
    <h3 class="card__name">${esc(p.name)}</h3>
    <p class="card__desc">${esc(p.desc)}</p>
    <div class="card__meta">
      <span class="card__size">${esc(p.size)}</span>
      <span class="card__price">${priceHtml}</span>
    </div>
    <a class="card__order" href="${waLink(msg)}" target="_blank" rel="noopener">
      ${ico('whatsapp', 'ico')} اطلب عبر واتساب
    </a>
  </div>
</article>`;
    }).join('');
    observe();
  }

  function renderFeatures() {
    $('#features').innerHTML = FEATURES.map(f => `
<div class="feature reveal">
  <span class="feature__ico">${ico(f.icon)}</span>
  <h3>${esc(f.title)}</h3>
  <p>${esc(f.text)}</p>
</div>`).join('');

    const hlIcons = ['camera', 'chat', 'flame', 'gift', 'heart', 'truck'];
    $('#highlights').innerHTML = HIGHLIGHTS.map((h, i) => `
<div class="hl reveal">
  <span class="hl__ring">${ico(hlIcons[i % hlIcons.length])}</span>
  <strong>${esc(h.title)}</strong>
  <span>${esc(h.text)}</span>
</div>`).join('');
  }

  function renderQuotes() {
    const star = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="m12 3.6 2.6 5.3 5.9.9-4.3 4.1 1 5.8-5.2-2.7-5.2 2.7 1-5.8L3.5 9.8l5.9-.9L12 3.6Z"/></svg>';
    $('#quotes').innerHTML = QUOTES.map(q => `
<figure class="quote reveal">
  <div class="quote__stars">${star.repeat(5)}</div>
  <p>${esc(q.text)}</p>
  <figcaption class="quote__by">
    <span class="quote__av">${esc(q.name.trim().charAt(0))}</span>
    <span><strong>${esc(q.name)}</strong><small>${esc(q.role)}</small></span>
  </figcaption>
</figure>`).join('');
  }

  function renderPhones() {
    const rows = [
      { num: BRAND.whatsapp, show: BRAND.phoneDisplay, note: 'واتساب — للطلب والاستفسار' },
      { num: BRAND.phone2,   show: BRAND.phone2Display, note: 'رقم إضافي للطلبات' }
    ].filter(r => r.num);

    $('#phones').innerHTML = rows.map(r => `
<a class="phone-row" href="${waLink('مرحباً، أود الطلب من الروقي للعطور.', r.num)}" target="_blank" rel="noopener">
  <span class="phone-row__ico">${ico('whatsapp')}</span>
  <span><strong>${esc(r.show)}</strong><small>${esc(r.note)}</small></span>
  <span class="phone-row__go">اضغط للمحادثة ←</span>
</a>`).join('');
  }

  function renderSocial() {
    $('#social').innerHTML = BRAND.social.map(s =>
      `<a href="${s.url}" target="_blank" rel="noopener" aria-label="${esc(s.label)}" title="${esc(s.label)}">${ico(s.icon)}</a>`
    ).join('');
  }

  /* ============================================================
     4) التفاعل
     ============================================================ */
  let io;
  function observe() {
    const items = $$('.reveal:not(.is-in):not(.is-pending)');
    if (!('IntersectionObserver' in window)) { items.forEach(i => i.classList.add('is-in')); return; }
    if (!io) {
      io = new IntersectionObserver((entries) => {
        entries.forEach(en => {
          if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    }
    /* ما يبدأ مخفياً إلا العناصر الموجودة تحت الشاشة — الصفحة تظهر كاملة عند التحميل */
    items.forEach((el, i) => {
      if (el.getBoundingClientRect().top < window.innerHeight * .95) { el.classList.add('is-in'); return; }
      el.classList.add('is-pending');
      el.style.transitionDelay = Math.min(i % 8, 6) * 55 + 'ms';
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
      header.classList.toggle('is-stuck', window.scrollY > 10);
      let current = '';
      $$('main section[id]').forEach(s => {
        if (window.scrollY >= s.offsetTop - 140) current = s.id;
      });
      links.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + current));
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  function wireWhatsapp() {
    $$('[data-wa]').forEach(el => {
      el.setAttribute('href', waLink(el.dataset.wa));
      el.setAttribute('target', '_blank');
      el.setAttribute('rel', 'noopener');
    });
  }

  /* ============================================================
     5) الإقلاع
     ============================================================ */
  document.addEventListener('DOMContentLoaded', () => {
    $('#markHeader').innerHTML = MARK;
    $('#markFooter').innerHTML = MARK;
    $('#heroArt').innerHTML = heroArt();
    $('#storyArt').innerHTML = storyArt();
    $('#year').textContent = new Date().getFullYear();

    renderFilters();
    renderProducts('all');
    renderFeatures();
    renderQuotes();
    renderPhones();
    renderSocial();
    wireWhatsapp();
    wireNav();
    observe();
  });
})();
