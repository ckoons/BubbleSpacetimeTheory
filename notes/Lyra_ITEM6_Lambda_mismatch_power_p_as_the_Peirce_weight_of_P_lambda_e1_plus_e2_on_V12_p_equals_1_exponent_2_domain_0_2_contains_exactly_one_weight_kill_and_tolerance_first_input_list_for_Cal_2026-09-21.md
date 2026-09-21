# Lyra — ITEM 6 OPENS (Casey's word, 2026-09-21): Λ's mismatch power p as linear algebra on D_IV⁵. Claim: p is the weight of the Jordan quadratic representation P(λe₁ + e₂) on the Peirce space that carries the residual; the three weights are {2, 1, 0} on {V₁₁, V₁₂, V₂₂}; the open domain (0, 2) of the thermostat form contains exactly one of them, p = 1, on V₁₂ — the descent's spatial sector. Prediction (blind, Elie): Λ/Λ_P = (t_K/t_P)². Cal hashes the input list before the number.
**Lyra, 2026-09-21 (Monday), 09:09 EDT (clock). Register F2; Lecture 9:56–65, 76, 81; controls T2571 and the K1057 cap. `didwe "mismatch power"` = 0 rows; `didwe "thermostat"` = 3 (K426, F219, F223: June interstasis/de Sitter rows, none on p). Written before any number; I have not evaluated t_K/t_P and will not.**

## 0. The kill, first (as Casey ordered)
- **Form limb.** The exponent 2p/(2−p) is monotone on [0, 2) with a pole at p = 2 and a sign flip beyond. A forced p ∉ (0, 2) falsifies the FORM. Under the derivation below p = 1 ∈ (0, 2): the form survives this limb. If Cal's hash of the inputs finds the residual on V₁₁ or V₂₂ instead (Section 3), p = 2 or 0 and the form dies — that is the can-fail.
- **Value limb, with its tolerance stated now.** The form Λ/Λ_P = (t_K/t_P)^(2p/(2−p)) carries no prefactor and no free scale; its only slack is the O(1) prefactor a fixed-point balance never fixes. **Tolerance: one decade — |log₁₀(Λ_pred/Λ_obs)| ≤ 1**, with Λ_P = 1/ℓ_P² and Λ_obs the Planck 2018 value in those units, both pinned by Elie in the prereg. A forced p inside (0, 2) whose Λ misses by more than one decade falsifies the VALUE of the form at this bank of t_K/t_P (T2405, the candidate form α^(C₂²)); the derivation's weakest input is then (iii) below, and T2405's bank is the second suspect.
- **Blindness, honestly.** Λ_obs ℓ_P² ~ 10⁻¹²² is public physics and I cannot un-know its order; what is blind is Elie's evaluation of the exponent and of t_K/t_P from the bank, under Cal's hash, with Λ_obs excluded from the script. I have not computed (t_K/t_P)² and this note contains no value.

## 1. The objects (all banked)
- D_IV⁵ ≅ the spin-factor Jordan algebra J = ℝ ⊕ ℝ⁵ of rank 2 (Lecture 2); Jordan frame (e₁, e₂), e₁ + e₂ = 1. Peirce decomposition of ℂ⁵ = V₁₁ ⊕ V₁₂ ⊕ V₂₂, complex dimensions 1 + 3 + 1 (T2545: V₁₂ = J_{1/2}, dim n_C − 2 = 3 = the short-root multiplicity a).
- The descent (Lecture 9, T2545): one idempotent, codimension one, signature (3,1): the **3** is V₁₂ (the real-SO(3) vector by Frobenius–Schur type), the **1** is the time line V₁₁ = ℂe₁ — the Peirce-1 space of the idempotent the descent is built on; V₂₂ = ℂe₂ is the dropped direction.
- The thermostat (F2; Elie's Lane Λ record 08-26): Λ/Λ_P = (t_K/t_P)^(2p/(2−p)); p = "how many ticks' worth of action per horizon cycle escape absorption ≡ the 5D→4D reduction of the residual"; t_K/t_P banked as a candidate form by T2405.
- The Jordan quadratic representation: for a = λ₁e₁ + λ₂e₂, **P(a) acts on V_ij by λ_i λ_j** (Faraut–Korányi, Peirce multiplication rules) — the grading the standing order asks for.

## 2. The derivation (four lines)
1. The residual is a per-cycle action mismatch; action is quadratic in the fields; so the residual's scaling under a rescaling a of the Jordan frame is P(a), not L(a): weights λ_iλ_j on V_ij.
2. The tick ratio λ = t_K/t_P is a ratio of two clocks along the time line of the descent, V₁₁ = ℂe₁. It is carried by the one-parameter family a(λ) = λe₁ + e₂ — the time idempotent scaled, the dropped idempotent held. (Not the SO(2) centre: that is a phase, not a scale, and it would put every sector at weight 2, the pole.) **This is input (iii).**
3. Under P(a(λ)): V₁₁ → λ², V₁₂ → λ¹, V₂₂ → λ⁰. The "mismatch power" of a sector is its weight: **p ∈ {2, 1, 0}**.
4. The thermostat's domain (0, 2) is the open interval between the extreme weights; it contains exactly one weight, 1, on V₁₂. **So the residual can sit in (0, 2) only if it is carried by the middle Peirce space V₁₂ — the descent's three spatial directions — and then p = 1 exactly.** V₁₁ (p = 2) is the pole: the time line is fully absorbed by construction (the clock is the thermostat). V₂₂ (p = 0) is the dropped direction: unsuppressed but invisible to the 4-space — it is not in the descent's image and cannot enter a 4D Λ. That is why the power sits in (0, 2): the geometry has three sectors, the form's domain admits one, and it is the sector the descent keeps as space.

**Result: p = 1, exponent 2p/(2−p) = 2, Λ/Λ_P = (t_K/t_P)².** A mixture of sectors would give a sum of two powers, not one; the form assumes one power, so the derivation is either V₁₂ alone or the form is wrong.

## 3. Input list for Cal's hash (five items; (iii) is the only one that is mine)
(i) Peirce decomposition of the rank-2 spin factor with dims (1, 3, 1) — T2545, Lecture 2. (ii) The descent's assignment time = V₁₁, space = V₁₂, dropped = V₂₂ — T2545, Lecture 9. (iii) The tick ratio is carried by a(λ) = λe₁ + e₂ (time scaled, dropped idempotent held) — Lyra, this note, Section 2 line 2. (iv) P(a) acts on V_ij by λ_iλ_j — Faraut–Korányi. (v) The thermostat form and its domain — F2, Lecture 9:62–65, Elie 08-26. **Circularity check:** no input mentions Λ, Λ_obs, or the residual's size; p is read off a grading; the target enters only at Elie's compare step.

## 4. Elie's task (blind, under Cal's hash)
Compute t_K/t_P from T2405's banked form and nothing else; raise it to the exponent 2p/(2−p) at p = 1; pin Λ_P and Λ_obs (Planck 2018) in the prereg with the target excluded from the script's inputs until the compare line; controls: (C1) p = 2 must return the pole; (C2) p = 0 must return Λ/Λ_P = 1; (C3) T2571's un-fed reproduction must still pass. Report |log₁₀(Λ_pred/Λ_obs)| against the one-decade tolerance. Toy counter: read `play/.next_toy` before creating.

## 5. What would make this note wrong
A Peirce sector other than V₁₂ shown to carry the residual (kills the form, Section 0); a scaling of the frame other than a(λ) shown to carry the tick ratio (my input (iii)); a P(a)-weight on V₁₂ other than λ (it is λ₁λ₂ = λ·1; this is not in doubt); T2571 or the K1057 cap failing under the exponent 2.

— Lyra. Derivation only; the number is Elie's.
