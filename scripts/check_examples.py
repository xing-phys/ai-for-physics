"""Execute each notebook in a clean kernel; retain outputs and a JSON report."""
import json
import os
import argparse
from pathlib import Path
import time
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
os.environ['MPLBACKEND'] = 'module://matplotlib_inline.backend_inline'
parser = argparse.ArgumentParser()
parser.add_argument('--only', help='Execute only notebook stems beginning with this prefix')
args = parser.parse_args()
report_path = ROOT/'research'/'example-checks.json'
previous = json.loads(report_path.read_text()) if args.only and report_path.exists() else []
report = {row['notebook']:row for row in previous}
for path in sorted((ROOT / 'notebooks').glob('*.ipynb')):
    if args.only and not path.stem.startswith(args.only):
        continue
    nb = nbformat.read(path, as_version=4)
    start = time.monotonic()
    NotebookClient(nb, timeout=180, kernel_name='python3',
                   resources={'metadata': {'path': str(ROOT)}}).execute()
    nbformat.write(nb, path)
    count = sum(c.cell_type == 'code' for c in nb.cells)
    item = {'notebook': path.name, 'code_cells': count,
            'seconds': round(time.monotonic()-start, 2), 'status': 'passed'}
    report[path.name] = item
    print(f'PASS {path.name} ({count} code cells)', flush=True)
rows = [report[name] for name in sorted(report)]
report_path.write_text(json.dumps(rows, indent=2)+'\n')
print(f'Verified {sum(x["code_cells"] for x in rows)} cells in {len(rows)} clean kernels')
