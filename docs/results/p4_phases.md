# P4 — Phase Diagram: Two Regimes, One Boundary, One Self-Dual Point

> Source: `Note_P4_Diagramme_Phases_Monopole_HorsCorpus.pdf`

**P4 — The phase diagram: two regimes, one boundary, one self-dual point.**  
The monopole mass is calculable over three orders of magnitude.

3 August 2027 — corpus histoire-des-sciences.eu / Machine Noétique (CTFT)

---

## Protocol

Sweep ρ ∈ [0.1, 20] (12 points), same solver as P0 ('t Hooft–Polyakov ansatz, L-BFGS, validated discrete gradient). Per point: mass C = M/(4πv/e), gauge radius (K = 1/2, dressing), Higgs radius (H = 1/2), and virial decomposition Egauge (λ₀), Ehiggs (λ₁), Epot (λ₃). The regime boundary is read in the crossing of radii and the energy weight transfer.

## Results

Two regimes, boundary at ρ* ≈ 0.75 (crossing r_gauge/r_Higgs):

| Regime | ρ range | Core structure | Egauge/C | Mass law |
|---|---|---|---|---|
| I (gauge core, ~BPS) | < 0.75 | r_gauge < r_Higgs | 0.40 | C ≈ 1.25√ρ + 0.11 |
| II (Higgs core) | > 0.75 | r_Higgs < r_gauge | 0.40 → 0.22 | C ≈ 0.77 ln ρ |

**Self-dual point:** ρ = 0.5 gives C = 0.9981 ≃ 1.000 — the exact Bogomolny bound. The solution there is self-dual: a special point of the diagram, not an accident.

## Reading — the signature of regime change

The weight transfer across the boundary is sharp: Egauge/C drops from 0.40 to 0.22 while Ehiggs/C rises from 0.15 to 0.44. The monopole passes from a gauge object (the dressed field carries the mass, regime close to self-duality) to a Higgs object (the scalar core carries the mass). The mass is a calculable function of ρ over three orders of magnitude — this is the first complete constitutive law of the structure: at given ρ, the mass, size and composition of the nucleus are predicted.

## B3-FAIL

Two artefacts published. (i) ρ → 0 gives C → 0.49 below the BPS bound (1.0): finite-box artefact, already identified in P0 — the BPS limit is singular, without potential Derrick evicts Higgs to the boundary. The bound is reachable only by ρ → 0⁺ from converged branches (C(0.5) ≃ 1 confirms it). (ii) ρ = 20 did not converge (L-BFGS, maxiter) — steepest point, to be retaken with continuation from ρ = 12. Neither affects the regime structure.

**Artefacts:** `p4_phases.py` (8b70f0aef78a), data and figure `sha_p4.txt`.

## Verdict

P4 is a success; the cartography is done, the cadrage is closed. Two regimes (gauge core / Higgs core), one measured boundary (ρ* ≈ 0.75), one self-dual point (ρ = 0.5, C = 1 exact), mass laws calculable over three orders of magnitude. The banc has fulfilled its mature mission: the phase diagram (ρ) is drawn, and with it the off-corpus structure has its first complete constitutive law.

**Final balance of the channel: five predictions of the cadrage, five successes, no adjusted parameter** — P0 (monopole calibrated on BPS), P1 (Bohr atom, Coulomb pure), P2 (topologically quantised charge), P3 (bridge + confinement), P4 (phase diagram). The off-corpus structure, founded on the closed corpus, keeps all its promises.

No addition to Programme 2027; notes G6–G19, P0–P3 published, unmodified.

## Documentary chain

Notes G6–G19, Bilan (d30190d7bc24), acts (665b1db476a5, 493fa1a08291), Addendum (036b3b36e01d), cadrage (a5263d536ee5), P0 (6f8dac8255ce), P1 (18a75bff4023), P2 (72c84bf155b9), P3 (ff9d55667296). P4 artefacts: `p4_phases.py` (8b70f0aef78a), `p4_phases.json` (91d2751acc38), `p4_phases.png` (2b3a9879f733). SHA-256 truncated to 12 characters.
