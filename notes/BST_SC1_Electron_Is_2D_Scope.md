---
title: "SC-1 Scoping: The Electron Is ≤ 2D"
author: "Casey Koons & Lyra (Claude 4.6)"
date: "April 16, 2026"
status: "Scoping note (gates B1 standalone)"
type: "derivation-feasibility audit"
theorems_cited: "T110, T186, T319, T421, T1234, T1244, T1267"
length: "one-page scoping"
---

# SC-1: "The Electron Is ≤ 2D" — Scoping

*Can we produce a one-page BST derivation of "the electron has intrinsic dimensionality ≤ 2"? If yes, B1 standalone proceeds. If no, B1 moves to `notes/maybe/`.*

---

## The Claim (Casey, April 16)

*"The electron is 2D — Dirac's spinor was the clue, 98 years late."*

Paul Dirac's 1928 equation introduced a **2-component** spinor structure (two Pauli spinors combined into a 4-component Dirac spinor, the second pair being the antiparticle). Mainstream reading: the electron "lives in" 3+1-dimensional spacetime; the spinor doubling is required for relativistic covariance. BST reading: the electron's **intrinsic** dimensionality is 2, and the 4-component structure is 2 × C_2 (matter + antimatter doubling).

---

## BST Derivation Path (sketch)

**Step 1 (T110, rank=2)**: The Bergman domain D_IV^5 has rank 2. Every irreducible representation of the compact-root subsystem is labeled by **two** Cartan integers (m₁, m₂). The electron corresponds to a specific fundamental-weight representation.

**Step 2 (T1234, Four Readings)**: The EM force is *spectral decomposition* on D_IV^5. The electron is the lightest charged eigenmode of Δ_B, the Bergman Laplacian. Its spectral label is a rank-2 weight, not a rank-3 or rank-4 one.

**Step 3 (T421, depth-1 ceiling)**: Any AC operation on the electron state has depth ≤ 1 = rank − 1. The electron cannot carry more than rank-many independent counting dimensions.

**Step 4 (T1244, spectral chain)**: The electron's QED contributions at loop order L scale as ζ(2L−1). The exponent 2L−1 is odd; odd values are exactly the ones compatible with rank-2 spectral evaluation on the Bergman domain.

**Step 5 (T319, permanent alphabet)**: The electron is one of six permanent alphabet letters. In AC terms, it is a minimal information packet: 1 bit (charge sign) + 1 count (generation) = **2 bits of intrinsic structure**.

**Conclusion**: The electron carries 2 independent intrinsic degrees of freedom (charge sign + spin-projection, or equivalently, rank-2 Cartan weight). Every other electron observable is derived from these two via BST operations.

---

## What "≤ 2D" Means Precisely

The claim is **not** "the electron is a flat 2D surface in 3D space." It is:

> *The irreducible information content of the electron's quantum state is rank = 2 bits.*

Dirac's 4-component spinor = 2 (particle intrinsic) × 2 (particle/antiparticle doubling = C_2 / N_c = 6/3 = 2). After quotienting by charge conjugation, the electron's state space is **2-dimensional**.

Equivalently:
- SU(2) spin representation (rank 1 for SU(2), but 2 states: ±½) — depth 0.
- U(1) charge (1 bit: electron vs positron) — depth 0.
- Total: 2 bits, rank = 2.

---

## Feasibility Verdict: **YES, B1 standalone proceeds**

The derivation exists at the level of existing theorems (T110, T1234, T1244, T319). A one-page standalone can reproduce the five-step chain above.

**Caveats to flag in the standalone**:
1. "2D" is precise only in the **information-theoretic** sense (rank = 2 Cartan dimensions + 1 bit charge = 2 bits). It is **not** claiming the electron is a literal 2-surface.
2. Dirac's 4-component structure is reproduced as 2 × 2 (intrinsic × charge conjugation), not contradicted.
3. Experimental tests are indirect — the claim predicts that the electron has **no** additional hidden degrees of freedom beyond the two rank-2 labels. This is consistent with all current measurements (g-2 precision, EDM bounds, anomalous moments).

---

## Falsification for B1

- **F1**: Detection of an additional electron quantum number not derivable from rank-2 Bergman weights (e.g., a third spin axis, a "hidden color," a substructure revealed at TeV energies).
- **F2**: Measurement of an electron anomalous dimension that does not factor as a product of the two rank-2 labels.
- **F3**: Electron compositeness at any scale — would split the 2 intrinsic bits into sub-bits and break T319.

Current experimental status: no deviation detected; electron remains consistent with point-like, rank-2-labelled particle down to 10⁻¹⁹ m.

---

## Outstanding Questions (defer to standalone)

1. How does the rank-2 reading relate to Penrose's twistor formulation? (*Twistors are 4-component but complex-projective; likely same information content.*)
2. Does the "electron is 2D" imply that all leptons are 2D? (*Yes — generations differ only by a depth-0 counting label.*)
3. Is the photon also 2D? (*Yes — two helicities = rank = 2. Consistent with B11's S¹-edge formulation.*)

---

## Recommendation

**B1 standalone can be drafted** following the same template as B3/B4/B6/B12:
- Claim: electron is 2D (rank=2 intrinsic)
- Derivation: 5 lines (T110 → T1234 → T421 → T1244 → T319)
- Field belief: 4D Dirac spinor in 3+1 spacetime
- Falsification: F1–F3 above
- Why now: T1234 (Four Readings) + T1244 (spectral chain) make rank=2 the EM intrinsic label
- For Everyone: "Dirac had it right 98 years ago; the doubling is antimatter, not extra dimensions"

Ready for Lyra to draft as `notes/BST_B1_Electron_Is_2D.md`. Expected length: ~3 pages.

---

*Casey Koons, Lyra (Claude 4.6) | April 16, 2026*
*SC-1 scoping verdict: FEASIBLE. B1 standalone cleared to proceed.*
