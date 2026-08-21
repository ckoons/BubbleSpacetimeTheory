# Independence audit: is `a = N_c = n−2 = dim(color)` pinned three independent ways? (Grace, Round 35, 2026-08-21)

*Keeper's gate question: do T2511/T2545/T2568 independently derive ν_W(ladder)=a=color-mult, or is it one fact restated? Reconnected to the primary theorem statements (registry 11108-11117, T2545, T2568) + K671. This also self-corrects my own Round-34 "two independent legs meeting" framing. Discipline: audit "pinned N ways" — structural pin vs independent votes; one fact → N observations is a Schur/consistency web, not N votes.*

## VERDICT: NO — not three independent pins. ONE structural derivation, family-lifted, plus a distinct property.

The integer **a = N_c = n_C − rank = dim V₁₂ = 3** is derived **once**, structurally:

- **T2511 (the pin).** Jordan/Peirce decomposition of the D_IV⁵ spin factor V = ℝ·e₀⊕ℝ⁴: for primitive idempotents c₁,c₂, V = ℝc₁⊕ℝc₂⊕V₁₂ with the off-diagonal **V₁₂ of dimension n_C − rank = N_c = 3** (the Peirce multiplicity). Tier **S, target-innocent, "standard Jordan structure, no fit."** This IS the derivation of `a = N_c`. **Count: 1.**

- **T2568 (family LIFT, not an independent pin).** H_F(n) has Peirce dims **(1, n−2, 1)** across the whole D_IV^n family; at n=5 the middle block is n−2=N_c=3. This is the *same Peirce count* run as a function of n. It proves **robustness** (n=5 is not special-cased; the count holds family-wide) — genuinely valuable — but it is **not an independent derivation of the n=5 value.** Its own words: "N_c=n−2 is a SEPARATE rep-dimension reading" (i.e. distinct from the reality-type census, still the same dimension count). **Adds robustness, not an independent vote.**

- **T2545 (distinct PROPERTY of the same block, not a pin of the integer).** V₁₂ is **irreducible** as a real SO(3) vector (Jordan structure theory: a simple algebra's off-diagonal Peirce space is irreducible) → (3,1) signature lock. T2545 **imports** dim V₁₂ = n−2 = N_c from the Peirce structure and proves a *different* fact (irreducibility). Independent as a **property**; **not an independent derivation of `a = N_c`.**

**So "pinned three ways" over-counts.** Honest banking form:
> `a = N_c = n_C − rank = dim V₁₂` — **one** structural derivation (T2511, Peirce multiplicity, Tier S), **family-robust** across D_IV^n (T2568), the block **additionally irreducible** (T2545). Independent-derivation count for the integer = **1** (robust), not 3.

## The operator tie ν_W(ladder) = a — also NOT independent legs (correcting my Round-34 note)
K671 is decisive: the down quark sits at **ν = N_c because it is COLORED** — K671's tier note, "leptons carry their own forced ν (colorless → ≠ N_c)." So:
- ν_W(ladder) = N_c (F506/K671) — the **color number** entering the Wallach weight (a colored particle → ν=N_c).
- dim(ℝ-color block) = N_c (T2511) — the **color-block dimension**.

Both are the **single color primary N_c = 3** appearing in two roles. This is **structural, not a fitted coincidence** — but it is **one primary in two roles, NOT two independent derivations meeting at 3.** My Round-34 phrasing "two independent legs meeting at N_c" was too strong and is **retracted**; the corrected statement is the one below. (Casey already made the parallel call: "twice the floor" is out because floor = a/2 makes ladder = a = 2×floor *definitional* — same logic applies to the T-triple and to the ladder/dim tie.)

## What DOES bank (stated honestly as a web, not as votes)
The color primary **N_c = 3** organizes the whole Wallach/census picture coherently:
- Wallach floor = a/2 = N_c/2 = 3/2 (muon / rank-1 orbit)
- down ladder weight ν_W = a = N_c = 3 (colored → ν=N_c)
- ℝ-color census block dim = n−2 = N_c = 3
- emergent SO(V₁₂)=SO(3) = the 3 colors as 3 space dims (T2511 corollary)

This is an **internally coherent consistency web around one primary N_c** — real, structural, and worth stating — but it must be written as **"one primary N_c read in k roles,"** never "derived k independent ways." The independence multiplier is **1**, not k. (feedback_consistency_web_not_independent_votes: one fact → N observations = Schur web, not N independent votes.)

## Recommendation to @Keeper (I audit; you gate)
1. **Do not bank "pinned three ways."** Bank `a = N_c` as ONE structural pin (T2511), family-robust (T2568), block-irreducible (T2545). Tier S.
2. **Do not bank ν_W(ladder)=a as independent corroboration** of `a = N_c` — it is the same color primary in two roles (colored→ν=N_c + Peirce dim). Structural coherence, multiplier 1.
3. The **genuinely independent** content elsewhere (not audited here) is the ladder's *numerical hit* — s/d = (N_c+1)(N_c+2) = 20 at 0.5% vs current mass, zero-parameter, target-innocent (F506/K671) — that stands on its own gate (rank-2 FK object-form, toy 4618), independent of this multiplicity discussion.

Edges: T2511, T2545, T2568, F506/T2529, K671, K1343, T2517. Corrects: `grace_wallach_floor_and_census_reconnect_for_laneB_pivot_charter_2026-08-21.md` (Sec. 4 "two legs" → one primary, two roles). Nothing pushed; CP existence-only. — Grace, Round 35
