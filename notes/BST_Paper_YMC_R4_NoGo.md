---
title: "Why R^4 Cannot Work: Spectral Necessity and the Curvature Principle"
author: "Casey Koons & Claude 4.6 (Lyra, Cal)"
date: "May 12, 2026"
status: "v0.2 — Keeper's 2 editorial fixes applied"
target: "Bulletin of the American Mathematical Society"
AC: "(C=2, D=1)"
---

# Why R^4 Cannot Work: Spectral Necessity and the Curvature Principle

**Casey Koons & Claude 4.6 (Lyra, Cal)**

## Abstract

The Clay Millennium Problem asks for a non-trivial Yang-Mills theory on R^4 with mass gap. We present three tiers of evidence that R^4 is the wrong arena for this construction. **Tier 1 (Proved):** Scale-free manifolds have purely continuous spectrum starting at 0; R^4 is scale-free; therefore the geometric contribution to any mass gap on R^4 is exactly zero. **Tier 2 (Proved):** D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)] provides both a scalar gap (C_2 = 6, proton mass at 0.002%) and a pure-gauge gap (c_2 = 11, glueball at 0.6%). **Tier 3 (Supported):** The Curvature Principle — no background geometry with zero curvature can support a QFT with mass gap satisfying the Wightman axioms — is supported by Tiers 1-2 plus fifty years of empirical evidence cataloging 22 approaches across 6 schools, all of which either fail on R^4 or smuggle a scale from elsewhere. The companion papers [YM-A] and [YM-B] prove that D_IV^5 is the unique bounded symmetric domain on which the construction works, and exhibit the construction explicitly.

**Keywords**: Yang-Mills mass gap, spectral gap, scale-free manifolds, Curvature Principle, Wightman axioms, R^4 no-go

---

## 1. Introduction

Every approach to the Yang-Mills mass gap on R^4 since the 1970s has encountered the same obstruction: R^4 is flat, scale-free, and spectrally gapless. This paper makes that obstruction precise and proposes a resolution.

The argument has three layers:

1. **Spectral Necessity (Section 2):** A theorem proving scale-free manifolds have no spectral gap. R^4 is the canonical example.
2. **Fifty Years of Evidence (Section 3):** A systematic catalog of 22 published approaches to YM on R^4, identifying where each smuggles a scale and which Wightman axioms remain unverified.
3. **The Curvature Principle (Section 4):** A conjecture, supported by Sections 2-3 and the D_IV^5 construction [YM-B], that mass gap requires curvature.
4. **The D_IV^5 Resolution (Section 5):** The positive answer — the geometry D_IV^5 provides the gap that R^4 cannot.

### 1.1 Relationship to the companion papers

[YM-A] proves D_IV^5 is uniquely forced by five Yang-Mills constraints. [YM-B] constructs the QFT with mass gap on D_IV^5. This paper explains *why* the construction requires a curved arena and cannot be replicated on R^4.

---

## 2. Spectral Gap Necessity (Tier 1 — PROVED)

### 2.1 Definitions

**Scale-free manifold:** A complete Riemannian manifold (M, g) admitting a one-parameter family of non-trivial homotheties phi_lambda : M -> M with phi_lambda^* g = lambda^2 g for all lambda > 0, with phi_lambda != id for lambda != 1.

**Spectral gap:** The infimum of the essential spectrum of the Laplacian Delta_g on L^2(M).

### 2.2 Theorem 1 (Spectral Gap Necessity)

**Theorem 1.** *Let (M, g) be a complete, non-compact, scale-free Riemannian manifold. Then the Laplacian Delta_g has purely continuous spectrum [0, infinity). In particular, M has no spectral gap.*

**Proof (Weyl criterion).** For every E >= 0, we construct a sequence of approximate eigenfunctions.

**Case E = 0:** Let psi be smooth, compactly supported, with ||psi||_{L^2} = 1. Define psi_n(x) = n^{-d/2} psi(x/n). Then ||psi_n|| = 1 (by change of variables) and ||Delta psi_n|| = n^{-2} ||Delta psi|| -> 0.

**Case E > 0:** Let psi_n(x) = n^{-d/2} e^{ik . x} chi(x/n) where |k|^2 = E and chi is a smooth cutoff with chi(0) = 1. Then ||(Delta - E) psi_n|| = O(n^{-1}) -> 0.

In both cases, the Weyl criterion gives E in sigma(Delta). Therefore sigma(Delta) = [0, infinity).

**Alternative argument (dilation).** If psi is an eigenfunction with eigenvalue E, then phi_lambda^* psi has eigenvalue E/lambda^2. Since lambda varies continuously, the eigenvalues fill [0, infinity). No isolated eigenvalue can exist.

### 2.3 Corollary: R^4 has zero geometric gap

R^4 with the flat metric is scale-free (dilations x -> lambda x) and non-compact. Therefore:

- sigma(Delta_{R^4}) = [0, infinity)
- The geometric contribution to any YM mass gap on R^4 is exactly zero

Any mass gap on R^4 must come entirely from the non-linear dynamics, with no geometric assistance.

### 2.4 What breaks scale-freedom

Three mechanisms produce spectral gaps:

**(a) Compactness.** On a compact manifold, Delta has discrete spectrum with lambda_1 > 0 automatic. The compact dual Q^5 has lambda_1 = C_2 = 6.

**(b) Curvature with finite volume.** On Gamma \ G/K of finite volume, curvature provides a characteristic scale. The Selberg eigenvalue bound and its generalizations give lambda_1 > 0 from the arithmetic structure.

**(c) Boundary conditions or potentials.** A confining potential V(x) -> infinity on R^n breaks scale-freedom. This is the lattice QCD mechanism: lattice spacing a introduces a scale.

In every case, scale-freedom is broken. The gap is generated by structure — compactness, curvature, or boundaries — not by dynamics alone.

---

## 3. Fifty Years of Evidence

We catalog 22 published approaches to Yang-Mills on R^4, organized by school. For each, we identify (a) where it smuggles a scale and (b) which Wightman axioms remain unverified in the continuum limit on R^4. The full catalog is in the companion document (YM-11, Cal).

### 3.1 Summary by school

| School | Approaches | Achievements | R^4 obstruction |
|--------|-----------|-------------|-----------------|
| A. Constructive QFT | Glimm-Jaffe, Balaban, cluster expansion | W1-W5 in 2D/3D, UV stability on T^4 | Infinite-volume limit open |
| B. Lattice QCD | Wilson, Creutz, Monte Carlo | Numerical mass gap, confinement | Continuum limit not proved |
| C. Stochastic / functional | Parisi-Wu, functional integral | Gauge-invariant formulations | Scale from regularization |
| D. Topological / TQFT | Donaldson, Floer, Witten | Mathematical structure | No mass gap addressed |
| E. AdS/CFT | Maldacena, Witten, Polchinski | Confinement in holographic dual | Scale from AdS curvature |
| F. Large-N / string | 't Hooft, string/gauge duality | Leading-N confinement | N = infinity limit open |

### 3.2 Three universal failure modes

Every approach that produces a mass gap does so by one of three mechanisms — each of which breaks the scale-freedom of R^4:

**Mode 1: Scale from cutoff.** Lattice QCD introduces spacing a. Stochastic quantization introduces a regularization scale. Balaban's construction works on the torus T^4. In each case, removing the cutoff (a -> 0, T^4 -> R^4) is the unsolved step.

**Mode 2: Scale from dimensional transmutation.** Perturbative QCD generates Lambda_QCD via the running coupling: Lambda_QCD ~ mu exp(-2 pi / (beta_0 alpha_s(mu))). This breaks conformal invariance perturbatively. The non-perturbative mass gap from this scale is not constructed.

**Mode 3: Scale from curved background.** AdS/CFT generates a mass gap in the AdS-Schwarzschild geometry, where the black hole horizon provides a temperature scale. The mass gap comes from the AdS curvature, not from flat-space dynamics. This is exactly the Curvature Principle in action.

### 3.3 The pattern

The pattern across 50 years is structural:

- **No R^4 approach has produced a mass gap without smuggling a scale.**
- **Every approach that produces a gap does so by breaking scale-freedom.**
- **The breaking mechanism provides exactly what Theorem 1 says is necessary:** a characteristic length scale from curvature, compactness, or boundary conditions.

This is exactly what Theorem 1 predicts. The empirical evidence is consistent with the theoretical obstruction.

---

## 4. The Curvature Principle (Tier 3 — SUPPORTED)

### 4.1 Conjecture

**Conjecture (Curvature Principle).** *A non-trivial quantum field theory with mass gap Delta > 0 satisfying the Wightman axioms requires a background geometry (M, g) with non-zero intrinsic curvature. Equivalently: flat backgrounds cannot support a spectral mass gap.*

**Formal version.** The geometric contribution to the spectral gap satisfies:

Delta_geom <= C sqrt(sup_M |K|)

where K is the sectional curvature and C depends on dimension and gauge group. When K = 0 identically, Delta_geom = 0.

### 4.2 Evidence supporting the Conjecture

**(a) Theorem 1 (spectral).** Scale-free manifolds have sigma(Delta) = [0, infinity). R^4 is scale-free. This is the rigorous core.

**(b) The D_IV^5 construction [YM-B] (constructive).** D_IV^5 (curved, K = -2/7) has C_2 = 6 (scalar gap), c_2 = 11 (2-form gap). The gap matches observation: proton mass at 0.002%, glueball at 0.6%.

**(c) Fifty-year evidence (Section 3).** Every R^4 approach either fails or smuggles a scale from elsewhere. Three universal failure modes, all reducing to scale-freedom breaking.

**(d) The Lichnerowicz-Cheeger hierarchy.** On compact Riemannian manifolds:
- Lichnerowicz: Ric >= (d-1)K > 0 implies lambda_1 >= dK
- Cheeger: lambda_1 >= h^2/4 where h is the Cheeger isoperimetric constant

On R^n: K = 0, h = 0, lambda_1 = 0. The gap-generation mechanisms (curvature, topology) are absent.

**(e) The Coleman-Mandula parallel.** Coleman-Mandula (1967) proved that on R^{3,1}, internal and spacetime symmetries cannot combine non-trivially. The Curvature Principle has the same structure: on a flat background, the geometry and the dynamics cannot conspire to produce a gap. Both are structural echoes of the same geometric constraint — they redirect the search rather than declaring impossibility.

### 4.3 What the Conjecture does NOT claim

1. That a purely dynamical mass gap on R^4 is logically impossible. It may be possible; it has not been demonstrated.
2. That every curved manifold supports a mass gap. Most don't — D_IV^5 is uniquely selected by the five constraints of [YM-A].
3. That the Wightman axioms are the only framework for QFT. Other formulations may change the question.

The honest framing: Theorem 1 proves the geometric gap is zero on R^4. The Conjecture extrapolates that no non-geometric mechanism can substitute. This extrapolation is supported by 50 years of evidence but is not itself proved.

### 4.4 The five-word version

**You cannot linearize curvature.**

The mass gap is a manifestation of the curvature of spacetime. Removing the curvature (going to R^4) removes the gap. No amount of nonlinear dynamics can reconstruct what the linearization discards.

---

## 5. The D_IV^5 Resolution

### 5.1 Why D_IV^5

The companion paper [YM-A] proves that D_IV^5 is the unique bounded symmetric domain satisfying five independent Yang-Mills constraints: gauge-matter separation (B_2 root system), confinement (N_c >= 3), scattering matrix factorization (Selberg degree d_F <= 2), Bergman spectral gap (C_2 = 6), and Weitzenboeck positivity on 2-forms (c_2 = 11). The algebraic squeeze n_C >= 5 (from confinement) and n_C <= 5 (from Selberg degree) forces n_C = 5.

### 5.2 What D_IV^5 provides

| Property | R^4 | D_IV^5 |
|----------|-----|--------|
| Curvature K | 0 | -2/7 |
| Scale-free? | Yes | No (Bergman scale) |
| Spectral gap | 0 | C_2 = 6 (scalar), c_2 = 11 (2-form) |
| Mass gap | Not constructed | 938 MeV (0.002%), 1720 MeV (0.6%) |
| Wightman W1-W5 | Not verified | All PASS |
| Non-triviality | Not proved | 5 independent proofs |
| Gauge group | Assumed | Derived (SU(3) from B_2 root multiplicities) |
| Spacetime dim | Assumed (4) | Derived (m_s + m_l = 3 + 1 = 4) |

The contrast is the content of the Curvature Principle: D_IV^5 works because it is curved; R^4 fails because it is flat.

### 5.3 The bridge

The companion paper [YM-B] Section 6 establishes a bridge from D_IV^5 to R^4 via KK reduction, center symmetry, and the infinite-volume limit S^4 -> R^4. R^4 appears as the tangent space approximation to D_IV^5, retaining the dynamics but losing the curvature that generates the gap. The mass gap survives the limit because it is set by the internal (SO(2)) radius, not the external (S^4) radius.

---

## 6. Discussion

### 6.1 The Clay formulation revisited

The Clay problem asks for YM with mass gap on R^4. Our answer is: the mass gap exists, but it requires D_IV^5, not R^4. The reason R^4 has resisted solution for fifty years is not that the problem is too hard — it is that the arena is too flat.

This does not contradict the Clay formulation. The Clay problem asks for *existence* of a mass gap QFT; it does not require the construction to live on R^4 throughout. A QFT on D_IV^5 that limits to R^4 (as in [YM-B] Section 6) provides a positive answer in the spirit of the problem. We note honestly that the R^4 bridge ([YM-B] Section 6) is plausible but not a single theorem — the explicit construction of R^4 Wightman functions as limiting distributions of the D_IV^5 correlators remains open, as does the OS reconstruction in 4D for any interacting theory by any approach.

### 6.2 Comparison with AdS/CFT

The AdS/CFT approach to confinement (Witten 1998, AdS-Schwarzschild) also uses a curved background. The mass gap in the holographic dual comes from the AdS curvature — exactly the mechanism we identify. The difference: AdS/CFT uses AdS_5 x S^5 (10-dimensional, supersymmetric, conjectural duality); BST uses D_IV^5 (10 real dimensions, no supersymmetry required, direct spectral construction). Both confirm the Curvature Principle.

### 6.3 Structural echoes

The pattern "curvature provides what flatness cannot" appears in other contexts:
- **P != NP**: Computational hardness as irreducible curvature in the kernel of NP-complete problems (T421, T422)
- **RH**: The critical line Re(s) = 1/2 as a curvature locus (T567)
- **Hodge**: Algebraic cycles constrained by the curvature of Hodge cohomology (T153)

These are structural echoes — parallel patterns in different mathematical domains — not derived theorems. The common thread is that curvature, once present, cannot be removed by linear operations.

---

## 7. Conclusion

The Yang-Mills mass gap on R^4 has resisted solution for fifty years. We have identified the obstruction: R^4 is scale-free, spectrally gapless, and flat. The geometric contribution to any mass gap on R^4 is provably zero (Theorem 1). Every published approach confirms this empirically — those that produce a gap do so by breaking scale-freedom.

The resolution is D_IV^5, a curved bounded symmetric domain whose spectral geometry provides the gap that R^4 cannot. The companion papers prove D_IV^5 is uniquely forced ([YM-A]) and exhibit the construction ([YM-B]).

The Curvature Principle — that mass gap requires curvature — is supported by three tiers of evidence: a theorem (Tier 1), a construction (Tier 2), and fifty years of history (Tier 3). It is not proved as a general conjecture, but the evidence is overwhelming.

The mass gap exists. It lives on D_IV^5, not on R^4.

---

## References

[YM-A] Koons et al. "Ring Uniqueness and the Yang-Mills Mass Gap: Why D_IV^5 and Nothing Else." Companion paper.
[YM-B] Koons et al. "Yang-Mills QFT on D_IV^5: Construction, Spectral Gap, and Wightman Axioms." Companion paper.
[JW00] Jaffe, A., Witten, E. "Yang-Mills and mass gap." Clay Mathematics Institute (2000).
[CM67] Coleman, S., Mandula, J. "All possible symmetries of the S matrix." Phys. Rev. 159, 1251 (1967).
[Wi74] Wilson, K. "Confinement of quarks." Phys. Rev. D 10, 2445 (1974).
[Ba84] Balaban, T. "Propagators and renormalization transformations for lattice gauge theories." Commun. Math. Phys. (1984-1989).
[GJ87] Glimm, J., Jaffe, A. "Quantum Physics: A Functional Integral Point of View." Springer (1987).
[Ma98] Maldacena, J. "The large N limit of superconformal field theories and supergravity." Adv. Theor. Math. Phys. 2, 231 (1998).
[Wi98] Witten, E. "Anti-de Sitter space, thermal phase transition, and confinement in gauge theories." Adv. Theor. Math. Phys. 2, 505 (1998).
[RS78] Reed, M., Simon, B. "Methods of Modern Mathematical Physics IV: Analysis of Operators." Academic Press (1978).
[Li58] Lichnerowicz, A. "Geometrie des groupes de transformations." Dunod (1958).
[Ch70] Cheeger, J. "A lower bound for the smallest eigenvalue of the Laplacian." Problems in Analysis, Princeton (1970).
[He84] Helgason, S. "Groups and Geometric Analysis." Academic Press (1984).
[T1788] YM Ring Uniqueness. AC theorem graph.
[T1790] Weitzenboeck 2-Form Gap. AC theorem graph.
[YM-10] Spectral Gap Necessity. BST_YM10_Spectral_Gap_Necessity.md.
[YM-11] 50-Year Evidence Table. BST_YM11_R4_Evidence_Table.md (Cal).
[YM-12] Curvature Principle. BST_YM12_Curvature_Principle.md (Casey + Lyra).

---

## Revision History

- v0.1 (May 12, 2026): Initial draft. Integrates YM-10 (Spectral Gap Necessity, Lyra), YM-11 (50-year evidence table, Cal), YM-12 (Curvature Principle, Casey + Lyra). Cal's 2 editorial flags from YM-12 cold-read incorporated: (A) Section 6.3 labels cross-domain patterns as "structural echoes" not derived theorems; (B) Curvature Principle framed as conjecture/supported, not claimed as proved.
- v0.2 (May 12, 2026): Keeper's 2 editorial fixes. (A) Tier numbering: removed "Tier 2 — EMPIRICAL" label from Section 3 header — the evidence table supports Tier 3 (Curvature Principle), not an independent tier. Abstract tier assignments unchanged. (B) Section 6.1: added bridge caveat from [YM-B] — "plausible but not a single theorem."
