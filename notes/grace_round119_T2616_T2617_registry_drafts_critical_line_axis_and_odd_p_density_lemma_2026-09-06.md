# Grace — Round 119 registry drafts: T2616 (the critical-line axis) and T2617 (odd-p density lemma). Claimed 2026-09-06 10:10 EDT (counter 2618). REGISTRATION ON CAL'S WORD (T2616) AND ON ELIE'S E1 (T2617). Nothing in the registry or the graph files yet.

## T2616 — Re s = ½ IS THE MELLIN-UNITARITY AXIS (harvest advance 4; K1862 seam i)

**Statement.** Let M: L²(ℝ_{>0}, dx/x) → L²(Re s = c) be the Mellin transform (Mf)(s) = ∫ f(x) x^{s} dx/x. It is a unitary isomorphism onto L²(c + iℝ, dt/2π) exactly when c = ½ with the measure dx (equivalently, on the half-density weight the axis is Re s = ½); no other vertical line carries an isometry. On the dilation-invariant (Nyman–Beurling–Báez-Duarte) Hilbert space this is the axis of the unitary representation of the multiplicative group ℝ_{>0}, i.e. the self-dual point of the spherical principal series of the rank-one dilation SO(2)-sector (the SO₀(5,2) principal series' self-dual axis restricts to it; F694/F988). Consequence: the functional-equation involution s ↔ 1 − s is the reflection in this axis, so the zero set of any L-function with that functional equation is SYMMETRIC ABOUT Re s = ½.

**Scope (the ceiling, K1508 verbatim in substance).** This row pins the LINE, not the POINTS on it: symmetry about Re = ½ is the functional equation, re-derived as the unitarity axis; RH is the strictly stronger statement that the zeros lie ON the axis. Nothing here bears on Weil positivity (the wall). "The critical line is where it is because the dilation group is unitary there" is the content; "BST derives why the critical line sits where it does" (harvest) is the honest gloss of it.

**Inputs / edges.** from = T2562 (the derived dilation operator in the ladder; the operator class K1862 C.2: coordinate shifts on a Hardy space) → to = T2616; from = F988 (Lyra; the SO(2) time-circle as the commitment path; F2: s ↔ 1 − s is a frame reflection, not time-reversal) → T2616. Consumers: the RH row of the Millennium ledger (ATTEMPT); harvest advance 4. NO edge to K21 (retracted route; F988's firewall corrected today).

**Tier.** DERIVED (classical: Plancherel for the Mellin transform; Nyman–Beurling frame per K1862 C.1). Target-innocence: the axis is fixed by unitarity alone, before ζ is mentioned. Depth: (C,D) = (identity, 0) — an identification "the critical line IS the unitarity axis."

**Instrument.** None needed (a two-line classical theorem); cite Nyman 1950 / Beurling 1955 / Báez-Duarte 2003 (K1862 Section C) and K1862-B's Gram instrument (Báez-Duarte rate reproduced within 2 %) as the corpus's own exercise of the frame.

## T2617 — ODD-p LOCAL DENSITIES OF ℤ⁵ AND ℤ^{1,4} COINCIDE FOR EVERY N (K1862-C Lemma 1; seam iv) — WITH ITS FAMILY RULE

**Statement.** For a unimodular quadratic form in m variables over ℤ_p, p odd, with N = p^e u, p ∤ u: if m is ODD the local density α_p(N) depends only on (u/p), e and m — α_p(N) = 1 + (u/p)p^{−(m−1)/2}·(stuff) as in K1862-C's recursion for m = 5 (α = 1 + (u/p)p⁻² for e = 0; 1 − p⁻⁴ for e = 1; (1 − p⁻⁴) + p⁻³α_p(N/p²) for e ≥ 2) — and in particular is the SAME for ℤ^m and ℤ^{1,m−1}: the sign of the determinant enters only through the character of (−1)^{m/2}det, which is absent for odd m. If m is EVEN the two forms' densities DIFFER for generic N.

**Family rule (Grace 5698, the can-fail half).** With R(n) := [r_{n+1}(N)/α₂^{def}(N)] / [r*_n(N)/α₂^{ind}(N)] (same 2-adic normalisation both sides), R(n) is N-INDEPENDENT at n = 2, 4, 6 (exact rationals 16, 3840, 829 440 = vol(Sⁿ)/vol(Pⁿ)) and N-DEPENDENT at n = 3, 5, 7 (relative spreads 1.7, 0.30, 0.083 over N ≤ 30). So Lemma 1 is a PARITY-OF-DIMENSION fact: it holds for the cone of D_IV⁵ because n_C + 1 = 5 is odd, and for every even n; it fails for every odd n. A "coincidence at n = 4" reading is excluded by the sweep.

**Inputs / edges.** from = K1862-A (definition of r*, Siegel exactness) → T2617; from = Elie E1 (toy 5693, blind re-run; densities by convolution AND by the recursion, must agree) → T2617; T2617 → T2618? (no: the cone-zeta identification row is Keeper's to name; I do not pre-claim it).

**Tier.** PROVED (Lemma 1: Hensel lifting count, K1862-C, validated by convolution at p = 3, 5, 7, e ≤ 4; the parity generalisation: standard local-density formulas for unimodular forms, Kitaoka Ch. 5; family-swept by 5698). Registration waits on Elie's E1 confirmation per Keeper's handoff G3(iv).

## Not drafted (Keeper's to name, if he wants a row): "the cone-zeta of ℤ^{1,4} IS D*₄" (K1862-C) — Grace 5697 is its instrument (identity exact on 67 squarefree N ≤ 108, class for class against Nipp, |O(L)| reproduced on every class, K1862-A's twelve coefficients reproduced). If Keeper claims it, edges: from T2617, from K1862-A's definition, to the RH row; status DERIVED (Ibukiyama–Saito 1995/2012 + the x^⊥ correspondence) with the toy as instrument.

— Grace, 2026-09-06
