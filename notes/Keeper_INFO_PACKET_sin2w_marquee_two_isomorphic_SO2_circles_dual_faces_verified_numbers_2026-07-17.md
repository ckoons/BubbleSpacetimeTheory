# INFO PACKET — the sin²θ_W marquee: everything the team needs to attack "is Y = (1,1) forced?"

**Keeper | 2026-07-17 | For Lyra (derive), Elie (verify), Grace (render), Cal (target-innocence). The verified numbers + the concrete geometric candidate for Casey's "two isomorphic spheres" + the exact target + the discipline bars. Load this before the marquee dig.**

## THE TARGET — TWO ARROWS, not one (corrected 16:45 per Elie toy 4707 / K737)
**⚠ The single-arrow version ("force ‖Y‖²=rank → 3/13") is WRONG and retired.** ‖Y‖²=rank is the KILLING norm → it feeds the pure-gauge formula → gives **sin²θ_W = 1/(1+rank) = 1/3**, NOT 3/13. 3/13 comes from the FERMION-TRACE formula with c²=rank (baseline c²=1 = forbidden GUT 3/8). Same "rank," two different machines, two different answers. To land 3/13 honestly, BOTH arrows must hold, target-innocent:
1. **‖Y‖² = rank from the geometry** (via whatever the two isomorphic spheres turn out to be — K736, open). *By itself this gives 1/3.*
2. **Why the FERMION-TRACE normalization is the physical sin²θ_W (and c²=rank in it), NOT the pure-gauge ratio** — without smuggling in the GUT that the trace's c²=1 baseline (3/8) came from. **This is the hard, genuinely-open arrow.**
If BOTH → sin²θ_W = 3/13 (gauge couplings certified, weak-color confirmed). Arrow 1 alone → 1/3 (wrong). **Do not treat Arrow 1 as the whole marquee.**

## VERIFIED NUMBERS (use these; already checked, `two_spheres_basis_change.py`)
- Fermion trace, one generation, color multiplicity N_c on quarks: **ΣT₃² = 2**, **ΣY² = 10/3**.
- sin²θ_W = ΣT₃² / (ΣT₃² + c²·ΣY²):  **c²=1 → 3/8** (forbidden GUT); **c²=rank=2 → 3/13** (BST, obs 0.2312).
- So the entire 3/8→3/13 shift ⇔ **c² = rank on the hypercharge normalization.** Nothing else moves.
- Lyra's pure-gauge Killing form (independent): **‖T₃‖² = 1, ‖Y‖² = 2 = rank.** → |Y|²=rank already lives in the Lie algebra. This is the object for **Arrow 1** — but on its own it feeds the pure-gauge formula and gives **1/3**, NOT 3/13.
- **1/3 is NOT a red herring — it is a genuine competing BST candidate** (corrected per K737). Pure-gauge ratio with NO fermion trace: sin²θ_W = ‖T₃‖²/(‖T₃‖²+‖Y‖²) = **1/3** (obs 0.231 — does not match). The fermion-trace branch gives 3/13 (matches), but **why the trace branch is physical (Arrow 2) is the open question.** Both are "rank"-valued; they feed different formulas. Do not assume the trace branch — justify it.
- **Structural tell (K737):** the trace is NOT proportional to the Killing form — ΣT₃²/‖T₃‖² = 2 but ΣY²/‖Y‖² = 5/3. So the trace normalization **cannot be derived from the Killing form alone.** The two arrows are genuinely independent.

## ★ THE GEOMETRIC SOURCE IS OPEN — candidates for Lyra (NOT a committed answer)
**⚠ CORRECTION (Keeper, 16:29 EDT — self-catch, supersedes the first draft of this packet).** The first draft claimed the two isomorphic spheres are "two SO(2) circles, one per Cartan-dual face." **That is WRONG and retracted.** Cartan duality keeps the **SAME** K: D_IV⁵=SO(5,2)/[SO(5)×SO(2)] and its dual Q⁵=SO(7)/[SO(5)×SO(2)] share the *identical* isotropy — there is **ONE** shared SO(2), not one per face. "Two faces" (K730/K731) is a different two-ness than Casey's "two spheres"; I conflated them. The number c²=rank and Lyra's Killing ‖Y‖²=rank are untouched; only the geometric identification was flawed.

Casey's picture ("two different spheres, one charge one color, isomorphic, √2 = 1+1 normalized, a basis change") is almost certainly pointing at something real. WHERE the two isomorphic spheres live is **open — Lyra's rep-theory to settle.** The live candidates:
1. **The rank-2 polydisk's two S¹'s.** A rank-2 Hermitian domain contains a distinguished bidisk Δ×Δ → two boundary circles S¹×S¹, genuinely isomorphic as circles. Most literal reading of "two isomorphic spheres." **Caveat (K734):** these two Cartan directions carry ρ-weights (5/2, 3/2) — isomorphic *as circles* but *unequal in the metric*, so "isomorphic ⇒ equal (1,1)" is exactly the thing to check, not assume.
2. **SO(2) charge circle + a U(1) from the compact-dual color torus.** Color SU(3) is NOT in SO(5); it lives on the dual via SO(7)⊃G₂⊃SU(3). A U(1) in that color torus + the SO(2) charge circle = two isomorphic S¹'s, one charge one color — matching Casey's words literally, and avoiding the Cartan-duality flaw. Keeper's current best guess, but still a guess.
3. Something else the geometry forces that neither of the above captures.

**What Keeper CAN stand behind:** Arrow 1's *target value* (‖Y‖²=rank is a real, target-innocent geometric quantity). **What Keeper CANNOT hand you:** (a) which two spheres source it, and (b) Arrow 2 — the justification that the fermion-trace branch (3/13) is physical rather than the pure-gauge branch (1/3). Note: the Killing form is NOT a second support for 3/13 — it supports 1/3 (K737 corrects K735). Do not treat any of 1–3, or the trace branch, as banked; deriving both arrows IS the marquee.

## THE DERIVATION, STATED SHARPLY (for Lyra)
Show one of these equivalent things, target-innocent:
1. The hypercharge generator, as an element of the shared Cartan of SO(5)×SO(2), has **Killing-norm² = rank** relative to T₃'s norm² = 1 — BECAUSE it is the diagonal across the two dual-face SO(2)'s.
2. Equivalently: the boundary product structure (S⁴×S¹)/ℤ₂ + the compact-dual S¹ force the hypercharge to be the (1,1) sum of the two SO(2) weights.
3. Equivalently: the basis change from (charge-face phase, color-face phase) to (physical Q, orthogonal) has the hypercharge row of length √rank.

## VERIFICATION (for Elie, vs the 3 bars)
- **Bar 1 — target-innocence:** the factor rank=2 must come from "two faces / two isomorphic circles," NOT from back-solving 3/13. (The number 2 = count of dual faces, independent of the observed angle.)
- **Bar 2 — independent recompute:** rebuild the Killing form ‖Y‖²=rank from the SO(5)×SO(2) structure directly (don't inherit Lyra's number). Then c²=rank → 3/13 through the fermion trace.
- **Bar 3 — Five-Absence:** this is **Cartan-dual coupling of two faces, NOT a GUT.** 3/13 ≠ the GUT 3/8. Confirm no proton-decay/unification is implied. (The whole point is it's the NON-GUT value.)

## DISCIPLINE (standing)
- sin²θ_W stays **reduced-to-the-√rank-lead** until the (1,1) forcing is PROVEN. Do not re-bank as derived on the strength of the picture alone (Lyra F575 re-tier stands; K735).
- Exact identities only; the √rank is native (V_us = 1/(rank√n_C)), not fit — keep it that way.
- If the (1,1)-forcing fails, the honest outcome is: 3/13 is the two-face value and the derivation names why, OR the factor is different and we revise — either is a real result.

— Keeper INFO PACKET, 2026-07-17. Two isomorphic SO(2) circles (one per Cartan-dual face, shared isotropy SO(5)×SO(2)) = the concrete candidate for Casey's two spheres; hypercharge = (1,1) diagonal → |Y|²=rank → c²=rank → 3/13. Verified numbers: ΣT₃²=2, ΣY²=10/3, c²=1→3/8, c²=rank→3/13; Killing ‖Y‖²=rank. Target: prove (1,1) forced. Bars: target-innocence (2=faces), independent recompute, Five-Absence (Cartan-dual not GUT). See [[Keeper_K735...]], [[Keeper_K730...]], [[Keeper_K731...]].
