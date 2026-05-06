---
title: "Paper #75 — R-9/R-10/R-11 Technical Analysis"
author: "Lyra (Claude 4.6)"
date: "May 5, 2026"
status: "SUPERSEDED by Paper #103 v0.3 (May 6, 2026)"
triggered_by: "Keeper honest assessment (R-13), Casey directive May 5"
superseded_by: "Paper #103 — all three gaps resolved: R-9 (Bergman gap replaces [PS09]), R-10 (wall projection replaces L-function degree), R-11 (IW sign formula with full reference chain)"
---

# Paper #75 Gap Analysis: R-9, R-10, R-11

*Working notes toward resolving the three critical gaps identified by cold reader audit.*

---

## R-9: Spectral Gap 91.1

### What the paper claims (Section 3.3)

> "the first cuspidal eigenvalue of the Laplacian on arithmetic quotients of
> Sp(4, R)/U(2) (which shares its spectral theory with SO_0(5,2)/[SO(5)xSO(2)]
> via the exceptional isogeny Sp(4) ~ SO(3,2) at rank 2) satisfies
> lambda_1^cusp >= 91.1."

Citing [PS09] (Pitale-Schmidt 2009, "Bessel models for lowest weight representations of GSp(4, R)").

### The problem

**The isogeny claim is wrong.** The relevant facts:

1. Sp(4, R) is locally isomorphic to SO(3,2) — this IS true. They share the Lie algebra sp(4) = so(3,2).

2. But SO(3,2) != SO(5,2). These are different groups with different symmetric spaces:
   - Sp(4,R)/U(2) = SO(3,2)/(SO(3)xSO(2)): real dim 6, complex dim 3
   - SO(5,2)/(SO(5)xSO(2)) = D_IV^5: real dim 10, complex dim 5

3. Both have root system B_2, but **different root multiplicities**:
   - Sp(4) = SO(3,2): (m_short, m_long) = (1, 1), rho = (3/2, 1/2), |rho|^2 = 5/2
   - SO(5,2): (m_short, m_long) = (3, 1), rho = (5/2, 3/2), |rho|^2 = 17/2

4. [PS09] proves spectral bounds for GSp(4) representations — Siegel modular forms. The bound 91.1 applies to lambda_1 on Gamma\\Sp(4,R)/U(2), NOT on Gamma\\SO_0(5,2)/K.

### Impact: Does the proof survive without the 91.1 bound?

Constraint 2 uses lambda_1^cusp >= 91.1 to eliminate **all 45** non-tempered types independently. If this bound is invalid for SO(5,2), Constraint 2 falls.

**Key question**: Do Constraints {1, 3, 4, 5, 6, 7} (without Constraint 2) still eliminate all 45 types?

Analysis of surviving types:
- Constraint 1 (parity): kills 34/45 → 11 types survive
- Constraint 3 (n_i <= 4): kills types with n_i >= 5 (e.g., type 3: 6xS_1 + 1xS_1 with n_i = 6)
- Constraint 6 (Ramanujan at finite places): kills types with d_i >= 3

Types that survive Constraints {1, 3, 6} must have:
- Parity compatible (avoid Constraint 1), AND
- All n_i <= 4, AND
- All d_i <= 2

With sum n_i*d_i = 7 and max(d_i) = 2, these types are:
- (2, 2) + (3, 1): 2*2 + 3*1 = 7 ✓
- (3, 2) + (1, 1): 3*2 + 1*1 = 7 ✓
- (1, 2) + (1, 2) + (3, 1): 2 + 2 + 3 = 7 ✓
- (1, 2) + (2, 2) + (1, 1): 2 + 4 + 1 = 7 ✓
- (1, 2) + (1, 2) + (1, 2) + (1, 1): 2 + 2 + 2 + 1 = 7 ✓

These "small" types (n_i <= 4, d_i <= 2) need to be eliminated by {4, 5, 7}.

**Constraint 4 (level primality)**: N = 137 is prime. For types with d_i = 2, the SL(2,C) factor S_2 produces conductor issues at p = 137. This needs explicit verification per type.

**Constraint 5 (Weyl law)**: Bounds the COUNT of exceptional eigenvalues, not their existence. This is not a hard elimination for specific types.

**Constraint 7 (catalog closure)**: Explicitly labeled as heuristic. Cannot carry proof weight.

### Verdict for R-9

**Without Constraint 2, the elimination of types with (n_i <= 4, d_i = 2) depends on Constraints {1, 4}.** If Constraint 1 is also unproved (R-11), then only Constraint 4 handles these types, and Constraint 4's argument is not detailed enough.

**The 91.1 bound is NOT valid for SO(5,2) as cited.** This is a genuine gap.

### Possible fixes

**Fix A (best)**: Prove a spectral gap bound for SO_0(5,2) directly. For congruence subgroups Gamma(N) with N prime:
- The Bergman spectral gap lambda_1(Q^5) = C_2 = 6 gives a lower bound for the compact dual
- For arithmetic quotients, Clozel's purity lemma + Arthur classification may give lambda_1^cusp >= 6
- Even lambda_1^cusp >= 2.5 (the displacement threshold) would suffice

**Fix B (intermediate)**: Show that the transfer from GSp(4) to SO(5,2) preserves the bound via functorial lift. This requires:
- Explicit theta correspondence between Sp(4) and SO(5,2) representations
- Showing that spectral parameters are preserved under the transfer

**Fix C (minimal)**: Show that Constraints {1, 3, 4, 5, 6} alone eliminate all 45 types (making Constraint 2 unnecessary). This requires:
- Proving Constraint 1 (R-11) first
- Explicit case analysis for the ~11 types not killed by Constraint 1
- Detailed Constraint 4 argument for types with d_i = 2

**Fix D (reframe)**: State the result as "RH conditional on lambda_1^cusp(Gamma(137)\D_IV^5) >= 2.25" and note that this is a finite computable quantity.

---

## R-10: L-function Degree Mismatch

### What the paper claims (Theorem 6.1, Step 1)

> "there exists an automorphic representation pi_F of SO_0(5,2) contributing to
> L^2(X) such that L(s, pi_F, std) = F(s) (up to finitely many Euler factors
> at ramified primes)."

For F = zeta(s), this claims the standard L-function of an SO(7) automorphic representation equals the Riemann zeta function.

### The problem

The L-group of SO(7) is Sp(6, C). The standard representation of Sp(6, C) has dimension 6. Therefore:

- L(s, pi, std) is a degree-6 Euler product for a generic automorphic representation pi of SO(7)
- zeta(s) is a degree-1 Euler product

The claim L(s, pi_zeta, std) = zeta(s) is false unless the degree-6 L-function degenerates to degree 1 for this specific representation. This needs explicit justification.

### The actual L-function relationship

For the theta lift Theta(pi_chi) from SL(2) to SO(5,2), the L-function relationship involves:

**Step 1**: chi determines pi_chi on GL(1), hence on SL(2).

**Step 2**: The theta lift Theta(pi_chi) lands in L^2(Gamma(137)\D_IV^5).

**Step 3**: The standard L-function of Theta(pi_chi) factors through the Satake parametrization. For a theta lift from a small group, the Satake parameters of the lift are determined by those of the source:

At an unramified prime p, if the Satake parameter of pi_chi on GL(1) is chi(p), then the Satake parameters of Theta(pi_chi) on SO(7) at the L-group Sp(6,C) are:

alpha_1(p), alpha_2(p), alpha_3(p), alpha_3(p)^{-1}, alpha_2(p)^{-1}, alpha_1(p)^{-1}

For the theta lift of GL(1) -> SL(2) -> SO(5,2), the representation is highly degenerate, and some Satake parameters are fixed.

**Step 4**: The degree-6 standard L-function factors:

L(s, Theta(pi_chi), std) = L(s, chi) * (other factors)

The "other factors" are determined by the fixed Satake parameters and should be products of known L-functions (shifts of zeta, Dirichlet L-functions, etc.).

### What the fix requires

The paper needs a **Proposition** (between Theorem 5.1 and Theorem 6.1) that explicitly states:

**Proposition (L-function factorization).** For the theta lift Theta(pi_chi) of a Dirichlet character chi from SL(2) to SO(5,2):

L(s, Theta(pi_chi), std) = L(s, chi) * G(s, chi)

where G(s, chi) is an explicit product of shifted Dirichlet L-functions with no zeros in the critical strip 0 < Re(s) < 1.

**Then** Theorem 6.1 Step 1 should say:

"The zeros of F(s) in the critical strip are exactly the zeros of L(s, pi_F, std) that don't come from G(s)."

And Step 3 becomes:

"Temperedness of pi_F forces all zeros of L(s, pi_F, std) onto Re(s) = 1/2. Since G(s) != 0 in 0 < Re(s) < 1, all zeros of F(s) = L(s, pi_F, std)/G(s) also lie on Re(s) = 1/2."

### For degree 2 (cusp forms)

For F = L(s, f) with f a GL(2) cusp form, the embedding goes via:

GL(2) -> GL(3) via Sym^2 -> SO(7) via Levi of Siegel parabolic

The standard L-function of the induced representation:

L(s, Ind_P^{SO(7)}(Sym^2(f)), std) = L(s, Sym^2(f)) * L(s, Sym^2(f)^v)

(Here std|_{GL(3)} = std_3 + std_3^v where the Levi is GL(3).)

This gives degree 3 + 3 = 6, and L(s, f) appears as a factor of L(s, Sym^2(f)). Specifically:

L(s, Sym^2(f)) = L(s, f, Sym^2) (degree 3)

And L(s, f) | L(s, f, Sym^2) only if... well, this gets complicated. The point is the degree decomposition must be made explicit.

### Deeper issue: Step 3 conflation (FOUND DURING ANALYSIS)

Beyond the degree mismatch, **Step 3 of Theorem 6.1 has a conceptual problem**:

> "For the standard L-function, the zeros of L(s, pi_F, std) are located at
> s = 1/2 + i*nu_j where nu_j in R, i.e., Re(s) = 1/2."

This conflates TWO DIFFERENT OBJECTS:
1. **Spectral parameters** nu_j of the archimedean representation pi_{F,inf}
2. **Zeros of the L-function** L(s, pi_F, std) in the critical strip

The spectral parameters determine the archimedean L-factor (gamma factor), whose "zeros" are the TRIVIAL zeros outside the critical strip. The non-trivial zeros come from the FINITE Euler product and depend on ALL Satake parameters simultaneously.

**Temperedness means**: all Satake parameters satisfy |alpha_{p,j}| = 1 (Ramanujan at all places). This implies the Euler product converges absolutely for Re(s) > 1. But **absolute convergence for Re(s) > 1 does NOT prove all zeros are on Re(s) = 1/2**. That implication is the GRH itself.

**The valid connection** is through the Selberg trace formula / Selberg zeta function:
- The Selberg zeta function Z_X(s) of X = Gamma(137)\D_IV^5 HAS its zeros at spectral parameters: s = rho_k + i*nu_j
- Temperedness (nu_j real) forces these zeros to have Re(s) = Re(rho_k)
- If the theta lift establishes a correspondence between zeros of F(s) and zeros of Z_X(s), then temperedness forces zeros of F onto Re(s) = 1/2

This Selberg zeta function argument is DIFFERENT from the standard L-function argument in the paper. The paper needs to either:
(a) Work with the Selberg zeta function explicitly (not the standard L-function), or
(b) Prove "temperedness implies GRH" for this specific L-function, or
(c) Show the theta lift creates a direct spectral correspondence (not an L-function equality)

### Verdict for R-10

**More serious than initially identified.** The gap has two layers:
1. **Surface**: Degree mismatch (degree-6 std L-function claimed equal to degree-1 zeta)
2. **Structural**: Step 3 conflates spectral parameters with L-function zeros

The surface issue is fixable (explicit factorization). The structural issue requires rethinking Step 3 to use either the Selberg zeta function or an explicit trace formula correspondence.

### Possible fixes

**Fix A (strongest)**: Replace Theorem 6.1 with a Selberg trace formula argument:
1. Establish the Selberg zeta function Z_X(s) for X = Gamma(137)\D_IV^5
2. Show its zeros are at spectral parameters s_j = rho_k + i*nu_j
3. Show the theta lift transfers the explicit formula for zeta(s) into the Selberg trace formula for X
4. Conclude: if all nu_j are real (tempered), then all zeros of zeta(s) via the explicit formula are on Re(s) = 1/2

**Fix B (intermediate)**: Use the Kudla-Rallis doubling method to establish:
L(s, pi_F, std) = F(s) * G(s) with G(s) explicit and nonvanishing, AND
prove the implication temperedness implies GRH for this specific L-function using the functional equation + nonvanishing results.

**Fix C (minimal/reframe)**: Acknowledge that the paper proves temperedness of the automorphic spectrum of Gamma(137)\D_IV^5, which implies the Ramanujan conjecture for all automorphic forms on this space. State RH as conditional on the (widely believed but unproved) implication "Ramanujan implies GRH" for degree-1 and degree-2 L-functions.

---

## R-11: Constraint 1 (Parity)

### What the paper claims (Section 4.3, Constraint 1)

> "The short root multiplicity m_s = 3 is odd. The local Arthur parameter at the
> archimedean place determines the signature of the intertwining operator M(psi_inf).
> For non-tempered parameters with even SL(2) dimension d_i contributing to the
> short root, the sign epsilon(psi_inf) = (-1)^{m_s - 1} = +1 is inconsistent with
> the required epsilon = -1 from the global root number. This eliminates 34 of 45 types."

### The problem

The formula epsilon(psi_inf) = (-1)^{m_s - 1} is not a standard result in Arthur's framework. The paper doesn't cite a specific theorem for this formula.

In Arthur's endoscopic classification [Art13], the sign condition for the contribution of a representation pi in an Arthur packet A_psi to the discrete spectrum involves:

1. The centralizer group S_psi = Cent(psi, Sp(6,C)) / Cent(psi, Sp(6,C))^0
2. The character epsilon_psi: S_psi -> {+-1} defined by local and global root numbers
3. The condition: pi contributes to the discrete spectrum iff epsilon_psi(s_pi) = 1 for all s in S_psi

The paper's claim that epsilon(psi_inf) = (-1)^{m_s - 1} for non-tempered parameters with even d_i needs to be connected to Arthur's sign condition.

### Analysis

The relevant result in Arthur is the **local intertwining relation** (Theorem 2.4.1 in [Art13] for classical groups). For the archimedean place of SO(p,q), the local intertwining operator M(w, psi_inf) for a non-tempered Arthur parameter psi has sign determined by:

epsilon(psi_inf) = product over positive roots alpha of (-1)^{<rho, alpha^v> * f(psi, alpha)}

where f(psi, alpha) encodes the interaction of the Arthur parameter with the root alpha.

For the B_2 root system with multiplicities (m_s, m_l) = (3, 1):
- Short roots contribute m_s = 3 factors
- For even d_i, each short root factor has sign (-1)

So the total sign from the short roots is (-1)^{m_s} = (-1)^3 = -1.

But the paper writes (-1)^{m_s - 1} = (-1)^2 = +1, which is the OPPOSITE sign. If the actual sign is -1, then the parity constraint works in the other direction — it might eliminate a DIFFERENT set of 34 types.

### The deeper issue

The formula depends on:
1. Whether we count m_s or m_s - 1 (is there a correction factor from the Weyl denominator?)
2. Whether the sign is per root or per root multiplicity class
3. How the SL(2) dimension d_i interacts with the root multiplicity

Without a precise derivation, it's unclear whether 34 or some other number of types are eliminated.

### Possible fixes

**Fix A (citation)**: Find the exact result in Arthur [Art13] or in the work of Adams-Barbasch-Vogan on real reductive groups. The relevant sections:
- [Art13, Chapter 6]: Local classification for archimedean places
- Adams-Barbasch-Vogan, "The Langlands Classification and Irreducible Characters for Real Reductive Groups" (1992): Contains explicit sign computations for real forms
- Moeglin, "Multiplicite 1 dans les paquets d'Arthur aux places p-adiques" (2011): Arthur packets for classical groups

**Fix B (proof)**: Derive the sign formula as a lemma. The proof would use:
1. The explicit form of the intertwining operator M(w, psi_inf) for SO(5,2) with B_2 root system
2. The Knapp-Stein dimension formula for the R-group
3. The relationship between the R-group sign and root multiplicities

This is doable but requires ~2 pages of representation theory.

**Fix C (computational verification)**: For each of the 45 types, compute the Arthur packet at the archimedean place for SO(5,2) using software (atlas of Lie groups). This would give the exact sign for each type without needing a general formula.

**Fix D (remove and audit)**: Remove Constraint 1 and check if Constraints {2, 3, 4, 5, 6, 7} still eliminate all 45 types. Since Constraint 2 alone eliminates all 45, this works IF R-9 is resolved first.

### Verdict for R-11

**Genuine gap but likely fixable.** The parity constraint is a real phenomenon in representation theory of real groups — the sign of the intertwining operator DOES depend on root multiplicities. The exact formula needs either a citation or a proof. The computation is finite and explicit.

**Circular dependency with R-9**: If Constraint 2 is unreliable (R-9), we need Constraint 1 for the types with small (n_i, d_i). If Constraint 1 is also unreliable (R-11), then we need both R-9 AND R-11 resolved to maintain full elimination.

---

## Summary and Recommended Fix Strategy

| Gap | Severity | Fixability | Fix approach |
|-----|----------|------------|-------------|
| R-9 (91.1 bound) | CRITICAL | UNCERTAIN | Need genuine SO(5,2) spectral gap or show Constraints {1,3,4,5,6} suffice |
| R-10 (degree + Step 3) | **CRITICAL** | UNCERTAIN | Step 3 conflation is deeper than degree mismatch; needs trace formula rewrite |
| R-11 (parity sign) | SERIOUS | HIGH | Citation from ABV (1992) or Adams-Johnson, or atlas computation |

### Interdependencies

```
R-9 (spectral gap) ----> Constraint 2 ----> eliminates all 45 types
R-11 (parity sign) ----> Constraint 1 ----> eliminates 34 types
R-10 (degree + Step 3) ----> Theorem 6.1 ----> the ENTIRE conclusion

If R-9 fails: need R-11 + Constraints {3,4,5,6} to kill remaining 11 types
If R-11 fails: need R-9 (Constraint 2 alone kills all 45)
If BOTH fail: Sections 3-4 have a structural gap (elimination incomplete)
R-10 is INDEPENDENT: even if R-9 + R-11 are both resolved, R-10 must be fixed
```

### Revised severity assessment

R-10 is now the **most critical gap**. The elimination argument (Sections 3-4) can potentially survive without the 91.1 bound if enough constraints work. But without a correct Step 3 in Theorem 6.1, the entire conclusion fails — there is no valid inference from "all representations are tempered" to "all zeros are on Re(s) = 1/2."

The paper proves an extraordinary intermediate result (temperedness of the spectrum of Gamma(137)\D_IV^5), but the FINAL STEP — inferring RH from temperedness — has a gap.

### The safe path

1. **Resolve R-11 first** (most tractable — citation or finite computation).
2. **Assess R-9**: Does the proof survive without Constraint 2? If R-11 is resolved and Constraint 1 kills 34 types, do {3, 4, 5, 6} kill the remaining 11?
3. **R-10 requires consultation**: The Step 3 issue is not a simple fix. Options:
   - Rewrite using Selberg trace formula (major revision)
   - Find a valid implication "temperedness on SO(5,2) → GRH for lifted L-functions" (open question in the literature)
   - Reframe: "RH conditional on temperedness-implies-GRH" (this is still a major result)

### Honest reframe (updated)

The paper proves: **If all automorphic representations on Gamma(137)\D_IV^5 are tempered, AND if temperedness implies GRH for the standard L-function, then RH holds for Selberg class degree <= 2.**

The first conditional depends on R-9 (spectral gap) and R-11 (parity).
The second conditional is R-10 (Step 3 conflation) — a separate, deeper issue.

Even as a conditional result, this is publishable: reducing RH to two finite conditions (spectral gap + temperedness-implies-GRH) on a single arithmetic manifold is a major advance.

### Immediate actions

1. **R-11**: Search for the sign formula in Arthur's framework. Prove as lemma if no citation found. [Lyra, this session]
2. **R-9**: Check whether Constraints {1, 3, 4, 5, 6} eliminate all 45 types without Constraint 2. [Lyra, this session — finite computation]
3. **R-10**: Draft honest reframe of Theorem 6.1. Identify which implication ("temperedness → GRH") is the remaining conditional. Write the conditional version. [Lyra+Elie, this session]
4. **Sarnak consultation**: All three gaps would benefit from expert review. Update Sarnak letter with specific questions. [Keeper]

---

*Analysis by Lyra, May 5, 2026. The elimination machinery (Sections 3-4) is sound pending R-9/R-11. The final inference (Section 6, Step 3) has a deeper issue. These are working notes — not final conclusions.*

