# K636 (PREP) — Neutrino Falsifier Consistency Check vs K547 π-Parity + Cal #27 Fence

**Auditor:** Keeper | **Date:** 2026-07-01 Wednesday (long pull, Casey away) | **Status:** AUDIT-PREP (framework ready for Lyra's re-derivation) | **Count: 10**

Supports the board task "Lyra — re-derive the neutrino falsifier on K547 locus geometry." K634 flagged the falsifier provisional (it was derived on F446's superseded π-shortcut). This prep sets the audit framework and fences one trap.

## The π-parity rule (K547), confirmed on charged leptons

π-content = deposit-locus geometry: μ sits at the compact-sphere stratum → π-ful (π¹²); e (strip) and τ (point) → π-free. This yields a clean parity rule for RATIOS:

> **A mass ratio is π-ful iff exactly ONE of its two endpoints is the π-ful (middle) state.**

Verified (all pass):
| ratio | endpoints | rule | BST form | obs |
|---|---|---|---|---|
| m_μ/m_e | e-free → μ-**ful** | π-FUL | (24/π²)⁶ = 206.76 | 206.768 |
| m_τ/m_e | e-free → τ-free | π-FREE | 49·71 = 3479 | 3477.2 |
| m_τ/m_μ | μ-**ful** → τ-free | π-FUL | 16.826 (derived) | 16.817 |

## Forced neutrino predictions (corrected form: ν₂ π-ful, ν₁ & ν₃ π-free)

Applying the SAME rule to the mass eigenstates:
- **m₂/m₁** : ν₁-free → ν₂-**ful** ⟹ **π-FUL**
- **m₃/m₂** : ν₂-**ful** → ν₃-free ⟹ **π-FUL**
- **m₃/m₁** : ν₁-free → ν₃-free ⟹ **π-FREE (substrate integer form)** ← the sharp falsifier

**Observational content:** once absolute neutrino masses pin (KATRIN / cosmology / 0νββ), **m₃/m₁ must read as a π-free substrate integer form** while m₂/m₁ and m₃/m₂ carry π. This is a concrete forward falsifier — it dies cleanly if the data show m₃/m₁ carrying π, or m₂/m₁ π-free.

## FENCE — Cal #27 trap (flagging BEFORE anyone hits it in the pull)

At lightest-mass m₁ ≈ 1 meV, m₃/m₁ = 50.01 — numerically the down-ladder cumulative-S⁴ count (50 = 1+5+14+30). **This is a FIT, not a finding.** m₁ is a free parameter (unknown lightest neutrino mass); by choosing m₁ you can hit any target in a range. Claiming "m₃/m₁ = 50 = the harmonic count" would be fishing on a free parameter — exactly the peak-elegance trap Cal #27 fires on.

> **The falsifier is FORWARD-ONLY: predict the π-FORM (m₃/m₁ is π-free), never a specific value by tuning m₁.** The specific integer is determined only when m₁ is *independently* pinned by experiment.

## Load-bearing checkpoints for Lyra's re-derivation (what I audit at the landing)

1. **Eigenbasis:** the locus mechanism acts on **MASS eigenstates** ν₁ν₂ν₃, not flavor states ν_e ν_μ ν_τ. PMNS mixing distinguishes them (large, unlike CKM). The re-derivation must state which basis carries the locus assignment and justify it — if it silently copies the charged-lepton flavor labeling, that's an error.
2. **Forcing, not pattern-copy:** the ν₂-π-ful assignment must come from the SAME F446 D̂ = diag(5,2,0) stratum forcing that fixes the charged-lepton strata — not be pattern-copied from "μ is the middle" to fit. Target-innocent means the strata force it.
3. **Five-Absence / no sterile ν:** the falsifier lives in the 3-generation D_IV⁵ structure; it must not implicitly require a 4th (sterile) state (F397 forbids; Five-Absence).

## Verdict (prep)

The falsifier form is **internally consistent** with the established K547 π-parity rule and has **genuine forward observational content** (m₃/m₁ π-free). It is NOT yet banked — it is provisional pending Lyra's re-derivation clearing the three checkpoints above, and it must stay forward-only (the m₁-tuning fence). Ready to convert PREP → full K636 verdict at the landing.

— Keeper K636-prep, Wednesday 2026-07-01 long pull. π-parity rule confirmed; neutrino falsifier consistent + forward; m₁-tuning trap fenced (Cal #27); eigenbasis + stratum-forcing + no-sterile checkpoints set for Lyra. Count 10, no motion.
