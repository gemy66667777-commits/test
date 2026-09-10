# -*- coding: utf-8 -*-
"""يبني ملف HTML واحد قائم بذاته: يحتفظ بالـ <head> كاملاً (charset + viewport)
   ويضمّن CSS و JS والصور داخل الملف."""
import re, sys, base64, os

root, out_path = sys.argv[1], sys.argv[2]
html = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
css  = open(os.path.join(root, 'assets/css/styles.css'), encoding='utf-8').read()
data = open(os.path.join(root, 'assets/js/data.js'), encoding='utf-8').read()
site = open(os.path.join(root, 'assets/js/site.js'), encoding='utf-8').read()

def to_data_uri(m):
    with open(os.path.join(root, m.group(1)), 'rb') as f:
        return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()
data = re.sub(r'(assets/img/[A-Za-z0-9_\-]+\.jpg)', to_data_uri, data)

# استبدال وسم الـ CSS الخارجي بـ <style> مضمّن
html = html.replace(
    '<link rel="stylesheet" href="assets/css/styles.css">',
    '<style>\n' + css + '\n</style>'
)
# استبدال وسوم الـ JS الخارجية بسكربت مضمّن
html = re.sub(
    r'<script src="assets/js/data\.js"></script>\s*<script src="assets/js/site\.js"></script>',
    '<script>\n' + data + '\n</script>\n<script>\n' + site + '\n</script>',
    html
)
assert 'assets/css' not in html and 'assets/js' not in html, 'بقي مرجع خارجي'
assert '<meta charset="utf-8">' in html, 'ناقص charset'
assert 'name="viewport"' in html, 'ناقص viewport'

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('%s -> %.2f MB' % (os.path.basename(out_path), os.path.getsize(out_path)/1048576))
