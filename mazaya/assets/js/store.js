/* طبقة التخزين — localStorage */
(function (w) {
  var KEY = "mazaya.v1", EV = "mazaya:change";
  function clone(o) { return JSON.parse(JSON.stringify(o)); }
  function seed() { return clone(w.MAZAYA_SEED); }
  function read() {
    var db;
    try { db = JSON.parse(localStorage.getItem(KEY)); } catch (e) { db = null; }
    if (!db || typeof db !== "object") db = seed();
    var s = seed();
    db.settings = Object.assign({}, s.settings, db.settings || {});
    for (var i = 0, k = ["cats","stats","why","products","offers","gallery","faq"]; i < k.length; i++) {
      var key = k[i];
      if (s[key] && (!db[key] || !db[key].length)) db[key] = clone(s[key]);
    }
    if (!Array.isArray(db.orders)) db.orders = [];
    return db;
  }
  function write(db) {
    try { localStorage.setItem(KEY, JSON.stringify(db)); } catch (e) {}
    try { w.dispatchEvent(new CustomEvent(EV)); } catch (e) {}
  }
  w.MStore = {
    KEY: KEY, EV: EV,
    get: read,
    set: function (db) { write(db); return db; },
    patch: function (fn) { var db = read(); fn(db); write(db); return db; },
    reset: function () { try { localStorage.removeItem(KEY); } catch (e) {} write(read()); },
    on: function (fn) { w.addEventListener(EV, fn); }
  };
})(window);
