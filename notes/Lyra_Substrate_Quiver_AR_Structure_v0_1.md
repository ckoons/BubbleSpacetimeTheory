---
title: "Substrate quiver Auslander-Reiten structure v0.1"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-27 Wednesday EDT (~10:12 EDT actual via Casey FYI)"
status: "v0.1 FRAMEWORK. AR-quiver for substrate's Z_2-graded super-quiver. Multi-week math direction. AR-translation τ candidate = Möbius involution σ; almost-split sequences."
related: ["Multi-phase quiver v0.2 + v0.3", "A_sub v0.9 super-quiver", "Standard Auslander-Reiten 1974 theory"]
---

# Substrate quiver AR structure v0.1

## 1. Auslander-Reiten quiver background

For a finite-dimensional algebra A (or quiver Q with relations R), the **Auslander-Reiten quiver Γ_A** is a directed graph whose vertices are isomorphism classes of indecomposable A-modules and whose arrows are irreducible morphisms.

Standard structure:
- **AR-translation τ**: takes indecomposable non-projective module M to its translate τM
- **Almost-split sequences**: short exact sequences 0 → τM → E → M → 0
- **Mesh structure**: AR-quiver has mesh structure where translation connects parallel arrows

## 2. Substrate AR-quiver candidate

For substrate's multi-phase super-quiver Q with relation ideal R (Cal #132 SVC backbone):

### 2.1 AR-translation τ candidate

**Substrate-natural candidate**: τ = **Möbius involution σ** on D_IV⁵.

Per A_sub step 1 + step 5: P̂_op = γ̂⁵ ∘ σ where σ flips m_2 sign on Wallach K-types. This is structurally analogous to AR-translation taking module M to "twisted" τM.

Verification (multi-week): does σ acting on Wallach K-type representations satisfy AR-translation axioms?

### 2.2 Almost-split sequences

Substrate-natural candidates: substrate's "minimum-action transitions" between K-types via SWPP commitment cycle.

For each non-projective K-type V_K: almost-split sequence 0 → σ V_K → E_K → V_K → 0 where E_K is the substrate-natural "middle term" (substrate's commitment cycle intermediate state).

Verification (multi-week): explicit middle terms E_K computation.

### 2.3 Mesh structure

For substrate's tame quiver type: AR-quiver has tame mesh structure (one-parameter families of indecomposables per dimension).

For substrate's wild quiver type: AR-quiver has wild structure (multi-parameter families).

Substrate type determination: multi-week verification per multi-phase quiver v0.3 Gröbner basis output.

## 3. Connection to chain forcing

Per Cal #139 cyclotomic chain forcing (4 instances) + Grace 6-instance extension:
- Chain forcing arithmetic structure may MIRROR AR-quiver structure
- Each chain level → AR-component
- Mersenne-cyclotomic forcing → AR-translation structure

Substantive structural reading (FRAMEWORK pending verification): substrate's chain forcing IS the AR-quiver's translation structure restricted to substrate-natural K-types.

## 4. Multi-week derivation path

- v0.2: explicit τ = σ verification at small K-types
- v0.3: almost-split sequences explicit construction
- v0.4: AR-quiver structure type determination (tame vs wild)
- v0.5: connection to chain forcing structural verification

## 5. Honest scope

**What's RATIFIED**:
- Standard Auslander-Reiten 1974+ theory
- A_sub v0.9 super-quiver structure (Cal #132 SVC backbone)
- Möbius involution σ in P̂_op per step 1 + step 5

**What's FRAMEWORK in v0.1**:
- τ = σ AR-translation candidate
- Almost-split sequences via substrate commitment cycle
- AR-quiver type determination as multi-week verification

**Cal #29 STANDING audit pass**: structural candidate from standard AR theory; not back-fittable; multi-week verification.

— Lyra, substrate quiver AR structure v0.1 filed Wednesday 2026-05-27 ~10:12 EDT (actual time per Casey FYI; my doc timestamps drifted +50min). FRAMEWORK. Multi-week derivation per AR-quiver verification stage.
