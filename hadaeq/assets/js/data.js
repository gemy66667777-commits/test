/* بيانات معرض حدائق الزهور للعطور — الدمام | كل شيء هنا يُعدَّل من لوحة التحكم */
window.HZ_SEED = {
  settings: {
    brand: "HADAEQ AL ZOHOUR",
    brandAr: "حدائق الزهور",
    tagline: "معرض العطور",
    slogan: "العطور الحصرية والنادرة",
    intro: "معرض حدائق الزهور للعطور — نيش وحصري وكلاسيكيات نادرة من ديبتيك ولاليك وبولغاري وأتيليه دي زور ونيكولاي ومَجلر وشانيل. أصلية ١٠٠٪، وتوصيل وشحن يومي لكل مناطق المملكة.",
    domain: "https://hadaeq-alzohour.vercel.app",

    phone:  "0556002024",
    whats:  "966556002024",
    whats2: "",
    snap:   "sameh1241",

    hours: "يومياً من ٤ العصر حتى ١٢ منتصف الليل",
    ship:  "توصيل وشحن يومي لكل مناطق المملكة · استلام من المعرض · تغليف هدايا",

    adminPass: "123456",
    priceNote: "السعر عند الطلب",
    showPrices: true,
    currency: "ر.س",
    priceHint: "الأسعار تتغيّر حسب المتوفر والتشكيلة — تأكّدوا منها معنا قبل الحجز.",
    photoNote: "المعرض فيه تشكيلة أوسع بكثير مما هو معروض هنا — أرسلوا لنا اسم العطر وبنرسل لكم المتوفر بصوره وسعره."
  },

  branches: [
    { id:"b1", name:"المعرض", addr:"الدمام — سوق الجملة، زاوية مجمع المعجل التجاري",
      mapq:"مجمع المعجل التجاري سوق الجملة الدمام" }
  ],

  cats: [
    { id:"niche",   name:"نيش وحصري" },
    { id:"classic", name:"كلاسيكيات ونوادر" },
    { id:"women",   name:"نسائي" },
    { id:"care",    name:"بودرة وعناية" }
  ],

  stats: [
    { n:"أصلي ١٠٠٪", t:"لا نبيع إلا الأصلي" },
    { n:"نيش ونادر", t:"ماركات ما تلقاها بسهولة" },
    { n:"شحن يومي", t:"لكل مناطق المملكة" },
    { n:"الدمام",   t:"سوق الجملة" }
  ],

  why: [
    { n:"أصلية بضمان المعرض", t:"كل زجاجة أصلية بختمها، ولو طلعت غير ذلك نستردّها كاملة." },
    { n:"نيش ونوادر", t:"ديبتيك ولاليك وأتيليه دي زور ونيكولاي وبولغاري لي جيم — تشكيلة ما تلقاها في كل مكان." },
    { n:"نخدمك بالتوصية", t:"قل لنا ذوقك والمناسبة والوقت، ونرشّح لك العطر المناسب قبل ما تدفع ريال." },
    { n:"شحن يومي", t:"نشحن يومياً لكل مناطق المملكة، وتقدر تستلم من المعرض مباشرة." }
  ],

  products: [
    /* ---------- نيش وحصري ---------- */
    { id:"bvlgari-kobraa", name:"بولغاري لي جيم — كوبرا ١٠٠ مل", img:"assets/img/bvlgari-kobraa.jpg", cat:"niche", price:1450,
      note:"Bvlgari Le Gemme Kobraa · أو دو بارفان · عود وتوابل شرقية فخمة" },
    { id:"lelabo-santal", name:"لو لابو — سانتال ٣٣، ١٠٠ مل", img:"assets/img/lelabo-santal.jpg", cat:"niche", price:1350,
      note:"Le Labo Santal 33 · خشب صندل وجلد ودخان · من أشهر عطور النيش" },
    { id:"bottega-azalea", name:"بوتيغا فينيتا — باركو بالاديانو ٤ أزاليا", img:"assets/img/bottega-azalea.jpg", cat:"niche", price:1200,
      note:"Parco Palladiano IV Azalea · زهري أخضر راقٍ · إصدار محدود" },
    { id:"marly", name:"بارفان دو مارلي — الأزرق", img:"assets/img/marly.jpg", cat:"niche", price:1100,
      note:"Parfums de Marly · ثبات عالي وفوحان قوي · رجالي فاخر" },
    { id:"chanel-eaux", name:"شانيل لي زو — باريس فينيسيا / باريس باريس", img:"assets/img/chanel-eaux.jpg", cat:"niche", price:950,
      note:"Chanel Les Eaux de Chanel · خفيف وأنيق للاستخدام اليومي · للجنسين" },
    { id:"ysl-caban", name:"إيف سان لوران — كابان (لو فيستيير)", img:"assets/img/ysl-caban.jpg", cat:"niche", price:950,
      note:"YSL Le Vestiaire Caban · فلفل وورد وتونكا · للجنسين" },
    { id:"atelier-des-ors", name:"أتيليه دي زور — تشكيلة لودوريه", img:"assets/img/atelier-des-ors.jpg", cat:"niche", price:900,
      note:"Atelier des Ors · لون فيلين، روج سراي، روز أميّة · رقائق ذهب داخل الزجاجة" },
    { id:"grossmith-amelia", name:"غروسميث — أميليا", img:"assets/img/grossmith-amelia.jpg", cat:"niche", price:890,
      note:"Grossmith Amelia · زهري وردي منعش بقاعدة خشبية · نسائي بريطاني" },
    { id:"nicolai", name:"نيكولاي — إنتنس كوليكشن", img:"assets/img/nicolai.jpg", cat:"niche", price:850,
      note:"Nicolaï · بايكال ليذر، كوير كوبا، باتشولي إنتنس · ١٠٠ مل" },
    { id:"diptyque-orpheon", name:"ديبتيك — أورفيون ٧٥ مل", img:"assets/img/diptyque-orpheon.jpg", cat:"niche", price:820,
      note:"Diptyque Orphéon · إيريس وخشب الأرز وتبغ · هادئ وراقٍ" },
    { id:"diptyque-nabati", name:"ديبتيك — أو نباتي", img:"assets/img/diptyque-nabati.jpg", cat:"niche", price:780,
      note:"Diptyque Eau Nabati · إصدار الشرق الأوسط · عود وورد" },
    { id:"lalique-noir", name:"لاليك — نوار بريميير كوليكشن", img:"assets/img/lalique-noir.jpg", cat:"niche", price:780,
      note:"Lalique Noir Premier · أور آنتمبوريل، روز رويال، فلور أونيفرسيل · تشكيلة كاملة" },
    { id:"mugler-fougere", name:"مَجلر لي زكسبسيون — فوجير فوريوز", img:"assets/img/mugler-fougere.jpg", cat:"niche", price:750,
      note:"Mugler Les Exceptions · لافندر وطحلب البلوط · نادر ومميز" },

    /* ---------- كلاسيكيات ونوادر ---------- */
    { id:"hermes-caleche", name:"هيرمس — كاليش سوا دو بارفان", img:"assets/img/hermes-caleche.jpg", cat:"classic", price:550,
      note:"Hermès Calèche · عطر كلاسيكي نسائي · من العطور القديمة الجميلة" },
    { id:"ysl-supreme", name:"إيف سان لوران — سوبريم بوكيه", img:"assets/img/ysl-supreme.jpg", cat:"classic", price:650,
      note:"YSL Supreme Bouquet · تيوبروز وإيلانغ إيلانغ · متوفر كذلك سوبريم شير" },
    { id:"gucci-guilty", name:"غوتشي — غيلتي أبسولوت", img:"assets/img/gucci-guilty.jpg", cat:"classic", price:480,
      note:"Gucci Guilty Absolute · جلد وباتشولي · متوفر كذلك أنجيلينا هاليغونز" },
    { id:"boucheron", name:"بوشرون — أو دو بارفان (الإصدار القديم)", img:"assets/img/boucheron.jpg", cat:"classic", price:420,
      note:"Boucheron EDP · من أجمل العطور القديمة · زجاجة الخاتم الشهيرة" },
    { id:"sirocco", name:"سيروكو — مون كوليكشن", img:"assets/img/sirocco.jpg", cat:"classic", price:350,
      note:"Sirocco Lovers Moon · ١٠٠ مل · عطر شرقي فخم بسعر معقول" },

    /* ---------- نسائي ---------- */
    { id:"loccitane", name:"لوكسيتان — نيرولي وأوركيدية", img:"assets/img/loccitane.jpg", cat:"women", price:180,
      note:"L'Occitane Néroli & Orchidée · أو دو تواليت · نسائي صباحي منعش" },

    /* ---------- بودرة وعناية ---------- */
    { id:"franck-powder", name:"فرانك أوليفر — بودرة جسم ٢٠٠ جم", img:"assets/img/franck-powder.jpg", cat:"care", price:130,
      note:"Franck Olivier Dusting Powder · بودرة معطّرة للجسم · باريس" },
    { id:"gift-box", name:"بوكس هدايا مجمّع", img:"", cat:"care", price:0,
      note:"نجهّز لك بوكس هدية بعطر أو أكثر مع التغليف — كلّمنا وقل لنا الميزانية" }
  ],

  /* الباقات — تُعدَّل بالكامل من اللوحة */
  offers: [
    { id:"o-niche3", name:"باقة النيش الثلاثية", sub:"ثلاثة من أقوى عطور النيش عندنا",
      tag:"الأكثر طلباً", price:2650, feat:true,
      items:[ { id:"lelabo-santal", q:1 }, { id:"diptyque-orpheon", q:1 }, { id:"mugler-fougere", q:1 } ] },

    { id:"o-classic", name:"باقة الكلاسيكيات", sub:"العطور القديمة الجميلة في مجموعة واحدة",
      tag:"مقترحة", price:1250,
      items:[ { id:"hermes-caleche", q:1 }, { id:"boucheron", q:1 }, { id:"sirocco", q:1 } ] },

    { id:"o-her", name:"باقة الإهداء النسائية", sub:"عطر وبودرة جسم مع التغليف",
      tag:"مقترحة", price:640,
      items:[ { id:"hermes-caleche", q:1 }, { id:"franck-powder", q:1 } ] },

    { id:"o-daily", name:"باقة اليومي", sub:"منعش للنهار وثقيل للمساء",
      tag:"مقترحة", price:1050,
      items:[ { id:"loccitane", q:1 }, { id:"chanel-eaux", q:1 } ] }
  ],

  gallery: [
    { img:"assets/img/store-front.jpg",      cap:"معرض حدائق الزهور — سوق الجملة، الدمام" },
    { img:"assets/img/store-shelves.jpg",    cap:"من داخل المعرض — تشكيلة العطور والمكياج" },
    { img:"assets/img/bvlgari-kobraa.jpg",   cap:"بولغاري لي جيم كوبرا" },
    { img:"assets/img/lalique-noir.jpg",     cap:"لاليك نوار بريميير — التشكيلة الكاملة" },
    { img:"assets/img/atelier-des-ors.jpg",  cap:"أتيليه دي زور — تشكيلة لودوريه" },
    { img:"assets/img/nicolai.jpg",          cap:"نيكولاي إنتنس كوليكشن" },
    { img:"assets/img/chanel-eaux.jpg",      cap:"شانيل لي زو — باريس فينيسيا وباريس باريس" },
    { img:"assets/img/diptyque-orpheon.jpg", cap:"ديبتيك أورفيون ٧٥ مل" },
    { img:"assets/img/diptyque-nabati.jpg",  cap:"ديبتيك أو نباتي" },
    { img:"assets/img/marly.jpg",            cap:"بارفان دو مارلي" },
    { img:"assets/img/mugler-fougere.jpg",   cap:"مَجلر فوجير فوريوز" },
    { img:"assets/img/lelabo-santal.jpg",    cap:"لو لابو سانتال ٣٣" },
    { img:"assets/img/ysl-supreme.jpg",      cap:"إيف سان لوران سوبريم بوكيه وشير" },
    { img:"assets/img/gucci-guilty.jpg",     cap:"غوتشي غيلتي أبسولوت" },
    { img:"assets/img/sirocco.jpg",          cap:"سيروكو مون كوليكشن" },
    { img:"assets/img/grossmith-amelia.jpg", cap:"غروسميث أميليا" }
  ],

  reviews: [],

  faq: [
    { q:"وين المعرض؟", a:"الدمام — سوق الجملة، زاوية مجمع المعجل التجاري. تقدر تفتح الخريطة من الموقع مباشرة." },
    { q:"العطور أصلية؟", a:"كل ما نبيعه أصلي بختمه. ولو طلع غير ذلك نستردّه ونرجّع المبلغ كاملاً." },
    { q:"تشحنون لبقية المناطق؟", a:"نعم، نشحن يومياً لكل مناطق المملكة. وتقدر تستلم من المعرض مباشرة." },
    { q:"ما أعرف أختار — تساعدوني؟", a:"أكيد. أرسل لنا على الواتساب ذوقك والمناسبة (دوام، مناسبة، صيف، شتاء) والميزانية، ونرشّح لك المناسب قبل ما تدفع." },
    { q:"العطر اللي أبيه مو موجود بالموقع؟", a:"المعرض فيه تشكيلة أوسع بكثير. أرسل لنا اسم العطر أو صورته وبنقول لك المتوفر وسعره." },
    { q:"تسوّون تغليف هدايا؟", a:"نعم، وبنجهّز لك بوكس هدية بعطر أو أكثر حسب ميزانيتك." },
    { q:"الأسعار ثابتة؟", a:"الأسعار تتغيّر حسب المتوفر والتشكيلة. اللي بالموقع هو الشغّال حالياً — تأكّد منه معنا قبل الحجز." }
  ],

  orders: []
};
