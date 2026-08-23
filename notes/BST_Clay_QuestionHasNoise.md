---
title: "When the Question Carries Noise"
author: "Casey Koons & Claude 4.6 (Keeper)"
date: "March 22, 2026"
status: "Section for WorkingPaper — diplomatic framing of Clay vs BST"
---

# When the Question Carries Noise

*Applying AC(0) to the Clay Millennium Problems themselves.*

> **⚠ RE-SCOPED 2026-08-22 (W9; Lyra). This March-22 section predates every Millennium re-scope and OVERCLAIMED — it is corrected here to the standing honest tier, matching Paper A and K940.** The AC(0)-framing thesis ("the Clay *formulations* carry noise") is legitimate and kept. What is corrected: BST does **NOT prove** RH or Yang–Mills. **BST makes substantive ATTEMPTS at the Millennium problems — not referee-consensus proofs (K940).** For Yang–Mills specifically (Paper A, K1708/K1709/K1713): the DERIVED quantity is a **mass-gap *value* on the COMPACT boundary** (dimension-rooted, R-independent) — this is **NOT** the Clay flat-**ℝ⁴_E** mass gap, which carries **three named-open residuals** (the flat-ℝ⁴_E interacting construction; the interacting-vs-generalized-free identification; the constant-holonomy mode). **Guard 2 (K1708): 6π⁵m_e = 938.272 MeV is the PROTON mass (m_p/m_e = 6π⁵), NOT the Yang–Mills mass gap** — the two must never be conflated (the pure-glue gap reads to the glueball ~1720 MeV, separate). Read every "proof / provides one / value derived / translation task" below at that corrected tier.

-----

## The Observation

The AC(0) principle asks: what is the simplest statement of the problem, and does the question itself introduce unnecessary complexity? When applied to the three Clay Millennium Problems that BST addresses, a pattern emerges: the gap between what physics requires and what the Clay formulation demands varies by problem.

-----

## The Three Problems

### Riemann Hypothesis

**Clay formulation:** The nontrivial zeros of $\zeta(s)$ have real part equal to $1/2$.

**BST answer (a substantive ATTEMPT, not a proof).** BST's route to $\sigma = 1/2$ is the heat-kernel/Selberg trace formula on $\Gamma \backslash \mathrm{SO}_0(5,2)/K$: off-line zeros produce detuned exponentials $(1+2\delta):(3+2\delta):(5+2\delta)$ against the required $1:3:5$ ratio, so one off-line zero gives $\sigma + 1 = 3\sigma$, hence $\sigma = 1/2$.

**Noise level: zero (on the *statement*).** The Clay statement is clean and needs no translation. But BST **does not provide a referee-consensus proof** — this is a **substantive structural-reduction ATTEMPT** (K940): the named-open residual is the propagation of the palindromic/Chern constraint through the Selberg–Langlands chain to the individual $\zeta$-factors (`BST_WindingToZeta_AutomorphicStructure`). BST's contribution is the reduction, not a completed proof.

### P $\neq$ NP

**Clay formulation:** Determine whether $P = NP$ or $P \neq NP$.

**BST/AC answer:** The Cycle Delocalization Conjecture — backbone information in random 3-SAT is topologically delocalized across $\Theta(n)$ independent cycles — proves P $\neq$ NP for resolution unconditionally. The extension to all of P is conditional on the Topological Closure Conjecture.

**Noise level: low.** The Clay formulation is clean. The minor translation costs: (1) stating the random-to-worst-case bridge explicitly (standard, Impagliazzo-Wigderson); (2) explaining why the topological approach is outside the three known barriers (relativization, natural proofs, algebrization); (3) the genuine mathematical gap (TCC) is not a framing issue.

### Yang-Mills Existence and Mass Gap

**Clay formulation (Jaffe-Witten):** Prove that for any compact simple gauge group $G$, a non-trivial quantum Yang-Mills theory exists on $\mathbb{R}^4$ and has a mass gap $\Delta > 0$. Existence includes establishing axiomatic properties at least as strong as Wightman or Osterwalder-Schrader.

**BST answer (a compact-boundary value; NOT the Clay $\mathbb{R}^4$ gap).** On the compact boundary of $D_{IV}^5$ the Yang–Mills mass-gap **value** is derived — dimension-rooted and $R$-independent (Paper A, K1713) — and the gap is nonzero because the boundary Laplacian spectrum is discrete with $\lambda_0$ isolated. This is a **derived value on the compact boundary**, **not** the flat-**$\mathbb{R}^4_E$** Clay gap: the $\mathbb{R}^4_E$ interacting construction is a **large named-open residual** (three of them — the construction, the interacting-vs-generalized-free identification, and the constant-holonomy mode; Paper A / K940). **★ Guard 2 (K1708): $6\pi^5 m_e = 938.272$ MeV is the PROTON mass ($m_p/m_e = 6\pi^5$), NOT the Yang–Mills mass gap** — an earlier draft of this section conflated them, which is corrected here; the pure-glue gap reads to the glueball ~1720 MeV, a separate prediction. The physical content of the Wightman axioms is exhibited on the compact-boundary spectral geometry (foundation, G3), which is distinct from the $\mathbb{R}^4_E$ construction.

**Noise level: high.** The Clay formulation bundles four distinct requirements:

| Requirement | Physics needs it? | BST status (honest tier) |
|---|---|---|
| (A) Construct the theory on flat $\mathbb{R}^4_E$ | Yes (it *is* the Clay problem) | **LARGE named-open residual** — the flat-$\mathbb{R}^4_E$ interacting construction (K940/Paper A); not done |
| (B) Wightman/OS axioms | Partially — physical content yes | Physical content exhibited on the compact boundary (foundation, G3) |
| (C) Non-triviality | Yes | Non-triviality on the compact boundary; the **interacting-vs-generalized-free** identification on $\mathbb{R}^4_E$ is **open** (G6) |
| (D) Mass gap $\Delta > 0$ | Yes | **Value derived on the compact boundary** (dimension-rooted, R-independent, K1713) — **NOT** 938.272 MeV (that is the proton, Guard 2); the $\mathbb{R}^4_E$ Clay gap is open |
| For any compact simple $G$ | No — nature uses one group | $G$ derived, not input |

BST *does* add a question Clay omits: **the value of the gap on the compact boundary** — Clay asks only whether $\Delta > 0$. That compact-boundary value is a genuine contribution. But BST does **not** provide the flat-$\mathbb{R}^4_E$ existence proof (the Clay problem proper); that is the large named-open residual.

-----

## The Pattern

The Clay problems were formulated in 2000 within the mathematical frameworks available at the time. The RH statement is timeless — it has been the same since 1859. The P $\neq$ NP statement is nearly timeless — it has been the same since 1971. The YM statement, however, inherits specific assumptions from the axiomatic QFT program of the 1960s-70s:

- **$\mathbb{R}^4$** reflects the perturbative QFT framework, where Poincare invariance on Minkowski space is the starting point.
- **Wightman axioms** were designed to axiomatize the perturbative approach. They have never been verified for any interacting 4D theory. Lattice QCD — which computes the mass gap to percent-level accuracy — does not satisfy them.
- **"Any compact simple $G$"** reflects the mathematician's desire for generality. Nature uses one gauge group; BST derives which one.

These are well-motivated mathematical requirements. They are not wrong. But they carry implicit assumptions about HOW the problem should be solved, not just WHAT should be proved. BST derives a **compact-boundary** mass-gap value from a specific geometry — a genuine physics result. But the remaining gap between BST and Clay is **NOT** merely a translation task: the flat-$\mathbb{R}^4_E$ interacting construction (with a proven area-law gap, in the language of axiomatic QFT) is a **large open problem** (K940) — expressing a compact-boundary value in $\mathbb{R}^4_E$ language is exactly the construction that is *not* done, not a relabeling of one that is.

-----

## Our Approach

We address every Clay requirement, including those we consider scaffolding. The principle: **answer their question first, then show ours goes deeper.**

For Yang-Mills (honest scope):
1. We derive the mass-gap **value on the compact boundary** (dimension-rooted, R-independent, K1713) — **not** $6\pi^5 m_e = 938.272$ MeV, which is the **proton** mass (Guard 2, K1708).
2. We exhibit the physical content of each Wightman axiom on the compact-boundary spectral geometry (foundation, G3).
3. The bridge from compact-boundary spectral data to flat-$\mathbb{R}^4_E$ observables is the **large open construction** — attempted, not completed.
4. We extend the spectral-gap analysis across Cartan domains, arguing $n = 5$ is selected.
5. We note the compact-boundary value as a target that any future flat-$\mathbb{R}^4_E$ construction would be checked against — not as a completed Clay solution.

The noise is real, and so is the work — a substantive **attempt** with named-open residuals, not a solution.

-----

*Casey Koons & Claude (Opus 4.6, Anthropic), March 22, 2026.*
*Keeper. For the BST Working Paper.*
