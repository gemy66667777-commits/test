/* مول السعدني للمفروشات — منطق الموقع */
(function(){
'use strict';

const $  = (s,r)=> (r||document).querySelector(s);
const $$ = (s,r)=> Array.from((r||document).querySelectorAll(s));
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt = n => Number(n).toLocaleString('en-US');
const wa  = (num,msg) => `https://wa.me/${num}?text=${encodeURIComponent(msg)}`;

/* ---------------- أيقونات ---------------- */
const ICONS = {
  bed:'<path d="M2 20v-8a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v8"/><path d="M2 16h20"/><path d="M6 10V7a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v3"/><path d="M13 10V7a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v3"/>',
  towel:'<path d="M6 3h12a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/><path d="M8 7h8M8 11h8M8 15h5"/>',
  blanket:'<path d="M3 8a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v11H3z"/><path d="M3 12h18M7 5v14M12 5v14M17 5v14"/>',
  quilt:'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18M9 5v14M15 5v14"/>',
  robe:'<path d="M9 3 5 6v15h14V6l-4-3"/><path d="M9 3l3 5 3-5"/><path d="M12 8v13"/>',
  tag:'<path d="M20.6 13.4 12 22l-9-9V3h10z"/><circle cx="7.5" cy="7.5" r="1.4"/>',
  shield:'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
  truck:'<path d="M14 17V6a1 1 0 0 0-1-1H2v11a1 1 0 0 0 1 1h1"/><path d="M14 9h4l3 3v5h-2"/><circle cx="6.5" cy="17.5" r="2"/><circle cx="17.5" cy="17.5" r="2"/>',
  gift:'<path d="M20 12v9H4v-9"/><path d="M2 7h20v5H2z"/><path d="M12 21V7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/>',
  pin:'<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>'
};
const svg = (k,sz) => `<svg width="${sz||18}" height="${sz||18}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${ICONS[k]||''}</svg>`;

/* رسمة بديلة للمنتجات غير المصورة */
function placeholder(p){
  const icon = { beds:'bed', blankets:'blanket', quilts:'quilt', towels:'towel' }[p.cat] || 'bed';
  return `<div class="ph" style="color:rgba(74,14,26,.26)">
    <svg width="76" height="76" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">${ICONS[icon]}</svg>
  </div>
  <div class="card-note">الصورة قريباً — اسأل على واتساب</div>`;
}

/* ---------------- بيانات ثابتة في الواجهة ---------------- */
const featured = OFFERS.find(o => o.featured) || OFFERS[0];

$('#announce').innerHTML = `🎉 ${esc(featured.title)}: <b>${esc(featured.sub)}</b> بـ <b>${fmt(featured.price)} ${BRAND.currency}</b> بدل ${fmt(featured.was)} — الكمية محدودة`;
$('#brandName').textContent = BRAND.short;
$('#brandLatin').textContent = BRAND.latin;
$('#ftrName').textContent = BRAND.short;
$('#ftrLatin').textContent = BRAND.latin;
$('#ftrAbout').textContent = BRAND.tagline + '. بنبيع جملة وقطاعي، وبنشحن لكل المحافظات.';
$('#ftrHours').textContent = '🕒 ' + BRAND.hours;
$('#ftrRights').textContent = `© ${new Date().getFullYear()} ${BRAND.name} — كل الحقوق محفوظة.`;

const HI = `السلام عليكم ${BRAND.name}`;
$('#hdrWa').href = wa(BRAND.whatsapp, `${HI}، حابب أستفسر عن المنتجات والأسعار.`);
$('#fab').href    = wa(BRAND.whatsapp, `${HI}، حابب أستفسر عن المنتجات والأسعار.`);
$('#askWa').href  = wa(BRAND.whatsapp, `${HI}، ممكن تبعتولي صور وفيديوهات للأصناف المتاحة؟`);
$('#ctaWa').href  = wa(BRAND.whatsapp, `${HI}، عايز أجهّز جهاز عروسة وحابب أعرف الباكدچ المناسبة لميزانيتي.`);

/* ---------------- العروض ---------------- */
function offerMsg(o){
  const lines = o.groups.flatMap(g => g.items.map(i => `• ${i}`)).join('\n');
  return `${HI}، حابب أحجز «${o.title}» (${o.sub}) بسعر ${fmt(o.price)} ${BRAND.currency}.\n\nتفاصيل العرض:\n${lines}`;
}

$('#offerHero').innerHTML = `
<div class="offer-hero">
  <div class="offer-hero-img">
    <img src="${esc(featured.img)}" alt="${esc(featured.title)}" loading="lazy">
  </div>
  <div class="offer-hero-body">
    <span class="tag">${esc(featured.kicker)}</span>
    <h3>${esc(featured.title)}</h3>
    <p class="sub">${esc(featured.sub)}</p>
    <div class="price-row">
      <span class="price-big num">${fmt(featured.price)}<small>${esc(BRAND.currency)}</small></span>
      <s class="price-was num">${fmt(featured.was)}</s>
      <span class="save-pill">وفّر ${fmt(featured.was - featured.price)} ${esc(BRAND.currency)}</span>
    </div>
    <div class="groups">
      ${featured.groups.map(g => `
        <div class="group">
          <h4>${svg(g.icon,16)}<span>${esc(g.title)}</span></h4>
          <ul>${g.items.map(i => `<li>${esc(i)}</li>`).join('')}</ul>
        </div>`).join('')}
    </div>
    <a class="btn btn-gold btn-lg" href="${wa(BRAND.whatsapp, offerMsg(featured))}" target="_blank" rel="noopener">احجز العرض دلوقتي</a>
  </div>
</div>`;

$('#offerGrid').innerHTML = OFFERS.filter(o => !o.featured).map(o => `
<article class="offer-card">
  <span class="tag">${esc(o.kicker)}</span>
  <h3>${esc(o.title)}</h3>
  <p class="sub">${esc(o.sub)}</p>
  <div class="price-row">
    <span class="price-big num">${fmt(o.price)}<small>${esc(BRAND.currency)}</small></span>
    ${o.was ? `<s class="price-was num">${fmt(o.was)}</s><span class="save-pill">وفّر ${fmt(o.was-o.price)}</span>` : ''}
  </div>
  <ul class="flat">${o.groups.flatMap(g => g.items).map(i => `<li>${esc(i)}</li>`).join('')}</ul>
  <a class="btn btn-ghost" href="${wa(BRAND.whatsapp, offerMsg(o))}" target="_blank" rel="noopener">احجز العرض</a>
</article>`).join('');

/* ---------------- المنتجات ---------------- */
let activeCat = 'all';

$('#filters').innerHTML = CATEGORIES.map(c =>
  `<button class="chip${c.id==='all'?' on':''}" data-cat="${esc(c.id)}">${esc(c.name)}</button>`
).join('');

function renderGrid(){
  const list = activeCat === 'all' ? PRODUCTS : PRODUCTS.filter(p => p.cat === activeCat);
  $('#grid').innerHTML = list.map(p => `
  <article class="card">
    <div class="card-media">
      ${p.img ? `<img src="${esc(p.img)}" alt="${esc(p.name)}" loading="lazy">` : placeholder(p)}
      ${p.badge ? `<span class="card-badge">${esc(p.badge)}</span>` : ''}
    </div>
    <div class="card-body">
      <h3>${esc(p.name)}</h3>
      <p>${esc(p.desc)}</p>
      <div class="card-foot">
        <div class="p-price">
          ${p.price == null
            ? `<span class="ask">السعر على واتساب</span>`
            : `<b class="num">${fmt(p.price)}<small>${esc(BRAND.currency)}</small></b>
               ${p.was ? `<s class="num">${fmt(p.was)}</s>` : ''}`}
        </div>
        ${p.price == null
          ? `<a class="add" href="${wa(BRAND.whatsapp, `${HI}، عايز أعرف سعر «${p.name}».`)}" target="_blank" rel="noopener">اسأل عن السعر</a>`
          : `<button class="add" data-add="${esc(p.id)}">ضيف للسلة</button>`}
      </div>
    </div>
  </article>`).join('');
}
renderGrid();

$('#filters').addEventListener('click', e => {
  const b = e.target.closest('[data-cat]');
  if(!b) return;
  activeCat = b.dataset.cat;
  $$('.chip').forEach(c => c.classList.toggle('on', c === b));
  renderGrid();
});

/* ---------------- المزايا / الآراء / الفروع ---------------- */
$('#perks').innerHTML = PERKS.map(p => `
<div class="perk">
  <div class="perk-ic">${svg(p.icon,22)}</div>
  <h3>${esc(p.title)}</h3>
  <p>${esc(p.text)}</p>
</div>`).join('');

$('#reviewsGrid').innerHTML = REVIEWS.map(r =>
  `<figure class="review"><img src="${esc(r.img)}" alt="${esc(r.alt)}" loading="lazy"></figure>`
).join('');

$('#branchList').innerHTML = BRAND.branches.map(b => `
<div class="branch">
  <div class="branch-ic">${svg('pin',20)}</div>
  <div>
    <h3>${esc(b.name)}</h3>
    <p>${esc(b.addr)}</p>
    <a href="${esc(b.map)}" target="_blank" rel="noopener">افتح على الخريطة</a>
  </div>
</div>`).join('');

const waIcon = '<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.87 9.87 0 0 0 4.79 1.22c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2m4.52 12.2c-.26.72-1.51 1.41-2.07 1.46-.56.05-1.09.25-3.68-.77-3.11-1.22-5.14-4.35-5.3-4.56s-1.29-1.71-1.29-3.26c0-1.54.81-2.31 1.1-2.62s.63-.39.84-.39h.6c.19 0 .45-.7.69.53.25.61.85 2.11.93 2.26.08.15.13.33.03.54-.1.21-.15.34-.31.52-.15.18-.32.4-.46.54-.16.16-.32.32-.14.63.18.3.78 1.28 1.68 2.08 1.15 1.02 2.12 1.34 2.42 1.49s.47.13.65-.08c.17-.2.74-.88.95-1.19.2-.31.4-.26.68-.16s1.78.85 2.09 1c.31.15.52.23.6.36.08.13.08.74-.18 1.46z"/></svg>';
const telIcon = '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.4 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.4 1.8.6 2.8.8a2 2 0 0 1 1.7 2z"/></svg>';

const CONTACTS = [
  { kind:'wa',  label:'واتساب ١ — الطلبات', val:BRAND.whatsappShow,  href:wa(BRAND.whatsapp,  `${HI}، حابب أستفسر عن المنتجات.`) },
  { kind:'wa',  label:'واتساب ٢',           val:BRAND.whatsapp2Show, href:wa(BRAND.whatsapp2, `${HI}، حابب أستفسر عن المنتجات.`) },
  { kind:'tel', label:'للاتصال المباشر',    val:BRAND.phoneShow,     href:'tel:+'+BRAND.phone }
];

$('#contactStrip').innerHTML = CONTACTS.map(c => `
<a class="cbox" href="${esc(c.href)}"${c.kind==='wa'?' target="_blank" rel="noopener"':''}>
  <div class="cbox-ic${c.kind==='tel'?' tel':''}">${c.kind==='wa'?waIcon:telIcon}</div>
  <div><span>${esc(c.label)}</span><b class="num">${esc(c.val)}</b></div>
</a>`).join('');

$('#ftrContact').innerHTML = CONTACTS.map(c =>
  `<li><a href="${esc(c.href)}"${c.kind==='wa'?' target="_blank" rel="noopener"':''}>${esc(c.label)}: <span class="num" style="direction:ltr;display:inline-block">${esc(c.val)}</span></a></li>`
).join('') + BRAND.branches.map(b => `<li style="opacity:.8">${esc(b.name)}: ${esc(b.addr)}</li>`).join('');

/* ---------------- السلة ---------------- */
const KEY = 'alsadani_cart_v1';
let cart = {};
try { cart = JSON.parse(localStorage.getItem(KEY)) || {}; } catch(e){ cart = {}; }

const save = () => { try { localStorage.setItem(KEY, JSON.stringify(cart)); } catch(e){} };
const items = () => Object.keys(cart)
  .map(id => ({ p: PRODUCTS.find(x => x.id === id), q: cart[id] }))
  .filter(x => x.p && x.q > 0);
const count = () => items().reduce((s,x) => s + x.q, 0);
const total = () => items().reduce((s,x) => s + x.p.price * x.q, 0);

let toastT;
function toast(msg){
  const t = $('#toast');
  t.textContent = msg; t.classList.add('on');
  clearTimeout(toastT); toastT = setTimeout(() => t.classList.remove('on'), 2000);
}

function renderCart(){
  const list = items(), n = count();

  const cc = $('#cartCount');
  cc.textContent = n;
  cc.classList.toggle('on', n > 0);
  $('#drawerSub').textContent = n ? `${n} قطعة في السلة` : 'مفيش منتجات لسه';

  if(!list.length){
    $('#cartBody').innerHTML = `
    <div class="empty">
      <svg width="58" height="58" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
      <b>السلة فاضية</b>
      <p>ضيف المنتجات اللي عاجباك وابدأ طلبك.</p>
    </div>`;
    $('#cartFoot').hidden = true;
    return;
  }

  $('#cartBody').innerHTML = list.map(({p,q}) => `
  <div class="ci">
    <div class="ci-img">${p.img ? `<img src="${esc(p.img)}" alt="${esc(p.name)}">` : ''}</div>
    <div class="ci-b">
      <h4>${esc(p.name)}</h4>
      <div class="pr num">${fmt(p.price)} ${esc(BRAND.currency)} للقطعة</div>
      <div class="ci-ctl">
        <div class="qty">
          <button data-dec="${esc(p.id)}" aria-label="تقليل">−</button>
          <b class="num">${q}</b>
          <button data-inc="${esc(p.id)}" aria-label="زيادة">+</button>
        </div>
        <button class="rm" data-rm="${esc(p.id)}">إزالة</button>
      </div>
    </div>
  </div>`).join('');

  $('#cartTotal').innerHTML = `<span class="num">${fmt(total())}</span> ${esc(BRAND.currency)}`;
  $('#cartFoot').hidden = false;

  const lines = list.map(({p,q}) => `• ${p.name} × ${q} = ${fmt(p.price*q)} ${BRAND.currency}`).join('\n');
  const msg = `${HI}، حابب أأكد الطلب ده:\n\n${lines}\n\nعدد القطع: ${count()}\nالإجمالي: ${fmt(total())} ${BRAND.currency}\n\nالاسم:\nالمحافظة:\nالعنوان:`;
  $('#checkout').href = wa(BRAND.whatsapp, msg);
}
renderCart();

document.addEventListener('click', e => {
  const add = e.target.closest('[data-add]');
  if(add){
    const id = add.dataset.add;
    cart[id] = (cart[id] || 0) + 1;
    save(); renderCart();
    add.textContent = 'اتضاف ✓'; add.classList.add('done');
    setTimeout(() => { add.textContent = 'ضيف للسلة'; add.classList.remove('done'); }, 1200);
    toast('تمت الإضافة للسلة');
    return;
  }
  const inc = e.target.closest('[data-inc]');
  if(inc){ cart[inc.dataset.inc]++; save(); renderCart(); return; }

  const dec = e.target.closest('[data-dec]');
  if(dec){
    const id = dec.dataset.dec;
    cart[id]--; if(cart[id] <= 0) delete cart[id];
    save(); renderCart(); return;
  }
  const rm = e.target.closest('[data-rm]');
  if(rm){ delete cart[rm.dataset.rm]; save(); renderCart(); return; }
});

/* ---------------- فتح وقفل السلة والقائمة ---------------- */
const openCart  = () => { $('#drawer').classList.add('on'); $('#ov').classList.add('on'); document.body.style.overflow='hidden'; };
const closeCart = () => { $('#drawer').classList.remove('on'); $('#ov').classList.remove('on'); document.body.style.overflow=''; };

$('#cartBtn').addEventListener('click', openCart);
$('#closeCart').addEventListener('click', closeCart);
$('#ov').addEventListener('click', closeCart);
document.addEventListener('keydown', e => { if(e.key === 'Escape') closeCart(); });

$('#burger').addEventListener('click', () => $('#nav').classList.toggle('open'));
$$('#nav a').forEach(a => a.addEventListener('click', () => $('#nav').classList.remove('open')));

})();
