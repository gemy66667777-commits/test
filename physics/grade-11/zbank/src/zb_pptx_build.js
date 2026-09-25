// Z BANK A4 PowerPoint edition : one slide per page, the page art as the slide background
// and every line of question / answer text as an editable text box on top of it.
const pptxgen = require('pptxgenjs');
const fs = require('fs');
const path = require('path');
const dir = process.argv[2], out = process.argv[3];
const pages = JSON.parse(fs.readFileSync(path.join(dir, 'pages.json'), 'utf8'));
const IN = v => v / 72;
const pres = new pptxgen();
pres.defineLayout({ name: 'A4_PORTRAIT', width: IN(pages[0].w), height: IN(pages[0].h) });
pres.layout = 'A4_PORTRAIT';
pres.title = 'Z BANK - Chapter 2 - Lesson 1 - Simple Harmonic Motion';
for (const pg of pages) {
  const slide = pres.addSlide();
  slide.background = { path: path.join(dir, pg.bg) };
  for (const b of pg.boxes) {
    const runs = b.runs.map(r => {
      const o = { fontFace: r.f, fontSize: r.s, color: r.c, bold: r.b };
      if (r.sup) o.superscript = true;
      if (r.sub) o.subscript = true;
      return { text: r.t, options: o };
    });
    slide.addText(runs, { x: IN(b.x), y: IN(b.y), w: IN(b.w), h: IN(b.h), margin: 0, valign: 'top',
      align: 'left', wrap: false, fit: 'none', isTextBox: true });
  }
}
pres.writeFile({ fileName: out }).then(f => console.log('written', f, pages.length, 'slides'));
