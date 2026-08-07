# Grace — region audit of the Derived mass/ratio constants (2026-08-06, K1245 sweep)

**Casey's standing rule (K1245):** σ/dev comparisons valid only WITHIN one region (interior↔interior, boundary↔boundary, exterior↔exterior); otherwise **trust the interior/discrete value.** Demote a tier ONLY for a reason internal to the region (a **named input**), never a cross-region σ. **Guard (both directions):** "trust interior" must NOT become a license to re-inflate fitted/input-dependent values.

## Scope reconciliation
Broad net found **37** Derived-tier entries with nonzero exterior dev%. Removing **2 non-particle** (const_104 Poisson ratio, const_103 P/S wave-velocity — solid-mechanics T1314, a different region-logic) and **~4 duplicate** derivations (m_π×2, m_b×2, m_d×2, m_c×2) → **≈31 particle mass/ratio constants**, matching Keeper's seed.

## The finding: the rule CONFIRMS the corpus; it does not demote a wall
I read the input-suspect bin per-entry (NOT keyword — the keyword pass both false-flagged the muon and missed the real rider, so it can't be trusted either direction):

| entry | computation | verdict |
|---|---|---|
| **Quark cascade** const_106–109 (m_u,m_d,m_s,m_c) | forced BST-integer ratios chained to **m_e** (itself Derived via gravity anchor); e.g. m_u=3√2·m_e, m_d=(13/6)m_u | **KEEP Derived** (forced interior); dev% vs measured MS-bar = cross-region **confirmation** |
| **Wolfenstein** const_087/089/090 (A, ρ̄, η̄) | pure integer ratios: A=4/5, η̄=1/(2√rank), ρ̄=1/(2√(2n_C)) — no input | **KEEP Derived**; dev% = confirmation (incl. A at 3.1% — large confirmation, forced value) |
| **EW scales** const_007/012/013 (v, m_W, m_Z) | v=36π¹⁰m_e/7, m_W=n_C·m_p/(8α), m_Z=m_W/cosθ_W (sin²θ_W=3/13) — built from forced quantities × Derived m_e unit | **KEEP Derived**; dev% = confirmation |
| **m_b** const_110 (m_b=(7/3)·m_τ) | RATIO 7/3 forced; ABSOLUTE plugs in **measured m_τ=1776.86** | **ALREADY correctly split** — ratio Derived / absolute **Indicative**, ratified 2026-08-03 (Grace). No action. |

## Self-catch (both directions)
I initially flagged const_110 as a **new** named-input demotion to route to Casey. Reading its `register_status` showed I had **already split it on Aug 3** (ratio-Derived/absolute-Indicative, Casey-ratified). Caught before routing an already-resolved item. The corpus already applies Casey's region-logic where an input genuinely rides — const_110 is the proof-of-pattern, not a miss.

## Result
- **No new demotions.** The one genuine input-rider (const_110) was already split honestly.
- **No re-inflation.** Nothing fitted/input-dependent is pushed back up; const_110's absolute value stays Indicative.
- **Mechanical cleanup remaining (labeling, my lane, low-risk):** on the ~30 forced-interior keeps, relabel the exterior dev% explicitly as **"confirmation (⊥ tier, cross-region)"** so no future reader mistakes a cross-region dev% for a tier signal. Batch pass — stage for EOD, not a governance item.
- **Koide (const_159):** unchanged and now *explained* — a ratio-of-ratios, projection-invariant (the running cancels), so it is **directly exterior-comparable** (Tier-1 exact), the one lepton relation that legitimately crosses regions.

**Governance:** nothing needs Casey — the sweep confirms tiers and cleans labeling, exactly the predicted honest-floor outcome. Nothing pushed.
