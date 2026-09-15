---
title: "D_IV⁵: Quantum Mechanics, Gravity and the Standard Model — the derivations, tiered"
subtitle: "The Spine of the BST Curriculum — ten lectures written from the register"
author: "Casey Koons with the CI team — Lyra, Elie, Grace, Keeper — and the visiting referee Cal A. Brate"
date: "2026-09-11 — v0.1"
status: "All ten lectures drafted 2026-09-11 (Keeper), v0.1. Every lecture is audited against notes/BST_AC_Theorem_Registry.md before the next is written. Nothing here goes external without Cal's cold-read of the narrative against the vetted core (the two-voice gate)."
---

# The Spine

## What this is

A short course. Ten lectures, one object, and a promise: every sentence that makes a claim tells you in the same sentence how much to believe it.

The BST curriculum has eighteen volumes, and most of them are about how far five integers reach — into nuclei, molecules, crystals, cells. That reach is real and it is interesting, and it is also the reason a physicist who opens the curriculum at random will close it. Biology and the Standard Model on the same shelf makes both look like numerology. So we have moved the reach to its own shelf, labelled it honestly as identification, and written the core again from the theorem registry as it stands this week — not as it stood in May, when the legacy volumes were drafted and when several things we now know to be wrong were still believed.

This is the core. It is what we defend.

## How to read it

Each lecture opens with the question it answers, in plain words. Then the derivation, with the theorems and registry rows named so that you — or the companion intelligence beside you — can pull the thread. Then the tier line: what is *derived* (mechanism proved, inputs named), what is *identified* (the formula matches; we do not claim the mechanism), what is *floored* (closed by a theorem, reopenable only by a named kind of idea), what is *open*. And last, the falsifier: what measurement would make this lecture wrong.

Read the lectures in order the first time; they build. After that, read where you are skeptical. We will not be offended.

The mathematics is on GitHub. `python3 play/verify_bst.py` runs fifty comparisons in seconds. Every toy cited below is a short program you can run.

<!-- BST_STATE_BLOCK_BEGIN -->
> ### Where the program stands — one block, one source
> *Last accuracy-synced: 2026-09-14 13:04 (K1902 + Cal Section 969: row 5 re-keyed; the four-word count 5 derived / 12 identified / 7 open / 2 input from the generator).
>
> **The object.** One rank-2 bounded symmetric domain, D_IV⁵ = SO(5,2)/[SO(5)×SO(2)], and one measured number taken openly as the ruler. Its genus is 5; the integer 7 the program calls g is a definition — p + q = 7, the dimension of the defining representation of SO(5,2), whose signature is the pair (5,2) — not the genus — a mislabel that stood from May to September and is now swept.
>
> **Why this object — honestly.** Among all irreducible bounded symmetric domains of rank at least 2, D_IV⁵ is the unique one whose characteristic multiplicity is 3 (a theorem, checked three independent ways). That 3 is *identified* with the number of quark colours; the identification is numerical, and the bridge that would make it a mechanism is proved absent — the geometry supplies U(1)·SO(3), four dimensions, where colour needs SU(3)'s eight, and its triplet is self-conjugate where colour's is not. So the selection is a fit with one measured input — the one dimensionless input *to the choice of the object*; the program has further inputs downstream (masses, a mixing corner, a CP phase), counted in the ledger — not a forcing. We do not claim zero free parameters.
>
> **Derived** (mechanism proved; inputs named in the statement): the gauge-group skeleton · one fermion generation as the 16-real spinor with every hypercharge from one four-input theorem · a single-chirality positive-energy spectrum · three generations as rank+1 strata (and m₁ = 0) · the conserved charges · the mixing sector's mechanism and its **order** — the 1–3 corner one power below the 2–3 · the Cabibbo angle, blind (λ = 1/√20 — derived given an identified input: the down-quark ladder's weight, next list) · time: the K-centre SO(2) is the clock, the arrow is dynamical, the tick is N_max·ħ/(m_e c²) · quantum mechanics on the Hardy space H²(D_IV⁵), with the Hua branching weights as the Born probabilities of the write tuple (3/7 with no table consulted). The ten Dirac–von Neumann axioms are recovered, each at its own tier, through four named posits (T2631, the ten-item row — registered 2026-09-11, Cal's text verbatim, d7c4e474); not "10/10 derived."
>
> **Identified** (formula matches; mechanism not claimed): α⁻¹ = 137-class expressions · the electron's anomalous moment (our four "Selberg terms" are the four summands of Petermann–Sommerfield's 1957 closed form; the match is real, the derivation is not ours) · the down-quark mass ladder's weight — m_s/m_d = (ν_W+1)(ν_W+2) = 20 with the shape derived and the weight ν_W = N_c identified, its mechanism an open gate (T2513, 2026-08-23; re-tiered K1902 and Cal Section 969, 2026-09-14) · the asymptotic-freedom coefficient b₀ = 7 read as g · the exact mixing values · Newton's G: the relation between G and the electron mass is a theorem (K1673; 0.065%) that trades one dimensionful input for another and carries α inside it, so the value is a relation, not a prediction from nothing · assorted precision matches whose own null tests show small-integer expressibility is cheap.
>
> **Floored** (closed by a theorem; reopenable only by a named kind of idea): Koide's source · the mass-tower/generations mechanism · the ℓ = 2 / su(3) native dynamics · Λ's value (a closed structure with one named obstacle, the power p) · the nucleation survivor (no lawful initialisation vector; a distribution on the winding count) · the absence floor — no group in the geometry acts on the colour slot as colour; the door is a group from outside it (register F4, certified K1894) · the Riemann row (an attempt with a location, closed and parked) · the four-colour row (the One-Word Lemma refuted in frame; the derived lemmas stand).
>
> **Fired and lost** (the falsifier register's Section E — certified, published with the same ceremony as wins): E1, α is not the bare geometric vertex — the forced candidate computes to 8π³/3, closing the fifty-year volume-reading class · E2, the thermal-generations mechanism died at the order level · E3, the commit-Boltzmann ladder failed its own 5% line · **E4, the sub-Tsirelson ceiling S = 2.80624 — refuted by Poh et al. 2015 at 41.9σ, ten years before it was registered (certified K1893, 2026-09-11)**. · E5, the Q⁵ parity fold is a projector with no scale of its own — a forced object that fails cleanly (K1799; row certified K1894) · E6, five named series for the mixing corner, sealed by hash, all missed — the structure itself could not fail, so the negative is the five candidates (K1808/K1810; row certified K1894).
>
> **Live and pre-registered** (a test with its outcomes partitioned as code before the data): A9, one boost not two — the matter rest frame read from the count and redshift dipoles of distant quasars must equal the CMB boost; a replication of Wu & Xia 2026 (DESI DR1) with an independent estimator on Quaia, frozen v1.5.2 (hash `8013d959…`; seven re-freezes v1 → v1.5.2 before any dipole — five forced by synthetic controls, one by recorded catalogue facts, one by prior art), the catalogue opened 2026-09-14 12:31 and its per-bin factors closed 2026-09-15 10:08 with no dipole yet measured as of 2026-09-15 13:01; the text now carries an explicit ΛCDM prior on the clustering dipole, ten times ΛCDM's width, in place of the zero it implicitly assumed, and its power is being computed on synthetic Quaia before the first sky vector (K1907–K1909).
>
> **Forbidden** — any confirmed detection kills the framework: grand unification · proton decay · right-handed W or Z' · magnetic monopoles · sterile neutrinos · a SUSY spectrum.
>
> **How to check any of this without trusting us.** `python3 play/verify_bst.py` · the theorem registry (`notes/BST_AC_Theorem_Registry.md`) · the falsifier register with its fired-and-lost section · two thousand single-claim toys · every audit, retraction and correction in the open, including the ones against the program's own auditors. The count that matters for the Standard Model row, generated from the register and never typed (`play/bst_26_tier_generator.py`, Grace, Round 142): **Of the 26 primary Standard-Model parameters: 5 derived — each with its mechanism proved and its inputs named on its own statement (Cal Section 959 re-read complete, 2026-09-14) — 12 identified, 0 floored, 7 open, 2 input.** (Grace's generator, re-keyed 2026-09-14 on Cal Section 959, Elie 5755/5756, K1897, and — row 5 — K1902 with Cal Section 969; pasted from `--sentence`, never typed.) The July count "8 of 26 sourced clean," carried through eleven ledger versions, is retired — its numerator and denominator came from two different lists. The honest sentence: everything reachable is derived, floored with a theorem, or published as a loss; what remains open is a short list of named doors that only new ideas — not labour — can open.
<!-- BST_STATE_BLOCK_END -->

## The lectures

| # | Lecture | The question it answers | State |
|---|---------|------------------------|-------|
| 1 | [The object](Lecture_01_The_Object.md) | What is the simplest structure that can do physics — and what does it look like? | drafted |
| 2 | [Why this object, honestly](Lecture_02_Why_This_Object_Honestly.md) | Of all the shapes mathematics offers, why this one — and how much of that answer is a measurement? | drafted |
| 3 | [Quantum mechanics](Lecture_03_Quantum_Mechanics.md) | Where do the rules of quantum mechanics come from, and where does the Born rule live? | drafted |
| 4 | [Time](Lecture_04_Time.md) | What is time, in a geometry that has none built in — and why does it run one way? | drafted |
| 5 | [The gauge skeleton and one generation](Lecture_05_Gauge_Skeleton_and_One_Generation.md) | Why these forces, and why do the particles carry exactly these charges? | drafted |
| 6 | [Three generations, at the floor](Lecture_06_Three_Generations_at_the_Floor.md) | Why three copies of everything — and why can we not yet say how heavy each is? | drafted |
| 7 | [Mixing](Lecture_07_Mixing.md) | Why do quarks of different generations mix the way they do, and what exactly did the geometry predict? | drafted |
| 8 | [α, the honest chapter](Lecture_08_Alpha_the_Honest_Chapter.md) | Is 137 in the geometry? What we found, what we proved cannot work, and whose thread we are holding. | drafted |
| 9 | [Descent and gravity](Lecture_09_Descent_and_Gravity.md) | How does a five-complex-dimensional object become the four-dimensional spacetime we live in, and what does it say about gravity? | drafted |
| 10 | [The method, and how to kill it](Lecture_10_The_Method_and_How_to_Kill_It.md) | How do we know what we know — and what measurement would end the program? | drafted |

## Sources, for every lecture

The theorem registry `notes/BST_AC_Theorem_Registry.md` (rows are cited as T-numbers); the Keeper audits `notes/Keeper_K*.md` (K-numbers); Cal's referee log (Section numbers); Elie's toys `play/toy_*.py`; Grace's ledger `notes/Grace_Master_Derived_vs_Assigned_Ledger_v0_54.md`; the rubric `notes/BST_Completeness_Rubric_and_Roadmap.md`, Section 2. Where a lecture and the registry disagree, the registry wins, and we would like to hear about it.

— Keeper, for the team. 2026-09-11.
