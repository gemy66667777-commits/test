# الدرس الأول: المتجهات والسرعة النسبية
## Vectors & Relative Velocity — Grade 11 (تانية ثانوي لغات)

> **الزمن المقترح:** حصتين (90 دقيقة) + حصة مسائل
> **المطلوب على السبورة:** مسطرة، منقلة، ألوان (أحمر للمحصلة Resultant، أزرق للمركبات Components)
> **طريقة الشرح:** الكلام عربي، وكل المصطلحات والقوانين والمسائل English زي ما هي في الكتاب.

---

## 🎯 Lesson Objectives (اكتبهم على السبورة من الأول)

بنهاية الدرس الطالب يقدر:
1. يفرق بين **Scalar quantity** و **Vector quantity**.
2. يجمع ويطرح متجهين بيانياً (Triangle & Parallelogram rules) وجبرياً.
3. يستخدم قانون المحصلة `R = √(A² + B² + 2AB cos θ)`.
4. يحلل متجه إلى مركبتين متعامدتين (**Resolution into components**).
5. يوجد محصلة أكتر من متجهين بطريقة المركبات.
6. يعرّف **Frame of reference** ويحسب **Relative velocity** في حالات: نفس الاتجاه، اتجاهين متضادين، متعامدين.
7. يحل مسائل القارب والنهر (Boat–River) والمطر والراكب (Rain–Man).

---

# 🔵 الجزء الأول: Vectors (المتجهات) — 35 دقيقة

## 1) Opening Hook (3 دقايق) — متبدأش بتعريف

**قول للفصل:**
> "لو أنا قلت لك: امشي 100 متر… تعرف توصل فين؟"
> سيبهم يجاوبوا. "لأ طبعًا، لإن ناقصني حاجة… الاتجاه. لكن لو قلت لك درجة حرارة الأوضة 25°C — محتاج اتجاه؟ لأ. إذن في الفيزياء عندنا نوعين من الكميات."

**اكتب على السبورة:**

| Scalar Quantity (كمية قياسية) | Vector Quantity (كمية متجهة) |
|---|---|
| تتحدد بالمقدار فقط (magnitude only) | تتحدد بالمقدار والاتجاه (magnitude + direction) |
| Mass, Time, Temperature, Distance, Speed, Energy, Work, Power, Density | Displacement, Velocity, Acceleration, Force, Weight, Momentum, Torque |
| تُجمع جمع عادي (algebraic addition) | تُجمع جمع متجهي (vector addition) |

> ⚠️ **نقطة امتحان دايماً بتيجي:** `Distance` (scalar) مقابل `Displacement` (vector)، و `Speed` (scalar) مقابل `Velocity` (vector).
> **مثال سريع اسأله:** طالب لف ملعب دائري نصف قطره 7 m ورجع نفس النقطة.
> - Distance = محيط الدايرة = 2πr = 44 m
> - Displacement = **zero** (لإنه رجع نقطة البداية)
> - Average speed ≠ 0 ، Average velocity = **zero**

---

## 2) تمثيل المتجه — Representation (4 دقايق)

**ارسم على السبورة سهم:**
- طول السهم (length) ⟶ يمثل **the magnitude** حسب مقياس رسم (scale).
- اتجاه السهم (arrow head) ⟶ يمثل **the direction**.
- يُرمز للمتجه بـ **A⃗** ولمقداره بـ **|A⃗|** أو **A**.

**مفاهيم لازم تتقال بسرعة:**
- **Equal vectors:** نفس المقدار ونفس الاتجاه (حتى لو في مكانين مختلفين).
- **Negative vector (−A⃗):** نفس المقدار واتجاه معاكس.
- **Unit vector:** متجه مقداره = 1 ويحدد الاتجاه بس، ورموزه `î, ĵ` في اتجاه x و y.
  - أي متجه ممكن يتكتب: **A⃗ = Aₓ î + A_y ĵ**

---

## 3) Vector Addition — جمع المتجهات (12 دقيقة)

### (a) Triangle Rule — قاعدة المثلث
> "ارسم المتجه الأول، وابدأ الثاني من نهاية الأول (head to tail)، والمحصلة هي السهم من بداية الأول لنهاية الثاني."

### (b) Parallelogram Rule — قاعدة متوازي الأضلاع
> "ارسم المتجهين من نفس نقطة البداية (tail to tail)، كمّل متوازي أضلاع، والمحصلة هي القطر الخارج من نقطة البداية."

### (c) Polygon Rule — قاعدة المضلع
> لأكتر من متجهين: كل متجه يبدأ من نهاية اللي قبله، والمحصلة من بداية الأول لنهاية الآخر.
> 💡 **لو المتجهات كوّنت شكل مقفول (closed polygon) ⟹ المحصلة = zero ⟹ الجسم في اتزان (equilibrium).**

### 📐 القانون العام (احفظه واكتبه بلون مميز):

لو عندنا متجهين **A** و **B** الزاوية بينهم **θ**:

```
R = √( A² + B² + 2AB cos θ )        ← magnitude of the resultant

tan α = ( B sin θ ) / ( A + B cos θ )   ← direction, α is the angle between R and A
```

### 🔍 Special Cases (دي اللي بتيجي في الاختيار من متعدد):

| الحالة | θ | R | ملاحظة |
|---|---|---|---|
| نفس الاتجاه (same direction) | 0° | `R = A + B` | **Maximum resultant** |
| اتجاهين متضادين (opposite) | 180° | `R = |A − B|` | **Minimum resultant** |
| متعامدين (perpendicular) | 90° | `R = √(A² + B²)` | `tan α = B/A` |

> **سؤال للفصل:** قوتين 6 N و 8 N — إيه أكبر وأصغر محصلة ممكنة؟
> الإجابة: max = 14 N ، min = 2 N ⟹ **المحصلة لازم تكون بين 2 N و 14 N**.
> فلو حد قالك المحصلة = 20 N ⟹ مستحيل ❌

---

### ✏️ Example 1 (على السبورة)
> Two forces of 6 N and 8 N act at a point, perpendicular to each other. Find the resultant.

**Solution:**
```
R = √(6² + 8²) = √(36 + 64) = √100 = 10 N
tan α = 8/6 = 1.333  ⟹  α = 53°  (from the 6 N force)
```
✅ **Answer:** 10 N at 53° from the 6 N force.

---

### ✏️ Example 2
> Two forces 5 N and 3 N act at a point with an angle of 60° between them. Find the magnitude and direction of the resultant.

**Solution:**
```
R = √(5² + 3² + 2 × 5 × 3 × cos 60°)
R = √(25 + 9 + 30 × 0.5) = √(34 + 15) = √49 = 7 N

tan α = (3 sin 60°) / (5 + 3 cos 60°) = (3 × 0.866) / (5 + 1.5) = 2.598 / 6.5 = 0.3997
α = 21.8°
```
✅ **Answer:** R = 7 N at 21.8° from the 5 N force.

---

## 4) Vector Subtraction — طرح المتجهات (5 دقايق)

> **الفكرة كلها سطر واحد:** الطرح = جمع للمعكوس.

```
A⃗ − B⃗ = A⃗ + ( −B⃗ )
```

**على السبورة:** اعكس اتجاه B وبعدين اجمع عادي بقاعدة المثلث.

```
|A⃗ − B⃗| = √( A² + B² − 2AB cos θ )
```

> ⚠️ لاحظ الإشارة بقت **ناقص** قدام `2AB cos θ`. ده أكتر مكان الطلبة بتغلط فيه.
> وده بالظبط اللي هنستخدمه في **Relative Velocity** بعد شوية… فخلي بالك من السطر ده.

---

## 5) Resolution of a Vector — تحليل المتجه (10 دقايق)

> "الجمع بيدمج متجهين في واحد. التحليل عكسه تماماً: بياخد متجه واحد ويفككه لمتجهين متعامدين."

**ارسم متجه A مايل بزاوية θ على المحور الأفقي:**

```
Aₓ = A cos θ        ← horizontal component (المركبة الأفقية)
A_y = A sin θ       ← vertical component (المركبة الرأسية)

A = √( Aₓ² + A_y² )        tan θ = A_y / Aₓ
```

> 🔑 **قاعدة ذهبية قولها كتير:** *"المركبة الملاصقة للزاوية = cos، والمركبة المقابلة للزاوية = sin."*
> عشان لو الزاوية اتقاست من المحور الرأسي، الـ sin والـ cos **بيتبدلوا**.

### ✏️ Example 3
> A force of 100 N acts at 30° above the horizontal. Find its components.

```
Fₓ = 100 cos 30° = 100 × 0.866 = 86.6 N
F_y = 100 sin 30° = 100 × 0.5 = 50 N
```

---

## 6) Resultant of More Than Two Vectors — طريقة المركبات (8 دقايق)

**الخطوات (اكتبها مرقمة، الطلبة بتحبها كده):**
1. حلل كل متجه لمركبتين x و y.
2. `Rₓ = ΣAₓ` (اجمع كل المركبات الأفقية مع مراعاة الإشارة).
3. `R_y = ΣA_y`.
4. `R = √(Rₓ² + R_y²)`
5. `tan θ = R_y / Rₓ`

> **اتفاق الإشارات (sign convention):** يمين (+) / شمال (−) ، لأعلى (+) / لأسفل (−).

### ✏️ Example 4
> Three forces act at a point: 10 N along the +x axis, 20 N at 60° above the +x axis, and 15 N along the −x axis. Find the resultant.

**Solution:**
```
Rₓ = 10 + 20 cos 60° − 15 = 10 + 10 − 15 = 5 N
R_y = 0  + 20 sin 60° + 0  = 17.32 N

R = √(5² + 17.32²) = √(25 + 300) = √325 = 18.03 N
tan θ = 17.32 / 5 = 3.464   ⟹  θ = 73.9°
```
✅ **Answer:** R ≈ 18 N at 73.9° above the +x axis.

---
---

# 🟢 الجزء الثاني: Relative Velocity (السرعة النسبية) — 40 دقيقة

## 7) Opening Hook (3 دقايق) — دي أحلى حتة في الدرس

**قول للفصل:**
> "انت قاعد في القطار، والقطار ماشي 100 km/h. اسألك: انت سرعتك كام؟"
> هيقولوا 100. قولهم:
> "طب لو سألت الراكب اللي قاعد جنبك — هيقول إن سرعتك **zero**! انت ساكن بالنسبة له خالص.
> يبقى مين الصح؟ **الاتنين صح**. لإن السرعة معناها لا شيء من غير ما تقول **بالنسبة لمين**. وده اللي اسمه Frame of Reference."

**اكتب التعريفات:**
- **Frame of reference (الإطار المرجعي):** الجسم أو النظام اللي بننسب له الحركة.
- **Relative velocity (السرعة النسبية):** سرعة جسم بالنسبة لمراقب متحرك (moving observer).

---

## 8) The Master Equation — القانون الأساسي (5 دقايق)

> ⭐ **اكتبه بلون مختلف وحوّطه، وقول: "ده القانون الوحيد في الحتة دي، وكل الباقي حالات خاصة منه."**

```
v⃗(A relative to B)  =  v⃗A  −  v⃗B

              v⃗_AB = v⃗A − v⃗B
```

**اقرأها بصوت عالي مع الفصل:**
> "سرعة A بالنسبة لـ B = سرعة A ناقص سرعة B — **طرح متجهي مش عددي**."

> 🔑 **تريك يثبّتها في دماغهم:** الرموز بتتقرا من الشمال لليمين: `v_AB` ⟸ "A relative to B" ⟸ `v_A − v_B`.
> وبرضه: **v⃗_AB = − v⃗_BA** (نفس المقدار، اتجاه معاكس).

---

## 9) Case 1 — Same Direction (نفس الاتجاه) — 6 دقايق

```
v_AB = v_A − v_B          (الاتجاهين نفس الإشارة)
```

### ✏️ Example 5
> Car A moves at 72 km/h and car B moves at 54 km/h, both in the same direction. Find the velocity of A relative to B, and of B relative to A.

**Solution — حوّل للـ SI الأول (دي عادة لازم تزرعها فيهم):**
```
72 km/h = 72 × (1000/3600) = 20 m/s
54 km/h = 54 × (1000/3600) = 15 m/s

v_AB = 20 − 15 = +5 m/s   (A يتحرك للأمام بالنسبة لـ B بسرعة 5 m/s)
v_BA = 15 − 20 = −5 m/s   (B يتحرك للخلف بالنسبة لـ A)
```

**المعنى الفيزيائي (قوله بالعامية):**
> "لو انت في العربية B، هتشوف العربية A ماشية قدامك ببطء شديد — 5 m/s بس. مش 20."

**Extension:** لو A ورا B بـ 100 m، هتلحقه بعد كام؟ `t = 100 / 5 = 20 s`

---

## 10) Case 2 — Opposite Directions (اتجاهين متضادين) — 6 دقايق

```
v_AB = v_A − (−v_B) = v_A + v_B
```

### ✏️ Example 6
> Two cars approach each other on a straight road, at 20 m/s and 15 m/s. The distance between them is 350 m. Find the relative velocity and the time before they meet.

```
v_AB = 20 − (−15) = 35 m/s
t = 350 / 35 = 10 s
```
✅ **Answer:** 35 m/s ، وبيتقابلوا بعد 10 s.

> ⚠️ **أشهر غلطة:** الطالب بيجمع في نفس الاتجاه ويطرح في الاتجاه المضاد. اعكسها قدامهم بالقانون نفسه:
> القانون طرح **دايماً**، بس الإشارة هي اللي بتقلبه لجمع. متحفظوش حالتين — احفظوا قانون واحد وإشارة صح.

---

## 11) Case 3 — Perpendicular Velocities (متعامدتين) — 7 دقايق

```
v_AB = √( v_A² + v_B² )        tan θ = v_B / v_A
```

### ✏️ Example 7
> Car A moves east at 30 m/s and car B moves north at 40 m/s. Find the velocity of A relative to B.

```
v⃗_AB = v⃗A − v⃗B = (30 east) + (40 south)
|v_AB| = √(30² + 40²) = √(900 + 1600) = 50 m/s
tan θ = 40/30 ⟹ θ = 53° south of east
```
✅ **Answer:** 50 m/s in a direction 53° south of east.

> 💡 خلي بالهم إن الاتجاه بقى **جنوب** الشرق، لأننا عكسنا اتجاه B لما طرحناه.

---

## 12) Application 1 — Boat & River (القارب والنهر) — 8 دقايق

> دي أكتر مسألة بتتكرر في الامتحانات. ارسم النهر على السبورة بضفتين.

**المعطيات النموذجية:** سرعة القارب بالنسبة للماء `v_b`، سرعة التيار `v_r`، عرض النهر `d`.

### الحالة (a): القارب يوجّه عمودي على الضفة (aims straight across)

```
Resultant velocity = √( v_b² + v_r² )
Time to cross      = d / v_b          ← التيار مالوش أي تأثير على الزمن!
Drift (الانحراف)   = v_r × t
```

### ✏️ Example 8
> A boat can move at 4 m/s in still water. It crosses a river 80 m wide, aiming perpendicular to the bank. The river flows at 3 m/s. Find: (i) the resultant velocity, (ii) the time to cross, (iii) the drift downstream.

```
(i)   v = √(4² + 3²) = 5 m/s , at tan θ = 3/4 ⟹ θ = 36.9° from the perpendicular
(ii)  t = 80 / 4 = 20 s
(iii) drift = 3 × 20 = 60 m
```

> ❗ **النقطة الذهبية:** الزمن = العرض ÷ **المركبة العمودية بس** (4 مش 5). التيار بيحرك القارب مع النهر، مش بيقرّبه للضفة التانية.

### الحالة (b): القارب عايز يعبر **مباشرة** أمام النقطة المقابلة (straight across, zero drift)

> لازم يميل عكس التيار بزاوية α:

```
sin α = v_r / v_b                    ← α upstream from the perpendicular
Resultant (actual) speed = √( v_b² − v_r² )
Time = d / √( v_b² − v_r² )
```

**بنفس أرقام المثال:**
```
sin α = 3/4 = 0.75  ⟹ α = 48.6° upstream
v = √(16 − 9) = √7 = 2.65 m/s
t = 80 / 2.65 = 30.2 s      (أطول من 20 s — ثمن إنه وصل مظبوط)
```

---

## 13) Application 2 — Rain & Man (المطر والراكب) — 5 دقايق

> "ليه لما بتجري تحت المطر، المطر بيضرب في وشك مش في راسك؟"

**المطر بينزل رأسي بسرعة `v_r`، والشخص بيتحرك أفقي بسرعة `v_m`:**

```
v⃗(rain relative to man) = v⃗_rain − v⃗_man
|v_rm| = √( v_r² + v_m² )
tan θ = v_m / v_r        ← الزاوية عن الرأسي، والمطر بيبان مايل جهة الحركة
```

### ✏️ Example 9
> Rain falls vertically at 8.66 m/s. A man runs horizontally at 5 m/s. Find the velocity of the rain relative to the man.

```
|v_rm| = √(8.66² + 5²) = √(75 + 25) = 10 m/s
tan θ = 5 / 8.66 = 0.577 ⟹ θ = 30° from the vertical
```
✅ يعني لازم يميل الشمسية 30° **قدام** (في اتجاه حركته).

---

## ⚠️ Common Mistakes — حذّرهم منها بصوت عالي (4 دقايق)

1. جمع المتجهات **جبرياً**: `5 N + 3 N = 8 N` دايماً ❌ — ده صح بس لو θ = 0°.
2. نسيان تحويل `km/h → m/s` (اقسم على 3.6).
3. في السرعة النسبية: استخدام الجمع والطرح بالعشوائي بدل قانون واحد + sign convention.
4. في مسألة النهر: قسمة العرض على **المحصلة** (5) بدل سرعة القارب (4).
5. خلط `sin` و `cos` لما الزاوية تتقاس من الرأسي.
6. كتابة المحصلة من غير **اتجاه** — الإجابة ناقصة والدرجة بتضيع.

---

## 📝 Homework / Classwork

1. Two forces of 7 N and 24 N act perpendicular to each other. Find the resultant. *(Ans: 25 N, 73.7°)*
2. Two vectors of magnitudes 10 and 10 have a resultant of 10. Find the angle between them. *(Ans: 120°)*
3. A force of 200 N acts at 60° to the horizontal. Find its horizontal and vertical components. *(Ans: 100 N, 173.2 N)*
4. A train moves at 90 km/h. A man walks inside it at 1 m/s in the direction of motion. Find his velocity relative to the ground. *(Ans: 26 m/s)*
5. A boat with speed 5 m/s in still water crosses a 100 m wide river flowing at 3 m/s, aiming perpendicular. Find the time of crossing and the drift. *(Ans: 20 s, 60 m)*
6. Repeat (5) if the boat must land exactly opposite the starting point. *(Ans: α = 36.9° upstream, v = 4 m/s, t = 25 s)*
7. Two cars move at 25 m/s north and 25 m/s east. Find the velocity of the first relative to the second. *(Ans: 35.4 m/s, 45° north of west)*

---

## 🔚 Closing (2 دقيقة)

> "خدوا المفتاحين بتوع الدرس معاكم:
> **(1)** المتجهات بتتجمع بالرسم أو بالمركبات — مش بالجمع العادي أبداً.
> **(2)** السرعة النسبية = طرح متجهي: `v_AB = v_A − v_B`. قانون واحد بس، وشغل صح على الإشارات.
> والدرس الجاي هنستخدم **تحليل المتجهات** بالظبط اللي اتعلمناه النهاردة في **المقذوفات — Projectiles**، فاللي مش فاهم التحليل هيتوه معايا الحصة الجاية."

