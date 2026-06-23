---
title: "F298 — THE EXACT RADIAL EIGENVALUE, settled by Schur's lemma (Casey: 'get the exact radial eigenvalue'). This ENDS the F294→F295→F297 oscillation because it is a theorem, not a fit-preference. THE COMPUTATION: the scalar holomorphic discrete series of SO(5,2) on H²(D_IV⁵) is ONE irreducible representation. Its K-types under K = SO(5)×SO(2) are the graded polynomials C[z_1..z_5]: K-type (m_1,m_2) has harmonic/spin degree h = m_1−m_2 and radial power j = m_2 (the r^{2j} factor), with SO(2) conformal energy E = λ_0 + (m_1+m_2). THE DECISIVE FACT (Schur): the quadratic Casimir is CONSTANT on an irreducible rep, so it does NOT distinguish radial levels — the (1,1) r²-mode and the (0,0) ground have the SAME Casimir. Therefore there is NO within-irrep quadratic radial eigenvalue; the only quantum number that moves along the radial tower is the LINEAR conformal energy. EXACT RESULT: the first radial scalar excitation 0⁺⁺* = the (1,1) = r²-mode sits at E = λ_0 + 2 = 7 (LINEAR), degenerate with 2⁺⁺ (also E=7), → m(0⁺⁺*) = (7/5)·1720 = 2408 MeV (lattice ~2670, ~10%, within quenched excited-glueball error). RESOLUTION OF THE OSCILLATION: both Elie's q(q+4) (→2665) and my own ρ_rad=(4,1) → q(q+8) (→2564) imposed a quadratic that Schur FORBIDS within the irrep. My ρ_rad computation was answering a different question — the radial Laplacian eigenvalue for SPHERICAL functions (the principal-series/K-bi-invariant spectrum), which is genuinely quadratic but is NOT the holomorphic-discrete-series glueball operator. The glueball operator is the conformal Hamiltonian on the discrete series → LINEAR. So F295 (linear) was right; my F297 over-correction (back to quadratic) is RETRACTED, and Elie's retraction of q(q+4) is correct. CONSEQUENCE FOR CASEY #17: the spin-linear/radial-quadratic factorization and 'Curvature Principle at the operator level' framing is NOT established by this split — both spin and radial excitations are linear within the irrep. The ONLY quadratic structure is INTER-irrep (Grace's T2490 tower {6,10,12,14}); assigning 0⁺⁺* to a higher irrep by mass-fit is look-elsewhere (what killed q(q+4)). Count HOLDS 4."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-23 Tuesday (date-verified ~09:00 EDT)"
status: "v0.1 — DEFINITIVE radial eigenvalue via Schur. Scalar holo discrete series = ONE irrep; K-types = graded polynomials, (m_1,m_2) → spin h=m_1−m_2, radial j=m_2, energy E=λ_0+m_1+m_2. Schur: Casimir CONSTANT on the irrep → no within-irrep quadratic radial eigenvalue → radial tower is LINEAR (conformal energy). EXACT: 0⁺⁺* = (1,1) r²-mode at E=λ_0+2=7, degenerate with 2⁺⁺, m=2408 MeV (lattice ~2670, within quenched error). Both q(q+4) (Elie) and q(q+8) (my ρ_rad) imposed a Schur-forbidden within-irrep quadratic; my ρ_rad answered the SPHERICAL-function spectrum (different object). F295 linear RIGHT; F297 over-correction RETRACTED. Casey #17 factorization NOT established — both directions linear; only inter-irrep (T2490) is quadratic, and fitting 0⁺⁺* there is look-elsewhere. Count HOLDS 4. For Casey, Elie, Grace, Cal, Keeper."
---

# F298 — the exact radial eigenvalue: LINEAR, by Schur's lemma (the oscillation ends here)

Casey asked for the exact radial eigenvalue. Elie and I had swapped positions twice (F294 quadratic → F295 linear → my F297 back to quadratic → Elie now linear), which is the signature of nobody having actually computed it. Rep theory gives a definitive answer, and it's a *theorem*, so it ends the back-and-forth.

## The computation

The scalar holomorphic discrete series of SO(5,2) on H²(D_IV⁵) is **one irreducible representation**. Its K-types under K = SO(5)×SO(2) are the graded holomorphic polynomials C[z_1,…,z_5]:

  K-type (m_1, m_2):  spin/harmonic degree **h = m_1 − m_2**,  radial power **j = m_2** (the r^{2j} factor),  conformal energy **E = λ_0 + (m_1 + m_2)**.

| K-type | state | h (spin) | j (radial) | E |
|---|---|---|---|---|
| (0,0) | 0⁺⁺ ground | 0 | 0 | λ_0 = 5 |
| (1,1) | **0⁺⁺* (r² mode)** | 0 | 1 | λ_0 + 2 = 7 |
| (2,0) | 2⁺⁺ (spin-2) | 2 | 0 | λ_0 + 2 = 7 |
| (2,2) | 0⁺⁺** (r⁴) | 0 | 2 | λ_0 + 4 = 9 |

## The decisive fact (Schur's lemma)

The quadratic Casimir is central, so on an irreducible rep it acts as a **single scalar** — it is **constant across all K-types of one irrep**. The (1,1) r²-mode and the (0,0) ground have the *same* Casimir. Therefore:

- there is **no within-irrep quadratic radial eigenvalue**;
- the only quantum number that moves along the radial tower is the **linear conformal energy** E = λ_0 + (m_1+m_2).

**Exact radial eigenvalue:** the first radial scalar 0⁺⁺* = (1,1) sits at **E = λ_0 + 2 = 7**, degenerate with 2⁺⁺. In MeV: m(0⁺⁺*) = (7/5)·1720 = **2408 MeV** (lattice ~2670, ~10% — within quenched excited-glueball error). **Linear. Settled.**

## Why the quadratics were wrong (both of them)

Both Elie's q(q+4) (→2665) and my own ρ_rad = (4,1) → q(q+8) (→2564) imposed a quadratic that Schur **forbids within the irrep**. My restricted-root ρ_rad computation was answering a *different question*: the radial Laplacian eigenvalue for **spherical functions** (the K-bi-invariant / principal-series spectrum), which genuinely is quadratic — but that is **not** the holomorphic-discrete-series glueball operator. The glueball operator is the conformal Hamiltonian on the discrete series, which is linear. So I was computing the right number for the wrong object.

F295 (linear) was right. My F297 over-correction (back to quadratic) is **retracted**, and Elie's retraction of his q(q+4) is correct.

## What this does to the "Curvature Principle at the operator level" (Casey #17)

The appealing spin-linear / radial-quadratic factorization is **not established** — both spin and radial excitations are linear within the irrep. This is a clean negative on that framing. The **only** quadratic structure is **inter-irrep** (Grace's T2490 tower {6,10,12,14}); and assigning 0⁺⁺* to a higher irrep by mass-fit is exactly the look-elsewhere that killed q(q+4). So if 0⁺⁺* turns out genuinely heavier than 2⁺⁺ in precise lattice data, the explanation is "0⁺⁺* is the ground of a higher irrep" — but *which* irrep must be forced by structure (its J^PC and conformal energy), not chosen to fit the mass.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| Casimir constant on irrep (Schur) ⟹ radial tower is LINEAR | THEOREM (settles it) | — |
| exact radial eigenvalue: 0⁺⁺* = (1,1) at E = λ_0+2 = 7 → 2408 MeV | clean (= 2⁺⁺) | precise lattice spectroscopy |
| q(q+4) and q(q+8) both Schur-forbidden within irrep | retracted (mine F297) | — |
| Casey #17 spin/radial factorization | NOT established (both linear) | inter-irrep (T2490) is the only quadratic |

**Count HOLDS 4 of 26.** SU(3) scope. INTERNAL. The exact radial eigenvalue Casey asked for: **linear, E = λ_0 + 2, by Schur.**

@Elie — settled, and it's your linear reading: by Schur the Casimir is constant on the irrep, so the radial (1,1) r²-mode moves only in the linear conformal energy — E = λ_0 + 2 = 7, degenerate with 2⁺⁺ (2408 MeV). Both our quadratics (your q(q+4), my ρ_rad q(q+8)) are Schur-forbidden within the irrep; mine was actually the *spherical-function* Laplacian spectrum, a different object. So q(q+4) retracted (you) and my F297 quadratic retracted (me) — we converge on linear, by theorem. @Grace — the only quadratic is your inter-irrep T2490 tower; 0⁺⁺* fit to a higher irrep is look-elsewhere, so Casey #17's radial-quadratic leg is not established (note for the candidate). @Casey — the exact radial eigenvalue: it's **linear**, E = λ_0 + 2 = 7, by Schur's lemma (the Casimir can't distinguish radial levels within one irrep). 0⁺⁺* degenerate with 2⁺⁺ at 2408 MeV. That ends the oscillation — and it cost me a retraction of my own F297, which is the right outcome: the theorem beats both our quadratic fits.

— Lyra, Tue 2026-06-23 (date-verified ~09:00 EDT). F298: exact radial eigenvalue SETTLED by Schur. Scalar holo discrete series = ONE irrep; Casimir constant (Schur) ⟹ no within-irrep quadratic ⟹ radial tower LINEAR (conformal energy E=λ_0+m_1+m_2). 0⁺⁺* = (1,1) r²-mode at E=λ_0+2=7 = 2⁺⁺ energy → 2408 MeV (lattice ~2670, within quenched error). Both q(q+4) (Elie) and q(q+8) (my ρ_rad, actually the spherical-function spectrum) Schur-forbidden within irrep. F295 linear RIGHT; F297 over-correction RETRACTED. Casey #17 factorization NOT established (both linear); only inter-irrep T2490 is quadratic, fitting there = look-elsewhere. Count HOLDS 4.
