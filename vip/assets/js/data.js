/* =============================================================
   V.I.P SILVER — بيانات المتجر
   عدّل هذا الملف لتغيير الأرقام أو المنتجات أو الأسعار.
   ملاحظة: الأدمن يقدر يعدّل المنتجات من داخل الموقع مباشرة،
   والتعديلات تُحفظ في متصفحه (راجع README).
   ============================================================= */

const BRAND = {
  ar:'في آي بي',
  en:'V.I.P SILVER',
  tagline:'هدايا وفضة تليق بالمناسبة',

  whatsapp:'201156442660',           // رقم استقبال الطلبات (دولي بدون +)
  whatsappShow:'0115 644 2660',

  currency:'ج.م',
  freeShipFrom: 3000,                // حدّ الشحن المجاني بالجنيه — 0 لإلغائه
  city:'مصر',

  /* حسابات الأدمن: أرقام ثابتة بكلمة مرور ثابتة.
     تدخل مباشرة برقمها وكلمة المرور دون رمز تحقق.
     ⚠️ كلمة المرور مكتوبة هنا داخل ملف يقرأه أي زائر — راجع README. */
  admins:['01156442660','01065434420'],
  adminPass:'654321'
};

/* ------------------------- الأقسام ------------------------- */
const CATEGORIES = [
  { id:'all',    label:'الكل' },
  { id:'silver', label:'الفضة' },
  { id:'shoes',  label:'الأحذية' },
  { id:'gifts',  label:'الهدايا والإكسسوار' }
];

/* -------------------------- المنتجات -------------------------- */
const DEFAULT_PRODUCTS = [
  { id:'v01', cat:'gifts', name:'بوكس هدية VIP الفاخر', sub:'VIP Gift Box',
    desc:'بوكس متكامل يضم عطر سيلفر سنت وساعة وإسورة وبلاكة بالاسم، بتغليف جاهز للإهداء.',
    price:2450, badge:'الأكثر طلباً', img:'assets/img/gift-box.jpg' },

  { id:'v02', cat:'gifts', name:'طقم ساعة وإسورة', sub:'Watch & Bracelet Set',
    desc:'ساعة كلاسيك بإطار مزدوج اللون مع إسورة مطابقة — إطلالة رسمية تليق بالمناسبات.',
    price:3900, img:'assets/img/watch-set.jpg' },

  { id:'v03', cat:'silver', name:'خاتم فضة منقوش بالعربي', sub:'Arabic Engraved Ring',
    desc:'فضة ٩٢٥ عيار عالٍ بنقش عربي يدوي، ويمكن كتابة العبارة التي تختارها.',
    price:850, badge:'حسب الطلب', img:'assets/img/ring-arabic.jpg' },

  { id:'v04', cat:'silver', name:'خاتم فضة عريض بالاسم', sub:'Wide Name Ring',
    desc:'خاتم عريض من فضة ٩٢٥ منقوش بالاسم مع زخرفة جانبية، متوفر بكل المقاسات.',
    price:1150, img:'assets/img/ring-name.jpg' },

  { id:'v05', cat:'silver', name:'خاتم فضة دوّار', sub:'Spinner Ring',
    desc:'خاتم بحلقة دوّارة منقوشة — قطعة مريحة ومميزة للاستخدام اليومي.',
    price:980, img:'assets/img/ring-spinner.jpg' },

  { id:'v06', cat:'silver', name:'دبل فضة للثنائي', sub:'Couple Rings',
    desc:'دبلتان من فضة ٩٢٥ تُنقش عليهما الأحرف الأولى لكما — هدية الخطوبة الأشهر لدينا.',
    price:1650, badge:'هدية مثالية', img:'assets/img/couple-rings.jpg' },

  { id:'v07', cat:'silver', name:'سلسلة فضة بحرف', sub:'Letter Necklace',
    desc:'سلسلة فضة ناعمة بدلاية على شكل حرف — اختاري الحرف الذي يعنيك.',
    price:920, img:'assets/img/necklace-letter.jpg' },

  { id:'v08', cat:'silver', name:'سبيكة فضة ١ كيلو — نقاء ٩٩٩', sub:'1 Kilo Fine Silver 999',
    desc:'سبيكة فضة خالصة بنقاء ٩٩٩ وختم معتمد — للاقتناء والاستثمار.',
    price:48000, badge:'استثمار', img:'assets/img/silver-bar.jpg' },

  { id:'v09', cat:'gifts', name:'شنطة COACH', sub:'COACH Tote Bag',
    desc:'شنطة توت أنيقة بمقاس عملي وخامة متينة، تناسب الشغل والخروج.',
    price:2850, img:'assets/img/bag-coach.jpg' },

  { id:'v10', cat:'shoes', name:'سنيكرز إير ماكس — أبيض', sub:'Air Max — White',
    desc:'سنيكرز بنعل هوائي مريح وخامة خفيفة، متوفر من مقاس ٣٩ إلى ٤٥.',
    price:1950, img:'assets/img/sneaker-white.jpg' },

  { id:'v11', cat:'shoes', name:'سنيكرز إير ماكس — أصفر', sub:'Air Max — Yellow',
    desc:'لون جريء بنعل هوائي مريح — الأكثر طلباً بين الشباب هذا الموسم.',
    price:1950, img:'assets/img/sneaker-yellow.jpg' },

  { id:'v12', cat:'shoes', name:'سنيكرز إير ماكس — باستيل', sub:'Air Max — Pastel',
    desc:'تدرّجات باستيل هادئة بنعل هوائي، مناسب للبنات والولاد.',
    price:2050, badge:'جديد', img:'assets/img/sneaker-pastel.jpg' },

  { id:'v13', cat:'shoes', name:'حذاء كاجوال أسود', sub:'Black Casual',
    desc:'حذاء كاجوال أسود بتصميم بسيط يناسب الشغل واللبس اليومي.',
    price:1450, img:'assets/img/shoe-black.jpg' },

  { id:'v14', cat:'shoes', name:'سنيكرز أبيض وأحمر', sub:'White & Red Sneaker',
    desc:'تصميم رياضي بخطوط حمراء ونعل مرتفع مريح للمشي الطويل.',
    price:1890, img:'assets/img/sneaker-red.jpg' },

  { id:'v15', cat:'shoes', name:'سنيكرز إير ماكس — وردي', sub:'Air Max — Pink',
    desc:'إصدار وردي بنعل هوائي ولمسات مطبوعة — إطلالة لافتة ومريحة.',
    price:2100, img:'assets/img/sneaker-pink.jpg' }
];

/* ------------------------- مزايا المتجر ------------------------- */
const PERKS = [
  { icon:'shield', title:'فضة ٩٢٥ مضمونة', text:'كل قطعة مختومة، ومعها ضمان استبدال إن لم تطابق الوصف.' },
  { icon:'pen',    title:'نقش بالاسم مجاناً', text:'اكتب الاسم أو العبارة وننقشها لك قبل التسليم دون رسوم.' },
  { icon:'truck',  title:'شحن لكل المحافظات', text:'توصيل خلال ٢–٥ أيام، ومجاناً للطلبات فوق ٣٠٠٠ ج.م.' },
  { icon:'gift',   title:'تغليف هدية أنيق',  text:'علبة وتغليف يليقان بالمناسبة مع كل طلب.' }
];
