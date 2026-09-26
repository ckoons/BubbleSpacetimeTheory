---
node_type: k_audit
id: K1927
title: "Atomic-shell lane (Casey, K1926 Addendum 4, scoped to STRUCTURE): hydrogen's SO(4,2) representation is NOT a summand of H²(D_IV⁵) restricted to SO(4,2) — nor of any unitary scalar holomorphic module of SO(5,2). It IS the Wallach point (minimal representation) of the sub-geometry D_IV⁴. Verdict on Casey's three readings: recapitulation, not containment."
date: 2026-09-26
author: Keeper
instrument: play/keeper_K1927_shells_branching.py (ALL PASS, with a negative control)
lane: Int (external representation / structure); fresh — didwe "hydrogen SO(4,2) branching shells" = 0 hits; differs from K1878 (energies, STOP) by claiming structure only, per Casey's 19:42 scope
---

# K1927 — Hydrogen is the Wallach point of D_IV⁴, not a piece of H²(D_IV⁵)

*Keeper's independent derivation, written 10:45 EDT before Lyra's branching (round 5, Lyra item "branch H² to SO(4,2)") has landed. It is a second route for comparison, not a ruling on her work. Lyra: compare when yours is filed.*

**Kill line (written first).** Reading 1 ("isomorphic": hydrogen's representation is contained in the physical module) dies if no summand of H²(D_IV⁵)|SO(4,2) has hydrogen's K-types.

## 1. The objects (quoted invariants, not coordinates)
- **Physical module:** H²(D_IV⁵) at the Hardy point, scalar weight λ = n_C/2 = 5/2 (corpus G3).
- **K-types of a scalar holomorphic module H_λ(D_IV^n):** S(ℂⁿ) ⊗ C_λ. Degree-d polynomials split as ⊕_j H^{d−2j}·Q^j (harmonics times powers of the quadric), with SO(2) weight λ + d. At the Wallach point λ = (n−2)/2 only the harmonics survive.
- **Hydrogen (Fock 1935; Barut–Kleinert 1967; Malkin–Man'ko 1965 — pins owed, Grace's round-5 item 4):** the ladder representation of SO(4,2) is the scalar module at λ = 1. That is the Wallach point of D_IV⁴, and so the minimal representation. Its K-types are the harmonics of degree l on ℂ⁴, of dimension (l+1)², at SO(2) weight l + 1 = n. **That is the shell structure n², with no multiplicity and no extra quantum number.**

## 2. The branching (by K-types)
ℂ⁵ = ℂ⁴ ⊕ ℂ. Each power of the normal coordinate raises the SO(2) weight by one. SO(5) → SO(4) takes H^m to ⊕_{l≤m} H^l (Gelfand–Tsetlin). So

**H_λ(D_IV⁵)|SO(4,2) = ⊕_{k≥0} H_{λ+k}(D_IV⁴)**, multiplicity-free: the normal-derivative (Taylor) expansion (Jakobsen–Vergne 1979 — pin owed).

The instrument checks this as an identity of K-types to weight λ + 40. The negative control, dropping one summand, is detected. The K-type match decides the decomposition because the restriction is a sum of unitary highest-weight modules and their characters are triangular in the weight.

## 3. The verdicts
1. **Containment: NO.** For H² (λ = 5/2) the summands have weights 5/2, 7/2, …; hydrogen's weight is 1. More strongly, for any unitary scalar module of SO(5,2) the summands have weight λ + k ≥ λ. The Wallach set of D_IV⁵ is {0} ∪ [3/2, ∞) (Faraut–Korányi Ch. XIII — pin owed), so every nontrivial λ is at least 3/2 > 1. **No unitary scalar module of D_IV⁵ contains hydrogen on restriction.** Scope: scalar modules only. Vector-valued and non-holomorphic modules were not examined.
2. **Recapitulation: YES, and exactly.**
   - (a) Hydrogen is the minimal representation of the sub-geometry D_IV⁴ ⊂ D_IV⁵. It holds the same structural position (the Wallach point) that the corpus calls the seed for D_IV⁵ itself (λ = 3/2; `notes/BST_GC17c_Wallach_Point_Modularity_Seed.md`).
   - (b) D_IV⁵'s own minimal representation at level m carries SO(5)-harmonics of dimension 1, 5, 14, 30, 55, 91, … (square pyramidal numbers). Under SO(4) these are **exactly the spinless hydrogen states with n ≤ m + 1: the shells filled up to m + 1.**
   - (c) D_IV⁵'s minimal representation restricts to H_{3/2}(D_IV⁴) ⊕ H_{5/2}(D_IV⁴). Hydrogen's λ = 1 sits one half-step below both.
3. **Casey's third reading ("the D_IV⁵ representation in 3D")** is the most precise of the three once "3D" is read as the sub-geometry D_IV⁴, whose Šilov boundary is 3+1 compactified Minkowski space. Hydrogen is the construction that gives D_IV⁵ its minimal representation, carried out one dimension down.

## 4. What this does NOT claim
- No energies. The Coulomb 1/n² is 3D dynamics (Casey, 19:42).
- No periodic table. The cumulative 2n² sums (2, 10, 28, 60) match the noble-gas closures only at 2 and 10. The real table follows Madelung ordering, which is dynamics.
- No derivation of hydrogen from BST. The structural statement is standard representation theory. **BST's new content is only the placement:** the atom's symmetry is the minimal representation of the sub-geometry one step down from the one BST starts from.

## 5. Owed
- **Grace:** pin Jakobsen–Vergne 1979 (J. Funct. Anal.; the restriction of holomorphic representations) and the Faraut–Korányi Wallach-set statement, from the source.
- **Lyra:** compare with the round-5 branching; disagreement on any line gets its own resolution.
- **Cal:** is "recapitulation" a position (the Wallach point is intrinsic to D_IV⁴) or a coordinate? My reading: a position, because the Wallach set is an invariant of the domain.
- **Elie:** the instrument is Keeper's. The toy with a control from round 5 stays Elie's and is independent.

**Confidence.** Containment NO: high for scalar modules. The argument is a weight inequality on invariants, not a fit. Recapitulation (a) and (b): exact counts, with the instrument retained.
