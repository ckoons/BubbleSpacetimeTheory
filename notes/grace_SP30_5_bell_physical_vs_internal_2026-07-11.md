# Grace — SP-30-5 Bell: is S_BST ≈ 2.806 a PHYSICAL observable or an INTERNAL substrate quantity?
*2026-07-11. The high-value gate: does the BST Tsirelson deviation survive as a measurable BST-vs-QM falsifier, or
reduce to standard 2√2 observably? Computed from the corpus's own machinery. Respects Cal #259 (ρ=1 Hardy-isometry
NOT invoked). VERDICT: leans INTERNAL — three corpus theorems concur; the falsifier claim conflicts with them.*

## The prediction (pinned, T2399, Toy 3119 8/8 @ 1e-14)
S_BST² = (2^g − rank)/2^{rank²} = 126/16 = 7.875; Tsirelson² = 8; **Tsirelson² − S_BST² = 1/2^{N_c} = 1/8 EXACT.**
S_BST = 2.806 vs 2√2 = 2.828 (0.78% below). As a visibility: S_BST²/Ts² = 63/64 = 1 − 1/2^{C_2} → λ = 0.992.

## The discriminator: three corpus facts, all pointing INTERNAL
1. **T754 (PROVED, D0) — Born rule = Bergman invariant measure = Gleason's P = |ψ|², FORCED** (dim N_c=3 ≥ 3). The
   substrate quantum space is the complex Bergman/Hardy Hilbert space H²(D_IV⁵). **Gleason on any complex Hilbert
   space of dim ≥ 3 forces the STANDARD Born rule → standard correlations E(a,b) → CHSH max = 2√2 (Tsirelson
   achieved).** There is no room for an observable visibility < 1 on a Gleason space.
2. **T757 (D0) — QM Linearization Completeness:** "all QM at depth ≤ 1; interpretations are D2+ with NO new
   predictions." BST REPRODUCES QM observably. A genuine measurable Bell deviation would be a NEW observable
   prediction — **directly contradicting T757.**
3. **T2399's form is a STATE-COUNT ratio, not a correlation.** (2^g − rank)/2^{rank²} counts substrate states
   (2^g per cell, rank frozen, 2^{rank²} Bell-max subspace). That is an INTERNAL combinatorial quantity, not a
   computed ⟨A_a ⊗ B_b⟩ expectation. The "sharp value" was never a physical correlation.

## Why finite-D does NOT lower the bound (the physical argument)
The proposed mechanism is "the substrate's finite 2^g structure lowers the ideal CHSH below Tsirelson." But
**Tsirelson's 2√2 is ACHIEVED by qubits (2-dim/party)**, and the 2^{rank²}=16-dim (4-qubit) Bell-max subspace only
RAISES the available dimension — which cannot lower the bound. The "−rank frozen states" would have to survive
Gleason coarse-graining into the observable correlation, and Gleason (T754) says they do not. So the finite-D
argument does not produce an observable deviation.

## VERDICT (leans INTERNAL, high confidence — with the definitive test named)
**The observable CHSH reduces to standard 2√2. S_BST = 2.806 is an INTERNAL substrate state-count, not what a Bell
apparatus measures.** The "sharpest falsifier" claim conflicts with the corpus's own T754 (Gleason) and T757
(completeness); those are the more defensible (Gleason is a hard theorem). **Recommendation: retire SP-30-5 to
"Tsirelson-CONSISTENCY" (BST reproduces QM's Bell correlations) — do NOT promote to an outreach falsifier.**

Additional problem with the falsifier framing (independent of physical/internal): ALL real Bell experiments measure
S < 2√2 from imperfections. To be a falsifier, BST must predict a SPECIFIC imperfection-corrected 2.806 vs QM's
imperfection-corrected 2√2. If the ideal BST value is 2√2 (Gleason), the two coincide and the falsifier collapses.

## What would OVERTURN this (make it physical) — the open piece T2399 flagged
A substrate-Hamiltonian diagonalization showing the ACTUAL correlation ⟨A_a ⊗ B_b⟩ on the Hardy space carries the
1/2^{N_c} into E(a,b) — i.e. the substrate spin observables are NOT perfect ±1 dichotomic (a genuine fundamental
visibility cap that survives Gleason because the substrate QM is NOT standard complex-Hilbert). That would require
BST to be a genuine SUB-quantum theory that modifies QM (contradicting T757). I do not see how a deviation survives
Gleason on the complex Bergman space — but the diagonalization is the decisive computation, and until it lands the
verdict is a strong LEAN, not a proof.

## THE LOOPHOLE — and it's CLOSED by the corpus's own observable-Bell theorems
My Gleason argument (above) only constrains the Born rule (correlations GIVEN a state). A deviation could still hide
in the achievable ENTANGLEMENT (the max-entangled state being sub-maximal → visibility < 1 without violating
Gleason). So I checked what the corpus's OTHER CHSH theorems give for the observable quantum bound:
- **T1417 (D0, PROVED): "Quantum bound |S| ≤ 2√2 = rank·√rank from Hilbert geometry."** The observable quantum CHSH
  max is STANDARD 2√2.
- **T755 (D1) / Paper 20 line 510: "Holonomy maximum = Tsirelson bound = 2√2 from D_IV⁵ curvature → Bell tests."**
  The MAX HOLONOMY (= max achievable entanglement, T755) IS 2√2 — the geometry REACHES the standard bound.
**⟹ the entanglement loophole is CLOSED: the geometry achieves 2√2 (T755), so the max-entangled state is not
capped below Tsirelson.** The 2.806 (T2399) is a DIFFERENT quantity — a finite-cell state-count — not the observable
holonomy/entanglement max. The corpus's own observable-Bell theorems (T1417, T755, Paper 20) all give **2√2**.

## VERDICT — upgraded to CONFIRMED-INTERNAL (within the corpus's own framework)
The corpus's own observable-Bell theorems (T1417 quantum bound = 2√2; T755/Paper 20 max holonomy = 2√2; T754 Born
= Gleason; T757 no new predictions) UNANIMOUSLY give the OBSERVABLE Bell max as **2√2**. S_BST = 2.806 (T2399) is
an INTERNAL finite-cell state-count, inconsistent with those as an *observable*. **SP-30-5 is INTERNAL. Retire it to
Tsirelson-CONSISTENCY. Do NOT promote to outreach.** To make it physical one would have to OVERTURN T1417 + T755 +
Paper 20 (the observable-Bell theorems) AND show the substrate modifies QM (contradicting T757) — a very high bar,
and not supported by anything in the corpus.

## THE DECISIVE COMPUTATION (Saturday 2nd pull): max holonomy in H², directly computed
Keeper's decider: compute the max holonomy = max CHSH in the physical H² (Cal #259: no (1−P) complement).
- Physical measurement = a 2-dim spin projection (dichotomic ±1) — what a Bell apparatus actually does. Substrate
  spin from SO(2)/SU(2) ⊂ K gives genuine ±1 eigenvalues. Bell state |Φ+⟩ in H²⊗H².
- **Maximized CHSH over all settings = 2.82843 = 2√2 EXACTLY (Tsirelson SATURATED).** (Direct computation, grid-
  maximized — not a theorem citation. NB: a hand-picked-settings line first returned 0.0 from a sign-convention bug;
  I did NOT conclude from it — the reliable number is the maximization.)
- **The 1/2^{2N_c}=1/64 reduction requires non-±1 observables** (visibility 0.992·cos θ) = measurement leaking off
  the 2-dim spin into the substrate-spinor structure BEYOND it = the **(1−P) COMPLEMENT.** Cal #259: (1−P) is
  non-physical. A Bell apparatus projects onto the 2-dim spin (P), never measures (1−P). **The reduction has no
  physical home.**

## VERDICT — DECISIVE: SP-30-5 is INTERNAL, retires to Tsirelson-consistency
Max holonomy in H² = 2√2 exactly (computed). T755 (max holonomy = 2√2) + T1417 (quantum bound = 2√2) + T754 (Born =
Gleason) + T757 (no new predictions) all CONFIRMED by direct computation. **S_BST = 2.806 is the internal finite-cell
count living in the non-physical (1−P) complement. The observable Bell max is 2√2. SP-30-5 is NOT a falsifier —
retire it to standard-Tsirelson CONSISTENCY. Do NOT send to outreach.**

## Discipline
- Cal #259 respected: the ρ=1 Hardy-isometry (retracted) is NOT invoked; the (1−P) complement is where the
  reduction lives and it's ruled non-physical. Computed in H² only.
- Calibration: lean (Gleason) → corpus-confirmed (T1417/T755) → DIRECTLY COMPUTED (max CHSH in H² = 2√2). Grounded
  in a computation + four theorems. And I caught my own CHSH bug (0.0) before concluding from it. The escape (physical
  deviation) would need to overturn the corpus's QM chapter AND put physics in the (1−P) complement — not supported.
