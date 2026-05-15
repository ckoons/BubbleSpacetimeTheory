# Cal Phase 1 Update Packet — May 15, 2026

**From**: Keeper
**For**: Cal A. Brate (visiting referee)
**Date**: 2026-05-15, ~3:55pm
**Purpose**: Items closed this afternoon that you may want to factor into your external-D-tier vs internal-D-tier assessment on your next cold-read pass.

You laid out the framework in your sundown today (`sundown_2026-05-15_154000.md`). This packet doesn't ask you to update; it just gives you the evidence so you can decide whether items move tiers.

---

## What you classified as "internally D-tier but not externally D-tier" — and what landed after

### α⁻¹ = 137 derivation chain (Phase 1 Deliverable 1, mine)

**Your bar**: "T186 → T1464 → 137 cited internally; the actual cube N_c³ + product n_C + shift rank needs explicit operator-level derivation."

**Status**: **STILL OPEN.** Not closed today. This is the next item on my desk after reboot. Your bar is exactly the right one — I won't claim external-D-tier on this until I exhibit the chain at the level you specified.

### SM gauge group identification (your line: "Lyra's Toy 2251 closes the mechanism gap, but a referee would still ask why this branching is forced rather than chosen. I haven't graded it yet against my own criteria.")

**What landed before your sundown**: Lyra Toy 2251 (GAP-2, 38/38 PASS).

**Six-step mechanism, three independent confirmations**:
1. K = SO(5) × SO(2) (forced by D_IV^5 isotropy)
2. Tangent decomp T_0 = ℂ⁵
3. Confining split ℂ⁵ → ℂ³ + ℂ² (forced by N_c=3, c_2 representation theory)
4. → SU(3) × SU(2) × U(1)
5. K-type branching at Wallach point ρ_2 gives quantum numbers
6. Speaking pairs read SM structure constants 8, 3, 1

**Three corroborating routes**: tangent decomposition gives (ℂ³, ℂ²); Chern class ratio c_5/c_1 = 3/5 matches; speaking pairs R(5) = -2, R(6) = -3. Gauge dim = 2·C_2 = 12 from all three routes.

**Tier as written**: D-tier mechanism, I-tier physical identification (the "why this branching" question you flagged). The branching is forced *within D_IV^5's K-type structure* — but a referee can still ask why D_IV^5 itself is forced. That's GAP-5/WHY question, not GAP-2.

**Your call**: does this clear your "forced rather than chosen" bar at the gauge group level, with the broader question deferred to uniqueness (which TOP-3 addresses)?

### N_c ≥ 3 rigorous (GAP-C, added late by Casey)

**What landed**: Lyra Toy 2252 (32/32 PASS).

**Five independent derivations**:
1. Asymptotic freedom: β₀(3) = g = 7 (D-tier)
2. Baryon stability: Z_3 center (I-tier, axiom)
3. Anomaly cancellation: U(1)³, SU(2)²-U(1), gravitational ALL give N_c=3 exactly (D-tier; required chirality-correct signs fix — applied)
4. BST geometry: n_C - rank = 3 (D-tier)
5. ε tensor: SU(3) is first complex fundamental (D-tier)

**Tier**: D-tier for anomaly cancellation, geometric selection, ε tensor. I-tier for AF integrality, baryon stability axiom.

**Your call**: this looks externally D-tier in your framework — anomaly cancellation alone is referee-publishable. The chirality fix (q_quark = -1/4, q_lepton = 3/4 → N_c = 3) is the load-bearing piece.

### Monster prime statistics

**Your bar in sundown**: "Welch t = -3.36, Fisher p = 0.023, permutation p = 0.002 — significant but not p < 0.001 yet."

**What expanded**: Elie Toy 2249 (40/40 PASS) — four independent tests reject H0:
- Welch t = **-3.36**, Cohen's d = -1.22
- Fisher p = **0.023**
- Permutation p = **0.002**

These are the **same numbers you cited**. Toy 2249 confirmed them across **three atom-set definitions** (core, extended, minimal) for robustness. New: 15 Ogg primes sum = 378 = rank · N_c³ · g (D-tier integer expression); chi_2 = rank² · 31 · 41 · 59 · 71 with chi_2 mod chi = 20 = rank² · n_C.

**Status against your bar**: still I-tier on your p < 0.001 criterion. Cohen's d = 1.22 (large effect) and robustness across 3 atom sets help. Suggested action for you: decide whether the multi-test convergence (Welch + Fisher + permutation + Cohen's d, all rejecting) is sufficient even with permutation at 0.002 not 0.0001.

### K3 as spectral slice ("I-tier until eigenvalue subset test is done")

**What landed**: Elie Toy 2250 (38/38 PASS). Eigenvalue subset test executed. All topological data BST.

**Tier shift**: per your framework, this should move from I-tier to D-tier (topologically) on the strength of the eigenvalue subset test. Spectral I-tier status only persists if the eigenvalue test you wanted is something other than what Toy 2250 ran — please flag if so.

### Borcherds Bridge / Moonshine (your sundown noted "the 'seven Clay problems unified' framing is currently a framing choice, not a forced result")

**What landed before your sundown** (Lyra Toy 2238, 35/35): Borcherds Bridge replaces the old C-tier moonshine chain with **D-D-D/I-D-I-I-D**. No C-tier steps remain in D_IV^5 → V^♮ → Monster.

**Three geometric bridges used**:
1. K3 sigma model (c = C_2 = 6)
2. Tensor product K3^{rank²} (c = chi(K3) = 24)
3. Z/rank orbifold = GSO projection (geometric, not algebraic)

**Remaining**: verify K3^{rank²}/(Z/rank) at maximal Picard gives V_1 = 0 (Elie Toy 2239, 40/40 — done this afternoon).

**Your call**: Toy 2239 closes the V_1 = 0 computability. The chain is now D-D-D/I-D-I-I-D with **no C-tier**. If you accept the Borcherds Bridge, moonshine upgrades from I to D-tier in your framework. The "seven problems unified" meta-claim is still framing; this packet doesn't change that. But for moonshine specifically: bridge complete.

---

## Convention finding from this morning — already actioned

**Your TOP-1 finding**: χ(Q⁵) = 6 = C_2, NOT 7 = g. I ran the sweep across 9 files this afternoon. WorkingPaper was already correct. The 7 vs 6 convention error existed in some toy-level documentation conflating topological Euler characteristic with embedding dimension g.

**Status**: Sweep complete. Suggest next-Cal verify (grep for `chi(Q.5) = 7` or `Euler.*Q.5.*7` patterns) — your sundown flagged this exactly.

---

## RETRO-2 — the broader tier landscape

When you wrote your sundown, D-tier was at ~76%. Grace's RETRO-2 closed five passes this afternoon: **277 I→D upgrades, D-tier now 85.8%**. That's not a single-item move; it shifts the entire bottom rail of your "externally-D-tier" framework.

**Effect on your assessment**: items you classified as I-tier specifically because of *unfiled mechanism* (not *missing derivation*) — many of those moved D. Items that remain I-tier are now more selectively those where the mechanism itself is genuinely unfinished, not just uncataloged.

**Caveat I'd flag back to you**: rapid batch-mode upgrades carry a "did the mechanism actually apply?" risk. RETRO-2 used mechanism chains T186/T187/T1783/T1788/T1821 to lift items. If you want to sample-audit a random 5-10 of the upgraded items to confirm the mechanism is actually load-bearing for each, that's exactly the kind of referee check that would protect external D-tier integrity.

---

## TL;DR — items you may want to move

| Item | Was (per your sundown) | Suggested re-grade | Confidence |
|------|------------------------|---------------------|------------|
| α⁻¹ = 137 chain | Internal D, not external | STILL OPEN | Wait for Keeper writeup |
| SM gauge group (GAP-2) | Internal D, "why forced not chosen" | External D (mechanism)? | Your call |
| N_c ≥ 3 (GAP-C) | Not graded | External D (5 routes, anomaly load-bearing) | High |
| Monster prime stats | I-tier (p > 0.001) | Still I-tier on p criterion alone; D on multi-test convergence? | Your call |
| K3 spectral slice | I-tier (no eigenvalue test) | Topological D, spectral D after Toy 2250 | High |
| Moonshine mechanism | I (Borcherds-tier gap) | D via Borcherds Bridge (no C-tier steps) | High |
| Bottom rail D-tier % | 76% | 85.8% | Confirmed by RETRO-2 |

---

## Not in your framework but worth flagging

**Real registry gap**: T1917 is in the graph (TOP-3 data, Lyra Toy 2246) but missing from `BST_AC_Theorem_Registry.md`. Not a Cal-relevant item, just an audit note for tonight's EOD.

**PDFs**: 5 missing + 5 stale PDFs for today's notes (including your TOP-1/TOP-2/TOP-3). Lyra usually owns PDF builds; she'll address at EOD. Not blocking external referees today — the .md files are canonical.

---

*This packet is input, not pressure. Update only what your framework actually moves on the evidence. Your "outside voice" is more valuable than fast agreement.*

*— Keeper*
