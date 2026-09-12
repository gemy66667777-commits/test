/* =============================================================
   V.I.P SILVER — بيانات المتجر (عربي / English)
   كل نص ثنائي اللغة يُكتب هكذا: { ar:'...', en:'...' }
   ============================================================= */

const BRAND = {
  ar:'في آي بي',
  en:'V.I.P SILVER',

  whatsapp:'201156442660',           // رقم استقبال الطلبات (دولي بدون +)
  whatsappShow:'0115 644 2660',

  currency:{ ar:'ج.م', en:'EGP' },
  freeShipFrom: 3000,                // حدّ الشحن المجاني بالجنيه — 0 لإلغائه

  /* حسابات الأدمن: أرقام ثابتة بكلمة مرور ثابتة.
     ⚠️ كلمة المرور مكتوبة هنا داخل ملف يقرأه أي زائر — راجع README. */
  admins:['01156442660','01065434420'],
  adminPass:'654321'
};

/* ------------------------- نصوص الواجهة ------------------------- */
const T = {
  ar:{
    dir:'rtl', other:'EN', otherLabel:'English',
    announce:'شحن لكل المحافظات · <b>مجاناً للطلبات فوق ٣٠٠٠ ج.م</b> · نقش بالاسم مجاناً',
    navShop:'المنتجات', navAbout:'عن المحل', navPerks:'لماذا احنا', navContact:'تواصل معنا',
    heroT:'هدية تتقال عنها', heroEm:'«دي حاجة مميزة»',
    heroLead:'فضة ٩٢٥ بالنقش على الطلب، بوكسات هدايا جاهزة، ساعات وشنط وأحذية — كل حاجة تليق بالمناسبة، وبسعر عادل.',
    heroCta1:'اتفرّج على المنتجات', heroCta2:'اسأل على واتساب',
    m1:'فضة ٩٢٥ مختومة', m2:'نقش بالاسم مجاناً', m3:'الدفع عند الاستلام',
    shopKick:'المعروضات', shopTitle:'منتجاتنا',
    shopLead:'ضيف اللي عاجبك للسلة، ولما تضغط إتمام الطلب هيوصلنا طلبك كامل على واتساب.',
    aboutKick:'عن المحل', aboutTitle:'اسم بنيناه قطعة قطعة',
    aboutBody:'V.I.P SILVER بدأ من فكرة إن الهدية مش بس حاجة بتتشترى — دي حاجة بتفضل مع صاحبها سنين. عشان كده بنشتغل على الفضة عيار ٩٢٥ وبننقشها بإيدينا، وبنختار كل قطعة قبل ما تتعرض. اللي بيشتري مننا مرة بيرجع تاني، ودي أحسن شهادة عندنا.',
    perksKick:'ليه احنا', perksTitle:'اللي بيفرّقنا',
    ctaKick:'تواصل معنا', ctaTitle:'محتار تجيب إيه؟',
    ctaBody:'قولنا المناسبة والميزانية، ونرشّحلك أنسب هدية — من غير أي التزام بالشراء.',
    ctaBtn:'كلّمنا على واتساب',
    ctaWa:'السلام عليكم، محتار في اختيار هدية وعايز ترشيح.',
    askWa:'السلام عليكم، عايز أستفسر عن منتجات V.I.P SILVER.',
    ftrAbout:'هدايا وفضة ٩٢٥ بالنقش على الطلب. الطلب عبر واتساب والتوصيل لكل المحافظات.',
    ftrShop:'المتجر', ftrAll:'كل المنتجات', ftrStore:'المحل', ftrOrder:'الطلب',
    ftrWa:'واتساب', ftrBrowse:'تصفّح المنتجات',
    rights:'V.I.P SILVER — جميع الحقوق محفوظة.', country:'مصر',
    add:'أضف للسلة', added:'اتضاف', addedToast:'اتضاف للسلة', edit:'تعديل',
    cart:'السلة', cartEmptySub:'مفيش منتجات لسه', pieces:'قطعة في السلة',
    cartEmpty:'السلة فاضية.', cartEmptyHint:'ضيف اللي عاجبك وابدأ الطلب.',
    each:'للقطعة', remove:'إزالة', totalLabel:'الإجمالي',
    shipFree:'مبروك! الشحن مجاني على الطلب ده.',
    shipLeft:(n,c)=>`ضيف بـ <b class="num">${n}</b> ${c} وتاخد شحن مجاني.`,
    checkout:'إتمام الطلب عبر واتساب',
    cartNote:'هيفتح واتساب برسالة فيها طلبك كامل — راجعها وابعتها.',
    close:'إغلاق السلة', cartAria:'سلة المشتريات', menu:'القائمة',
    /* الحساب */
    signIn:'تسجيل الدخول', myAcc:'حسابي', adminAcc:'الأدمن',
    authSub:'التسجيل اختياري — تقدر تطلب من غيره عادي.',
    phoneLabel:'رقم الموبايل', phoneHint:'لو عندك حساب هنطلب كلمة المرور، ولو رقم جديد هتختار كلمة مرور جديدة.',
    next:'متابعة', badPhone:'اكتب رقم موبايل مصري صحيح — ١١ رقم يبدأ بـ 010 أو 011 أو 012 أو 015.',
    adminLogin:'دخول الأدمن', adminLoginSub:'حساب أدمن — اكتب كلمة المرور الخاصة بـ ',
    welcomeBack:'أهلاً بعودتك', loginSub:'اكتب كلمة المرور الخاصة بـ ',
    pickPass:'اختر كلمة المرور', pickPassSub:'حساب جديد لـ ',
    pickPassSub2:' — دي هتبقى كلمة السر بتاعتك.',
    pass:'كلمة المرور', passConfirm:'تأكيد كلمة المرور', passPh:'٦ أحرف على الأقل',
    createAcc:'إنشاء الحساب', login:'دخول', changePhone:'تغيير الرقم',
    passShort:'كلمة المرور لازم ٦ أحرف على الأقل.', passMismatch:'كلمتا المرور مش متطابقتين.',
    passWrong:'كلمة المرور غلط.',
    yourAcc:'حسابك', adminAccSub:'حساب أدمن — تقدر تعدّل المنتجات والأسعار.',
    clientAccSub:'حساب عميل.', adminNote:'👑 صلاحيات أدمن مفعّلة. هتلاقي زرار تعديل على كل منتج.',
    logout:'تسجيل الخروج', loggedOut:'تم تسجيل الخروج',
    welcomeAdmin:'أهلاً بيك يا أدمن 👑', accCreated:'تم إنشاء حسابك', welcome:'أهلاً بيك',
    /* الطلب */
    orderTitle:'بيانات الطلب', orderSub:'اكتب بياناتك عشان نقدر نوصّل الطلب — كلها مطلوبة.',
    fName:'الاسم بالكامل', fNamePh:'الاسم زي ما هو في البطاقة',
    fPhone:'رقم الموبايل', fGov:'المحافظة', fGovPick:'اختر المحافظة',
    fAddr:'العنوان بالتفصيل', fAddrPh:'المدينة، الشارع، رقم العمارة والدور والشقة',
    fNote:'ملاحظات (اختياري)', fNotePh:'مثال: النقش المطلوب، أو ميعاد التسليم',
    sendOrder:'تأكيد وإرسال الطلب على واتساب',
    orderNote:'هيفتح واتساب برسالة فيها الطلب وبياناتك — راجعها وابعتها.',
    errName:'اكتب اسمك بالكامل.', errGov:'اختر المحافظة.',
    errAddr:'اكتب العنوان بالتفصيل عشان نقدر نوصّل.',
    orderSent:'تمام! راجع الرسالة في واتساب وابعتها',
    msgHead:'طلب جديد من موقع V.I.P SILVER', msgCount:'عدد القطع', msgTotal:'الإجمالي',
    msgShip:'الشحن', msgFree:'مجاني', msgCustomer:'بيانات العميل:',
    msgName:'الاسم', msgPhone:'الموبايل', msgGov:'المحافظة', msgAddr:'العنوان', msgNote:'ملاحظات',
    /* الأدمن */
    adminBar:'👑 أنت داخل كـ <b>أدمن</b> — تقدر تعدّل أي منتج أو تضيف جديد.',
    addProduct:'+ إضافة منتج', resetProducts:'استرجاع القائمة الأصلية',
    editTitle:'تعديل المنتج', addTitle:'إضافة منتج',
    editSub:'التعديلات بتتحفظ على المتصفح ده — راجع ملاحظة README.',
    fNameAr:'اسم المنتج (عربي)', fNameEn:'اسم المنتج (إنجليزي)',
    fDescAr:'الوصف (عربي)', fDescEn:'الوصف (إنجليزي)',
    fPrice:'السعر', fCat:'القسم', fBadgeAr:'شارة (عربي)', fBadgeEn:'شارة (إنجليزي)',
    fImage:'الصورة', fImageHas:'فيه صورة حالياً — اختَر ملف جديد لو عايز تغيّرها.',
    fImageNew:'اختر صورة مربّعة للنتيجة الأفضل.', imgReady:'الصورة جاهزة — اضغط حفظ.',
    imgFail:'مقدرتش أقرأ الصورة دي.', save:'حفظ', del:'حذف المنتج',
    errNameReq:'اكتب اسم المنتج.', errPrice:'اكتب سعر صحيح.', errImg:'اختر صورة للمنتج.',
    errFull:'مساحة المتصفح امتلأت — جرّب صورة أصغر أو احذف منتجات.',
    savedNew:'تم إضافة المنتج', savedEdit:'تم حفظ التعديلات', deleted:'تم حذف المنتج',
    confirmDel:p=>'متأكد إنك عايز تحذف «'+p+'»؟',
    confirmReset:'هيرجع كل المنتجات لحالتها الأصلية ويلغي تعديلاتك. تمام؟',
    resetDone:'رجعت القائمة الأصلية', emptyCat:'مفيش منتجات في القسم ده حالياً.'
  },
  en:{
    dir:'ltr', other:'ع', otherLabel:'العربية',
    announce:'Delivery across Egypt · <b>Free over EGP 3,000</b> · Free name engraving',
    navShop:'Shop', navAbout:'About', navPerks:'Why us', navContact:'Contact',
    heroT:'A gift people call', heroEm:'“something special”',
    heroLead:'925 silver engraved to order, ready gift boxes, watches, bags and sneakers — everything the occasion deserves, at a fair price.',
    heroCta1:'Browse the shop', heroCta2:'Ask on WhatsApp',
    m1:'Hallmarked 925 silver', m2:'Free name engraving', m3:'Cash on delivery',
    shopKick:'The shop', shopTitle:'Our products',
    shopLead:'Add what you like to the bag — at checkout your full order reaches us on WhatsApp.',
    aboutKick:'About us', aboutTitle:'A name built piece by piece',
    aboutBody:'V.I.P SILVER started from one idea: a gift is not just something you buy — it stays with its owner for years. That is why we work in 925 silver, engrave it by hand, and inspect every piece before it goes on display. People who buy from us once come back, and that is the best testimony we have.',
    perksKick:'Why us', perksTitle:'What sets us apart',
    ctaKick:'Contact us', ctaTitle:'Not sure what to get?',
    ctaBody:'Tell us the occasion and your budget and we will suggest the right gift — with no obligation to buy.',
    ctaBtn:'Talk to us on WhatsApp',
    ctaWa:'Hello, I need a gift recommendation.',
    askWa:'Hello, I would like to ask about V.I.P SILVER products.',
    ftrAbout:'Gifts and 925 silver engraved to order. Order on WhatsApp, delivered across Egypt.',
    ftrShop:'Shop', ftrAll:'All products', ftrStore:'Store', ftrOrder:'Order',
    ftrWa:'WhatsApp', ftrBrowse:'Browse products',
    rights:'V.I.P SILVER — All rights reserved.', country:'Egypt',
    add:'Add to bag', added:'Added', addedToast:'Added to your bag', edit:'Edit',
    cart:'Your bag', cartEmptySub:'Nothing here yet', pieces:'items in your bag',
    cartEmpty:'Your bag is empty.', cartEmptyHint:'Add what you like and start your order.',
    each:'each', remove:'Remove', totalLabel:'Total',
    shipFree:'Nice! Shipping is free on this order.',
    shipLeft:(n,c)=>`Add <b class="num">${n}</b> ${c} more for free shipping.`,
    checkout:'Checkout on WhatsApp',
    cartNote:'WhatsApp will open with your full order — review it, then send.',
    close:'Close bag', cartAria:'Shopping bag', menu:'Menu',
    signIn:'Sign in', myAcc:'My account', adminAcc:'Admin',
    authSub:'Signing in is optional — you can order without an account.',
    phoneLabel:'Mobile number', phoneHint:'If you have an account we will ask for your password; a new number picks a new one.',
    next:'Continue', badPhone:'Enter a valid Egyptian mobile number — 11 digits starting 010, 011, 012 or 015.',
    adminLogin:'Admin sign in', adminLoginSub:'Admin account — enter the password for ',
    welcomeBack:'Welcome back', loginSub:'Enter the password for ',
    pickPass:'Choose a password', pickPassSub:'New account for ',
    pickPassSub2:' — this will be your password.',
    pass:'Password', passConfirm:'Confirm password', passPh:'At least 6 characters',
    createAcc:'Create account', login:'Sign in', changePhone:'Change number',
    passShort:'Password must be at least 6 characters.', passMismatch:'Passwords do not match.',
    passWrong:'Wrong password.',
    yourAcc:'Your account', adminAccSub:'Admin account — you can edit products and prices.',
    clientAccSub:'Customer account.', adminNote:'👑 Admin rights active. You will see an Edit button on every product.',
    logout:'Sign out', loggedOut:'Signed out',
    welcomeAdmin:'Welcome, admin 👑', accCreated:'Account created', welcome:'Welcome',
    orderTitle:'Order details', orderSub:'Fill in your details so we can deliver — all required.',
    fName:'Full name', fNamePh:'Your name as on your ID',
    fPhone:'Mobile number', fGov:'Governorate', fGovPick:'Select governorate',
    fAddr:'Full address', fAddrPh:'City, street, building, floor and flat number',
    fNote:'Notes (optional)', fNotePh:'e.g. the engraving you want, or a delivery date',
    sendOrder:'Confirm and send on WhatsApp',
    orderNote:'WhatsApp will open with your order and details — review it, then send.',
    errName:'Enter your full name.', errGov:'Select your governorate.',
    errAddr:'Enter a full address so we can deliver.',
    orderSent:'Done! Review the message in WhatsApp and send it',
    msgHead:'New order from the V.I.P SILVER website', msgCount:'Items', msgTotal:'Total',
    msgShip:'Shipping', msgFree:'Free', msgCustomer:'Customer details:',
    msgName:'Name', msgPhone:'Mobile', msgGov:'Governorate', msgAddr:'Address', msgNote:'Notes',
    adminBar:'👑 You are signed in as <b>admin</b> — you can edit any product or add a new one.',
    addProduct:'+ Add product', resetProducts:'Restore original list',
    editTitle:'Edit product', addTitle:'Add product',
    editSub:'Changes are saved in this browser only — see the README note.',
    fNameAr:'Product name (Arabic)', fNameEn:'Product name (English)',
    fDescAr:'Description (Arabic)', fDescEn:'Description (English)',
    fPrice:'Price', fCat:'Category', fBadgeAr:'Badge (Arabic)', fBadgeEn:'Badge (English)',
    fImage:'Image', fImageHas:'There is an image already — pick a new file to replace it.',
    fImageNew:'A square image gives the best result.', imgReady:'Image ready — press Save.',
    imgFail:'Could not read that image.', save:'Save', del:'Delete product',
    errNameReq:'Enter the product name.', errPrice:'Enter a valid price.', errImg:'Choose an image.',
    errFull:'Browser storage is full — try a smaller image or delete some products.',
    savedNew:'Product added', savedEdit:'Changes saved', deleted:'Product deleted',
    confirmDel:p=>'Delete “'+p+'”?',
    confirmReset:'This restores all products and discards your edits. Continue?',
    resetDone:'Original list restored', emptyCat:'No products in this category yet.'
  }
};

/* ------------------------- الأقسام ------------------------- */
const CATEGORIES = [
  { id:'all',    label:{ ar:'الكل',                en:'All' } },
  { id:'silver', label:{ ar:'الفضة',               en:'Silver' } },
  { id:'shoes',  label:{ ar:'الأحذية',             en:'Footwear' } },
  { id:'gifts',  label:{ ar:'الهدايا والإكسسوار',  en:'Gifts & Accessories' } }
];

/* ------------------------- المحافظات ------------------------- */
const GOVS = [
  {ar:'القاهرة',en:'Cairo'},{ar:'الجيزة',en:'Giza'},{ar:'الإسكندرية',en:'Alexandria'},
  {ar:'القليوبية',en:'Qalyubia'},{ar:'الشرقية',en:'Sharqia'},{ar:'الدقهلية',en:'Dakahlia'},
  {ar:'الغربية',en:'Gharbia'},{ar:'المنوفية',en:'Menoufia'},{ar:'البحيرة',en:'Beheira'},
  {ar:'كفر الشيخ',en:'Kafr El Sheikh'},{ar:'دمياط',en:'Damietta'},{ar:'بورسعيد',en:'Port Said'},
  {ar:'الإسماعيلية',en:'Ismailia'},{ar:'السويس',en:'Suez'},{ar:'شمال سيناء',en:'North Sinai'},
  {ar:'جنوب سيناء',en:'South Sinai'},{ar:'الفيوم',en:'Fayoum'},{ar:'بني سويف',en:'Beni Suef'},
  {ar:'المنيا',en:'Minya'},{ar:'أسيوط',en:'Assiut'},{ar:'سوهاج',en:'Sohag'},{ar:'قنا',en:'Qena'},
  {ar:'الأقصر',en:'Luxor'},{ar:'أسوان',en:'Aswan'},{ar:'البحر الأحمر',en:'Red Sea'},
  {ar:'مطروح',en:'Matrouh'},{ar:'الوادي الجديد',en:'New Valley'}
];

/* -------------------------- المنتجات -------------------------- */
const DEFAULT_PRODUCTS = [
  { id:'v01', cat:'gifts', price:2450, img:'assets/img/gift-box.jpg',
    name:{ar:'بوكس هدية VIP الفاخر',en:'VIP Luxury Gift Box'},
    desc:{ar:'بوكس متكامل يضم عطر سيلفر سنت وساعة وإسورة وبلاكة بالاسم، بتغليف جاهز للإهداء.',
          en:'A complete box with Silver Scent perfume, a watch, a bracelet and a name plate, gift-wrapped and ready.'},
    badge:{ar:'الأكثر طلباً',en:'Bestseller'} },

  { id:'v02', cat:'gifts', price:3900, img:'assets/img/watch-set.jpg',
    name:{ar:'طقم ساعة وإسورة',en:'Watch & Bracelet Set'},
    desc:{ar:'ساعة كلاسيك بإطار مزدوج اللون مع إسورة مطابقة — إطلالة رسمية تليق بالمناسبات.',
          en:'A classic two-tone watch with a matching bracelet — a formal look for occasions.'} },

  { id:'v03', cat:'silver', price:850, img:'assets/img/ring-arabic.jpg',
    name:{ar:'خاتم فضة منقوش بالعربي',en:'Arabic Engraved Ring'},
    desc:{ar:'فضة ٩٢٥ عيار عالٍ بنقش عربي يدوي، ويمكن كتابة العبارة التي تختارها.',
          en:'Fine 925 silver with hand-cut Arabic engraving — we write the phrase you choose.'},
    badge:{ar:'حسب الطلب',en:'Made to order'} },

  { id:'v04', cat:'silver', price:1150, img:'assets/img/ring-name.jpg',
    name:{ar:'خاتم فضة عريض بالاسم',en:'Wide Name Ring'},
    desc:{ar:'خاتم عريض من فضة ٩٢٥ منقوش بالاسم مع زخرفة جانبية، متوفر بكل المقاسات.',
          en:'A wide 925 silver band engraved with a name and side patterning, in every size.'} },

  { id:'v05', cat:'silver', price:980, img:'assets/img/ring-spinner.jpg',
    name:{ar:'خاتم فضة دوّار',en:'Spinner Ring'},
    desc:{ar:'خاتم بحلقة دوّارة منقوشة — قطعة مريحة ومميزة للاستخدام اليومي.',
          en:'An engraved spinning band — comfortable and distinctive for everyday wear.'} },

  { id:'v06', cat:'silver', price:1650, img:'assets/img/couple-rings.jpg',
    name:{ar:'دبل فضة للثنائي',en:'Couple Rings'},
    desc:{ar:'دبلتان من فضة ٩٢٥ تُنقش عليهما الأحرف الأولى لكما — هدية الخطوبة الأشهر لدينا.',
          en:'Two 925 silver bands engraved with your initials — our most popular engagement gift.'},
    badge:{ar:'هدية مثالية',en:'Perfect gift'} },

  { id:'v07', cat:'silver', price:920, img:'assets/img/necklace-letter.jpg',
    name:{ar:'سلسلة فضة بحرف',en:'Letter Necklace'},
    desc:{ar:'سلسلة فضة ناعمة بدلاية على شكل حرف — اختاري الحرف الذي يعنيك.',
          en:'A fine silver chain with a letter pendant — choose the letter that means something.'} },

  { id:'v08', cat:'silver', price:48000, img:'assets/img/silver-bar.jpg',
    name:{ar:'سبيكة فضة ١ كيلو — نقاء ٩٩٩',en:'1 Kilo Fine Silver 999'},
    desc:{ar:'سبيكة فضة خالصة بنقاء ٩٩٩ وختم معتمد — للاقتناء والاستثمار.',
          en:'A pure 999 silver bar with a certified hallmark — to keep or to invest.'},
    badge:{ar:'استثمار',en:'Investment'} },

  { id:'v09', cat:'gifts', price:2850, img:'assets/img/bag-coach.jpg',
    name:{ar:'شنطة COACH',en:'COACH Tote Bag'},
    desc:{ar:'شنطة توت أنيقة بمقاس عملي وخامة متينة، تناسب الشغل والخروج.',
          en:'An elegant tote in a practical size and durable material, for work and going out.'} },

  { id:'v10', cat:'shoes', price:1950, img:'assets/img/sneaker-white.jpg',
    name:{ar:'سنيكرز إير ماكس — أبيض',en:'Air Max — White'},
    desc:{ar:'سنيكرز بنعل هوائي مريح وخامة خفيفة، متوفر من مقاس ٣٩ إلى ٤٥.',
          en:'Air-cushioned sneakers in a light material, sizes 39 to 45.'} },

  { id:'v11', cat:'shoes', price:1950, img:'assets/img/sneaker-yellow.jpg',
    name:{ar:'سنيكرز إير ماكس — أصفر',en:'Air Max — Yellow'},
    desc:{ar:'لون جريء بنعل هوائي مريح — الأكثر طلباً بين الشباب هذا الموسم.',
          en:'A bold colour on a comfortable air sole — this season’s most wanted.'} },

  { id:'v12', cat:'shoes', price:2050, img:'assets/img/sneaker-pastel.jpg',
    name:{ar:'سنيكرز إير ماكس — باستيل',en:'Air Max — Pastel'},
    desc:{ar:'تدرّجات باستيل هادئة بنعل هوائي، مناسب للبنات والولاد.',
          en:'Soft pastel tones on an air sole, for women and men alike.'},
    badge:{ar:'جديد',en:'New'} },

  { id:'v13', cat:'shoes', price:1450, img:'assets/img/shoe-black.jpg',
    name:{ar:'حذاء كاجوال أسود',en:'Black Casual'},
    desc:{ar:'حذاء كاجوال أسود بتصميم بسيط يناسب الشغل واللبس اليومي.',
          en:'A simple black casual shoe for work and everyday wear.'} },

  { id:'v14', cat:'shoes', price:1890, img:'assets/img/sneaker-red.jpg',
    name:{ar:'سنيكرز أبيض وأحمر',en:'White & Red Sneaker'},
    desc:{ar:'تصميم رياضي بخطوط حمراء ونعل مرتفع مريح للمشي الطويل.',
          en:'A sporty design with red lines and a raised sole built for long walks.'} },

  { id:'v15', cat:'shoes', price:2100, img:'assets/img/sneaker-pink.jpg',
    name:{ar:'سنيكرز إير ماكس — وردي',en:'Air Max — Pink'},
    desc:{ar:'إصدار وردي بنعل هوائي ولمسات مطبوعة — إطلالة لافتة ومريحة.',
          en:'A pink edition on an air sole with printed details — striking and comfortable.'} }
];

/* ------------------------- مزايا المتجر ------------------------- */
const PERKS = [
  { icon:'shield', title:{ar:'فضة ٩٢٥ مضمونة',en:'Guaranteed 925 silver'},
    text:{ar:'كل قطعة مختومة، ومعها ضمان استبدال إن لم تطابق الوصف.',
          en:'Every piece is hallmarked, with an exchange guarantee if it does not match.'} },
  { icon:'pen', title:{ar:'نقش بالاسم مجاناً',en:'Free engraving'},
    text:{ar:'اكتب الاسم أو العبارة وننقشها لك قبل التسليم دون رسوم.',
          en:'Send the name or phrase and we engrave it before delivery at no cost.'} },
  { icon:'truck', title:{ar:'شحن لكل المحافظات',en:'Nationwide delivery'},
    text:{ar:'توصيل خلال ٢–٥ أيام، ومجاناً للطلبات فوق ٣٠٠٠ ج.م.',
          en:'Delivered in 2–5 days, free on orders over EGP 3,000.'} },
  { icon:'gift', title:{ar:'تغليف هدية أنيق',en:'Elegant gift wrap'},
    text:{ar:'علبة وتغليف يليقان بالمناسبة مع كل طلب.',
          en:'A box and wrapping worthy of the occasion with every order.'} }
];
