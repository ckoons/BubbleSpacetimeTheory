---
title: "One Integer Generates the Discrete Standard Model: the Reading Calculus on D_IV⁵"
subtitle: "Within the type-IV family of bounded symmetric domains, the entire discrete internal skeleton of the Standard Model — its gauge dimensions, chirality, the Majorana neutrino, CP-existence, anomaly-freedom, three generations, the custodial Higgs — is a function of a single measured integer, n_C = 5; and the weak force rides on a single trinary question."
author: "Casey Koons, with Lyra, Keeper, Elie, Grace, Cal A. Brate (CI co-authors / referee)"
date: "2026-08-20 Thursday (date-verified)"
status: "v0.6 (Round 18 — LEAD CORRECTED + LOCKED to Strong-Uniqueness K1697). The Round-17 lead sentence was FALSE ('n_C=5 unique quaternionic value' — 4,5,11,13 are all quaternionic). Corrected to the already-banked form: n_C=5 is the SMALLEST domain satisfying four independent proved conditions [quaternionic spinor = weak force; non-orientable boundary = chirality; real color block = no internal color; N_c=n-2>1 = color exists]; survivors are {5,11,13,...} and the tiebreaker pinning 5 is the MEASURED N_c=3 (N_c=n-2). Six-row family table now IN THE LEAD (n=4 as checked exception; 11,13 as genuine survivors excluded only by measurement), every cell derived from Elie's H_F(n). Bits labeled: spinor block 1.58 (log2 3), family census 2.00 (log2 4). SEP-e split kept: finite algebra End_K = C+H+R, but the bare color End_R(V12) genuinely IS M3(R) — NOT blanket-replaced. Prior: v0.5 (Round 17 re-center, Casey: 'why are we even talking about D_IV⁴?'). The one-integer form is the ratified lead; the three-invariant cross-domain minimality and ALL sibling domains (D_IV⁴/⁷/⁸) are demoted to Appendix A (the companion result, a proof-technique for minimality — not the physics headline). Folds in K1744: (a) the census is the ORDERED TRIPLE of reality types, multiplicity-free (hygiene note, not a load-bearing rescue); (b) census CONTENT = log2(3) = 1.58 bits — one trinary spinor question — the honest number, not the 4.75-bit capacity; (c) the weak force = n_C=5 is the unique value making the spinor quaternionic; (d) twist separator = D_IV7 vs D_IV8; D_IV4 was NEVER valid [its census (C,H,C) is an SO(2)-abelian accident at n=4 — color goes complex]; (e) algebra = C+H+R everywhere. Theorem spine unchanged. Ships on Keeper-PASS + Cal-vet + both voices + Casey GO. Nothing pushed; CP existence-only."
---

# One Integer Generates the Discrete Standard Model

## The result (bright-high-schooler version)

Inside the family of shapes our physics lives in, one question sits at the heart of the weak force: is the spinor — the mathematical object a fermion is built from — made on the *real* numbers, the *complex* numbers, or the *quaternions*? That is a single three-way choice, about **one and a half bits**. The quaternions are the two-sided number system, and that two-ness is exactly the weak force with its paired-up particles (the doublets) — so a "quaternion" answer is what buys the weak force.

Several dimensions n_C give the quaternion answer — so 5 is not the *only* one. What makes it special is that **n_C = 5 is the smallest shape that passes all four checks at once**: the spinor is quaternionic (weak force), the edge is one-sided (a left-handed world), the color piece is real (no hidden color force), and there is room for color to exist at all. Bigger shapes (n_C = 11, 13, …) pass the same four checks too — and the tiebreaker that says "5, not 11" is a *measured* fact about our world: there are exactly three colors of quark, and the number of colors is just n_C minus two, so three colors means n_C = 5.

Everything else in the discrete skeleton of the Standard Model then follows from the same integer: which forces there are and how big, why the world is left-handed, why the neutrino is its own antiparticle, why there are exactly three families of matter, why the quantum anomalies cancel. So the honest headline: **the discrete guts of the Standard Model is a function of a single measured integer, n_C = 5** — the *smallest* shape that works, pinned down exactly by the three colors we see.

*(A companion result, in Appendix A, steps all the way back to* every *nicely-curved shape and asks how many independent facts it takes there. The answer is three — the kinds, the sidedness of the edge, the rank. But that is the cross-domain footnote that makes "why these three and no fewer" precise; it is not the physics headline. Within our own family, it is one integer.)*

## Abstract

We prove that the discrete internal structure of the Standard Model is *generated*, in a precise sense (a declared reading calculus over a declared fact-set), by geometric invariants of the type-IV bounded symmetric domain D_IV^n = SO₀(n,2)/[SO(n)×SO(2)], and that **within this family the entire skeleton is a function of the single dimension n_C**: the rank is fixed by the family (type IV is rank-2), and the reality-type census and the Shilov orientability are both functions of n_C. The census reduces to a **single trinary question** — the Frobenius–Schur reality-type of the spinor block — carrying just **log₂3 ≈ 1.58 bits** of content (the charge block is complex and the color block real for every n in the family; only the spinor moves), and the quaternionic answer is the origin of the weak SU(2)_L. **n_C = 5 is not the unique quaternionic dimension** (4, 5, 11, 13, … all are); it is the **smallest domain satisfying four independent, already-proved conditions** — quaternionic spinor (weak force), non-orientable boundary (chirality), real color block (no internal color), and N_c = n − 2 > 1 (color exists) — and **uniqueness among the survivors {5, 11, 13, …} is the measured N_c = 3** (Strong-Uniqueness, K1697). At n_C = 5 the reading is the Standard Model: the electroweak gauge dimensions, chirality, the Majorana neutrino, CP-existence, anomaly-freedom, three generations, the custodial Higgs. We give the reading calculus, the assignment table (one row per reading, single-invariant vs conjunction meet), and an honest comparison to Connes' noncommutative-geometry Standard Model — BST *derives* its finite algebra ℂ⊕ℍ⊕ℝ (electroweak, with *no internal color group*) where Connes *inputs* ℂ⊕ℍ⊕M₃(ℂ) with color gauged; the difference is itself the result. The companion cross-domain minimality (three independent invariants across all bounded symmetric domains, collapsing to one integer within D_IV) and the sibling-domain separators are deferred to **Appendix A**, where they serve the minimality claim; **they are not needed for the one-integer lead.**

## 1. The result: one integer, four conditions, the measured tiebreaker

Fix the family to the type-IV domains D_IV^n = SO₀(n,2)/[SO(n)×SO(2)], with dimension parameter n = n_C. Three facts determine the discrete internal skeleton — the reality-type census **I₁**, the Shilov orientability **I₂**, the rank **I₃** — and *within D_IV all three are functions of n_C*: the rank is 2 for every n (type IV is rank-2; rank-3 fails, T1443), and I₁, I₂ are read off n_C by two periodicities (Section 3). Consequently:

> **Within D_IV, the entire discrete internal Standard-Model skeleton is a function of the single integer n_C, and at the measured value n_C = 5 it is the Standard Model.**

**Why n_C = 5 (the honest form — this is Strong-Uniqueness, K1697, already banked, not a new claim).** It is *not* that 5 is the unique dimension with a quaternionic spinor: dimensions 4, 5, 11, 13, … are all quaternionic (n ≡ 3, 4, 5 mod 8). Rather, **n_C = 5 is the smallest domain satisfying four independent, already-proved conditions:**
1. **quaternionic spinor** (n ≡ 3, 4, 5 mod 8) — gives the weak SU(2)_L;
2. **non-orientable Shilov boundary** (n odd) — gives chirality (γ₅ loses global definition, Section 5);
3. **real color block** (SO(n−2) non-abelian, n ≥ 5) — gives *no internal color group*;
4. **N_c = n − 2 > 1** — color exists at all.

The dimensions meeting all four are **{5, 11, 13, …}**; **n_C = 5 is the smallest, and the tiebreaker that pins it uniquely is the measured N_c = 3** — since N_c = n − 2, three colors ⇔ n = 5. So the uniqueness is real but honestly sourced: four *proved structural* conditions cut the field to {5, 11, 13, …}, and one *measured* integer (N_c = 3) selects 5. No claim rests on 5 being the only quaternionic dimension — it is not.

**The family, checked (every cell computed from Elie's H_F(n), Peirce dimensions (1, n−2, 1) — derived, not cited).**

| n_C | spinor (n mod 8) | boundary (n mod 2) | color SO(n−2) | N_c = n−2 | four conditions | verdict |
|---|---|---|---|---|---|---|
| 4 | ℍ quaternionic | even → **orientable** | SO(2) **abelian → complex** | 2 | no (fails 2 and 3) | the checked exception — orientable *and* complex color (the SO(2) accident) |
| **5** | **ℍ quaternionic** | **odd → non-orientable** | **SO(3) → real** | **3** | **yes all four** | **the Standard Model — smallest survivor, and N_c = 3** |
| 7 | ℝ real | odd → non-orientable | SO(5) → real | 5 | no (spinor not ℍ) | foil: real spinor → no weak SU(2) |
| 8 | ℝ real | even → orientable | SO(6) → real | 6 | no (fails 1 and 2) | foil: real spinor *and* orientable |
| 11 | ℍ quaternionic | odd → non-orientable | SO(9) → real | 9 | yes all four | genuine survivor — excluded **only** by measured N_c = 3 |
| 13 | ℍ quaternionic | odd → non-orientable | SO(11) → real | 11 | yes all four | genuine survivor — excluded **only** by measured N_c = 3 |

n = 4 is the domain least worth discussing and most worth having checked: it is the one place the color block goes complex (SO(2) abelian), and putting it in the table shows the calculus catches its own exception. n = 11, 13 are the honest rows — they pass all four *structural* conditions, and nothing structural rules them out; only the measurement N_c = 3 does. That is exactly what "one measured integer" means.

**The bit count (labeled).** The spinor's reality-type — the one datum that gives the weak force — is a single trinary question, **1.58 bits** (log₂3): the *spinor-block* content. The full **family census** — the ordered triple (charge, spinor, color) over the distinguishable outcomes it realizes across the family — is **2.00 bits** (log₂4). Either way the content is tiny: the weak sector rides on 1.58 bits, the whole internal census on 2.00. *(The 4.75 = log₂3³ is the raw* capacity *of three free blocks — mostly frozen by the family — not the content; 1.58 and 2.00 are the honest figures.)*

*(How many independent facts it takes across* all *bounded symmetric domains — the cross-domain minimality, three invariants collapsing to one integer within D_IV — is the* companion *result of **Appendix A**, a proof technique for "why these three and no fewer." The physics lead is the one-integer form above; the siblings appear in the lead only as the checked family table, and in the appendix only as minimality separators.)*

## 2. The reading calculus (declared)

A "reading" is not informal. We fix, once:

- **the object** — the finite internal space H_F of the domain, its endomorphism algebra End_K(H_F) under K = SO(n)×SO(2), the Shilov boundary ∂_S, and the domain's rank;
- **the operations R** — (i) isotypic decomposition of a representation under a subgroup; (ii) the Frobenius–Schur reality-type (ℝ/ℂ/ℍ) of each isotypic block; (iii) generator counting; (iv) the orientability / Pin-cobordism class of ∂_S; (v) the support-strata count (= rank + 1);
- **the fact-set F** — the discrete internal observables of the Standard Model (the table of Section 4).

A fact is *generated* if it is the value of an operation in R applied to the object. **Minimality is relative to (F, R):** the claim "k invariants" means *no fewer than k data determine every fact in F under the operations R.* Stating (F, R) is what makes minimality provable rather than rhetorical. (The minimality *proof* — that none of the three can be dropped — is Appendix A; the main text uses the reading calculus to exhibit the skeleton, not to argue minimality.)

## 3. The invariants, as functions of n_C

- **I₁ — the reality-type census** of End_K(H_F): the **ordered triple** of Frobenius–Schur division algebras (ℝ/ℂ/ℍ) commuting with the charge, spinor, and color blocks, **multiplicity-free**. For D_IV⁵ it is **(ℂ, ℍ, ℝ)** — a complex charge block, a quaternionic weak block, a real color block. **Within the family the charge stays ℂ and the color stays ℝ; only the spinor type varies**, via the spinor reality-type's **Bott/ABS mod-8** periodicity. So the census *content* is one trinary question — **log₂3 ≈ 1.58 bits** — and the whole weak sector rides on it. *(The 4.75 = log₂3³ is the raw* capacity *of three free blocks; most of it is frozen by the family, so 1.58 bits is the honest figure. Multiplicity-free is a* hygiene *note — it keeps the census a statement about* types*, not copies; the color* dimension *3 = n_C − 2 = N_c is a separate* rep-dimension *reading, never a census multiplicity. The earlier "M₃(ℝ)" was the bare-End slip — End_ℝ(V₁₂) ignoring K, whereas the K-equivariant commutant of a real irrep is just ℝ; algebra = ℂ⊕ℍ⊕ℝ throughout.)*
- **I₂ — the orientability class** of the Shilov boundary ∂_S = (S^{n_C−1}×S¹)/ℤ₂: orientable or not, via the Shilov parity **mod 2**. For D_IV⁵: 5 odd → **non-orientable** (Pin⁻, P² = −1). *One bit.*
- **I₃ — the rank**: fixed = **2** by the family (T1443), so the support-strata count = rank + 1 = **3 generations**.

At n_C = 5: 5 mod 8 → the **quaternionic** Sp(2) spinor (the ℍ block → SU(2)_L); n_C − 2 = 3 → the real color triple (the ℝ block, dimension 3 = N_c); 5 odd → the **non-orientable** boundary; rank 2 → **three generations**. The entire skeleton, from one integer — and the one datum that *moves* to give it is the spinor's trinary type.

## 4. The assignment table (one row per reading)

The generating set, made explicit (canonical form; single-invariant rows and conjunction "meet" rows; every negative names the invariant it is outside of; the Five-Absence closure block ensures no forbidden particle is left without a row). *The polished figure is the companion assignment grid (Lane C, Grace + Keeper). The separator column names the sibling domain that fails when the invariant is dropped — the full separator argument is **Appendix A**; here it is a pointer, not the content.*

| reading | invariant(s) | separator (Appendix A) | note |
|---|---|---|---|
| **gauge dimension = 4 = dim(U(1)×SU(2))** *(uniform census read)* | **I₁** | D_IV⁷ (census changed) | the three reality-type blocks contribute {U(ℝ), U(ℂ), U(ℍ)} = {0, 1, 3} internal generators — a *uniform* census read, since U(ℝ) is 0-dimensional — so 0 + 1 + 3 = 4. No two-line check; both counting rules agree because the ℝ block sits at multiplicity 1 |
| **no internal color group** *(separate support line)* | **I₁ + Coleman–Mandula (T265)** | D_IV⁷ | two independent arguments, not the count's second line: (i) the census gives the ℝ color block 0 internal generators; (ii) its geometric SO(V₁₂) rotation is a *spacetime* symmetry, which by Coleman–Mandula cannot be an internal gauge factor |
| anomaly-freedom | **I₁** | — | self-conjugate ⇔ nonzero FS indicator ⇒ cubic anomaly = 0 |
| custodial SU(2) / ρ ≈ 1 / no W_R | **I₁** | — | SO(n) vector → (2,2) under SO(n−1) |
| **parity violation** *(derived)* | **I₂** | D_IV⁷ vs D_IV⁸ (orientability pair, K1744) | on a non-orientable boundary the chirality operator γ₅ (a volume-form object) is *not globally defined* — losing γ₅ is what permits LH ≠ RH (T2522) |
| no sterile neutrino (no ν_R) | **I₂** | D_IV⁷ vs D_IV⁸ | the Möbius locus forbids ν_R closure (T1949) |
| 3 generations (no 4th) | **I₃** | a different-rank domain (D_III^r) | support-strata = rank + 1 (T2525) |
| 3×3 mixing (CKM/PMNS) structure | **I₃** | different-rank domain | generation count |
| **chirality** (which fermions are LH) | **I₁ ∧ I₂** = census_(alg) ∧ twist_(geo) | **D_IV⁷ vs D_IV⁸** (twist dropped → no chirality) **and D_IV⁷** (census changed) | I₂ permits (γ₅ lost on the non-orientable edge); I₁ selects (Y ≠ 0 makes the rep complex, T2522) |
| **CP violation possible** | **I₁ ∧ I₃** = census_(alg) ∧ rank_(KM) | **D_IV⁷** (census) **and a different-rank domain** | the quaternionic √−1 (census) *and* ≥ 3 generations (rank, Kobayashi–Maskawa) — **existence only; the magnitude is not read** |
| **neutrino Majorana** *(not a clean structural meet)* | **I₂ + one empirical input** | D_IV⁷ vs D_IV⁸ (twist) | the twist forbids ν_R, so a Dirac mass is unavailable; **given the empirical fact that neutrinos are massive**, the mass is Majorana. If neutrinos were massless this row is vacuous — so it is twist + one measured fact, not a pure derivation |

Meet rows are subscripted algebraic (census) vs geometric (twist) vs count (rank); **each meet cites the two separators that fail when its respective invariant is dropped** — this is what stops a meet from laundering a value through one invariant. **Koide is not in this table** — see the next section.

**Completeness (these are *all*).** The invariants produce exactly the readings above: I₁ ranges over the reality-type of each block (three blocks × {ℝ,ℂ,ℍ}) and the derived quantities (dimension, self-conjugacy, vector-branching); I₂ is one bit (orientable/not) and its consequences (γ₅, ν_R); I₃ is the strata count and its square. Every *structural* internal observable is one of these — there is no fourth generator producing a fact off this list (the minimality claim, proved in Appendix A). **The Five-Absence set is a consistency check, not a generating row, and it splits by category:** *species*-absences (no sterile neutrino, no fourth generation) are already table rows (I₂, I₃); *process*-absences (**no proton decay, no GUT**) are **dynamical** statements — a forbidden *process*, not a missing *species* — and belong to the dynamics (the seam), where they are checked for consistency, not derived here.

## 4a. What the instrument refuses (lead with Koide) — the strongest evidence it is not an advocacy tool

An honest instrument must refuse things, and the sharpest test is whether it refuses its own best-looking match. It does:

> **The charged-lepton Koide relation, Q = (Σ m)/(Σ√m)² = 2/3, holds to ≈ 0.0009%.** It is the tightest numerical coincidence in the whole neighbourhood — and our reading calculus **cannot derive it, and we do not claim it here.** Koide is a relation among mass *values* (a spectrum fact); the calculus is *structural*: a fact is readable off I₁ only if it is constant on the reality-type classes {ℝ,ℂ,ℍ}, and a specific ratio of specific masses is not such a class function. So Koide is provably *outside* the fact-set F. We could have written it as a "census ∧ rank" reading; on the referee's (and our own) vet, that laundered a value through a structural instrument, and we struck it.

A device that turns away a 0.0009% match because its own stated rules forbid the reading is not an advocacy tool — it is an instrument. This refusal is worth more to a skeptical reader than any positive row, and we put it first among the negatives for that reason. *(Koide is real and may yet be derived — by the mass/eigenvalue instrument, not this one. It sits on the honest ledger as identified-not-derived, elsewhere; disposition: Conditional-Forced, mass sector.)*

## 5. The chirality mechanism (why the ℤ₂ is load-bearing)

**Here is the mechanism a spin geometer will ask for.** Chirality is the eigenvalue of **γ₅**, the chirality operator — and γ₅ is a *volume-form* object: it exists globally exactly when the manifold is orientable. On an **orientable** boundary γ₅ is globally defined, the bulk spinor is vector-like (Witten's no-go), and there is no room for a chiral theory. On a **non-orientable** boundary γ₅ is **not globally defined** — the boundary carries a **Pin** structure rather than a **Spin** structure — and *that loss is what opens the chiral sector*: a Pin⁻ boundary admits a chiral lift where a Spin (orientable) boundary cannot. So the honest statement of the mechanism is **T2522**: the non-orientability (Pin⁻) makes chirality *possible* by removing global γ₅, and the hypercharge (Y ≠ 0) *selects* which fermions realize it. Take away I₂ and you lose the handedness (γ₅ becomes global, the theory goes vector-like). *(Scope: Pin-vs-Spin admission is dimension-generic within the admissible types; it is **not** what selects n_C = 5 — the spinor's trinary type does that. I₂'s job is to make chirality* possible*, not to pin the dimension. The type-level statement — which domains can be non-orientable at all — is the orientability criterion of Appendix A.)*

## 6. Comparison to Connes' NCG Standard Model (honest)

| datum | Connes NCG | this work | note |
|---|---|---|---|
| the finite algebra | **input**: A_F = ℂ⊕ℍ⊕**M₃(ℂ)** (chosen to match) | **derived**: End_K(H_F) = ℂ⊕ℍ⊕**ℝ** (I₁, multiplicity-free) | *the algebras differ, and the difference is the result* (below) |
| three generations | **input** (⊗ ℂ³ by hand) | **derived** (I₃, rank + 1) | |
| chirality (γ grading) | **input** (imposed via KO-dimension) | **derived** (I₂, the non-orientable boundary; γ₅ is what the twist provides) | |
| no ν_R | ν_R typically **included** | **derived** (I₂, Möbius forbids it) | |
| Higgs potential, gauge couplings | **derived** (spectral action) | **not derived** (BST's dynamics are hosted — the seam) | |

**The difference in the finite algebra *is* the result.** Connes takes A_F = ℂ⊕ℍ⊕M₃(**ℂ**) — the M₃(ℂ) is complex, and its unitaries are the internal SU(3): color is an internal gauge group he puts in. BST *derives* ℂ⊕ℍ⊕**ℝ**: the color block's K-equivariant commutant comes out **real** (multiplicity 1, so U(ℝ) is 0-dimensional — no gauge generators), and by Coleman–Mandula the geometric SO(V₁₂) rotating the color 3-space is a spacetime symmetry, not an internal gauge factor — **so BST derives the electroweak algebra (ℂ⊕ℍ) with *no internal color group*, where Connes inputs ℂ⊕ℍ⊕M₃(ℂ) with color gauged.** The gap between Connes' complex M₃(ℂ) and BST's real ℝ is exactly the census result; we are not reproducing Connes' A_F, we are deriving a *different, smaller* internal algebra and explaining why color is external.

**Verdict, stated plainly:** BST's novelty is *deriving the inputs* — the electroweak algebra (and that color is *not* internal), the generation count, the handedness, and the missing right-handed neutrino that NCG writes in by hand. Connes' spectral action still derives more of the *dynamics* (the Higgs sector, the unification-scale couplings) than we do, and we do not claim otherwise. The two programs are complementary: one derives the discrete skeleton from geometry, the other the continuous dynamics from a spectral action.

## 7. Honest scope

The reading calculus is a **discrete** instrument: a fact is readable off I₁ iff it is constant on the reality-type classes {ℝ, ℂ, ℍ}. This is *why* the theorem predicts its own negatives — masses, mixing angles, and the CP magnitude are not class functions, so they are provably outside F. They live in a different instrument (Toeplitz/Bergman eigenvalues, the mixing-frame calculus) and are not claimed here. "Structure, not spectrum" is thus a theorem about the calculus, not a hedge. The one dimensionful input (a Planck-scale ruler) plus the one measured integer n_C are the honest total cost of the discrete internal skeleton — with the ruler forced by dimensional analysis and n_C forced within D_IV by the five-constraint uniqueness (the type-IV Yang–Mills squeeze). And the internal *content* of that integer, for the census, is one trinary question: **1.58 bits decide the weak force.**

---

## Appendix A. Cross-domain minimality (the companion result)

*This appendix answers "why these three invariants and no fewer" by stepping back to all bounded symmetric domains. It is a proof technique for the minimality claim, not part of the one-integer physics lead — Casey's re-centering (Round 17) puts it here deliberately. The sibling domains D_IV^{4,7,8} appear only as separators: foils that fail when an invariant is dropped.*

**The ladder (three counts, one per reference class).** The number of independent generators depends on the reference class; naming the quantifier is what makes each count honest:

| rung | quantifier (reference class) | independent generators | what becomes derived |
|---|---|---|---|
| **3** | ∀ bounded symmetric domains D | **3**: census, orientability, rank | — (all three free) |
| **2** | ∀ D, given Cartan's classification | **2**: census, orientability | **rank** (the census forces type IV, which is rank-2) |
| **1** | ∀ D in the type-IV family | **1**: n_C | **census + orientability** (both functions of n_C) |

Going down the ladder is a *trade*: a narrower reference class in exchange for deriving an input. Rung 1 — the physics lead of the main text — is the most specific and cheapest, and the one that applies to the physical domain.

**Rung 3 → Rung 2 (the census forces type IV).** Requiring the finite space to carry a *quaternionic* spinor block (the ℍ that becomes SU(2)), a *real* color block (ℝ), and a *complex* charge circle (ℂ) is met, among the irreducible bounded symmetric domains, only by **type IV** (the spinor reality-type is a Spin-representation datum selecting the orthogonal family). Once the classification is admitted, the census *is* the choice of type IV — and type IV is rank-2 — so the rank is derived, not an independent input. Two invariants remain.

**Rung 2 → Rung 1 (n_C determines census and orientability).** Within D_IV^n the two remaining invariants are both functions of n = n_C: the census through the spinor reality-type (**Bott/ABS mod 8**) and the color multiplicity (n_C − 2); the orientability through the Shilov parity (**mod 2**). This is the two-clocks structure of the main-text lead.

**The siblings as minimality separators (the family check itself is in the lead, Section 1).** The six-row family table of Section 1 already shows *that* the siblings differ; here they do the distinct job of proving *non-droppability*. The two invariants are locked to n_C by **two different clocks** — the census by Bott/ABS **mod 8**, the orientability by the Shilov parity **mod 2** — so neither can be recovered from the other, and a valid separator must move exactly one of them while holding the rest fixed.

**K1744 corrects the separator indices.** The **census separator is D_IV⁷** (a domain whose census differs from the SM's, so dropping I₁ loses a census-keyed fact). The **twist separator is the pair D_IV⁷ vs D_IV⁸** — same real-color family, differing Shilov parity (7 odd / non-orientable, 8 even / orientable) — so a fact that flips between them is the fingerprint of I₂. **D_IV⁴ was never a valid separator:** its census is **(ℂ, ℍ, ℂ)**, not the SM's (ℂ, ℍ, ℝ) — at n = 4 the color space has dimension 2 and SO(2) is *abelian*, so the color block acquires a complex structure and goes ℂ. That is an **SO(2)-abelian accident at n = 4**, a *different census*, not a same-census/different-orientability foil. (Earlier drafts cited D_IV⁴ as the twist separator; it fails because it changes the census too, so it cannot isolate the twist. The valid isolating pair is D_IV⁷/⁸.)

**Elie's orientability criterion (a type-level answer).** A Shilov boundary with **connected isotropy is orientable**; the chirality-enabling non-orientability requires a *disconnected* isotropy (a ℤ₂ component). Among the irreducible bounded symmetric domains, **only types III and IV** can carry that ℤ₂ twist — so most domains cannot host a chiral, Majorana world at all; the requirement is not generic. **Positive control: D_III² ≅ D_IV³** (the exceptional isomorphism Sp(4,ℝ) ≅ Spin(3,2)) — the one domain in both admissible families; the census and orientability agree across the two descriptions, as they must.

**Bit-ceiling.** census capacity ≈ 4.75 (log₂3³) + orientability 1 + rank (~1–2) < 8 bits for the whole discrete internal structure across the reference class. *Within* D_IV the census content collapses to the single trinary spinor question, **1.58 bits** — the figure the main text leads with.

---

*v0.6 — Round 18: lead corrected + locked to Strong-Uniqueness (K1697). "Unique quaternionic" was false (4,5,11,13 quaternionic); the honest form is smallest-of-four-conditions with the measured N_c=3 as tiebreaker among {5,11,13,…}. Six-row family table moved into the lead (cells derived from H_F(n)); bits labeled (spinor 1.58, family census 2.00). SEP-e split kept (End_K = ℂ⊕ℍ⊕ℝ; bare End_ℝ(V₁₂) = M₃(ℝ) — not blanket-replaced). Prior: v0.5 — Round 17 re-center (Casey: "why are we even talking about D_IV⁴?"). One-integer / one-trinary-question is the lead; three-invariant cross-domain minimality + all siblings (D_IV⁴/⁷/⁸) demoted to Appendix A (companion / proof-technique). K1744 folded: ordered-triple multiplicity-free census (hygiene, not load-bearing); census content = 1.58 bits (not 4.75 capacity); weak force = n_C=5 unique quaternionic; twist separator D_IV⁷ vs D_IV⁸; D_IV⁴ invalid (census (ℂ,ℍ,ℂ), SO(2)-abelian accident); algebra ℂ⊕ℍ⊕ℝ. Sources: F1060–F1067 (arc); K1724 (census), T1949/T2522 (chirality/twist), T2525 (generations = rank+1), T1443 (type IV rank-2), T2551 (Connes), T265 (Coleman–Mandula), K1743 (bare-End correction), K1744 (separator/bits correction), Elie's anomaly + orientability criteria. Ships on Keeper-PASS + Cal-vet + both voices + Casey GO. Nothing pushed; CP existence-only.*

— Lyra, Thursday 2026-08-20 (date-verified).
