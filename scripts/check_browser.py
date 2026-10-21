"""Headless visual/rendering checks against a served book, with screenshots."""
import argparse
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--base-url', default='http://127.0.0.1:8765/')
args = parser.parse_args()
OUT = ROOT/'artifacts'/'browser'
OUT.mkdir(parents=True, exist_ok=True)
report = []
with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True,
                                args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 1440, 'height': 1000}, device_scale_factor=1)
    for path in sorted((ROOT/'_site').glob('*.html')):
        page.goto(args.base_url.rstrip('/')+'/'+path.name, wait_until='networkidle')
        assert page.locator('main').count(), path.name
        math_count = page.locator('.math').count()
        if math_count:
            page.wait_for_function('window.MathJax && MathJax.startup && MathJax.startup.promise')
            page.evaluate('async () => { await MathJax.startup.promise; }')
            page.wait_for_selector('mjx-container')
            assert page.locator('mjx-merror').count() == 0, f'MathJax error: {path.name}'
        assert page.locator('.quarto-xref-unresolved').count() == 0
        images = page.locator('main img').evaluate_all('(images) => images.map(i => ({src:i.src,ok:i.complete && i.naturalWidth>0}))')
        assert all(i['ok'] for i in images), f'Broken images: {path.name}'
        report.append({'page':path.name, 'math_expressions':math_count,
                       'figures':len(images), 'status':'passed'})
        if path.name in ['index.html','08-neural-quantum-states.html',
                         '15-physics-informed-learning.html','18-experiment-design.html']:
            page.screenshot(path=str(OUT/(path.stem+'.png')), full_page=False)
    # Follow real chapter navigation and an equation cross-reference.
    page.goto(args.base_url+'05-optimization-and-autodiff.html', wait_until='networkidle')
    xref = page.locator('a.quarto-xref').first
    assert xref.count()
    xref.click()
    assert '04-neural-networks' in page.url
    page.goto(args.base_url+'index.html', wait_until='networkidle')
    search = page.locator('#quarto-search input')
    search.fill('stochastic reconfiguration')
    page.wait_for_selector('.aa-Item')
    assert page.locator('.aa-Item').count() > 0
    page.keyboard.press('Escape')
    page.screenshot(path=str(OUT/'search.png'))
    toggle = page.locator('.quarto-color-scheme-toggle').first
    if toggle.count():
        toggle.click()
        assert 'quarto-dark' in page.locator('body').get_attribute('class')
        page.screenshot(path=str(OUT/'index-dark.png'))
        toggle.click()
    page.set_viewport_size({'width':390,'height':844})
    page.screenshot(path=str(OUT/'index-mobile.png'), full_page=False)
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 2'), 'Mobile document overflow'
    # Confirm the actual download target works over HTTP.
    response = page.request.get(args.base_url+'AI-for-Physics.pdf')
    assert response.ok and response.body().startswith(b'%PDF-')
    response = page.request.get(args.base_url+'notebooks/09-variational-monte-carlo.ipynb')
    assert response.ok and json.loads(response.body())['nbformat'] == 4
    browser.close()
(ROOT/'research'/'browser-checks.json').write_text(json.dumps(report, indent=2)+'\n')
print(f'PASS: {len(report)} pages, MathJax, images, cross-chapter navigation, themes, mobile, PDF, notebook')
