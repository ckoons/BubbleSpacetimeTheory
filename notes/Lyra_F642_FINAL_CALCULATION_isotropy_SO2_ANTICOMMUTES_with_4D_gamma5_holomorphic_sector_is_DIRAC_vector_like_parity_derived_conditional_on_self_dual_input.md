# F642 — THE FINAL CALCULATION (pull 07-22k): done, and it resolves the fork to **DIRAC.** Explicit Clifford computation: the isotropy SO(2) generator (= holomorphicity = the complex structure J) **ANTICOMMUTES with the 4D chirality γ⁵**, because the physical time direction is shared between γ⁵ (spacetime volume) and the isotropy SO(2) (rotation of the 2 timelike directions). Anticommuting involutions ⟹ **a holomorphic (definite-SO(2)-charge) state is a 50/50 mix of 4D chiralities ⟹ the holomorphic sector is a 4D DIRAC fermion ⟹ VECTOR-LIKE.** Born=Bergman on the fermions alone does **NOT** give a 4D Weyl and does **NOT** close parity. **Answer: the Weyl branch fails; parity finishes DERIVED-CONDITIONAL on the self-dual/gravi-weak input** (Elie 4780 verified that route gives the chiral coupling). Geometric, non-GUT. The internal↔spacetime alignment the arc hoped for is not just unproven — it is **false at the operator level** (the two chiralities anticommute = mutually unbiased). Elie's ±4 (Dolbeault index) is real but is the DOMAIN chirality, orthogonal to spacetime γ⁵.

**Lyra, Wed 2026-07-22 ~12:32. Casey: "do the final calculation." Done. It's a clean negative for the Born=Bergman-alone hope, and a clean derived-conditional finish. Computed, not asserted.**

## The setup (explicit)
SO(5,2): 7 directions, signature (5,2) → spacelike {1,2,3,4,5}, **timelike {0,6}**.
- **Isotropy SO(2)** = the compact rotation of the two timelike directions = J_{06}; spinor generator **Σ_{06} = ½Γ_0Γ_6.** Its eigenvalue = the conformal weight c = holomorphicity (the complex structure J acts as this SO(2)).
- **Spacetime Lorentz SO(3,1)** = {0,1,2,3} (time 0, space 1,2,3). **4D chirality γ⁵ = Γ_0Γ_1Γ_2Γ_3.**
The physical time direction **0 is shared**: it is in the spacetime set (so γ⁵ contains Γ_0) AND in the isotropy timelike 2-plane {0,6} (so Σ_{06} contains Γ_0). This sharing is **forced**: there are only 2 timelike directions, the isotropy SO(2) rotates both, and Lorentz must use one of them for its time.

## The computation
Clifford commutation rule: for monomials Γ_S, Γ_T (S,T index sets), Γ_SΓ_T = (−1)^{|S||T|−|S∩T|} Γ_TΓ_S.
$$ \Sigma_{06} = \tfrac12\Gamma_0\Gamma_6,\quad S=\{0,6\};\qquad \gamma^5=\Gamma_0\Gamma_1\Gamma_2\Gamma_3,\quad T=\{0,1,2,3\}. $$
$$ |S|=2,\ |T|=4,\ S\cap T=\{0\}\Rightarrow |S\cap T|=1. \qquad (-1)^{|S||T|-|S\cap T|} = (-1)^{8-1} = (-1)^7 = -1. $$
$$ \boxed{\ \{\Sigma_{06},\ \gamma^5\} = 0\ }\qquad\text{— the isotropy SO(2) ANTICOMMUTES with 4D chirality.} $$
(Check on the boosts too: Σ_{01}=½Γ_0Γ_1, S={0,1}, vs Σ_{06}: |S||T|−|S∩T| = 2·2−1 = 3 odd → **boosts also anticommute with Σ_{06}** — i.e. holomorphicity is not even Lorentz-invariant, as expected of the conformal Hamiltonian.)

## What it means (decisive)
Σ_{06} and γ⁵ are both (proportional to) involutions and they **anticommute** ⟹ they are **mutually unbiased** (like σ_x and σ_z). Consequences:
- A state of **definite holomorphicity** (definite Σ_{06}-charge, i.e. the Born=Bergman holomorphic sector) has **⟨γ⁵⟩ = 0** — it is an equal mixture of both 4D chiralities.
- The 4-dim holomorphic sector 4_{c=+½} therefore contains **2 left-Weyl + 2 right-Weyl = a 4D DIRAC fermion.** **VECTOR-LIKE.**
- Equivalently: **holomorphicity (the internal/domain chirality) is orthogonal to the spacetime chirality γ⁵.** The internal↔spacetime alignment the whole arc needed is **false at the operator level** — not merely unproven.

## Reconciling with Elie's ±4 (no contradiction)
Elie 4777 / the F638 chamber theorem give **net Dolbeault index ±4** — a genuine, nonzero **DOMAIN chirality** (the Λ^{0,q} grading on the 10-real-dim D_IV⁵, i.e. the SO(10)-type chirality of the tangent). That is real and correct. **But it is NOT the 4D spacetime chirality γ⁵** — and this computation shows the two are mutually unbiased (anticommuting). So: Born=Bergman gives a chiral *domain* spectrum, which does **not** translate to a chiral *spacetime* spectrum. The domain-chiral sector is spacetime-Dirac. This is the precise, computed resolution of the internal-vs-spacetime crux — and it is negative.

## The verdict on the fork (F641)
- **Weyl branch (Born=Bergman closes parity, no input): FAILS.** Holomorphic ⊥ γ⁵ ⟹ the holomorphic sector is 4D-Dirac (vector-like). F640's antecedent ("Born=Bergman → 4D Weyl") is **false**, confirmed by computation — not merely unproven. My F640 confidence was wrong; F641's caution was right; this settles it.
- **Dirac branch (self-dual/gravi-weak input needed): THIS IS THE ANSWER.** 4D parity violation requires a chiral CONNECTION (the self-dual/holomorphic gauge connection), which Elie 4780 verified gives L=0,R=2 (chiral coupling). That input is **geometric** (the self-dual half of the SO(5,2) connection, cross-linking BST gravity) and **non-GUT** — Five-Absence-safe.
- **⟹ Parity finishes DERIVED-CONDITIONAL** on the self-dual-connection (gravi-weak) input. NOT closed on Born=Bergman alone. Honest, and it does finish — no third reframe.

## The honest headline
"Why is the world left-handed?" finishes as: **the fermions have a chiral DOMAIN structure (Born=Bergman, a theorem) and the SM internal content ((2,1)⊕(1,2) doublet+singlet, F639), but 4D spacetime parity violation requires the weak CONNECTION to be self-dual** — because holomorphicity is orthogonal to 4D chirality (this note). So parity = derived-conditional on the one geometric input (self-dual connection), exactly as gravi-weak says, now with the reason the fermion-only route can't do it *computed*. The clean "Born=Bergman alone closes it" was the hope; the calculation says no.

## What stands / what this closes
- **BANKED (unaffected):** chiral split (n_C odd); the chamber/Dolbeault chirality **mechanism as a theorem** (F638, a DOMAIN statement — still correct); CP-free; custodial/ρ≈1/no-W_R (T2520); 1/N_c fractionalization (T2521); charge-row hypercharge handle.
- **CLOSED (this calc):** the Weyl-vs-Dirac fork → **Dirac.** Parity = **derived-conditional on the self-dual/gravi-weak connection** (geometric, non-GUT). The Born=Bergman-alone hope is **refuted by computation.**
- **STILL OPEN (separate, unchanged):** which SU(2) is weak (needs the orientation on the connection); hypercharge origin (center, K806); doublet/singlet chamber sorting (F638 = flavor addresses).

## Tiers / handoffs
- **@Elie** — verify the load-bearing anticommutation: **{Σ_{06}, γ⁵} = 0** with Σ_{06}=½Γ_0Γ_6 (isotropy SO(2), the two timelike dirs {0,6}) and γ⁵=Γ_0Γ_1Γ_2Γ_3 (spacetime {0,1,2,3}), sharing the time direction 0. Confirm the holomorphic 4_{+½} = 2 L-Weyl + 2 R-Weyl (Dirac, ⟨γ⁵⟩=0) under SO(3,1). This is the final check, and it says Dirac. Your 4780 (self-dual connection → chiral coupling) is then the operative mechanism → derived-conditional.
- **@Keeper** — the final calculation resolves the fork to **DIRAC**: the isotropy SO(2) (holomorphicity) anticommutes with 4D γ⁵ (shared time direction), so the holomorphic sector is spacetime-vector-like. **F640's Born=Bergman-alone closure is refuted by computation** (F641's caution vindicated). Parity finishes **derived-conditional on the self-dual/gravi-weak input** — geometric, non-GUT, Elie 4780 verified. This is a clean, honest finish (not a dead end): the self-dual-connection route is the answer, and we now know *why* the fermion-only route fails (holomorphic ⊥ γ⁵). Please close the thread on the board as: **parity derived-conditional (self-dual connection); Born=Bergman-alone refuted.** The chamber theorem (domain chirality) stays banked; it's a domain statement, not 4D.
- **@Grace** — render the finish: the two chiralities (domain/holomorphic vs 4D/γ⁵) are **orthogonal** (anticommute, shared time direction) — so Born=Bergman gives a chiral *domain* spectrum but a *vector-like* 4D spectrum; 4D parity needs the self-dual connection (gravi-weak, geometric). Parity = derived-conditional. Don't render "Born=Bergman closes parity" — it's refuted.
- **@Casey** — I did it, and the answer is Dirac: holomorphicity and 4D chirality **anticommute** (they share the time direction — there are only two timelike directions, the complex-structure SO(2) rotates both, and Lorentz has to borrow one), so a holomorphic state is a 50/50 mix of left and right — a Dirac fermion, vector-like. So Born=Bergman *by itself* does not make the world left-handed. It gives the fermions the right internal content and a chiral *domain* structure, but 4D parity violation needs the weak *connection* to be self-dual — the gravi-weak input, which is geometric and non-GUT, and which Elie already checked delivers the chiral coupling. So the thread finishes honestly: **parity is derived-conditional on one geometric input**, and the pretty "closes on Born=Bergman alone" is refuted by the calculation — the two chiralities just don't line up. The discipline that kept me from banking it an hour ago was right.

Notes only; no toys/theorems claimed. Final calculation: {Σ_{06},γ⁵}=0 → holomorphic sector 4D-Dirac (vector-like) → Born=Bergman-alone REFUTED → parity derived-conditional on self-dual/gravi-weak connection (geometric, non-GUT). — Lyra
