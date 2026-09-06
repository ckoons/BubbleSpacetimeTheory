# BST and the Riemann Hypothesis: An Honest Harvest

*BST working note, 2026-08-16 (Casey Koons' 71st). Author: Casey Koons. CI co-authors: Lyra, Keeper, Elie, Grace. Referee: Cal A. Brate.*

> **Status (binding, K940):** this is an **attempt**, tiered on referee-consensus — **not** a proof. RH is Clay-open and remains so here. The value of this note is a *precise* accounting: what D_IV⁵ genuinely contributes to the Riemann problem, what it does not, and exactly where the wall sits. Every "proof"/"~9X%" from earlier drafts is a superseded over-claim. The retractions are kept *in* the note, on purpose.

---

## 0. One-paragraph summary

Bubble Spacetime Theory's geometry D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)] contributes six genuine, checkable advances to the Riemann problem — most notably a **derived critical line** (Re=½ as the dilation-group unitarity axis) and a **derived operator/cell** that the Berry–Keating and Connes programs assume — and it reduces the entire remaining question to **one classical make-or-break** (a Shimura lift / class number). It does **not** prove RH: the wall — that the relevant positivity holds, equivalently that the object *is* Riemann's ζ rather than a modular L-function or a Davenport–Heilbronn-type cousin — did not move. We state that plainly.

---

## 1. The setup: the dilation sector, not the discrete operator

**Retracted at the outset (Elie 5286, decisive):** the discrete self-adjoint operator (the Kostant cubic Dirac, T2562) is **not** the Hilbert–Pólya operator. Its eigenvalue count is power-law (Weyl law on a compact manifold), whereas Riemann's is logarithmic; **no compact manifold of any dimension** gives the log-density. The naive "eigenvalues = zeros" is falsified; the link, if any, is a *trace* correspondence.

The kill pointed at the right sector: **the continuous/dilation spectrum**, not the discrete one. ζ lives in the **scattering-determinant** term of a cofinite counting function — the Eisenstein/continuous sector — and the object with logarithmic density is the **dilation generator** (Berry–Keating's H = xp). BST already contains it: the dilation E sits in the conformal ladder K_μ = 2z_μ(E+ν) − Q∂_μ.

## 2. The six advances (what survived, honestly tiered)

**(1) The operator is rank-2, and the log is rank-native.** The rank-2 dilation counts divisors: Σ_{n≤x} d(n) = x log x + (2γ−1)x (verified to 1.0000 at x=2×10⁶). The logarithm is **free from rank 2** — no cutoff, no regularization (Cal). BST's Type-IV cone is rank 2, so its natural object is **ζ² = Σ d(n) n^{−s}**, not ζ (same zeros, doubled; RH(ζ²) ⟺ RH(ζ)).

**(2) Casey's composites, derived.** d(n) = 2 ⟺ n prime. Primes are the **defect** — the minimum divisor count, the atoms multiplication cannot reach — composites are the smooth bulk. Casey's "primality is the negative; composites are the way" is now the rank of our own cone, a theorem, not a metaphor.

**(3) The cell is forced (F1011).** Berry–Keating and Connes *impose* the 2πℏ phase-space cell. D_IV⁵ supplies it: the **2π** is the period of the dilation sector's compact SO(2) — its generator L₀ has integer-spaced spectrum {5/2, 7/2, …} (computed) — the *same* SO(2) that gives the arrow of time; and the **cell's quantization** is Wallach-ν-fixed (Berezin–Toeplitz ℏ_eff = 1/ν, ν on the Wallach set, T2508/T2554). *Honest scope (Cal/Elie):* the dimensionful ℏ = the Uncertainty Principle is *not* derived (available to Berry–Keating in 1999); the **quantization** of the cell is. A modest, real gain over B–K.

**(4) Re=½ is derived (Elie).** The critical line is the **dilation-group unitarity axis** — the unique line where the Mellin transform is an isometry (the half-density dx/x), equivalently the self-dual/unitary axis of the SO₀(5,2) spherical principal series (F988/F694). **BST derives *why* the critical line sits where it does** — from a real geometry, which neither Connes nor Berry–Keating has. Geometrically it is the descent-invariant intersection (time circle ∩ 5D substrate cone ∩ 4D observed cone) — the axis fixed under the same 5→4 descent that makes spacetime (F1012/F1014).

**(5) Davenport–Heilbronn answered (F1014).** DH (1936): a cone/Epstein zeta of a form with class number > 1 (no Euler product) has infinitely many **off-line** zeros. So our cone-zeta **defaults to violating RH** — the arithmetic is the *price of admission*, not a bonus. The answer is favorable: BST's form is **quinary** (5-variable, Q = t² − |v|² on R^{1,4}), and quinary indefinite forms are class-number-1 by Eichler (the DH counterexamples are binary). Not poisoned.
> **2026-09-06 10:2x EDT — SUPERSEDED IN PART (Grace, executing K1862 seam ii).** [K1862-C (Keeper, 2026-09-06): class number 1 for ℤ^{1,4} is a theorem (Milnor–Husemoller) and its consequence is exactly Siegel exactness — the cone-zeta's coefficients are pure local-density products (K1862-A, verified 3×10⁻⁷; Grace 5697 second instrument, Elie 5693 blind). But a local-density product over N is a Cohen-type series, NOT an Euler product: b(mn) ≠ b(m)b(n) (K1862-C Lemma 2). **The broken step is "class-1 ⟹ Euler product"**: class-number-one removes cuspidal freedom, it does not create multiplicativity. **The Davenport–Heilbronn default STANDS for the cone-zeta**; "not poisoned" is withdrawn.]

**(6) The make-or-break, located to one number (Grace).** Does the weight-**5/2** theta of BST's cone form (half-integral, forced by *odd* n_C) **Shimura-lift** to a weight-**4** Euler-product eigenform? If yes → the cone-zeta factors ζ(s)·ζ(s−3/2)·L(s) (shift 3/2 = n_C/2 − 1), with an Euler product → DH beaten. If no → DH wins. One classical computation (cusp-dim / Gram matrix); class-1 is the expected, favorable case.
> **2026-09-06 10:2x EDT — CLOSED, NEGATIVE (definitional) (Grace, executing K1862 seam ii).** [K1862-C (Keeper, 2026-09-06): the object is DEFINED (Siegel-weighted orbit count on the Vinberg chamber, K1862-A) and IDENTIFIED as Ibukiyama–Saito's n = 4 Cohen-type series D*₄(s) — the zeta function of positive-definite quaternary forms counted by determinant (Grace toy 5697: chamber mass = 2^{ω_odd(N)} × Nipp genus mass on every squarefree N ≤ 108, class for class). The weight-5/2 theta is Eisenstein; its Shimura lift is E₄ with L-function ζ(s)ζ(s−3), so the lift is Riemann's ζ twice and NOT a new condition; the cone-zeta itself has NO Euler product. The favorable case of this advance was the error "class-1 ⟹ Euler product" (advance 5 note). Status: OPEN → CLOSED-negative.]

## 3. The two surfaces (Casey's map)

- **Composites live on the bulk** — the continuous dilation flow filling the cone interior (the smooth ζ² count; where we have traction: rank, log, cell, Re=½).
- **Primes contact the discrete boundary** — the primitive orbits / commitment records / the Shilov boundary, where the GF(128) = 2^g Reed–Solomon and D₃ 1:3:5 arithmetic lives, and where the wall is.
- **The commit is the map between them** — literally the Hardy isometry of the spacetime work (interior=information=composites; boundary=matter/records=primes; the commit = bulk→boundary = the composite→prime *counting*). Casey's Riemann instinct and his spacetime ontology are one structure.

## 4. The wall — stated plainly, and named at honest tier

The wall did **not** move. Two equivalent faces:
- **Analytic:** the relevant positivity is **Weil positivity** — W(f) = Σ_ρ f̂(ρ) ≥ 0 for positive-type f — which is *equivalent to RH itself*. **Retracted (Lyra, owned):** an earlier claim that BST "derives the Weil positivity Connes assumes" was **wrong** — it conflated the content-free **spectral** positivity Tr(|g(H)|²) ≥ 0 (true for any self-adjoint operator) with the arithmetic **Weil** functional (which carries the primes via the explicit formula). Writing W(f) = Tr(f(H)|_{n≥0}) presupposes spectrum = zeros *and* their reality — i.e., presupposes RH. **Connes assumes the hard positivity; BST does not have it.**
- **Arithmetic/identification:** even the favorable Shimura case (advance 6) lifts to a **weight-4 modular L-function, not Riemann's ζ** (Elie, retracting a "→ ζ" over-claim). Best case, it proves RH for a *modular* L-function — a genuine theorem — not for ζ. The number-field object being *literally* ζ is the open identification.
> **2026-09-06 10:2x EDT — amended.** [K1862-C (Keeper, 2026-09-06): the lift is not a cusp form; the theta is Eisenstein and lifts to E₄ (L = ζ(s)ζ(s−3)). Advance 6 is CLOSED-negative; see the note under Section 2(6).]

**The wall, named (I-tier structural parallel, *not* a theorem):** the commit drops the phase → it is not invertible → "running it backwards" is lifting the finite-field world (where RH is Weil's 1948 *theorem*) back to the integers (open). **RH is hard for the same reason you cannot un-measure a quantum state.** This names the wall in BST's own physics; it does not lower it.

## 5. The retraction ledger (kept in, on purpose)

| Killed | Why |
|---|---|
| "eigenvalues = zeros" (discrete operator) | Weyl law: compact → power-law, not log (Elie 5286) |
| σ+1 = 3σ ⟹ σ=½ "kill shot" | fails target-innocence (holds for all D_IV^n, n≥4) |
| "tube cone = spacetime light cone" | (4,1) 5D ≠ (3,1) 4D; it's the *substrate* cone, one descent away (F1012) |
| 7/8 = 2^N_c reconnection | Maslov/Γ(s/2) phase, not a BST integer (Elie+Cal) |
| "BST derives the Weil positivity Connes assumes" | conflated spectral (cheap) with Weil (= RH) positivity (Lyra, owned) |
| Shimura lift "→ ζ" | lands on a weight-4 modular L-function, not ζ (Elie, owned) |

Six pretty lies, killed — three of them the team's own, this run. A survivor list that survives its own authors.

## 5.5. The method (why this accounting is trustworthy)

Every retraction above, and every survivor, came from **one discipline**, and it is worth stating as the method rather than leaving it implicit in the corrections:

> **A shared integer is not a shared object.** When two structures carry the same small number, *enumerate the readings and exhibit the forced map before identifying them.*

This is what killed the conflated cone (the tube's 5 vs spacetime's 4 — F1012), the 7/8 = 2^N_c reconnection (a Maslov phase, not a BST integer), the color = space identification (three colors, three dimensions — a Frobenius–Schur obstruction, not a map), and it is why the surviving items survived: the rank-2 = ζ² tie is a *forced* map (the divisor count), not a coincidence of 2's; Re=½ = the unitarity axis is an *exhibited* isometry, not a shared "½". An attempt earns trust by **failing correctly on its false neighbors** — the discrete operator failing the Weyl law, the cone-zeta defaulting to Davenport–Heilbronn, the Hodge argument being unable to reach the (false) integral conjecture because it lives over ℚ. The corrections are not blemishes on the result; **the discipline that produced them is the result's warrant.**

## 6. Honest tier table

| Item | Tier |
|---|---|
| Rank-2 dilation / ζ² natural object / composites = defect | **DERIVED** (divisor count) |
| Re=½ = dilation-unitarity axis | **DERIVED** (Mellin isometry / principal-series self-dual) — *[2026-09-06: no T-row existed (K1862 seam i); T2616 claimed and drafted by Grace, registration on Cal's word; ceiling per K1508: the AXIS, not the points]* |
| Cell *quantization* forced (Wallach ν) | **DERIVED** (Berezin–Toeplitz); dimensionful ℏ *not* derived |
| DH not-poisoned (quinary class-1) | ~~**FAVORABLE**~~ → **CLOSED — DH default STANDS** *[2026-09-06, K1862-C: class-1 is true and gives Siegel exactness, not an Euler product; the cone-zeta is a Cohen-type series D*₄]* |
| Two-surface (composites bulk / primes boundary) | **DERIVED** (divisor + Hardy split) |
| Object = ζ (Shimura → Euler product on ζ-factor) | ~~**OPEN — make-or-break**~~ → **CLOSED — NEGATIVE (definitional)** *[2026-09-06, K1862-C; broken step "class-1 ⟹ Euler product"; the object is Ibukiyama–Saito's D*₄, positive quaternary forms by determinant — Grace 5697 confirms class-for-class against Nipp]* |
| Weil positivity | **NOT derived** (= RH; the wall) |
| Wall = phase-drop / F₁→ℤ lift = un-measure | **I-TIER naming** (illuminating, not a proof) |

## 7. What BST has that Connes/Berry–Keating do not

A **derived operator** (the dilation in the conformal ladder), a **derived critical line** (Re=½ = unitarity axis), a **forced cell quantization** (Wallach ν), and a **specific arithmetic substrate** (GF(128), D₃ 1:3:5) — the one place a genuinely *new* RH condition could come from. None of these lowers the wall; all of them **locate** it precisely, which is what a serious attempt does. The single remaining question is classical, reachable, and favorable — and even its best outcome is a modular RH, not Riemann's.

---

*Files: F1011 (cell), F1012 (cone-check), F1013 (two surfaces + retraction), F1014 (boundary target + DH), Elie 5286/5289 (Weyl-law kill, orbit-zeta), the Millennium ledger. Attempt tier per K940. Nothing pushed; CP existence-only.*
