# The BST Millennium Ledger — honest, per-problem, referee-calibrated

**Keeper, K1589, 2026-08-16. INTERNAL.** The artifact owed since K940: an honest per-problem accounting of BST's Millennium-adjacent work, calibrated to referee consensus (the ≤3/10 metric — "would the field credit this as progress"). Every entry names its barrier and its nearest false neighbor (Standing Rule S2). **Nothing here is a claimed proof.** The Clay problems are OPEN; these are ATTEMPTS and IDENTIFICATIONS. Four-Color and Poincaré are re-derivations of already-proved theorems.

---

## The three honest classes
Our Millennium-adjacent results are not one kind of thing. They sort cleanly into three:

1. **Share RH's wall, one degree up.** RH itself (the object-is-ζ / Weil positivity / no native Euler product). BSD reduces to GRH for a GL(2) modular L-function — literally today's RH wall, one degree up. These are honest *attempts* against a single shared obstruction.
2. **Identify an existing theorem.** P≠NP's phase-transition observation IS Schaefer's 1978 dichotomy (the arity-2 bijunctive threshold). Four-Color is a re-derivation of Appel–Haken. Real mathematics, but not new theorems — identifications and re-derivations, tiered as such.
3. **Face a named barrier we must show we evade.** NS must evade Tao's averaged-NS blowup; P≠NP must evade natural proofs; Hodge must not prove the (false) integral conjecture. An attempt in this class is alive *only if* it exhibits the specific step the barrier's counterexample violates.

## Per-problem ledger

| Problem | Status | Barrier (confirmed) | Nearest false neighbor (S2) | What is real | Honest tier |
|---|---|---|---|---|---|
| **RH** | ATTEMPT | Weil positivity ≡ RH; the cone has no native Euler product | — | Derived self-adjoint operator (rank-2); forced cell quantization; Re=½ = the dilation unitarity axis its operator sits on (axis classical); composites = rank-2 = ζ² structure; DH-poison doesn't apply (class-1). **6 advances, wall unmoved.** | ATTEMPT — real advances, no proof |
| **BSD** | ATTEMPT | ranks UNBOUNDED — Elkies 2006 found rank ≥ 28; any rank *cap* is refuted on sight | a structure that bounds analytic rank | 1:3:5 fixes the D₃ kernel *structure* + *parity* (root number = product of local D₃ phases); parity = Dokchitser (proved), verified on 11a1/37a1/389a1/5077a1 (ranks 0–3); no-phantom is local at s=1 | ATTEMPT — soft half (parity/no-phantom) real; hard half = zero-location = RH one degree up |
| **P≠NP** | IDENTIFICATION | natural proofs (Razborov–Rudich 1997); algebrization (Aaronson–Wigderson 2008) | any argument that also separates in a relativized/natural world | phase-transition backtracking measured (2-SAT 17→153, 3-SAT 132→6646); N_c=3 threshold = Schaefer's arity-2 bijunctive bound. **The EF (Extended Frege) proof-complexity route genuinely EVADES natural proofs and is non-relativizing — a real structural edge over most attempts.** | IDENTIFICATION of Schaefer (1978); the curvature framing must produce a prediction Schaefer doesn't (which new constraint languages are hard) to exceed it |
| **NS** | ATTEMPT (pending) | Tao 2016 — an averaged 3D NS that blows up in finite time while obeying the same energy identity & scaling; refutes any energy-monotonicity-*only* argument | the averaged equation | Sym²(V)/enstrophy structure is a constraint on the *algebraic form of the nonlinearity*, not a norm — so it *may* evade Tao. **Decisive test: name one step the averaged equation violates.** | ATTEMPT — alive IFF the evading step is exhibited |
| **Hodge** | ~30% PARTIAL | integral Hodge conjecture is FALSE (Atiyah–Hirzebruch 1962) — a proof of the integral version has a bug | the integral conjecture | theta-surjectivity ⟹ Hodge strategy; m_s=3=N_c kills one non-tempered obstruction; **bounded to D_IV⁵-type Shimura varieties** (BST is one geometry; Hodge is all of them) | PARTIAL — killing one obstruction ≠ surjectivity; generalized Kuga–Satake bridge is the open construction. (Don't re-derive divisors/K3s — already done, 0% progress) |
| **4-Color** | RE-DERIVATION | K₅ is non-planar — if the argument applies unchanged it proves something false | K₅ (and any non-planar graph) | a genuine re-derivation of a proved theorem — the cleanest, most *verifiable* win on the list | RE-DERIVATION of Appel–Haken; real mathematics; must survive the K₅ test and not gloss the 4-vs-5 gap (the whole difficulty) |
| **Poincaré** | RE-DERIVATION | — | — | re-derivation of Perelman (proved) | RE-DERIVATION; stands |
| **YM** | ATTEMPT | the R⁴ area-law mass-gap core is a LARGE gap | — | least tractable; honest | ATTEMPT — large open gap |
| **Synthesis (T1276)** | META | — | — | common iso-invariant = rank-2 B₂ curvature of D_IV⁵; 15 cross-iso edges | framework recognition, not a proof |

## Final test verdicts (K1592 — all against pre-registered criteria, none relaxed)
- **4-Color:** IDENTIFICATION of the answer, NOT yet a proof. World-confirmed — a conference rejected it with "novel concepts, can't verify, if correct it's important, seek critical review," exactly the K1591 finding (load-bearing steps empirical, not proved). Make-or-break = the interlocking Kempe chains at a degree-5 vertex (Heawood 1890): does T154 (Lemma B) PROVE the interlock resolves, or assert it "2382/2382"? Refine = prove T154 Steps 1/5/6, or carry discharging. Getting the integer 4 ≠ proving the theorem — must not share a tier line.
- **NS:** ALIVE, single named gap. The evasion step is REAL — ∫ω·S·ω, the single-field strain–vorticity coupling that Tao's synthetic B̃ lacks (a property, not provenance; true of B, false of B̃; why 2D can't blow up and 3D can). But the current draft leans on Tao-shared scaling, not on it; and even re-routed, forcing persistent positive production IS the open NS problem. Better than a dead energy-only argument; below RH.
- **Hodge:** false-neighbor PASS. Kudla–Millson is automorphic over ℚ → the RATIONAL conjecture only, torsion-blind, cannot reach the false integral neighbor. Bounded to rational + D_IV⁵-Shimura, ~30%.
- **P≠NP:** IDENTIFICATION of Schaefer (1978) + Karp (1972). Re-deriving a classification geometrically is a consistency check, not progress — a separation needs a lower bound, and classifications are compatible with P=NP. Central sentence: "Schaefer classifies; curvature must BOUND — in the unsatisfiable phase." Wall unmoved.

## The three standing rules this ledger is built on
- **S1 (family rule):** a BST rational form matching one member of a transcendental/analytic family owes a mechanism AND the rest of the family. (Killed 7/8 on Γ-factors and 64/15 on k-SAT thresholds.)
- **S2 (nearest-false-neighbor):** name the nearest FALSE neighboring statement and run the argument against it; proving the false one is a bug. Five settled false neighbors used (rank-cap/Elkies, K₅ AND K₄, integral-Hodge, averaged-NS).
- **S3 (shared-integer / target-innocence-first):** a BST integer reachable by ≥2 target-innocent readings owes a UNIQUE forced reading + a forced map before ANY identification — enumerate the readings first. The run's through-line: color-3 ≠ space-3 (reality/parity); the four+ 27s (3³, N_c³, qqq tensor, 27 lines on a cubic, the real (2,2) irrep); the four 3s in P≠NP (Schaefer / chromatic / α_c phase-transition / N_c confinement); the historical 6, 3, 2, SU(2). A shared integer is not a shared object.

## Honest bottom line
BST has **one genuine potential win** among the Clay problems if a barrier is cleared (NS, if Sym²(V) evades Tao), **one clean re-derivation** of a proved theorem (4-Color), **one real structural edge** that doesn't close the problem (P≠NP's EF route evading natural proofs), and **the rest share RH's single wall**. That is a defensible, honest map of the hardest problems in mathematics — an attempt that respects its walls, which is the only kind worth publishing beside real work. No proof is claimed. The Clay problems remain open.

— Keeper, 2026-08-16. Internal. Barriers confirmed (Razborov–Rudich, Aaronson–Wigderson, Tao 2016, Atiyah–Hirzebruch 1962, Elkies 2006, Schaefer 1978, Dokchitser parity). Nothing pushed. CP existence-only.
