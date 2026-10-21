"""Check citation and cross-reference definitions before a Quarto build."""
from collections import Counter
from pathlib import Path
import re
import sys
import bibtexparser
import yaml

ROOT = Path(__file__).resolve().parents[1]
config = yaml.safe_load((ROOT / '_quarto.yml').read_text())
keys = []
dois = []
errors = []
for name in config['bibliography']:
    entries = bibtexparser.loads((ROOT/name).read_text()).entries
    keys.extend(e['ID'] for e in entries)
    dois.extend(e['doi'].lower() for e in entries if e.get('doi'))
    for entry in entries:
        for field in ['title', 'author', 'year']:
            if not entry.get(field):
                errors.append(f'{name}: {entry["ID"]} missing {field}')
labels = []
references = []
citations = []
for path in ROOT.glob('*.qmd'):
    text = path.read_text()
    text = re.sub(r'^```.*?^```\s*$', '', text, flags=re.S | re.M)
    labels.extend(re.findall(r'\{#([\w-]+)', text))
    # Executable cell labels are also cross-reference definitions.
    labels.extend(re.findall(r'^#\| label:\s*([\w-]+)', path.read_text(), re.M))
    for ref in re.findall(r'(?<![\w/])@([\w][\w:.-]*)', text):
        if ref.startswith(('eq-', 'sec-', 'fig-', 'tbl-')):
            references.append((path.name, ref))
        else:
            citations.append((path.name, ref.rstrip('.')))
for key, count in Counter(keys).items():
    if count > 1:
        errors.append(f'Duplicate bibliography key: {key}')
for doi, count in Counter(dois).items():
    if count > 1:
        errors.append(f'Duplicate DOI record: {doi}')
for key, count in Counter(labels).items():
    if count > 1:
        errors.append(f'Duplicate label: {key}')
for path, key in citations:
    if key not in keys:
        errors.append(f'{path}: unresolved citation {key}')
for path, key in references:
    if key.rstrip('.') not in labels:
        errors.append(f'{path}: unresolved cross-reference {key}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'PASS: {len(keys)} bibliography records, {len(citations)} citations, '
      f'{len(labels)} labels, {len(references)} cross-reference uses')
