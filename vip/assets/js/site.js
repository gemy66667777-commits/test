/* =============================================================
   V.I.P SILVER — اللغة + السلة + الحساب + لوحة الأدمن
   ============================================================= */
(function () {
  'use strict';

  const $  = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.from((c || document).querySelectorAll(s));
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));
  const money = n => Number(n).toLocaleString('en-US');
  const wa = msg => 'https://wa.me/' + BRAND.whatsapp + '?text=' + encodeURIComponent(msg);
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; } },
    del(k) { try { localStorage.removeItem(k); } catch (e) {} }
  };

  /* ------------------------------ اللغة ------------------------------ */
  const LKEY = 'vip_lang';
  let lang = 'ar';
  try { const v = localStorage.getItem(LKEY); if (v === 'ar' || v === 'en') lang = v; } catch (e) {}
  const t   = k => T[lang][k];
  const tx  = v => (v && typeof v === 'object') ? (v[lang] || v.ar || v.en || '') : (v || '');
  const cur = () => tx(BRAND.currency);

  /* ------------------------------ الشعار ------------------------------ */
  const LOGO = `
<svg viewBox="0 0 224 108" style="direction:ltr" role="img" aria-label="V.I.P SILVER">
  <defs>
    <linearGradient id="vg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f4e4b6"/><stop offset=".45" stop-color="#cfa84e"/><stop offset="1" stop-color="#8f6f2a"/>
    </linearGradient>
  </defs>
  <g fill="url(#vg)">
    <g transform="translate(112,42)">
      <g id="vw">
        <path d="M6 -7C26 -15 54 -17 80 -11 55 -6 33 -3 13 1Z"/>
        <path d="M6 -1C24 -7 48 -8 70 -4 47 1 28 4 11 7Z"/>
        <path d="M6 5C22 2 43 3 62 8 42 11 26 12 9 13Z"/>
        <path d="M6 11C19 9 35 11 50 15 33 16 20 17 8 18Z"/>
      </g>
      <use href="#vw" transform="scale(-1,1)"/>
    </g>
    <path d="M100 30l2.6-14 5.2 8 4.2-12 4.2 12 5.2-8 2.6 14z"/>
    <circle cx="112" cy="40" r="6.4"/>
  </g>
  <text x="112" y="82" text-anchor="middle" font-family="Cinzel,Georgia,serif" font-size="33"
        font-weight="700" letter-spacing="1.5" fill="url(#vg)">V.I.P</text>
  <text x="112" y="99" text-anchor="middle" font-family="Cinzel,Georgia,serif" font-size="11.5"
        letter-spacing="10" fill="#cfa84e" opacity=".9">SILVER</text>
</svg>`;

  const ICONS = {
    shield:'<path d="M12 3l7 3v5.6c0 4.3-2.9 7.6-7 9.4-4.1-1.8-7-5.1-7-9.4V6l7-3Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" fill="none"/><path d="m9 12 2.2 2.2L15.5 10" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/>',
    pen:'<path d="M4 20h4L19.5 8.5a2.1 2.1 0 0 0 0-3l-1-1a2.1 2.1 0 0 0-3 0L4 16v4Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" fill="none"/><path d="m14.5 6.5 3 3" stroke="currentColor" stroke-width="1.5"/>',
    truck:'<rect x="2.5" y="6.5" width="11" height="9" rx="2" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M13.5 9.5h3.6l2.9 3v3h-6.5Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" fill="none"/><circle cx="7" cy="17.5" r="1.9" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="16.5" cy="17.5" r="1.9" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    gift:'<rect x="3.5" y="9" width="17" height="11.5" rx="2" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M2.5 9h19M12 9v11.5" stroke="currentColor" stroke-width="1.5"/><path d="M12 9c-1-3-2.5-4.5-4-4.5S5.5 6 7 9m5 0c1-3 2.5-4.5 4-4.5S18.5 6 17 9" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    bag:'<path d="M4 7h16l-1.3 12.1a2 2 0 0 1-2 1.9H7.3a2 2 0 0 1-2-1.9Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round" fill="none"/><path d="M8.6 7V5.9a3.4 3.4 0 0 1 6.8 0V7" stroke="currentColor" stroke-width="1.4" fill="none"/>',
    plus:'<path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>',
    check:'<path d="m5 13 4 4L19 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>',
    edit:'<path d="M4 20h4L19.5 8.5a2.1 2.1 0 0 0 0-3l-1-1a2.1 2.1 0 0 0-3 0L4 16v4Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" fill="none"/>',
    wa:'<path fill="currentColor" d="M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.48 1.34 5L2 22l5.2-1.36a9.9 9.9 0 0 0 4.84 1.24h.01c5.5 0 9.96-4.46 9.96-9.96C22.01 6.46 17.54 2 12.04 2Zm5.8 14.06c-.24.68-1.4 1.32-1.94 1.36-.5.05-.96.23-3.24-.68-2.74-1.08-4.46-3.88-4.6-4.06-.13-.18-1.1-1.46-1.1-2.78 0-1.32.7-1.97.94-2.24.25-.27.54-.34.72-.34h.52c.16 0 .4-.06.62.48.24.58.8 2 .87 2.14.07.14.12.3.02.48-.1.18-.15.3-.29.46-.14.16-.3.36-.43.48-.14.14-.29.29-.12.57.17.28.75 1.24 1.6 2 1.11.98 2.04 1.29 2.32 1.43.28.14.45.12.62-.07.17-.2.72-.83.91-1.12.19-.29.38-.24.64-.14.26.09 1.66.78 1.94.93.28.14.47.21.54.33.07.12.07.68-.17 1.36Z"/>'
  };
  const ico = n => '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">' + (ICONS[n] || '') + '</svg>';

  /* ------------------------------ المنتجات ------------------------------ */
  const PKEY = 'vip_products_v2';
  let PRODUCTS = store.get(PKEY, null) || JSON.parse(JSON.stringify(DEFAULT_PRODUCTS));
  const saveProducts = () => store.set(PKEY, PRODUCTS);
  const byId = id => PRODUCTS.find(p => p.id === id);
  const catLabel = id => { const c = CATEGORIES.find(x => x.id === id); return c ? tx(c.label) : ''; };
  const otherName = p => (p.name && typeof p.name === 'object') ? (lang === 'ar' ? p.name.en : p.name.ar) : '';

  /* ------------------------------ الحساب ------------------------------ */
  const UKEY = 'vip_users_v1', SKEY = 'vip_session_v1';
  let users = store.get(UKEY, {});
  let me = store.get(SKEY, null);
  let pending = null;

  const normPhone = v => String(v || '').replace(/[^\d]/g, '');
  const validPhone = v => /^01[0125]\d{8}$/.test(normPhone(v));
  const isAdminPhone = v => BRAND.admins.map(normPhone).includes(normPhone(v));
  const isAdmin = () => !!(me && isAdminPhone(me));

  async function hashPw(pw, salt) {
    const txt = salt + '|' + pw;
    if (window.crypto && crypto.subtle) {
      const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(txt));
      return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
    }
    let h = 0;
    for (let i = 0; i < txt.length; i++) h = (h * 31 + txt.charCodeAt(i)) | 0;
    return 'x' + (h >>> 0).toString(16);
  }
  const newSalt = () => Math.random().toString(36).slice(2) + Date.now().toString(36);

  /* ------------------------------ السلة ------------------------------ */
  const CKEY = 'vip_cart_v1';
  let cart = store.get(CKEY, {});
  const saveCart = () => store.set(CKEY, cart);
  const count = () => Object.values(cart).reduce((a, b) => a + b, 0);
  const total = () => Object.entries(cart).reduce((s, [id, q]) => { const p = byId(id); return p ? s + p.price * q : s; }, 0);

  /* ============================================================
     العرض
     ============================================================ */
  function renderTabs() {
    const el = $('#tabs .tab.is-on');
    const on = el ? el.dataset.cat : 'all';
    $('#tabs').innerHTML = CATEGORIES.map(c =>
      `<button class="tab${c.id === on ? ' is-on' : ''}" data-cat="${c.id}" role="tab">${esc(tx(c.label))}</button>`
    ).join('');
  }
  const currentCat = () => { const el = $('#tabs .tab.is-on'); return el ? el.dataset.cat : 'all'; };

  function renderGrid(cat) {
    cat = cat || currentCat();
    const list = (cat === 'all') ? PRODUCTS : PRODUCTS.filter(p => p.cat === cat);
    $('#grid').innerHTML = list.map(p => {
      const sub = otherName(p);
      return `
<article class="card rev">
  <div class="card__shot">
    ${p.badge && tx(p.badge) ? `<span class="card__tag">${esc(tx(p.badge))}</span>` : ''}
    ${isAdmin() ? `<button class="card__edit" data-edit="${p.id}">${ico('edit')} ${esc(t('edit'))}</button>` : ''}
    <img src="${esc(p.img)}" alt="${esc(tx(p.name))}" loading="lazy" decoding="async">
  </div>
  <div class="card__body">
    ${sub ? `<span class="card__sub">${esc(sub)}</span>` : ''}
    <h3 class="card__name">${esc(tx(p.name))}</h3>
    <p class="card__desc">${esc(tx(p.desc))}</p>
    <div class="card__foot">
      <span class="card__price"><span class="num">${money(p.price)}</span><small>${esc(cur())}</small></span>
      <button class="card__add" data-add="${p.id}">${ico('plus')} ${esc(t('add'))}</button>
    </div>
  </div>
</article>`;
    }).join('') || `<p class="lead">${esc(t('emptyCat'))}</p>`;
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

  function renderCart() {
    const n = count(), sum = total();
    const badge = $('#cartCount');
    badge.textContent = n;
    badge.classList.toggle('is-on', n > 0);
    $('#cartSub').textContent = n ? n + ' ' + t('pieces') : t('cartEmptySub');

    const body = $('#cartBody'), foot = $('#cartFoot');
    if (!n) {
      body.innerHTML = `<div class="cart__empty">${ico('bag')}<p>${esc(t('cartEmpty'))}</p><p style="font-size:.84rem">${esc(t('cartEmptyHint'))}</p></div>`;
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
    <div class="li__n">${esc(tx(p.name))}</div>
    <div class="li__u"><span class="num">${money(p.price)}</span> ${esc(cur())} / ${esc(t('each'))}</div>
    <div class="li__r">
      <div class="qty">
        <button data-dec="${p.id}" aria-label="−">−</button><span class="num">${q}</span><button data-inc="${p.id}" aria-label="+">+</button>
      </div>
      <span class="li__s"><span class="num">${money(p.price * q)}</span> ${esc(cur())}</span>
    </div>
    <button class="li__d" data-del="${p.id}">${esc(t('remove'))}</button>
  </div>
</div>`;
    }).join('');
    foot.hidden = false;
    $('#cartTotal').textContent = money(sum);
    $('#curLabel').textContent = cur();

    const ship = $('#ship'), left = BRAND.freeShipFrom - sum;
    if (!BRAND.freeShipFrom || left <= 0) {
      ship.className = 'ship is-free';
      ship.innerHTML = ico('check') + '<span>' + t('shipFree') + '</span>';
    } else {
      ship.className = 'ship';
      ship.innerHTML = ico('truck') + '<span>' + t('shipLeft')(money(left), esc(cur())) + '</span>';
    }
  }

  let toastT;
  function toast(msg) {
    const el = $('#toast');
    el.innerHTML = ico('check') + '<span>' + esc(msg) + '</span>';
    el.classList.add('is-on');
    clearTimeout(toastT);
    toastT = setTimeout(() => el.classList.remove('is-on'), 2400);
  }

  function add(id, btn) {
    cart[id] = (cart[id] || 0) + 1;
    saveCart(); renderCart(); toast(t('addedToast'));
    if (btn) {
      btn.classList.add('is-added');
      btn.innerHTML = ico('check') + ' ' + t('added');
      setTimeout(() => { btn.classList.remove('is-added'); btn.innerHTML = ico('plus') + ' ' + t('add'); }, 1400);
    }
  }

  /* ------------------------------ النوافذ ------------------------------ */
  function scrim(on) {
    const any = on || ['#authModal', '#editModal', '#orderModal'].some(s => $(s).classList.contains('is-on'))
                || $('#cart').classList.contains('is-on');
    $('#scrim').classList.toggle('is-on', any);
    document.body.classList.toggle('is-locked', any);
  }
  function openCart(on) {
    $('#cart').classList.toggle('is-on', on);
    $('#cart').setAttribute('aria-hidden', String(!on));
    scrim(on);
    if (on) $('#cartClose').focus();
  }
  function openAuth(on) {
    $('#authModal').classList.toggle('is-on', on);
    scrim(on);
    if (on) { authMsg(''); setTimeout(() => { const f = $('#authModal input'); if (f) f.focus(); }, 120); }
  }
  function openEdit(on) { $('#editModal').classList.toggle('is-on', on); scrim(on); }
  function openOrder(on) { $('#orderModal').classList.toggle('is-on', on); scrim(on); }

  /* ============================================================
     الحساب — رقم ثم كلمة مرور (بلا رمز تحقق)
     ============================================================ */
  function authMsg(text, kind) {
    const el = $('#authMsg');
    el.className = 'msg' + (text ? ' is-on msg--' + (kind || 'err') : '');
    el.textContent = text || '';
  }

  function authView() {
    const b = $('#authBody');
    if (me) {
      const admin = isAdmin();
      $('#authTitle').textContent = t('yourAcc');
      $('#authSub').textContent = admin ? t('adminAccSub') : t('clientAccSub');
      b.innerHTML = `
        <div class="field"><label>${esc(t('phoneLabel'))}</label><input type="tel" value="${esc(me)}" disabled></div>
        ${admin ? `<div class="msg is-on msg--note">${esc(t('adminNote'))}</div>` : ''}
        <button class="btn btn--ghost btn--wide" id="logout">${esc(t('logout'))}</button>`;
      $('#logout').onclick = () => {
        me = null; store.del(SKEY);
        refreshAuthUI(); renderGrid(); openAuth(false); toast(t('loggedOut'));
      };
      return;
    }

    if (!pending) {
      $('#authTitle').textContent = t('signIn');
      $('#authSub').textContent = t('authSub');
      b.innerHTML = `
        <div class="field">
          <label>${esc(t('phoneLabel'))}</label>
          <input type="tel" id="ph" inputmode="numeric" placeholder="01xxxxxxxxx" maxlength="11" autocomplete="tel">
          <small>${esc(t('phoneHint'))}</small>
        </div>
        <button class="btn btn--gold btn--wide" id="go">${esc(t('next'))}</button>`;
      $('#go').onclick = stepPhone;
      $('#ph').onkeydown = e => { if (e.key === 'Enter') stepPhone(); };
      return;
    }

    if (pending.step === 'pass') {
      $('#authTitle').textContent = t('pickPass');
      $('#authSub').textContent = t('pickPassSub') + pending.phone + t('pickPassSub2');
      b.innerHTML = `
        <div class="field"><label>${esc(t('pass'))}</label><input type="password" id="p1" minlength="6" placeholder="${esc(t('passPh'))}"></div>
        <div class="field"><label>${esc(t('passConfirm'))}</label><input type="password" id="p2" minlength="6"></div>
        <button class="btn btn--gold btn--wide" id="go">${esc(t('createAcc'))}</button>
        <div class="modal__foot"><button class="link-btn" id="back">${esc(t('changePhone'))}</button></div>`;
      $('#go').onclick = stepPass;
      $('#p2').onkeydown = e => { if (e.key === 'Enter') stepPass(); };
      $('#back').onclick = () => { pending = null; authMsg(''); authView(); };
      return;
    }

    if (pending.step === 'login') {
      $('#authTitle').textContent = pending.admin ? t('adminLogin') : t('welcomeBack');
      $('#authSub').textContent = (pending.admin ? t('adminLoginSub') : t('loginSub')) + pending.phone;
      b.innerHTML = `
        <div class="field"><label>${esc(t('pass'))}</label><input type="password" id="p1" autocomplete="current-password"></div>
        <button class="btn btn--gold btn--wide" id="go">${esc(t('login'))}</button>
        <div class="modal__foot"><button class="link-btn" id="back">${esc(t('changePhone'))}</button></div>`;
      $('#go').onclick = stepLogin;
      $('#p1').onkeydown = e => { if (e.key === 'Enter') stepLogin(); };
      $('#back').onclick = () => { pending = null; authMsg(''); authView(); };
    }
  }

  function stepPhone() {
    const v = normPhone($('#ph').value);
    if (!validPhone(v)) return authMsg(t('badPhone'));
    authMsg('');
    if (isAdminPhone(v)) pending = { phone: v, step: 'login', admin: true };
    else if (users[v])   pending = { phone: v, step: 'login' };
    else                 pending = { phone: v, step: 'pass' };
    authView();
  }

  async function stepPass() {
    const a = $('#p1').value, b2 = $('#p2').value;
    if (a.length < 6) return authMsg(t('passShort'));
    if (a !== b2) return authMsg(t('passMismatch'));
    const salt = newSalt();
    users[pending.phone] = { salt, hash: await hashPw(a, salt), at: Date.now() };
    store.set(UKEY, users);
    me = pending.phone; store.set(SKEY, me);
    pending = null; authMsg('');
    refreshAuthUI(); renderGrid(); openAuth(false);
    toast(t('accCreated'));
  }

  async function stepLogin() {
    if (pending.admin) {
      if ($('#p1').value !== String(BRAND.adminPass)) return authMsg(t('passWrong'));
    } else {
      const u = users[pending.phone];
      const h = await hashPw($('#p1').value, u.salt);
      if (h !== u.hash) return authMsg(t('passWrong'));
    }
    me = pending.phone; store.set(SKEY, me);
    pending = null; authMsg('');
    refreshAuthUI(); renderGrid(); openAuth(false);
    toast(isAdmin() ? t('welcomeAdmin') : t('welcome'));
  }

  function refreshAuthUI() {
    const admin = isAdmin();
    $('#accTxt').textContent = me ? (admin ? t('adminAcc') : t('myAcc')) : t('signIn');
    $('#accBtn').classList.toggle('ib--admin', admin);
    $('#adminBar').hidden = !admin;
    document.body.classList.toggle('is-admin', admin);
  }

  /* ============================================================
     بيانات الطلب
     ============================================================ */
  const OKEY = 'vip_customer_v1';

  function orderMsgBox(text, kind) {
    const el = $('#orderMsg');
    el.className = 'msg' + (text ? ' is-on msg--' + (kind || 'err') : '');
    el.textContent = text || '';
  }

  function orderView() {
    const saved = store.get(OKEY, {});
    orderMsgBox('');
    $('#orderBody').innerHTML = `
      <div class="row2">
        <div class="field"><label>${esc(t('fName'))} *</label><input id="o_name" value="${esc(saved.name || '')}" placeholder="${esc(t('fNamePh'))}"></div>
        <div class="field"><label>${esc(t('fPhone'))} *</label><input id="o_phone" type="tel" inputmode="numeric" maxlength="11" value="${esc(saved.phone || me || '')}" placeholder="01xxxxxxxxx"></div>
      </div>
      <div class="field"><label>${esc(t('fGov'))} *</label><select id="o_gov">
        <option value="">${esc(t('fGovPick'))}</option>
        ${GOVS.map(g => `<option value="${esc(g.ar)}"${g.ar === saved.gov ? ' selected' : ''}>${esc(tx(g))}</option>`).join('')}
      </select></div>
      <div class="field"><label>${esc(t('fAddr'))} *</label><textarea id="o_addr" placeholder="${esc(t('fAddrPh'))}">${esc(saved.addr || '')}</textarea></div>
      <div class="field"><label>${esc(t('fNote'))}</label><input id="o_note" placeholder="${esc(t('fNotePh'))}"></div>
      <button class="btn btn--wa btn--wide" id="o_send">${ico('wa')} ${esc(t('sendOrder'))}</button>
      <p class="cart__note">${esc(t('orderNote'))}</p>`;
    $('#o_send').onclick = sendOrder;
  }

  const govLabel = ar => { const g = GOVS.find(x => x.ar === ar); return g ? tx(g) : ar; };

  function orderMessage(info) {
    const L = [t('msgHead'), ''];
    let i = 1;
    for (const [id, q] of Object.entries(cart)) {
      const p = byId(id);
      if (!p) continue;
      L.push(i++ + '. ' + tx(p.name));
      L.push('   ' + q + ' × ' + money(p.price) + ' = ' + money(p.price * q) + ' ' + cur());
    }
    const sum = total();
    L.push('', '— — — — —', t('msgCount') + ': ' + count(), t('msgTotal') + ': ' + money(sum) + ' ' + cur());
    if (BRAND.freeShipFrom && sum >= BRAND.freeShipFrom) L.push(t('msgShip') + ': ' + t('msgFree'));
    L.push('', t('msgCustomer'),
      t('msgName') + ': ' + info.name, t('msgPhone') + ': ' + info.phone,
      t('msgGov') + ': ' + govLabel(info.gov), t('msgAddr') + ': ' + info.addr);
    if (info.note) L.push(t('msgNote') + ': ' + info.note);
    return L.join('\n');
  }

  function sendOrder() {
    const info = {
      name: $('#o_name').value.trim(),
      phone: normPhone($('#o_phone').value),
      gov: $('#o_gov').value,
      addr: $('#o_addr').value.trim(),
      note: $('#o_note').value.trim()
    };
    if (info.name.length < 3) return orderMsgBox(t('errName'));
    if (!validPhone(info.phone)) return orderMsgBox(t('badPhone'));
    if (!info.gov) return orderMsgBox(t('errGov'));
    if (info.addr.length < 10) return orderMsgBox(t('errAddr'));
    store.set(OKEY, info);
    window.open(wa(orderMessage(info)), '_blank', 'noopener');
    openOrder(false);
    toast(t('orderSent'));
  }

  /* ============================================================
     تعديل المنتجات (للأدمن فقط)
     ============================================================ */
  function editMsg(text, kind) {
    const el = $('#editMsg');
    el.className = 'msg' + (text ? ' is-on msg--' + (kind || 'err') : '');
    el.textContent = text || '';
  }

  function editView(id) {
    if (!isAdmin()) return;
    const isNew = !id;
    const src = isNew ? null : byId(id);
    const p = isNew
      ? { id: 'v' + Date.now().toString(36), cat: CATEGORIES[1].id, name: {ar:'',en:''}, desc: {ar:'',en:''}, price: 0, badge: {ar:'',en:''}, img: '' }
      : JSON.parse(JSON.stringify(src));
    const g = (o, k) => (o && typeof o === 'object') ? (o[k] || '') : (k === 'ar' ? (o || '') : '');

    $('#editTitle').textContent = isNew ? t('addTitle') : t('editTitle');
    $('#editSubText').textContent = t('editSub');
    editMsg('');
    $('#editBody').innerHTML = `
      <div class="row2">
        <div class="field"><label>${esc(t('fNameAr'))}</label><input id="f_name_ar" dir="rtl" value="${esc(g(p.name,'ar'))}"></div>
        <div class="field"><label>${esc(t('fNameEn'))}</label><input id="f_name_en" dir="ltr" value="${esc(g(p.name,'en'))}"></div>
      </div>
      <div class="row2">
        <div class="field"><label>${esc(t('fDescAr'))}</label><textarea id="f_desc_ar" dir="rtl">${esc(g(p.desc,'ar'))}</textarea></div>
        <div class="field"><label>${esc(t('fDescEn'))}</label><textarea id="f_desc_en" dir="ltr">${esc(g(p.desc,'en'))}</textarea></div>
      </div>
      <div class="row2">
        <div class="field"><label>${esc(t('fPrice'))} (${esc(cur())})</label><input id="f_price" type="number" min="0" step="1" value="${Number(p.price) || 0}"></div>
        <div class="field"><label>${esc(t('fCat'))}</label><select id="f_cat">
          ${CATEGORIES.filter(c => c.id !== 'all').map(c => `<option value="${c.id}"${c.id === p.cat ? ' selected' : ''}>${esc(tx(c.label))}</option>`).join('')}
        </select></div>
      </div>
      <div class="row2">
        <div class="field"><label>${esc(t('fBadgeAr'))}</label><input id="f_badge_ar" dir="rtl" value="${esc(g(p.badge,'ar'))}"></div>
        <div class="field"><label>${esc(t('fBadgeEn'))}</label><input id="f_badge_en" dir="ltr" value="${esc(g(p.badge,'en'))}"></div>
      </div>
      <div class="field">
        <label>${esc(t('fImage'))}</label>
        <input id="f_img" type="file" accept="image/*">
        <small>${esc(p.img ? t('fImageHas') : t('fImageNew'))}</small>
      </div>
      <div class="row2">
        <button class="btn btn--gold" id="f_save">${esc(t('save'))}</button>
        ${isNew ? '' : `<button class="btn btn--ghost" id="f_del">${esc(t('del'))}</button>`}
      </div>`;

    let newImg = null;
    $('#f_img').onchange = e => {
      const file = e.target.files && e.target.files[0];
      if (!file) return;
      shrink(file, 560).then(d => { newImg = d; editMsg(t('imgReady'), 'ok'); })
                       .catch(() => editMsg(t('imgFail')));
    };

    $('#f_save').onclick = () => {
      const nameAr = $('#f_name_ar').value.trim(), nameEn = $('#f_name_en').value.trim();
      const price = Number($('#f_price').value);
      if (!nameAr && !nameEn) return editMsg(t('errNameReq'));
      if (!(price >= 0)) return editMsg(t('errPrice'));
      const img = newImg || p.img;
      if (!img) return editMsg(t('errImg'));
      const rec = {
        id: p.id, cat: $('#f_cat').value, price, img,
        name: { ar: nameAr || nameEn, en: nameEn || nameAr },
        desc: { ar: $('#f_desc_ar').value.trim(), en: $('#f_desc_en').value.trim() },
        badge: { ar: $('#f_badge_ar').value.trim(), en: $('#f_badge_en').value.trim() }
      };
      const i = PRODUCTS.findIndex(x => x.id === p.id);
      if (i >= 0) PRODUCTS[i] = rec; else PRODUCTS.push(rec);
      if (!saveProducts()) return editMsg(t('errFull'));
      renderGrid(); renderCart(); openEdit(false);
      toast(isNew ? t('savedNew') : t('savedEdit'));
    };

    const del = $('#f_del');
    if (del) del.onclick = () => {
      if (!confirm(t('confirmDel')(tx(p.name)))) return;
      PRODUCTS = PRODUCTS.filter(x => x.id !== p.id);
      delete cart[p.id];
      saveProducts(); saveCart(); renderGrid(); renderCart(); openEdit(false);
      toast(t('deleted'));
    };
  }

  function shrink(file, size) {
    return new Promise((res, rej) => {
      const fr = new FileReader();
      fr.onerror = rej;
      fr.onload = () => {
        const img = new Image();
        img.onerror = rej;
        img.onload = () => {
          const s = Math.min(img.width, img.height);
          const c = document.createElement('canvas');
          c.width = c.height = size;
          c.getContext('2d').drawImage(img, (img.width - s) / 2, (img.height - s) / 2, s, s, 0, 0, size, size);
          res(c.toDataURL('image/jpeg', 0.82));
        };
        img.src = fr.result;
      };
      fr.readAsDataURL(file);
    });
  }

  /* ============================================================
     تطبيق اللغة
     ============================================================ */
  function applyLang() {
    const d = document.documentElement;
    d.setAttribute('lang', lang);
    d.setAttribute('dir', t('dir'));

    $$('[data-t]').forEach(el => {
      const v = t(el.dataset.t);
      if (typeof v !== 'string') return;
      if (el.hasAttribute('data-html')) el.innerHTML = v; else el.textContent = v;
    });
    $$('[data-cat-label]').forEach(a => {
      const c = CATEGORIES.find(x => x.id === a.dataset.cat);
      if (c) a.textContent = tx(c.label);
    });

    $('#langTxt').textContent = t('other');
    $('#langBtn').setAttribute('aria-label', t('otherLabel'));
    $('#cartBtn').setAttribute('aria-label', t('cartAria'));
    $('#cartClose').setAttribute('aria-label', t('close'));
    $('#burger').setAttribute('aria-label', t('menu'));
    $('#cart').setAttribute('aria-label', t('cartAria'));

    [['#ctaWaBtn', 'ctaWa'], ['#askWaBtn', 'askWa'], ['#waLink', 'askWa']].forEach(([sel, key]) => {
      const el = $(sel);
      if (!el) return;
      el.href = wa(t(key)); el.target = '_blank'; el.rel = 'noopener';
    });

    refreshAuthUI();
    renderTabs(); renderGrid(); renderPerks(); renderCart();
    if ($('#authModal').classList.contains('is-on')) authView();
    if ($('#orderModal').classList.contains('is-on')) orderView();
    reveal();
  }

  function toggleLang() {
    lang = lang === 'ar' ? 'en' : 'ar';
    try { localStorage.setItem(LKEY, lang); } catch (e) {}
    applyLang();
  }

  /* ============================================================
     التفاعل العام
     ============================================================ */
  let io;
  function reveal() {
    const items = $$('.rev:not(.is-in):not(.is-wait)');
    if (!('IntersectionObserver' in window)) { items.forEach(i => i.classList.add('is-in')); return; }
    if (!io) io = new IntersectionObserver(en => en.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    }), { rootMargin: '0px 0px -6% 0px', threshold: .05 });
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
    $('#heroLogo').innerHTML = LOGO;
    $('#year').textContent = new Date().getFullYear();
    $('#waShow').textContent = BRAND.whatsappShow;

    applyLang();
    wireNav();

    $('#langBtn').addEventListener('click', toggleLang);

    $('#tabs').addEventListener('click', e => {
      const b = e.target.closest('.tab');
      if (!b) return;
      $$('#tabs .tab').forEach(x => x.classList.toggle('is-on', x === b));
      renderGrid(b.dataset.cat);
    });

    $('#grid').addEventListener('click', e => {
      const a = e.target.closest('[data-add]'), ed = e.target.closest('[data-edit]');
      if (a) add(a.dataset.add, a);
      else if (ed) { editView(ed.dataset.edit); openEdit(true); }
    });

    $('#cartBody').addEventListener('click', e => {
      const inc = e.target.closest('[data-inc]'), dec = e.target.closest('[data-dec]'), del = e.target.closest('[data-del]');
      if (inc) cart[inc.dataset.inc]++;
      else if (dec) { const id = dec.dataset.dec; cart[id]--; if (cart[id] <= 0) delete cart[id]; }
      else if (del) delete cart[del.dataset.del];
      else return;
      saveCart(); renderCart();
    });

    $('#cartBtn').addEventListener('click', () => openCart(true));
    $('#cartClose').addEventListener('click', () => openCart(false));
    $('#checkout').addEventListener('click', () => {
      if (!count()) return;
      openCart(false); orderView(); openOrder(true);
      setTimeout(() => { const f = $('#o_name'); if (f && !f.value) f.focus(); }, 140);
    });
    $('#orderClose').addEventListener('click', () => openOrder(false));

    $('#accBtn').addEventListener('click', () => { pending = null; authView(); openAuth(true); });
    $('#authClose').addEventListener('click', () => openAuth(false));
    $('#editClose').addEventListener('click', () => openEdit(false));
    $('#addProduct').addEventListener('click', () => { editView(null); openEdit(true); });
    $('#resetProducts').addEventListener('click', () => {
      if (!confirm(t('confirmReset'))) return;
      PRODUCTS = JSON.parse(JSON.stringify(DEFAULT_PRODUCTS));
      store.del(PKEY); renderGrid(); renderCart(); toast(t('resetDone'));
    });

    $('#scrim').addEventListener('click', () => { openCart(false); openAuth(false); openEdit(false); openOrder(false); });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') { openCart(false); openAuth(false); openEdit(false); openOrder(false); }
    });

    $$('.ftr__nav [data-cat]').forEach(a => a.addEventListener('click', () => {
      $$('#tabs .tab').forEach(x => x.classList.toggle('is-on', x.dataset.cat === a.dataset.cat));
      renderGrid(a.dataset.cat);
    }));
  });
})();
