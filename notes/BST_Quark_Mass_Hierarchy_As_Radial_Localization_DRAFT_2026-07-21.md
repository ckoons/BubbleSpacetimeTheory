# The Quark Mass Hierarchy as Radial Localization on D_IV⁵

**BST Working Paper — DRAFT 2026-07-21**
Author: Casey Koons · CI co-authors: Lyra, Elie, Grace, Keeper · Referee: Cal

---

## Abstract

We show that the quark mass hierarchy in Bubble Spacetime Theory (BST) arises from a single geometric mechanism — the radial localization of fermion wavefunctions on the support strata of the bounded symmetric domain D_IV⁵ = SO(5,2)/[SO(5)×SO(2)] — and that the up/down steepness asymmetry is fixed by the ceiling-saturation of the top quark (y_t = 1). We derive one quark mass ratio exactly, **m_s/m_d = rank²·n_C = 20**, as a primary-algebraic number, alongside the previously established charged-lepton ladder. We are explicit that the remaining quark ratios sit at the theory's structural (Tier-2) floor and are **not** derived as clean numbers; we identify precisely why (soft light-quark masses, RG running, and non-unique nearby algebraic forms), and we show that the common "powers of the Cabibbo parameter λ" framing is a lossy encoding that camouflages exact structure. The result is a *located mechanism plus one exact new ratio*, not a derivation of the full quark spectrum — and we mark that boundary sharply.

## 1. The one-overlap-object picture

In BST every Yukawa coupling is a single overlap (Gram) matrix on the Hardy space H²(D_IV⁵): masses are its singular values (the radial part), mixings its angular part, CP its commutator. A single condensate O — the SO(5) vector (1,0), boundary-reaching — makes the leading mass matrix **rank-1**, so at leading order only the third generation is massive (the top, with y_t saturating the Cauchy–Schwarz ceiling |y| ≤ 1). The lighter generations are the off-rank-1 corrections. The mass hierarchy is therefore the structure of those corrections.

## 2. Mechanism: radial localization (no texture zero)

The three generations are the three Korányi–Wolf support strata of the rank-2 domain (bulk / Cartan slice / Shilov boundary) — **radial copies of one angular K-type**, differing by where they localize, not by their SO(5) representation. By Wigner–Eckart the Yukawa factorizes into an angular Clebsch (does f_L ⊗ f_R* contain the vector (1,0)?) times a radial reduced matrix element. Because all three generations share the same angular representation, the angular selection rule is **identical** for all of them: since the top couples (CG = 1, via 4⊗4 ⊃ 5), the charm and up couple too — with a smaller radial overlap. An exact texture zero is therefore impossible; the sub-leading masses are radially suppressed but nonzero. (An exact grading would require a generation in a *different* angular representation — an (a,0) spherical harmonic, whose diagonal vector-coupling vanishes identically; the natural one-field/three-strata structure does not realize this.)

**The hierarchy is continuous radial-overlap suppression, not a texture-zero grading.** This matches the observation that the effective "λ-powers" are non-integer and scattered (2.0–4.3) — the fingerprint of continuous localization, not a grading (which would force clean integers).

## 3. The up/down asymmetry: top saturation sets the anchor

The one qualitative asymmetry — up-type steps are ~twice as steep as down-type — has a geometric home. The up-type ladder hangs from the **saturated** top (top = O, sitting at the boundary), so its overlaps fall off steeply with each stratum inward. The down-type ladder hangs from the **unsaturated** bottom (y_b ≈ 0.024, interior-like), so it falls off gently. Saturation sets *where the ladder anchors*, hence the falloff *rate* — a continuous rate, not a clean integer power. (Saturation stabilizes the top's own mass at second order; it does **not**, by itself, steepen the tower — a distinction that corrects an earlier internal claim.)

## 4. Precision: test the ratios, not the exponents

The "m_c/m_t ≈ λ⁴" framing is misleading. The exponent p = ln(ratio)/ln(λ) is a ratio of logarithms — almost always transcendental — so a non-integer p is **not** evidence that the underlying physics is continuous. Proof: **m_s/m_d = 20 exactly** (= rank²·n_C) appears as p ≈ 2.01, indistinguishable from "messy λ² scatter." The exponent encoding projects multiplicative integer structure onto a continuous logarithmic axis, where exact ratios look like noise. The correct test is on the **ratios** themselves, which — for same-sector pairs — are RG-invariant (flavor-universal running) and hence clean, scale-independent targets, expected (T719 closure) to be algebraic in the BST primaries.

**Results of the ratio test (target-innocence bar: unique form, within observational error, RG-invariant):**

| Ratio | Value | BST form | Verdict |
|---|---|---|---|
| m_s/m_d | 20.1 ± 0.4 | **rank²·n_C = 20** (0.7%; competitor 21 is 4.5% off) | **Tier-1, exact identification** |
| m_μ/m_e, m_τ/m_e | — | (24/π²)⁶ ; 49·71 (T190/T2003) | Tier-1 (prior) |
| m_b/m_s | 51.4 ± 1.4 | 45, 50, 54 all bracket it | **Tier-2 — fit-trap, no unique form** |
| m_c/m_u | 589 (±22% via m_u) | rank²·N_c·g² = 588 | **rejected — over-fit inside a 22% window** |
| m_t/m_c | ~277 (RGI) | (137 = pole/running artifact) | **rejected — artifact** |
| m_u/m_d | 0.47 | — | Tier-2, open |

Exactly one new quark ratio survives as exact. The tempting up-type coincidences do not — which is the point: honesty here is what makes the surviving rung credible.

## 5. What is and is not claimed

- **Derived (structural):** the quark hierarchy is radial localization on the D_IV⁵ strata; the up/down asymmetry is the top's ceiling-saturation.
- **Derived (exact ratio):** m_s/m_d = rank²·n_C = 20 (exact identification; the full radial-overlap computation confirming the value is the remaining step to D-tier), joining the charged-lepton ladder.
- **NOT derived:** the full quark spectrum. Most quark mass ratios sit at the Tier-2 structural floor, limited by the soft light-quark masses, RG running, and non-unique nearby algebraic forms. We do **not** claim clean integer powers of λ, and we exclude the over-fit coincidences by construction.

## 6. Falsifiability and outlook

The mechanism predicts no texture zeros in the quark sector (all generations couple; hierarchy is continuous) — distinct from grading models that force clean integer power ratios. The exact rung m_s/m_d = rank²·n_C is a fixed number, falsifiable as lattice determinations of m_s/m_d tighten. The open frontier is pinning the K-type (a,b) addresses of the three generations, which would compute the radial overlaps directly and test whether further ratios join m_s/m_d at Tier-1.

---
*Status: DRAFT. Tiers per BST methodology (D/I/C/S). Lyra to finalize prose + PDF; Keeper audit K792–K799; Elie toys 4761–4766; Grace ledger. Companion to the CP/neutrino flavor-synthesis and the electron-ground-rung papers.*
