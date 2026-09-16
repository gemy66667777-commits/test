/* بيانات فيستا إيفينت — كل حاجة هنا بتتغير من لوحة التحكم */
window.VISTA_SEED = {
  settings: {
    brand: "VISTA",
    brandAr: "فيستا إيفينت",
    tagline: "EVENTS & DECOR",
    intro: "كوش خطوبة وكتب كتاب وتنسيق حفلات. ستاير وشيفون وورد وشمعدانات وإضاءة بألوانها — نجهّزلك المكان من الألف للياء.",
    phone: "01500095042",
    whats: "201500095042",
    hours: "الرد يوميًا من ١١ ص لـ ١٢ بالليل",
    area: "بنجهّز في البيت والقاعات والحدائق",
    adminPass: "123456",
    priceNote: "السعر عند الطلب",
    showPrices: false,
    currency: "ج.م",
    priceHint: "السعر بيتحدد على حسب المساحة وعدد الشمعدانات والورد والإضاءة — ابعتلنا التفاصيل ويوصلك السعر حالًا."
  },
  shapes: [
    { id:"round", name:"دائرية", note:"حلقة ورد كاملة ورا الكوشة" },
    { id:"cross", name:"متقاطعة", note:"ستاير متقاطعة على شكل X" },
    { id:"drape", name:"منسدلة", note:"ستارة سادة أو بسحبة جانبية" }
  ],
  lights: [
    { id:"blue",   name:"أزرق",    css:"#5FC8E8" },
    { id:"green",  name:"أخضر",    css:"#57D08F" },
    { id:"purple", name:"بنفسجي",  css:"#A68CE8" },
    { id:"warm",   name:"دافي",    css:"#F2C87A" }
  ],
  flowers: [
    { id:"white", name:"ورد أبيض" },
    { id:"none",  name:"من غير ورد" }
  ],
  stats: [
    { n:"كوش خطوبة", t:"وكتب كتاب" },
    { n:"٤ ألوان", t:"إضاءة تختار منها" },
    { n:"بيت وقاعة", t:"وحدايق مفتوحة" },
    { n:"تجهيز كامل", t:"ستاير وورد وشمع ونيون" }
  ],
  services: [
    { ic:"arch",   n:"كوش خطوبة وكتب كتاب",  t:"كوشة دائرية أو متقاطعة أو ستارة منسدلة، بورد وشمعدانات." },
    { ic:"bulb",   n:"إضاءة ملوّنة",          t:"أزرق أو أخضر أو بنفسجي أو دافي — اللون اللي يناسب لبس العروسة." },
    { ic:"neon",   n:"كلمات نيون وأسماء ذهبي", t:"«وجعل بينكم مودة ورحمة» أو اسم العروسين بحرف ذهبي." },
    { ic:"flower", n:"ورد وشمعدانات",         t:"أعمدة ورد أبيض وشمعدانات دهبي على جانبين الكوشة." },
    { ic:"tree",   n:"تنسيق حدائق وحفلات خارجية", t:"ترابيزات وكراسي دهبي ولمبات معلّقة ونجف على الشجر." },
    { ic:"seat",   n:"كنبة العروسين",          t:"كنبة كابتونيه بقاعدة دهبي، جزء من التجهيز." }
  ],
  packages: [
    { id:"p-round", name:"كوشة دائرية", img:"assets/img/g-arch-blue.jpg", price:0,
      items:["حلقة ورد أبيض كاملة","ستارة شيفون خلفية","إضاءة باللون اللي تختاره","كنبة العروسين","كلمة نيون"] },
    { id:"p-cross", name:"كوشة ستاير متقاطعة", img:"assets/img/g-blue-cross.jpg", price:0,
      items:["ستاير متقاطعة على شكل X","شمعدانات على الجانبين","عمودين ورد أبيض","إضاءة باللون اللي تختاره","كنبة العروسين"] },
    { id:"p-drape", name:"كوشة ستارة منسدلة", img:"assets/img/g-strips.jpg", price:0,
      items:["ستارة بيضا بسحبة","شرايط لمبات على الستارة","عمودين ورد أبيض","اسم أو كلمة ذهبي","كنبة العروسين"] }
  ],
  gallery: [
    { img:"assets/img/g-arch-blue.jpg",   cap:"كوشة دائرية بورد أبيض وإضاءة زرقا",            shape:"round", light:"blue",   fl:"white" },
    { img:"assets/img/g-arch-round.jpg",  cap:"كوشة دائرية بورد أبيض وكلمة نيون ذهبي",        shape:"round", light:"blue",   fl:"white" },
    { img:"assets/img/g-arch-blue2.jpg",  cap:"كوشة دائرية بورد أبيض وشيفون أزرق في النص",     shape:"round", light:"blue",   fl:"white" },
    { img:"assets/img/g-blue-cross.jpg",  cap:"ستاير متقاطعة بإضاءة زرقا وشمعدانات",          shape:"cross", light:"blue",   fl:"white" },
    { img:"assets/img/g-green.jpg",       cap:"ستاير متقاطعة بإضاءة خضرا وشمعدانات",           shape:"cross", light:"green",  fl:"white" },
    { img:"assets/img/g-purple.jpg",      cap:"ستاير متقاطعة بإضاءة بنفسجي وشمعدانات",         shape:"cross", light:"purple", fl:"white" },
    { img:"assets/img/g-warm-x.jpg",      cap:"ستاير متقاطعة بإضاءة دافية وحرف ذهبي",          shape:"cross", light:"warm",   fl:"white" },
    { img:"assets/img/g-warm-cross.jpg",  cap:"ستاير متقاطعة بشمعدانات وعمودين ورد أبيض",      shape:"cross", light:"warm",   fl:"white" },
    { img:"assets/img/g-candles.jpg",     cap:"ستارة بيضا بشمعدانات دهبي وورد أبيض",           shape:"cross", light:"warm",   fl:"white" },
    { img:"assets/img/g-ve.jpg",          cap:"ستاير بشمعدانات وورد أبيض وسجاد أحمر",          shape:"cross", light:"warm",   fl:"white" },
    { img:"assets/img/g-swag.jpg",        cap:"ستارة منسدلة بسحبة وإضاءة زرقا وحرف ذهبي",      shape:"drape", light:"blue",   fl:"none"  },
    { img:"assets/img/g-gold-name.jpg",   cap:"ستارة بكرات بيضا وحرف ذهبي وعمودين ورد",        shape:"drape", light:"warm",   fl:"white" },
    { img:"assets/img/g-pom.jpg",         cap:"ستارة بكرات بيضا وشمعدانات وورد أبيض",          shape:"drape", light:"warm",   fl:"white" },
    { img:"assets/img/g-strips.jpg",      cap:"ستارة بشرايط لمبات وعمودين ورد أبيض",           shape:"drape", light:"warm",   fl:"white" },
    { img:"assets/img/g-garden.jpg",      cap:"تنسيق حديقة بترابيزات وكراسي دهبي ولمبات معلقة", shape:"drape", light:"warm",   fl:"none"  }
  ],
  faq: [
    { q:"بتشتغلوا في البيت ولا القاعات بس؟", a:"الاتنين. بنجهّز في الشقق والقاعات وكمان الحدايق والحفلات المفتوحة." },
    { q:"أقدر أختار لون الإضاءة؟", a:"أيوه. عندنا أزرق وأخضر وبنفسجي ودافي، وتقدر تشوف كل لون على الطبيعة من «صمّم كوشتك» في الموقع." },
    { q:"الكوشة بتشمل إيه؟", a:"الستاير والورد والشمعدانات والإضاءة وكنبة العروسين. الكلمة النيون والأسماء الذهبي بتتضاف حسب طلبك." },
    { q:"بتحجزوا قبل بكام؟", a:"كل ما تحجز بدري كل ما كان أفضل، خصوصًا في مواسم الأفراح. ابعتلنا التاريخ ونقولك متاح ولا لأ." },
    { q:"ليه الأسعار مش مكتوبة؟", a:"السعر بيختلف حسب المساحة وعدد الشمعدانات والورد. اختار شكلك من الموقع وابعته، ويوصلك السعر على واتساب." }
  ],
  bookings: []
};
