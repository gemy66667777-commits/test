/* طبقة التخزين — localStorage */
(function (w) {
  var KEY = "abo3omar.v1", EV = "abo3omar:change";
  var LISTS = ["branches","cats","stats","why","products","offers","gallery","reviews","faq"];
  function clone(o) { return JSON.parse(JSON.stringify(o)); }
  function seed() { return clone(w.ABO_SEED); }

  function read() {
    var db;
    try { db = JSON.parse(localStorage.getItem(KEY)); } catch (e) { db = null; }
    if (!db || typeof db !== "object") db = seed();
    var s = seed();
    db.settings = Object.assign({}, s.settings, db.settings || {});
    for (var i = 0; i < LISTS.length; i++) {
      var k = LISTS[i];
      if (s[k] && (!db[k] || !db[k].length)) db[k] = clone(s[k]);
    }
    if (!Array.isArray(db.orders)) db.orders = [];
    /* ترقية: عروض قديمة بمصفوفة نصوص → {id,q} */
    (db.offers || []).forEach(function (o) {
      o.items = (o.items || []).map(function (it) {
        return typeof it === "string" ? { id: it, q: 1 } : { id: it.id, q: Number(it.q) || 1 };
      });
    });
    return db;
  }
  function write(db) {
    try { localStorage.setItem(KEY, JSON.stringify(db)); }
    catch (e) { try { w.dispatchEvent(new CustomEvent(EV + ":full")); } catch (e2) {} }
    try { w.dispatchEvent(new CustomEvent(EV)); } catch (e) {}
  }
  w.AStore = {
    KEY: KEY, EV: EV,
    get: read,
    set: function (db) { write(db); return db; },
    patch: function (fn) { var db = read(); fn(db); write(db); return db; },
    reset: function () { try { localStorage.removeItem(KEY); } catch (e) {} write(read()); },
    on: function (fn) { w.addEventListener(EV, fn); }
  };
})(window);
