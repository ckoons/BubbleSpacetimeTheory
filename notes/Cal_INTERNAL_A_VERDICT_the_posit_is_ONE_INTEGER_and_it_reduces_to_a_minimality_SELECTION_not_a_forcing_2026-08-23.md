---
node_type: referee_verdict
id: Cal-internal-A-verdict
title: "Internal A closed at PARTIAL-CONDITIONAL with the residual named to one integer. The three namings of the posit -- 'the invariant is quadratic', 'the complement is atomic', 'a primitive commitment is two-outcome' -- are VERIFIED equivalent, and equivalence means they are one posit stated three ways, which does not reduce it. But the posit is smaller than it looks. Two of the four steps in the chain ARE derivable: repeatability forces idempotence (e.e = e is what 'measuring twice gives the same answer' says), and NONTRIVIALITY forces rank >= 2 (rank 1 is R, whose only idempotents are 0 and 1, so no nontrivial commitment exists there -- verified). And rank 2 -> type IV is a THEOREM, not a posit: the simple rank-2 Euclidean Jordan algebras are exactly the spin factors, whose bounded symmetric domains are the Lie balls D_IV^n (Jordan-von Neumann-Wigner; cited to Faraut-Koranyi, needs a primary pin). So the entire residual sits on ONE step: rank = 2 rather than rank >= 3. That step is MINIMALITY -- the minimal rank admitting a nontrivial commitment -- and minimality is a SELECTION PRINCIPLE, NOT A DERIVATION. Verdict: not derivable as a forcing; reducible to a minimality selection, which is a real result and closes the cell. TWO REFEREE WARNINGS ATTACHED: (1) isotropy does no rank work -- every D_IV^n is rank 2 for all n >= 3 and the other EJA families run over all ranks, so isotropy delivers the symmetric-space structure and cannot be what forces rank 2; naming it in the forcing chain overstates its role. (2) rank = 2 is ALREADY a banked BST primitive, so 'commitment forces rank 2' and 'rank 2 is a BST input' are the SAME FACT and must never be counted as two independent legs of a uniqueness argument."
date: 2026-08-23
author: Cal
verdict: "Internal A: CLOSED at PARTIAL-CONDITIONAL. Chain is four steps with exactly ONE selection in it -- repeatability -> idempotence (DERIVED); nontriviality -> rank >= 2 (DERIVED, verified); rank = 2 (SELECTION, minimality); rank 2 -> type IV (THEOREM, cited); which n (OPEN). The honest statement is 'it is the posit, and here is exactly how small it is': one integer, reachable by minimality but not by forcing. Never 'commitment forces D_IV^5' -- rank 2 yields the type IV FAMILY for every n >= 3 and says nothing whatever about n = 5, so dimension remains separately and fully open. Cited classification facts need a primary pin to Faraut-Koranyi before banking; the consequences I checked numerically (complement-of-a-primitive is primitive at rank 2 and is not at rank 3; rank 1 admits no nontrivial idempotent). Nothing pushed."
related: [T2543, Internal-A, K1809]
---

# Cal — Internal A. The posit is one integer, and it is a selection, not a forcing.

**The question:** is *"a primitive commitment is two-outcome"* derivable from commitment + isotropy, or is
it the irreducible posit?

## 1. The three namings are equivalent — verified, and that is not progress

| naming | Jordan-algebra content |
|---|---|
| *"the invariant is quadratic"* | characteristic polynomial has degree = **rank**; degree 2 ⟺ rank 2 |
| *"the complement is atomic"* | e primitive ⟹ 1−e primitive ⟺ **rank 2** |
| *"a primitive commitment is two-outcome"* | a Jordan frame has **2** elements ⟺ rank 2 |

**Checked, not asserted.** In the spin factor ℝ⊕V the primitive idempotents are (1/2, u) with \|u\| = 1/2;
the complement (1, 0) − (1/2, u) = (1/2, −u) has \|−u\| = 1/2 and **is primitive** — verified at n = 3, 5, 7.
In Sym₃(ℝ) a primitive idempotent is a rank-1 projector and its complement has **rank 2 — not primitive**.

> **All three say `rank = 2`. They are one posit in three costumes, and restating a posit three ways does
> not reduce it.** *(Worth saying plainly, because three equivalent namings can read as three
> corroborating arguments. They are one.)*

## 2. But two of the four steps ARE derivable, and that shrinks the residual a long way

**Step 1 — repeatability ⟹ idempotence. DERIVED.** *"Measuring a committed record twice returns the same
answer"* **is** e∘e = e. T2543's "committed records are idempotents" is not a posit; it is the algebraic
transcription of repeatability.

**Step 2 — nontriviality ⟹ rank ≥ 2. DERIVED.** The rank-1 EJA is ℝ, whose idempotents solve x² = x,
giving **x ∈ {0, 1}** and nothing else. **At rank 1 a nontrivial commitment does not exist.** So rank ≥ 2
is forced by the mere existence of a commitment that is not the trivial one. **Verified.**

**Step 4 — rank 2 ⟹ type IV. THEOREM, not posit.** The simple Euclidean Jordan algebras of rank 2 are
**exactly the spin factors** ℝ⊕V, whose bounded symmetric domains are the Lie balls **D_IV^n**
(Jordan–von Neumann–Wigner classification). *(Cited to Faraut–Korányi; **needs a primary pin to the book**
before this is banked — I verified the consequences numerically, not the classification itself.)*

## 3. ⟹ The whole residual is ONE step, and that step is minimality

Steps 1, 2 and 4 carry themselves. **What remains is exactly:**

> **rank = 2 rather than rank ≥ 3.**

And there is a reduction available, though not the one hoped for: **rank 2 is the minimal rank admitting a
nontrivial commitment.** Step 2 gives rank ≥ 2; taking the minimum gives rank = 2.

**Minimality is a selection principle, not a derivation.** It picks a member of an admissible set by an
ordering we supply; it does not exclude rank 3 on physical grounds. **So the honest answer to the cell's
question is:**

| | |
|---|---|
| **Derivable as a forcing?** | **No.** |
| **Reducible?** | **Yes — to a minimality selection on rank, with the ordering (rank) natural rather than chosen for convenience.** |
| **Residual** | **one integer: rank = 2, selected as minimal, not forced.** |

**That closes the cell at PARTIAL-CONDITIONAL with the residual named exactly** — which is the outcome
this cell was scoped to accept, and it is a smaller residual than "a posit."

## 4. ★ Referee warning one — isotropy does no rank work, and naming it overstates the chain

The standing phrasing is *"commitment + isotropy forces type IV mod one posit."* **Isotropy cannot be
carrying the rank.**

- **Every D_IV^n is rank 2, for every n ≥ 3.** Isotropy does not distinguish them.
- The other EJA families (Sym_n(ℝ), Herm_n(ℂ), Herm_n(ℍ), Herm₃(𝕆)) give isotropic domains **at every
  rank**. Isotropy does not exclude rank 3.

**What isotropy delivers is the symmetric-space structure — i.e. that we are on the classified list at
all.** That is real and necessary. **But the step that lands on type IV is rank = 2, and rank = 2 is the
posit.** ⟹ **The honest chain is "commitment ⟹ Jordan structure; isotropy ⟹ bounded symmetric domain;
rank = 2 ⟹ type IV" — three distinct jobs, and the posit sits in the third, alone.**

## 5. ★★ Referee warning two — one fact, one vote

**rank = 2 is already one of the five banked BST integers.**

> **"Commitment forces rank 2" and "rank 2 is a BST primitive" are THE SAME FACT.** They must never be
> counted as two independent legs of a uniqueness or over-determination argument.

This is the consistency-web caution in its sharpest form: **a single input read through two vocabularies
is one input.** If Internal A's closure is later cited alongside the five-integer count as corroboration,
that is double-counting, and a referee will find it immediately because the integer is the same integer.

## 6. Dimension — still fully open, and the classification says why

**rank 2 yields the type IV FAMILY for every n ≥ 3.** It constrains n not at all. So:

> **Never "commitment forces D_IV⁵."** Commitment + isotropy + minimality reach **D_IV^n**, a family.
> **n = 5 is untouched by this argument** and its minimality (n ≥ 5, and why not 7) is owed separately.

## What would change the verdict

A genuine derivation would need an argument that **excludes rank 3** on grounds other than "2 < 3" —
something about commitment, or about the substrate's dynamics, that a rank-3 Jordan frame cannot satisfy.
**I do not see one, and I looked for it in the direction of the complement condition** (rank 2 is the only
rank where negation of an atom is an atom, which is suggestively bit-like). **But "negation of an atom is
an atom" is just rank 2 again** — the third naming, not a new argument. **If someone finds a physical
requirement that forbids a three-outcome primitive commitment, this becomes a derivation. Absent that,
it is a selection, and saying so is the result.**

— Cal, 2026-08-23. Internal A closes with the residual at one integer: repeatability and nontriviality are
derived, rank-2-to-type-IV is a theorem, and everything not yet earned is concentrated in "rank = 2 rather
than 3," which minimality reaches and forcing does not. Isotropy is not doing the work the phrasing gives
it, and the residual integer is one we already bank — so it is one fact, not two.
