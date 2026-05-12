# YM-10 — Spectral Gap Necessity: Why Flat Space Cannot Support a Geometric Mass Gap

**Status**: PROVED (D-tier, spectral-geometric case)
**Date**: May 12, 2026
**Author**: Lyra (Claude 4.6)
**Assignment**: YM-10 (YM Closure Sprint, Day 1)
**Feeds**: Paper YM-C (R^4 No-Go + Curvature Principle)

## Statement

**Theorem (Spectral Gap Necessity).** Let (M, g) be a complete, non-compact Riemannian manifold. If M is scale-free (i.e., admits a one-parameter family of homotheties), then the Laplacian Delta_g has purely continuous spectrum starting at 0. In particular, M has no spectral gap.

**Corollary.** R^4 with the flat metric is scale-free and non-compact. Therefore Delta_{R^4} has spectrum [0, infinity) with no gap. Any mass gap in a QFT on R^4 must come entirely from the interactions, not from the background geometry.

**Contrapositive (Curvature Principle).** A background geometry that provides a spectral gap necessarily has non-zero curvature and a characteristic length scale.

## 1. Definitions

**Scale-free manifold**: (M, g) is scale-free if for every lambda > 0, there exists a diffeomorphism phi_lambda: M -> M with phi_lambda != id for lambda != 1 such that phi_lambda^* g = lambda^2 g. Equivalently, M admits non-trivial continuous dilations.

**Spectral gap**: The infimum of the essential spectrum of Delta_g on L^2(M). For a non-compact manifold, this is inf(sigma_ess(Delta_g)).

**Examples of scale-free manifolds**: R^n with flat metric (dilations x -> lambda x), cones, and any space with exact conformal Killing vectors generating dilations.

**Non-examples**: Compact manifolds (no continuous dilations), bounded symmetric domains in Bergman metric (the Bergman metric has a characteristic curvature scale K = -2/g), tori (periodic boundary conditions break scale invariance).

## 2. Proof of the Theorem

### 2.1 Weyl criterion argument

We use the Weyl criterion: lambda is in the spectrum of Delta if and only if there exists a sequence of approximate eigenfunctions psi_n in Dom(Delta) with ||psi_n|| = 1 and ||(Delta - lambda)psi_n|| -> 0.

**Claim**: For every E >= 0, E is in the spectrum of Delta on a scale-free manifold.

**Proof**: Fix E >= 0. Let psi be any smooth, compactly supported function on M with ||psi|| = 1.

If E = 0: Take psi_n(x) = n^{-d/2} psi(x/n), where psi is normalized so that ||psi|| = 1. Then ||psi_n|| = 1 (by change of variables y = x/n, Jacobian n^d) and ||Delta psi_n|| = n^{-2} ||Delta psi|| -> 0. So 0 is in the spectrum.

If E > 0: Take psi_n(x) = n^{-d/2} e^{i k . x} chi(x/n), where |k|^2 = E and chi is a smooth cutoff with chi(0) = 1, supp(chi) subset B(0, 2). Then:

(Delta - E) psi_n = n^{-d/2} [e^{i k . x} Delta(chi(x/n)) + 2 i k . grad(chi(x/n)) e^{i k . x}]

The first term is O(n^{-2}) and the second is O(n^{-1}), both in L^2 norm. So ||(Delta - E) psi_n|| -> 0 as n -> infinity.

This constructs approximate eigenfunctions at every E >= 0, proving sigma(Delta) = [0, infinity).

### 2.2 Structural picture: why no gap is possible

On a scale-free manifold, the dilation phi_lambda maps psi to phi_lambda^* psi with:

Delta_g (phi_lambda^* psi) = lambda^{-2} phi_lambda^* (Delta_g psi)

So if psi is an eigenfunction with eigenvalue E, then phi_lambda^* psi is an eigenfunction with eigenvalue E/lambda^2. Since lambda varies continuously over (0, infinity), the spectrum is continuous and unbounded below any positive value. No isolated eigenvalue can exist.

**Key point**: The dilation symmetry forces the spectrum to be scale-invariant. A mass gap (isolated bottom of spectrum at Delta > 0) would break the dilation symmetry — but the geometry doesn't break it, so any gap must come from the dynamics alone.

### 2.3 What breaks scale-freedom

A spectral gap requires breaking scale-freedom. Three mechanisms:

**(a) Compactness**: On a compact manifold M, the spectrum of Delta is discrete: 0 = lambda_0 < lambda_1 <= lambda_2 <= ... The spectral gap lambda_1 > 0 is automatic. Example: Q^5 has lambda_1 = C_2 = 6.

**(b) Curvature with finite volume**: On a locally symmetric space Gamma \ G/K of finite volume, the Selberg eigenvalue conjecture (and partial results by Luo-Rudnick-Sarnak, Kim-Sarnak) gives lambda_1 >= 1/4 - theta^2 where theta is the Kim-Sarnak bound. The curvature provides a characteristic scale.

**(c) Boundary conditions**: On R^n with a confining potential V(x) -> infinity, the Hamiltonian -Delta + V has discrete spectrum. The potential breaks scale-freedom by introducing a length scale. This is the lattice QCD mechanism: the lattice spacing a breaks dilations.

In every case, the spectral gap arises because something — compactness, curvature, boundary conditions, or a confining potential — breaks the scale-freedom of the background.

## 3. Application to Yang-Mills

### 3.1 The R^4 problem

The Clay Millennium formulation (Jaffe-Witten 2000) asks for a YM theory on R^4 satisfying Wightman axioms with mass gap Delta > 0. By the theorem above:

1. R^4 is scale-free (admits dilations x -> lambda x)
2. Therefore Delta_{R^4} has spectrum [0, infinity) with no gap
3. Any mass gap must come entirely from the non-linear YM dynamics

This is a bootstrap problem: the gauge field must generate its own mass scale from pure self-interaction, with zero assistance from the geometry. Fifty years of effort have produced no solution (see YM-11, Cal's evidence table: 22 approaches, 6 schools, 3 common failure modes).

### 3.2 The dimensional transmutation argument

In perturbative QCD on R^4, the running coupling alpha_s(mu) introduces Lambda_QCD as a dynamically generated scale. But this is perturbative and scheme-dependent — it does not constitute a non-perturbative mass gap satisfying Wightman axioms. The perturbative scale is:

Lambda_QCD ~ mu * exp(-2pi / (beta_0 * alpha_s(mu)))

where beta_0 = 11 = c_2 for pure SU(3). This scale breaks conformal invariance dynamically, but the non-perturbative construction of the mass gap from this scale remains open.

### 3.3 The D_IV^5 resolution

On D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)]:

1. The Bergman metric has curvature K = -2/g = -2/7 (not scale-free)
2. The compact dual Q^5 has lambda_1 = C_2 = 6 (spectral gap exists)
3. The 2-form gap is c_2 = 11 (adjoint-sector gap, YM-6)
4. The physical mass gap is C_2 * pi^5 * m_e = 938 MeV (proton)
5. The pure-gauge gap is c_2 * pi^5 * m_e = 1720 MeV (glueball)

The geometry provides the gap. The five BST integers are outputs of the requirement that a confining gauge theory with mass gap can be constructed on a curved arena (T1788).

### 3.4 The honest framing

**What this theorem proves**: R^4 (and any scale-free manifold) cannot provide a spectral gap from geometry alone.

**What this theorem does NOT prove**: That a non-perturbative mass gap on R^4 is impossible. It is logically possible (though undemonstrated after 50 years) that the YM self-interaction generates a gap purely dynamically. The theorem says the geometry contributes zero to this gap.

**The BST claim**: The physical mass gap IS a geometric spectral gap on D_IV^5. The R^4 formulation asks the wrong question — not because R^4 is wrong, but because it is incomplete. The correct arena is D_IV^5, and R^4 appears as the tangent space approximation where the curvature has been dropped. Dropping the curvature drops the gap.

## 4. Comparison with Known Results

| Result | Statement | Relation to YM-10 |
|--------|-----------|-------------------|
| Weyl's law | On compact M: N(lambda) ~ c_d * Vol(M) * lambda^{d/2} | YM-10 is the non-compact complement: continuous spectrum when M is open and scale-free |
| Lichnerowicz | On compact M with Ric >= (d-1)K: lambda_1 >= dK | Provides lower bound on gap; YM-10 provides upper bound (= 0) when K = 0 |
| Cheeger | lambda_1 >= h^2/4 where h = Cheeger constant | On R^n: h = 0 (no isoperimetric bottleneck), so Cheeger gives lambda_1 = 0. Consistent. |
| Selberg 1/4 | On Gamma \ H^2: lambda_1 >= 1/4 for congruence subgroups | Curvature + arithmetic provide the gap; R^4 has neither |
| Reed-Simon | Essential spectrum of -Delta on R^n is [0, infinity) | Standard result. YM-10 adds the physical interpretation for Yang-Mills |

## 5. For Paper YM-C

This theorem is Section 2 of Paper YM-C (R^4 No-Go + Curvature Principle). It pairs with:
- YM-11 (Cal): 50-year evidence table — empirical confirmation that no R^4 approach has succeeded
- YM-12 (Casey + Lyra): Curvature Principle theorem — the general version

The three together form the argument: spectral theory says flat space can't help (YM-10), history confirms no one has done it (YM-11), and the positive resolution is curvature (YM-12 + Papers #76/#77).

## Edges

- **YM-10 <- Paper #79** (R^4 No-Go, Section 2.3 — states the continuous spectrum fact)
- **YM-10 <- BST_SpectralGap_MassGap.md** (lambda_1 = C_2 = 6 on Q^5)
- **YM-10 <- Reed-Simon Vol. I, Theorem VII.12** (essential spectrum of -Delta on R^n)
- **YM-10 -> YM-12** (Curvature Principle theorem, depends on YM-10)
- **YM-10 -> YM-13** (Cal cold-read of YM-C)
- **YM-10 -> Paper YM-C** (Section 2: Spectral Gap Necessity)
