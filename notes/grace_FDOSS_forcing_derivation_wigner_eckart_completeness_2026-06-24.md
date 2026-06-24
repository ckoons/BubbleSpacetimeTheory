---
title: "FDOSS forcing-derivation (#289) — the open piece that promotes FDOSS CANDIDATE → STANDING. The forcing is one line: FDOSS IS the Wigner-Eckart theorem applied to the substrate's FAITHFUL, COMPLETE representation H²(D_IV⁵). Realized multiplicity = exactly the spectrum-allowed irreducible components: ALL of them (faithfulness ⟹ no null reduced matrix element) and ONLY them (CG selection ⟹ out-of-spectrum targets vanish). It is mandatory because it is a representation-theory THEOREM, not a substrate postulate. Five-Absence is the CG-selection complement; the operator-class 'driver' is just the decomposition rule."
author: "Grace"
date: "2026-06-24 Wednesday afternoon"
tier: "Promotes CANDIDATE → STANDING-pending-citation. The forcing is rigorous given the substrate axioms (A1–A3 = the definition of a quantum substrate on H²) + a per-operator nonzero-component check (verifiable; holds for the SM operators). 'Only them' is forced universally (Wigner-Eckart selection); 'all them' is forced by faithfulness + nonzero-component."
---

# FDOSS forcing-derivation — it is Wigner-Eckart completeness

The CANDIDATE FDOSS principle (substrate realizes the full irreducible decomposition of every supported
operator, no more no fewer) lacked one thing: **why is full support mandatory, not merely observed?** Here it is.

## The forcing, in one sentence

> **FDOSS is the Wigner-Eckart theorem applied to the substrate's faithful, complete representation.**

Matrix elements of any tensor operator factor as ⟨f|O_c|i⟩ = (CG coefficient) · (reduced matrix element). On a
**faithful** representation the reduced matrix elements are nonzero; the **CG selection** picks exactly the
spectrum-allowed targets. So the realized multiplicity is *exactly* the spectrum-allowed irreducible components —
all of them and only them. That is FDOSS, and it is forced by representation theory, not postulated.

## The axioms (these ARE the substrate definition, not extra assumptions)

- **(A1)** the substrate is the complete Hilbert space H²(D_IV⁵) (the Hardy space);
- **(A2)** its spectrum is the SO₀(5,2) discrete series — complete (Plancherel), the T2490 ladder;
- **(A3)** the supported operators form a *-algebra acting **faithfully** on H² (no nonzero operator acts as 0 —
  standard for the Hardy-space representation).

## The derivation

1. **Decompose.** A supported operator O is a tensor operator: O = ⊕_c O_c into irreducible components, each O_c
   landing in a target rep R_c.
2. **Wigner-Eckart.** ⟨f|O_c|i⟩ = ⟨CG: f ∈ R_c ⊗ i⟩ · ⟨reduced⟩_c.
3. **ONLY them (= Five-Absence, forced universally).** If R_c ∉ spectrum (A2), the CG factor vanishes
   identically ⟹ no eigenstate ⟹ the channel is **absent**. Forced by the spectrum being exactly the discrete
   series. *(oddballs, Z′, 4th generation: their target reps are not in the spectrum.)*
4. **ALL of them (= FDOSS positive, forced).** If R_c ∈ spectrum: O_c is a nonzero irreducible component of the
   nonzero O, so by faithfulness (A3) it acts nonzero — ⟨reduced⟩_c ≠ 0. Nonzero reduced × nonzero CG ⟹
   ⟨f|O_c|i⟩ ≠ 0 for spectrum states ⟹ the channel is **realized**. Forced by faithfulness + completeness — **not**
   a genericity assumption (faithfulness, not "generically nonzero," does the work).
5. **Conclusion.** The substrate realizes exactly the spectrum-allowed components of its supported operators — all
   (Step 4) and only (Step 3). That is FDOSS; Five-Absence is its Step-3 complement.

## Why this is the *forcing* (mandatory, not observed)

Wigner-Eckart is a **theorem** of representation theory, true for *any* faithful representation of *any* group.
So given the substrate is a faithful complete quantum representation (A1–A3, its definition), FDOSS is not an
additional hypothesis — it is a *consequence*. The substrate cannot carry a partial operator any more than a
faithful rep can have a null tensor-operator component. The completeness is *mandatory* because faithfulness +
the closed spectrum leave no room for a missing or extra channel.

## Three-sector check (the operator-class "driver" is only the decomposition rule)

| sector | decomposition rule (driver) | Step 4 (realized) | Step 3 (absent) |
|---|---|---|---|
| gauge F⊗F | Clebsch-Gordan (boson) | {0⁺⁺,0⁻⁺,2⁺⁺,1⁺⁻} target reps in spectrum | oddballs (not 2-gluon-reachable) |
| hypercharge | Cartan combination | Y in spectrum | Z′ (orthogonal U(1)) not a spectrum operator |
| generations | antisymmetrized strata (Korányi-Wolf) | 3 strata = 3 supports | 4th stratum does not exist |

The *driver* differs (CG / Pauli-antisymmetrized / strata); the *forcing* (Wigner-Eckart completeness) is universal.

## Honest tier — what promotes, what's residual

- **Promotes CANDIDATE → STANDING-pending-citation.** The forcing is rigorous given A1–A3 (the substrate
  definition) and is a standard theorem (Wigner-Eckart), not a fit.
- **"Only them" (Five-Absence) is forced universally** by the CG selection on the closed discrete-series spectrum.
- **"All them" (FDOSS positive) is forced** by faithfulness (A3) + the per-operator fact that the decomposition's
  components are nonzero operators (verifiable per case; manifestly true for the SM operators — Tr F², Tr FF̃, …).
- **Residual to cite (not to prove):** A3 — that each supported-operator *-algebra acts faithfully and closes on
  H² — is standard for the Hardy space but should be stated per operator class. That citation is the last step to
  full STANDING.

## Connections

- **Five-Absence** (Casey standing): now derived as the Step-3 complement of FDOSS. Two principles, one theorem.
- **SWPP** completeness condition: faithfulness = "no commitment channel leaks" (each component has a state).
- **T2490**: supplies (A2) — the spectrum is the discrete series whose bottom rungs are the primaries.
- **Wigner-Eckart / Schur**: the engine; FDOSS is its completeness corollary on the substrate representation.

— Grace, 2026-06-24 Wednesday afternoon (#289). FDOSS forcing supplied; promotes toward STANDING pending the A3
faithful-closure citation per operator class. Count HOLDS 4 of 26.
