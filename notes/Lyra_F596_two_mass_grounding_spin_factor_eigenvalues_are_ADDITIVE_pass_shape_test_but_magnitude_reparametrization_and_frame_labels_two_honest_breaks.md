# F596 — Grounding the two-mass candidate. The rank-2 spin-factor eigenvalues are λ± = t ± |v| — ADDITIVE by construction, so the make-or-break "additive not ratio" test PASSES on shape. But trying to break it (as instructed): the magnitude |v| is per-quark (a re-parametrization, not derived), and the bulk/Shilov labeling of the idempotents is frame-dependent (currently a naming). CANDIDATE strengthened on shape, honest on two breaks.

**Lyra, Sun 2026-07-19. My lane: does the mass operator genuinely have two idempotent eigenvalues (c₁ bulk / c₂ Shilov), and is the relation additive or a ratio?** Casey: try to break it as hard as confirm. Result: one genuine structural pass, two genuine breaks.

## ✅ PASS (structural, genuine) — the make-or-break shape test
The Jordan algebra of D_IV⁵ is the **rank-2 spin factor**: an element x = (t, v), t∈ℝ, v∈ℝ^{n_C−1}. Its spectral decomposition (standard):
$$ x = \lambda_+ c_+ + \lambda_- c_-, \qquad \lambda_\pm = t \pm |v|, \qquad c_\pm = \tfrac12(1 \pm \hat v). $$
So a mass element has **exactly two spectral eigenvalues** — the "two masses" — and they relate by
$$ \boxed{\;\lambda_+ - \lambda_- = 2|v| \quad(\text{ADDITIVE, not a ratio}),\qquad \lambda_+ + \lambda_- = 2t.\;}$$
**The rank-2 geometry predicts an ADDITIVE split by construction.** This is the make-or-break test (Casey: additive → survive, ratio → die) and it **PASSES on shape** — the eigenvalues of a spin factor are trace/2 ± discriminant, an additive spread, never a ratio. Map: **constituent = λ₊ = t+|v|** (larger, dressed), **current = λ₋ = t−|v|** (smaller, bare); constituent − current = 2|v|. Non-trivial, real, and it's the right shape.

**Bonus consistency with yesterday:** a *current-massless* quark has λ₋ = t−|v| = 0 ⟹ t = |v|, eigenvalues {0, 2|v|} — the same rank-2 "one zero eigenvalue" that gave m₁=0 (F589). The up (current ≈ 0) sits near this limit; its two masses are ≈ {0, 2|v|} = {bare≈0, constituent≈confinement scale}. Off-diagonal |v| lives in the Peirce J₁₂ space, **dim 3 = N_c = color** — the dressing is the color/off-diagonal part, consistent with confinement=Shilov (F588).

## ✗ BREAK 1 (honest) — the magnitude |v| is per-quark, NOT universal; it's re-parametrization until derived
Computed |v| = (constituent − current)/2 across the six quarks:
| q | current | constituent | t=(sum)/2 | **|v|=(diff)/2** |
|---|---|---|---|---|
| u | 2.2 | 336 | 169 | **167** |
| d | 4.7 | 340 | 172 | **168** |
| s | 93 | 486 | 290 | **196** |
| c | 1270 | 1550 | 1410 | **140** |
| b | 4180 | 4730 | 4455 | **275** |

**|v| ranges 140–275 MeV — NOT universal.** So "constituent = current + universal Λ" is a **light-quark approximation** (good only for u,d where |v|≈167). Worse: writing the two masses as (t, |v|) = (sum/2, diff/2) is just **re-parametrizing two numbers as their sum and difference** — it carries no predictive content until the geometry **derives |v|** (the off-diagonal/color-space magnitude) independently. Right now |v| is fitted per quark. **The additive SHAPE is derived; the additive MAGNITUDE is not.** To become a real derivation, the geometry must produce |v| from the confinement (Shilov/J₁₂ color) scale — that's the open step, and it must explain why |v| *varies* (140–275), not why it's constant.

## ✗ BREAK 2 (honest) — the bulk/Shilov labeling of the idempotents is FRAME-DEPENDENT
My assignment asked "c₁=bulk / c₂=Shilov, not a relabeling?" Honest answer: **the two eigenvalues are invariant** (λ± are the genuine spectral values, frame-independent), and they're invariantly ordered (constituent > current). **But the idempotents c± = ½(1±v̂) depend on the frame direction v̂** — same frame-dependence I flagged killing the Peirce-confinement route two days ago (F588). So tagging the larger eigenvalue "the Shilov idempotent" is currently a **naming, not a frame-independent geometric identity.** It's *motivated* (confinement adds mass ⟹ dressed=constituent=confined=Shilov), but "c₂ = Shilov" is not yet derived — it needs v̂ pinned geometrically. Until then, the bulk/Shilov tags are at risk of being exactly the relabeling the assignment warned against.

## ⚠ COINCIDENCE TRAP (flag for Cal/Keeper) — m_p/N_c is near-tautological
"Λ_Shilov = m_p/N_c ≈ 313 MeV" matching constituent(u,d) ≈ 336 is **partly circular**: constituent masses are *defined* so that the proton = N_c constituents (m_p ≈ N_c·m_const). So "constituent ≈ m_p/N_c" is nearly a tautology, not an independent match. **Do NOT bank Λ_Shilov = m_p/N_c as a derivation** — it's the coincidence trap Keeper warned about.

## Verdict / tier
- **Additive-not-ratio (make-or-break SHAPE): PASS** — genuine, structural, the spin-factor eigenvalues are additive by construction.
- **Two genuine eigenvalues: YES** (invariant spectral values, not a relabeling).
- **Magnitude |v|: OPEN** — per-quark re-parametrization; geometry must derive it (and its variation) from the color/Shilov scale. **This is the real open step.**
- **Bulk/Shilov idempotent labels: FRAME-DEPENDENT** — a naming until v̂ pinned.
- **m_p/N_c match: near-tautology, do not bank.**
- **Net: CANDIDATE strengthened on shape (real), open on magnitude, honest on two breaks.** Not a FAIL — the geometry has the right shape — but not a clean PASS either.

## Handoffs
- **@Elie** — your Λ_Shilov toy: the decisive number isn't "is the offset universal" (it isn't — |v| = 140–275); it's **can the geometry DERIVE |v| per quark from the J₁₂/color–Shilov scale?** If |v| falls out of the off-diagonal (color) Peirce norm, magnitude closes; if |v| stays fitted, it's re-parametrization. And test the current-massless limit (u,d): does 2|v| → the confinement scale independently of m_p (avoiding the tautology)?
- **@Cal** — two referee calls: (1) is 2|v|=offset a derivation or a re-parametrization of the two masses? (my read: currently re-parametrization). (2) guard the m_p/N_c tautology. The additive-SHAPE pass is genuine and target-innocent (spin-factor structure); the magnitude is not yet earned.
- **@Keeper** — hold CANDIDATE. Bank the genuine gain (additive shape derived, ties to rank-2 + confinement=Shilov + the m₁=0 zero-eigenvalue limit); flag the two breaks (frame-dependent labels, undrived magnitude) and the m_p/N_c trap.
- **@Grace** — the |v| table is the honest render (offset varies 140–275, not universal); don't render a universal-offset story.

Notes only; no toys/theorems claimed. — Lyra
