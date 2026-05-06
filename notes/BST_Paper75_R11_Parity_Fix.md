---
title: "R-11 Analysis: Constraint 1 Parity — Status and Fix Path"
author: "Lyra (Claude 4.6)"
date: "May 5, 2026"
status: "SUPERSEDED by Paper #103 v0.3 (May 6, 2026)"
resolves: "R-11 (Constraint 1 justification, URGENT)"
paper: 75
superseded_by: "Paper #103 Section 2 — IW sign formula with full reference chain replaces Constraint 1"
---

# R-11: Constraint 1 — Parity Analysis

## 1. The Problem

Paper #75 Section 4.3, Constraint 1 states:

> "The short root multiplicity m_s = 3 is odd. The local Arthur parameter at the
> archimedean place determines the signature of the intertwining operator M(psi_inf).
> For non-tempered parameters with even SL(2) dimension d_i contributing to the
> short root, the sign epsilon(psi_inf) = (-1)^{m_s - 1} = +1 is inconsistent with
> the required epsilon = -1 from the global root number. This eliminates 34 of 45 types."

**Problems:**
1. The formula epsilon(psi_inf) = (-1)^{m_s - 1} has no citation
2. It doesn't appear in Arthur [Art13]
3. The phrase "contributing to the short root" is vague
4. The "required epsilon = -1 from the global root number" is not derived

## 2. What the Constraint Should Be

Constraint 1 should be one of the following established results:

### Option A: The Adams-Johnson Inner Form Condition

For the inner form SO(5,2) of the quasisplit SO(7), the local archimedean A-packet A_psi(SO(5,2)) may be empty for certain non-tempered parameters. The Adams-Johnson theorem [AJ87] classifies which Arthur parameters have nonempty local packets at each real form.

The condition involves the interaction between the SL(2) factors S_{d_i} and the signature (5,2) of the real form. Specifically, the Hodge decomposition of the parameter must be compatible with the compact/noncompact structure of SO(5,2).

**Status**: This IS a rigorous and established result. But the exact count of excluded types for SO(5,2) with sum n_i d_i = 7 requires explicit computation (45 cases). I have NOT completed this computation.

**Citation**: Adams-Johnson, "Endoscopic groups and packets of nontempered representations," Compositio Math. 64 (1987), 271-309.

### Option B: Arthur's Epsilon Sign Condition

Arthur [Art13, Theorem 1.5.1] defines the character epsilon_psi on the centralizer S_psi. A representation pi in the A-packet contributes to the discrete spectrum only if epsilon_psi(s_pi) = 1 for specific elements s in S_psi.

For the inner form SO(5,2), there is an additional Kottwitz sign:

e(SO(5,2)) = (-1)^{q(q-1)/2} = (-1)^{2*1/2} = -1

The condition becomes: epsilon_psi * e(G) = 1, i.e., epsilon_psi = -1 for SO(5,2).

For non-tempered parameters, the epsilon character depends on:
- Local root numbers epsilon(1/2, mu_i x mu_j) at each place
- The SL(2) dimensions d_i (which affect the sign through the L-function functional equation)

**Status**: This IS the correct framework, but computing epsilon_psi for each of the 45 types requires evaluating root numbers at the archimedean place. This is doable but involves the Langlands-Shahidi method and is ~2 pages per type (or automatable via Atlas software).

**Citation**: Arthur [Art13], Theorem 1.5.1 and Chapter 6.

### Option C: Computational Verification via Atlas

The Atlas of Lie Groups project (atlas.math.umd.edu, Adams-Vogan et al.) can compute Arthur packets for specific real forms. For SO(5,2):

```
atlas> set G = SO(5,2)
atlas> for each Arthur parameter psi with sum n_i d_i = 7:
atlas>   compute A_psi(G)
atlas>   check if A_psi contains discrete series
```

This would give the EXACT count of excluded types.

**Status**: Requires running the Atlas software. Cannot be done from first principles in a CI session.

## 3. Discrepancy: 34/45 vs Table

The paper's Appendix A table shows Constraint 1 in the "Killed by" column for ALL types except Type 3 (which suggests 44/45 killed, not 34/45). But the text says "34 of 45."

Possible resolutions:
1. The table's compressed entries (types 9-45) include individual types not killed by Constraint 1, but the group listing only shows the most common constraints
2. The 34/45 count in the text is correct and the table is misleading
3. The 34/45 count is wrong

This discrepancy must be resolved. If 44/45 types are killed by Constraint 1 (as the table suggests), then combined with Constraint 3 killing Type 3 (n_i = 6 > 4), ALL 45 types are eliminated without Constraint 2. This would make R-9 completely moot.

## 4. Why R-11 is Essential

If R-9 (spectral gap) is dropped (because the 91.1 bound is wrong for SO(5,2)):
- Without Constraint 1 AND without Constraint 2: types with (n_i <= 4, d_i = 2) survive all remaining constraints {3, 4, 5, 6, 7}
- These d_i = 2 types are NOT killed by Constraint 6 (Ramanujan at finite places — the depth (d-1)/2 = 1/2 matches the trivial bound)
- They're not killed by Constraint 3 (n_i <= 4)
- Constraints 4, 5, 7 don't give hard eliminations

So WITHOUT Constraints {1, 2}: the proof fails for types with small (n_i, d_i).
WITH Constraint 1 but without 2: the proof works (R-9 is moot).

**Bottom line: R-11 is the ESSENTIAL fix for the elimination argument.**

## 5. Recommended Path

1. **Immediate**: Replace the ad hoc formula with a citation to Adams-Johnson [AJ87] and Arthur [Art13, Theorem 1.5.1]. State: "By the Adams-Johnson inner form condition and Arthur's epsilon character, the non-tempered types compatible with the inner form SO(5,2) are restricted to those whose SL(2) parameters are (p,q)-compatible and whose epsilon characters match the Kottwitz sign e(SO(5,2)) = -1."

2. **Verification**: Run the Atlas of Lie Groups software to compute the exact count of excluded types. This is a finite computation (45 cases for a fixed real form).

3. **Fallback**: If the Atlas computation shows Constraint 1 kills FEWER than 34 types, check whether the remaining types are killed by Constraints {3, 5, 6}. If not, the paper needs Constraint 2 (R-9) after all.

4. **Sarnak question**: Ask Sarnak specifically: "For the inner form SO_0(5,2) of the quasisplit SO(7), what fraction of the 45 non-tempered Arthur types (sum n_i d_i = 7) contribute to the discrete spectrum? We claim 'at most 11 of 45' — is this consistent with the Adams-Johnson classification?"

## 6. Draft Replacement Text for Paper #75

**Replace** the current Constraint 1 paragraph with:

> **Constraint 1 (Inner form restriction).** The real form SO_0(5,2) is an inner form of the quasisplit SO(7), with Witt index q = 2 and Kottwitz sign e(G) = (-1)^{q(q-1)/2} = -1. By Adams-Johnson [AJ87] and Arthur [Art13, Theorem 1.5.1], a non-tempered Arthur parameter psi contributes to the discrete spectrum of SO(5,2) only if:
>
> (i) The local A-packet A_{psi_inf}(SO(5,2)) at the archimedean place is nonempty (Adams-Johnson compatibility: the SL(2) parameters {d_i} must be compatible with the signature (5,2)), and
>
> (ii) The global epsilon character satisfies epsilon_psi = e(G) = -1 (Arthur's sign condition).
>
> Condition (i) excludes parameters whose SL(2) components are too large for the noncompact dimension q = 2 (e.g., S_7, which requires q >= 4). Condition (ii) imposes a parity constraint depending on the root numbers of the GL components {mu_i}. Together, these eliminate **[N] of 45** non-tempered types. [N to be verified by Atlas computation.]

---

*Lyra, May 5, 2026. R-11 analysis. The fix is tractable (correct citations + finite computation) but requires either Atlas software or expert verification for the exact count.*
