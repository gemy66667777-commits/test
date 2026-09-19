# الدرس الثالث: عزم القوة
## Moment of Force (Torque) — Grade 11 (تانية ثانوي لغات)

> **الزمن المقترح:** حصتين (90 دقيقة) + حصة مسائل
> **المطلوب:** مسطرة خشب وقلم كمفصلة (pivot)، مفتاح صواميل (spanner) لو متاح، وزنات صغيرة
> **متطلب سابق:** تحليل المتجهات (الدرس الأول) — لأننا هنحلل القوة المائلة.

---

## 🎯 Lesson Objectives

بنهاية الدرس الطالب يقدر:
1. يعرّف **Moment of force** ويحدد وحدته وطبيعته المتجهة.
2. يحسب العزم لقوة عمودية ولقوة مائلة `M = F L sin θ`.
3. يفهم **moment arm (ذراع القوة)** ويحدده بالرسم.
4. يعرّف **Couple (الازدواج)** ويحسب عزمه.
5. يطبق **شرطي الاتزان** و **Principle of moments**.
6. يحل مسائل القضيب المتزن وإيجاد ردود الأفعال (reactions).

---

## 1) Opening Hook (5 دقايق) — سؤال يفتح دماغهم

**قف عند باب الفصل وقول:**
> "هفتح الباب مرتين. مرة من الطرف البعيد عن المفصلة، ومرة من جنب المفصلة بالظبط."
> (افتحه فعلاً قدامهم مرة من كل مكان.)
> "ليه لما أدفع من جنب المفصلة الباب تقيل جداً، مع إن **نفس القوة**؟"

**النتيجة اللي عايزهم يقولوها:**
> "تأثير القوة في الدوران مش بيعتمد على مقدار القوة بس — بيعتمد كمان على **المسافة من محور الدوران**."

**سؤال تاني:** ليه مفتاح الصواميل الطويل بيفك الصامولة أسهل من القصير؟ ✅ نفس السبب.

> اكتب على السبورة: **Turning effect of a force = Moment**

---

## 2) Definition & Formula (8 دقايق)

**Definition:**
> **Moment of a force** about a point is the product of the force and the perpendicular distance between the line of action of the force and the point (the axis of rotation).

```
M = F × L
```

حيث:
- `M` = moment of force (عزم القوة)
- `F` = force in newtons (N)
- `L` = **moment arm** = the **perpendicular** distance from the axis to the line of action of the force (m)

**Unit:** `N·m` (newton · metre)

> ⚠️ **نبّههم:** الوحدة `N·m` زي وحدة الشغل (Joule) من حيث الأبعاد، **بس مش نفس الكمية ولا نفس الوحدة** — العزم N·m مش Joule أبداً.

**Nature:** عزم القوة **كمية متجهة (vector quantity)**.

**Sign convention (اتفاق الإشارات) — اكتبه وحوّطه:**
```
Anticlockwise moment  ⟹  positive (+)   عكس عقارب الساعة
Clockwise moment      ⟹  negative (−)   مع عقارب الساعة
```

---

## 3) متى يكون العزم = صفر؟ (4 دقايق)

> سؤال بيجي كتير في الاختيار من متعدد.

العزم بيساوي **zero** في حالتين:
1. **`F = 0`** (مفيش قوة أصلاً).
2. **`L = 0`** — يعني **خط عمل القوة يمر بمحور الدوران** (the line of action passes through the axis).

**المثال العملي:** الدفع على المفصلة نفسها ⟹ الباب مش هيتحرك مهما دفعت بقوة.

---

## 4) القوة المائلة — Moment of an inclined force (10 دقايق)

> دي أهم نقطة في الدرس، وأكتر واحدة الطلبة بتغلط فيها.

لو القوة `F` بتأثر على قضيب طوله `L` من محور الدوران، وبتصنع زاوية `θ` مع القضيب:

### الطريقة الأولى: تحليل القوة (Resolving the force)
> حلل القوة لمركبتين: واحدة **عمودية** على القضيب وواحدة **موازية** له.
```
F⊥ = F sin θ     ← دي اللي بتعمل دوران ✅
F∥ = F cos θ     ← دي بتشد أو تضغط القضيب، عزمها = zero ❌

M = F⊥ × L = F L sin θ
```

### الطريقة الثانية: ذراع القوة العمودي (Perpendicular moment arm)
> بدل ما تحلل القوة، مدّ خط عمل القوة وانزل عمود من محور الدوران عليه.
```
L⊥ = L sin θ
M = F × L⊥ = F L sin θ      ← نفس النتيجة ✔
```

```
⭐  M = F L sin θ
```

**حالات خاصة:**
| θ | M | ملاحظة |
|---|---|---|
| 90° | `M = F L` | **أكبر عزم ممكن** (القوة عمودية على القضيب) |
| 0° أو 180° | `M = 0` | القوة على امتداد القضيب — مفيش دوران |

> 💡 **علّمهم:** *"اللي بيلف الجسم هي المركبة **العمودية** بس."*
> وده بيفسر ليه بندفع الباب **عمودي** على سطحه مش بزاوية.

---

## 5) Couple — الازدواج (8 دقايق)

**Definition:**
> A **couple** is a pair of forces, equal in magnitude, opposite in direction, and having **different lines of action** (parallel, not on the same line).

**خصائص الازدواج (اكتبها كنقط):**
- المحصلة `R = F − F = 0` ⟹ **لا يحدث انتقال (no translation)**.
- لكن العزم ≠ صفر ⟹ **يحدث دوران فقط (pure rotation)**.
- عزم الازدواج **ثابت** بالنسبة لأي نقطة في مستواه (independent of the chosen point) — دي نقطة مميزة جداً.

```
Moment of a couple  =  M = F × d
```
حيث `d` = the perpendicular distance between the two lines of action (المسافة العمودية بين خطي عمل القوتين).

**أمثلة من الحياة:** عجلة قيادة السيارة (steering wheel)، فتح الحنفية، مفك البراغي، مفتاح الباب.

---

## 6) شروط الاتزان — Conditions of Equilibrium (8 دقايق)

> "عشان الجسم يبقى متزن تماماً، لازم يحقق شرطين مع بعض — مش شرط واحد."

```
(1)  ΣF = 0        ⟹  no translation (اتزان انتقالي)
     ΣFₓ = 0   and   ΣF_y = 0

(2)  ΣM = 0        ⟹  no rotation (اتزان دوراني)
```

### ⭐ Principle of Moments — قاعدة العزوم

> **When a body is in equilibrium, the sum of the anticlockwise moments about any point equals the sum of the clockwise moments about the same point.**

```
Σ M(anticlockwise) = Σ M(clockwise)
```

### 🧠 أهم تريك في حل المسائل (قوله بصوت عالي مرتين):
> **"اختار نقطة أخذ العزوم بحيث تمر بأكبر عدد من القوى المجهولة — عشان عزمها يبقى zero وتتشال من المعادلة."**

---

## 7) Worked Examples (25 دقيقة)

### ✏️ Example 1 — أبسط تطبيق
> A force of 50 N is applied at the end of a spanner of length 20 cm, perpendicular to it. Find the moment.

```
L = 20 cm = 0.2 m
M = F × L = 50 × 0.2 = 10 N·m
```

---

### ✏️ Example 2 — قوة مائلة
> A force of 100 N acts at the end of a rod of length 2 m, making an angle of 30° with the rod. Find the moment about the other end.

```
M = F L sin θ = 100 × 2 × sin 30° = 100 × 2 × 0.5 = 100 N·m
```
> **اسألهم:** لو نفس القوة بقت عمودية (90°)؟
> `M = 100 × 2 × 1 = 200 N·m` — ضعف العزم بنفس القوة! 💡

---

### ✏️ Example 3 — الأرجوحة (Seesaw)
> A child of weight 400 N sits 1.5 m from the pivot of a seesaw. Where must a second child of weight 300 N sit to balance it?

**Solution — principle of moments:**
```
Anticlockwise = Clockwise
400 × 1.5 = 300 × d
600 = 300 d
d = 2 m
```
✅ **Answer:** على بعد 2 m من المحور، على الجهة المقابلة.
> **لاحظ معاهم:** الأخف بيقعد أبعد. وده هو مبدأ الرافعة (lever) كله.

---

### ✏️ Example 4 — قضيب منتظم وردود الأفعال (المسألة المفتاحية)
> A uniform rod AB of length 4 m and weight 100 N rests horizontally on two supports at its ends A and B. A load of 200 N is placed 1 m from A. Find the reactions at the supports.

> 🖊️ **ارسم الشكل الأول:** القضيب، الوزن 100 N في **المنتصف** (لإنه uniform ⟹ مركز ثقله في المنتصف)، الحمل 200 N على بعد 1 m من A، و R_A و R_B لأعلى.

**Solution:**
```
خد العزوم حول A (عشان R_A عزمها = zero وتختفي):

ΣM about A = 0:
   R_B × 4 = (200 × 1) + (100 × 2)
   4 R_B = 200 + 200 = 400
   R_B = 100 N

من شرط الاتزان الأول:
   R_A + R_B = 100 + 200 = 300 N
   R_A = 300 − 100 = 200 N
```
✅ **Answer:** R_A = 200 N ، R_B = 100 N

> ✔️ **تأكيد سريع علّمهم عليه:** خد العزوم حول B وشوف هتطلع R_A = 200 N برضه.
> ومنطقياً: الحمل أقرب لـ A ⟹ A بتشيل أكتر. ✅

---

### ✏️ Example 5 — قضيب مفصلي (Hinged rod)
> A uniform rod AB of length 3 m and weight 60 N is hinged at A and held horizontal by a vertical force F applied at B. Find F.

```
ΣM about A = 0:
   F × 3 = 60 × 1.5        (وزن القضيب في منتصفه)
   F = 90/3 = 30 N
```

---

### ✏️ Example 6 — ازدواج
> Two parallel forces, each of 20 N, act in opposite directions. The perpendicular distance between their lines of action is 0.5 m. Find the moment of the couple.

```
M = F × d = 20 × 0.5 = 10 N·m
```
> والمحصلة = zero ⟹ الجسم **بيلف في مكانه من غير ما ينتقل**.

---

## ⚠️ Common Mistakes

1. استخدام المسافة **المائلة** بدل المسافة **العمودية** ⟹ نسيان `sin θ`.
2. نسيان **وزن القضيب نفسه** في مسائل القضيب المنتظم — وزنه بيأثر في **المنتصف**.
3. أخذ العزوم حول نقطة عشوائية والدخول في معادلتين مجهولين بدون داعي — اختار النقطة بذكاء.
4. الخلط بين `N·m` (moment) و `Joule` (work).
5. الاعتقاد إن `ΣF = 0` لوحده كفاية للاتزان — لأ، لازم `ΣM = 0` كمان (والازدواج أحسن مثال).
6. إهمال الإشارات (clockwise / anticlockwise) عند الجمع.
7. تحويل السنتيمتر لمتر منسي: `20 cm = 0.2 m` مش 20.
8. استخدام `cos θ` بدل `sin θ` في القوة المائلة — فكّرهم إن المركبة **العمودية** هي اللي بتلف.

---

## 📝 Homework / Classwork

1. A force of 25 N acts perpendicular at 40 cm from the axis. Find the moment. *(Ans: 10 N·m)*
2. A force of 80 N acts at 1.5 m from the pivot, at 60° to the rod. Find the moment. *(Ans: 103.9 N·m)*
3. A boy of weight 500 N sits 2 m from the pivot of a seesaw. Find where a 400 N boy must sit to balance. *(Ans: 2.5 m)*
4. A uniform beam of length 6 m and weight 200 N rests on supports at its ends. A man of weight 600 N stands 2 m from A. Find both reactions. *(Ans: R_A = 500 N, R_B = 300 N)*
5. Two equal and opposite forces of 15 N are separated by 40 cm. Find the moment of the couple. *(Ans: 6 N·m)*
6. A non-uniform rod AB of length 4 m rests on a support 1.5 m from A. A weight of 30 N hangs at A to balance it. If the centre of gravity of the rod is 0.5 m from the support (on the B side), find the weight of the rod. *(Ans: 90 N)*
7. Explain why the moment of a couple is the same about **any** point in its plane. *(إثبات نظري — خليها للمتفوقين)*

---

## 🔚 Closing (2 دقيقة)

> "خدوا المفاتيح التلاتة:
> **(1)** `M = F × L` — والـ `L` دايماً **المسافة العمودية**، ولو القوة مايلة بقى `M = F L sin θ`.
> **(2)** الازدواج: محصلة = صفر، عزم ≠ صفر ⟹ دوران خالص.
> **(3)** الاتزان شرطين مش شرط: `ΣF = 0` **و** `ΣM = 0`.
> وفي المسائل: **اختار نقطة العزوم بحيث تشيل المجهول**، ومتنساش وزن القضيب في منتصفه.
> راجعوا مسألة 4 كويس — دي شكل السؤال اللي بييجي في الامتحان."

