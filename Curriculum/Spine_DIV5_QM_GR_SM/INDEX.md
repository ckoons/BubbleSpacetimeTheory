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
> *Last accuracy-synced: 2026-09-11 12:58 (K1892; rulings through Cal Round 142 C1). One registry edit is owed and named: T2543's colour clause was RULED struck on 09-09 and the row still carries it. This block lives in `notes/BST_PRESENTATION_STATE_BLOCK.md` and is copied into every front matter by `play/sync_presentation_state.py`. Edit it there, nowhere else. Where any chapter and this block disagree, the block wins; where this block and the theorem registry disagree, the registry wins.*
>
> **The object.** One rank-2 bounded symmetric domain, D_IV⁵ = SO(5,2)/[SO(5)×SO(2)], and one measured number taken openly as the ruler. Its genus is 5; the integer 7 the program calls g is a definition (the signature p+q), not the genus — a mislabel that stood from May to September and is now swept.
>
> **Why this object — honestly.** Among all irreducible bounded symmetric domains of rank at least 2, D_IV⁵ is the unique one whose characteristic multiplicity is 3 (a theorem, checked three independent ways). That 3 is *identified* with the number of quark colours; the identification is numerical, and the bridge that would make it a mechanism is proved absent — the geometry supplies U(1)·SO(3), four dimensions, where colour needs SU(3)'s eight, and its triplet is self-conjugate where colour's is not. So the selection is a fit with one measured input — the one dimensionless input *to the choice of the object*; the program has further inputs downstream (masses, a mixing corner, a CP phase), counted in the ledger — not a forcing. We do not claim zero free parameters.
>
> **Derived** (mechanism proved; inputs named in the statement): the gauge-group skeleton · one fermion generation as the 16-real spinor with every hypercharge from one four-input theorem · a single-chirality positive-energy spectrum · three generations as rank+1 strata (and m₁ = 0) · the conserved charges · the mixing sector's mechanism and its **order** — the 1–3 corner one power below the 2–3 · the Cabibbo angle, blind (λ = 1/√20) · time: the K-centre SO(2) is the clock, the arrow is dynamical, the tick is N_max·ħ/(m_e c²) · quantum mechanics on the Hardy space H²(D_IV⁵), with the Hua branching weights as the Born probabilities of the write tuple (3/7 with no table consulted). The ten Dirac–von Neumann axioms are recovered; that count is quoted here at the tier of its registry row, which is owed, and not as "10/10" until the row exists.
>
> **Identified** (formula matches; mechanism not claimed): α⁻¹ = 137-class expressions · the electron's anomalous moment (our four "Selberg terms" are the four summands of Petermann–Sommerfield's 1957 closed form; the match is real, the derivation is not ours) · the asymptotic-freedom coefficient b₀ = 7 read as g · the exact mixing values · Newton's G: the relation between G and the electron mass is a theorem (K1673; 0.065%) that trades one dimensionful input for another and carries α inside it, so the value is a relation, not a prediction from nothing · assorted precision matches whose own null tests show small-integer expressibility is cheap.
>
> **Floored** (closed by a theorem; reopenable only by a named kind of idea): Koide's source · the mass-tower/generations mechanism · the ℓ = 2 / su(3) native dynamics · Λ's value (a closed structure with one named obstacle, the power p) · the nucleation survivor (no lawful initialisation vector; a distribution on the winding count) · the Riemann row (an attempt with a location, closed and parked) · the four-colour row (the One-Word Lemma refuted in frame; the derived lemmas stand).
>
> **Fired and lost** (pre-registered, certified, published with the same ceremony as wins): α is not the bare geometric vertex — the forced candidate computes to 8π³/3, closing the fifty-year volume-reading class · the thermal-generations mechanism died at the order level · the Q⁵ parity fold is a projector with no scale of its own · five named series for the mixing corner, sealed by hash, all missed · the commit-Boltzmann ladder failed its own 5% line.
>
> **Forbidden** — any confirmed detection kills the framework: grand unification · proton decay · right-handed W or Z′ · magnetic monopoles · sterile neutrinos · a SUSY spectrum.
>
> **How to check any of this without trusting us.** `python3 play/verify_bst.py` · the theorem registry (`notes/BST_AC_Theorem_Registry.md`) · the falsifier register with its fired-and-lost section · two thousand single-claim toys · every audit, retraction and correction in the open, including the ones against the program's own auditors. The count that matters for the Standard Model row: **8 of the 26 primary dimensionless parameters are sourced clean** (Grace's ledger, v0.54). The honest sentence: everything reachable is derived, floored with a theorem, or published as a loss; what remains open is a short list of named doors that only new ideas — not labour — can open.
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
