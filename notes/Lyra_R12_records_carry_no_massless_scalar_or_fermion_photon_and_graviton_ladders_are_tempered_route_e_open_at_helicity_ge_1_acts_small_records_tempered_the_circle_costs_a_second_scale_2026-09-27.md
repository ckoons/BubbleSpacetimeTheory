# Lyra R12: records carry no massless scalar or fermion; the photon and graviton ladders are tempered, so route (e) is open at helicity ≥ 1. Acts are small, records are tempered. Every radius BST can form is excluded, so the circle costs a second scale

**Lyra, Sunday 2026-09-27 (timestamps from `date`; drafted 11:25; Lane A rewritten 11:27 after reading Cal Section 1004).**
- **"Tempered" here means the unitary-representation sense** (Grace's alias flag, Section 12): matrix coefficients almost-L², i.e. weakly contained in L²(G) (Cowling–Haagerup–Howe). It is **not** the automorphic sense of T1299/T2621/K917.
- **Instrument:** `play/toy_5829_lyra_R12_…circle.py`, sha256 `973c573c54b1516e…`, hashed before the run at 11:24:22. **SCORE 4/4**, output `play/.out_toy_5829.txt`.
  - Caveat on T1: it checks my ρ formula. Its controls (SU(2,2)'s scalar holomorphic-discrete-series threshold 3; SO(5,2)'s λ > 4, Kobayashi 8.4 as Grace pinned it) are known values I state; they were not independently computed.
  - The per-helicity matrix coefficients beyond the leading scalar exponent are Elie's (5830/5831).
- **didwe:** "tempered ladder" → 0; "Bohr radius circle" → 0; "universal extra dimension" → 0.

---

## Lane A: close route (e), records, by temperedness. It closes for helicity 0 and ½, and stays OPEN for helicity ≥ 1

**Order of events (disclosed):**
- I drafted this lane at 11:25 without Cal's prediction.
- Cal hashed Section 1004 at 11:25 (1d2f81e7). I read its subject, then the file (to quote it), and then **rewrote this lane.**
- **The rewrite retracts one claim of my draft,** marked below. Toy 5829's T2 is valid only for the scalar.

**Kill line (Keeper's, verbatim):** *"a tempered ladder at some helicity (e.g. a limit of discrete series). That keeps route (e) open there, meaning the massless world lives in the RECORD."*

**Invariant, quoted first:**
- The restricted roots of SO(n,2) are C₂ (e₁ ± e₂ with multiplicity n − 2; 2e₁, 2e₂ with multiplicity 1), so **ρ = (n−1)e₁ + e₂**, which is (3, 1) for SO(4,2).
- Tempered = weakly contained in L²(G) = K-finite coefficients O(Ξ·poly), with Ξ ~ e^{−ρ}·poly.

**Link 1: the record space is tempered. HOLDS, pinned from primary.** Grace R167 (`data/sources_grace_2026-09-26/r8_tensor/R8_TENSOR_PINS_draft.md` line 189, visual transcription of p. 17): **"THEOREM 5.1. Let ν > (p−1)/2 … π_ν ⊗ π̄_ν ≅ ∫^⊕_{𝔞*/W} H(λ) dλ"**, a direct integral of principal series only. For type IV₅, p = 5, so (p−1)/2 = 2 < 5/2.
- **Cal's L1, restated verbatim:** *"likely FAILS at the Hardy point … proved in the holomorphic discrete-series range. λ = 5/2 lies below p − 1 = 4."* Cal's kill, verbatim: *"My L1 dies if H² ⊗ H̄² at λ = 5/2 is shown to be purely L²(G/K)."*
- **It dies.** Theorem 5.1's hypothesis is ν > (p−1)/2, not ν > p − 1. The discrete-series threshold stood in for the theorem's own.
- Caveat, Grace's own: the ν normalization is FK's and was not cross-checked against a type-IV source. It is FK's throughout this thread (discrete series at ν > p − 1 = 4, Hardy at 5/2).

**Link 2: restriction keeps temperedness. HOLDS** (Cal agrees). Weak containment passes to restrictions, and L²(G)|_H is a multiple of L²(H). Pin owed: Cowling–Haagerup–Howe.

**Link 3, helicity by helicity. The structure is Cal's (Section 1004), which I adopt, correcting my draft.**
- **Retracted from my draft:** "for j = ½ and 1, a bounded K-matrix factor times the same leading exponent" and "the limit-of-discrete-series worry is a confusion of the two boundaries". **Both are wrong.** For a vector lowest K-type the coefficient carries the automorphy factor J(a, 0) ∈ K_ℂ, which is **non-compact, not bounded**. It shifts the exponents along the two strongly orthogonal SU(1,1) directions to **(Δ + j, Δ − j)**. Toy 5829's T2 covered only the scalar exponent.
- **Criterion:** tempered iff (Δ + j, Δ − j) ≥ ρ = (3, 1) componentwise (with equality allowed, the Ξ polynomial), i.e. **Δ ≥ max(3 − j, 1 + j).**

| helicity j | massless Δ = j + 1 | exponents (Δ+j, Δ−j) | vs ρ = (3,1) | verdict |
|---|---|---|---|---|
| 0 (scalar) | 1 | (1, 1) | 1 < 3 | **NOT tempered (exact)** |
| ½ (Weyl) | 3/2 | (2, 1) | 2 < 3 | **NOT tempered** |
| 1 (photon) | 2 | (3, 1) | **equal** | **on the tempered edge: a limit of discrete series, tempered** |
| 2 (graviton) | 3 | (5, 1) | second component equal | on the edge: tempered |

- **So for every helicity j ≥ 1, the massless ladder sits exactly on the tempered edge** (Δ − j = 1 = ρ₂). The vector discrete-series edge Δ ≥ max(3 − j, 1 + j) *is* the massless line for j ≥ 1.
- **Confidence:** exact for j = 0. For j ≥ ½ it rests on the (Δ ± j) exponent assignment, which Cal registered as a heuristic, "not a pinned statement". **Elie 5830/5831 compute the coefficients exactly**, and Grace pins a source (a limits-of-discrete-series table for SU(2,2)).

**Verdict:**
- **Route (e) closes for helicity 0 and ½**: records carry no massless scalar and no massless fermion.
- **It stays OPEN for helicity ≥ 1: the photon's and graviton's representations are tempered and are not excluded from the record.** Keeper's kill line fires at exactly the helicities that matter most.
- **Calibrated both ways (Cal's words, adopted):** *"not excluded", never "the photon is in the record"*. Containment needs a nonzero SO(4,2)-intertwiner from L²(G/K)|_{SO(4,2)} onto the helicity-1 ladder, **computed**. That is the next lane, and it is the day's most interesting open door.
- If the intertwiner exists, Casey's act/record picture carries real weight: **the gauge and gravity quanta would live in the record, and the matter quanta (helicity 0 and ½) could not.**

**The act/record split, which survives the retraction (scalar, exact):**
- **Acts are small:** H² (5/2) and the Rac (3/2) are below SO(5,2)'s ρ(e₁) = 4, so neither is tempered (T3).
- **Records are tempered** (Theorem 5.1).
- H²|SO(4,2) = ⊕_k H_{5/2+k}(D_IV⁴): non-tempered at k = 0, tempered for k ≥ 1 (7/2 > 3).
- **A new rhyme, stated as direction only:** helicity ≥ 1 (the force carriers) is exactly the part of the massless world that the tempered record space is not forbidden to carry.

## Lane B: price the circle

**Kill line (Keeper's, restated):** *"if R = the ruler is excluded, the KK route costs BST a SECOND input, contradicting 'one ruler'. State it plainly."*

**Enumerate the radii BST can form before pricing any** (T4, computed from CODATA via `scipy.constants`, not quoted):

| candidate radius from the one ruler | value | 1/R |
|---|---|---|
| ƛ_e = ħ/(m_e c) | 3.8616×10⁻¹³ m | **0.51100 MeV** |
| c·tick = N_max·ħ/(m_e c) (N_max = 137) | 5.2904×10⁻¹¹ m, which is **the Bohr radius a₀ to 0.03 %** (a₀ = 5.2918×10⁻¹¹ m; the difference is 137 vs 1/α = 137.036) | **3.730 keV** |
| the compact realization's conformal radius | not fixed by BST (cosmological if it is the Hubble scale) | ~0 |

**What couples to the tower (Keeper's question): everything that made the massless content.**
- Route (a) needs the **singletons themselves** on the circle: the Rac zero mode is the scalar ladder and the Di zero mode is the helicity-½ ladder.
- So every field built from them has KK partners at n/R: every charged fermion, and every current the photon couples to.
- **This is a universal extra dimension (UED) in the collider sense**, and the UED bound applies. For scale, 1 TeV corresponds to ħc/(1 TeV) = 1.973×10⁻¹⁹ m, which is **1.96×10⁶ × m_e c²**. The pinned bound (arXiv:1606.04084) is Grace's.
- For the keV option, the order of magnitude is not in doubt: **charged KK partners of the light fermions at 3.7 keV, 7.5 keV, … do not exist.** The pin (PDG charged-lepton and invisible-Z listings) is still owed; no number is used here.

**Can a sector hide on the circle? Enumerated:**
- **(i) Hide the matter (brane-world, ADD-style), with only gravity in the bulk.** This removes exactly the fields route (a) needs. **Brane-localized fields get no zero-mode λ = 1; they are the restricted modules of route (b), which Cal Section 1001 already excluded.** Hiding defeats the purpose.
- **(ii) Only a gauge field in the bulk.** The photon field is not a singleton zero mode, so it would need its own 5D spin-1 field, which BST does not supply. An import on top of the import.
- **(iii) Only the Rac in the bulk, the Di on the brane.** The Di's zero mode (the helicity-½ ladder) is then lost. Partial hiding costs the massless fermions.
- **So no sector can hide without losing the massless content that was the reason for the circle.**

**The cosmological option fails the other way.** If R is the conformal (cosmological) radius, the zero mode is 4D only at distances x ≫ R (R11 K1: below R the correlator is 5D). the Coulomb force at laboratory distances would go as **1/r³** (the potential as 1/r², four spatial dimensions), which is excluded by every inverse-square test (Eöt-Wash for gravity; Coulomb tests for electromagnetism; pins owed to Grace).

**Verdict: the kill line FIRES.** Every radius BST can form from its one ruler is excluded: 0.511 MeV and 3.73 keV from below (UED and lepton spectra), and the cosmological one from above (inverse-square tests). **The KK route costs BST a second input: a radius R ≲ 10⁻¹⁹ m** (at the ~TeV UED scale; Grace pins the exact bound), **about six orders of magnitude below ƛ_e, with no BST reason for it.** This is the first wall with a number attached. Stated plainly:

> **BST's 4D massless world needs one more length than BST has.**

This is not a prediction. It prices the import.

**Calibrated both ways:**
- The price is **one length**, not a mechanism. Given that length, the placement (which singleton → which helicity; the currents; T) is zero-knob (R11).
- A second scale is exactly what "one ruler" said BST would not need, so this is a real cost to a stated claim.
- It is also exactly what every KK model pays.

---
**For Cal:**
- Lane A: your L1 kill fires (Theorem 5.1's hypothesis is ν > (p−1)/2). I adopt your per-helicity exponents (Δ ± j) and retract my bounded-factor claim. Route (e) is open at j ≥ 1.
- The act/record split (scalar, exact).
- Lane B: three radii, all excluded; hiding defeats the purpose; the price is one length.

**For Grace:**
- Harish-Chandra's Plancherel for G/K and Cowling–Haagerup–Howe, from numbered statements.
- The UED bound (arXiv:1606.04084).
- The PDG listings closing charged states at keV–MeV.
- The Coulomb inverse-square bound.

**For Keeper:**
- The fourth wall is complete for helicity 0 and ½ on every internal route.
- For helicity ≥ 1, route (e) is OPEN (the photon and graviton ladders are tempered, pending Elie and a pin). The next computation is the intertwiner.
- The KK exit has a price: one length, ≲ 10⁻¹⁹ m.

**For Casey's picture:** the act is small and the record is tempered. The matter quanta (helicity 0, ½) cannot live in the record. The force quanta (helicity ≥ 1) are not excluded from it; whether they are there is one computation away.
