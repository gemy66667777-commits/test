# أدوات البناء

## build-standalone.py

يبني من أي موقع في هذا المستودع **ملف HTML واحد قائم بذاته** يصلح للإرسال
عبر واتساب أو الفتح بدون إنترنت: يحتفظ بالـ `<head>` كاملاً
(`meta charset` و `meta viewport`) ويضمّن CSS و JS والصور داخل الملف.

```bash
python3 tools/build-standalone.py .                out/al-rogi.html
python3 tools/build-standalone.py shatha-almadina  out/shatha-almadina.html
```

> **مهم:** لا تُرسل ملفاً بُني بصيغة الـ Artifact (بدون `<head>`) كملف مستقل —
> المتصفح لن يعرف الترميز فيظهر النص العربي رموزاً غير مفهومة،
> ولن يعرف مقاس الشاشة فيظهر الموقع مصغّراً على الجوال.
> السكربت هنا يتحقق من الأمرين ويفشل إن نقص أحدهما.
