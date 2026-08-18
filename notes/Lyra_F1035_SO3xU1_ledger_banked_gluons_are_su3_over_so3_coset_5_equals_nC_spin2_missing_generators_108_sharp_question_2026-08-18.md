# F1035 — The SO(3)×U(1) color ledger, banked: the isometry reaches the so(3) ⊂ su(3) subalgebra (3 gluons, spin-1); the missing gluons are the su(3)/so(3) coset — exactly 5 = n_C generators (spin-2 of the color-SO(3)). The 5 = n_C hook flagged. #108's sharp question: how are the 5 coset generators added? (T1930 triple-cover / the 5=n_C geometric identification are the candidates.)

**Lyra + Grace, Tuesday 2026-08-18, Round 4. Banking the SO(3)×U(1) ledger (F1033/F1034 decided the isometry is SO(3)×U(1), three ways). Reconnected: F1033/F1034, T1930 (triple-cover), Lyra_BulkColor_v0.6 (prior Toeplitz su(3) attempt), F531/F66 (bulk/boundary coset). LA on D_IV⁵. Nothing pushed; CP existence-only.**

## The ledger — banked (group theory, solid)
The isometry K = SO(5)×SO(2) realizes **SO(3) × U(1)** on the color-3 (V₁₂)_ℂ (F1033 real-type; F1034 invariant symmetric form; K1659 SU(3)⊄SO(5) — three independent proofs). Now place that inside the physical gauge group SU(3):

- **SO(3) ⊂ SU(3)** is the *real* (principal for the vector-3) subgroup: the 3-dim so(3) subalgebra. **These 3 gluon-directions ARE reached by the isometry.**
- **U(1)** is the SO(2)-center phase — the **trace** u(1) (overall phase), *not* a gluon: su(3) is traceless, so the U(1) is baryon-number-like, outside su(3). (This is why the isometry group is SO(3)×U(1), not a subgroup of SU(3) alone.)
- **The gap** is the coset **su(3)/so(3)**, and its dimension is exact:
$$\dim\mathfrak{su}(3) - \dim\mathfrak{so}(3) = 8 - 3 = \mathbf{5}.$$
Under the color-SO(3), the adjoint decomposes **8 = 3 ⊕ 5**: the **3** is so(3) (spin-1, reached), the **5** is the coset (the **symmetric traceless spin-2** of SO(3), *not* reached). SU(3)/SO(3) is the rank-2, 5-dimensional symmetric space (Cartan type AI, n=3).

> **The banked statement:** of SU(3)'s 8 gluons, the D_IV⁵ isometry reaches **3** (the so(3), as spin-1); **the missing 5 gluon-generators are the su(3)/so(3) coset — a spin-2 of the color-SO(3).** SU(3) is the gauge completion of SO(3)×U(1) by these 5 (#108). This is *why* SU(3) is not an isometry: the isometry stops at SO(3)×U(1), and the completion is a definite, named 5-dimensional coset.

## The 5 = n_C hook — flagged (candidate, not banked)
The number of missing gluon-generators is **5 = n_C** — the same integer as the domain's complex dimension and its Shilov boundary's real dimension (S⁴×S¹/ℤ₂, dim 5). Sharper: **SU(3)/SO(3) is rank-2 and dimension-5** — the *same rank and same dimension* as D_IV⁵'s boundary. This is a genuine coincidence-or-content flag (Casey's "no wave-through on a perfect number" — 5 = n_C could be a numerical accident or a structural map). **Tier: hook, not banked.** The test is whether there is a *forced map* from the domain's 5 (holomorphic tangent / boundary) to the coset's 5 (spin-2 of color-SO(3)) — an exhibited intertwiner, not a shared integer (the F1033/F1034 discipline: real-3 ≠ complex-3 shares only the number; likewise here, don't count 5=n_C as content until a map is exhibited).

## #108 — the sharp question, now stated precisely
Previously #108 was "where does SU(3) live?" — vague. The ledger sharpens it to a definite question:

> **#108 (sharp): how are the 5 = n_C coset generators (the spin-2 of the color-SO(3)) added to SO(3)×U(1) to complete SU(3)?**

Candidates, tiered:
1. **T1930 triple-cover / ℤ₃ sub-substrate** (the standing candidate): SU(3)'s ℤ₃ center is the thirds/confinement grading; a triple-cover / ℤ₃ sub-substrate is where the *center* lives. But note honestly: a **ℤ₃ (discrete) does not supply 5 continuous coset generators** — so the triple-cover, if it works, explains the *center* (ℤ₃) and confinement, **not** the 5-dim coset completion. These are two different pieces (discrete center vs continuous coset); do not conflate.
2. **The 5 = n_C geometric identification** (the hook above): if the domain's 5 (tangent/boundary) maps to the coset's 5 (spin-2), the completion is geometric. Requires the forced intertwiner — open.
3. **The Toeplitz construction** (Lyra_BulkColor_v0.6, prior, unclosed): 8 = 3 T_a + 3 T_a^† + 2 Cartan, SO(3)-vector Toeplitz operators. This is a candidate *realization* of su(3) on the bulk — its closure (verifying the su(3) commutators) is the multi-week check that would decide whether the 5 coset generators are the T_a/T_a^† off-diagonal content. Reconnect there before rebuilding.

**Honest floor:** the ledger (SO(3)×U(1) reached; 5=n_C-dim coset missing, spin-2) is banked. The completion mechanism (#108) is **open with three candidates**; none is ratified, and the discrete-center (ℤ₃) route explicitly does *not* by itself supply the continuous 5. The number 5=n_C is a hook, not a proof.

## RUBRICS Layer-2 done-bar
- [x] Reconnected before deriving (F1033/F1034, T1930, BulkColor v0.6, F66/F531). Cited the prior Toeplitz attempt rather than rebuilding.
- [x] Banked at tier: SO(3)×U(1) reached + 8=3⊕5 coset (group theory, solid); separated the U(1)=trace (not a gluon) cleanly.
- [x] Flagged 5=n_C as a HOOK not content (shared integer ≠ forced map — the F1033/F1034 discipline applied to numbers again).
- [x] Sharpened #108 to a definite question; tiered the three candidates; flagged the ℤ₃-doesn't-supply-5 honesty (discrete center ≠ continuous coset).
- [x] Did not ratify a completion; the gauge-emergence box stays open.

## Handoffs
- **@Grace** — the ledger is ours jointly; the data-layer entry should read: *isometry reaches SO(3)×U(1); the 8 gluons split 3⊕5 under color-SO(3); the missing 5 = su(3)/so(3) coset = spin-2 = n_C-dimensional; SU(3) = gauge completion (#108, open).* Cross-check my 8=3⊕5 branching (SO(3)⊂SU(3) principal-for-vector, coset = symmetric traceless spin-2) — it's textbook but worth your independent confirmation. And log the 5=n_C hook as candidate-structural, not banked.
- **@Elie** — if the Möbius C4 test frees you: the BulkColor v0.6 Toeplitz su(3) closure (do the 3 T_a + 3 T_a^† + 2 Cartan satisfy su(3) commutators, and is the off-diagonal content the spin-2 coset?) is the computational form of #108 candidate 3. Not asking now; flagging it's the tractable one.
- **@Keeper** — banking request: SO(3)×U(1) ledger + 8=3⊕5 coset (group theory) as **banked**; 5=n_C as **hook**; #108 sharpened with three tiered candidates, none ratified. The color piece ships with this ledger as its honest structure.
- **@Casey** — the color picture, now with a clean ledger. The geometry gives us three colors organized as an ordinary SO(3) (they have a length and angles — F1034). Physics needs the bigger SU(3), whose eight gluons split, under that SO(3), into 3 that the geometry already reaches and **5 that it doesn't** — and that 5 is exactly n_C, the domain's own dimension. That last fact is either a beautiful accident or the door to how the gluons get added, and we've flagged it as a *hook* to test, not a win to claim — because a shared number isn't a proof until we exhibit the map (the same lesson the SU(3)/SO(3) question just taught us). The honest state: three colors forced and organized (banked); five gluons missing with a tantalizing 5=n_C address (open, #108).

Notes only; no theorem/toy claimed (ledger-bank + hook-flag + #108 sharpening). F1035: isometry reaches SO(3)×U(1) (F1033/F1034 ×3); of 8 gluons, 3 = so(3) reached (spin-1), U(1)=trace (not a gluon), **missing = su(3)/so(3) coset = 8−3 = 5 = n_C = spin-2 of color-SO(3)** (SU(3)/SO(3) = rank-2 dim-5 symmetric space AI). 5=n_C HOOK (SU(3)/SO(3) rank-2 dim-5 = boundary rank-2 dim-5) — candidate, needs a forced map not a shared integer. #108 sharp: how are the 5 coset generators added? Candidates: (1) T1930 triple-cover/ℤ₃ — but ℤ₃ discrete ≠ 5 continuous (explains center/confinement, NOT the coset); (2) 5=n_C geometric map (open); (3) BulkColor v0.6 Toeplitz su(3) closure (Elie, tractable). None ratified; ledger banked, completion open. — Lyra
