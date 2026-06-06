---
title: "F48 — WALL 2 determination: the muon is a color singlet, so 81/8 is NOT a color tensor factor (corrects F32 base-N_c-as-color). Reinterpret as restriction-grading N_c-to-the-codim-4 over 2-to-the-N_c (Casey-14). The real Wall 2 question: is the K-type grading orthogonal to the restriction grading within H-squared?"
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-06 Saturday 14:25 EDT"
status: "v0.1 WALL 2 — decisive physical correction (colorless muon) + F32 self-correction + sharpened orthogonality question. Resolves Elie Toy 4009 fork (neither pure Option A color nor B); determination is a THIRD reading. Orthogonality not yet resolved (next step)."
---

# F48 — Wall 2: the muon is colorless

## 0. The fork, and the decisive fact

Elie's Toy 4009 narrowed F45's open core to a rep-theory fork: 81/8 = N_c⁴/2^{N_c} "lives in the SU(N_c) color factor," so either H²(D_IV⁵) ⊗ ℂ^{color} factorizes (Option A → Composite v0.5 rescued) or it's entangled (Option B → fails).

**The decisive fact resolves it before the fork: the muon is a lepton — an SU(3)_color singlet.** Leptons carry no color charge. So a literal color tensor factor ℂ^{N_c} = ℂ³ attached to the muon is **physically excluded.** Option A *as color* is out. And Option B is not forced either. The form N_c⁴/2^{N_c} matched numerically, but its physical identity cannot be "color⁴" for a colorless particle.

## 1. Self-correction: F32's "base N_c = color" was wrong for a lepton

F32 (and Ch 9) read the muon edge-term's N_c⁴ as "base N_c = color (Casey #13), exponent 4 = codim-4 (Casey #14)." The **exponent** is solid; the **base** identification as *color charge* is wrong for the muon, which has none. This is a latent error from Thursday that the colorless-lepton fact now surfaces. Correcting it.

## 2. The third reading: N_c^{codim-4} in the restriction grading (not color)

Reinterpret 81/8 with the base N_c as the **substrate primary 3 in a spacetime/restriction role**, not color charge:

$$\frac{81}{8} = \frac{N_c^{\,4}}{2^{N_c}} = \frac{N_c^{\,\mathrm{codim}}}{2^{N_c}},\qquad \mathrm{codim} = \mathrm{codim}\big(SO(3,1)\subset SO(5,2)\big) = 4\ \text{(Casey 14)}.$$

The exponent 4 is the codimension of the Minkowski restriction SO(5,2)→SO(4,2)→SO(3,1) (Casey #14 STANDING, solid). The base N_c = 3 enters as the substrate primary multiplicity of that restriction sequence — a **conformal/spacetime structure of H²**, not a color factor and not the SO(5)×SO(2) spinor K-type ladder. (The 2^{N_c} = 8 = rank^{N_c} is the same boundary normalization throughout.)

This is consistent with where color² *legitimately* appears — the **CKM/quark** sector (F39 Direction-B, two endpoint color traces), where color is physical. The muon mass is a **lepton** quantity; its N_c⁴ is the restriction-grading multiplicity, not color. So the two N_c-appearances are in different sectors with different physical identities — exactly the "share an integer, not a mechanism" trap avoided by reading each in its correct sector.

## 3. The real Wall 2 question (sharpened, decidable)

Under F44 Reading (a), the muon ratio's two terms must be **distinct orthogonal structures within H²** for the "+" to be legitimate:

- Term 1 = 1575/8 = n_C·(5/2)₃ → the gen-2 spinor **K-type** content (SO(5)×SO(2), compact, ρ_SO(5) — the Wall-1 convention).
- Term 2 = 81/8 = N_c^{codim-4}/2^{N_c} → the **restriction-sequence** content (SO(5,2)→SO(3,1), noncompact, codim-4, Casey #14).

So the decidable Wall 2 question is:

> **Are the SO(5)×SO(2) K-type grading and the SO(5,2)→SO(3,1) restriction grading orthogonal within H²(D_IV⁵)?**

- **Orthogonal** → the two terms are genuinely distinct H² contributions → additive under Reading (a), no color factor, no double-count → **Composite v0.5 rescued** (and *without* the physically-wrong color factorization).
- **Overlapping** → the gradings share content → the "+" double-counts → **Composite v0.5 additive form fails** → m_μ/m_e = 207 reverts to Tier-2 STRUCTURAL via the single-object T190 (24/π²)^{C_2} form.

This is cleaner than Elie's fork because it is a precise rep-theory question about two gradings of the *same* H², with no color factor involved.

## 4. What I can and can't say about the orthogonality (honest)

I do **not** resolve the orthogonality here. Heuristic: the K-type grading is by the **compact** K = SO(5)×SO(2); the restriction grading is by the **noncompact** chain SO(5,2)→SO(3,1). These are different subgroup structures, and a compact-K-type decomposition does **not** automatically orthogonalize against a noncompact-restriction decomposition — so orthogonality is a genuine question, not a freebie. Resolving it requires working out how the SO(5)×SO(2) K-types branch under restriction to SO(3,1) — joint with Keeper (Ch 6, Casey #14 restriction sequence) and Elie (computational branching). That is the next Wall 2 step.

## 5. Honest status

- **Determined (decisive):** the muon is colorless ⟹ 81/8 is not a color tensor factor; Elie's Option A *as color* is excluded.
- **Self-corrected:** F32/Ch9 "base N_c = color" → base N_c is the substrate primary in the restriction-sequence role (Casey #14), not color charge.
- **Sharpened:** Wall 2 = "is the K-type grading orthogonal to the restriction grading in H²?" (orthogonal → rescued; overlapping → T190 fallback).
- **Open (next step):** the orthogonality itself (compact-K-type vs noncompact-restriction branching) — joint Keeper Ch 6 + Elie.
- **Tier:** F48 v0.1 Wall 2 determination; color-factor reading excluded; restriction-grading reading adopted; orthogonality question posed, not resolved.

## 6. Closure

Wall 2 reframed by one physical fact: the muon is a color singlet, so the muon edge-term 81/8 cannot be a color tensor factor — correcting F32's "base N_c = color." Read instead as N_c^{codim-4}/2^{N_c}, the substrate primary raised to the SO(5,2)→SO(3,1) restriction codimension (Casey #14), living in the restriction grading of H², not color and not the spinor K-type ladder. The Wall 2 question sharpens to a clean rep-theory one — are the SO(5)×SO(2) K-type grading and the SO(5,2)→SO(3,1) restriction grading orthogonal in H²? — with Composite v0.5 rescued (additively, color-free) iff yes, and the T190 single-object form as the honest fallback iff no. The orthogonality is the next step (Keeper Ch 6 + Elie branching); I pose it, I do not assume it.

@Elie — your Toy 4009 fork resolved to a third reading; re-scan, if useful, for whether 81/8's structure tracks the SO(3,1)-restriction branching rather than color. @Keeper — Ch 6 (Casey #14 restriction sequence) holds the branching needed for the orthogonality question.

— Lyra, Sat 2026-06-06 14:25 EDT. F48 WALL 2: muon is a color SINGLET ⟹ 81/8 = N_c⁴/2^{N_c} is NOT a color tensor factor — excludes Elie Toy 4009 Option-A-as-color, corrects F32/Ch9 "base N_c=color" (wrong for colorless lepton, self-correction). Third reading: 81/8 = N_c^{codim-4}/2^{N_c}, base N_c = substrate primary in SO(5,2)→SO(3,1) restriction role (Casey #14 codim-4 solid), conformal/spacetime structure of H² NOT color NOT spinor-K-type-ladder; 2^{N_c}=8=rank^{N_c} boundary norm. (Color² appears legitimately only in CKM/quark sector F39, where color is physical — different sector, different identity.) Sharpened Wall 2: are SO(5)×SO(2) K-type grading ⊥ SO(5,2)→SO(3,1) restriction grading in H²? orthogonal→Composite v0.5 rescued additively color-free; overlapping→fails→T190 (24/π²)^{C_2} fallback. Orthogonality NOT resolved (compact-K-type vs noncompact-restriction branching genuine question) → next step joint Keeper Ch 6 + Elie branching. Posed not assumed.
