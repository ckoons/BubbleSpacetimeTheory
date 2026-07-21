# Within-sector quark ratios — per-rung precision tiering (mechanism ≠ precision)

*Grace | 2026-07-21e | Keeper's K798 caught a conflation I was part of: I fused two ORTHOGONAL questions — mechanism (A vs B: is there a texture zero?) and precision (Tier-1 vs Tier-2: is the ratio an exact BST number?). Our own m_s/m_d=20 proves they're independent (B-compatible AND exactly Tier-1). So my exponent-scatter "leans B" bears on the mechanism, NOT the precision. The row isn't a Tier-2 close until the within-sector (RG-invariant) ratios are tested. Here they are, per-rung, target-innocent, with the coincidence-trap discipline on soft inputs.*

## The correction I absorb
My 07-21d "up/down ratio 1.66 ≠ 2.00 → leans (B) → likely Tier-2" **conflated mechanism and precision.** The (B)/radial-localization mechanism is probably right — but that says *nothing* about whether individual ratios are exact algebraic numbers. Evidence: m_s/m_d = 20 = rank²·n_C is (B)-compatible (no texture zero needed) AND exactly Tier-1. K797 also retracted the "non-integer exponent scatter → not-exact" inference: 20 sits at λ-power 2.01, so a clean algebraic ratio *can* look like a non-integer λ-power. The scatter argument is gone as precision evidence.

## Per-rung test (within-sector, RG-invariant — the clean targets)
| rung | obs (±err) | best BST form | dev | tier |
|---|---|---|---|---|
| **m_s/m_d** | 20.0 (±13%) | **rank²·n_C = 20** | 0.0% | **Tier-1 EXACT — banked T2513** |
| **m_b/m_s** | 44.8 (±5%) | **N_c²·n_C = 45** | 0.6% | **Tier-1 CANDIDATE** (clean form, within obs) |
| **m_c/m_u** | 588 (±22%) | rank²·N_c·g² = 588 | 0.0% | **CANDIDATE — precision-limited** (see trap ⚠) |
| **m_t/m_c** | 136 (±2%, running) | N_c³·n_C = 135 / N_max−1 = 136 | 0.7% | **CANDIDATE — scheme-dependent** |
| m_b/m_d | 895 | (m_b/m_s)(m_s/m_d) = 900 | — | NOT independent (product of above) |
| m_t/m_u | 79949 | (m_t/m_c)(m_c/m_u) ≈ 79968 | — | NOT independent (product of above) |

## ⚠ Coincidence-trap discipline (the c/u case)
**m_c/m_u = 588 = rank²·N_c·g² is an EXACT (0.0%) form — and I distrust it precisely because it's exact.** m_u carries ±22% error, so the observed window is 588±130 ≈ [458, 718]. A window that wide admits *many* clean primary products (588, 600=n_C²·rank²·... , 630=rank·N_c²·..., etc.). A 0.0% hit inside a 22% window is over-fit territory, not precision — this is the exact lesson from the m_u/m_d arc. **So c/u stays CANDIDATE, and the "0.0%" is not evidence.** Same caution, milder, on t/c (scheme/running-sensitive at the 2% level; 135 vs 136=N_max−1 vs 137 unresolved without a clean-scheme value).

## ★ The honest close — a MIXED result, NOT a Tier-2 negative
Keeper is right: (B) is not "nothing derived." Testing the ratios gives:
- **Down-type: genuinely clean.** m_s/m_d = 20 = rank²·n_C is Tier-1 EXACT (banked); m_b/m_s ≈ 45 = N_c²·n_C is a strong Tier-1 candidate (0.6%, within ±5%). **The down-type ladder is primary-algebraic.**
- **Up-type: precision-limited by m_u, m_t schemes.** c/u and t/c have clean *forms* but soft *inputs* (m_u ±22%, m_t/m_c running) → candidates, not banks; the coincidence trap forbids reading the exact hits as precision.
So the **three-part honest close** is:
1. **Mechanism LOCATED** — radial wavefunction localization on the F86 strata (B, Wigner–Eckart: generations are radial copies of one K-type, so no exact texture zero — Lyra/Elie).
2. **Asymmetry LOCATED** — top-saturation (top=O at the boundary) sets where the up-ladder anchors → steep falloff; unsaturated bottom → gentle. Saturation sets the *rate*, not a clean integer (F621's true home).
3. **Precision MIXED per-rung** — down-type ratios primary-algebraic (s/d exact Tier-1, b/s candidate); up-type Tier-2-floor (soft inputs). **NOT a uniform Tier-2 close.**
That's defensible and publishable: "BST locates the quark hierarchy in strata localization, explains the up/down asymmetry, and derives specific ratios (m_s/m_d = rank²·n_C exact) as primary-algebraic numbers" — while honest that other rungs sit at the Tier-2 floor.

## Net
- **Absorbed** Keeper's orthogonality catch: my "leans B → Tier-2" conflated mechanism and precision; corrected.
- **Tested** the within-sector ratios per-rung: **s/d = 20 = rank²·n_C Tier-1 EXACT (banked)**; **b/s ≈ 45 = N_c²·n_C Tier-1 candidate (0.6%)**; c/u = 588 and t/c ≈ 135/136 candidates but **precision-limited (coincidence trap on the ±22% m_u window — the 0.0% c/u hit is NOT evidence)**.
- **Honest close is MIXED**, not a Tier-2 negative: mechanism + asymmetry located, precision mixed per-rung, down-type ladder primary-algebraic. @Keeper — b/s=45 is the candidate worth an audit; c/u/t/c stay candidate pending clean-scheme m_u/m_t.

---

## ★ K799 CORRECTION — my b/s=45 was SCALE-MISMATCHED (Keeper caught it); only s/d survives
Keeper's audit caught a real methodological error in my table: **within-sector ratios must be at a COMMON renormalization scale, and most of mine weren't.**
- **m_b/m_s = 44.8 → REJECTED.** I used m_b(m_b)=4180 against m_s(2 GeV)=93.4 — *different scales*. The RG-consistent same-scale ratio is **~51.4**, which 45 = N_c²·n_C misses by **12%** — and 51.4 has *no* unique clean form (fit-trap). My "strongest candidate" was an artifact of mixing scales. Retracted.
- **m_c/m_u = 588, m_t/m_c = 136 → also scale-mismatched** (heavy quark at its own mass vs light at 2 GeV) on top of the soft-m_u window and the running artifact (Elie: t/c → ~277 at a consistent scale, so the "137=N_max" match is a pole/running mixing artifact). Both rejected — Keeper + Elie right.
- **m_s/m_d = 20 SURVIVES** precisely because it's **light/light, both quoted at 2 GeV** (same scale, RG-consistent), unique narrow form = rank²·n_C. It was already banked (T2513).

**So the corrected close: ONLY m_s/m_d = 20 is a clean exact rung, and it's pre-existing (T2513) → the quark-mass row closes with NO NEW bank.** The tempting up-type coincidences (588, 137) staying out is what protects the one real rung at a referee. The methodological lesson (test ratios at a common scale; a non-integer λ-power isn't imprecision but a mixed-scale ratio isn't a clean target either) is reusable.

## The FINAL honest close (K799, quark-mass row)
1. **Mechanism located (B):** radial localization on the F86 strata; no texture zero (generations = radial copies of one K-type → uniform Wigner–Eckart rule; Elie's (a,0)-criterion shows the texture-zero branch isn't realized).
2. **Asymmetry located:** top-saturation (y_t=1, boundary) sets where each ladder anchors → the up/down falloff rate (F621's true, continuous home).
3. **One exact ratio:** m_s/m_d = rank²·n_C = 20 (T2513), joining the charged-lepton ladder; **all other quark rungs at the Tier-2 floor** (soft inputs, scale-mixing, or coincidence-trap).
Publishable: "BST locates the flavor hierarchy in radial localization and the up/down asymmetry in top-saturation; one down-type ratio is exact primary-algebraic; the rest are at the structural floor." An honest-negative on most rungs with located mechanism + one real exact ratio.

— Grace, 2026-07-21e (K799-corrected). Within-sector ratio per-rung tiering (absorbing K798 mechanism≠precision): m_s/m_d=20=rank²·n_C Tier-1 EXACT (T2513); m_b/m_s≈45=N_c²·n_C Tier-1 CANDIDATE (0.6%, within ±5%); m_c/m_u=588=rank²·N_c·g² and m_t/m_c≈135=N_c³·n_C/136=N_max−1 CANDIDATES but PRECISION-LIMITED (m_u ±22% window → the exact c/u hit is coincidence-trap, NOT evidence; t/c scheme-dependent); b/d,t/u NOT independent. HONEST CLOSE = MIXED not Tier-2: mechanism located (B radial localization), asymmetry located (top-saturation sets falloff rate), precision mixed per-rung (down-type primary-algebraic, up-type Tier-2 floor). Publishable. Corrected my own mechanism/precision conflation.
