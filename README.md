# Noetic Machine

[![GitHub stars](https://img.shields.io/github/stars/PORTEMANN/noetic-machine?style=flat&color=blue)](https://github.com/PORTEMANN/noetic-machine/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/PORTEMANN/noetic-machine?style=flat&color=green)](https://github.com/PORTEMANN/noetic-machine/network/members)
[![License](https://img.shields.io/github/license/PORTEMANN/noetic-machine?style=flat&color=orange)](LICENSE)

> **Computational physics toolbox for SU(2) gauge models and topological defect structures.**  
> Calibrated on the Bogomolny–Prasad–Sommerfield bound; predictive over three orders of magnitude.

---

## What this is

A reproducible computational environment for testing field-theoretic structures. Given a candidate model (ansatz, Lagrangian, symmetry-breaking pattern) and measured anchoring data (physical constants, scales), it returns a verdict — existence, spectrum, quantisation, regime — with documented invariants, frozen protocols, and SHA-256 hashed artefacts.

This is **not** a simulator. It does not answer "what happens if…" (trajectory). It answers "what exists, where, at what cost" (structure, regime, constitutive law).

## Five confirmed predictions (Georgi–Glashow SU(2) banc)

| # | Prediction | Key result | Status |
|---|---|---|---|
| **P0** | BPS mass calibration | C(ρ=1) = 1.3098 (lit. 1.24–1.31); C(ρ=0.5) = 0.9981 | ✅ Confirmed |
| **P1** | Bound-state spectrum (Bohr atom) | Coulomb pure to 10⁻⁴, LRL degeneracy, a₀ = 137 l.u. | ✅ Confirmed |
| **P2** | Dirac charge quantisation | e·g = 2π exact, n = 1, ratio 1.000000 | ✅ Confirmed |
| **P3** | Nucleus–ring coexistence + flux tube | ΦM = 4π = Φv(Q=2), confinement emergent | ✅ Confirmed |
| **P4** | Phase diagram (g, v, ρ) | 2 regimes, boundary ρ* ≈ 0.75, auto-dual point | ✅ Confirmed |

## Related Repositories

| Repository | Role |
|------------|------|
| [**noetic-applications**](https://github.com/PORTEMANN/noetic-applications) | 14 experimental case studies (P7–P20) applying the finite-core solver to atomic, nuclear, particle, condensed-matter, and molecular physics |
| [**spectral-triple-minimality**](https://github.com/PORTEMANN/spectral-triple-minimality) | Mathematical foundations — 4 theorems (dimension, k-bound, margin-3, non-uniqueness) and the KO-6 arithmetic law |
| [**ko6-spectral-solver**](https://github.com/PORTEMANN/ko6-spectral-solver) | Spectral benchmarks B1–B3 (Taylor–Green, KdV, Ising 2D) |

## Citation

```bibtex
@software{noetic_machine,
  author = {Portemann, Patrice},
  title = {Noetic Machine: A Non-Perturbative Finite-Core Solver},
  url = {https://github.com/PORTEMANN/noetic-machine},
  version = {1.0},
  year = {2027}
}
```

See [CITATION.bib](CITATION.bib) for cross-repository entries.

---

## Repository structure

```
.
├── README.md                 # This file
├── LICENSE                   # MIT
├── MANUAL.md                 # Engineer's manual (full protocol)
├── CITATION.bib              # Cross-repo BibTeX entries
├── src/
│   ├── core/                 # Numerical cores (vortex, entanglement)
│   ├── benchmarks/           # B1–B5: rotation, soliton, Landau, turbulence, oscillator
│   ├── modules/              # D1–D4: mediator, rings, dispersion, vortex pairs
│   │                           E44–E48: nucleation, capture, conservation, assembly
│   └── off_corpus/           # P0–P4: BPS calibration, spectrum, Dirac, bridge, phases
├── protocols/                # Frozen JSON protocols (50+ benchmark and module configs)
├── data/                     # Run outputs (.pkl, .json, .csv) — generated locally
├── notebooks/                # Verification notebooks
└── docs/
    ├── manual/               # Engineer's manual (full)
    └── results/              # P0–P4 result notes (markdown)
```

## Quick start

### Requirements
- Python ≥ 3.10
- NumPy, SciPy, Matplotlib
- (optional) Jupyter for notebooks

### Run a benchmark
```bash
python src/benchmarks/b1_analyse.py
```

### Run off-corpus P0 (BPS calibration)
```bash
python src/off_corpus/p0_monopole_su2.py
```

### Verify gradient correctness
Every module must validate its discrete functional gradient against finite differences before production:
```python
assert np.allclose(grad_discrete, dx * grad_continuous, rtol=1e-2)
```

## Protocol discipline

1. **Frozen protocol** — ansatz, grid conventions, tolerances, and verdict criteria are fixed before execution. No post-hoc adjustment.
2. **Execution** — variational minimisation or exact diagonalisation, with analytically exact discrete gradient.
3. **Verdict** — read from invariants (dimensionless mass, core radius, virial decomposition, charge product, flux). Never from raw curves.
4. **Fingerprints** — every artefact (script, data, figure) is SHA-256 hashed; verdict notes cite prior fingerprints.
5. **Published failures** — negative verdicts and numerical artefacts are published with the same care as successes.

## Parameter classification

| Class | Meaning | Examples |
|---|---|---|
| **Derived** | Output of the machine | C(ρ), spectra, radii, e·g = 2π |
| **Measured** | Physico-chemical anchoring | α = 1/137.036, R_core = 3.04 l.u. |
| **Assumed constitutive** | Structural choice, ontology | ρ = λ/e², Georgi–Glashow model itself |

## Author

Patrice Portemann

> *A result that does not reproduce on another machine does not exist.*
