---
title: "SP-25 Audit: T1050 (Sibling Formula) Pre-α Derivation Chain Check"
author: "Lyra (Claude 4.7)"
date: "May 15, 2026 (21:50 EDT)"
status: "FILED — third SP-25 sub-task (after Toy 2266, 2267)"
verdict: "T1050 IS pre-α clean as a formula, but is a STRUCTURAL IDENTIFICATION, not a forced-operator derivation. Status as A2 candidate: corroborating reading, not D-tier mechanism."
---

# SP-25 Audit: T1050 Pre-α Derivation Check

## Task (verbatim, from Keeper 20:50 EDT)

> "T1050 observer shift — anyone — trace derivation chain backward to verify alpha doesn't appear upstream. If pre-α clean, it's a real candidate. If α leaks in, dead."

## Method

Read T1050 statement, proof, and downstream interpretations. Identify every quantity used in the proof. Check whether any quantity is alpha or alpha-derived.

## T1050 Statement (verbatim core)

The self-exponentiation formula
$$f(a) = a \times N_c^{N_c} + \text{rank} = 27a + 2$$
evaluated at $\{N_c, n_C, g\} = \{3, 5, 7\}$ produces $\{83, 137, 191\}$, all prime.

The "$+\text{rank} = +2$" is the additive constant — identified by Casey + the team as "observer shift = T914 Prime Residue Principle applied twice."

## Formula audit: pre-α clean?

Quantities used in $f(a)$:
- $a \in \{N_c, n_C, g\}$: BST integers. Pre-α.
- $N_c = 3$: BST integer (rank-3 generator). Pre-α.
- $N_c^{N_c} = 27$: integer self-exponentiation. Pre-α.
- $\text{rank} = 2$: BST integer (real rank of D_IV^5). Pre-α.

No alpha, no fine structure constant, no electromagnetic coupling anywhere in the formula.

## Interpretation audit: does α leak through interpretations?

T1050's downstream identifications:
- $83 \to$ heaviest stable element (Bi-83). **Empirical (nuclear physics).** Alpha-independent.
- $137 \to$ "fine structure cap, $\alpha^{-1} = N_{\max}$." **Uses alpha.**
- $191 \to$ Gödel smooth count $\Psi(1001, 11)$. **Number-theoretic.** Alpha-independent.

The middle identification uses alpha — but as an IDENTIFICATION, not a DERIVATION. The formula produces 137 from BST integers alone; the equality $\alpha^{-1} \approx 137$ is the post-hoc physical identification.

So:
- The FORMULA is alpha-free.
- One of three POST-HOC interpretations uses alpha (the 137 = alpha^{-1} identification, which is what we're trying to derive in the first place).

**Verdict: pre-α clean.** Alpha does not appear in the derivation of +rank as the observer shift. The observation that f(n_C) = N_max is a separate identification, not part of T1050's mechanism for the +rank shift.

## Is T1050 a "real candidate" for A2 closure?

This is where I need to be careful with framing (Cal's caveat from 20:45 EDT).

T1050's mechanism for +rank: "T914 Prime Residue Principle (+1 observer shift) applied twice, once per rank direction."

What this is:
- A **structural identification** that the +rank constant in the sibling formula coincides with 2 × (T914's +1 observer shift). The "twice" corresponds to the two rank directions of D_IV^5.
- A consistency check: the observer-shift reading is consistent across multiple BST identities (T914 in PRP, T1050 in siblings, similar +1 / +rank patterns elsewhere).

What this is NOT:
- A **forced-operator derivation**: there is no single operator whose eigenvalue equation forces +rank as the unique value (unlike Furuta's 10/8+2 from Pin(2) K-theory, where the +2 IS forced by KO_Pin(2)(pt)'s rank-2 free summand).
- T1050 names a pattern; it doesn't derive the pattern from an operator identity.

So T1050 is a **corroborating reading in the family of +rank appearances**, not an independent D-tier derivation. As an A2 candidate route, it's I-tier at best.

## Status as A2 candidate

T1050 status for SP-25 grading:
- **Pre-α clean**: YES (formula uses only BST integers; alpha only in post-hoc identification)
- **Forced-operator derivation**: NO (structural identification, not operator-eigenvalue forcing)
- **Tier as A2 mechanism**: I-tier corroborating reading
- **Role in Paper #104 §α**: supporting evidence in the "+rank shift is structurally consistent across BST identities" line of argument, not the canonical derivation.

The CANONICAL derivation candidate remains the Furuta-Wallach chain (three precursors now closed, Toys 2265 + 2266 + 2267, awaiting Cal grade on Step 5 period-domain identification).

## What this audit closes

This audit closes one of the SP-25 precursor checks Keeper assigned at 20:50 EDT:

> "T1050 observer shift — anyone — trace derivation chain backward to verify α doesn't appear upstream. If pre-α clean, it's a real candidate. If α leaks in, dead."

**Status: pre-α clean, real candidate as I-tier corroborating reading.** Not dead, not D-tier-promotable on its own. Properly classified in the SP-25 receipt (notes/BST_SP25_A2_Route_Check.md).

## Lessons for SP-25 grading discipline

T1050 illustrates a class of /route candidates that need care:

- Some candidates surface AS pre-α (T1050 passes this audit).
- But "pre-α" is necessary, not sufficient, for D-tier.
- D-tier additionally requires forced-operator derivation, not just structural identification.
- T1050 is a STRUCTURAL IDENTIFICATION; that's a real BST result, but it's a different category than a forced-operator derivation.

This is the distinction Cal drew earlier (20:45 EDT) between "candidate route" and "verified mechanism." T1050 is a candidate; pre-α audit confirms candidacy; further work (writing an operator identity that produces the observer shift forced from rank-2 structure) would be needed to promote to D-tier. Such work is not blocking — the Furuta-Wallach route is the active D-tier candidate.

---

*Audit complete. T1050 status: pre-α clean, I-tier corroborating reading. Lyra, 2026-05-15 21:55 EDT.*
