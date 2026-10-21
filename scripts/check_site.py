"""Resolve local HTML links and fragments, including nested relative URLs."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT/'_site'
files = sorted(SITE.glob('*.html'))
errors = []
ids = {}
if not files:
    errors.append('No HTML pages found: render the HTML book before checking')
for path in files:
    soup = BeautifulSoup(path.read_text(), 'html.parser')
    ids[path.resolve()] = {tag['id'] for tag in soup.find_all(id=True)}
    if soup.select('.quarto-xref-unresolved, .citation[data-cites=""]'):
        errors.append(f'{path.name}: unresolved rendered reference')
    if re.search(r'\?\?\s*(?:fig|eq|sec|tbl)-', soup.get_text()):
        errors.append(f'{path.name}: unresolved-reference marker')
    for tag in soup.select('a[href], img[src], script[src], link[href]'):
        url = tag.get('href', tag.get('src', ''))
        split = urlsplit(url)
        if split.scheme or split.netloc or not split.path and not split.fragment:
            continue
        if split.path.startswith('/ai-for-physics/'):
            target = SITE/split.path.removeprefix('/ai-for-physics/')
        elif split.path.startswith('/'):
            target = SITE/split.path.lstrip('/')
        elif split.path:
            target = path.parent/unquote(split.path)
        else:
            target = path
        if target.is_dir():
            target /= 'index.html'
        target = target.resolve()
        if not target.exists():
            errors.append(f'{path.name}: missing {url}')
        elif split.fragment and target.suffix == '.html':
            if target not in ids:
                ids[target] = {t['id'] for t in BeautifulSoup(target.read_text(), 'html.parser').find_all(id=True)}
            if unquote(split.fragment) not in ids[target]:
                # Browser text-fragment links are not HTML ids.
                if not split.fragment.startswith(':~:text='):
                    errors.append(f'{path.name}: missing anchor {url}')
if errors:
    print('\n'.join(sorted(set(errors)))); sys.exit(1)
print(f'PASS: {len(files)} HTML pages, local links, resources, and fragments')
