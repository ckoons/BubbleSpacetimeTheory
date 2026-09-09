# PRE-REGISTRATION — Toys 5744 (E1, E2) and 5745 (E3, E4), Round 137. Hashed before any runs.

**Elie, 2026-09-09 (Wednesday) 10:27 EDT (shell-copied).** ν subscripted throughout. For D_IV⁵: rank r = 2, a = n − 2 = 3, **ν_floor = (r−1)a/2 = 3/2 (Wallach floor), ν_Hardy = n/2 = 5/2, ν_Bergman = genus = 5.** Wallach set = {0, 3/2} ∪ (3/2, ∞).

## E1 — Toy 5744: pin the zero
- **A1 (can fail):** c_ν(j,k) = 1 − L_ν − M_ν with L_ν = [(k+3)/(2k+3)]·(j+k+5/2)/(j+k+ν), M_ν = [k/(2k+3)]·(j+1)/(j+ν−3/2). **At ν = ν_Hardy = 5/2 this is IDENTICALLY ZERO for every (j,k), not only at k = 0** — L + M = (k+3)/(2k+3) + k/(2k+3) = 1 exactly. The zero is at the Hardy point; at ν_floor = 3/2 the matter term M_ν has a pole at j = 0 and the quantity is undefined, so the floor is singular, not a zero.
- **A2:** the constant across the admissible range: c_ν(j,0) = (ν − 5/2)/(j + ν), **positive above ν_Hardy, zero at it, and NEGATIVE for 3/2 < ν < 5/2.** A negative "cost" means ⟨|z|²⟩_ν > 1, which no probability measure on the ball can give — so below ν_Hardy the quantity is a formal norm ratio, not an expectation.
- **A3 (the measure caveat, stated as a limit on every Born reading):** the weight-ν norm is an integral against a positive measure on D only for **ν > n − 1 = 4**; at ν_Hardy it is an integral over Š; strictly between 5/2 and 4 it is neither. So "1 − c is a probability" is available at ν_Bergman = 5 and nowhere else in the corpus's range.

## E2 — Toy 5744: the sign fork (the round's can-fail)
Reading (a): the cost c_ν(j,k). Reading (b): the Hardy-over-weight-ν norm ratio R_ν(j,k) = (ν)_{j+k}(ν−3/2)_j / [(5/2)_{j+k}(1)_j], whose 1 − 1/R form runs 0 → 0.987 at ν = 5 (my 5721 P5 numbers).
- **B1 (hashed, exact):** R_ν(j+1,k)/R_ν(j,k) = (ν+j+k)(ν−3/2+j) / [(5/2+j+k)(1+j)]. **R_ν rises in j iff ν > 5/2, falls iff ν < 5/2, and is identically 1 at ν = 5/2.**
- **B2 (the verdict, can fail): there is NO admissible weight at which both readings are positive costs falling with j.** For every ν > ν_Hardy the two are exactly opposed (c_ν falls, 1 − 1/R_ν rises); at ν_Hardy both are trivial (0 and 1); below ν_Hardy reading (a) is negative and so not a cost at all. The fork is not resolvable by choosing ν.

## E3 — Toy 5745: ħ, if it is there
- **C1 (hashed):** ν is a dimensionless representation parameter; the Berezin ħ_B = 1/ν is likewise dimensionless. **ν_Bergman = 5 gives ħ_B = 0.2 and ν_Hardy = 5/2 gives ħ_B = 0.4 — both order one, i.e. maximally quantum, and neither is a physical action.** Equating ħ_B to the physical ħ = 1.054572e−34 J·s requires an action unit for D_IV⁵; **the corpus's own floor (T2623, K1879: no record→spacetime map, no momentum, no ΔE/E) says there is none.** Report: **the units do not connect**, with the SI gap printed (order 10³⁴).
- **C2:** if the reading were inherited literally, two rows at ν = 5 and ν = 5/2 assert two Berezin constants in ratio 2. A factor 2 in a physical ħ is refuted by any spectroscopy at many orders; so the literal inheritance is dead on arrival and the honest reading is two SPACES, not two values of one constant.

## E4 — Toy 5745: the classical limit as a control (cannot fail; reported as such)
- **D1:** as ν → ∞, L_ν, M_ν → 0 so **c_ν → 1 and ⟨|z|²⟩_ν → 0**: the states concentrate at the origin, which is the classical limit of the coherent-state family. Consistent with ν = 1/ħ_B → ∞.
- **D2 (the control's content):** the write branching (k+3)/(2k+3), k/(2k+3) is the Stein–Weiss share of S⁴ and is **ν-independent**, so the 3/7 word, the saturation degree and the chain's whole law are unchanged at every weight. **The chain is ν-blind exactly as it is j-blind (Round 134 L1). Only the norms move.**

Score: E1 X/3 (A1 can fail), E2 X/2 (both can fail), E3 X/2, E4 X/2.
