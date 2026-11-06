// Render build/bible.html to PDF with Chromium (Playwright).
// Usage: node tools/render_pdf.js <input.html> <output.pdf>
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [input, output, mode] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle', timeout: 120000 });
  await page.evaluate(() => document.fonts.ready);
  if (mode === 'landscape') {
    await page.pdf({ path: output, preferCSSPageSize: true, printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
    await browser.close();
    console.log('PDF:', output);
    return;
  }
  await page.pdf({
    path: output,
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate:
      '<div style="width:100%;font-family:monospace;font-size:7px;color:#8a7f72;padding:0 14mm;display:flex;justify-content:space-between">' +
      '<span>ZERO-SUM: OMEN · World &amp; Art Bible</span><span class="pageNumber"></span></div>',
    margin: { top: '14mm', bottom: '16mm', left: '14mm', right: '14mm' },
  });
  await browser.close();
  console.log('PDF:', output);
})().catch((e) => { console.error(e); process.exit(1); });
