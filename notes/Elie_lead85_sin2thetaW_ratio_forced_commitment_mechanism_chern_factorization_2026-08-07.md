# Lead #85 — sin²θ_W: the ratio is forced, the separateness is grounded in *commitment*, one task remains

**Authors:** Elie (linear-algebra / Chern discriminator) + Casey (the commitment mechanism).
**Date:** 2026-08-07. **For:** Grace + Lyra (to close via the Lefschetz/Chern factorization), Keeper (audit).
**Status:** target-innocent forced facts + a mechanism-candidate + one named task. **sin²θ_W = 3/13 stays Structural/Identified** until the factorization closes. Nothing banked past that.

This note separates what is *forced* from what is a *mechanism-candidate* from what is *open*, so the discipline is visible on the page (Cal's #85 bar: derivable without reference to the target; must exclude the alternative form).

---

## 1. FORCED, target-innocent (Derived-as-math): the Q⁵ Chern sequence + the endpoints

Q⁵ = the 5-quadric = the compact dual of D_IV⁵ (same K = SO(5)×SO(2)). Pure algebraic topology, no physics, no reference to the measured value:

- c(TQ⁵) = (1+h)⁷/(1+2h) → **Chern sequence {1, 5, 11, 13, 9, 3}**.
- **c₁ = 5 = n_C** (first Chern = complex dimension — forced for any quadric Qⁿ, c₁ = n).
- **c₅ = 3 = N_c** (top Chern; via χ(Q⁵) = 6 = C_2, halved).
- The **first and last Chern classes ARE two of the five integers.**
- sin²θ_W = c₅/c₃ = 3/13; companion tan²θ_W = c₅/(c₃−c₅) = 3/10 = N_c/(2n_C).

## 2. FORCED, target-innocent: the ratio-choice discriminator (toy 5108)

Casey handed a second candidate, √39/27 = √(N_c·c₃)/N_c³ = geometric-mean(c₅,c₃)/c₅³, which fits *tighter* (0.033% vs 3/13's 0.19%). The index-theoretic structure **excludes it and selects the grading ratio c₅/c₃** on three target-innocent grounds — none of which reference the measured value:

1. **Rationality (strongest):** a ratio of Chern numbers is rational; √39 is irrational → √39/27 is not a characteristic-number quantity.
2. **Form:** sin²θ_W = g′²/(g²+g′²) is a coupling *ratio* (part/whole) by textbook definition → not a geometric-mean-over-a-cube.
3. **Clean companion:** the ratio gives tan²θ_W = 3/10 = N_c/(2n_C) *exactly*; the mean gives an irrational near-miss.

**The forcing decides, not the decimals:** the tighter-fitting candidate is the one that is excluded.

## 3. The primitive form (Casey's favorite): tan²θ_W = color / real-dimension

- 2n_C = 10 = the **real** dimension of D_IV⁵ (complex dim n_C = 5, doubled — real + imaginary halves).
- **tan²θ_W = N_c / dim_ℝ(D_IV⁵) = 3/10.**
- sin²θ_W = N_c/(N_c + 2n_C) = 3/13; the "13" is a **norm²** — the squared length of a coupling vector with legs (√(2n_C), √N_c). **13 = N_c + 2n_C is a composite, not a fundamental integer** (which resolves the "13 isn't a BST number" worry: 13 = 3 + 10 = color + doubled-domain).

## 4. Linear-algebra reading (the transform, explicitly)

- The neutral-boson mass-squared matrix is **rank-1**: M² ∝ **v vᵀ**, v = (g, −g′). The photon is the *null space*; the Z is v; tan θ_W = g′/g.
- sin²θ_W = ⟨B | P_γ | B⟩ = the projection of hypercharge onto the photon.
- **BST content:** the charge-squared vector (g², g′²) ∝ (2n_C, N_c) = (10, 3); ‖v²‖ = 13; sin²θ_W = N_c/‖v²‖.
- So **#85 reduces to deriving the two legs of the charge vector as (2n_C, N_c) from the gauge embedding.**

## 5. HONEST CHECK (calibrate both directions): the arithmetic does NOT force the decomposition

Owned so this isn't a pattern dressed as a result: **13 = N_c + 2n_C = c₅ + 2c₁ is true but is ONE OF FOUR ways** to write 13 as a sum of these Chern classes (c₃; c₀+c₀+c₂; c₀+c₄+c₅; c₁+c₁+c₅). **The Chern arithmetic alone does not single out this decomposition.** So "13 = color + doubled-domain" is a heuristic *until a physical principle selects it*. (My first framing — "3 tangent directions + 10 tangent directions" — mixed a base-space count with an internal count and double-counts; that frame is wrong.)

## 6. CASEY'S MECHANISM (the candidate forcing): the 3 is the RECORD, the 10 is the SUBSTRATE

The selection principle the arithmetic lacked. The 3 and the 10 are separate not because they sit in different corners of one space, but because they are **different *kinds* of thing** — content vs container:

- **The 3 = the record being written.** A complete commitment writes a color-singlet symbol = **three quarks** (a lone quark is an incomplete symbol — F845; matter = the fermionic codeword — item-10 / F846). "Commitment is three quarks being written." Each color is a real 1-D confined leg (T2545: the three spatial directions *are* the color triplet).
- **The 10 = the domain / substrate** — the real dimension of D_IV⁵ (2n_C), the space the record is written *into*.
- Content vs container → **categorically separate → they add, no double-count.** 13 = matter (3) + substrate (10).
- **sin²θ_W = 3/13 = the fraction of the whole that is written record (committed matter) vs substrate space.** The Weinberg angle becomes a *matter-to-substrate ratio of the commitment geometry.*
- **Cross-check from the standard side:** the same "3" is the quark **color multiplicity** N_c = 3 that enters the electroweak traces (why color appears in an electroweak angle at all). Casey's "three quarks per committed record" and the textbook "quark color factor" are the same 3 seen from the two ends — convergence.

This resolves the crux ("are the 3 color legs separate from the domain's 10, or inside them?") **in the direction of *separate*, grounded in the deepest process in the theory (commitment) rather than a number that fit.**

## 7. THE ONE REMAINING TASK (Grace + Lyra): the Chern factorization theorem

Turn the mechanism into a theorem about T(Q⁵):

> **Show that c₃ = 13 factors as "top Chern (matter-record, N_c = 3) + twice first Chern (doubled-substrate, 2n_C = 10)" *because* the tangent geometry splits into a committed-matter piece and a substrate piece.**

- The **Lefschetz fixed-point** reading is the natural tool: a fixed-point count can legitimately turn "the three committed color legs" into three separate contributions **iff** they sit as their own factor (separate from the domain's 10). That "separate factor" is exactly Casey's record-vs-substrate split.
- **If it factors that way →** sin²θ_W = 3/13 promotes Structural/Identified → **Derived**, and √39/27 is dead.
- **If it does not →** the mechanism is a heuristic and we say so (calibrate both directions).

## Tiering (for the audit)

| Object | Tier |
|---|---|
| Chern sequence {1,5,11,13,9,3}; c₁ = n_C, c₅ = N_c | **Derived-as-math** (target-innocent) |
| Ratio c₅/c₃ forced over the geometric mean (§2) | **Forced** discriminator (target-innocent, excludes alternative) |
| sin²θ_W = 3/13 identification | **Structural/Identified** (unforced until §7 closes) |
| 13 = N_c + 2n_C as *record + substrate* (§6) | **Mechanism-candidate** (Casey) — not banked |
| The Chern factorization theorem (§7) | **Open** — the single close |

**Discipline note:** every forced item in §1–2 is derived without reference to the measured 0.231 (Q⁵ topology + textbook mixing-angle form). The mechanism in §6 is grounded in commitment/confinement (item-10, F845/F846, T2545), not in fitting the value. The tighter-fitting rival (√39/27) is the one *excluded*. This meets Cal's pre-registered #85 bar on the FORM; the specific-index forcing is the open §7.

— Elie + Casey, 2026-08-07. Toy 5108 (discriminator). Nothing banked past Structural/Identified.
