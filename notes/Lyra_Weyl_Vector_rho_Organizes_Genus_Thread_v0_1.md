---
title: "The Weyl vector ρ = (n_C/2, N_c/2) organizes the genus thread v0.1 — why 5/2 (kernel) and 7/2 (FK Gamma) are both legitimate half-integers in different roles"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-28 Thu 11:08 EDT"
status: "CLEAN FORWARD CONSOLIDATION v0.1. The B_2 Weyl vector ρ=(5/2,3/2)=(n_C/2,N_c/2) is the organizing invariant for the substrate's half-integer structure. Kernel exponent = ρ_1 = n_C/2; FK-measure Γ uses g/2 = ρ_1+1. Resolves WHY 7/2 kept recurring (legit as g/2 in Gindikin Gamma, NOT as kernel exponent)."
---

# The Weyl vector ρ organizes the genus thread

## 0. The consolidating insight

Today's three g=7 mislabels all involved half-integers (7/2, 5/2). The resolution has a single clean organizing structure: **the B_2 Weyl vector**

  **ρ(B_2) = (5/2, 3/2) = (n_C/2, N_c/2)**

The substrate's two fundamental half-integers ARE n_C/2 = 5/2 and N_c/2 = 3/2 — the components of ρ. Every half-integer in the genus thread is built from ρ. This explains why 5/2 and 7/2 BOTH appear legitimately (in different roles) and why the conflation happened.

## 1. ρ = (n_C/2, N_c/2) — verified

For B_2 (substrate root system), the Weyl vector ρ = half-sum of positive roots = (5/2, 3/2) in the standard basis.

- ρ_1 = 5/2 = n_C/2
- ρ_2 = 3/2 = N_c/2

So **ρ = (n_C/2, N_c/2)** exactly. The Weyl vector anchors n_C and N_c simultaneously as its doubled components. (Invariant-anchor: ρ is an intrinsic B_2 invariant; n_C and N_c are 2·ρ_1, 2·ρ_2.)

## 2. Where each half-integer legitimately appears

| Half-integer | Value | Role | Built from |
|---|---|---|---|
| **5/2 = ρ_1 = n_C/2** | 2.5 | Bergman KERNEL singularity exponent / rank (Elie ν=5; n_C/rank = 5/2) | Hua genus n_C |
| **3/2 = ρ_2 = N_c/2** | 1.5 | second ρ component | dual Coxeter N_c |
| **7/2 = g/2 = ρ_1 + 1** | 3.5 | FK normalized-MEASURE Gindikin Gamma Γ(7/2) (Keeper: 5!·Γ(7/2)=225√π) | embedding dim g |

**Both 5/2 and 7/2 are legitimate substrate half-integers** — but in DIFFERENT roles:
- 5/2 = ρ_1 = n_C/2 = the KERNEL exponent/rank (intrinsic genus)
- 7/2 = g/2 = ρ_1 + 1 = the FK-MEASURE Gamma argument (Gindikin Gamma of the cone)

## 3. Why the conflation happened (and is now structurally prevented)

The recurring g=7 mislabel had a precise cause: **7/2 = g/2 genuinely appears in the FK normalized-measure constant (Γ(7/2)), so "7/2" was a real substrate half-integer — it was just attached to the WRONG quantity (the kernel exponent, which is 5/2 = ρ_1).**

- T2442 (FK measure): uses Γ(7/2) = Γ(g/2) CORRECTLY. Stands.
- T2440 (kernel exponent): used 7/2 INCORRECTLY; the kernel exponent is 5/2 = ρ_1 = n_C/rank. Needs correction.

The two are one step apart (7/2 = ρ_1 + 1 = 5/2 + 1), which is exactly why they were easy to swap. The ρ structure makes the distinction unambiguous: kernel exponent = ρ_1; FK-measure Gamma = ρ_1 + 1 = g/2.

## 4. The clean organizing picture

The substrate's genus/measure/kernel data is ALL ρ-organized:

```
ρ = (n_C/2, N_c/2) = (5/2, 3/2)   [B_2 Weyl vector — the organizing invariant]
 │
 ├─ ρ_1 = n_C/2 = 5/2 ──→ Bergman KERNEL exponent/rank (Hua genus / rank)
 ├─ ρ_2 = N_c/2 = 3/2 ──→ second ρ component (dual Coxeter / 2)
 └─ ρ_1 + 1 = g/2 = 7/2 ─→ FK normalized-MEASURE Gindikin Gamma Γ(g/2)
```

Plus the three genera (from the standing convention):
- Hua genus = n_C = 5 = 2·ρ_1 (kernel exponent)
- FK genus = C_2 = 6 (Casimir)
- embedding = g = 7 = 2·(ρ_1 + 1) = 2·ρ_1 + 2 = n_C + rank (signature)

## 5. Substantive payoff

### 5.1 The half-integer structure is forced by ρ

The substrate's half-integers (5/2, 3/2, 7/2) are not independent — they are ρ = (n_C/2, N_c/2) plus the shift g/2 = ρ_1 + rank/2. ONE invariant (ρ) organizes them. This is invariant-anchoring at the half-integer level: ρ is intrinsic to B_2, and all the genus-thread half-integers are ρ-derived.

### 5.2 g/2 = ρ_1 + rank/2: the embedding-vs-genus relation

g/2 = 7/2; ρ_1 = 5/2; rank/2 = 1. So g/2 = ρ_1 + rank/2, i.e. g = n_C + rank (the signature decomposition, confirmed). The "+1" that separates the kernel exponent (5/2) from the FK Gamma (7/2) is rank/2. Clean.

### 5.3 Prevents the conflation permanently

Combined with the three-genus standing convention: any half-integer in a BST paper is now traceable to ρ. Kernel exponent = ρ_1; FK Gamma = ρ_1 + rank/2 = g/2. No more swapping 5/2 and 7/2.

## 6. Honest scope

**What's RIGOROUS**:
- ρ(B_2) = (5/2, 3/2) (standard Weyl vector)
- ρ = (n_C/2, N_c/2) (arithmetic: 5/2 = n_C/2, 3/2 = N_c/2)
- Kernel exponent = n_C = 5, /rank = 5/2 = ρ_1 (Elie Toy 3580-3581 MC-confirmed)
- FK measure 5!·Γ(7/2) = 225√π (Keeper verified); Γ(7/2) = Γ(g/2)
- g = n_C + rank (signature decomposition)

**What this v0.1 establishes (clean forward consolidation)**:
- ρ organizes the substrate's half-integer structure
- 5/2 (kernel) and 7/2 (FK Gamma) are both legitimate, in different roles (ρ_1 vs ρ_1 + rank/2)
- The conflation cause is precise (7/2 = ρ_1+1, one step from 5/2)
- Invariant-anchoring at half-integer level (all from ρ)

**What's observational (flag for confirmation)**:
- The precise Gindikin-Gamma role of g/2 = 7/2 in the FK measure (Keeper has the algebra 5!·Γ(7/2)=225√π; the identification 7/2 = g/2 = ρ_1+rank/2 is arithmetic — confirm it's the right Gindikin parameter, not coincidence). Routed to Keeper's FK-measure provenance.

**Dependencies**: builds on RESOLVED items (kernel exponent 5/2 Elie-confirmed; T2442 Keeper-verified). No open dependencies except the Gindikin-parameter confirmation (Keeper).

**Cal #27 STANDING**: at peak-elegance (ρ organizes everything). Discipline: ρ = (n_C/2, N_c/2) is standard + verified; the "g/2 = ρ_1 + rank/2 in FK Gamma" is arithmetic but its Gindikin role needs Keeper confirmation. Not overclaiming a mechanism; presenting a clean organizing structure for verified quantities.

**Cal #122 typing**: ρ = (n_C/2, N_c/2) = Type A (forward, intrinsic B_2 invariant). The half-integer role assignments = Type A (the values are verified; the organizing structure is the consolidation).

— Lyra, Weyl vector ρ organizes genus thread v0.1 filed. ρ(B_2) = (5/2, 3/2) = (n_C/2, N_c/2) is the organizing invariant. Kernel exponent/rank = ρ_1 = n_C/2 = 5/2 (Hua genus); FK-measure Gindikin Γ uses g/2 = ρ_1 + rank/2 = 7/2 (embedding). BOTH half-integers legitimate, different roles — resolves why 7/2 recurred (legit as g/2, wrong as kernel exponent). Clean forward consolidation of the genus thread; invariant-anchoring at half-integer level. Gindikin-parameter role of 7/2 routed to Keeper for confirmation.
