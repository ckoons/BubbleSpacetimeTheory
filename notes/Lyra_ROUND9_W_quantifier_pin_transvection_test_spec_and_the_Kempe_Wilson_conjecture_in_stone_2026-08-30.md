---
title: "Round 9 — the W-quantifier pin (one sentence, plus the naming rule that prevents the next collision); the transvection test spec for tonight's stored gate words (with the McLaughlin routing table); and the Kempe–Wilson conjecture in stone with its proof skeleton"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 17:21 EDT at round start)"
status: "ROUND 9. The pin is Cal's to freeze into the harvest schema; the spec is Elie's to run tonight; the conjecture is pre-registered, can-fail, with its exceptional list OPEN. Nothing banks."
---

# 1. THE W-QUANTIFIER PIN (first action, as ordered)

**PIN: W is per-GRAPH — W(G) := Span_GF(2) of the achieved straddle indicators over the FULL
stated population of G (all classes); per-class spans are a different object and get a different
symbol: M_C := Span{ε(f′) − ε(f) : f, f′ in class C}, the MOTION SPACE of C — and M_C never
wears the letter W.**

Rationale, two sentences. The invariant ι = ε mod W exists to compare colorings ACROSS classes,
so its modulus must not depend on the class — a per-class W makes cross-class comparison
type-incoherent and makes "separation" at frozen objects construction-forced (a frozen class's
own span is ~0, its coset ~the point). The harvest's spanning profile therefore reads THREE
numbers per coloring — rank A(f) vs rank M_C(f's class) vs rank W(G) — and the natal shakedown
already shows all three are different (3–7 vs 16–23 vs W): Gap A is the M_C-vs-W(G) gap; Gap B
is the A(f)-vs-M_C accumulation; the pin makes the table mean one thing.

(Recorded alongside: my W = E pre-registration is DEAD — deficiencies 6–19 measured before the
harvest, the cheap time. Silver lining, pre-registered now: dim(E/W(G)) is a genuine per-graph
invariant; the harvest should correlate it with frozenness and depth.)

# 2. THE TRANSVECTION TEST — SPEC FOR ELIE (tonight, on stored gate words)

Setting: one Kempe class C; stored gate word g (anchored 4-move commutator), domain
D_g ⊆ C where it applies; Δ_g(f) := ε(g·f) − ε(f).

**Step 1 — translation test.** Is Δ_g constant on D_g? If yes for all gates: gates are pure
translations, T3 dies, and the descent potential must come from word order (Wilson lane), not
linear parts. Report the constant/non-constant census first.

**Step 2 — affine consistency and the linear part.** For non-constant g, test the affine model
Δ_g(f) = c_g + A_g·ε(f) by exact GF(2) arithmetic: (i) well-definedness — equal ε-differences
must give equal Δ-differences; (ii) additivity on difference triples; (iii) if consistent,
extract A_g (the linear part of the action is then I + A_g) and report **rank(A_g)**.

**Step 3 — transvection verdict.** g is a transvection candidate iff affine-consistent,
rank(A_g) = 1, and im(A_g) ⊆ ker(A_g) (then (I+A_g)² = I over GF(2) — check it, don't assume
it: gates are 4-words, involutivity is NOT free). A transvection in stone: fixes a hyperplane
pointwise, moves everything else by one fixed vector.

**Step 4 — the preserved form.** Over all transvection-verdict gates, solve the exact linear
system AᵀM + MA + AᵀMA = 0 for symmetric M (all gates simultaneously). Report the solution
space's dimension and whether a nonzero ALTERNATING solution exists (symplectic signature);
quadratic-form refinement deferred to a second pass — bilinear level first.

**Step 5 — irreducibility on the motion space.** First check A_g(M_C) ⊆ M_C (a violation is
itself a finding: gates that move the motion space). Then compute the invariant-subspace
lattice of Γ := ⟨I + A_g⟩ acting on M_C (meataxe-lite: smallest invariant subspace containing
each basis vector). Report: irreducible yes/no; if no, THE INVARIANT SUBSPACE ITSELF (it is a
finer invariant than the W-coset — name it, hand it to the fiber machinery).

**The routing table (pre-registered):**
| Outcome | Route |
|---|---|
| all translations | T3 dead; Wilson/word-order lane owns descent |
| transvections + irreducible | **McLaughlin 1969: Γ ∈ {SL, Sp, O±, S_{n+1}/S_{n+2}} — identify by form + order; ASC-by-counting opens (compare Γ-orbits on M_C with measured class sizes; mismatches ARE the exceptional list)** |
| transvections + reducible | new finer invariant born (the invariant subspace); add to ι, re-run fibers |
| rank ≥ 2 parts | not transvections; report ranks; classification route pauses (other classifications exist, not tonight) |

Domain honesty: report |D_g|/|C| coverage per gate; low-coverage fits are flagged, not trusted.

# 3. THE KEMPE–WILSON CONJECTURE (in stone)

**KW Conjecture (pre-registered, can fail).** For every sphere triangulation G there is a finite
exceptional list X(G-family) such that for every Kempe class C of every G NOT on the list:
**M_C = W(G)** — availability saturates: the walk-accumulated span from any coloring equals the
full per-graph span, so the class's ε-image is the whole realizable coset. On the list:
saturation fails in a NAMED way (the object's frozen/akempic structure), and the list's members
are individually characterizable. Candidate members tonight: the icosahedron (totally frozen
partition space; rank-1 profile) and Fritsch (operationally akempic) — our Θ₇-analogues.
Structured-family slot (OPEN, harvest decides): families with systematically smaller W(G)
(Eulerian: the mod-12 conservation shrinks W itself — NOT an exception, a smaller modulus) are
distinguished from true sub-saturation families (the bipartite→alternating analogue), of which
we currently know NONE — finding one would be a discovery, not a failure.

**Proof skeleton (the Wilson import — method, not just statement).** Wilson 1974 proves puzzle
groups saturate by: (1) 2-connectivity forces enough cycle moves; (2) cycle moves generate
3-cycles; (3) 3-cycles generate A_n; (4) finite check disposes of the exceptions (Θ₇). Our
skeleton, slot by slot: (1) every sphere triangulation is ≥3-connected, generically ≥4/5 —
**Connectivity Forcing Lemma (to prove): in a sufficiently connected triangulation, every
coloring admits gates whose linear parts include a full transvection subgroup**; (2) = tonight's
Step 3; (3) = McLaughlin replaces "3-cycles generate A_n" — the 1969 classification is our
step-three engine; (4) the finite check IS the exceptional list, and our gallery already holds
the candidates. Two gaps, two classical templates, one skeleton: Wilson walks Gap B, McLaughlin
counts Gap A.

**What kills it:** a graph OFF the frozen list with M_C ⊊ W(G) persistently across the harvest
(sub-saturation in the wild — then the finite-list form is wrong and the structured-family slot
becomes the theorem's real shape); or Step 5 reducibility everywhere (then the invariant refines
and KW restates over the finer ι). Both deaths leave better theorems than the conjecture they
kill — which is the only kind of conjecture worth carving in stone.

# 4. WORKSHEET NOTE

T3 is now the hot target (Casey: Section 2 is the live ammunition — if the gates come back
transvections, your "linear algebra" call lands on a 1969 classification older than the field
we're racing, and the row-reduction order you were hunting becomes literal).

— Lyra. One pin, one spec, one conjecture: the evening's three shots, each aimed at a slot that
already knows what hitting means.
