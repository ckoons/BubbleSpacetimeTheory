---
title: "LAG-2 Phase 2 (start): Embedding of ℝ^{3,1} ⊂ D_IV⁵"
author: "Lyra"
date: "2026-05-17"
status: "Phase 2 PARTIAL — embedding question articulated + candidates evaluated"
parent: "BST_LAG2_Scoping_and_Phase1.md"
toy: "play/toy_3004_lag2_phase2_embedding.py"
---

# LAG-2 Phase 2 (start): Embedding Question

Phase 1 (T2340) identified the dimensional split: dim_R(D_IV⁵) = rank² + C_2 = 4 + 6. Today's Phase 2 start addresses the next question: **WHICH 4-dim sub-locus of D_IV⁵ is the external spacetime ℝ^{3,1}?**

## The question

The dimensional split is forced (Phase 1). The embedding is not — there are multiple candidate 4-dim sub-loci of D_IV⁵, and we need to identify which is the canonical choice for dimensional reduction.

Once embedded, the orthogonal complement (6-dim) is the internal compactified manifold. The reduction integral S_4D = ∫_{internal} S_BST integrates over this 6-dim complement.

## Constraints on the embedding

The 4-dim sub-locus must:

1. **Have the right dimension**: real dim = 4 = rank²
2. **Be totally geodesic** (or close to it) — so the reduction integral has a clean structure
3. **Support a Lorentz-signature metric** (or Wick-rotatable to one) — D_IV⁵'s Bergman metric is positive-definite Riemannian; we need to extract the (3+1) Lorentz signature somehow
4. **Be BST-structurally natural** — derivable from D_IV⁵'s symmetries, not chosen ad hoc
5. **Have a 6-dim "orthogonal complement"** that carries the internal structure cleanly

## Candidate sub-loci

### Candidate A: D_IV² ⊂ D_IV⁵ (sub-type-IV bidisk-like)

D_IV² = SO_0(2,2)/[SO(2)×SO(2)] is a Hermitian symmetric domain with complex dim 2, real dim 4.

**Embedding**: D_IV² ⊂ D_IV⁵ as totally geodesic sub-domain (Cartan classification of sub-Cartan-types of D_IV^n).

**Pros**:
- Real dim 4 ✓
- Totally geodesic ✓ (Hermitian symmetric sub-domain)
- BST-structurally natural ✓ (D_IV² is a smaller Cartan type IV)
- Has SO(2,2) action — provides 2 "time-like" directions, 2 "space-like" — close to Lorentz (3+1) but not exact

**Cons**:
- (2,2) signature, not (3,1) — needs an additional involution or signature choice to recover (3,1)
- The complement D_IV⁵ \ D_IV² is not naturally a 6-dim Hermitian symmetric space (it's a coset with extra structure)

### Candidate B: 4-ball sub-locus of M(D_IV⁵)

T2328 showed M(D_IV⁵) = open 5-ball in ℝ^5. Take the 4-ball M(D_IV⁵) ∩ {x_5 = 0} as the external spacetime.

**Pros**:
- Real dim 4 ✓
- BST-structurally natural ✓ (sub-locus of the canonical Möbius locus)
- All real (no imaginary coordinates) — Euclidean signature, Wick-rotatable to Lorentzian
- Complement = 6 dims (1 from x_5 + 5 from imaginary parts) — clean dim accounting

**Cons**:
- Not totally geodesic in general (4-ball ⊂ 5-ball in Euclidean metric is geodesic; in Bergman metric on D_IV⁵ it's not)
- Choice of "x_5 = 0" is arbitrary — any (5-1)-dim sub of the 5-ball would work; need a canonical reason for THIS slice
- The complement isn't a single connected 6-dim manifold

### Candidate C: Cartan involution fixed locus

Every bounded symmetric domain has a Cartan involution θ. The fixed-point set of θ on D_IV⁵ is the maximal compact sub-group K's orbit through the origin — but K is the isotropy group, so its orbit is just {0}, not 4-dim.

Alternative: use an "anti-Cartan" involution σ such that the fixed set σ-fixed is a 4-dim sub-manifold.

**Pros**:
- If exists, naturally Lorentz signature (σ might be the analog of complex conjugation in a Lorentzian sense)

**Cons**:
- Construction of σ is non-obvious for type IV; needs to be worked out
- May not give exactly 4-dim fixed locus

### Candidate D: A Lagrangian sub-manifold

A Lagrangian sub-manifold of D_IV⁵ (with respect to its symplectic / Kähler structure) has real dim = (complex dim) = n_C = 5. Too large by 1.

A 4-dim sub-manifold of a Lagrangian L ⊂ D_IV⁵ would work if natural. But Lagrangian is 5-dim, sub-Lagrangian 4-dim is not standard.

### Candidate E: 4-dim totally-geodesic sub of M(D_IV⁵)

T2328's M(D_IV⁵) is a real 5-ball. Its totally-geodesic 4-dim sub-manifolds (in the Bergman-restricted metric on M) are 4-dim hyperbolic balls H^4 ⊂ H^5 = M(D_IV⁵).

**Pros**:
- Real dim 4 ✓
- Totally geodesic ✓ (within M, the 4-ball is geodesic)
- Hyperbolic structure ✓ — H^4 has (-,+,+,+) signature after Wick rotation
- BST-structurally natural ✓ (canonical 4-dim sub of canonical 5-dim Möbius locus)

**Cons**:
- H^4 is Lorentz-signature after Wick rotation, not directly; standard physics interpretation requires Wick rotation
- Complement (6-dim) includes the imaginary-direction Hermitian part of D_IV⁵ \ M, not a single manifold

## Leading candidate: E (H^4 ⊂ M(D_IV⁵))

Among the five candidates, **E is the leading choice** because:

1. **All constraints satisfied**: 4-dim ✓, totally geodesic ✓, Wick-rotatable to Lorentz ✓, BST-natural ✓, has 6-dim complement ✓
2. **Builds on prior work**: T2328 already identified M(D_IV⁵); E is its canonical 4-dim totally-geodesic sub
3. **Hyperbolic structure**: H^4 with negative curvature matches AdS_4 / dS_4-style cosmology — natural for cosmological reduction
4. **Wick rotation is standard**: physicists use Wick rotation routinely between Euclidean H^4 and Lorentzian H^4 / AdS_4

**Specifically**: external spacetime ≅ H^4 ⊂ M(D_IV⁵) ⊂ D_IV⁵, then Wick rotate H^4 → AdS_4 or ℝ^{3,1} per physical interpretation.

## 6-dim internal complement

If external ≅ H^4 ⊂ M(D_IV⁵), the complement is D_IV⁵ \ H^4 with real dim 10 − 4 = 6 = C_2.

Decomposition of complement:
- 1 real dim from M(D_IV⁵) \ H^4 (the "extra" Möbius direction)
- 5 real dims from D_IV⁵ \ M(D_IV⁵) (the imaginary part)
- Total: 1 + 5 = 6 = C_2 ✓

The 1+5 internal split is itself BST: 1 = trivial, 5 = n_C. The internal complement has structure {1 trivial + n_C internal Hermitian} = 6 = C_2.

## What Phase 2 START produces today

1. The embedding question articulated precisely
2. Five candidates evaluated against five constraints
3. Leading candidate identified: **H^4 ⊂ M(D_IV⁵)** with internal complement 6 = 1 + n_C
4. BST-structural reading: external 4D = rank² emerges as H^4 totally-geodesic sub of M; internal 6 = C_2 splits as 1 + n_C
5. Wick rotation to physical Lorentz signature flagged as standard step

## What Phase 2 FULL still needs (multi-week)

- **Phase 2.1** (~3-5 days): formal proof that H^4 ⊂ M(D_IV⁵) is the canonical totally-geodesic 4-dim sub-locus
- **Phase 2.2** (~1-2 weeks): compute the reduction integral S_4D = ∫_{internal 6-dim} S_geom[Bergman curvature] explicitly
- **Phase 2.3** (~3-5 days): verify the 4D effective action S_4D recovers Einstein-Hilbert at low energy

Total Phase 2: 2-3 weeks, staged. Today closes the LEADING-CANDIDATE identification (the gate to Phase 2.1-2.3).

## Tier reading

Phase 2 START identifies the embedding to I-tier. Full closure of the embedding (Phase 2.1) promotes to D-tier. The reduction integral (Phase 2.2) is the substantive multi-week work.

## Connection to other LAG work

- **LAG-1 S1 (T2339)**: Bergman Dirac D_B is defined on full D_IV⁵; restriction to H^4 ⊂ M gives the 4D Dirac after Wick rotation
- **LAG-2 Phase 3**: with H^4 embedding fixed, the 6 S_BST terms get reduced via integration over the 6-dim internal complement
- **Möbius cohomology (T2328-T2335)**: M(D_IV⁵) is the canonical Möbius locus; H^4 is its canonical 4-dim sub. The Möbius mechanism (T2091) places leptons on M; under H^4 ⊂ M embedding, lepton mass formulas restrict to 4D spacetime — consistent.

## Status

Phase 2 START complete: leading candidate identified (H^4 ⊂ M(D_IV⁵), internal 1 + n_C = 6). Full Phase 2.1-2.3 deferred to multi-session work.

— Lyra, 2026-05-17 ~16:30 EDT
