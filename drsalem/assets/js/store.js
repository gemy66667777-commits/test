/* طبقة التخزين — localStorage */
(function (w) {
  var KEY = "drsalem.v1", EV = "drsalem:change";
  var LISTS = ["days","slots","stats","procs","visits","steps","why","branches","reviews","faq"];
  function clone(o) { return JSON.parse(JSON.stringify(o)); }
  function seed() { return clone(w.DS_SEED); }

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
    if (!Array.isArray(db.bookings)) db.bookings = [];
    return db;
  }
  function write(db) {
    try { localStorage.setItem(KEY, JSON.stringify(db)); }
    catch (e) { try { w.dispatchEvent(new CustomEvent(EV + ":full")); } catch (e2) {} }
    try { w.dispatchEvent(new CustomEvent(EV)); } catch (e) {}
  }
  w.DStore = {
    KEY: KEY, EV: EV,
    get: read,
    set: function (db) { write(db); return db; },
    patch: function (fn) { var db = read(); fn(db); write(db); return db; },
    reset: function () { try { localStorage.removeItem(KEY); } catch (e) {} write(read()); },
    on: function (fn) { w.addEventListener(EV, fn); }
  };
})(window);
