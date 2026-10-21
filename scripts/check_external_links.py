"""Audit external source URLs; distinguish HTTP failures from access restrictions."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import re
import requests
import bibtexparser

ROOT = Path(__file__).resolve().parents[1]
urls = set()
for path in ROOT.glob('*.qmd'):
    urls.update(re.findall(r'\]\((https?://[^\s)]+)\)', path.read_text()))
for path in (ROOT/'assets').glob('*.bib'):
    for entry in bibtexparser.loads(path.read_text()).entries:
        if entry.get('url'):
            urls.add(entry['url'])
        if entry.get('doi'):
            urls.add('https://doi.org/'+entry['doi'])
# This publication is tested separately after deployment.
urls = {u for u in urls if not u.startswith('https://xing-phys.') and
        not u.startswith('https://github.com/xing-phys/')}

def check(url):
    try:
        response = requests.get(url, timeout=20, stream=True,
                                headers={'User-Agent':'AI-for-Physics-source-link-check/1.0'})
        status = response.status_code
        final = response.url
        response.close()
        state = ('accessible' if status < 400 else
                 'access-restricted' if status in [401,403,429] else 'http-failure')
        return {'url':url,'status':status,'final_url':final,'result':state}
    except requests.RequestException as exc:
        return {'url':url,'result':'network-unavailable','error':str(exc)[:200]}

with ThreadPoolExecutor(max_workers=6) as pool:
    results = list(pool.map(check, sorted(urls)))
(ROOT/'research'/'external-link-checks.json').write_text(json.dumps(results,indent=2)+'\n')
from collections import Counter
print(dict(Counter(r['result'] for r in results)))
for r in results:
    if r['result'] == 'http-failure':
        print(r['status'],r['url'])
