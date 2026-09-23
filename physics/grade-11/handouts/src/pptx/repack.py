"""pptxgenjs stores the XML parts uncompressed ; deflate them (pictures stay stored)."""
import sys, zipfile
src, dst = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(src) as zi, zipfile.ZipFile(dst, 'w') as zo:
    for info in zi.infolist():
        data = zi.read(info.filename)
        comp = zipfile.ZIP_STORED if info.filename.endswith(('.jpeg', '.jpg', '.png')) \
            else zipfile.ZIP_DEFLATED
        zo.writestr(info, data, compress_type=comp, compresslevel=9 if comp else None)
