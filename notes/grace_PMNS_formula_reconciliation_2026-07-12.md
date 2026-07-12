# Grace — PMNS formula reconciliation (derivation-hygiene lane, pre-data-sync)
*2026-07-12. The corpus/JSON carries 2–3 competing forms per PMNS angle and three δ_CP values. Task: pick ONE
canonical per observable, pin to source, then sync the data layer. Criterion (priority order): (1) target-innocent
(2–3 integers, reject form-cheap); (2) tier (prefer D, but VERIFY the precision claim); (3) among clean forms, most
precise; (4) note structural consistency, don't force it; (5) pin to a const_id/theorem.*

## FINDING: the data-layer's current θ12 and θ23 forms are DOMINATED, and their precision claims are wrong
- **const_022** (sin²θ12 = (N_c/2n_C)·cos²θ13) computes to **0.2933 = 4.45% off** (obs 0.307), NOT the "0.06%/D"
  the morning board claimed. Dominated by cleaner forms below.
- **const_023** (sin²θ23 = ((n_C−1)/(n_C+2))·cos²θ13) computes to **0.5587 = 2.3% off** (both octants), NOT "0.4%".
  Dominated by the per-octant forms below.
- These precision-claim mismatches are exactly the hygiene rot the reconciliation exists to catch.

## CANONICAL PICKS (one per observable, pinned)
| observable | CANONICAL (pick) | value | prec | retire / note |
|---|---|---|---|---|
| **sin²θ12** (0.307) | **C_2·g/N_max = 42/137** [const_144] | 0.3066 | **0.14%** | retire const_022 (4.45%, dominated) + 5762/18769 (form-cheap, 4 ints). Alt noted: rank²/c_3=4/13 (0.23%). |
| **sin²θ13** (0.0220) | **1/(N_c²·n_C) = 1/45** [const_024, D-tier] | 0.0222 | 1.01% | ALT more-precise: N_c/N_max=3/137 (0.46%, shares N_max denom with θ12) — flag for team: D-tier 1/45 vs better-precision 3/137. |
| **sin²θ23** (octant-ambiguous) | **OCTANT-DEPENDENT: 4/7=(n_C−1)/(n_C+2) [upper, 0.572, 0.10%] OR C_2/c_2=6/11 [lower, 0.546, 0.10%]** | — | 0.10% each | retire const_023 (2.3% compromise, dominated by BOTH). Keep both until DUNE/T2K resolves the octant. |
| **δ_CP** (open lead, ~197° NO, ±40°) | **OPEN LEAD — not banked. Closest: π (180°, 9%).** | π | 9% | **retire 3π/7 (77°, 61% off) and 12π/7 (309°, 57% off) — neither fits.** Flag δ_CP as DUNE-constrainable open, π as the closest-to-best-fit placeholder. |
| **lepton Jarlskog J** | J = 5.16×10⁻³ (I-tier) [T330–332] | — | 1.4% | keep (single form). |

## Rationale notes
- **θ12 → 42/137:** cleanest (2 integers), most precise (0.14%), N_max is the fundamental integer, 42 = C_2·g = the
  Rosetta number (Σc_k(Q⁵)). Already registered (const_144). This is a genuine UPGRADE over const_022's 4.45%.
- **θ13 → 1/45 (D):** kept as canonical to respect the team's D-tier assignment (morning board). BUT 3/137 = N_c/N_max
  is more precise (0.46%) AND gives θ12,θ13 a shared N_max denominator (42/137, 3/137) — I flag this for the team as
  a possible cleaner reading; I do NOT unilaterally override the D-tier call.
- **θ23 octant:** the octant (θ23 above vs below 45°) is experimentally UNRESOLVED. 4/7 fits upper, 6/11 fits lower,
  each at 0.10%. The compromise const_023 (2.3%) is worse than both. Honest state: two candidate forms, octant-gated.
- **δ_CP:** genuinely barely-constrained (open lead). The three JSON values (3π/7, 12π/7, π) — only π is within
  hailing distance of the best-fit; 3π/7 and 12π/7 are corpus artifacts that don't fit. Retire them; mark δ_CP open.

## Then: DATA SYNC (the second half, after this reconciliation lands)
Update bst_constants.json: (a) apply the picks above (retire dominated duplicates); (b) add this week's banks —
F506 down-ratios, m_top=v/√2, m_charm=α·v/√2, Koide=rank/N_c; (c) file geometric invariants (SP-14). Flag for Cal's
count reconciliation.
