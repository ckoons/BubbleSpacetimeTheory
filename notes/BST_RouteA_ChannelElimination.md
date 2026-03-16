# Route A: Channel Elimination and the Trace Formula

**Casey Koons & Lyra (Claude Opus 4.6)**
**March 17, 2026**

**Status:** Route A investigation COMPLETE. Four channels eliminated, one standing.

---

## 1. Context

The rank-2 coupling proof of the Riemann Hypothesis (v3, Toys 206-207) was
**withdrawn** after Elie's gap analysis (Toy 213) showed the overconstrained
system mechanism is vacuous: the deepest pole never fires (Re > 1 always),
and shallower poles give no contradiction. The proof was tautological — Route B
(identities that hold regardless of zero location).

This note documents **Route A**: the systematic search for inequality-based
arguments where BST's geometry genuinely constrains ξ-zero locations.

## 2. The Five Channels Tested

Starting from the landscape survey (Toy 214), five potential channels were
identified where the Riemann zeta function could interact with the spectral
theory of D_IV^5 = SO₀(5,2)/[SO(5) × SO(2)]:

| # | Channel | Toy | Mechanism | Status |
|---|---------|-----|-----------|--------|
| 1 | Pure Plancherel | 214 | \|c(λ)\|⁻² positivity on G/K | **DEAD** |
| 2 | Arithmetic lattice / Arthur | 215-216 | Residual spectrum from ξ-poles | **DEAD** |
| 3 | Period integrals | 217 | SO₀(4,2)\SO₀(5,2) unfolding | **DEAD** |
| 4 | Trace formula | 218 | Selberg trace for Γ\G | **STANDING** |
| 5 | Tautological identities | 213 | M(s)·M(−s) = 1 | **DEAD** (Route B) |

Each elimination was earned by explicit computation, not assumption.

## 3. Channel 1: Pure Plancherel (Toy 214) — ELIMINATED

**Idea:** The Plancherel measure |c(λ)|⁻² on G/K is manifestly positive.
Since c(λ) involves ξ-functions, perhaps positivity constrains zeros.

**Finding:** The Plancherel measure on G/K (no lattice) is:

$$|c(\lambda)|^{-2} = \prod_{\alpha \in \Sigma^+} |c_\alpha(\langle \lambda, \alpha^\vee \rangle)|^{-2}$$

Each c_α involves only **Gamma functions** (via Gindikin-Karpelevič), not ξ.
The ξ-functions enter only through the **intertwining operators** M(w,s),
which appear on the arithmetic quotient Γ\G, not on G/K itself.

**Conclusion:** Pure Plancherel has no ξ content. The constraint lives in
the lattice, not the space.

## 4. Channel 2: Arthur Obstruction (Toys 215-216) — ELIMINATED

**Idea:** An off-line ξ-zero ρ = 1/2 + δ + iγ creates poles in M(w,s) at
complex values s₀. If these poles generate L² residues, Arthur's classification
(which enumerates all residual spectrum for classical groups) might forbid them.

**Finding (Toy 215):** The arithmetic lattice Γ = SO(Q,ℤ) for the form
Q = x₁² + ··· + x₅² − x₆² − x₇² gives a cofinite quotient with cusps.
Eisenstein series exist, and the trace formula applies.

**Finding (Toy 216):** For a hypothetical off-line zero at ρ = 0.6 + 14.134i,
the extra poles at complex s₀ have **growing Weyl terms**:

For all w ≠ e in W(B₂):

$$\text{Re}\langle ws_0 + \rho, H \rangle > 0$$

This means the residue **grows** in the cusp direction → not L² → not in the
discrete spectrum → Arthur classification never sees it. The extra poles are
absorbed into the continuous spectrum, exactly as in rank 1.

**Correction:** Toy 215's claim of "pole-on-pole amplification" was incorrect.
Each ξ-zero creates 3 **simple** poles (order 1), not higher-order poles.

**Conclusion:** The Arthur obstruction doesn't fire. Extra poles from off-line
zeros live in the continuous spectrum where Arthur has nothing to say.

## 5. Channel 3: Period Integrals (Toy 217) — ELIMINATED

**Idea:** The symmetric pair (G,H) = (SO₀(5,2), SO₀(4,2)) embeds AdS inside
BST. The period integral

$$P(s) = \int_{H \backslash G} E(g, s)\, dg$$

unfolds to a ratio of ξ-functions (Jacquet). If ξ-zeros appear in the
numerator at physical evaluation points, non-vanishing of the period constrains
zero locations.

**Finding:** The period integral evaluates to:

$$P(s_1, s_2) \sim \frac{\xi(2s_1 - 2) \cdot \xi(2s_2 - 2)}{\xi(2s_1 + 3) \cdot \xi(2s_2 + 3)}$$

On the unitary axis s = ρ + iv (where ρ = (5/2, 3/2)):

| Factor | Argument | Re part | Location |
|--------|----------|---------|----------|
| ξ(2s₁ − 2) | 3 + 2iv₁ | 3 | Outside strip |
| ξ(2s₂ − 2) | 1 + 2iv₂ | 1 | Strip boundary |
| ξ(2s₁ + 3) | 8 + 2iv₁ | 8 | Outside strip |
| ξ(2s₂ + 3) | 6 + 2iv₂ | 6 | Outside strip |

All ξ-arguments have Re ≥ 1 on the unitary axis. The boundary value ξ(1 + 2iv₂)
has no zeros (prime number theorem). Off-axis at σ₂ = −1/4, the argument
reaches Re = 1/2 — but this is off the physical evaluation axis.

**Conclusion:** Period integrals don't directly constrain ξ-zeros on-axis.
The m_s difference between BST and AdS (3 vs 2) shifts the ξ-arguments
further from the strip, not closer.

## 6. Channel 4: Trace Formula (Toy 218) — STANDING

**This is the only surviving channel.**

### 6.1 The Framework

The Arthur-Selberg trace formula for Γ\SO₀(5,2) equates:

**Spectral side:**
$$\sum_{\pi\, \text{discrete}} m(\pi)\, \hat{h}(\lambda_\pi) + \frac{1}{|W|} \int_{i\mathfrak{a}^*} \hat{h}(i\nu)\, |c(i\nu)|^{-2}\, d\nu - \frac{1}{4\pi} \int \hat{h}(i\nu)\, \frac{\varphi'}{\varphi}(i\nu)\, d\nu$$

**Geometric side:**
$$\text{vol}(\Gamma \backslash G) \cdot \hat{h}(\rho) + \sum_{[\gamma]\, \text{hyperbolic}} \text{vol}(\Gamma_\gamma \backslash G_\gamma) \cdot O_\gamma(h) + \cdots$$

The geometric side is **computable** and **ξ-independent**.

### 6.2 How ξ-Zeros Enter

The scattering contribution involves φ'/φ(s), where φ(s) = det M(w₀,s).
The log-derivative φ'/φ involves ξ'/ξ at arguments that, on the unitary axis,
have Re ≥ 3 — safely outside the strip.

**But:** by contour deformation from Re(s) = ρ toward Re(s) = 0, we cross
the **poles** of ξ'/ξ. Each ξ-zero ρ_zero creates poles at:

$$s_1 = \frac{\rho_{\text{zero}} + j}{2}, \quad j = 0, 1, \ldots, m_s - 1$$

For m_s = 3 (BST): poles at Re(s₁) = 1/4, 3/4, 5/4 — all **crossed**
during deformation. The denominator poles have Re(s₁) < 0 and are not crossed.

### 6.3 The 6× Advantage

Each ξ-zero contributes at **3 shifted evaluation points** per short root.
With 2 short roots (2e₁, 2e₂), the total is:

**6 constraints per zero.**

| Space | m_s | Shifts/root | Total constraints/zero |
|-------|-----|-------------|----------------------|
| SL(2,ℝ), rank 1 | — | 1 | 1 |
| SO₀(3,2), rank 2 | 1 | 1 × 2 | 2 |
| SO₀(4,2), rank 2 | 2 | 2 × 2 | 4 |
| SO₀(5,2), rank 2 | 3 | 3 × 2 | **6** |

BST gives 6× the information per zero compared to the classical rank-1
trace formula. This is the quantitative advantage of m_s = N_c = 3.

### 6.4 Test Functions and Zero Contributions

The resolvent test function $\hat{h}(s_1, s_2) = (s_1^2 + s_2^2 + A)^{-k}$
gives convergent zero sums. For the first ξ-zero (γ ≈ 14.13):

| j | Z_j(ρ₁) | Re(s₁) crossed |
|---|----------|----------------|
| 0 | 3.89 × 10⁻⁷ | 1/4 |
| 1 | 3.61 × 10⁻⁷ | 3/4 |
| 2 | 3.14 × 10⁻⁷ | 5/4 |

The three contributions are of comparable magnitude — the shifts are
**not redundant**. Off-line displacement (δ > 0) changes the magnitudes
by ~5–10% but does not flip signs for the resolvent. The sign question
requires deeper analysis with optimized test functions.

### 6.5 The Spectral Gap Constraint

BST gives λ₁ = C₂ = 6 with multiplicity d₁ = 7. The continuous spectrum
starts at |ρ|² = 17/2. The trace formula then requires:

$$\sum_\rho Z(\rho) = \text{vol}(\Gamma \backslash G) \cdot \hat{h}(\rho) - 7 \cdot \hat{h}(\sqrt{6}) - (\text{other discrete}) - (\text{boundary})$$

The right side is a **computable constant** (for fixed h). The spectral gap
provides a **floor** on the discrete contribution, constraining how large
the zero sum can be.

### 6.6 What Remains

Three steps to complete the program:

1. **Compute the geometric side explicitly.** The volume vol(Γ\G) for
   Γ = SO(Q,ℤ) involves Gauss-Bonnet and special zeta values. The orbital
   integrals for hyperbolic conjugacy classes require the Harish-Chandra
   integral formula. Both are computable in principle.

2. **Find the optimal test function.** The trace formula gives different
   information for different h. The right h must satisfy:
   - K-biinvariance on G
   - Rapid decay (convergence of all sums)
   - Discriminating power: Z(ρ_on) vs Z(ρ_off) have different signs
     or magnitudes that are inconsistent with the geometric bound

3. **Prove the definite sign criterion.** Show that for the optimal h,
   the trace formula is inconsistent with off-line zeros. This is the
   rank-2 analog of Li's criterion, where the 6 constraints per zero
   and the 2-parameter test function family provide the leverage that
   rank 1 lacks.

## 7. The Quaker Assessment

Five channels tested. Four eliminated honestly:

- Pure Plancherel: no ξ content (the wrong space)
- Arthur obstruction: doesn't fire (poles not L²)
- Period integrals: ξ outside strip on-axis (the wrong evaluation)
- Tautological identities: Route B (the wrong type of argument)

One channel standing:

- **Trace formula:** the only place where ξ-zeros inside the critical strip
  meet a computable, ξ-independent geometric bound. BST's m_s = 3 gives it
  6 constraints per zero. The spectral gap λ₁ = 6 provides a floor. The
  2-parameter test function family provides flexibility.

This is genuine mathematics — a research program, not a closed proof.
The geometry of D_IV^5 speaks through the trace formula.
And m_s = 3 gives it the loudest voice.

## 8. Relation to Existing Work

- **Koons-Claude Conjecture** (Toys 208-210): Survives independently.
  The conjecture that D_IV^5 uniquely derives physics + proves RH + explains
  GUE does not depend on any specific proof mechanism. GUE from SO(2),
  AdS failure, and Plancherel=primes are established results.

- **Rank-2 coupling paper** (BST_RiemannProof_Rank2Coupling.md): **Withdrawn.**
  The overconstrained system mechanism is vacuous (Toy 213).

- **From Winding to Zeta** (BST_WindingToZeta_AutomorphicStructure.md):
  The automorphic structure (WZW, Verlinde, Langlands) remains valid.
  The trace formula is the natural endpoint of that chain.

---

*Toys 213-218. Each elimination sharpened where the truth lives.*
*The trace formula is the Fourier transform. Spectral = geometric.*
*The geometry of BST is the source of all power.*
*But the power flows through the trace formula.*
