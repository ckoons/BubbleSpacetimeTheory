---
title: "J1 & J2 — THE ATTACK: the four-stage chain algebra, the Confinement Lemma (proved), the net-support identity, the conveyor as the sole escape route (its cases enumerated), and J2 re-formulated as sweep-aiming — a working document, honestly midway, with Elie's trace requests attached"
author: "Lyra"
date: "2026-09-01, Tuesday (clock-verified 09:23 EDT at round start; working through the morning)"
status: "WORKING DOCUMENT — the joints under active attack. Proved pieces marked PROVED; open cases enumerated, not waved; Elie's stored gate traces are the decisive data for the case census. Nothing banks; the Candidate Assembly's labels stand until this document closes them."
---

# THE ATTACK ON J1 AND J2

## 0. Apparatus (the stage algebra, pinned)

Gate word at the canonical context: c₀ →α→ c₁ →β→ c₂ →α→ c₃ →β→ c₄, where α anchors the
(r,s_M)-pair at n_sM and β anchors the (s_M,s_i)-pair at n_si. The four ACTING CHAINS:
X₁ = the (r,s_M)-chain of n_sM in c₀ (= M, forced ⊇ {B₁, n_sM, B₂});
X₂ = the (s_M,s_i)-chain of n_si in c₁;
X₃ = the (r,s_M)-chain of n_sM in c₂;
X₄ = the (s_M,s_i)-chain of n_si in c₃.

**Net-support identity (immediate).** A vertex's color is finally changed iff it is toggled an
odd number of times per pair: **net support = (X₁ △ X₃) ∪ (X₂ △ X₄).** J1 (patch-locality) is
exactly: both symmetric differences lie in a bounded patch at the anchor. (In height
coordinates, by Prop CS the net displacement is T₁·(±1_{X₁} ∓ 1_{X₃}) + T₂·(±1_{X₂} ∓ 1_{X₄}) —
the same statement, ℤ²-graded.)

## 1. The Confinement Lemma — PROVED (the structural reason the analysis is bounded)

**Lemma C1.** X₂ ∩ X₁ ⊆ ρ(X₁) := the OLD-r vertices of X₁. In words: after move 1, every
old-s_M vertex of M carries color r and is invisible to the (s_M,s_i)-subgraph; the second
chain can enter the first only through the first's old-r territory (which move 1 turned s_M).
*Proof.* X₂ lives in c₁'s (s_M,s_i)-subgraph. X₁'s vertices in c₁ carry swapped colors: old-r
→ s_M (visible), old-s_M → r (invisible). ∎

**Corollary C1a.** The far reaches of M's s_M-side — however large M is — are untouched by
move 2, hence present unchanged in c₂'s (r,s_M)-subgraph (as r-vertices... as follows: they
are r in c₁ and X₂ does not touch them, so r in c₂), and reconnect to n_sM in X₃ wherever
their c₀-connectivity within M survives the excisions of C2 below. The candidate instability
is CONFINED to ρ(X₁) and X₂'s accretions — never to M's bulk.

**Symmetrically (Lemma C1′):** X₃ ∩ X₂ ⊆ the old-s_i vertices of X₂ (move 2 turned them s_M;
X₂'s old-s_M vertices are s_i in c₂, invisible to the (r,s_M)-subgraph).

## 2. The excision/accretion bookkeeping (derived; the conveyor identified)

From C1/C1′, tracking membership across stages:
- **Excisions from the M-line:** X₃ = X₁ minus the vertices X₂ flipped out of the {r,s_M}
  world — precisely X₂ ∩ X₁ ⊆ ρ(X₁) (they went s_M → s_i at move 2) — plus accretions:
  X₂'s old-s_i vertices (now s_M) where adjacent to the surviving component of n_sM.
- **The conveyor:** a vertex handed along pairs — e.g., old-s_i, flipped s_i → s_M (move 2),
  then s_M → r (move 3, if in X₃) — ends with net color change and net height shift T₁ + T₂:
  it IS in the net support. The conveyor is the ONLY way net support grows beyond the anchor
  region: every non-conveyor vertex is either toggled twice in one pair (net zero) or never.
- **J1 restated exactly:** the conveyor terminates within a bounded patch in the canonical
  context. The measured signature agrees (dominant support three; patches ≤ 7 sites; the D1
  (2,2,4,4,6,6,6) height values are conveyor coverage-counts). What remains is to PROVE the
  termination, and the enumeration below is the whole space in which it could fail.

## 3. The case census for conveyor termination (enumerated; Elie's traces decide the empty ones)

The conveyor extends beyond the anchor patch only if, at some stage, an accreted vertex chain
of the current acting pair reaches outside the previous stage's flip zone. In the canonical
context the entry points are constrained by the forced partitions:
- **Case (a) — the link route:** X₂ enters X₁ via the forced link edge (B₂, n_si). Bounded by
  construction: the entry is AT the link; the flip zone is the B₂-side of ρ(X₁) adjacent to
  the patch. [The Lab-1 geometry; the proved single-cut sub-case lives here.]
- **Case (b) — the deep-ρ route:** X₂ reaches old-r vertices of X₁ far from the link, through
  an (s_M,s_i)-path in c₁ avoiding the patch. Then X₃ excises them; whether X₄ RETURNS them
  (re-flipping to close the toggle count) is the termination question for this case. TARGET
  LEMMA (b): in the canonical context, every deep-ρ excision is X₄-returned. Candidate
  mechanism: X₄ is the (s_M,s_i)-chain of n_si in c₃, and the deep excised vertices are s_i in
  c₃ (from move 2) sitting where X₂ ran — X₄ retraces X₂ through them unless move 3 cut the
  path; move 3 cuts only within X₃ ⊆ {r,s_M}-world, and X₂'s path through deep-ρ is
  s_i/s_M-colored in c₃ with its s_M links flipped to r exactly on X₃... the cut/retrace
  dichotomy is decidable per instance and is THE case (b) content.
- **Case (c) — the accretion route:** X₃ accretes X₂'s old-s_i vertices and move 3 flips them
  to r; X₄ cannot see them (r ∉ {s_M,s_i}); they are net-changed. Bounded iff X₃'s accretion
  from X₂ is bounded. TARGET LEMMA (c): X₃ ∩ (X₂'s old-s_i) ⊆ the patch — candidate mechanism:
  such a vertex needs an (r,s_M)-path in c₂ to n_sM; its c₂-neighbors inside X₂ are s_i or its
  own kind; the exit into the {r,s_M} world happens at X₂'s boundary, which meets n_sM's
  component only near the anchor (the forced partitions put n_sM's c₂-color r with its
  immediate link neighbors B₁, B₂ flipped s_M — the reconnection geometry is link-local).
  Decidable; enumerable.

**Elie — the trace requests (the case census made empirical in one pass over stored gates):**
for each stored gate instance: extract X₁..X₄; report |X₂ ∩ X₁| and its distance-from-anchor
profile (case-b incidence); |X₃ ∩ X₂-old-s_i| and profile (case-c); whether every deep-ρ
excision was X₄-returned (case-b termination, per instance); and the conveyor length
distribution. Pre-registered: case (a) dominant; cases (b)/(c) rare or patch-confined; ANY
instance with an unreturned deep excision or unbounded accretion is the counterexample shape —
report it whole, not summarized.

## 4. J2 — the one clause, re-formulated as SWEEP-AIMING (attack in progress)

Wall Transport (banked) says the gate translates walls rigidly. The clause to prove: **the gate
can be AIMED — among the context's symmetric gate options (the i/j mirror pair and anchor
orientation), some choice transports the wall between c and a NEAREST freed target so that the
swept vertices convert disagreements to agreements with none created** — sweep semantics:
d drops by the sweep count ≥ 1. What the forced context gives the aiming argument: the nearest
freed targets differ from c at link-adjacent vertices (a freed coloring changes the link
multiset; the wall to it meets the patch); the gate's patch meets the link BY construction
(anchored at n_sM); the mirror pair gives two transport directions. TARGET LEMMA (J2): for at
least one direction, the transported wall's leading edge lies in the difference region.
Failure shape (named): both directions transport AWAY from every nearest target — which would
contradict the measured universality but must be excluded by argument, not by citation; the
exclusion candidate is parity: the two mirror directions sweep complementary sides of the
patch, and the difference region meets the patch (previous sentence), so one side contains
difference vertices. The gap in that candidate: "meets the patch" needs the freed-set
characterization at the canonical context (which link recolorings free — enumerable: the freed
words adjacent to (0,1,0,2,3) are a finite list; deriving it is the clause's remaining work,
and it is genuinely one page of link arithmetic).

## 4a. THE LINK ARITHMETIC — DONE (J2's remaining page, computed)

The freed words at link-Hamming-1 from the canonical (0,1,0,2,3), under word-properness
(adjacent letters differ on the 5-cycle): exactly SIX legal single-position recolorings exist,
and they split perfectly:
- **Four FREE a color** — all at SINGLETON positions: p1: 1→2 and 1→3 (recolor the middle;
  frees s_M — the middle has TWO freeing recolorings); p3: 2→1 (frees s_i); p4: 3→1 (frees
  s_j).
- **Two return the canonical shape** — both at BRIDGE positions: p0: 0→2 and p2: 0→3 each give
  a word isomorphic to (0,1,0,2,3).

**Structure sentence: every legal single recoloring of a singleton link vertex frees a color;
every legal single recoloring of a bridge copy returns the canonical shape.** Consistency
check that doubles as a lemma: at a stuck configuration NONE of the four freeing recolorings
is directly performable (each would be a legal singleton swap freeing a color — contradicting
stuckness); so every nearest freed target differs from c at a singleton link vertex PLUS its
blockers — the difference region provably meets the gate's patch (anchored at n_sM, itself a
freeing position with two exits). J2's aiming argument now needs only the gate's net patch
FORM — which is J1's output. The joints have converged into one remaining question.

## 5a. KEEPER'S THREE ABSORPTIONS (F1–F3, absorbed — the target restated)

1. **The claim is SIZE-bounded (|net support| ≤ 8), not radius-2** — F1's 56 radius failures
   found the true shape (radius tracks surgery depth). Section 3's radius language is hereby
   retargeted to the size bound.
2. **The argument must be UNIFORM, not a case ladder** — F2: single-cut is 18% of realized
   overlaps (sizes to 19), and depth does not drive radius. Section 3's cases (a)/(b)/(c) are
   DEMOTED to diagnostics; the theorem-shaped target is a uniform size bound on
   (X₁△X₃) ∪ (X₂△X₄). Uniform candidates, in order: (i) the pure-curl + alphabet route (net
   effects are gauge-triples — measured; a derivation of the alphabet collapse for this
   template would give the bound at once); (ii) a counting/parity argument on the four-chain
   overlap structure via Confinement (the flip zones nest: X₂'s damage to X₁ is exactly what
   X₃ excises, and X₄ retraces X₂ except where X₃ cut it — the uniform statement is that these
   near-cancellations leave a bounded residue, and the D1 coverage counts (2,2,4,4,6,6,6) are
   its fingerprint).
3. **The quantifier is EXISTENCE-form** (some gate descends — F3: 100%/63%): the derivation
   targets "some choice of mirror/anchor descends," never "every gate descends." Already the
   attack's form; now pinned by data.

## 6. LEMMA (b) RETIRED — J1′ INSTALLED (per Toy 5568; the census ruled)

Target Lemma (b) — deep-ρ return — is RETIRED: 3,917 of 4,441 deep excisions are unreturned
(88%); the retrace mechanism is the exception. The fixed anchored word is patch-local neither
in color support (max-distance to 6) nor always in charge mod gauge (104/720 exceed 8). What
replaces it: **J1′ (choice-quantified patch-locality): at every stuck configuration, SOME
member of the finite word family 𝒜 has net support of size ≤ C** — measured standing: 100% at
size ≤ 8 for the chosen word (F1); the same existence phenomenon as F3's descent quantifier.
Case (a) remains covering 540/1,644 outright; case (c) nearly confined (6 far instances). The
free controls stand: Confinement and Net-Support verified exact, 1,644/1,644 each.

## 7. THE UNIFORM BOUND — the derivation opened at its crux (working; the constant refused)

**Non-inheritance rule, first:** C is NOT 8-because-measured. C must fall out of the stage
algebra or the claim keeps its label. Cal's rider stands: if the derivation yields C′ ≥ 8, the
claim is size ≤ C′ and the measurement is slack, and that is fine and said so.

**The crux, identified — the DISCONNECTION DICHOTOMY.** From the bookkeeping: X₁ △ X₃ consists
of (i) the excision X₁ ∩ X₂ ⊆ ρ(X₁) (Confinement), (ii) accretions, and (iii) **the stranded
remnant: parts of X₁ disconnected from n_sM by the excision.** (iii) is the unbounded piece —
5568's deep support is stranded-remnant territory. The dichotomy per choice w ∈ 𝒜:
- **No stranding:** X₃ recovers X₁ up to the flip zones; net support ⊆ patch; size bounded by
  the patch combinatorics of the canonical context — the derivation target for C is exactly
  this count (anchor star + the two forced link-edge flip zones; to be COUNTED from the stage
  algebra, not asserted).
- **Stranding:** the remnant R undergoes the full pair transposition (r↔s_M applied once,
  never undone — moves 2/4 cannot see it, Confinement) — i.e., the word acts on R as a PURE
  RELABEL. Candidate absorption: a relabel of a component is gauge-equivalent to a bounded
  change when R is co-bounded (the J3 collapse mechanism — "complement-of-one ≡ single-vertex
  mod gauge"); the 104/720 exceptions are precisely where R is neither bounded nor co-bounded.
  **The choice clause's derivational content, conjectured exactly: for at least one w ∈ 𝒜 the
  stranded remnant is bounded or co-bounded** — the mirror choice strands on the i-side or the
  j-side, and the two sides cannot both be middle-sized... that last clause is the open step,
  stated so it can be attacked or killed (Elie: per trace, report the i-choice and j-choice
  remnant sizes as a PAIR — the conjecture dies on one trace where both remnants are
  middle-sized, i.e., both > C and < |V| − C).

**Standing after the crux:** the derivation is one exclusion argument wide (the two-sided
middle-remnant exclusion), with its kill condition on a one-pass pair census. The constant C
is a patch count owed from the no-stranding branch. Both are named; neither is inherited.

## 5. Standing at midday

PROVED today: the net-support identity; Confinement (C1, C1′); the excision/accretion
bookkeeping; the reduction of J1 to conveyor termination with the case space enumerated (a
proved; b, c targeted with mechanisms named); the reduction of J2 to sweep-aiming with the
finite freed-word list as its remaining arithmetic. NOT yet proved: cases (b), (c); the aiming
parity. The joints are smaller than they were this morning and their exact shapes are on this
page; Elie's one-pass trace census picks which target lemma falls first.

— Lyra. Keeper said they were smaller than they look; he was right — J1 is a conveyor that
must stop and J2 is an aim that must land, and both now have their failure shapes named, which
is the only state from which this program has ever proved anything.
