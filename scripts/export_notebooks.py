"""Export chapter text and executable cells without a hidden second code source."""
from pathlib import Path
import re
import nbformat

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'notebooks'
OUT.mkdir(exist_ok=True)
paths = sorted(ROOT.glob('[0-9][0-9]-*.qmd'))
links = []
for path in paths:
    source = path.read_text()
    cells = [nbformat.v4.new_markdown_cell(
        f'This notebook accompanies [{path.stem}](https://xing-phys.github.io/ai-for-physics/{path.stem}.html). '
        'Run cells from top to bottom. The web chapter provides typeset citations and numbered cross-references. '
        'Teaching code: MIT; text and figures: CC BY 4.0. All data are generated locally.\n')]
    cursor = 0
    pattern = re.compile(r'^```\{python\}[^\n]*\n(.*?)^```\s*$', re.M | re.S)
    def clean_markdown(text):
        text = re.sub(r'\{#(?:sec|eq|fig|tbl)-[^}]+\}', '', text)
        text = text.replace('](figs/', '](../figs/')
        text = re.sub(r'\]\((\d\d-[^)]+)\.qmd\)', r'](\1.ipynb)', text)
        return text.strip()
    for match in pattern.finditer(source):
        prose = clean_markdown(source[cursor:match.start()])
        if prose:
            cells.append(nbformat.v4.new_markdown_cell(prose))
        code = '\n'.join(line for line in match.group(1).splitlines()
                         if not line.startswith('#|'))
        cells.append(nbformat.v4.new_code_cell(code.rstrip()))
        cursor = match.end()
    prose = clean_markdown(source[cursor:])
    if prose:
        cells.append(nbformat.v4.new_markdown_cell(prose))
    nb = nbformat.v4.new_notebook(cells=cells)
    nb.metadata.kernelspec = {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}
    nb.metadata.language_info = {'name': 'python', 'version': '3.12'}
    destination = OUT / f'{path.stem}.ipynb'
    if destination.exists():
        previous = nbformat.read(destination, as_version=4)
        executed = {cell.source: cell for cell in previous.cells if cell.cell_type == 'code'}
        for cell in nb.cells:
            if cell.cell_type == 'code' and cell.source in executed:
                cell.outputs = executed[cell.source].outputs
                cell.execution_count = executed[cell.source].execution_count
    nbformat.write(nb, destination)
    title = re.search(r'^# (.+?)(?: \{|$)', source, re.M).group(1)
    links.append(f'- [{path.stem[:2]} · {title}](notebooks/{path.stem}.ipynb)')
lab = ROOT / 'computational-labs.qmd'
if lab.exists():
    source = lab.read_text()
    block = '<!-- NOTEBOOK-LIST -->\n\n'+'\n'.join(links)+'\n\n<!-- /NOTEBOOK-LIST -->'
    source = re.sub(r'<!-- NOTEBOOK-LIST -->(?:.*?<!-- /NOTEBOOK-LIST -->)?',
                    lambda _: block, source, count=1, flags=re.S)
    lab.write_text(source)
print(f'Exported {len(paths)} notebooks')
