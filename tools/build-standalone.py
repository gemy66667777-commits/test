# -*- coding: utf-8 -*-
"""يبني من مجلد موقع ملف HTML واحد قائم بذاته يصلح للإرسال أو الفتح بدون إنترنت.

يحتفظ بالـ <head> كاملاً (meta charset و meta viewport)، ويضمّن CSS و JS
وكل الصور داخل الملف، ثم يتحقق من سلامة الناتج قبل الكتابة.

    python3 tools/build-standalone.py <مجلد الموقع> <ملف الخرج>
"""
import re, sys, base64, os

def main(root, out_path):
    html = read(os.path.join(root, 'index.html'))
    css  = read(os.path.join(root, 'assets/css/styles.css'))
    data = read(os.path.join(root, 'assets/js/data.js'))
    site = read(os.path.join(root, 'assets/js/site.js'))

    # تضمين الصور أولاً في كل جزء على حدة، حتى تبقى المقارنة النهائية دقيقة
    css, data, site, html = (embed_images(root, t) for t in (css, data, site, html))
    js = data + '\n</script>\n<script>\n' + site

    # ملاحظة مهمة: كل استبدال يمرّ عبر دالة (lambda) وليس نصاً مباشراً،
    # لأن re.sub يفسّر تسلسلات مثل \n و \g داخل نص الاستبدال فيُفسد الكود.
    html = sub_once(html, r'<link rel="stylesheet" href="assets/css/styles\.css">',
                    '<style>\n' + css + '\n</style>', 'وسم CSS')
    html = sub_once(html, r'<script src="assets/js/data\.js"></script>\s*<script src="assets/js/site\.js"></script>',
                    '<script>\n' + js + '\n</script>', 'وسمَي JS')

    check(html, css, data, site)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('%s -> %.2f ميجابايت' % (os.path.basename(out_path), os.path.getsize(out_path)/1048576))

def embed_images(root, text):
    return re.sub(r'assets/img/([A-Za-z0-9_\-.]+\.(?:jpg|jpeg|png|webp))',
                  lambda m: data_uri(os.path.join(root, 'assets/img', m.group(1))), text)

def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()

def sub_once(html, pattern, replacement, what):
    new, n = re.subn(pattern, lambda m: replacement, html, count=1)
    if n != 1:
        raise SystemExit('لم يُعثر على %s في index.html' % what)
    return new

def data_uri(path):
    ext = os.path.splitext(path)[1].lower()
    mime = {'.jpg':'image/jpeg', '.jpeg':'image/jpeg', '.png':'image/png', '.webp':'image/webp'}[ext]
    with open(path, 'rb') as f:
        return 'data:%s;base64,%s' % (mime, base64.b64encode(f.read()).decode())

def check(html, css, data, site):
    """يمنع تكرار الأخطاء التي وقعت سابقاً."""
    if '<meta charset="utf-8">' not in html:
        raise SystemExit('ناقص meta charset — سيظهر النص العربي رموزاً غير مفهومة')
    if 'name="viewport"' not in html:
        raise SystemExit('ناقص meta viewport — ستظهر الصفحة مصغّرة على الجوال')
    if 'assets/' in html:
        raise SystemExit('بقي مرجع خارجي لملف داخل assets/')
    # يجب أن يظهر كل ملف مضمّن كما هو حرفاً بحرف، بلا أي تحويل للتسلسلات
    for name, src in (('styles.css', css), ('data.js', data), ('site.js', site)):
        if src not in html:
            raise SystemExit('محتوى %s تغيّر أثناء التضمين — تحقّق من الاستبدال' % name)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('الاستخدام: build-standalone.py <مجلد الموقع> <ملف الخرج>')
    main(sys.argv[1], sys.argv[2])
