/* سمر — البيانات الأساسية (تُنسخ أول مرة لذاكرة المتصفح ويعدّلها الأدمن) */
window.SAMAR_SEED = {
  settings: {
    brand: "سمر",
    latin: "Samar",
    tagline: "تجهيز كوش ومناسبات",
    intro: "كوشة ونيون وإضاءة بتخلّي ليلتك شكلها زي ما اتخيلتيها — وبأسعار على قد إيدك",
    phones: ["01125382142"],
    whatsapp: "201125382142",
    address: "بنجهّز في البيت والقاعة والجاردن والأوبن إير",
    hours: "الرد يوميًا من ١٠ ص حتى ١٢ م",
    showPrices: false,
    priceLabel: "السعر عند الطلب",
    adminPhones: ["01125382142"],
    adminPass: "123456"
  },

  services: [
    { icon: "arch",   name: "كوش وديكور",     desc: "كوشة ورد أو تل متضفّر على مقاس المكان والثيم اللي في بالك" },
    { icon: "neon",   name: "كلمة نيون",       desc: "آية أو اسمين أو جملة بخط النيون المضيء — التفصيلة اللي بتفضل في كل صورة" },
    { icon: "light",  name: "إضاءة وبيبي لايت", desc: "ستارة نور وفيري لايت وشمعدانات تغيّر إحساس المكان" },
    { icon: "chair",  name: "كراسي وأثاث",     desc: "كرسيين العروسين أو بانكيت، وأحدث كراسي المعازيم" },
    { icon: "music",  name: "دي جي وصوتيات",   desc: "سماعات بتشتغل بلوتوث أو فلاشة، جاهزة على طول" },
    { icon: "camera", name: "تصوير",           desc: "فوتوغرافر يفضل معاكي اليوم كله وعدد الصور مفتوح" }
  ],

  /* العروض — منقولة زي ما البراند كاتبها */
  packages: [
    {
      id: "pkg-1",
      name: "العرض الأول",
      sub: "البداية المظبوطة",
      desc: "كل الأساسيات اللي تخلّي الركن جاهز للتصوير، من غير تكلفة زيادة.",
      price: 0, guests: "كتب كتاب وخطوبة", badge: "",
      features: ["كوشة من اختيارك","كرسيين العروسين","ستارة نور بيبي لايت","كلمة خشب","ستارة تل على الديكور","تزيين باب الشقة بالتل والورد هدية 🌹"]
    },
    {
      id: "pkg-2",
      name: "العرض التاني",
      sub: "بالنيون المضيء",
      desc: "زي الأول بس بكلمة نيون مضيئة وخلفية شيفون — الفرق بيبان في الصور على طول.",
      price: 0, guests: "الأنسب لمعظم الحالات", badge: "الأكثر طلبًا",
      features: ["كوشة ورد من اختيارك","كلمة نيون مضيئة","ستارة نور بيبي لايت","خلفية شيفون","كرسيين العروسين أو بانكيت","تزيين باب الشقة بالتل والورد هدية 🌹"]
    },
    {
      id: "pkg-3",
      name: "العرض التالت",
      sub: "الكامل",
      desc: "النيون والشمعدانات والخلفية الشيفون مع بعض — أشمل عرض عندنا.",
      price: 0, guests: "فرح وخطوبة", badge: "الأشمل",
      features: ["كوشة ورد من اختيارك","كرسيين العروسين أو بانكيت","كلمة نيون مضيئة","شمعدان على اليمين والشمال","ستارة شيفون خلفية للديكور","تزيين باب الشقة بالتل والورد هدية 🌹"]
    }
  ],

  /* إضافات تتطلب مع أي عرض */
  addons: [
    { icon: "music",  name: "سماعات دي جي",    desc: "بتشتغل بلوتوث أو فلاشة" },
    { icon: "tray",   name: "صواني الشبكة",     desc: "بالأسماء وتاريخ المناسبة" },
    { icon: "chair",  name: "كراسي المعازيم",   desc: "أحدث الموديلات" },
    { icon: "board",  name: "ويلكم بورد",       desc: "بالأسامي وتاريخ المناسبة" },
    { icon: "light",  name: "ستيدچ مضيء",      desc: "يرفع الكوشة ويبيّن الديكور" },
    { icon: "camera", name: "فوتوغرافر",        desc: "اليوم كله وعدد الصور مفتوح" }
  ],

  occasions: ["كتب كتاب", "فرح", "خطوبة", "عيد ميلاد", "سبوع", "تقفيل جاردن وأوبن إير"],

  /* المعرض — الاسم وصف مباشر للي في الصورة */
  items: [
    { id:"g01", slug:"koshet-neon-aya-shamadan",    name:"كوشة تل متضفّر وشمعدانات ذهبي", cat:"كتب كتاب",  price:0, featured:true,  desc:"نيون آية وشجر أبيض وبنش فرو" },
    { id:"g02", slug:"koshet-neon-aya-shagar",      name:"كوشة نيون آية وشجر أبيض",        cat:"كتب كتاب",  price:0, featured:false, desc:"خلفية تل متضفّرة وشمعدانات على الجانبين" },
    { id:"g03", slug:"koshet-dayra-neon-aya",       name:"كوشة دايرة بنيون آية",           cat:"كتب كتاب",  price:0, featured:true,  desc:"إطار ورد أبيض وستارة نور وبنش فرو" },
    { id:"g04", slug:"koshet-amoudein-ward-aya",    name:"كوشة عمودين ورد ونيون آية",      cat:"كتب كتاب",  price:0, featured:false, desc:"خلفية متضفّرة بين عمودين شجر أبيض" },
    { id:"g05", slug:"koshet-dayra-neon-wardy",     name:"كوشة دايرة بنيون وردي",          cat:"كتب كتاب",  price:0, featured:false, desc:"إطار ورد مضيء وبنش أبيض" },
    { id:"g06", slug:"koshet-dayra-itwasalwaysyou", name:"كوشة دايرة ونيون It Was Always You", cat:"كوش دايرة", price:0, featured:true, desc:"إطار زهر أبيض كامل وبنش ذهبي" },
    { id:"g07", slug:"koshet-dayra-bettertogether", name:"كوشة دايرة ونيون Better Together",   cat:"كوش دايرة", price:0, featured:true, desc:"ستارة نور داخل الإطار وبنش فرو" },
    { id:"g08", slug:"koshet-dayra-korsyen-abyad",  name:"كوشة دايرة وكرسيين أبيض",        cat:"كوش دايرة", price:0, featured:false, desc:"نيون We Found Love وستارة تل ولمبات معلّقة" },
    { id:"g09", slug:"koshet-dayra-neon-wardy-wide",name:"كوشة دايرة ونيون وردي وشمعدانات",cat:"كوش دايرة", price:0, featured:false, desc:"شجر أبيض وأرضية نور وبنش بيج" },
    { id:"g10", slug:"koshet-wefoundlove-setara",   name:"كوشة نيون We Found Love وستارة نور", cat:"خطوبة", price:0, featured:true,  desc:"شجر أبيض وشمعدانات وبنش بيج" },
    { id:"g11", slug:"koshet-wefoundlove-dahaby",   name:"كوشة نيون We Found Love وكرسيين ذهبي", cat:"خطوبة", price:0, featured:false, desc:"إطار زهر أبيض على ستارة تل" },
    { id:"g12", slug:"koshet-setaret-firylight",    name:"كوشة ستارة فيري لايت وبنش فرو",  cat:"خطوبة",     price:0, featured:false, desc:"نيون We Found Love وورد متناثر على الأرض" },
    { id:"g13", slug:"koshet-neon-thestorybegins",  name:"كوشة نيون The Story Begins",     cat:"خطوبة",     price:0, featured:false, desc:"خلفية متضفّرة رمادي وكرسيين أبيض" },
    { id:"g14", slug:"koshet-tol-motadafer-farw",   name:"كوشة تل متضفّر وبنش فرو",        cat:"خطوبة",     price:0, featured:false, desc:"عمودين شجر أبيض وشمعدانات تحت النجفة" },
    { id:"g15", slug:"koshet-marwahet-tol",         name:"كوشة مروحة تل ونيون Better Together", cat:"خطوبة", price:0, featured:false, desc:"تل مفرود بالنور وشجر أبيض على الجانبين" }
  ],

  /* رأي عميلة حقيقي — منقول من رسالة واتساب بعد المناسبة */
  testimonials: [
    { name:"عروسة من عملائنا", event:"كتب كتاب", real:true,
      text:"أنا فوقت بعد الدربكة اللي كانت حصلت والدوشة. حبة أقولك شكرًا جدًا ليكي على صبرك وعلى شغلك، بجد كان تحفة من قبل ما الليل يجي، والكوشة باينة إنها تحفة وجميلة. تسلم إيدك على تعبك معايا ❤️" }
  ],

  bookings: []
};
