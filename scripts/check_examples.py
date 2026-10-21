"""Execute each notebook in a clean kernel; retain outputs and a JSON report."""
import json
import os
from pathlib import Path
import time
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
os.environ['MPLBACKEND'] = 'module://matplotlib_inline.backend_inline'
report = []
for path in sorted((ROOT / 'notebooks').glob('*.ipynb')):
    nb = nbformat.read(path, as_version=4)
    start = time.monotonic()
    NotebookClient(nb, timeout=180, kernel_name='python3',
                   resources={'metadata': {'path': str(ROOT)}}).execute()
    nbformat.write(nb, path)
    count = sum(c.cell_type == 'code' for c in nb.cells)
    item = {'notebook': path.name, 'code_cells': count,
            'seconds': round(time.monotonic()-start, 2), 'status': 'passed'}
    report.append(item)
    print(f'PASS {path.name} ({count} code cells)', flush=True)
out = ROOT / 'research' / 'example-checks.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print(f'Executed {sum(x["code_cells"] for x in report)} cells in {len(report)} clean kernels')
