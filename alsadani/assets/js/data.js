/* بيانات مول السعدني للمفروشات — كل حاجة هنا بتتغيّر من لوحة التحكم */
window.SADANI_SEED = {
  settings: {
    brand: "ALSADANI MALL",
    brandAr: "مول السعدني",
    tagline: "للمفروشات",
    slogan: "احنا على قد ايدك",
    intro: "فوط وملايات وبطاطين ودفايات ولحف وكوفرتات وبرانس — أجود الخامات بأسعار الجملة. وبنجهّز جهاز العروسة كامل من مكان واحد.",
    domain: "https://alsadani-mafroshat.vercel.app",

    phone:  "01097730579",
    whats:  "201015908083",
    whats2: "201037578176",

    hours: "يوميًا من ١٠ ص لـ ١١ م",
    ship:  "شحن لكل المحافظات · استلام من الفرع · حجز مسبق للتجهيز",

    adminPass: "123456",
    priceNote: "السعر عند الطلب",
    showPrices: true,
    currency: "ج.م",
    priceHint: "الأسعار تقريبية وبتتغيّر حسب المتاح — أكّدها معانا قبل الحجز.",
    photoNote: "مش كل الأصناف متصوّرة — اطلب صور أي صنف على واتساب وهنبعتهالك."
  },

  /* الفروع — تطوير عن فرع واحد */
  branches: [
    { id:"b1", name:"الفرع الأول", addr:"طريق المحلة طنطا — بجوار قرية المريلاند",
      mapq:"طريق المحلة طنطا قرية المريلاند" },
    { id:"b2", name:"الفرع الثاني", addr:"الشون — أمام قسم تاني",
      mapq:"الشون طنطا قسم تاني" }
  ],

  cats: [
    { id:"beds",     name:"أطقم سرير ومفارش" },
    { id:"blankets", name:"بطاطين ودفايات" },
    { id:"quilts",   name:"لحف وكوفرتات" },
    { id:"towels",   name:"فوط وبرانس" }
  ],

  stats: [
    { n:"فرعين",      t:"في طنطا" },
    { n:"جملة وقطاعي", t:"بنفس السعر" },
    { n:"٤ أقسام",    t:"تحت سقف واحد" },
    { n:"كل مصر",     t:"بنشحن لأي محافظة" }
  ],

  why: [
    { n:"أسعار الجملة للكل", t:"مش لازم تشتري كمية عشان تاخد سعر جملة. احنا على قد ايدك." },
    { n:"الخامة زي ما بنقول", t:"بنجرّب الصنف قبل ما يدخل المحل، وبنوصفه لك زي ما هو بالظبط." },
    { n:"بنجهّز الجهاز كامل", t:"من الملاية للفوطة للدفاية — قايمة واحدة وسعر واحد ومن غير لف." },
    { n:"بنشحن لكل المحافظات", t:"اطلب وانت في بيتك، أو عدّي على أي فرع وشوف بنفسك." }
  ],

  /* المنتجات — اللي من غير img بيظهر برسمة بديلة مكتوب عليها «الصورة قريبًا» */
  products: [
    { id:"bed-big",      name:"طقم سرير كبير مبطّن",              img:"",                              cat:"beds",     price:1800, note:"طقم ٢×٢ مبطّن بالكامل — ألوان وتصميمات كتير في الفرع" },
    { id:"bed-kid-blue", name:"طقم سرير أطفال مخمل TAG — لبني",  img:"assets/img/tag-kids-blue.jpg",  cat:"beds",     price:1450, note:"٤ قطع: لحاف مخمل ٢٠٠×٢٤٠ + ٢ مخدة ٥٨×٧٠ — تطريز دباديب" },
    { id:"bed-kid-olive",name:"طقم سرير أطفال مخمل TAG — زيتي",  img:"assets/img/tag-kids-olive.jpg", cat:"beds",     price:1450, note:"٤ قطع بنفس المقاسات بدرجة هادية" },
    { id:"merva",        name:"مفرش مرفا — دريم هاوس",            img:"assets/img/merva.jpg",          cat:"beds",     price:2200, note:"مفرش مبطّن بتطريز هندسي — ٦ ألوان" },
    { id:"green-beige",  name:"طقم ملايات Green — بيج مورّد",     img:"assets/img/green-beige.jpg",    cat:"beds",     price:950,  note:"٤ قطع قطن: ملاية ٢٤٠×٢٨٠ + مخدة ٥٥×٧٠ + كيس ٤٥×١٨٠" },
    { id:"green-white",  name:"طقم ملايات Green — أبيض مورّد",    img:"assets/img/green-white.jpg",    cat:"beds",     price:950,  note:"٤ قطع قطن بنفس المقاسات بورد كلاسيك" },
    { id:"fitted",       name:"ملاية مخمل بالاستيك",              img:"assets/img/velvet-fitted.jpg",  cat:"beds",     price:700,  note:"فيتد بالاستيك حوالين السرير + ٢ كيس مخدة — مش بتتزحلق" },

    { id:"heater-big",   name:"دفاية تركي كبيرة",                 img:"",                              cat:"blankets", price:1650, note:"مقاس ٢×٢٤٠ — وبر ناعم تقيل ما بيتساقطش" },
    { id:"heater-kid",   name:"دفاية أطفال",                      img:"",                              cat:"blankets", price:850,  note:"مقاس سرير الأطفال — نفس خامة الكبير" },
    { id:"blanket-big",  name:"بطانية مخمل كبيرة",                img:"",                              cat:"blankets", price:1150, note:"مخمل خفيف — تنفع للسرير أو الأنتريه" },
    { id:"blanket-kid",  name:"بطانية أطفال",                     img:"",                              cat:"blankets", price:750,  note:"مخمل برسومات كارتون" },

    { id:"quilt-big",    name:"لحاف كبير",                        img:"",                              cat:"quilts",   price:900,  note:"حشو مناسب للجو المعتدل — ألوان متعددة" },
    { id:"quilt-kid",    name:"لحاف أطفال",                       img:"",                              cat:"quilts",   price:600,  note:"مقاس سرير الأطفال" },
    { id:"cover-big",    name:"كوفرتة كبيرة",                     img:"",                              cat:"quilts",   price:1250, note:"مبطّنة ٢×٢٤٠ — صيف وشتا وسهلة الغسيل" },
    { id:"cover-kid",    name:"كوفرتة أطفال",                     img:"",                              cat:"quilts",   price:800,  note:"مبطّنة بمقاس سرير الأطفال" },

    { id:"towel-big",    name:"فوطة كبيرة",                       img:"",                              cat:"towels",   price:180,  note:"قطن بوزن عالي — سادة ومطبوعة" },
    { id:"towel-bath",   name:"فوطة حمام",                        img:"",                              cat:"towels",   price:140,  note:"قطن ماص سريع النشاف" },
    { id:"towel-kid",    name:"فوطة أطفال",                       img:"",                              cat:"towels",   price:90,   note:"قطن ناعم برسومات" },
    { id:"towel-kitchen",name:"فوطة مطبخ",                        img:"",                              cat:"towels",   price:45,   note:"قطن ماص — ألوان متنوعة" },
    { id:"towel-table",  name:"فوطة سفرة",                        img:"",                              cat:"towels",   price:55,   note:"مطرّزة — تليق على ترابيزة الضيوف" },
    { id:"burnus",       name:"بورنس دابل",                       img:"",                              cat:"towels",   price:650,  note:"قطن دابل بقلنسوة وجيوب — مقاس واسع" }
  ],

  /* العروض — items بكميات {id,q}. عدد القطع والسعر قبل العرض بيتحسبوا لوحدهم.
     was: سعر قبل العرض يدوي (لو موجود بيغلب المحسوب) — زي المكتوب على البوستر.
     pieces: عدد قطع يدوي (لو موجود بيغلب المحسوب). */
  offers: [
    { id:"o-mawlid2", name:"عرض المولد ٢", sub:"جهاز عروسة كامل — العرض الرسمي",
      tag:"العرض الرسمي", img:"assets/img/offer-mawlid.jpg", price:15000, was:20000, feat:true,
      items:[
        { id:"burnus", q:1 },
        { id:"towel-big", q:12 }, { id:"towel-kid", q:4 }, { id:"towel-bath", q:12 },
        { id:"towel-kitchen", q:12 }, { id:"towel-table", q:6 },
        { id:"bed-big", q:7 }, { id:"bed-kid-blue", q:3 },
        { id:"heater-big", q:2 }, { id:"heater-kid", q:1 },
        { id:"blanket-big", q:1 }, { id:"blanket-kid", q:1 },
        { id:"quilt-big", q:1 }, { id:"quilt-kid", q:1 },
        { id:"cover-big", q:1 }, { id:"cover-kid", q:1 }
      ] },

    { id:"o-eco", name:"جهاز العروسة الاقتصادي", sub:"البداية المظبوطة بأقل ميزانية",
      tag:"مقترح", price:8500, items:[
        { id:"bed-big", q:3 }, { id:"bed-kid-blue", q:1 },
        { id:"towel-big", q:6 }, { id:"towel-bath", q:4 },
        { id:"heater-big", q:1 }, { id:"blanket-big", q:1 },
        { id:"quilt-big", q:1 }, { id:"cover-big", q:1 }
      ] },

    { id:"o-winter", name:"عرض الشتا", sub:"دفا البيت كله في باكدچ واحدة",
      tag:"مقترح", price:4200, items:[
        { id:"heater-big", q:2 }, { id:"blanket-big", q:2 },
        { id:"blanket-kid", q:1 }, { id:"quilt-big", q:1 }
      ] },

    { id:"o-towels", name:"عرض الفوط الكامل", sub:"٢٤ فوطة تكفّي البيت سنة",
      tag:"مقترح", price:1900, items:[
        { id:"towel-big", q:6 }, { id:"towel-bath", q:6 },
        { id:"towel-kitchen", q:6 }, { id:"towel-table", q:6 }
      ] },

    { id:"o-beds", name:"عرض المفارش", sub:"تغيير كامل لغرف البيت",
      tag:"مقترح", price:4900, items:[
        { id:"merva", q:1 }, { id:"green-beige", q:1 },
        { id:"green-white", q:1 }, { id:"fitted", q:2 }
      ] }
  ],

  gallery: [
    { img:"assets/img/offer-mawlid.jpg",   cap:"عرض المولد ٢ — جهاز عروسة ٣١ قطعة" },
    { img:"assets/img/wholesale.jpg",      cap:"أوردر متجهّز ومترتب قبل الشحن" },
    { img:"assets/img/store-1.jpg",        cap:"من جوه المحل — قسم البطاطين والدفايات" },
    { img:"assets/img/store-2.jpg",        cap:"من جوه المحل — قسم الملايات والمفارش" },
    { img:"assets/img/merva.jpg",          cap:"مفرش مرفا دريم هاوس — ٦ ألوان" },
    { img:"assets/img/tag-kids-blue.jpg",  cap:"طقم سرير أطفال مخمل TAG لبني" },
    { img:"assets/img/tag-kids-olive.jpg", cap:"طقم سرير أطفال مخمل TAG زيتي" },
    { img:"assets/img/green-beige.jpg",    cap:"طقم ملايات Green بيج مورّد" },
    { img:"assets/img/green-white.jpg",    cap:"طقم ملايات Green أبيض مورّد" },
    { img:"assets/img/velvet-fitted.jpg",  cap:"ملاية مخمل بالاستيك" }
  ],

  /* آراء العملاء — سكرين شوت من واتساب (مش موجودة في مزايا) */
  reviews: [
    { img:"assets/img/wa-1.jpg", cap:"الحاجات ما شاء الله تحفة وخامة جميلة" },
    { img:"assets/img/wa-3.jpg", cap:"الأوردر وصل وكل حاجة فيه جميلة" },
    { img:"assets/img/wa-2.jpg", cap:"الأوردر وصل حالًا وكل حاجة فيه جميلة جدًا" },
    { img:"assets/img/wa-4.jpg", cap:"الحاجة وصلت ما شاء الله زي الفل" }
  ],

  faq: [
    { q:"الفروع فين؟", a:"عندنا فرعين في طنطا: الأول على طريق المحلة طنطا بجوار قرية المريلاند، والتاني في الشون أمام قسم تاني. تقدر تفتح الخريطة من الموقع على طول." },
    { q:"بتشحنوا لبرّه طنطا؟", a:"أيوه، بنشحن لكل المحافظات. وتقدر كمان تعدّي على أي فرع وتشوف بنفسك أو تحجز المنتج لحد ما تيجي." },
    { q:"ليه مش كل المنتجات متصوّرة؟", a:"الأصناف عندنا أكتر بكتير من اللي على الموقع والألوان بتتغيّر باستمرار. ابعتلنا على واتساب اسم الصنف وهنبعتلك صور وفيديو للمتاح دلوقتي." },
    { q:"أقدر أظبط العرض على ميزانيتي؟", a:"أيوه. ابعتلنا ميزانيتك على واتساب وهنعملك قايمة على قدها، أو نزوّد ونقلل في قطع أي عرض." },
    { q:"العروض دي ثابتة؟", a:"العروض بتتغيّر حسب المتاح والكميات. اللي على الموقع هو الشغال دلوقتي — أكّده معانا قبل الحجز." },
    { q:"بتبيعوا جملة ولا قطاعي؟", a:"الاتنين، وبنفس السعر تقريبًا. مش لازم تشتري كمية عشان تاخد سعر كويس." }
  ],

  orders: []
};
