/* =============================================================
   باهية | BAHIA — بيانات المتجر
   عدّل هذا الملف فقط لتغيير الرقم أو المنتجات أو الأسعار.
   ============================================================= */

const BRAND = {
  ar:'باهية',
  en:'BAHIA',
  tagline:'مكياج يليق بملامحك',

  whatsapp:'96651447772',        // رقم استقبال الطلبات (بالصيغة الدولية بدون +)
  whatsappShow:'+966 51 447 772',

  currency:'ر.س',
  freeShipFrom: 200,             // حدّ الشحن المجاني بالريال — غيّره أو اجعله 0 لإلغائه
  city:'المملكة العربية السعودية'
};

/* ------------------------- الأقسام ------------------------- */
const CATEGORIES = [
  { id:'all',   label:'الكل' },
  { id:'lips',  label:'الشفاه' },
  { id:'face',  label:'الوجه' },
  { id:'eyes',  label:'العيون' },
  { id:'tools', label:'الفرش والأدوات' },
  { id:'sets',  label:'الأطقم' }
];

/* -------------------------- المنتجات --------------------------
   price: بالريال السعودي  |  was: السعر قبل الخصم (اختياري)
   -------------------------------------------------------------- */
const PRODUCTS = [
  { id:'b01', cat:'lips', name:'أحمر شفاه مطفي', sub:'Matte Lipstick',
    desc:'قوام كريمي مطفي يدوم طويلاً دون أن يجفّف الشفاه، بتغطية كاملة من أول لمسة.',
    price:89, badge:'الأكثر مبيعاً', img:'assets/img/lipstick-matte.jpg' },

  { id:'b02', cat:'lips', name:'أحمر شفاه ساتان', sub:'Satin Lipstick',
    desc:'لمعة ساتان ناعمة ودرجات دافئة تناسب البشرة الحنطية والفاتحة.',
    price:89, img:'assets/img/lipstick-satin.jpg' },

  { id:'b03', cat:'lips', name:'أحمر شفاه كلاسيك', sub:'Classic Lipstick',
    desc:'الدرجة الجريئة التي لا تخطئ — تغطية غنية بلمسة نهائية مخملية.',
    price:95, img:'assets/img/lipstick-classic.jpg' },

  { id:'b04', cat:'lips', name:'قلم تحديد الشفاه', sub:'Lip Liner',
    desc:'قلم ناعم يرسم حدوداً دقيقة ويمنع خروج أحمر الشفاه عن مساره.',
    price:55, img:'assets/img/lip-liner.jpg' },

  { id:'b05', cat:'face', name:'كونسيلر مقاوم للماء', sub:'Waterproof Concealer',
    desc:'يخفي الهالات والعيوب بتغطية عالية وثبات يمتد طوال اليوم.',
    price:85, badge:'جديد', img:'assets/img/concealer.jpg' },

  { id:'b06', cat:'face', name:'كريم أساس مخملي', sub:'Velvet Foundation',
    desc:'تغطية متوسطة قابلة للبناء بملمس خفيف لا يترك أثراً على البشرة.',
    price:145, img:'assets/img/foundation.jpg' },

  { id:'b07', cat:'face', name:'برايمر مثبّت', sub:'Grip Primer',
    desc:'قاعدة تُمسك بالمكياج وتوحّد الملمس قبل الأساس، وتصغّر مظهر المسام.',
    price:110, img:'assets/img/primer.jpg' },

  { id:'b08', cat:'face', name:'سيروم الأساس المرطّب', sub:'Hydrating Base Serum',
    desc:'يُستخدم قبل المكياج ليمنح البشرة نعومة ولمعة صحية تدوم.',
    price:135, img:'assets/img/serum.jpg' },

  { id:'b09', cat:'face', name:'بلاشر مخبوز', sub:'Baked Blush',
    desc:'مسحوق مخبوز ناعم يمنح الوجنتين لوناً طبيعياً متدرّجاً دون تكتّل.',
    price:79, img:'assets/img/blush.jpg' },

  { id:'b10', cat:'face', name:'باليت كونتور وإضاءة', sub:'Contour & Glow Palette',
    desc:'أربع درجات لنحت الوجه وإبراز ملامحه، مع مرآة مدمجة في العلبة.',
    price:165, badge:'مميّز', img:'assets/img/face-palette.jpg' },

  { id:'b11', cat:'eyes', name:'باليت ظلال ١٢ لون', sub:'12-Shade Eye Palette',
    desc:'اثنتا عشرة درجة بين المطفي واللامع، بتصبّغ عالٍ وثبات ممتاز.',
    price:175, badge:'الأكثر طلباً', img:'assets/img/eye-palette.jpg' },

  { id:'b12', cat:'eyes', name:'ماسكارا تكثيف وتطويل', sub:'Volume & Length Mascara',
    desc:'فرشاة تفصل الرموش وتمنحها كثافة مضاعفة دون تكتّل أو تساقط.',
    price:95, img:'assets/img/mascara.jpg' },

  { id:'b13', cat:'tools', name:'طقم فرش أوفال', sub:'Oval Brush Set',
    desc:'فرش بشعيرات كثيفة وناعمة توزّع المنتج بتساوٍ وتسهّل الدمج.',
    price:120, img:'assets/img/brushes.jpg' },

  { id:'b14', cat:'tools', name:'إسفنجة المكياج', sub:'Beauty Sponge',
    desc:'إسفنجة تتمدّد بالماء لدمج الأساس والكونسيلر بلمسة نهائية ناعمة.',
    price:35, img:'assets/img/sponge.jpg' },

  { id:'b15', cat:'sets', name:'طقم باهية الكامل', sub:'The Bahia Set',
    desc:'مجموعة متكاملة من الأساس والكونسيلر والسيروم في علبة هدية أنيقة.',
    price:449, was:599, badge:'وفّري ١٥٠ ر.س', img:'assets/img/full-set.jpg' }
];

/* ------------------------- مزايا المتجر ------------------------- */
const PERKS = [
  { icon:'truck',  title:'شحن سريع',        text:'توصيل لكل مدن المملكة خلال ٢–٤ أيام عمل.' },
  { icon:'shield', title:'منتجات أصلية',    text:'كل قطعة مختومة وأصلية، وإلا استرجاع كامل.' },
  { icon:'gift',   title:'تغليف هدية',      text:'تغليف أنيق مجاني مع كل طلب فوق ٢٠٠ ر.س.' },
  { icon:'chat',   title:'استشارة مجانية',  text:'نساعدك في اختيار الدرجة المناسبة لبشرتك.' }
];
