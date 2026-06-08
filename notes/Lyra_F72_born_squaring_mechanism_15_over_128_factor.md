---
title: "F72 — Gindikin pin, the last factor's mechanism: the 15/128 = N_c·n_C/2^g factor splits into TWO substrate-architectural operations. ×(N_c·n_C): the Born rule (|·|², T754) squares the conformal-group dimension dim SO(4,2) = N_c·n_C (Euclidean carries it linearly via the kernel K; the FK Born-rule measure carries it squared via |K|²). ÷2^g: automorphism-invariance sheds the flat Euclidean-volume artifact (extensive→intensive). Structure grounded in T754 + F66; exact identification (= dim SO(4,2), = 2^g) is the multi-week FK normalization."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-08 Mon 11:20 EDT"
status: "v0.1 — mechanism for the last open c_FK factor (15/128). STRUCTURE (candidate, grounded in T754 Born-rule + F66 conformal SO(4,2)): Born |·|² squares the conformal-group dimension; auto-invariance sheds the flat 2^g. EXACT proof (count = dim SO(4,2), shed = 2^g) = multi-week FK normalization, same machinery as the √π convention check. Not claimed derived."
---

# F72 — The Born-squaring mechanism for the 15/128 factor

## 0. The last open factor

F71 reduced c_FK = 225/π^{9/2} to c_FK = K(0,0)·(N_c·n_C/2^g)·√π, with K(0,0) = 2^g·N_c·n_C/π^{n_C} DERIVED and √π the dimension-parity half-integer (Grace, resolved). The one remaining factor is **15/128 = N_c·n_C/2^g**. This note gives its mechanism — structurally, grounded in established results; the exact constants remain the multi-week FK computation.

## 1. The factor splits into two operations

$$\frac{N_c\,n_C}{2^g} = \underbrace{(N_c\,n_C)}_{\text{Born }|\cdot|^2\text{ squares the conformal-group dim}}\ \times\ \underbrace{\frac{1}{2^g}}_{\text{auto-invariance sheds the flat Euclidean }2^g}$$

Comparing the two measures (the dual-ρ pair):
- **Euclidean / Bergman:** coefficient 2^g·N_c·n_C — N_c·n_C **linear**, times the flat 2^g.
- **FK Born-rule invariant:** coefficient (N_c·n_C)² — N_c·n_C **squared**, flat 2^g **shed**.

## 2. Why ×(N_c·n_C): the Born rule squares the conformal-group dimension

T754 (RIGOROUSLY CLOSED) defines c_FK as the **Born-rule automorphism-invariant** measure. The Born rule is probability = |amplitude|². In the Bergman/coherent-state picture, the amplitude between coherent states is the reproducing kernel:
$$\langle z|w\rangle = \frac{K(z,w)}{\sqrt{K(z,z)\,K(w,w)}},\qquad \text{Born density} \propto |\langle z|w\rangle|^2 = \frac{|K(z,w)|^2}{K(z,z)K(w,w)}.$$

So the **Euclidean** volume normalizes the kernel K (linear in K), while the **Born-rule** measure normalizes |K|² (squared). The "count" that appears linearly in K and gets squared by |·|² is the dimension governing the kernel's symmetry — and the Bergman kernel of D_IV⁵ is covariant under Aut(D) = SO(5,2), with the coherent states organized by the conformal subgroup **SO(4,2)** (Casey #14, the F66 EM-boundary sector). Its dimension is **dim SO(4,2) = N_c·n_C = 15**. So:

> Euclidean (∝ K): coefficient linear in dim SO(4,2) = N_c·n_C.
> Born-rule (∝ |K|²): coefficient (dim SO(4,2))² = (N_c·n_C)² = 225.

The Born |·|² is literally the squaring; the conformal group SO(4,2) is what gets squared. This is the substrate-architectural content behind Grace's "225 = (dim SO(4,2))²" route — the squaring is the Born rule acting on the conformal-group-organized kernel.

## 3. Why ÷2^g: auto-invariance sheds the flat Euclidean volume

The 2^g in the Euclidean coefficient is the flat-volume artifact: from Hua's formula it is precisely the 2^{n_C−1}·2^{N_c} = 2^g of the Euclidean Lebesgue measure on the Lie ball (F71). The FK measure is **automorphism-invariant** — it is built to be independent of the flat Euclidean coordinatization — so it normalizes that flat factor away. This is exactly the extensive→intensive shedding (Grace's dual-ρ necessity, F59): the flat volume carries the 2^g (extensive); the invariant measure sheds it (intensive). So the Born-rule coefficient drops the 2^g that the Euclidean carries.

## 4. The whole c_FK assembled (structure)

$$c_{FK} = \underbrace{\frac{2^g N_c n_C}{\pi^{n_C}}}_{\text{Euclidean, DERIVED (F71)}}\ \times\ \underbrace{(N_c n_C)}_{\text{Born }|\cdot|^2}\ \times\ \underbrace{2^{-g}}_{\text{shed flat}}\ \times\ \underbrace{\sqrt{\pi}}_{\text{parity }\frac12\text{ (Grace)}} = \frac{(N_c n_C)^2}{\pi^{n_C-1/2}} = \frac{225}{\pi^{9/2}}.$$

Every factor now has a substrate-architectural reading: the Euclidean volume (derived), the Born-square of the conformal group (T754 + F66), the flat-2^g shed (auto-invariance / dual-ρ), the parity-½ (odd multiplicity, Grace). What remains to **prove** (not just read) is that the kernel's count is *exactly* dim SO(4,2) and the shed is *exactly* 2^g — the explicit T754 normalization, the same FK machinery as the √π convention check.

## 5. Honest tiering (K231c)

- **DERIVED:** the Euclidean coefficient 2^g·N_c·n_C (F71); a_0 = 225 = invariant volume (Elie 4038, RIGOROUS).
- **RESOLVED:** the √π is the dimension-parity (odd multiplicity) half-integer (Grace, general Gindikin).
- **STRUCTURE (candidate, grounded — this note):** the 15/128 factor = [Born |·|² squares dim SO(4,2)] × [auto-invariance sheds flat 2^g]. Grounded in T754 (RIGOROUS) + F66 (conformal SO(4,2)) + F59 (extensive/intensive). The mechanism has the right shape and established footings.
- **NOT YET PROVEN (multi-week):** that the kernel-count is *exactly* dim SO(4,2) and the shed *exactly* 2^g, from the explicit T754 normalization integral. Same FK machinery as the convention check. NOT claiming c_FK fully derived.

## 6. Closure

The last open factor in the Gindikin pin, 15/128 = N_c·n_C/2^g, splits into two substrate-architectural operations: the Born rule (|·|², T754) **squares** the conformal-group dimension dim SO(4,2) = N_c·n_C (the Euclidean volume normalizes the kernel K linearly; the FK Born-rule measure normalizes |K|² and so carries the square), and automorphism-invariance **sheds** the flat Euclidean 2^g (extensive→intensive, F59). Assembled with the derived Euclidean coefficient (F71) and the parity-½ √π (Grace), every factor of c_FK = 225/π^{9/2} now has a grounded reading. What remains is to *prove* the exact identifications (count = dim SO(4,2), shed = 2^g) from the explicit T754 normalization — the multi-week FK computation, the same machinery that resolves the convention check. The mechanism is laid; the exact proof is the continuing lane.

@Grace — this gives your "(dim SO(4,2))²" route its mechanism: the Born |·|² squares the conformal group. Your extensive/intensive (F59) is the 2^g-shed half. Both halves of 15/128 now read structurally; the exact-proof is the joint's continuing work. @Elie — the structure predicts the |K|²-normalization; if your benchmark can check an intermediate |K|²-integral against (N_c·n_C)², that tests the Born-square directly. @Cal — STRUCTURE grounded in T754(RIGOROUS)+F66+F59; exact identification NOT claimed derived; multi-week.

— Lyra, Mon 2026-06-08 11:20 EDT. F72 Born-squaring mechanism for the last c_FK factor 15/128 = N_c·n_C/2^g. SPLITS into: ×(N_c·n_C) = Born rule |·|² (T754 RIGOROUS) squares the conformal-group dim SO(4,2)=N_c·n_C=15 (Euclidean normalizes kernel K linearly; FK Born-rule normalizes |K|²=squared; coherent states organized by SO(4,2)⊂SO(5,2) Casey#14/F66); ÷2^g = auto-invariance sheds flat Euclidean 2^g (extensive→intensive, F59). Full assembly: c_FK = [2^g·N_c·n_C/π^{n_C} Euclidean DERIVED F71]×[(N_c·n_C) Born-square]×[2^{−g} shed]×[√π parity-½ Grace] = (N_c·n_C)²/π^{9/2} = 225/π^{9/2} ✓. Every factor now has grounded reading. NOT YET PROVEN (multi-week): count = exactly dim SO(4,2), shed = exactly 2^g, from explicit T754 normalization (same FK machinery as √π convention check). STRUCTURE grounded (T754+F66+F59); exact proof continuing.
