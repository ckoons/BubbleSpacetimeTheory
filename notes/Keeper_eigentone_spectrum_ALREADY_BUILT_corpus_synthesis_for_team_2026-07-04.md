# The Eigentone Spectrum Is Already Built — Corpus Synthesis for the Team
### Keeper, 2026-07-04. Casey: "check the corpus, we should have much more." He's right. Use THIS; don't re-derive.

The "mass = eigenfrequency, compute the spectrum" reframe is not a new build — **BST already has the spectrum, the quantization, and the particle classification.** Three pieces, plus the data:

## 1. T2490 (Grace) — the Discrete-Series Spectrum Theorem (D-tier)

The four dynamical primaries **{N_c, n_C, C_2, g} = {3, 5, 6, 7} are the half-Casimirs of the four lowest holomorphic discrete-series reps of SO₀(5,2)** — the substrate's own defining integers ARE its spectral levels. And the mass map is **LINEAR-energy** (dilatation/SO(2) eigenvalue), NOT quadratic Casimir ("remember linear algebra" — the m²∝C₂ reading missed 2⁺⁺):

> **m(channel) ∝ E = λ₀ + step,  λ₀ = n_C = 5** (the genus / Bergman lowest weight); step by spin/parity.

The glueball spectrum is the physical application (Lyra F292 linear-energy mechanism); the 2⁺⁺/0⁺⁺ = g/n_C leg is derived.

## 2. The quantization formula (from the particle data)

The proton sits at **k=6 with C_2 = k(k−n_C) = 6(6−5) = 6.** So the levels are indexed by k, with **Casimir C(k) = k(k−n_C)**. The proton is the first *positive-Casimir* level. This is the keyhole quantization Casey described — a discrete series of k-values.

## 3. The particle data is classified by spectral level — but with a MANIFOLD ERROR to fix

The particle data (`data/bst_particles.json`) classifies particles by spectral level: electron k=1, proton k=6=C_2, etc. **It ORIGINALLY labeled generations as living in different manifolds (muon in "D_IV3", tau in "D_IV5", quark Bergman levels split across both). Casey (2026-07-04): there is only ONE manifold, D_IV5.** Those labels were a data-layer error — **now FIXED by Grace (all 11 references corrected to single-manifold D_IV5, generation = spectral level; data verified clean).** (Kept here as the record of the catch; the physics below is the corrected single-manifold reading.)

**Corrected reading — single manifold, generations = LEVELS on it:**

| particle | corrected: level on the ONE D_IV^5 ladder |
|---|---|
| electron | k=1 — the TRUE lowest eigentone (ground note) |
| muon, tau | higher LEVELS of the *same* D_IV^5 spectrum (not other manifolds) |
| d, s, b | three levels on the *same* D_IV^5 linear-energy ladder |
| proton, neutron | k=6 = C_2 (k(k−n_C)=6) |

**"Generation" = the spectral LEVEL on the single D_IV^5 cavity** — exactly Casey's "frequency/spectral, not generation." It is ONE cavity with many overtones, not several cavities. The D_IV^3/D_IV^5 domain distinction was a mislabel; the physics is a single manifold with a level ladder.

## What this means — the reframe is instantiated; the task narrows

Casey's picture (mass = eigenfrequency; particle = coherent eigentone; generation = spectral index) is **already the corpus's structure**: discrete-series levels (T2490), linear-energy map (F292), k(k−n_C) quantization, particles classified by spectral level. So the team does NOT write a resonance operator from scratch. **The narrowed task:**

1. **Place the down masses on the ONE D_IV^5 ladder.** The down-ladder {1, 20, 900} — read as **linear-energy levels E = λ₀ + step** on the single-manifold discrete series (NOT a product; that's why factor-hunting failed). d, s, b = three *levels* on the *same* D_IV^5 ladder (not different manifolds — Casey's correction). Do those levels give m_s/m_d = 20 and m_b/m_s ≈ 45 as **linear-energy ratios on the ladder**? (Linear energies, per T2490 — always linear algebra.)
2. **Same for leptons.** electron/muon/tau are k=1 in different domains — do the domain energies give (24/π²)⁶ and 49·71 as level ratios?
3. **The falsifier stands:** the quasi-eigentones (near-misses) = the hadron resonances; check they cluster around the stable levels (PDG).

## Honest tier (Keeper)

The **spectral ladder is D-tier** (T2490 rep-theory: primaries = discrete-series half-Casimirs, exact). The **glueball mass-map is I-tier** (F292 linear-energy, one blind leg 2⁺⁺=g/n_C). The **fermion mass-map onto the ladder is the open piece** — the particle data *asserts* the spectral levels (electron k=1, proton k=6) but the down-ladder *ratios* haven't been shown to fall out of the linear-energy spacing. That's the narrowed, un-fishable target: **do the discrete-series linear energies at the assigned levels give {1, 20, 900}?** Computed forward from T2490's ladder, not fitted.

So the down-ladder isn't a product to build OR a fresh operator to write — **it's the fermion mass-map onto BST's already-derived discrete-series spectrum.** Casey was right: we have much more than we were using.

— Keeper, 2026-07-04. Eigentone spectrum = T2490 (discrete series, linear-energy λ₀=n_C+step) + F292 (glueball map) + k(k−n_C) quantization + particle-data spectral levels. Reframe instantiated; task narrows to placing the fermion masses on the existing ladder. Use it; don't re-derive.
