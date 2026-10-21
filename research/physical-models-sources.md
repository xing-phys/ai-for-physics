# Research and verification record: physical-model chapters

Prepared 21 October 2026. This record covers chapters 12–16. The chapters are organized around physical questions; papers serve as representative research bridges rather than as the curriculum's organizing units. Bibliography keys are local to `assets/physical-models.bib` and start with `p-`.

The mathematical exposition, examples, exercises, and figures are original. No paper figure, paragraph, or implementation has been copied. Source claims are paraphrased briefly. Software is linked as an optional research extension; the textbook demonstrations run independently using NumPy and Matplotlib. Article metadata were checked against publisher pages, PMLR/JMLR proceedings, or author-deposited arXiv records. Preprints are not silently described as peer-reviewed results. Some bibliography entries use a preprint URL alongside verified publication metadata to preserve open access.

## Primary-source map

| Key | Primary record checked | Pedagogical role and limit |
|---|---|---|
| `p-wu2019` | [PRL 122, 080602](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.122.080602), [preprint](https://arxiv.org/abs/1809.10606) | Normalized autoregressive variational distributions in statistical mechanics. No claim of universal mode coverage. |
| `p-noe2019` | [Author preprint](https://arxiv.org/abs/1812.01729); publisher DOI resolves but automated text access returned 403 | Boltzmann coordinate generators. Reweighting and finite-model bias are explained explicitly. |
| `p-albergo2019` | [Author preprint with journal DOI](https://arxiv.org/abs/1904.12072) | Flow proposals and Metropolis correction in scalar lattice theory. |
| `p-kanwar2020` | [Author preprint with journal DOI](https://arxiv.org/abs/2003.06413) | Gauge-equivariant flow demonstration in two-dimensional U(1), not a general QCD scaling result. |
| `p-albergo2021` | [Interactive notebook tutorial](https://arxiv.org/abs/2101.08176) | Open implementation-oriented source for scalar and gauge examples. |
| `p-song2021` | [Author preprint](https://arxiv.org/abs/2011.13456) | Score/SDE framework; reverse-time sign convention stated. |
| `p-liu2023genphys` | [Author preprint](https://arxiv.org/abs/2304.02637) | Physical PDEs as a generative design space. Smoothing assumptions distinguished from arbitrary unitary dynamics. Includes Di Luo and collaborators as scientifically relevant, without special prominence. |
| `p-price2025` | [Nature publisher record](https://www.nature.com/articles/s41586-024-08252-9) | Conditional probabilistic weather generation; benchmark result distinguished from exact path-distribution correctness. Online date 2024, issue year 2025. |
| `p-gilmer2017` | [PMLR 70, 1263–1272](https://proceedings.mlr.press/v70/gilmer17a.html) | Molecular message-passing abstraction. |
| `p-sanchez2020` | [PMLR 119, 8459–8468](https://proceedings.mlr.press/v119/sanchez-gonzalez20a.html) | Particle graph simulation; empirical rollout ability distinguished from conservation guarantees. |
| `p-satorras2021` | [PMLR 139, 9323–9332](https://proceedings.mlr.press/v139/satorras21a.html) | Scalar/vector Euclidean-equivariant construction. |
| `p-batzner2022` | [Nature Communications publisher record](https://www.nature.com/articles/s41467-022-29939-5), [author preprint](https://arxiv.org/abs/2101.03164) | NequIP and data efficiency; no universal architecture ranking. |
| `p-batatia2022` | [Author preprint](https://arxiv.org/abs/2206.07697) | Higher-body-order equivariant messages in MACE. |
| `p-batatia2025` | [JCP publisher DOI](https://doi.org/10.1063/5.0297006), [full author record](https://arxiv.org/abs/2401.00096) | Broad atomistic pretraining and fine tuning. Bibliography abbreviates the very long author list transparently. |
| `p-lu2021` | [Nature Machine Intelligence publisher record](https://www.nature.com/articles/s42256-021-00302-5) | DeepONet branch/trunk decomposition. Finite-sensor ambiguity explained independently. |
| `p-kovachki2023` | [JMLR 24(89), 1–97](https://jmlr.org/papers/v24/21-1524.html) | Integral-layer operator formulation; discretization sharing distinguished from accuracy guarantees. |
| `p-li2021fno` | [Author preprint](https://arxiv.org/abs/2010.08895) | FNO spectral layers and bounded-scope empirical results. |
| `p-takamoto2022` | [Author preprint](https://arxiv.org/abs/2210.07182) | PDEBench as a broad benchmark instrument. |
| `p-alkin2024` | [Author preprint](https://arxiv.org/abs/2402.12365), NeurIPS 2024 proceedings PDF | Grid/particle-independent latent operator representations. |
| `p-herde2024` | [Author preprint](https://arxiv.org/abs/2405.19101) | PDE pretraining and downstream transfer. |
| `p-berner2026` | [Nature Machine Intelligence publisher record](https://www.nature.com/articles/s42256-026-01267-z) | July 2026 perspective on principled function-space architecture conversion. |
| `p-raissi2019` | [JCP publisher record](https://www.sciencedirect.com/science/article/pii/S0021999118307125) | Residual and data combination for forward/inverse problems. |
| `p-wang2021pathologies` | [SIAM publisher DOI](https://doi.org/10.1137/20M1318043) | Demonstrated gradient imbalance and stiffness in training. |
| `p-krishnapriyan2021` | [Author preprint with NeurIPS reference](https://arxiv.org/abs/2109.01050) | Demonstrated optimization failures; exact title checked rather than using an informal remembered title. |
| `p-wang2023guide` | [Author preprint](https://arxiv.org/abs/2308.08468) | Reproducible training guidance and ablations. |
| `p-chen2018` | [Author preprint](https://arxiv.org/abs/1806.07366) | Neural ODE formulation; idealized memory claim qualified. |
| `p-gholami2019` | [Author preprint](https://arxiv.org/abs/1902.10298) | Discrete/continuous adjoint consistency and reconstruction concerns. |
| `p-blondel2022` | [Author preprint](https://arxiv.org/abs/2105.15183), NeurIPS 2022 proceedings PDF | Modular implicit differentiation. |
| `p-greydanus2019` | [Author preprint](https://arxiv.org/abs/1906.01563) | Scalar Hamiltonian model structure; integrator distinction made explicit. |
| `p-cranmer2020` | [Author preprint](https://arxiv.org/abs/2003.04630) | Lagrangian network formulation; Hessian invertibility assumed explicitly. |
| `p-rackauckas2020` | [Author preprint](https://arxiv.org/abs/2001.04385) | Known-plus-learned differential equations. |
| `p-um2020` | [Author preprint](https://arxiv.org/abs/2007.00016) | Training learned corrections inside rollouts. |
| `p-kochkov2024` | [Nature publisher record](https://www.nature.com/articles/s41586-024-07744-y) | Hybrid differentiable atmospheric simulation; different-climate extrapolation limitation retained. |

## Open implementation links checked

- [Variational autoregressive statistical mechanics](https://github.com/wdphy16/stat-mech-van).
- [MACE](https://github.com/ACEsuit/mace), [NequIP](https://github.com/mir-group/nequip), the latter also confirmed in the primary paper's code-availability section.
- [NeuralOperator](https://github.com/neuraloperator/neuraloperator), [PDEBench](https://github.com/pdebench/PDEBench), [Poseidon](https://github.com/camlab-ethz/poseidon), the last two also supplied by their primary papers.
- [JAX-PI](https://github.com/PredictiveIntelligenceLab/jaxpi), [gradient-pathology PINN experiments](https://github.com/PredictiveIntelligenceLab/GradientPathologiesPINNs).
- [torchdiffeq](https://github.com/rtqichen/torchdiffeq), [SciML](https://sciml.ai/), the latter associated with the UDE primary paper.
- [GraphCast/GenCast](https://github.com/google-deepmind/graphcast), confirmed by the GenCast paper's code-availability section.

No third-party code was incorporated into the chapter demonstrations, so these projects' licenses do not license or constrain the independently written examples. Reusing their code or checkpoints in a later research project requires checking the specific artifact's license.

## Derivation and numerical audit

Essential derivations checked by independent algebra include the KL/free-energy identity and discrete score-function gradient; two-spin partition function; triangular coupling Jacobian; importance and Metropolis correction identities; denoising conditional-score identity; invariant-energy force equivariance and force/torque sums; Fourier heat/advection multipliers; spectral least-squares fitting; finite-volume telescoping; PINN hard-constraint derivatives; heat residual stability estimate; discrete and continuous adjoints; implicit-solve gradients; Lagrangian velocity Hessian; and explicit/symplectic Euler oscillator updates.

All seven Python cells in these five chapters executed successfully in the project's `.venv` using Matplotlib's noninteractive Agg backend on 21 October 2026. Separate per-chapter namespaces were used. Assertions test scientific identities and held-out numerical values, rather than merely checking successful execution.

| Chapter | Execution and observed result |
|---|---|
| 12 | Two-spin exact probabilities and correlation agreed; analytic noisy-mixture density/score figure generated. |
| 13 | Radial potential recovered coefficients `(0.7, 0.2)`; rotation, translation, permutation, total-force and total-torque tests passed. |
| 14 | Learned multiplier agreed with exact diffusion multiplier; independent 128-point evaluation agreed below `1e-12`; mean and norm conditions passed. |
| 15 | Random-feature hard-constrained heat PINN passed an independent test grid. Maximum errors at times `(0, 0.2, 0.5)` were approximately `(0, 2.07e-9, 4.58e-9)`; collocation residual assertion passed. |
| 16 | Discrete adjoint agreed with finite differences and an analytic discrete derivative; inferred Euler rate `0.91210557` compared to continuous rate `0.91629073`; symplectic identity and long-time energy assertions passed. |

These are compact pedagogical checks, not new frontier-scale numerical evidence. The PINN example trains only output weights of fixed random features; the operator example learns a linear diagonal spectral map. Both limitations are stated in the chapter text. Root project integration performs Quarto rendering, notebook export, bibliography resolution, and website checks separately.
