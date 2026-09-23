// Build the A4 PowerPoint edition : one slide per page, the page design as the slide
// background and every line of text as an editable text box on top of it.
const pptxgen = require('pptxgenjs');
const fs = require('fs');
const path = require('path');

const dir = process.argv[2];
const out = process.argv[3];
const pages = JSON.parse(fs.readFileSync(path.join(dir, 'pages.json'), 'utf8'));
const IN = v => v / 72;                       // points → inches
const DY = parseFloat(process.env.DY || '0.09'); // baseline correction, in em

const pres = new pptxgen();
const W = IN(pages[0].w), H = IN(pages[0].h);
pres.defineLayout({ name: 'A4_PORTRAIT', width: W, height: H });
pres.layout = 'A4_PORTRAIT';
pres.author = 'Mr. Gemy';
pres.company = 'Mr. Gemy Physics';
pres.title = 'Physics Grade 11 - Performance and Assessment Tasks';

for (const pg of pages) {
  const slide = pres.addSlide();
  slide.background = { path: path.join(dir, pg.bg) };
  for (const b of pg.boxes) {
    const runs = b.runs.map(r => {
      const o = { fontFace: r.f, fontSize: r.s, color: r.c, bold: r.b, italic: r.i };
      if (r.cs) o.charSpacing = r.cs;
      if (r.sup) o.superscript = true;
      if (r.sub) o.subscript = true;
      return { text: r.t, options: o };
    });
    slide.addText(runs, {
      x: IN(b.x), y: IN(b.y - DY * Math.max(...b.runs.map(r => r.s))), w: IN(b.w), h: IN(b.h),
      margin: 0, valign: 'top', align: 'left', wrap: false, fit: 'none',
      isTextBox: true,
    });
  }
}
pres.writeFile({ fileName: out }).then(f => console.log('written', f, pages.length, 'slides'));
