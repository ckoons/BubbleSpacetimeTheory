# Grace R165 — STAGED for Cal's hash: register row A14 (T_bb, option B), row E8 (the "19 only with colour" prediction, falsified), and registry pointer row T2632 (the Cayley transform)
*2026-09-26, round 6 items 2–3. Nothing below is in the register or registry until Cal hashes this file and rules. Invariants are stated before any number. One edit was applied without a hash because it changes no claim: T1947's mis-pointer (see Section 4).*

## Section 1 — A14 (Section A, live): the T_bb test for the proximity rule (Casey: option B, provisional, K1928 Addendum 11:38)
| # | falsifier | BST claim (provenance) | current bound | kill-condition | owner |
|---|---|---|---|---|---|
| A14 | **A deeply bound, weak-only doubly-bottom tetraquark T_bb (bb ū d̄, J^P = 1⁺)** | **Invariant:** the signed offset δ = M − M_threshold to the nearest two-hadron threshold, a mass difference in one theory, the same in every scheme. **Claim (option B; K1925 Addenda 3–4; K1928 Addendum 11:38):** observed exotics sit AT their two-hadron thresholds, on both sides — a "window" at the Šilov boundary (Casey: a winding that falls short of closure or overshoots it). **BST registers NO bet against lattice QCD** (BST's colour sector is QCD's, so lattice QCD computes BST's own QCD; K1928 Part 1 item 7). T_bb is named as the discriminating test of whether the window is a scale of its own. | **Observed (Grace R164, toy 5802):** 14/14 thresholded exotics have \|δ\| ≤ 30 MeV, 7 below and 7 above. X(3872) sign unsettled (−0.06 BW / +0.01 pole). X(6900) has no natural threshold (+704 above di-J/ψ) — outside the rule's scope, stated. **T_bb:** ten lattice calculations, all bound. 2023–2026: −74(17)(10) Hoffmann–Meinel 2026 to −116 Tripathy+ 2025; 2017–2020: −128 to −189. "can decay only via the weak interaction" (Colquhoun+ 2024). Not observed; no dedicated search found (PIN OWED). | **The window dies as a scale of its own if** T_bb is observed with \|δ\| ≥ 50 MeV below B B* (weak-decay-only). That is \|δ\| tracking the reduced mass as QCD predicts, so the window adds nothing beyond QCD (Keeper's kill, Addendum 1). **Lattice QCD (hence BST's own QCD) is in trouble if** a search with sensitivity to the lattice-predicted yield finds no weak-decaying T_bb, OR finds it only within 30 MeV of threshold. That is the one outcome where the window says something QCD does not. **Unit frozen before re-reading the table (Elie freezes, Cal hashes): pending.** | Casey (option), Grace (row), Lyra/Cal (window scale); register before LHCb Upgrade II |

## Section 2 — E8 (Section E, fired and lost): "19 appears only when colour is added"
| # | what fired | what DIED | what SURVIVED | numbers + certification |
|---|---|---|---|---|
| E8 | **The colour-only-19 prediction** (K1926 Addendum, 09-25 19:17: "19 only where colour is present"; first look 3/3 coloured) | **"19 only in coloured quantities" — FALSIFIED as stated.** Invariant: the prediction is a claim about a CLASS (every corpus formula whose denominator or count is 19 carries colour). One colourless member kills it. | 19 = 16 + 3 and 19 = 3³ − 2³ stay as arithmetic readings. The shared denominator of 13 + 6 (Ω_Λ, Ω_m) and 16 + 3 goes into the menu count, NOT into support (K1928 Part 1 item 2). | **T192:** Ω_Λ = 13/19, Ω_m = 6/19 (registry, BST Five Integers batch) — a colourless 19. Found by Lyra R5 (b1b8905e); ruled Cal Section 990; Keeper's "first look 3/3" withdrawn (K1926 amended); K1928 Part 1 item 2. Elie 5799: the 19-scan kill fired, 1/3. |

## Section 3 — T2632 (registry pointer row, NOT a new theorem): the Cayley transform
**Why a row:** the registry has 0 rows naming the Cayley transform (K1928 Part 4), yet F222, F475 and T2625 all use it.

**Invariant first (the reason this row must be careful):**
- The conjugacy type of a one-parameter subgroup (elliptic, parabolic, hyperbolic) is preserved by EVERY automorphism of so(5,2).
- The Cayley transform relates two REALIZATIONS of the same group action:
  - the bounded domain D_IV⁵, whose Šilov boundary is (S⁴ × S¹)/ℤ₂;
  - the tube T_Ω = ℝ^{1,4} + iΩ, whose Šilov boundary is ℝ^{1,4}, compactified.
- So it cannot carry the elliptic clock J to the parabolic P₀. **Under it, J (the generator of rotations about the base point, the centre of K) becomes the generator fixing the tube's base point i e: the conformal Hamiltonian ½(P₀ + K₀), still elliptic.**
- P₀ is a different, parabolic element of the same sl(2,ℝ) (K1928 Part 3).
- The boundary relation between their parameters is t = tan(τ/2) (F222): the two times are related by a coordinate map on the boundary, not by conjugation.
- **This corrects one phrase in round 6's Lyra item 2** ("the Cayley transform as the operator that carries J to P₀"): there is no such operator. The bridge from interior to boundary is a change of generator within one sl(2,ℝ) (elliptic → parabolic, which is a tilt or contraction, not a conjugation). The Cayley transform supplies only the picture in which both generators act on ℝ^{1,4}.
- **F475's "Cayley = Wick" is loose:** Wick rotation is an analytic continuation t → −iτ in one time; Cayley maps one realization onto another. Pin owed on which F475 means (Lyra).

**Row text (pointer):**
> T2632 | CAYLEY TRANSFORM — POINTER ROW (no new claim). The Cayley transform maps the bounded realization D_IV⁵ onto the tube ℝ^{1,4} + iΩ (standard; Faraut–Korányi, as already pinned for T2625). It maps the Šilov boundary (S⁴×S¹)/ℤ₂ onto compactified ℝ^{1,4}. It sends the centre of K (the clock J, elliptic) to the conformal Hamiltonian ½(P₀+K₀) (elliptic; Lüscher–Mack 1975 convention, pin landing). It is NOT a map J → P₀: conjugacy type is invariant. Users: F222 (two times, t = tan(τ/2)), F475 (tower 21 → 15 → 6; "Cayley = Wick", loose), T2625 (three sectors on the tube picture), K1928 Part 3 (one sl(2,ℝ), three types). | Pointer | — | 2026-09-26

## Section 4 — Applied without a hash (no claim changes)
- **T1947 re-key:** "(T1939)" is a mis-pointer. The 6 = 21 − 15 is the vector representation ℝ^{4,2} (dim so(p+1,q) − dim so(p,q) = p + q). Its equality with C₂ = 6 is numerical. The pointer now goes to F475 and K1927. There is no graph edge T1939 → T1947, so no edge moves.
- A2 and 16/3 wording per K1928 Part 1 items 5–6 lands with Cal's final word (register v0.28).
