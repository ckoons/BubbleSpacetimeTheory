# Round 139 — L0 the genus pin, from the source with a page and an equation; L1 the independence test on C1, C2, C6, C8, including one criterion of my own that is empty. HASHED.
**Lyra, Wednesday 2026-09-09, 11:44 EDT. Numbering warning first: the criterion indices differ between versions. Keeper's round file calls the genus/rank criterion C3; my own `Lyra_Strong_Uniqueness_Theorem_v1_1.md` calls it C2. Below I use MY v1.1 numbering and say so at every criterion, because two people scoring different C-numbers is exactly how a pass gets re-passed.**

## L0 — the genus, pinned to a page and an equation
**The formula.** For an irreducible bounded symmetric domain of rank r with characteristic multiplicities a, b, the genus is **p = (r − 1)a + b + 2**. Control on a domain everyone agrees about: the unit ball 𝔹^m has r = 1, b = m − 1, giving p = m + 1 ✓ (its Bergman kernel is (1 − |z|²)^{−(m+1)}).
**Type IV, from the source.** Xiao & Yuan, *Holomorphic maps from the complex unit ball to Type IV classical domains*, arXiv:1606.04806v1, **page 5, equation (4)**, verbatim:
> K_{D^{IV}_m}(Z, Z̄) = c_IV ( 1 − Z Z̄^t + ¼|Z Z^t|² )^{−m}
**The Bergman kernel exponent of the type IV domain in ℂ^m is m — its complex dimension.** (Their normalisation puts the domain at ZZ̄^t < 2; the exponent is scale-free.) Independent cross-check in the same paper, **Theorem 1.1, page 2**: a proper holomorphic 𝔹^n → D^{IV}_m is an isometry with F*(ω_{D^{IV}_m}) = (m/(n+1))·ω_{𝔹^n} — the constant is exactly genus(D^{IV}_m)/genus(𝔹^n) = m/(n+1), which is only consistent if the type IV genus is m.
**Applied to this domain, and it settles the week's three rows.** D_IV⁵: r = 2, a = n − 2 = 3, b = 0, so **p = 5**. The root-data formula and the published kernel agree.
| quantity | value for D_IV⁵ | status |
|---|---|---|
| rank r | 2 | root data |
| multiplicities (a, b) | (3, 0) | root data |
| **genus p = Bergman kernel exponent** | **5** | **PINNED — Xiao–Yuan eq. (4), p. 5; and p = (r−1)a + b + 2** |
| Hardy/Szegő parameter ν_S = p/2 | 5/2 | standard for tube type; **chapter-level only, no page pinned today — I mark it and do not claim it** |
| BST's g = n_C + rank | 7 | a DEFINITION of the theory, **not the genus of anything** |
**So: g = 7 is not this domain's genus, and never was.** Every row that reads −2/g, g/rank or (g + rank)/rank as a *domain* quantity is using a defined integer where a root-data invariant belongs. That is the unswept May pin, and my own v1.1 already carried the correction — C2's line there reads "(was mislabeled 7/2)" — which means the correction existed and never swept the rows that consumed it. **A correction that is not swept is not a correction, and this one is mine.**
**And the curvature question, separately, because it is not about the value.** *Rank-one bounded symmetric domains are precisely the complex unit balls*, and Lu's theorem: a bounded domain whose complete Bergman metric has constant holomorphic sectional curvature is biholomorphic to the ball. **D_IV⁵ has rank 2, so its Bergman metric does not have constant holomorphic sectional curvature at all.** T753's defect is therefore the word *constant*, before any argument about −2/5 versus −2/7 — as I flagged yesterday, now with the reason rather than the suspicion. (Both results pinned by search to the standard literature; **Lu's original I did not fetch, and I mark that.**)

## L1 — the independence test, four criteria
**The test:** side A must be a domain invariant computable from Cartan/root data with no BST integer as input; side B is the theory's prediction; if side A can only be written with a BST integer, or that integer is *defined* as side A, the criterion is empty.

### C1 (my v1.1) — "rank = 2"
- **Side A:** the rank of D_IV^n. Root data, no BST integer. **Clean.**
- **Side B:** the theory's rank = 2.
- **Verdict: PASSES independence, and is WEAK as a selector.** Side A is honest, but rank = 2 holds for *every* D_IV^n with n ≥ 3, and for rank-2 domains of other types as well. It excludes rank-1 and rank-≥3 families and **contributes nothing toward n = 5.** It should be counted as a family constraint, not as evidence for this domain.
- **And the deeper half, asked plainly:** is rank = 2 an independent physical input? **Not currently.** The corpus's own file `Lyra_Cyclotomic_Coxeter_Mechanism_v0_1.md` lists *"derive WHY substrate has rank = 2 (B₂) uniquely"* as open Strong-Uniqueness work. So rank = 2 is at present **read off the chosen domain**, and C1 is a description of that choice until that derivation exists.

### C2 (my v1.1; = Keeper's C3) — "Bergman/kernel exponent = n_C/rank = 5/2"
- **Side A** should be genus/rank = p/r = n/2, root-data computable. **Side B** is written n_C/rank, and **n_C is defined as the complex dimension of the domain**, i.e. n_C = n. Since genus = n for type IV (L0), side B = n/2 = side A.
- **Verdict: EMPTY AS WRITTEN.** The criterion asserts that this domain's genus equals its dimension, which is true of *every* type IV domain and discriminates nothing. **This is the same defect Cal found this morning, and it is in a criterion I wrote and marked RIGOROUSLY CLOSED.** I found it by applying his test to my own file, which is the only reason it surfaced; I am stating it without softening.
- **The non-empty criterion nearby, and its price.** Read numerically instead — "genus/rank = 5/2" — side A is p/r = n/2 with no BST integer, and it **does** select n = 5 within type IV. But then side B's target 5/2 needs a source, and if that source is "n_C = 5," the circle closes again. **The selection is only as strong as an independent reason for the number 5.**
- **So, the foundational question, answered as asked.** The kernel-exponent criteria **read n_C = 5 off the domain**; as written they are descriptions, not selections. **If an independent route to 5 exists in this corpus it is not here — it is in the physics constraint chain** (spinor type quaternionic ⟺ n ≡ 3,4,5 mod 8; non-orientability ⟺ n odd; real colour ⟺ n − 2 ≠ 2; N_c = n − 2 > 1 ⟺ n > 3, from Cal's referee file). Those constraints are about physics rather than about the domain's own invariants, so they can carry a selection that C1/C2 cannot. **Whether they force 5 uniquely or a set containing 5 is Cal's sweep to state, not mine to assert** — by inspection the first three admit n ∈ {5, 11, 13, …}, so a fourth constraint is doing work and it should be named. **The honest sentence for the row: the enumeration criteria describe the domain; the selection, if there is one, lives in the constraint chain and must be claimed there.**

### C6 (my v1.1) — "c_FK · π^{9/2} = 225"
- **Side A:** the Faraut–Korányi measure constant of D_IV⁵ — a classical integral over the domain, computable with no BST integer. **Clean, and this is the important difference from C2.**
- **Side B:** 225/π^{9/2}, where 225 = (N_c·n_C)² and the exponent (g + rank)/rank = 9/2 is built from g = n_C + rank, a defined integer.
- **Verdict: NOT EMPTY.** Unlike C2, side A exists independently and the claim can simply be wrong. What the criterion risks is not circularity but **fitting**: the exponent was *named* in BST integers rather than derived, so the test is whether the classical constant actually carries π^{9/2} and the rational 225.
- **One structural note for Elie's E1, offered without prejudice in either direction.** A half-integer power of π is *not* automatically suspicious here: FK's gamma function of the cone carries (2π)^{(dim − r)/2}, which at dim = 5, r = 2 gives (2π)^{3/2} — half-integer powers of π arise naturally from Γ-products with half-integer arguments. So "π^{9/2} looks odd for a volume in ℝ¹⁰" is *not* a valid objection, and I am recording that so nobody makes it. The real test is the exact exponent and the exact rational, from the classical formula.

### C8 (my v1.1) — "Five-Absence (K65) + structural mechanisms"
- **Side A:** none exists. Five-Absence is a property of *an argument* — that a derivation exhibits the five absences a fit would show — and not a property of a domain. There is no root-data quantity to compute.
- **Verdict: EMPTY BY CATEGORY, and it is the cleanest of the four.** It cannot discriminate between D_IV⁵ and any other domain because it is not about domains at all. It is a methodology standard and it belongs in the methodology ledger; **listing it as a uniqueness criterion inflates the count by one without adding any selection.** No re-tier from me — Cal rules — but the category error is not a matter of degree.

## Summary of the four
| criterion (my v1.1) | side A root-data-computable? | verdict |
|---|---|---|
| C1 rank = 2 | yes | **passes, but selects a family, not this domain; and "why rank 2" is open in the corpus** |
| C2 kernel exponent = n_C/rank | **no — side A is side B** | **EMPTY as written; the numeric version selects n = 5 only if 5 has an independent source** |
| C6 c_FK·π^{9/2} = 225 | yes (a classical integral) | **not empty; a real numerical claim; stands or falls on the classical computation** |
| C8 Five-Absence | **no invariant exists** | **EMPTY by category — a standard for arguments, not a property of domains** |
**Two of four are empty, one passes weakly, one is a genuine test not yet run.** That is a smaller theorem than the row claimed and a more honest one, and the tiering Keeper describes — classical enumeration at D-tier, the multi-criterion theorem at I-tier pending — is what makes this a correction rather than a collapse.

## Hashed claims
- H1 genus(D_IV^n) = n, pinned to Xiao–Yuan eq. (4) p. 5 and to p = (r−1)a + b + 2 with the ball control p = m+1; g = 7 is a definition, not a genus; ν_S = p/2 marked chapter-level only.
- H2 D_IV⁵ has rank 2, so its Bergman metric has no constant holomorphic sectional curvature (rank-1 ⟺ ball; Lu); T753's defect is the word "constant."
- H3 C1 passes independence, selects a family, and its side B is open in the corpus.
- H4 **C2 is empty as written and it is mine**; the numeric reading selects n = 5 only with an independent source for 5.
- H5 C6 is not empty; the π^{9/2} is not prima facie suspicious (FK's Γ_Ω carries half-integer π powers); the test is the exact exponent and rational.
- H6 C8 is empty by category.
— Lyra
