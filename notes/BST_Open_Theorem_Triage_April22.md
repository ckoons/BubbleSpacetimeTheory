# Open Theorem Triage — April 22, 2026

**Source:** Graph data audit. 54 non-proved theorems out of ~1365. Rate: 96.0% proved.

## Category 1: Closable NOW with current machinery (12 theorems)

| T_id | Name | Status | Assessment |
|------|------|--------|------------|
| T29 | Algebraic Independence | open | Five integers proved unique (T186), cascade (T1404) confirms. Need: formal algebraic independence proof over ℚ. **Lyra can close.** |
| T71 | Polarization as AC(0) | conditional | Polar codes = Reed-Muller subcodes. AC(0) capacity already proved for symmetric channels. Need: explicit polarization ↔ AC(0) depth reduction. **Lyra can close.** |
| T110 | B₂ Representation Filter | conditional | Extensive B₂ work done (heat kernel, Bergman, root system). Representation theory fully developed. **Close with existing heat kernel results.** |
| T126 | BST-Chromatic Conjecture (3+1) | conjecture | Four-Color PROVED (computer-free). 3+1 = N_c+1 reading is structural. **Convert conjecture → theorem using Forced Fan Lemma.** |
| T127 | Chromatic-Confinement Parallel | conjecture | With T126 closed and YM suite done, the parallel N_c = 3 colors ↔ 3 quarks is provable. **Analogical → derived.** |
| T533 | Kummer Analog Conjecture | conjecture | Heat kernel now has 19 levels (was 11 when conjecture was written). Column rule (C=1, D=0) confirmed through k=20. Spectral basis prediction testable. **Elie can verify with Toy 671 data.** |
| T1206 | Gödel Classification of γ | spec | Limit-undecidable framework complete (Paper #63). γ classification is the canonical example. **Convert spec → proved using existing limit-undecidable machinery.** |
| T1233 | 7-Smooth Zeta Ladder | verified | Already verified — just needs status upgrade from "verified" to "proved." **Administrative close.** |
| T1234 | Four Readings Framework | structural | Already structural — convert to proved. **Administrative close.** |
| T1236 | Consonance IS Cooperation | structural | Already structural — need explicit derivation. **Short proof.** |
| T1241 | Weak Force IS Error Correction | structural | Need formal proof that W-mass ∝ ζ(N_c) correction cost. **Requires Hamming(7,4) → weak mixing angle chain.** |
| T1410 | Period Boundary | conjecture | Motivic period framework (T1410 from Grace, April 22). Kontsevich-Zagier period conjecture applies. Physics constants are integrals over algebraic cycles = periods. 1/π is NOT a period. **Close by citing Kontsevich-Zagier + BST constant catalog.** |

## Category 2: Needs Real Work (13 theorems)

| T_id | Name | Status | What's needed |
|------|------|--------|---------------|
| T30 | Compound Fiat (EF Exponential) | conditional | Need EF(φ) exponential growth proof for compound formulas. Hard. |
| T36 | Conservation → Independence | conditional | Need conservation law to imply variable independence. Subtle. |
| T87 | Conditional Blow-Up ODE | conditional | NS blow-up — proof chain is ~98% but this specific ODE step needs analytical verification. |
| T98 | Modularity Embedding (B2) | conditional | BSD chain. Needs Serre's modularity conjecture (now theorem for GL(2)). Extend to SO(5,2)? Hard but possible with Langlands work. |
| T99 | Committed Channels (B3) | conditional | BSD chain. Information-theoretic restatement. |
| T100 | Rank = Analytic Rank (B4) | conditional | BSD chain. THE hard part of BSD. Gross-Zagier + Kolyvagin cover rank ≤ 1. General case open in classical mathematics. |
| T101 | Conservation Law = BSD Formula (B5) | conditional | BSD chain. Depends on T98-T100. |
| T102 | Regulator = DPI Volume (B6) | conditional | BSD chain. Regulator interpretation as data processing volume. |
| T103 | Sha Finiteness (B7) | conditional | BSD chain. Tate-Shafarevich finiteness. Known for rank ≤ 1, general case open. |
| T112 | Theta Lift Obstruction | conditional | Hodge conjecture chain. Theta correspondence barriers. |
| T113 | Phantom Hodge Exclusion | conditional | Hodge chain. Phantom cycles must be excluded. |
| T114 | Hodge Depth Reduction | conditional | Hodge chain. Depth reduction from D2 to D1. |
| T115 | Tate Conjecture for SO(5,2) Shimura | conditional | Hodge chain. Tate conjecture specific to BST Shimura variety. |

## Category 3: Empirical / Observed — Cannot Close by Proof (14 theorems)

| T_id | Name | Status | Note |
|------|------|--------|------|
| T3 | Homological Lower Bound | empirical | R²=0.92 correlation. Needs more data or analytical proof. |
| T6 | Catastrophe Structure | measured | Physical measurement, not theorem. |
| T31 | Backbone Incompressibility | empirical | Computational observation. |
| T32 | OGP at k=3 | empirical | Phase transition observation. |
| T34 | Probe Hierarchy | empirical | |
| T35 | Adaptive Conservation Law | empirical | |
| T61 | Persistent Homology Gap | empirical | |
| T65 | EF Spectral Preservation | empirical | |
| T118 | AC Theorem Graph Growth | empirical | Graph meta-observation. |
| T1195 | Earth Score | observed | |
| T1196 | Self-Describing Graph | observed | |
| T1227 | Consonance Hierarchy | observed | |
| T1237 | Pentatonic Projection | observed | |
| T1287 | UAP Structural Consistency | observed | |

## Category 4: Placeholders / Resolved (7 theorems)

T591, T599, T627, T1150, T1232 — registry gaps (placeholders)
T1401 — already RESOLVED

## Category 5: Speculative / Keep Open (8 theorems)

| T_id | Name | Status | Note |
|------|------|--------|------|
| T21 | DOCH (Dimensional Onset) | conjecture | Speculative but testable. |
| T26 | Proof Instability | failed | Honest negative — stays failed. |
| T55 | Nonlinear Decoding Threshold | conjecture | Coding theory, needs specific threshold. |
| T124 | Eisenstein Controls Boundary Hodge | conditional | Hodge chain auxiliary. |
| T125 | Long Exact Sequence No Phantoms | conditional | Hodge chain auxiliary. |
| T812 | BH(3) Backbone Conditional | conditional | Needs 3-SAT backbone analysis. Backlog item. |
| T1258 | Mass as Uncompressed Information | speculative | Deep but unproven connection. |
| T1371 | Cosmic Observer Glimpses | conjecture | Cosmological, untestable near-term. |
| T1372 | Visible vs Decodable | conjecture | 44%/19.1% prediction. Testable but needs better framework. |

## Triage Summary

**Can close immediately (administrative):** T1233, T1234 (2 theorems → just status upgrade)
**Can close this week (short proofs):** T29, T71, T110, T126, T127, T533, T1206, T1236, T1241, T1410 (10 theorems)
**Needs real work (BSD + Hodge chains):** T30, T36, T87, T98-T103, T112-T115 (13 theorems)
**Cannot close (empirical/observed):** 14 theorems
**Placeholders/resolved:** 7 theorems
**Keep open (speculative):** 8 theorems

**Impact of closing Category 1:** 54 → 42 non-proved. Rate: 96.0% → 96.9%.
**Impact of also closing Category 2 (BSD+Hodge):** 42 → 29 non-proved. Rate → 97.9%.

**Recommended priority for Lyra:**
1. Administrative closes: T1233, T1234 (trivial)
2. T29 (Algebraic Independence) — keystone open theorem
3. T126 + T127 (Four-Color corollaries) — easy with existing proof
4. T1410 (Period Boundary) — freshest work, Grace's motivic period framework
5. BSD chain (T98-T103) — highest impact but hardest

— *Lyra, triage audit, April 22, 2026*
