# AI for Physics: From Fundamental Methods to Scientific Discovery

A self-contained, computational web textbook for senior undergraduate and beginning graduate physics students. The curriculum develops probability, learning, optimization, and validation before quantum many-body methods, generative physical models, symmetry and graphs, neural operators, physics-informed learning, differentiable simulation, inverse problems, experiment design, and scientific discovery.

**Read:** https://xing-phys.github.io/ai-for-physics/

## Reproduce

Requires Python 3.12+, Quarto 1.10.18, and LuaLaTeX for the combined PDF. All teaching calculations use NumPy/Matplotlib; no GPU or external data are needed.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
export QUARTO_PYTHON="$PWD/.venv/bin/python"
python scripts/make_figures.py
python scripts/export_notebooks.py
python scripts/check_sources.py
python scripts/check_examples.py
quarto render --to pdf
quarto render --to html --no-clean
python scripts/check_site.py
quarto preview --no-browser
```

HTML and the combined `AI-for-Physics.pdf` are written to `_site/`. Serve `_site/` with `python -m http.server --directory _site 8765` for an independent static preview. The generated notebooks are in `notebooks/` and can be opened with `jupyter lab`.

`requirements.txt` specifies package ranges; `requirements-lock.txt` records the edition environment. To force a complete Quarto cell rerun, use `quarto render --execute`. The standalone notebook check always uses fresh kernels.

## Structure

- `01-*.qmd` through `21-*.qmd`: teaching chapters; each is the source of its notebook.
- `index.qmd`, `notation.qmd`, `computational-labs.qmd`, `literature-and-reproducibility.qmd`: study routes and appendices.
- `assets/*.bib`: primary literature and textbook references; `research/*-sources.md`: source audits and claim caveats.
- `assets/macros.sty`, `assets/mathjax-config.html`: equivalent PDF and HTML physics macros.
- `scripts/`: figure generation, notebook export/execution, citation/reference checks, site/link checks, browser validation.
- `.github/workflows/publish.yml`: tested build, PDF and HTML rendering, and GitHub Pages deployment.

The research bridges distinguish established results, numerical observations, and conjectures. The demonstrations are intentionally small calibration and learning experiments; building the book does not reproduce every cited research-scale calculation.

## Authorship and review

Prepared for Ze-Yu Xing with AI-assisted drafting, literature research, implementation, and mathematical/numerical checks. The author metadata follows the project owner's report template. Publication does not imply an independent external scientific peer review. Corrections and reproducible counterexamples are welcome through repository issues.

## Licenses

Original prose and figures: [Creative Commons Attribution 4.0](LICENSE-CONTENT). Original teaching code: [MIT](LICENSE-CODE). Linked papers, software, weights, and external datasets retain their own terms. No publisher figures or substantial source passages have been reproduced.
