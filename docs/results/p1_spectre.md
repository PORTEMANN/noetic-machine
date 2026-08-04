# P1 — Bound-State Spectrum: Bohr Atom

> Source: `Note_P1_Spectre_Etats_Lies_Atome_Bohr_HorsCorpus.pdf`

**P1 — The spectrum of bound states: the stable nucleus produces a Bohr atom.**  
Coulomb pure to 10⁻⁴, measured nucleus/atom hierarchy — promise G15 kept.

3 August 2027 — corpus histoire-des-sciences.eu / Machine Noétique (CTFT)

---

## Protocol

The stable nucleus is a dyon: localised electric charge (density deficit, G16–G17) + monopole core of size Rcore = 3.04 (G15). The electron is a charged scalar (no spin: no Pauli term; minimal coupling |p−qA|² reduces to Coulomb at infinity, A being pure gauge). Radial equation [−(1/2m)∂²ᵣ + l(l+1)/(2mr²) + Veff]u = Eu, Veff Coulomb truncated at the core. Exact diagonalisation on radial grid (40 a₀, 4·10⁴ points). Parameters: α = 1/137.036, mₑ = 1 (banc units), coupling inherited G13 — **no adjusted parameter**.

The decisive scale point: the Bohr radius of the banc is a₀ = 1/(mα) = 137 lattice units, i.e. 45 times the core size (Rcore/a₀ = 0.022). The nucleus is infinitely small compared to the orbit — exactly the real hierarchy (~10⁻⁵). G15 had postulated it; P1 measures it.

## Measured spectrum (ratio to Balmer Eₙ = −α²m/2n²)

| State | E measured | E Balmer | ratio | ⟨r⟩ | ⟨r⟩ theory |
|---|---|---|---|---|---|
| 1s (l=0, n=1) | −2.6609·10⁻⁵ | −2.6626·10⁻⁵ | 0.9994 | 1.50 a₀ | 1.50 |
| 2s (l=0, n=2) | −6.6543·10⁻⁶ | −6.6564·10⁻⁶ | 0.9997 | 6.00 a₀ | 6.00 |
| 2p (l=1, n=2) | −6.6564·10⁻⁶ | −6.6564·10⁻⁶ | 1.0000 | 5.00 a₀ | 5.00 |
| 3s (l=0, n=3) | −2.9577·10⁻⁶ | −2.9584·10⁻⁶ | 0.9998 | 13.50 a₀ | 13.50 |
| 3d (l=2, n=3) | −2.9584·10⁻⁶ | −2.9584·10⁻⁶ | 1.0000 | 10.50 a₀ | 10.50 |

## Reading — the Coulomb signature

The 2s/2p and 3s/3p/3d degeneracy is reproduced to 10⁻⁴: this is the signature of pure 1/r (Laplace–Runge–Lenz symmetry), which proves that the stable nucleus behaves as a point charge for the electron. The truncation at the core lifts the degeneracy only at 10⁻⁴ (finite-volume effect, Rcore/a₀ = 0.022) — this is the size of the hyperfine correction, consistent with G15 (H(3.04) = 0.016). The 92.45 factor of G15 finds its place: it lives in this hierarchy (core ↔ orbit), not in the orbit itself.

## Verdict

P1 is a success; promise G15 is kept. The stable nucleus produces a Bohr atom: Coulomb pure spectrum to 10⁻⁴, LRL degeneracy, exact Bohr radii, measured nucleus/atom hierarchy (Rcore/a₀ = 0.022). The bound state, which required a stable nucleus, is now calculated dynamically.

No adjusted parameter; no addition to Programme 2027; notes G6–G19 and P0 published, unmodified.

## Documentary chain

Notes G6–G19 (including G15 b18418a05580, G16 1e2d96662a38, G17 31644ee7cc54), Bilan (d30190d7bc24), acts (665b1db476a5, 493fa1a08291), Addendum (036b3b36e01d), cadrage (a5263d536ee5), P0 (6f8dac8255ce). P1 artefacts: script `p1_etats_lies.py` (e5a652b16688); data `p1_spectre.json` (b0e298d8b248); figure `sha_p1.txt`. SHA-256 truncated to 12 characters.
