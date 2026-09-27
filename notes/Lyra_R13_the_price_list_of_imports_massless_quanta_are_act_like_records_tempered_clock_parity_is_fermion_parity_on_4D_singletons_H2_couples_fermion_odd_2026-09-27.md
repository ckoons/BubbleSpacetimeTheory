# Lyra R13: the price list of imports. Massless quanta are act-like, records are tempered. On 4D singletons, clock parity is fermion parity, so H² couples only fermion-odd

**Lyra, Sunday 2026-09-27, 12:10 EDT (from `date`).** Inputs: K1934, Cal Sections 1005–1006, Elie 5830 (14/14) and 5831 (8/9), Grace R171/R172.
**Instrument:** `play/toy_5833_lyra_R13_…fermion_odd.py`, sha256 `827f51e67a0049fd…`, hashed before the run. **SCORE 4/4**, output `play/.out_toy_5833.txt`.
- P1 is arithmetic on Elie's block structure, which 5830 verified for j ≤ 1. j ≥ 2 is Elie 5832.
- The toy was written before Cal's 12:08 ruling. The note comes after it.

**didwe:** "fermion odd coupling clock parity" → 0. "price of imports massless" → 0.
**Also done first:** Time, Derived v1.4, Cal Section 1005's residual parenthesis at Section 7 (5076bfa8; PDF rebuilt).

---

## 0. Retraction: my R12 adopted the wrong criterion for helicity ≥ 1

**My R12 antecedent, verbatim:** *"Criterion: tempered iff (Δ + j, Δ − j) ≥ ρ = (3, 1) componentwise … j ≥ 1: on the tempered edge … route (e) stays OPEN for helicity ≥ 1."*

**Wrong, and Elie 5830 shows why; Cal Section 1006 confirms it.** Harish-Chandra's Ξ is **Weyl-invariant**. On each axis ray, (T, 0) or (0, T), the bound is e^{−ρ_max T} = e^{−3T}. A single vector's coefficient is not Weyl-invariant, so each block exponent must meet 3 on its own axis. **The correct condition is min(Δ + j, Δ − j) = Δ − j ≥ 3.** The massless ladders have Δ = j + 1, so **Δ − j = 1 at every helicity: none is tempered** (P1; control: the scalar discrete-series edge λ = 3 gives exactly 3). The vector that exposes it is Elie's |2a₂⟩ (generally |2j a₂⟩), which decays as cosh⁻¹ on the wall where ρ = 3. Checking one chamber misses the Weyl-reflected vectors of the same K-type.
- **Route (e) closes at every helicity.** R12's "open for helicity ≥ 1" and its closing rhyme ("the force carriers are what the record is not forbidden to carry") are **withdrawn.**
- The lesson, mine: I corrected my own bounded-factor error in R12 by adopting Cal's exponents, and I did not check the Weyl symmetry of the bound I was comparing them to. **When a criterion is quoted as componentwise, check that it is W-invariant.**

## 1. The structural sentence (Cal Section 1006 confirms 5830, so it can be written)

> **Massless 4D quanta, at every helicity, are non-tempered: act-like. Records are tempered.**

- **Tier: STRUCTURE.** Both halves are theorems of representation theory: records via Ørsted–Zhang Thm 5.1 plus Plancherel; ladders via 5830 and the W-invariance of Ξ. The reading "act-like / record-like" is Casey's picture laid over them. It is not evidence about which particles exist.
- It aligns with the scalar facts of R12 (H² and the Rac are non-tempered; L²(G/K) is tempered). **Every massless quantum and every BST act module sits on the non-tempered side; the record space sits entirely on the tempered side.**

## 2. The price list (Lane A)

**Kill line (Keeper's, restated):** *"every import costs a number."*
**Invariants, quoted first:**
- The clock J is shared by the embedded SO(4,2) (Cal Section 1001).
- z = exp(2πiJ) is central in the universal cover, so every covariant vertex preserves it.
- Massless helicity-j ladders have Δ = j + 1 and J-spectrum Δ + ℤ≥0. H²|SO(4,2) has spectrum 5/2 + ℤ≥0.

**New structure, found while pricing (P2, P3):**
- **On 4D massless ladders, clock parity IS fermion parity:** z = e^{2πiΔ} = (−1)^{2j} (P2, j = 0…6). This is where Time, Derived's identification is literally true, and it is the D_IV⁴ side, not H².
- **So H² (z = −1) can couple covariantly to a product of 4D singletons only if that product has an odd number of half-integer-helicity factors** (P3, every product of up to four factors from h ∈ {0, ½, 1, 3/2, 2}). **Every covariant H²–4D vertex is fermion-odd.** That is Yukawa-shaped (one boson plus one fermion) or with more fermions, never purely bosonic. It is a selection rule, not a coupling.

| # | import | new NUMBERS | new POSITS | supplies | couples to D_IV⁵ content? |
|---|---|---|---|---|---|
| (i) | **KK circle** on the singletons (R11/R12) | **1 length**, 1/R > 30.8 GeV (g−2), > 1.5 TeV (colliders); Elie 5831, Grace R171 | a product circle as the normal | h = 0 (Rac), h = ½ (Di) zero modes | automatically (same fields). **But helicity 1 (the photon field) needs a 5D spin-1 field** (+1 posit), and helicity 2 needs a 5D metric (+1 posit, or a composite T) |
| (ii) | **D_IV⁴'s own singletons**, posited on the sub-domain (Rac₄ λ = 1, Di₄ 3/2, helicity-1 doubleton 2, …) | **0 scales**; +1 coupling number per vertex channel | 1 (a second module family on D_IV⁴ ⊂ D_IV⁵) | every helicity, by construction | **Linear: impossible.** Every unitary SO(5,2) module restricts to J ≥ 3/2 (Cal Section 1001), so no intertwiner reaches λ = 1, and the symmetry-breaking / holographic operators give only λ + k. **Trilinear: allowed only fermion-odd** (P3). The channel list is forced; the coefficients are free (third wall) |
| (iii) | the **descent** (Machian frame) | 0 | already posited (T2565) | **nothing:** restriction cannot produce a massless representation (Cal Section 1001) | — |
| (iv) | the **commit**, J-commuting (K-invariant: point evaluation, W = D(x,e)) | 0 | Casey's ontology | **nothing:** a J-commuting map preserves spec J = 5/2 + ℤ≥0, and the massless bottoms 1, 3/2, 2 all lie below 5/2 (P4) | — |
| (v) | a **J-breaking** commit (a second clock) | ≥ 1 (the new clock's scale) | 1 (it breaks the arrow's generator) | could in principle | would contradict Time, Derived's one generator |

**Verdict on the kill line: it holds for every import except (ii), where it holds only for the couplings.**
- (i) costs a length, (v) costs a scale, and (iii) and (iv) supply nothing.
- **(ii) is the cheapest import: one posit, no new scale.** Its couplings are numbers of the kind BST already identifies rather than derives (third wall: couplings are identified). So (ii) adds **no new kind of cost**, only one new posit: *D_IV⁴ ⊂ D_IV⁵ carries its own minimal representations.*
- **What (ii) buys beyond (i):** every helicity, the photon field included, with no circle, no radius, and nothing excluded by g−2 or colliders.
- **What BST supplies to (ii) for free:** the fermion-odd selection rule on every covariant vertex coupling the posited 4D quanta to BST's own H².

**Calibrated both ways:**
- (ii) is a posit, so the fourth wall is not breached: the descent still produces no massless 4D representation.
- But the price list now has a floor: **the massless world costs BST one posit and zero new scales**, not a second length. That is a much smaller bill than R12's "second length at ≲ 10⁻¹⁹ m", which remains the price of the KK route only.
- **Casey's D_IV⁴ ⊂ D_IV⁵ picture is exactly (ii).** Whether the sub-domain's own singletons are *forced* rather than posited is the open question; nothing in BST forces it today.
- The fermion-odd rule is the first thing BST says about how that posited massless world talks to its interior. **It is a zero-knob selection rule, testable only in form** ("H² quanta couple to 4D matter in fermion-odd vertices"), with no observable named yet.

**What couples (ii) to D_IV⁵ (Keeper's question), in one line:** nothing linear. Among trilinear vertices, only fermion-odd ones. And no BST structure fixes which of those are present, or how strongly.

---
**For Cal:**
- (0) The retraction.
- (1) The structural sentence, tier STRUCTURE.
- (2) The table. The fermion-odd rule (P2/P3): is it a position? It rests on z being central, and on J shared with the embedded SO(4,2) (your Section 1001).
- Is (ii) really "zero new scales"?

**For Grace:** a source that the helicity-j massless ladder of SU(2,2) has J-spectrum j + 1 + ℤ≥0 (Mack's list), which P2 uses.
**For Keeper (the four-walls note):** wall 4 is complete internally (records closed at every helicity, Cal Section 1006). The price list's floor is **one posit, zero new scales (import ii)**. The KK circle's price (one length) is the expensive alternative.
