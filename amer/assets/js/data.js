/* بيانات سنتر الأمير والأميرة — كل حاجة هنا بتتغير من لوحة التحكم */
window.AMER_SEED = {
  settings: {
    brand: "AMER & AMIRA",
    brandAr: "سنتر الأمير والأميرة",
    tagline: "APPLIANCES · FURNITURE · HOME",
    intro: "أجهزة كهربائية وموبيليا وسجاد ومفروشات — كل اللي البيت محتاجه في مكان واحد، وكل قسم ليه رقم مخصص يرد عليك على طول.",
    addr: "الحي السادس — أمام سنتر وادي الملوك، ٦ أكتوبر",
    mapq: "الحى السادس امام سنتر وادى الملوك 6 اكتوبر",
    phone: "01229445542",
    whats: "201229445542",
    hours: "الرد يوميًا من ١٠ ص لـ ١٠ م",
    adminPass: "123456",
    priceNote: "السعر عند الطلب",
    priceHint: "الأسعار شاملة الضريبة وقابلة للتغيير — أكّدها معانا قبل الطلب.",
    showPrices: true,
    currency: "ج.م",
    facebook: "سنتر الامير والاميرة للاجهزة الكهربائية والموبليا"
  },
  depts: [
    { id:"home",   name:"الأجهزة والأدوات المنزلية", icon:"plug",
      note:"خلاطات، أفران، عجانات، مكاوي، ترامس وأطباق تقديم",
      phones:["01229445542"] },
    { id:"wash",   name:"الغسالات والسخانات", icon:"drop",
      note:"غسالات أوتوماتيك وسخانات بكل المقاسات",
      phones:["01202676940","01287329932"] },
    { id:"furn",   name:"الأثاث والموبيليا", icon:"sofa",
      note:"غرف نوم، سفرة، أنترية ومستلزمات البيت",
      phones:["01227047007"] },
    { id:"carpet", name:"السجاد والمفروشات", icon:"rug",
      note:"سجاد ومفروشات بمقاسات وألوان مختلفة",
      phones:["01229445542"] }
  ],
  stats: [
    { n:"٦١ ألف", t:"متابع على فيسبوك" },
    { n:"٤ أقسام", t:"تحت سقف واحد" },
    { n:"٤٬٦٠٠+", t:"منشور ومنتج معروض" },
    { n:"٦ أكتوبر", t:"مكان المعرض" }
  ],
  products: [
    { id:"mixer",  name:"عجان كهربائي رفال",                    img:"assets/img/p-mixer.jpg",  dept:"home", price:4500, note:"وعاء استانلس وخفاقة ومضرب عجين" },
    { id:"oven",   name:"فرن كهربائي رفال بشواية",              img:"assets/img/p-oven.jpg",   dept:"home", price:4200, note:"ثلاث مفاتيح تحكم وصينية وشبكة شوي" },
    { id:"blender",name:"خلاط رفال ١٨٠٠ وات ٢ لتر",            img:"assets/img/p-blender.jpg",dept:"home", price:3400, note:"دورق مضاد للكسر ويكسر التلج، ومعاه مطحنة" },
    { id:"kettle", name:"كاتيل زجاج رفال ١٥٠٠ وات ٢ لتر",      img:"assets/img/p-kettle.jpg", dept:"home", price:1350, note:"زجاج حراري وقاعدة استانلس" },
    { id:"iron",   name:"مكواة بخار رفال ٣٠٠٠ وات",            img:"assets/img/p-iron.jpg",   dept:"home", price:1950, note:"قاعدة سيراميك وبخار رأسي" },
    { id:"chopper",name:"كبة لحوم ومفرمة خضروات رفال",          img:"assets/img/p-chopper.jpg",dept:"home", price:1870, note:"وعاء شفاف وسكاكين استانلس", src:"سعر الملصق" },
    { id:"fridge", name:"ثلاجة نوفروست زجاج أسود باب علوي",     img:"assets/img/p-fridge.jpg", dept:"home", price:34000, note:"موجودة في المعرض — اسأل عن المقاسات المتاحة" },
    { id:"table",  name:"سفرة خشب بستة كراسي",                  img:"assets/img/p-table.jpg",  dept:"furn", price:28000, note:"ترابيزة خشب وكراسي بظهر منجّد" },
    { id:"spice",  name:"طقم توابل ١٢ برطمان على قاعدة خشب",    img:"assets/img/p-spice.jpg",  dept:"home", price:220, note:"برطمانات زجاج بغطا أسود" },
    { id:"pleo",   name:"طبق تقديم برسمة نمر",                  img:"assets/img/p-plate-leopard.jpg", dept:"home", price:55, note:"طبق دائري لامع" },
    { id:"pwood",  name:"طبق تقديم بيضاوي خشب",                 img:"assets/img/p-plate-wood.jpg",    dept:"home", price:65, note:"طبق بيضاوي بلون الخشب" },
    { id:"tlab",   name:"ترمس لابوبو بشاشة حرارة",              img:"assets/img/p-thermos-labubu.jpg",dept:"home", price:380, note:"غطا بشاشة بتوريك حرارة المياه" },
    { id:"tbeige", name:"ترمس بيج بحزام وماصة",                 img:"assets/img/p-thermos-beige.jpg", dept:"home", price:450, note:"استانلس ٣١٦ بغطا قفل" },
    { id:"mug",    name:"مج FOCUS بغطا",                        img:"assets/img/p-mug.jpg",           dept:"home", price:220, note:"مج سيراميك طويل بغطا" }
  ],
  offers: [
    { id:"o-kitchen", name:"عرض المطبخ", sub:"الأساسيات اللي مفيش مطبخ بيستغنى عنها",
      items:["blender","kettle","chopper"], price:5900, tag:"الأكثر طلبًا" },
    { id:"o-bride",   name:"عرض العروسة", sub:"جهاز المطبخ الكامل في مرة واحدة",
      items:["mixer","oven","blender","iron"], price:12900, tag:"أوفر عرض" },
    { id:"o-serve",   name:"عرض التقديم", sub:"طقم توابل وأطباق ومج",
      items:["spice","pleo","pwood","mug"], price:480, tag:"" },
    { id:"o-dining",  name:"عرض السفرة", sub:"سفرة ٦ كراسي وطقم التوابل معاها",
      items:["table","spice"], price:27900, tag:"" }
  ],
  gallery: [
    { img:"assets/img/p-table.jpg",           cap:"سفرة خشب بستة كراسي منجّدة" },
    { img:"assets/img/p-fridge.jpg",          cap:"ثلاجة زجاج أسود في المعرض" },
    { img:"assets/img/p-blender.jpg",         cap:"خلاط رفال أسود جنب علبته" },
    { img:"assets/img/p-kettle.jpg",          cap:"كاتيل زجاج بغطا أزرق" },
    { img:"assets/img/p-iron.jpg",            cap:"مكواة بخار سوداء وذهبي" },
    { img:"assets/img/p-chopper.jpg",         cap:"مفرمة فضي على ترابيزة خشب" },
    { img:"assets/img/p-spice.jpg",           cap:"١٢ برطمان توابل على قاعدة خشب" },
    { img:"assets/img/p-plate-leopard.jpg",   cap:"طبق تقديم برسمة نمر" },
    { img:"assets/img/p-thermos-labubu.jpg",  cap:"ترمس أبيض برسمة لابوبو" },
    { img:"assets/img/p-mug.jpg",             cap:"مج كحلي مكتوب عليه FOCUS" },
    { img:"assets/img/p-mixer.jpg",           cap:"عجان رفال أبيض بوعاء استانلس" },
    { img:"assets/img/p-oven.jpg",            cap:"فرن رفال أسود مفتوح" }
  ],
  faq: [
    { q:"المعرض فين بالظبط؟", a:"الحي السادس بـ٦ أكتوبر، أمام سنتر وادي الملوك. تقدر تفتح الخريطة من الموقع على طول." },
    { q:"أكلّم مين لو عايز غسالة أو سخان؟", a:"قسم الغسالات والسخانات ليه رقمين مخصصين: 01202676940 و 01287329932." },
    { q:"وعايز موبيليا؟", a:"قسم الأثاث والموبيليا رقمه 01227047007." },
    { q:"ليه الأسعار مش مكتوبة؟", a:"الأسعار بتتغير حسب المقاس والموديل والعرض الشغال. ابعت اللي عايزه ويوصلك السعر النهائي حالًا." },
    { q:"أقدر أطلب أكتر من حاجة مرة واحدة؟", a:"أيوه. ضيف اللي عايزه في قايمة الطلب، والموقع هيقسّمها لوحده ويبعت كل قسم لرقمه الصح." }
  ],
  orders: []
};
