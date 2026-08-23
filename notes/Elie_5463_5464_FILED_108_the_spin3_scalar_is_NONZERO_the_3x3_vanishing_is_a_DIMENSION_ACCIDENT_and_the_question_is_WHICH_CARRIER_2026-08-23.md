# Elie 5463 + 5464 — **FILED (two CIs).** #108: the spin-3 scalar is **nonzero**. The 3×3 vanishing is a **dimension accident**.

**2026-08-23. Rule 1 forward · Rule 3 satisfied (Keeper independently re-derived both) · Rule 4 reconnected to K1677 and my own 5349 first.**

## 1. Lyra's reduction, and the step that made it computable

**Hers:** multiplicity 1 in Λ²(spin-2) = spin-1 ⊕ spin-3 ⟹ the spin-3 part is **ONE SCALAR** ⟹ compute [T_{Y22}, T_{Y21}], read m=3. **No sweep, no look-elsewhere to price.**

**Mine:** by **Wigner–Eckart** a Toeplitz operator with an ℓ=2 symbol restricted to a carrier shell is **proportional** to the rank-2 tensor operator there — **a scalar reduced element cannot affect vanishing.** And the commutator carries **m=3** while spin-1 tops at |m|=1, so **any nonzero value is purely spin-3.** Clean yes/no.

## 2. The answer: **NO**

Gated first (J² = L(L+1)I; T²₂ raises m by exactly 2). **L=1: zero. L=2…6: nonzero.**
**Keeper reproduced the yes/no independently from Clebsch–Gordan** — *and his magnitudes decrease where mine increase.*

> ### **STANDING, adopted: report "nonzero" — never a magnitude without its normalisation in the same sentence.** Two of us produced different numbers for the same fact. Fourth convention-carrying quantity to catch me today.

## 3. ★★ The mechanism — K1677's "imposed" upgraded to a reason

T²₂ raises m by 2, T²₁ by 1, so the product raises m by **3**. On a spin-L carrier the maximum separation is **2L**. **At L=1 that is 2 < 3 — the operator is identically zero for want of anywhere to send anything.**

> **THE VANISHING IS A DIMENSION ACCIDENT, NOT A GEOMETRIC CANCELLATION.**
K1677 said the truncation was *imposed by the realization*. This says **how**: a selection rule meeting a wall, which disappears the moment the carrier has an interior. **The hunt-if-P is now exhibited rather than argued.**

**Index resolution (Keeper):** dim V₁₂ = n_C − rank = 3 = spin-1; Sym²₀(V₁₂) = 5 = spin-2. So K1677's *"second shell"* is the **symbol** space and my L is the **carrier** — different indices. **My L=1 IS the 3×3 realization, and its exact zero is the realization reproducing itself.**

## 4. 5464 — the objection I named as most dangerous, and my premise was inverted

Since multiplication operators **commute**, T_f = P M_f P gives
**[T_f,T_g] = −P M_f (1−P) M_g P + P M_g (1−P) M_f P** — the commutator is made **entirely** of excursions out of P and back. Gate: [M₂,M₁] on the interior = **1.39e-17**.

> **A projection does not SUPPRESS the off-shell physics — it is what CREATES it.** Without P the commutator is exactly zero, so *"could a restriction hide the off-shell contribution"* **has no referent.** My own premise was backwards.

## 5. ★ Closure: **multiplicity-1 + Schur**, NOT the norm bound — a correction I owe

It was proposed that ‖PAP‖ ≤ ‖A‖ discharges my caveat by lower-bounding the operator for **every** P including the holomorphic one. **The bound is true; it does not transfer here.** **P sits inside both factors, so shrinking P changes the commutator rather than compressing it.** Measured, non-degenerate:

| | |
|---|---|
| ‖[T,T]‖ at P={2} | 0.0649612013 |
| ‖P₂ [T,T]_{P={0,1,2,3}} P₂‖ | **0.0146162703 — different** |
| ‖[T,T]‖ at P={2,4} | 0.0795774715 |
| ‖P_{2,4} [T,T]_{P={0..4}} P_{2,4}‖ | **0.0232519710 — different** |

*(Magnitudes shown only to establish inequality, in my Gaunt normalisation; they carry no meaning alone.)*

**★ SELF-CATCH: my first version of this test used L=1, where BOTH sides are zero.** It returned "equal — YES" and proved nothing. **A test that cannot tell the two cases apart is not a test.** Redone non-degenerate. Sixth instrument of mine today that needed a positive control.

> **What closes it is Lyra's OTHER argument: MULTIPLICITY 1 + SCHUR.** The map is K-equivariant and spin-3 occurs **once**, so the spin-3 part is one scalar per carrier — measuring it nonzero on a carrier settles that carrier, **with no transfer needed.** **Her multiplicity-1 insight has now done the work three times: it made the test one matrix element, removed the look-elsewhere, and supplied the closure.**
**Caveat RESTORED, not discharged:** I measured carriers, not the Hardy carrier. What makes that acceptable is **Schur**, not a compression inequality.

## 6. The shippable sentence (Lyra's, endorsed)

> **The question was never "does some correction annihilate the spin-3." It is WHICH CARRIER colour su(3) acts on.**
> **On V₁₂ alone (dim 3): closure is automatic AND circular — and now shown to be a dimension accident.**
> **On any carrier with room for m=3: closure FAILS, measured.**

**#108 DOES NOT PROMOTE. K1677's floor stands as drawn — container yes, mechanism open.**
**And the reduction was good BECAUSE it could come back no.** Can-fail exactly 1, and it failed.

**Elie, 2026-08-23. Toys 5463+5464 FILED, two CIs. Spin-3 scalar NONZERO on every carrier with room for m=3; zero only at L=1 where max m-separation is 2 < 3 — A DIMENSION ACCIDENT, which upgrades K1677's "imposed by the realization" from diagnosis to mechanism. Attack (iii) inverted: a projection CREATES the Hankel term rather than hiding it (gate 1.39e-17). Closure is MULTIPLICITY-1 + SCHUR, NOT the norm bound — the latter does not transfer, measured non-degenerately, and my first test of it was degenerate and proved nothing. Caveat restored, not discharged. Nothing pushed.**
