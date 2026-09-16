/* بيانات أبو عمر للأجهزة المنزلية — كل حاجة هنا بتتغيّر من لوحة التحكم */
window.ABO_SEED = {
  settings: {
    brand: "ABO OMAR",
    brandAr: "أبو عمر",
    tagline: "للأجهزة المنزلية",
    slogan: "الجهاز اللي نفسك فيه",
    intro: "كل الماركات العالمية في مكان واحد — إل جي، سامسونج، هيتاشي، شارب، بيكو، ميديا، فريش، تورنيدو، براون. ثلاجات وغسالات وبوتاجازات وأجهزة مطبخ بضمان الوكيل وبالتقسيط.",
    domain: "https://abo3omar.vercel.app",

    phone:  "01003197515",
    whats:  "201003197515",
    whats2: "",

    hours: "يوميًا من ١٠ ص لـ ١١ م",
    ship:  "توصيل وتركيب لكل المحافظات · تقسيط بالبطاقة · ضمان الوكيل",

    adminPass: "123456",
    priceNote: "السعر عند الطلب",
    showPrices: true,
    currency: "ج.م",
    priceHint: "الأسعار بتتغيّر حسب المتاح وسعر الوكيل — أكّدها معانا قبل الحجز.",
    photoNote: "عندنا موديلات وماركات أكتر من اللي على الموقع — ابعتلنا اسم الجهاز وهنبعتلك المتاح بصوره وسعره."
  },

  branches: [
    { id:"b1", name:"فرع القاهرة", addr:"شارع جسر السويس الرئيسي — أول شارع جمال عبد الناصر",
      mapq:"شارع جسر السويس الرئيسي القاهرة" }
  ],

  cats: [
    { id:"cooling", name:"ثلاجات وديب فريزر" },
    { id:"washers", name:"غسالات ملابس" },
    { id:"dish",    name:"غسالات أطباق" },
    { id:"cookers", name:"بوتاجازات وميكروويف" },
    { id:"kitchen", name:"أجهزة مطبخ صغيرة" },
    { id:"home",    name:"أجهزة منزلية" }
  ],

  stats: [
    { n:"٩٦٦ ألف", t:"متابع على فيسبوك" },
    { n:"كل الماركات", t:"في مكان واحد" },
    { n:"ضمان الوكيل", t:"على كل جهاز" },
    { n:"تقسيط", t:"بالبطاقة وبدون فوايد" }
  ],

  why: [
    { n:"كل الماركات تحت سقف واحد", t:"إل جي وسامسونج وهيتاشي وشارب وبيكو وميديا وفريش وتورنيدو — تقارن وتختار من غير ما تلف." },
    { n:"ضمان الوكيل مش ضماننا", t:"كل جهاز بكارت ضمان الشركة المصنّعة، وخدمة ما بعد البيع من الوكيل نفسه." },
    { n:"تقسيط يريّحك", t:"تقسيط بالبطاقة على فترات مختلفة — تاخد الجهاز دلوقتي وتدفع على راحتك." },
    { n:"توصيل وتركيب", t:"بنوصّل لكل المحافظات، والتركيب والتشغيل عندك في البيت." }
  ],

  products: [
    /* ---------- ثلاجات وديب فريزر ---------- */
    { id:"fz-tornado", name:"ديب فريزر تورنيدو ٦ درج — إنفرتر", img:"assets/img/freezer-tornado.jpg", cat:"cooling", price:28000,
      note:"نو فروست · ضمان العربي ١٠ سنين · كفاءة طاقة A" },
    { id:"fz-midea", name:"ديب فريزر ميديا رأسي — إنفرتر", img:"assets/img/freezer-midea.jpg", cat:"cooling", price:26500,
      note:"نو فروست · ضمان جنرال ١٠ سنين · شاشة تحكم خارجية" },
    { id:"fz-fresh", name:"ديب فريزر فريش أسود — ٥ درج", img:"assets/img/freezer-fresh.jpg", cat:"cooling", price:24500,
      note:"ضمان كامل ١٠ سنين · باب زجاج أسود" },
    { id:"fz-drawers", name:"ديب فريزر ٦ درج — درع داخلي", img:"assets/img/freezer-open.jpg", cat:"cooling", price:25500,
      note:"٦ أدراج شفافة بسعة كبيرة · ترموستات قابل للضبط" },
    { id:"fridge-14", name:"ثلاجة نو فروست ١٤ قدم", img:"", cat:"cooling", price:32000,
      note:"متوفرة من إل جي وسامسونج وتورنيدو — اسأل عن المتاح والألوان" },
    { id:"fridge-18", name:"ثلاجة نو فروست ١٨ قدم", img:"", cat:"cooling", price:45000,
      note:"باب مزدوج · موزّع مياه في بعض الموديلات" },

    /* ---------- غسالات ملابس ---------- */
    { id:"wm-lg9", name:"غسالة إل جي ٩ كيلو — دايركت درايف", img:"assets/img/washer-lg.jpg", cat:"washers", price:32000,
      note:"إنفرتر · بخار · ١٤٠٠ لفة · ضمان ١٠ سنين على الموتور" },
    { id:"wm-beko9", name:"غسالة بيكو ٩ كيلو — برو سمارت إنفرتر", img:"assets/img/washer-beko.jpg", cat:"washers", price:29000,
      note:"بخار · ستين إكسبرت · ١٢٠٠ لفة · ضمان ١٠ سنين" },
    { id:"wm-midea10", name:"غسالة ميديا نص أوتوماتيك ١٠ كيلو", img:"assets/img/washer-midea-twin.jpg", cat:"washers", price:12500,
      note:"حوضين · إير فلو ٣٦٠ للتجفيف · مناسبة للكميات الكبيرة" },
    { id:"wm-fresh-twin", name:"غسالة فريش نص أوتوماتيك — حوضين", img:"assets/img/washer-fresh-twin.jpg", cat:"washers", price:10500,
      note:"غسيل وعصر منفصل · تايمر لكل حوض" },
    { id:"wm-fresh-85", name:"غسالة فريش عادية ٨٫٥ كيلو", img:"assets/img/washer-fresh-single.jpg", cat:"washers", price:6500,
      note:"حوض واحد · خفيفة وسهلة النقل · أوفر حاجة في الغسالات" },

    /* ---------- غسالات أطباق ---------- */
    { id:"dw-beko", name:"غسالة أطباق بيكو", img:"assets/img/dish-beko.jpg", cat:"dish", price:28000,
      note:"مصنوعة بمعايير الجودة الأوروبية · برامج متعددة · ضمان الوكيل" },
    { id:"dw-midea", name:"غسالة أطباق ميديا — ١٣ فرد", img:"assets/img/dish-midea.jpg", cat:"dish", price:26000,
      note:"فلتر مضاد للبكتيريا · نص حمولة موفّرة للطاقة · شاشة رقمية" },

    /* ---------- بوتاجازات وميكروويف ---------- */
    { id:"ck-midea", name:"بوتاجاز ميديا ٥ شعلة — إكسبريس جريل", img:"assets/img/cooker-midea.jpg", cat:"cookers", price:22000,
      note:"شواية إنفراريد · توزيع حرارة ٣٦٠ · إشعال ذاتي · ستانلس" },
    { id:"ck-fresh", name:"بوتاجاز فريش هامر ٥ شعلة", img:"assets/img/cooker-fresh.jpg", cat:"cookers", price:24000,
      note:"أسود بالكامل · شاشة رقمية وتايمر · غطاء زجاج" },
    { id:"mw-sharp", name:"ميكروويف شارب رقمي", img:"assets/img/microwave-sharp.jpg", cat:"cookers", price:9500,
      note:"لوحة تاتش · برامج طهي جاهزة · ديفروست أوتوماتيك" },

    /* ---------- أجهزة مطبخ صغيرة ---------- */
    { id:"ch-sokany", name:"كبة سوكاني ١٠٠٠ وات — ٣٫٥ لتر", img:"assets/img/chopper-sokany.jpg", cat:"kitchen", price:3200,
      note:"٦ سكاكين ستانلس · شاشة LCD · موتور نحاس · ضمان سنة" },
    { id:"ch-tornado", name:"كبة الملوخية تورنيدو ٤٠٠ وات", img:"assets/img/chopper-tornado.jpg", cat:"kitchen", price:1900,
      note:"CH-400ML · وعاء زجاج · ضمان العربي" },
    { id:"ch-fresh", name:"كبة فريش ٤٠٠ وات — ١٫٥ لتر", img:"assets/img/chopper-fresh.jpg", cat:"kitchen", price:1750,
      note:"CH-400 · وعاء شفاف بسعة كبيرة · سكاكين ستانلس" },
    { id:"gr-sonai", name:"شواية سوناي هيلثي جريل ١٥٠٠ وات", img:"assets/img/grill-sonai.jpg", cat:"kitchen", price:3500,
      note:"MAR-610 · سطحين شواية ٢×١ · تفلون · ضمان سنتين" },
    { id:"blender", name:"خلاط كهربائي", img:"", cat:"kitchen", price:2200,
      note:"متوفر من تورنيدو وسوكاني وكينوود — اسأل عن الموديلات والقدرات" },

    /* ---------- أجهزة منزلية ---------- */
    { id:"ir-panasonic", name:"مكواة بخار باناسونيك NI-JW650T", img:"assets/img/iron-panasonic.jpg", cat:"home", price:2800,
      note:"قاعدة سيراميك · مضادة للتنقيط والكلس · خزان مياه كبير" },
    { id:"fan-fresh", name:"مروحة فريش عمود", img:"assets/img/fan-fresh.jpg", cat:"home", price:3200,
      note:"٣ ريش · ارتفاع قابل للضبط · ٣ سرعات" },
    { id:"wc-fresh", name:"كولدير مياه فريش — تاتش", img:"assets/img/cooler-fresh.jpg", cat:"home", price:8500,
      note:"بارد وساخن · لوحة تاتش · دولاب تخزين سفلي" },
    { id:"wc-jac", name:"كولدير مياه JAC", img:"assets/img/cooler-jac.jpg", cat:"home", price:7800,
      note:"بارد وساخن وعادي · تصميم مموّج · دولاب سفلي" }
  ],

  /* العروض — items بكميات {id,q}. عدد القطع والسعر قبل العرض بيتحسبوا لوحدهم. */
  offers: [
    { id:"o-bride", name:"عرض جهاز العروسة الكامل", sub:"الأجهزة الكبيرة كلها في مرة واحدة",
      tag:"الأكثر طلبًا", img:"assets/img/offer-bride.jpg", price:106000, feat:true,
      items:[ { id:"fridge-14", q:1 }, { id:"wm-beko9", q:1 }, { id:"ck-midea", q:1 },
              { id:"fz-fresh", q:1 }, { id:"mw-sharp", q:1 } ] },

    { id:"o-kitchen", name:"عرض المطبخ الصغير", sub:"اللي بتحتاجه كل يوم في المطبخ",
      tag:"مقترح", price:16500,
      items:[ { id:"ch-sokany", q:1 }, { id:"gr-sonai", q:1 }, { id:"blender", q:1 }, { id:"mw-sharp", q:1 } ] },

    { id:"o-laundry", name:"عرض الغسيل الكامل", sub:"غسالة ملابس وغسالة أطباق مع بعض",
      tag:"مقترح", price:51500,
      items:[ { id:"wm-beko9", q:1 }, { id:"dw-midea", q:1 } ] },

    { id:"o-summer", name:"عرض الصيف", sub:"تبريد ومية ساقعة",
      tag:"مقترح", price:10800,
      items:[ { id:"fan-fresh", q:1 }, { id:"wc-fresh", q:1 } ] },

    { id:"o-basic", name:"عرض البداية", sub:"أقل تجهيز يكفّي بيت جديد",
      tag:"مقترح", price:54500,
      items:[ { id:"wm-fresh-twin", q:1 }, { id:"ck-fresh", q:1 }, { id:"fz-fresh", q:1 } ] }
  ],

  gallery: [
    { img:"assets/img/freezer-tornado.jpg", cap:"ديب فريزر تورنيدو رأسي بضمان العربي ١٠ سنين" },
    { img:"assets/img/freezer-open.jpg",    cap:"ديب فريزر ٦ درج — من جوه" },
    { img:"assets/img/washer-lg.jpg",       cap:"غسالة إل جي ٩ كيلو دايركت درايف" },
    { img:"assets/img/washer-beko.jpg",     cap:"غسالة بيكو ٩ كيلو برو سمارت إنفرتر" },
    { img:"assets/img/cooker-midea.jpg",    cap:"بوتاجاز ميديا ٥ شعلة ستانلس" },
    { img:"assets/img/cooker-fresh.jpg",    cap:"بوتاجاز فريش هامر ٥ شعلة أسود" },
    { img:"assets/img/dish-midea.jpg",      cap:"غسالة أطباق ميديا ١٣ فرد" },
    { img:"assets/img/dish-beko.jpg",       cap:"غسالة أطباق بيكو بمعايير أوروبية" },
    { img:"assets/img/microwave-sharp.jpg", cap:"ميكروويف شارب رقمي بلوحة تاتش" },
    { img:"assets/img/cooler-fresh.jpg",    cap:"كولدير مياه فريش تاتش" },
    { img:"assets/img/chopper-sokany.jpg",  cap:"كبة سوكاني ١٠٠٠ وات ٣٫٥ لتر" },
    { img:"assets/img/grill-sonai.jpg",     cap:"شواية سوناي هيلثي جريل ٢×١" }
  ],

  reviews: [],

  faq: [
    { q:"المحل فين؟", a:"فرع القاهرة: شارع جسر السويس الرئيسي — أول شارع جمال عبد الناصر. تقدر تفتح الخريطة من الموقع على طول." },
    { q:"الضمان إيه؟", a:"كل جهاز بضمان الوكيل نفسه مش ضماننا، وبكارت ضمان الشركة المصنّعة. خدمة ما بعد البيع من مركز صيانة الوكيل." },
    { q:"بتقسّطوا؟", a:"أيوه، تقسيط بالبطاقة على فترات مختلفة. كلّمنا على واتساب وقولنا الجهاز والفترة اللي تناسبك ونقولك القسط." },
    { q:"بتوصّلوا وبتركّبوا؟", a:"بنوصّل لكل المحافظات، والتركيب والتشغيل عندك في البيت للأجهزة اللي محتاجة تركيب." },
    { q:"لو الموديل اللي عايزه مش على الموقع؟", a:"عندنا موديلات وماركات أكتر بكتير. ابعتلنا اسم الجهاز أو صورته على واتساب وهنقولك المتاح وسعره." },
    { q:"الأسعار دي ثابتة؟", a:"الأسعار بتتغيّر حسب سعر الوكيل والمتاح. اللي على الموقع هو الشغال دلوقتي — أكّده معانا قبل الحجز." }
  ],

  orders: []
};
