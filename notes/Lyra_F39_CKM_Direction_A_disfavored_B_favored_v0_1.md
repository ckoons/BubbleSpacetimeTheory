---
title: "F39 — CKM color² Direction A is disfavored, Direction B favored (color-counting); corrects F36 lean"
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-06 Saturday 12:50 EDT"
status: "v0.1 — Phase 5; one clean finding + F36 self-correction. Direction A (rate-primitive) does not resolve color², it relocates it; Direction B (two-endpoint color sum) is the candidate"
---

# F39 CKM color² — Direction A disfavored, B favored

## 0. Goal

F36 named two directions for the substrate-color² source in sin θ_C = N_c²/(2^{N_c}·n_C) = 9/40 = λ, and tentatively leaned toward Direction A (the forced primitive is the rate sin²θ_C, where N_c² is "natural as a two-trace"). Pulling Direction A at depth shows that lean was wrong. This corrects it.

## 1. Direction A does not resolve color² — it relocates it

The claim was: if the substrate forces the *rate* sin²θ_C rather than the amplitude, then N_c² is the natural two-color-trace factor of |amplitude|². Check the color powers:

- amplitude sin θ_C = N_c²/(2^{N_c}·n_C) = 9/40 — carries **N_c² (two color powers)**.
- rate sin²θ_C = N_c⁴/(2^{N_c}·n_C)² = 81/1600 = λ² — carries **N_c⁴ (four color powers)**.

A rate carries two color traces (|amp|²). So a rate with N_c⁴ requires the *amplitude* to carry N_c² — which is exactly the thing we were trying to explain. Direction A therefore does not make N_c² natural; it pushes the question from "why N_c² in the amplitude" to "why N_c⁴ in the rate = (N_c² amplitude)²." **Same puzzle, relocated.** Direction A is disfavored.

## 2. Direction B is the candidate, and F24's "3" doesn't refute it

Direction B: the amplitude carries N_c² because the substrate mixing matrix element ⟨V_{gen-1}⊗color | T_W | V_{gen-2}⊗color⟩ has **two independent color sums** — the gen-1 (down) quark's color triplet and the gen-2 (strange) quark's color triplet — summed independently in the Bergman inner product, rather than tied by a single δ as in the SM color-diagonal single-trace picture.

F24 v0.1 reported a color factor of 3 (not 9) and seemed to block Direction B. But F24 computed the **Sym^k symmetric-power index combinatorics** (1×3 across the gen-1→gen-2 K-types), which is the *representation degree* structure — not the color-triplet index sums. Those are different objects: the Sym^k degree is the Sp(2) symmetric-power count (Ch 7); the color sum is over the SU(N_c=3) triplet attached to each quark. F24's "3" is a category mismatch with the color² question and does **not** refute Direction B.

## 3. The sharpened test

The question is now single and concrete: in the substrate Bergman matrix element for d→s mixing, are the initial-quark and final-quark color sums **independent** (⟹ N_c × N_c = N_c² in the amplitude, Direction B confirmed) or **tied** by color conservation to a single trace (⟹ N_c, and 9/40 is not color²)?

- If independent: N_c² in the amplitude is forced, sin θ_C = N_c²/(2^{N_c}·n_C) = λ is a genuine substrate-mechanism form, and the color-diagonal-single-trace intuition simply fails because the two quarks live in *different* generation K-types whose color indices are not identified.
- If tied: 9/40 = λ remains an excellent identification (0.000%) but the "9" is not color² — it is one of the Casey #5 composites (e.g. 2^{N_c}+1, or C_2+N_c), and the color reading is retired.

This is a clean falsifiable fork, resolvable by the explicit FK Bergman color-tensored matrix element (the same Ch 7 machinery F38 needs for ε). One computation decides it.

## 4. Honest status

- **Corrected (F36 self-fire):** Direction A (rate-primitive) is disfavored — it relocates the N_c² puzzle to N_c⁴, does not resolve it.
- **Favored:** Direction B (two independent endpoint color sums) is the candidate; F24's "3" is a category mismatch (Sym^k degree, not color sum) and does not refute it.
- **Test:** are the d and s color sums independent or tied in the substrate matrix element? Independent ⟹ N_c² forced; tied ⟹ 9 is a Casey #5 composite, color reading retired. Decidable by the explicit FK color-tensored matrix element.
- **Tier:** F39 v0.1 diagnostic; substrate-color² source OPEN, fork sharpened to one computation; multi-week per Cal #189.

## 5. Closure

Pulling CKM Direction A showed it disfavored: making the rate the primitive relocates N_c² to N_c⁴ rather than explaining it. Direction B (two independent color sums, one per generation-K-type endpoint) is the real candidate for N_c² in the amplitude, and F24's earlier "3" computed symmetric-power degrees, not color sums, so it does not block B. The open question is now a single falsifiable fork — are the endpoint color sums independent or tied — decidable by the same FK color-tensored Bergman matrix element that F38 needs for ε. Two of my Phase 5 threads (vacuum ε, CKM color²) now converge on one computational tool.

— Lyra, Sat 2026-06-06 12:50 EDT. F39 v0.1: CKM Direction A (rate-primitive) DISFAVORED — rate sin²θ_C has N_c⁴, so making it primitive relocates the N_c² puzzle (amplitude) to N_c⁴ (rate) rather than resolving it; corrects F36's tentative lean toward A. Direction B (two independent endpoint color sums, gen-1 d-quark color × gen-2 s-quark color, in the Bergman matrix element) is the candidate for N_c² in the amplitude; F24's "3" computed Sym^k degree not color sum — category mismatch, does NOT refute B. Sharpened fork: are d,s color sums independent (N_c² forced) or tied (9 = Casey #5 composite, color reading retired)? Decidable by explicit FK color-tensored matrix element — same Ch 7 tool F38 needs for ε. multi-week per Cal #189.
