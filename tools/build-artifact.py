# -*- coding: utf-8 -*-
"""يبني نسخة الـ Artifact: نفس الصفحة بلا <head> لأن المنصة تضيفه بنفسها.

    python3 tools/build-artifact.py <مجلد الموقع> <ملف الخرج> <عنوان الصفحة>

لا تُرسل ناتج هذا السكربت كملف مستقل — استخدم build-standalone.py لذلك.
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib import import_module
_s = import_module('build-standalone')

def main(root, out_path, title):
    html = _s.read(os.path.join(root, 'index.html'))
    css  = _s.read(os.path.join(root, 'assets/css/styles.css'))
    data = _s.read(os.path.join(root, 'assets/js/data.js'))
    site = _s.read(os.path.join(root, 'assets/js/site.js'))
    css, data, site, html = (_s.embed_images(root, t) for t in (css, data, site, html))

    fonts = re.search(r'<link href="https://fonts\.googleapis[^>]*>', html).group(0)
    body  = re.search(r'<body>(.*)</body>', html, re.S).group(1)
    body  = re.sub(r'<script src="[^"]*"></script>\s*', '', body)

    parts = ['<title>', title, '</title>\n', fonts,
             '\n<style>\n', css, '\n.site{background:inherit}\n</style>\n\n',
             '<div class="site" dir="rtl" lang="ar">\n', body, '\n</div>\n\n',
             "<script>\ndocument.documentElement.setAttribute('dir','rtl');\n",
             "document.documentElement.setAttribute('lang','ar');\n</script>\n",
             '<script>\n', data, '\n</script>\n<script>\n', site, '\n</script>\n']
    out = ''.join(parts)

    for name, src in (('styles.css', css), ('data.js', data), ('site.js', site)):
        if src not in out:
            raise SystemExit('محتوى %s تغيّر أثناء التجميع' % name)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(out)
    print('%s -> %.2f ميجابايت' % (os.path.basename(out_path), os.path.getsize(out_path)/1048576))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise SystemExit('الاستخدام: build-artifact.py <مجلد الموقع> <ملف الخرج> <العنوان>')
    main(sys.argv[1], sys.argv[2], sys.argv[3])
