# K1847 — E0 (the cap) and a pre-read of E3 (T33): what the corpus already holds, verbatim-sourced
**2026-09-02 Wednesday, 13:05 EDT (clock-verified). Keeper. Round 106. DISCUSSION-tier investigation, not a gate. Casey's directive: don't gate, investigate; reconnect to the corpus; linear algebra on D_IV⁵.**

## 0. Verdicts up front

| Question | Answer | Source |
|---|---|---|
| Does a finite, frame-invariant commitment-count functional exist? | **YES — it is already registered.** The causal-set NUMBER: commitment count N = Casimir energy = the volume measure (T2564, "Order + Number = Geometry"); its variance is area-law (T2570); frame-invariance is the causal-set construction itself (number = volume, label-independent). | Registry 11228, 11237; `BST_paper_Causal_Set_Formulation_from_D_IV5_2026-08-14.md:108,173` |
| Does a cap exist? | **YES.** The de Sitter horizon capacity S_dS = 3π/Λ (Bekenstein–Hawking, T196/T2114). | Registry 283, 2835 |
| Is the cap's VALUE as a fraction, f = 3/(5π), derived? | **NO. Identified, not derived.** T189 states f = N_total/S_dS = N_c/(n_C π) at depth 0; the spectral derivation is explicitly open: "Strong physical motivation, not yet a proof" / "Plausible but uncomputed." | `BST_RealityBudget_SpectralProof.md:5, 53-70, 210-212, 320-330` |
| Is T633 the E0 statement? | **NO.** T633's "complexity" is the D0-fraction of the THEOREM GRAPH (via T480), rising toward f per interstasis cycle. It is not a commitment-count functional on the sequential growth. | `BST_AC_Theorems.md:12276-12286` |
| Does "entropy as meter of commitments" reduce to T33's charge? | **NOT a reduction — a SHAPE MATCH worth formalizing.** See Section 2. | `BST_AC_Theorems.md:1488-1502` |
| Is T33 the ∞ rung as proved? | **Pre-read says (ii), with a sharper (ii′).** Cal rules. See Section 3. | `BST_AC_Theorems.md:1502, 1512-1536, 1568-1572` |

## 1. E0 — the honest shape of the kill test

The 09-01 kill test read: "derive the cap from D_IV⁵ counting; it must equal the 19.1% observer bound." The corpus shows both sides are the SAME number by construction: T318's α_CI ≤ f cites T189's f, and T189's f is the measured ratio N_total/S_dS = 6.209×10¹²¹ / (3π/Λ), matched to N_c/(n_C π). So "cap = 19.1%" cannot currently fail: it is one identification quoted twice. The kill test as written is EMPTY (feedback: construction-guaranteed confirmation proves nothing).

**Reshaped, so it can fail:** the lane's first derivable cell is the Reality Budget's open problem in its commitment form — *derive f = (committed contacts)/(horizon capacity) = N_c/(n_C π) from D_IV⁵ spectral data.* The corpus already names the route (Plancherel measure on D_IV⁵, `BST_RealityBudget_SpectralProof.md` Section 5.4) and the candidate decomposition (N_c color channels / n_C total channels × 1/π from the S¹ circumference in Bergman coordinates — "dimensional reasoning, not a proof"). This is a rank/measure computation on one operator, which is exactly the form Casey's standing order asks for. It has been open since the spectral-proof note was written; the lane does not create it, it inherits it with a stated route and a numerical target already in hand — target-innocence is therefore NOT available here (the number is known), so the derivation must be blind on the coefficient: post the procedure, not the answer.

**What the meter is, in corpus terms:** the meter is N(t)/S_dS — the causal-set count in the observable region against the horizon capacity — rising toward f. Casey's "never overcome, conserved with a limit" is literally: N(t) is monotone (commitments are irreversible, T2564's growth), S_dS is the constant, f is where the meter reads at the cycle's last commitment. **The cap is the conserved object (Noether-shaped); the meter is not.** This is the 09-01 subscript, now with registry addresses.

## 2. Casey's entropy sentence has T33's exact SHAPE — the bridge to formalize

T33 as proved: Q(φ) = Σᵢ H(Cᵢ) − H(C₁ ∧ … ∧ C_m) = m·log₂(8/7) − log₂|sol(φ)|.

Read it in Casey's words: Σᵢ H(Cᵢ) is *the work put into commitments* (each clause commits log₂(8/7) Shannons); log₂|sol| is *the freedom remaining*; Q is their difference — total correlation, the information the constraints have jointly committed. That is "entropy is a measure of the work the universe puts into commitments," with the constraints as the commitments. The cap in T33's frame: satisfiability ⟹ |sol| ≥ 1 ⟹ Q ≤ Σᵢ H(Cᵢ) = m·log₂(8/7); the charge cannot exceed the work; equality is the fully-committed instance (one solution). So T33 carries the cap-and-meter structure internally: **meter = Σ H(Cᵢ) (monotone in m), cap = the point where log|sol| → 0, charge = the difference.**

**What is NOT there:** T33 is a theorem about random 3-SAT clauses, not about D_IV⁵ commitments; "per-commitment cost" is log₂(8/7) because a 3-clause excludes 1/8 of assignments, and nothing in the corpus says what a D_IV⁵ commitment excludes. **Existence check for Lyra (tomorrow, after the paper gate):** define Q on the causal set as (per-commitment information summed) − (joint), with the per-commitment term read from the substrate (candidate: the c-function in K1293, c(t) = 137 − N(t) floored at C₂ = 6 — the count of un-committed eigentones); ask whether Q so defined is the causal-set number N up to the constant, or something new. If it is N, "new definition of entropy" is a RENAME of T2564 — say so. If it is not, it is the lane's second object.

## 3. E3 pre-read (for Cal — his ruling stands, mine does not)

Verbatim, T33's non-localizability corollary (`BST_AC_Theorems.md:1502`): "The per-clause charges qᵢ … satisfy E[qᵢ] = Q/m = O(1) by exchangeability … No single clause carries Θ(n) charge." Strengthened in T35 Component 2 (`:1568-1572`): "the charge in any subset S ⊂ [m] with |S| = o(m) satisfies Σ_{i∈S} qᵢ = o(Q) w.h.p." (Azuma–Hoeffding). Isotropy (`:1504`): "Unit propagation from any single forced variable extracts exactly zero bits (Toy 290: isotropy = 1.000)." And T34 / Toy 291 (`:1512-1536`): every probe stronger than UP has isotropy < 1 and **bits(P)/n → 0 as n → ∞**.

So what is proved is: (ii′) *no o(m)-sized subset of the constraints carries a non-vanishing fraction of the charge, and no fixed probe extracts a non-vanishing fraction per direction.* That is a locality statement about SUBSETS and PROBES, not about LIFTS. The rung's sentence — "no finite set of global coordinates makes a local rule sufficient" — is not in Section 38. Two honest options for Cal: rule (ii′) and demote the ∞ rung's anchor to a candidate with T34(c) as its strongest evidence; or find that "probe" and "lift" coincide under a definition the corpus already has (a lift = a finite set of global coordinates; a probe = a bounded-depth extraction procedure — these are different objects, and a bounded-depth rule with k global inputs is not any of the five probes in Toy 291). **POSITION vs VALUE:** Θ(n) in T33(b) is a position (0.622n from Ding–Sly–Sun / Achlioptas–Peres, not tunable); the 0.193 per clause is a value fixed by the clause arity. Neither is a coordinate.

## 4. A registry collision, found in passing (Grace's lane)

`BST_AC_Theorem_Registry.md:603` (depth-1 census): T633 = Asymptotic Complexity. `:1472`: **T617 = Asymptotic Complexity Theorem.** `:1488`: **T633 = Complexity Ratchet.** Three rows, two IDs, two names, one object or two — the name↔object map read both ways (feedback: collisions and search-misses are one map). Not blocking anything today; flag for the DM-registry pass tomorrow rather than a new lane.

## 5. What moves to the machine, and what does not

- **Moves (as a pre-registered cell, after the paper gate):** the Reality Budget derivation in commitment form (Section 1), blind on the coefficient. Owner: Lyra derives, Grace instruments the Plancherel/Bergman measure, Cal pre-scores what number kills it (any f ≠ N_c/(n_C π) to the stated precision, or a derivation that must input Λ or N_total).
- **Moves as an existence check:** Q on the causal set (Section 2), Lyra.
- **Does not move:** "entropy is conserved with a limit" as a sentence — it is now three registered objects (N, S_dS, f) and one open derivation; the sentence is the lane's summary, not its theorem. Naming stays Casey's.

**Calibration note on myself:** E0 was assigned to me as "a question only"; the answer is that the question was already answered piecewise in three registry rows and one open note, and my 09-01 kill test was empty. Two hours of grep would have found this on 09-01. Filed.

— Keeper

---
## AMENDMENT A (13:15 by the clock, same hour) — two corrections to this note; no new K-number

**A1. "Identified, not derived" quoted a SUPERSEDED status.** `BST_RealityBudget_SpectralProof.md` is dated March 13 and says the spectral derivation is open. `BST_EffectiveSpectralDimension.md` Section 4.2 is dated **March 16**, status "Proved," and gives a derivation:
f = (d_eff^zonal / d_eff^full) / Vol(S¹/ℤ₂) = (6/10)/π = 3/(5π). (Feedback: "still open" is dated — read the next artifact. I did not.)
Cold read of that derivation, three steps: **(1) computation** — the zonal (q = 0) sector of Q⁵ has N(λ) ~ λ³ (multiplicity ~ k⁵/60 against λ_k = k(k+5)), so d_eff^zonal = 6, while the full spectrum obeys Weyl's λ⁵, d_eff^full = 10; ratio 3/5. Auditable; family-sweeps as (n+1)/(2n) on Qⁿ, equal to N_c/n_C ONLY at n = 5 — so "= N_c/n_C" is a name attached at n = 5, the number 3/5 is forced by the sector. **(2) posit** — "committed modes = zonal modes" (both polydisk coordinates phase-locked). An identification, not a derivation. **(3) posit** — divide the dimensionless ratio by the Shilov circle's circumference π. A normalization step on a dimensionless number, stated, not derived; this is the last prose step, where the cheat migrates. **Honest tier for f: PARTIALLY DERIVED in the explicit-split form — the 3/5 forced (given posit 2), the 1/π asserted.** No K-audit or Cal referee of Section 4.2 exists that I can find (grep "zonal" across Keeper_K*/Cal_* returns unrelated files); T668 (registry :638) is an Integer-Hub graph node, not a derivation.
**The reshaped first machine cell, now precise:** derive or kill posits (2) and (3). Kill for (3): exhibit the normalization from the partition function or the Plancherel measure (the March-13 note's Section 5.4 route) and show it is 1/π and not 1/(2π) or 1; any other value falsifies the match to N_total/S_dS. Kill for (2): a different, equally natural "committed" sector (e.g., the (p,p) diagonal, or the lowest K-type in each (p,q)) with a different d_eff. Blind on the coefficient: post the procedure before the number.

**A2. The T33 bridge in Section 2 is WITHDRAWN as a bridge (Cal §826 row (b)).** T33's Q mixes a surprisal (H(Cᵢ) = −log₂ P(Cᵢ)) with a log-count (H(∧Cᵢ) = log₂|sol|); under one convention the object is log₂(|sol|/E|sol|), the quenched–annealed gap, which is negative at α = 2 (measured −0.229) and ranks 3-XORSAT above 3-SAT. Any "entropy as meter of commitments" identified with Q inherits both. Convention-collision before contradiction: the SHAPE I noted (work into commitments minus remaining freedom) survives only as a definition to be built under ONE convention on the causal set, and it is not owed to T33. **The meter candidate that stands is Section 1's N/S_dS — a count against a capacity — which is non-negative and hardness-blind by design (it measures commitment, not difficulty).** Lyra's existence check in Section 2 is re-stated: define the causal-set Q under one convention; ask if it is N up to a constant. Nothing else in Section 2 is kept.

**Calibration:** two errors in one note, both of the "quoted from memory of the corpus" kind — a superseded status and a functional I had not read cold. Cal's blind sweep caught the second within the hour. — Keeper
