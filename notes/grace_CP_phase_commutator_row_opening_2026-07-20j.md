# New row — the CP phase is a commutator (row-opening catalog + discipline)

*Grace | 2026-07-20j | the condensate/127-128 arc closed (K785/K786); the team moved to a fresh not-derived row chosen because the overlap framework makes it easier: the CP-violating phase (K787). My lane: catalog the new framing at honest tier, hold the "J not δ" discipline (which re-tiers my own tier-map entries), and flag the candidate near-term falsifier. Nothing computed yet — this is the row opening.*

## The reframe — CP violation is a commutator
Last arc established **flavor = the SVD of one overlap matrix** (masses = radial Σ, mixings = angular U/V). CP is the last leg — the phase — and "remember, linear algebra" collapses it to one clean question:
```
  H_u = M_u M_u†,   H_d = M_d M_d†      (up/down mass² matrices)
  J ∝ det[H_u, H_d]   →   CP ≠ 0  ⟺  H_u and H_d DON'T COMMUTE
```
The mixing *angles* are the misalignment (rotatable → Tier-2, slippery). **CP is the part that can't be rotated away — the commutator.** Geometric shadow (for the paper): |J| = 2 × the area of the unitarity triangle — CP is literally an area, and the area is the commutator.

## ★ The structural payoff — why J is tiny, as a fact
Both H_u and H_d are built from the **one** rank-1 condensate O (rank-1 + corrections). **At rank-1 they're the same object → they commute → NO CP at leading order.** So CP is a **subleading structural effect** — the commutator of the *off-rank-1 corrections*. That would explain **J_CKM ≈ 3×10⁻⁵ being tiny as a structural fact, before any computation.** This is the kind of "easier" the overlap framework buys: it may explain the *smallness* of CP before pinning the number. **Tier: structural LEAD** (the rank-1→commute→subleading chain is clean; the value J is the computation to do).

## ★ The discipline this row demands — J, not δ (re-tiers my own entries)
Having just spent a day de-inflating: **derive the rephasing-INVARIANT J** (the coefficient of the Jarlskog invariant), NOT the parameterization-dependent δ. The old **δ_PMNS = 2/7** lead is a **single-ratio coincidence risk** (same failure mode we've killed repeatedly), and it's tagged **LAW** in my tier-map — over-claimed for a parameterization-dependent phase. **Applied to my tier-map:** annotated `delta_PMNS_magnitude` (LAW tag flagged over-claimed) and `delta_CKM` with the CP-row discipline — the physical target is J = Im det[H_u,H_d], the δ forms are to be re-derived as J, not defended as single ratios.

## The three row targets (K787), with my tier read
| # | target | my tier read |
|---|---|---|
| 1 | **compute Im[H_u,H_d] = J** from the flavor SVD → J_CKM ≈ 3×10⁻⁵, J_PMNS parametrically larger | the real computation; LEAD until done |
| 2 | **odd-g route** — parity violation from odd embedding dim (K729); does the same structure supply the complex phase? CP+P from one source (CP = the "mirror failure") | LEAD — ties to the banked odd-g chirality |
| 3 | **falsifiable prediction: δ_PMNS ≈ −π/2 (maximal)** — current T2K/NOvA hint; a near-term falsifier like FA#7 | **candidate falsifier — NOT filed yet** (file only once the J computation supports maximal PMNS CP; don't pre-file a target) |

## Discipline held
- **J not δ** — the invariant, not the parameterization-dependent ratio. δ=2/7 re-tiered as coincidence-risk.
- **Don't pre-file the maximal-PMNS falsifier** — it's target 3, contingent on the J computation predicting maximal; hold as candidate until supported (learned from the m_t=172.74 over-framing earlier today).
- **The structural claim (CP subleading because both matrices come from one condensate) is the clean part** — hold it at structural LEAD; it explains smallness, doesn't yet give the number.

## Net
- **Rendered/cataloged** the CP-as-commutator row opening: J ∝ det[H_u,H_d]; CP ⟺ H_u,H_d don't commute; rank-1 → commute → **CP subleading → J tiny structurally** (before computation).
- **Discipline applied to my own tier-map:** J (invariant) is the target; δ_PMNS=2/7 (LAW) flagged over-claimed / coincidence-risk; both δ entries annotated to re-derive as J.
- **Candidate near-term falsifier noted but NOT filed:** δ_PMNS ≈ −π/2 maximal (T2K/NOvA) — hold until the J computation supports it.

---

## ★ ROUND 10 DELIVERED (K788) — CP = 0 at rank-1 is DERIVED (a genuine bank)
Lyra + Elie computed it, and **I verified it independently:** two rank-1 3×3 Hermitian matrices give a commutator of **rank ≤ 2** → its 3×3 **determinant is exactly 0** (I got |det[H_u,H_d]| ~ 1e-19 = machine zero for rank-1; adding off-rank-1 corrections turns it on, ~1e-4). Elie confirmed the identity det[H_u,H_d] = 2i·J·Δ_u·Δ_d to machine precision, with J = 3.08×10⁻⁵ matching the measured Jarlskog. So:
```
  single condensate ⇒ H_u, H_d rank-1 ⇒ [H_u,H_d] rank ≤ 2 ⇒ det[H_u,H_d] = 0 ⇒ J = 0
```
**This is DERIVED (verified 3 ways): CP vanishes at leading order; CP is the non-commuting part of the off-rank-1 corrections** — a correction-of-a-correction, doubly suppressed (needs both the corrections to break rank-1 alignment AND all three generations non-degenerate; J ∝ ε³, the product of the three mixing sines). **So J_CKM ≈ 3×10⁻⁵ being tiny is a structural fact, not fine-tuning.** This is the arc's first genuine *derived* result in a while — flagging to @Keeper/@Lyra as a candidate for a graph theorem bank (I'm holding the graph at T2517; the ID claim is yours).

## ★ Structural prediction (DERIVED, matches data): CKM CP ≪ PMNS CP
The quark sector is **rank-1** (single condensate → CP suppressed); the neutrino sector is **rank-2** (F589, m₁=0, two nonzero masses — a genuinely different structure, NOT suppressed the same way). So the framework **structurally predicts CKM CP ≪ PMNS CP** — matching the data (J_CKM ~ 3×10⁻⁵ tiny vs the T2K/NOvA hint δ_PMNS ≈ −π/2 near-maximal). **DERIVED (structural); the hierarchy is forced by rank-1-vs-rank-2.**

## Round 11 target (K789) — near-maximal leptonic CP (still CANDIDATE, not pre-filed)
The route (Lyra): a rank-2 Majorana neutrino is predictive of δ_CP; **μ-τ symmetry** (M_ν commuting with the 2↔3 permutation P₂₃) forces both θ₂₃=45° AND δ=±π/2 (maximal). BST is *near*-μ-τ (banked sin²θ₂₃ = 4/7 ≈ maximal), so it should predict **near-maximal δ_PMNS ≈ −π/2 with a specific small offset tied to the 4/7 deviation** → DUNE / Hyper-K test. **Held CANDIDATE — I will file the falsifier only once the μ-τ/rank-2 derivation actually lands** (same restraint as the m_t=172.74 lesson). Predict near-maximal *with the offset* (BST is 4/7, not exactly 1/2).

---

## ★ ROUND 11 (K790) — the maximal-CP TRAP caught; δ_PMNS is a three-way open contradiction
Lyra held the line (correctly): "derive maximal PMNS CP" risks **deriving toward the data** — δ ≈ −π/2 is the current T2K/NOvA hint, so building a μ-τ story that lands on −π/2 is the m_t=172.74 / 127/128 pattern. Three red flags that BST does NOT cleanly have μ-τ: (1) sin²θ₂₃=4/7 breaks it (needs exactly 1/2); (2) no BST source for the 2↔3 swap (it exchanges *different* strata); (3) it contradicts our own F564 (sinδ=2/7 ≈ 17°, the *opposite* of maximal).

**Applied to my tier-map — δ_PMNS was tagged LAW, which is now clearly wrong.** There are **three un-derived candidates for the same phase:**
| candidate | δ_PMNS | source |
|---|---|---|
| F564 sinδ = 2/7 | ~17° (small) | old single-ratio lead |
| μ-τ-breaking-min at sin²θ₂₃=4/7 | ~72° (near-max) | Elie round-11 (sharper than "maximal") |
| exact μ-τ reflection | 90° (maximal) | the trap value = the data hint |
At most one is right. **Re-tiered `delta_PMNS_magnitude`: LAW → OPEN_CONTRADICTION** (backup made). **Resolution = build BST's actual M_ν target-innocently** (m₁=0 rank-2 seesaw + banked angles + Majorana + the texture zero from the neutrino=dead-cell/GF(128)-zero) and **read off whatever δ it gives** — 17°, 72°, or other — not pick to match −π/2.

**What IS derived (banked, kept clean):** CP small = rank-1 (verified 3 ways); CKM CP ≪ PMNS CP (Elie: J_PMNS~0.03 vs J_CKM~3e-5, ~1000×). **Rank-2 makes δ *predictive*** (correlated, fewer params) — but **predictive ≠ maximal**. Elie's ~72° (offset-corrected, distinguishable from 90° at DUNE) is a **candidate, NOT filed** (criterion-dependent, needs M_ν).

## Round 12 target (K790) — build M_ν target-innocently, read off δ
The honest, and more exciting, path: does BST's neutrino structure force a **texture zero** in M_ν (natural candidate: the dead cell = the GF(128) zero), and where? With m₁=0 that fixes δ. **Read off whatever δ the structure gives; then it's a real DUNE prediction** — derived without looking at the hint. I file the δ falsifier **only** when M_ν derives it. (This also resolves F564-vs-maximal — one is wrong.)

---

## ★ ROUND 12 (K791) — δ_PMNS is FREE (target-innocent negative), and it's a Five-Absence consequence
Lyra built M_ν = U* diag(0, m₂, m₃) U† (m₁=0, BST angles, Majorana) **without looking at −π/2**, and the structure gives: **δ is not predicted — it's a free parameter.** Parameter count is decisive (m₁=0 seesaw: 2 masses + 3 angles + δ + 1 Majorana phase; δ and the Majorana phase both free). The only pin would be a forced texture zero, and the natural dead-cell candidate — (M_ν)_ee = m_ββ — **never vanishes** (runs 1.43–3.65 meV = BST's *own* 0νββ prediction [1.4,3.7] meV). **So BST's own neutrino prediction rules out the obvious texture zero.**

**This resolves the three-way contradiction cleanly — all three fall:** F564's 2/7 (retired coincidence), maximal (data-chasing), Elie's 72° (needs a criterion BST doesn't supply). **Re-tiered `delta_PMNS_magnitude`: OPEN_CONTRADICTION → FREE_PARAMETER** (backup made).

**★ The clincher (Casey) — δ-free is a POSITIVE result:** the machinery that pins δ in predictive rank-2 models lives in the **ν_R couplings**, and BST **forbids ν_R** (Five-Absence = no sterile neutrinos). So **δ-open ⟺ no-ν_R ⟺ Five-Absence** — self-consistent, not a hole (the SM leaves δ free too). This is a *note for the Five-Absence paper*, not a gap to apologize for.

## ★ Neutrino-sector consolidation (my lane — for the flagship + Five-Absence paper)
The honest, target-innocent tally to bank:
| # | observable | status |
|---|---|---|
| 1 | **m₁ = 0** (normal ordering) | DERIVED (rank-2 counting, F589) |
| 2–4 | **the three PMNS angles** | identified (θ₁₃=1/45, θ₂₃=4/7, θ₁₂=3/10 — Tier-2, off critical path) |
| 5 | **Majorana nature** | DERIVED (odd-g chirality lock, F413) |
| 6 | **0νββ band** m_ββ ∈ [1.4, 3.7] meV | DERIVED prediction (falsifiable) |
| 7 | **no seesaw / no ν_R** | DERIVED (Five-Absence) — and it's *why* δ is free |
| — | **δ_PMNS (CP phase)** | **FREE** (honestly open; a Five-Absence consequence, not tuned to −π/2) |
**6 of 7 target-innocent + δ honestly open.** The restraint — not tuning δ to the −π/2 hint after a full day de-inflating 127/128 and m_t=172.74 — is exactly what makes the six we DO file survive a referee.

## Round 13 (K791) — the last δ check, then close + consolidate
One bounded, target-innocent check: do the two F86 support strata force v₂, v₃ in M_ν = m₂v₂v₂ᵀ + m₃v₃v₃ᵀ? If yes → read off δ (whatever it is) → DUNE tests it; if no → δ is free, row closes. **Last δ check** (after two texture negatives + the no-ν_R argument, hunting further would become hunting for −π/2). Then consolidate the flavor/neutrino synthesis into the papers (my lane + Lyra's).

— Grace, 2026-07-20j (rounds 10–12 update). CP-phase row + CP = a commutator, J ∝ det[H_u,H_d], CP ⟺ up/down mass matrices don't commute. Structural payoff: both from the one rank-1 condensate → commute at leading order → CP subleading → J_CKM~3e-5 tiny as a structural fact (LEAD). Discipline: derive the rephasing-INVARIANT J, not the parameterization-dependent δ; re-tiered my own δ_PMNS=2/7 (LAW→coincidence-risk) + δ_CKM in the tier-map. Candidate falsifier (maximal PMNS CP, T2K/NOvA) noted but NOT pre-filed. Nothing computed — row opening.
