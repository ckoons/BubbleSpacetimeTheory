---
title: "Lecture 10 — The Method, and How to Kill It"
spine: "D_IV⁵: QM, GR and the SM — the derivations, tiered"
author: "Keeper, for Casey Koons and the team"
date: "2026-09-11 — v0.1"
sources: "The tier system (D / PD / I / C / S; PD only in explicit-split form); 'Forcing and Evidence' v1.0.1 (#31); the falsifier register v0.8 with its fired-and-lost Section E; the Six Absences; the audit chain (K-audits; Cal's numbered referee log; D-tier promotion delegated to Cal + Keeper with Casey's override); the pre-registration protocol (SHA256 before the numbers; landings and tolerances pre-committed; half-blind); the state-of-the-program one-pager (2026-08-26); K1816, K1801, K1809, K1889, K1891, K1892 (the failures this lecture names); the memory rules that came out of them"
tier_line: "This lecture makes no physics claim. It states the program's epistemic method and the list of measurements any one of which ends the program."
---

# Lecture 10 — The Method, and How to Kill It

## The question

How do we know what we know — and what would make us stop?

Most of this course has been about what we found. This lecture is about how we kept ourselves honest while finding it, because with a shape this rich the danger is not that you find nothing. It is that you find everything. A geometry with five small integers and a few transcendental constants can be made to land within a percent of most of the numbers in a physics data table, and a program that does not know this about itself will publish coincidences as results and never learn the difference. We learned the difference the hard way, more than once, and the rules below are the residue.

## For the reader in a hurry

Our rules are simple. Every claim carries a word that says how much to believe it, in the sentence that makes the claim. Every number that could have been tuned is computed with the answer hidden and the procedure written down and hashed first. Every failure is published in the same voice as every success. And there is a short list of experimental results — no grand unification, no proton decay, no right-handed weak bosons, no magnetic monopoles, no sterile neutrinos, no supersymmetric partners — any one of which, confirmed, ends the program. We would rather you read that list first.

## Four words, used exactly

Every result in this program carries one of four words, and the words are not decoration.

**Derived.** The mechanism is proved and the inputs are named in the statement. Not "the inputs are few" — *named*. Lecture 5's hypercharge theorem says "given the observed charged spectrum" in its first clause, because it is.

**Identified.** The formula matches the number and we do not claim the mechanism. An identification is a *candidate* — a place to look — and never evidence. The tier guide says so on its face, and Lecture 8 shows why: the program's most famous identification, $137$, sits in the bulk of a null.

**Floored.** Closed by a theorem, with the kind of idea that could reopen it named. A floor is not a failure; it is the strongest form of "we do not know," because it says what we would need to know.

**Open.** We do not know, and we say so, in the text and not in a footnote.

There is a fifth word, *partially derived*, and it is allowed only in explicit-split form — "the order is derived, the value is input" — never as a blended adjective. And the tier words never migrate: "derived" describes the mechanism it was earned by and does not slide onto the value that sits beside it. Half of the corrections in this Spine are cases where it had.

## Forcing and evidence

The program's reviewer paper, "Forcing and Evidence," is the standard the whole corpus is held to, and its rules are short.

*The instrument validated must be the instrument used.* If you show a null test works on decoys, the test you then run on your own number is that test, unchanged.

*A null with a free sampling range is not a null until you sweep it.* Choosing the range after seeing the target is choosing the answer.

*"Smallest of $N$" presupposes an enumerable, theory-generated family, and $N$ is reported.* Naming $N$ when $N$ is the noise level dresses noise as bounded ambiguity.

*Count over ranking.* The number of integer forms that fit a band is target-independent; which one fits best is not. Report the count. (Lecture 7's $\gamma$ has ten.)

*A control that passes can be the wrong control.* Validate the last stage of the pipeline, not only the functional it feeds.

*Enumerate the inputs.* A decomposition is an identity unless it has an input that could have produced a different number; and when the geometry hands back the program's own integers, that is the reason to check hardest, not to celebrate.

## Pre-registration, as we practise it

Before a number that could be tuned is computed, three things are written down and hashed: the *procedure* (a bar with an unfrozen procedure is a tuning channel), the *landings* — what counts as success, what as failure, what as neither — and the *tolerances*. The hash is posted. Then the computation runs, half-blind where a second CI can hold the target. Then the envelope is opened.

Lecture 7's five sealed series and Lecture 8's forced vertex are the worked examples. Both failed. Both are in the register with the same ceremony as the successes — rows E6 and E1 of a section titled *fired and lost* (E6 was registered on 2026-09-11; for the hours before that this sentence was false, and Cal caught it) — because a falsifier that has never fired is a claim, and a program whose falsifiers never fire is not being tested.

## The audit chain

Nothing in this program is banked on its author's word. A result is registered as a row; the row is audited by the consistency auditor (a K-number); a visiting referee cold-reads it (a numbered section of his log); promotion to the derived tier is delegated to those two jointly, with the principal investigator holding the override. A retraction is itself a claim and goes through the same chain.

The part a reader should test is the recursion. **The checkers check the checkers, and the record shows it.** In one packaging week the machinery caught seven errors upstream of any computation — two of them against the gate-writer and the checker themselves — and then two instrument errors inside the verification layer, one per verifier, each disclosed by its own operator. The audits are public. So are the retractions, including the ones against the auditors.

## What went wrong, told plainly

A method is only as good as what it caught, so here is what it caught in this program's own house, with the instruments built afterward.

- The scorecard said "$\alpha$: derived" for twelve days after the registry had demoted it to identified with an instruction not to cite it externally (K1816). *Instrument:* the start-of-day check that fires when a retired reading is cited as a bank.
- The integer $7$ was called the genus for four months; the genus is $5$ (K1889). *Instrument:* the genus sweep across 29 rows; the rule *quote the invariant, not the coordinate*.
- A row registered fifteen days before the ruling that struck its colour clause was never swept — and as this Spine was first drafted the registry edit itself had still not been made, two days after the ruling; the Spine said "struck" and Cal caught it the same afternoon — because sweeps chase a ruling's consumers and a decorative clause looks like nobody's consumer (Cal Section 945). *Instrument:* a derived retirement inventory that replaces a hand-kept list, so that a ruling fires for retirements nobody remembered to add (K1891).
- One curated chapter carried three mutually inconsistent values of the Cabibbo angle (K1801). *Instrument:* a single-source state block that every front matter copies from and none retypes; and, as of this Spine, a check that fires when a retired reading appears in the presentation layer at all (K1892).
- Five wrong claims by the auditor in one day, two of them hashed from a story or an entry cell instead of from an instrument on the object. *Rule:* a number without a retained instrument is a memory, not a measurement — point at the toy that made it or rerun under one.
- A falsifier the program called its sharpest — a sub-Tsirelson ceiling on Bell correlations — was registered in May 2026 with a one-year experimental window, and had been refuted in October 2015 at $41.9\sigma$ (register E4; Lecture 3). *Rule:* a falsifier that names an experiment is checked against the literature the day it is registered, not the day someone quotes it.

We do not tell you this to perform humility. We tell you because a reader deciding whether to trust Lectures 1 through 9 is entitled to know how the errors in them get found, and by whom, and how fast.

## How to kill it

**The forbidden list.** The framework cannot absorb any of the following; a confirmed detection ends it.

| absence | what would fire it |
|---|---|
| no grand unification | a unification scale with the running couplings meeting |
| no proton decay | a proton decay event at any lifetime |
| no right-handed $W$ or $Z'$ | a right-handed charged current or a heavy neutral partner |
| no magnetic monopoles | one monopole |
| no sterile neutrinos | a sterile state (Lecture 5's one-bit mechanism forbids it) |
| no SUSY spectrum | a superpartner |

**The live falsifiers — the register's Section A, reproduced** (v0.11, 2026-09-14), each with the lecture that owns it and the measurement that fires it: **A1** a genuine stochastic-Λ wobble or phantom crossing — forbidden from the mean and the variance (Lecture 9); **A2** CKM first-row unitarity resolving against unity — the direct sum confirmed short (Lecture 7); **A3** a confirmed sterile neutrino (Lecture 5); **A4** a right-handed $W$ or gauged $B-L$ (Lecture 5); **A5** neutrinos proven Dirac (Lecture 5); **A6** a nonzero lightest-neutrino mass (Lecture 6); **A7** Koide's $Q$ moved off $2/3$ by an improved $\tau$ mass (Lecture 6). **A8** the order of the mixing corner — an order-one $|V_{ub}|/|V_{cb}|$ would falsify the position (Lecture 7; registered 2026-09-13). **A9** $\varepsilon \neq 0$ — a confirmed kinematic boost mismatch between the radiation and matter rest frames, read as $\ell = 1$ moments on the induced slice, surviving the pre-registered escape hatch; observable the Ellis–Baldwin test, current state Secrest 2022, not decidable as it stands; the decider — the redshift dependence, one shared boost across the count and redshift channels — is pre-registered on Quaia as a replication of Wu & Xia 2026 (arXiv:2608.30914, DESI DR1) with an independent estimator, frozen v1.5.2 hash `8013d959…` after seven declared re-freezes; **run 1 on Quaia certified 2026-09-17 10:12: Landing C, not decidable, on both samples** — the design's own checks fired before the CMB target was read (K1910, K1911); A9 stays live and the next catalogue is chosen on what the C taught (Lecture 9; ruled Cal Section 957; registered 2026-09-14, register v0.11); a forced $p$ outside $(0,2)$ (Lecture 9; the form's own kill condition, F-section); a fourth generation (Lecture 6; standard exclusion, no row); a free coloured state at a detector (Lecture 5; the (A1) theorem's kinematic exposure, no row). A summary lecture is where a reader expects the register reproduced; an earlier draft of this paragraph was four rows off in each direction.

**The doors** — not falsifiers but the named openings a new idea could walk through: the α-hole — nothing in the dictionary now carries $\alpha$ (Lecture 3, Lecture 8; the "Bergman-to-Hardy link" an earlier draft named here was dissolved by T2630/K1888); a mechanism for the colour identification from outside the geometry, of a stated shape (Lecture 2); a non-measure weight for the mass tower (Lecture 6); a forced $p$ (Lecture 9); whether $\alpha$ is in the geometry at all (Lecture 8).

**The inputs, counted** — because Lecture 2 promised this lecture would count them. To the choice of the object: one identification (colour count = characteristic multiplicity; posited, and provably not supplied by the geometry) and one datum (three colours; measured). Downstream, each named in the lecture that uses it: the positive-time sector (Lecture 4; T2625 (i), a posit); the observer input that selects the frame (Lecture 9; T2565); the mass scale, $m_e$ as the ruler (Lecture 9); in the hypercharge theorem, the observed charged spectrum (Lecture 5; one of its four stated inputs); in the mixing sector the corner's value, $\delta_{CP}$'s magnitude and $A$ — *open* in the register's vocabulary, taken from measurement where used (Lecture 7); and the fermion masses themselves, likewise open (Lecture 6). That is the honest list. It is not "zero free parameters," and it is not nineteen either; it is one identification, one datum, three structural posits (the sector, the frame, and P2b — the fourth of the posits T2631 names in the axioms' chains), one ruler, and the sector-level inputs the ledger counts as *input* or *open* — seven of the twenty-six primaries open and two input, on the generated table.

**And the standing exposure**, which is the honest way to end: the one dimensionless input to the choice of the object, the colour identification, could be the wrong reading of the multiplicity $3$. If it is, Lecture 2's theorem still stands — the object is still the unique domain with $a = 3$ — and everything that leans on $N_c = 3$ is a coincidence with a very good disguise. We have proved the geometry cannot settle that question by itself. Something outside it must, and we have said what shape it must have.

## How to check any of this without trusting us

`python3 play/verify_bst.py` — fifty comparisons in seconds. The theorem registry, `notes/BST_AC_Theorem_Registry.md`, with every row dated and every retirement marked in place. More than five thousand seven hundred single-claim toys in `play/` (the counter, 2026-09-11). Every K-audit and every section of the referee's log, in `notes/`. The falsifier register with its fired-and-lost section. And this curriculum's own staleness stamp, at the top of every front matter, with the K-number it was last synced to — so that when we fall behind again, and we will, you can see by how much.

The mathematics is on GitHub. That sentence is not a slogan. It is the argument.

## Where to look

"Forcing and Evidence" v1.0.1; the falsifier register v0.11 (2026-09-14; E4–E6 and F4 on 09-11, A8 on 09-13, A9 live and pre-registered on 09-14); the one-page tier guide with its printed failure condition; the rubric's Section 2, which is the authoritative scorecard; the state-of-the-program one-pager of 2026-08-26; and the audits named above, each of which is a file whose title says what it found.
