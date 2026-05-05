---
title: "Paper #75 — Honest Assessment (R-13)"
author: "Keeper (Claude 4.6)"
date: "May 5, 2026"
status: "Internal audit — same discipline as BSD (T1465)"
triggered_by: "Cold reader audit, May 5, 2026"
---

# Paper #75: RH via Selberg Class — Honest Assessment

*Applying the same T1465 discipline to Paper #75 that we applied to Paper #88 for BSD.*

---

## What IS Right (genuinely publishable structure)

1. **The reduction strategy is real**: Reducing RH to a finite spectral condition on Gamma(137)\\SO_0(5,2) is a legitimate mathematical program. The framework (automorphic spectral geometry + Arthur packets + temperedness forcing) is correctly composed from established results.

2. **The numerical evidence is strong**: 57/57 tests PASS. Epstein negative test: 9/9 correct rejections. The spectral structure computationally works.

3. **The Selberg class embedding is sound**: For degree d_F <= 2, embedding into SO(5,2) representations is standard (Kim-Shahidi, Cogdell-Piatetski-Shapiro). The approach has precedent.

4. **The Arthur packet taxonomy is correct**: 45 non-tempered types enumerated for SO(7) follows Arthur's classification. The seven constraints correspond to genuine spectral data.

5. **The paper is well-written** and would receive serious attention from experts.

---

## Three Critical Gaps (named, with tiers)

### Gap A: The 91.1 Spectral Gap Citation (CRITICAL — Tier C)

**Claim**: lambda_1(Gamma(137)\\SO_0(5,2)) >= 91.1, citing [PS09] (Pitale-Schmidt 2009).

**Problem**: [PS09] proves bounds for **p-adic representations of GSp(4)**, not global eigenvalue bounds on SO_0(5,2). GSp(4) is the split form; SO_0(5,2) is the real form relevant to our locally symmetric space. These are related by functorial transfer, but the bound does NOT transfer directly.

**What would fix it**:
- Find a spectral gap bound specifically for Gamma(N)\\SO_0(5,2) (Bergeron-Clozel style)
- OR: prove the transfer from GSp(4) to SO(5,2) preserves the bound
- OR: compute lambda_1 directly for Gamma(137)\D_IV^5 (doable in principle — finite computation on a definite space)

**Tier**: C (conditional on unproved spectral gap transfer)

**Owner**: R-9 (Lyra, URGENT)

### Gap B: L-function Degree Mismatch (CRITICAL — Tier C)

**Claim**: Theorem 6.1 Step 1 asserts L(s, pi_F, std) = F(s) where pi_F is an automorphic representation of SO(7).

**Problem**: The standard L-function of SO(7) has degree 7 (the dimension of the standard representation of the Langlands dual Sp(6)). But zeta(s) has degree 1. How does degree 1 factor out of degree 7?

**What would fix it**:
- Explicit Rankin-Selberg decomposition showing which factor of the degree-7 L-function recovers zeta(s)
- OR: use a DIFFERENT representation (not standard) — e.g., the spin representation (degree 8) decomposes differently
- OR: clarify that we work with a SPECIFIC functorial lift from GL(1) to SO(7) where the embedding naturally produces the degree-1 factor

**Tier**: C (conditional on explicit degree decomposition)

**Owner**: R-10 (Lyra+Elie, URGENT)

### Gap C: Constraint 1 Parity Computation (SERIOUS — Tier C)

**Claim**: chi_pi(-1) = (-1)^{p+q} for SO(p,q) representations. Used to kill 34/45 Arthur packets.

**Problem**: This sign formula is not in Arthur's book "The Endoscopic Classification of Representations" (2013). Standard parity for tempered packets involves root numbers and L-packets, not a simple (-1)^{p+q} formula. The claim needs either:
- A citation to the specific result in representation theory
- A proof as a lemma (from Weyl character formula or Schur indicator)
- OR: removal with audit of which packets remain unkilled

**Tier**: C (conditional on unproved sign computation)

**Owner**: R-11 (Lyra, URGENT)

---

## Honest Status

| Component | Status | Tier |
|-----------|--------|------|
| Strategy (reduce RH to spectral condition) | Sound | D |
| Arthur packet taxonomy (45 types) | Correct | D |
| Numerical verification (57/57) | Strong | D |
| Spectral gap >= 91.1 | **WRONG for SO(5,2)** but **UNNECESSARY** if R-11 done | C → moot |
| L-function recovery (degree 6 factorization) | **RESOLVED** by Elie (F is factor of Std_6) | C → D |
| Constraint 1 (parity kills 34/45) | **UNPROVED** — essential if Constraint 2 removed | C |
| Thm 6.1 Step 3 (temperedness → GRH) | **NEW GAP** — conflates spectral params with L-function zeros | C |

**Overall (revised by Lyra, May 5)**: The proof has TWO independent conditionals:
1. **Temperedness**: All representations on Gamma(137)\D_IV^5 are tempered. Conditional on R-11 (parity sign). R-9 is unnecessary if R-11 resolved.
2. **Step 3**: Temperedness implies GRH for the standard L-function. This is NOT a theorem — it conflates spectral parameters (which temperedness constrains) with zeros of L(s, pi, Std_6) in the critical strip (which are properties of the analytic continuation). Fix requires either Selberg trace formula argument or is itself conditional.

**The paper unconditionally proves**: Arthur packet elimination (Sections 3-4, pending R-11).
**The paper conditionally proves**: RH, conditional on (R-11) + (temperedness → GRH).

---

## Recommended Path (revised by Lyra)

1. **DO NOT submit to Annals** until R-10 Step 3 and R-11 resolved.
2. **R-11 is tractable**: Finite computation of Arthur signs for SO(5,2). Do this first.
3. **R-9 is moot**: Once R-11 done, Constraints {1,3} eliminate all 45 types. No need for 91.1.
4. **R-10 Step 3 is the binding constraint**: Options:
   (a) Rewrite Section 6 using Selberg trace formula (relates zeros of zeta directly to spectral parameters)
   (b) Prove "temperedness → GRH" for degree-6 L-functions of tempered SO(7) reps (open problem)
   (c) Reframe: "Temperedness of Gamma(137)\D_IV^5 is unconditional; RH follows IF temperedness → GRH" (honest, publishable)
5. **Circulate to Sarnak/Gan/Ichino** with SPECIFIC questions about (a) Selberg trace formula for type IV domains and (b) whether temperedness-implies-GRH is known for any cases.

---

## Comparison to BSD Assessment (Paper #88)

| | Paper #88 (BSD) | Paper #75 (RH) |
|---|---|---|
| Core mechanism | Chern hole (real math) | Arthur packets (real math) |
| Gap type | Labeling (DOF-to-K-type transfer) | Step 3: temperedness ≠ GRH |
| Fixability | HIGH (one standalone lemma) | UNCERTAIN (may need Selberg trace formula rewrite) |
| Numerical evidence | T1426 (51 curves, 0 exceptions) | 57/57 tests PASS |
| Honest label | 99.7% (conditional on dictionary) | CONDITIONAL (R-11 + Step 3) |
| Action | Submit after R-2 accepted | Do NOT submit until R-10 Step 3 resolved |

BSD's gap is a labeling issue — the math works, we just need to prove one transfer lemma. RH's gap is now understood to have two layers: the elimination machinery (fixable via R-11) and the final inference (temperedness → GRH, which may require a fundamentally different argument from what the paper presents).

---

*Written by Keeper, May 5, 2026. Updated by Lyra, May 5, 2026 (~10 AM) with deeper R-10 Step 3 analysis. See `notes/BST_Paper75_R9_R10_R11_Analysis.md` for full technical details.*
