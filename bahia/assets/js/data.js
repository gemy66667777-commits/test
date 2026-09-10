/* =============================================================
   باهية | BAHIA — بيانات المتجر (عربي / English)
   كل نص ثنائي اللغة يُكتب هكذا: { ar:'...', en:'...' }
   ============================================================= */

const BRAND = {
  ar:'باهية',
  en:'BAHIA',

  whatsapp:'96651447772',            // رقم استقبال الطلبات (دولي بدون +)
  whatsappShow:'+966 51 447 772',

  currency:{ ar:'ر.س', en:'SAR' },
  freeShipFrom: 200,                 // حدّ الشحن المجاني — اجعله 0 لإلغاء الميزة
  site:'https://bahia-ecru.vercel.app'
};

/* ------------------------- نصوص الواجهة ------------------------- */
const T = {
  ar:{
    dir:'rtl', other:'EN', otherLabel:'English',
    announce:'شحن مجاني للطلبات فوق <b>٢٠٠ ر.س</b> · توصيل لكل مدن المملكة',
    navShop:'المنتجات', navStory:'عن باهية', navPerks:'لماذا باهية', navContact:'تواصلي معنا',
    heroKicker:'مجموعة هذا الموسم',
    heroTitle:'ملامحك تستحق', heroTitleEm:'أن تُبرَز لا أن تُخفى',
    heroLead:'مكياج بدرجات مصنوعة للبشرة العربية — تغطية تدوم، ملمس خفيف، وألوان تُكمل ملامحك بدل أن تغيّرها.',
    heroCta1:'تسوّقي المجموعة', heroCta2:'تعرّفي على باهية',
    heroM1:'منتجات أصلية', heroM2:'خالية من القسوة على الحيوان', heroM3:'شحن خلال ٢–٤ أيام',
    heroTagName:'باليت ظلال ١٢ لون', heroTagNote:'الأكثر طلباً هذا الشهر',
    shopKicker:'المتجر', shopTitle:'تسوّقي حسب القسم',
    shopLead:'أضيفي ما تحبينه إلى السلة، وعند إتمام الطلب سيصلنا طلبك كاملاً على واتساب.',
    storyKicker:'عن باهية', storyTitle:'اسمٌ معناه الجمال الظاهر',
    storyBody:'بدأت باهية من سؤال بسيط: لماذا تشتري المرأة العربية درجاتٍ صُمّمت لبشرة غيرها؟ فاخترنا أن نبدأ من الدرجة الصحيحة — أساسٌ يذوب في البشرة الحنطية، ودرجات شفاه دافئة، وظلال تليق بالعين الواسعة. كل قطعة نختبرها قبل أن نطرحها، ولا نطرح لوناً لا نستخدمه بأنفسنا.',
    perksKicker:'لماذا باهية', perksTitle:'تجربة تسوّق مريحة',
    ctaKicker:'تواصلي معنا', ctaTitle:'محتارة في اختيار الدرجة؟',
    ctaBody:'أرسلي لنا صورة ليدك أو وجهك في ضوء طبيعي، ونرشّح لك الدرجة الأقرب لبشرتك — مجاناً وبلا التزام بالشراء.',
    ctaBtn:'استشارة مجانية على واتساب',
    ctaWa:'مرحباً باهية، أحتاج مساعدة في اختيار الدرجة المناسبة لبشرتي.',
    ftrAbout:'مكياج بدرجات مصنوعة للبشرة العربية. الطلب عبر واتساب، والتوصيل لكل مدن المملكة.',
    ftrShop:'المتجر', ftrAll:'كل المنتجات', ftrBrand:'باهية', ftrOrder:'الطلب',
    ftrWa:'واتساب', ftrBrowse:'تصفّحي المجموعة',
    rights:'باهية BAHIA — جميع الحقوق محفوظة.', country:'المملكة العربية السعودية',
    add:'أضيفي للسلة', added:'تمت الإضافة', addedToast:'تمت الإضافة إلى السلة',
    cart:'سلة المشتريات', cartEmptySub:'لا توجد منتجات بعد', pieces:'قطعة في السلة',
    cartEmpty:'سلتك فارغة.', cartEmptyHint:'أضيفي منتجاتك المفضلة وابدئي الطلب.',
    each:'للقطعة', remove:'إزالة', totalLabel:'الإجمالي',
    shipFree:'مبروك! الشحن مجاني على هذا الطلب.',
    shipLeft:(n,c)=>`أضيفي بـ <b class="num">${n}</b> ${c} واحصلي على شحن مجاني.`,
    checkout:'إتمام الطلب عبر واتساب',
    cartNote:'سيفتح واتساب برسالة تحتوي طلبك كاملاً — راجعيها ثم أرسليها.',
    close:'إغلاق السلة', cartAria:'سلة المشتريات', menu:'القائمة',
    orderHi:'مرحباً باهية، أرغب في تأكيد الطلب التالي:',
    orderCount:'عدد القطع', orderTotal:'الإجمالي', orderShip:'الشحن', orderShipFree:'مجاني',
    orderName:'الاسم:', orderCity:'المدينة:', orderAddr:'العنوان:',
    askWa:'مرحباً باهية، أود الاستفسار عن المنتجات.'
  },
  en:{
    dir:'ltr', other:'ع', otherLabel:'العربية',
    announce:'Free shipping on orders over <b>SAR 200</b> · Delivery across the Kingdom',
    navShop:'Shop', navStory:'About', navPerks:'Why Bahia', navContact:'Contact',
    heroKicker:'This season’s collection',
    heroTitle:'Your features deserve', heroTitleEm:'to be seen, not hidden',
    heroLead:'Makeup in shades made for Arab skin — lasting coverage, a weightless finish, and colours that complete your features instead of changing them.',
    heroCta1:'Shop the collection', heroCta2:'About Bahia',
    heroM1:'Authentic products', heroM2:'Cruelty free', heroM3:'Ships in 2–4 days',
    heroTagName:'12-Shade Eye Palette', heroTagNote:'Most wanted this month',
    shopKicker:'The shop', shopTitle:'Shop by category',
    shopLead:'Add what you love to the bag — at checkout your full order reaches us on WhatsApp.',
    storyKicker:'About Bahia', storyTitle:'A name that means visible beauty',
    storyBody:'Bahia began with one question: why should an Arab woman buy shades designed for someone else’s skin? So we started from the right shade — a base that melts into olive skin, warm lip tones, and eyeshadows made for wide eyes. Every piece is tested before it launches, and we never sell a colour we would not wear ourselves.',
    perksKicker:'Why Bahia', perksTitle:'A shopping experience that respects you',
    ctaKicker:'Contact us', ctaTitle:'Not sure which shade is yours?',
    ctaBody:'Send us a photo of your hand or face in natural light and we will recommend the closest match — free, with no obligation to buy.',
    ctaBtn:'Free consultation on WhatsApp',
    ctaWa:'Hello Bahia, I need help choosing the right shade for my skin.',
    ftrAbout:'Makeup in shades made for Arab skin. Order on WhatsApp, delivered across the Kingdom.',
    ftrShop:'Shop', ftrAll:'All products', ftrBrand:'Bahia', ftrOrder:'Order',
    ftrWa:'WhatsApp', ftrBrowse:'Browse the collection',
    rights:'Bahia BAHIA — All rights reserved.', country:'Saudi Arabia',
    add:'Add to bag', added:'Added', addedToast:'Added to your bag',
    cart:'Your bag', cartEmptySub:'Nothing here yet', pieces:'items in your bag',
    cartEmpty:'Your bag is empty.', cartEmptyHint:'Add your favourites and start your order.',
    each:'each', remove:'Remove', totalLabel:'Total',
    shipFree:'Nice! Shipping is free on this order.',
    shipLeft:(n,c)=>`Add <b class="num">${n}</b> ${c} more for free shipping.`,
    checkout:'Checkout on WhatsApp',
    cartNote:'WhatsApp will open with your full order — review it, then send.',
    close:'Close bag', cartAria:'Shopping bag', menu:'Menu',
    orderHi:'Hello Bahia, I would like to confirm this order:',
    orderCount:'Items', orderTotal:'Total', orderShip:'Shipping', orderShipFree:'Free',
    orderName:'Name:', orderCity:'City:', orderAddr:'Address:',
    askWa:'Hello Bahia, I would like to ask about your products.'
  }
};

/* ------------------------- الأقسام ------------------------- */
const CATEGORIES = [
  { id:'all',   label:{ ar:'الكل',            en:'All' } },
  { id:'lips',  label:{ ar:'الشفاه',          en:'Lips' } },
  { id:'face',  label:{ ar:'الوجه',           en:'Face' } },
  { id:'eyes',  label:{ ar:'العيون',          en:'Eyes' } },
  { id:'tools', label:{ ar:'الفرش والأدوات',  en:'Brushes & Tools' } },
  { id:'sets',  label:{ ar:'الأطقم',          en:'Sets' } }
];

/* -------------------------- المنتجات -------------------------- */
const PRODUCTS = [
  { id:'b01', cat:'lips', price:89, img:'assets/img/lipstick-matte.jpg',
    name:{ ar:'أحمر شفاه مطفي', en:'Matte Lipstick' },
    desc:{ ar:'قوام كريمي مطفي يدوم طويلاً دون أن يجفّف الشفاه، بتغطية كاملة من أول لمسة.',
           en:'A creamy matte finish that lasts without drying, with full coverage from the first swipe.' },
    badge:{ ar:'الأكثر مبيعاً', en:'Bestseller' } },

  { id:'b02', cat:'lips', price:89, img:'assets/img/lipstick-satin.jpg',
    name:{ ar:'أحمر شفاه ساتان', en:'Satin Lipstick' },
    desc:{ ar:'لمعة ساتان ناعمة ودرجات دافئة تناسب البشرة الحنطية والفاتحة.',
           en:'A soft satin sheen in warm tones that suit olive and fair skin alike.' } },

  { id:'b03', cat:'lips', price:95, img:'assets/img/lipstick-classic.jpg',
    name:{ ar:'أحمر شفاه كلاسيك', en:'Classic Lipstick' },
    desc:{ ar:'الدرجة الجريئة التي لا تخطئ — تغطية غنية بلمسة نهائية مخملية.',
           en:'The bold shade that never misses — rich coverage with a velvet finish.' } },

  { id:'b04', cat:'lips', price:55, img:'assets/img/lip-liner.jpg',
    name:{ ar:'قلم تحديد الشفاه', en:'Lip Liner' },
    desc:{ ar:'قلم ناعم يرسم حدوداً دقيقة ويمنع خروج أحمر الشفاه عن مساره.',
           en:'A smooth pencil that draws a precise line and keeps colour where it belongs.' } },

  { id:'b05', cat:'face', price:85, img:'assets/img/concealer.jpg',
    name:{ ar:'كونسيلر مقاوم للماء', en:'Waterproof Concealer' },
    desc:{ ar:'يخفي الهالات والعيوب بتغطية عالية وثبات يمتد طوال اليوم.',
           en:'Covers dark circles and blemishes with high coverage that holds all day.' },
    badge:{ ar:'جديد', en:'New' } },

  { id:'b06', cat:'face', price:145, img:'assets/img/foundation.jpg',
    name:{ ar:'كريم أساس مخملي', en:'Velvet Foundation' },
    desc:{ ar:'تغطية متوسطة قابلة للبناء بملمس خفيف لا يترك أثراً على البشرة.',
           en:'Buildable medium coverage with a weightless feel that never looks like a mask.' } },

  { id:'b07', cat:'face', price:110, img:'assets/img/primer.jpg',
    name:{ ar:'برايمر مثبّت', en:'Grip Primer' },
    desc:{ ar:'قاعدة تُمسك بالمكياج وتوحّد الملمس قبل الأساس، وتصغّر مظهر المسام.',
           en:'A gripping base that smooths texture before foundation and blurs pores.' } },

  { id:'b08', cat:'face', price:135, img:'assets/img/serum.jpg',
    name:{ ar:'سيروم الأساس المرطّب', en:'Hydrating Base Serum' },
    desc:{ ar:'يُستخدم قبل المكياج ليمنح البشرة نعومة ولمعة صحية تدوم.',
           en:'Worn under makeup for lasting softness and a healthy glow.' } },

  { id:'b09', cat:'face', price:79, img:'assets/img/blush.jpg',
    name:{ ar:'بلاشر مخبوز', en:'Baked Blush' },
    desc:{ ar:'مسحوق مخبوز ناعم يمنح الوجنتين لوناً طبيعياً متدرّجاً دون تكتّل.',
           en:'A finely baked powder that gives cheeks a natural, blendable flush.' } },

  { id:'b10', cat:'face', price:165, img:'assets/img/face-palette.jpg',
    name:{ ar:'باليت كونتور وإضاءة', en:'Contour & Glow Palette' },
    desc:{ ar:'أربع درجات لنحت الوجه وإبراز ملامحه، مع مرآة مدمجة في العلبة.',
           en:'Four shades to sculpt and lift your features, with a built-in mirror.' },
    badge:{ ar:'مميّز', en:'Featured' } },

  { id:'b11', cat:'eyes', price:175, img:'assets/img/eye-palette.jpg',
    name:{ ar:'باليت ظلال ١٢ لون', en:'12-Shade Eye Palette' },
    desc:{ ar:'اثنتا عشرة درجة بين المطفي واللامع، بتصبّغ عالٍ وثبات ممتاز.',
           en:'Twelve shades from matte to shimmer, richly pigmented and long wearing.' },
    badge:{ ar:'الأكثر طلباً', en:'Most wanted' } },

  { id:'b12', cat:'eyes', price:95, img:'assets/img/mascara.jpg',
    name:{ ar:'ماسكارا تكثيف وتطويل', en:'Volume & Length Mascara' },
    desc:{ ar:'فرشاة تفصل الرموش وتمنحها كثافة مضاعفة دون تكتّل أو تساقط.',
           en:'A brush that separates lashes and doubles volume with no clumps or flaking.' } },

  { id:'b13', cat:'tools', price:120, img:'assets/img/brushes.jpg',
    name:{ ar:'طقم فرش أوفال', en:'Oval Brush Set' },
    desc:{ ar:'فرش بشعيرات كثيفة وناعمة توزّع المنتج بتساوٍ وتسهّل الدمج.',
           en:'Dense, soft bristles that lay product down evenly and blend without effort.' } },

  { id:'b14', cat:'tools', price:35, img:'assets/img/sponge.jpg',
    name:{ ar:'إسفنجة المكياج', en:'Beauty Sponge' },
    desc:{ ar:'إسفنجة تتمدّد بالماء لدمج الأساس والكونسيلر بلمسة نهائية ناعمة.',
           en:'Expands with water to blend foundation and concealer to a seamless finish.' } },

  { id:'b15', cat:'sets', price:449, was:599, img:'assets/img/full-set.jpg',
    name:{ ar:'طقم باهية الكامل', en:'The Bahia Set' },
    desc:{ ar:'مجموعة متكاملة من الأساس والكونسيلر والسيروم في علبة هدية أنيقة.',
           en:'Foundation, concealer and serum together in an elegant gift box.' },
    badge:{ ar:'وفّري ١٥٠ ر.س', en:'Save SAR 150' } }
];

/* ------------------------- مزايا المتجر ------------------------- */
const PERKS = [
  { icon:'truck',  title:{ ar:'شحن سريع', en:'Fast delivery' },
    text:{ ar:'توصيل لكل مدن المملكة خلال ٢–٤ أيام عمل.', en:'Across the Kingdom in 2–4 working days.' } },
  { icon:'shield', title:{ ar:'منتجات أصلية', en:'Authentic only' },
    text:{ ar:'كل قطعة مختومة وأصلية، وإلا استرجاع كامل.', en:'Every item sealed and genuine — or a full refund.' } },
  { icon:'gift',   title:{ ar:'تغليف هدية', en:'Gift wrapping' },
    text:{ ar:'تغليف أنيق مجاني مع كل طلب فوق ٢٠٠ ر.س.', en:'Free elegant wrapping on orders over SAR 200.' } },
  { icon:'chat',   title:{ ar:'استشارة مجانية', en:'Free advice' },
    text:{ ar:'نساعدك في اختيار الدرجة المناسبة لبشرتك.', en:'We help you find the shade that matches your skin.' } }
];
