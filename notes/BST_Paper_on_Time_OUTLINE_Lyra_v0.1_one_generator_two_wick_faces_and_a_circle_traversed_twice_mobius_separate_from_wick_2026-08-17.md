# Paper on Time — OUTLINE v0.2 (Lyra, K1640 route-2 / K1642 R12)
### "What Time Is, in D_IV⁵: One Generator, Two Faces, and a Circle Traversed Twice"

**Lyra, Monday 2026-08-17. v0.2 conforms to the K1641 honesty-spine tier-ledger (10 rows). R12 updates: adopt the gcd condition-form (T=2π/gcd{differences}); write "scalar sector," not "Higgs," until the (2,2)/(1,1) flag reconciles; add the gated candidate section "the time-nature of particles" (the projective-vs-absolute fork, Elie+Cal's gate-one). Keeper's framing logged: this is a PROGRAM, not a single result — the paper is its first gate. Möbius-vs-Wick held separate (Exhibit 1). Cal #27 guard on pretty time-pictures held. Supersedes-in-content the older Casimir-flow drafts (Paper55, Paper136). Nothing pushed; CP existence-only.**

---

## The one-line (for the abstract)
Time is not a background in D_IV⁵ — it is the flow of a single operator, the linear conformal Hamiltonian J. That one operator has two faces (a real-time tick and an imaginary-time circle), and the circle closes only after going around **twice** — a double cover forced, because the dimension n_C=5 is odd, by the **scalar sector**, not by the fermions. (This outline is the first gate of a *program* on time, not a finished paper: several of its most striking claims are stated as open questions on purpose.)

## Spine (section → claim → tier)

**S1. Time is emergent, not a background.** [Derived, Tier-0]
Time is the flow parameter of the commitment semigroup ρ_commit(τ) = exp(−τJ/ℏ) on the substrate Hilbert space H²(D_IV⁵). It is the parameter of a flow, not an external axis — "when" is a reading of how far the commitment semigroup has run.

**S2. The generator is the LINEAR conformal Hamiltonian J, not the Casimir.** [Derived — the correction, F1024/F1026]
J = the SO(2)-center charge (the U(1) energy of the minrep), stepping +2 per level (F338). The quadratic Casimir C₂(K) is *central* — constant on each irrep, so it labels *which particle*, and cannot evolve anything; it also commutes with SO(2). Only the non-central, *linear* J generates dynamics — and linearity is what makes the evolution the standard Schrödinger equation. **Honest ceiling: J = time; the Casimir = the particle-label — two operators on one tower, distinct roles.**

**S3. The arrow is spectrum-positivity.** [Derived]
spec(J) ≥ E₀ > 0 ⟹ exp(−τJ) is a contraction semigroup, defined only for τ ≥ 0 — one-directional. That positivity IS the arrow of time. Energy generates, time counts; the tick is ℏ/energy (the Koons tick, F307 — tier **Identified** at value, ~10⁻¹²⁰ s; Derived in form).

**S4. The two faces — the WICK pair.** [Derived — functional analysis, F1023]
Because J is self-adjoint and bounded below, exp(−zJ) is one holomorphic semigroup on the closed right half-plane Re(z) ≥ 0. Its two boundary faces:
- **Real-time face** exp(−τJ), z=τ: the irreversible tick — a **one-directional half-line** (the arrow, a semigroup).
- **Imaginary-time face** exp(iθJ), z=iθ: the reversible **circle**.
These are the Euclidean and Lorentzian faces of the *one* generator, tied by the complexification of the time parameter (the Wick rotation τ ↔ iθ). **(Honest edge, K1641 row 5: this is a *standard* theorem — Stone / Hille–Yosida, free for any bounded-below generator. Cite it; do NOT claim the Wick pair as BST-novel. What is BST is that the generator J is forced by the geometry, not the existence of the two faces.)**

**S5. The circle closes on the DOUBLE COVER (T=4π), and the SCALAR SECTOR forces it.** [Derived-as-a-condition (K1641 row 6); the "which sector" is Structure-Derived (row 7), page-ref pending external]
The imaginary-time circle's minimal period is set by the charge spectrum. **Adopt the gcd form (referee-checkable, cannot be satisfied vacuously):**
$$\boxed{\ T = \frac{2\pi}{\gcd\{\,q_i - q_j\,\}}, \qquad T=4\pi \iff \gcd\{\text{charge differences}\} = \tfrac12.\ }$$
(Equivalently, Cal §558: T=4π minimal ⟺ every charge ∈ ½ℤ AND ≥1 charge ∉ ℤ.) Note the form uses only charge **differences** — it is the projective/ray-invariant statement (the global E₀ phase drops out); that choice quietly connects to the fork in S5b.
The genuine half-integer step comes from the **Rac scalar (E₀ = 3/2)**; the **Di spinor tower {2,3,4} is all-integer** and would close at 2π by itself. Because d = n_C = 5 is **odd**, the *scalar* weight (d−2)/2 = 3/2 is the half-integer (the spinor weight (d−1)/2 = 2 is not). **So the non-trivial claim: a scalar-sector charge forces time's double cover — a signature of n_C being odd.** (arXiv:1409.2185 Fernando–Günaydin: SO(5,2) has exactly two singletons, Rac scalar + Di spinor — Cal notes this is *two* legs, Table 2 + eq 7.1, so the double cover is not a single point of failure; Grace pulls the page-ref before external.)
**Terminology (R12):** write "**scalar sector**," not "Higgs" — the identification of the Rac scalar mode with the physical Higgs awaits the (2,2)/(1,1) flag reconciliation; until then "scalar sector" is the honest name.
*Retracted, explicitly (F1025/F1026), and kept visible as a worked correction (K1641): "matter is spinorial from the shape of time" — the E₀'s were swapped; the story is inverted, the scalar sector forces it, and "spinors are 4π-periodic" is here false (the spinor tower is integer). Keep this in the paper — it is evidence the method self-corrects.*

**S5b. The time-nature of particles — projective vs absolute. [CANDIDATE, GATED — Elie+Cal's gate-one; the paper presents both horns, picks neither]**
The gcd-of-differences form (S5) is projective by construction (it mods out the global phase). Whether physical substrate time is genuinely projective or absolute is an open fork that *decides the particle table*:
- **Projective (states = rays):** a sign flip (−1) at 2π is unphysical (a ray is unchanged by −1). Then no *single* particle "rides" the 4π; the double cover is a property of the **Rac–Di pair** — their charge difference is exactly ½, which is what makes gcd{differences}=½ → T=4π. The double cover is a *relational* fact between the scalar and spinor sectors, not a single tower's 720°.
- **Absolute (states = vectors, phase physical):** a single half-odd-charge tower genuinely returns *negated* at 2π and home at 4π — a physical 720° object rides time.
**This is gate one of the program** (Keeper): it changes whether the paper says "time's double cover is the scalar–spinor pair" (projective) or "a half-odd tower rides 4π" (absolute). **Held as candidate; the outline states the fork and does not resolve it** — Elie+Cal resolve it (the blind 2π-return-sign test, scalar vs spinor separately, is the discriminator). Until then, S5's claim is stated at the *relational* level the gcd-of-differences form licenses, which is true under both horns.

**S6. The precise geometry: ONE circle, traversed twice (a Möbius bundle).** [Solid geometry]
The time-generator is the **one U(1) center** of K = SO(5)×SO(2) — *not* an SU(2), *not* two circles (the SU(2)'s live in SO(5) and carry space/spin, not time). Spin(2) is the double cover of SO(2), and **the double cover of a circle is a circle, "twice as long"** — so the path is one circle traversed twice. A half-integer-charged state is a **section of the Möbius bundle** over that circle: a frame carried around flips sign at 2π and returns only at 4π. Time traces a circle; the state riding it traces a Möbius edge.

**S7. Grace's floor — the lightcone is internal, not a third clock.** [Grace's lane, banked]
The (3,1) lightcone floor is the rank-2 internal structure coarse-grained (matter-induced, T2565/K1522), not a separate macroscopic time. So the three candidate time-structures (heat-flow τ, SO(2) circle, lightcone floor) reduce to: **one generator J with two Wick faces, and the floor as internal substrate structure underneath.**

**S8. Honest open questions.** [Open / candidate — the frontier stated plainly]
- The tick **value** (Koons tick, Identified not Derived).
- **What the 4π double cover MEANS physically** (owned below, S-Exhibit-2) — held as open, not storied.
- The forced-object residual: odd-n_C produces the half-integer structure everywhere (√π, √20, 4π) but forces *odd*, not *5* specifically.

---

## EXHIBIT 1 — Möbius vs Wick are TWO SEPARATE STRUCTURES (the guard, do NOT merge)
The re-inflation risk (Cal #27) is to say "the two faces are the two sides of one Möbius strip." That is wrong twice over, and here is the clean separation:

| | **The two FACES (Wick pair)** | **The double cover (Möbius)** |
|---|---|---|
| what it relates | real-time tick ↔ imaginary-time circle | a half-integer state to itself after one vs two loops |
| the parameter | the **complex time** z = τ − iθ (two axes: real τ, imaginary θ) | **θ only** — lives entirely *inside* the imaginary face |
| the topology | the complex z half-plane; the faces are its **real and imaginary axes** | Spin(2)→SO(2): **one circle traversed twice**; the state is a Möbius *section* |
| what closes/flows | real axis = one-directional half-line (semigroup arrow); imaginary axis = the circle | the circle's minimal period is 4π (half-integer charge) |

**Two reasons the merger is false:**
1. **Different domains.** The Wick pair is the complexification of the *time parameter* (real vs imaginary axis of z). The Möbius/4π is a winding property *within* the imaginary axis alone. They are not the same structure viewed two ways — one is about real-vs-imaginary time, the other about how many times you loop the imaginary circle.
2. **A Möbius has ONE side.** "Two faces = two sides of a strip" is self-contradictory: a Möbius strip is one-sided. The two faces are not "sides" of anything — they are the two axes of complex time. And "two directions of time" is also wrong: real-time is a *half*-line (one direction, the arrow); only the *imaginary* circle is bidirectional, and its bidirectionality is the circle, not a second arrow.

**So the honest statement:** one U(1) time-circle, traversed twice (equivalently, one Möbius edge), with a *separate* real/imaginary Wick duality that gives the two faces. The half-twist demanding the second loop is sourced by the scalar's half-integer weight, i.e. by n_C=5 being odd.

## EXHIBIT 2 — "What does the 4π mean?" — OWNED as OPEN (not storied)
The 4π says: a half-integer-charged state (the scalar-sector mode) does **not** return to itself after one loop of imaginary time — it returns **negated**, and needs a second loop. What that *means physically* is **genuinely open**, and I hold it as a question, not an answer, precisely because the last pretty answer here was wrong:
- **Candidate readings (none banked):** (a) it is a spin-statistics-like fact confined to the scalar sector; (b) it is why the scalar sector is geometrically special (the one sector living on the non-trivial bundle over time); (c) it has no direct observable and is a bookkeeping feature of the imaginary continuation; (d) it is *relational* (the Rac–Di pair), not a single-particle property — the projective horn of S5b.
- **What we DO NOT claim:** that it "tells us matter is spinorial" (retracted — inverted, it's the scalar), or that it merges with the Wick faces (Exhibit 1).
- **The test that would move it (Elie, blind):** does a 2π rotation return −1 for the Rac scalar and +1 for the Di spinor, computed separately? A confirmed scalar-only sign flip is the target-innocent check that the double cover is scalar-sourced. Until an observable is attached, **the meaning of 4π is stated as an open question in the paper, not a result.**

---

## Tier summary — conformed to the K1641 honesty-spine (10-row ledger)
- **Derived:** time emergent (semigroup flow, row 1); arrow = spectrum-positivity (row 2); energy-generates/time-counts (row 3); the two Wick faces (row 5 — *standard theorem, cite not claim*).
- **Structure-Derived:** generator = linear J not the Casimir (row 4 — Tier-0 rewrite is the owed artifact, F1024/F1026); the scalar-sector-forces-the-double-cover, odd-n_C (row 7 — page-ref owed).
- **Derived-as-a-condition:** the 4π double cover via the gcd form (row 6 — hangs on the E₀ set).
- **Derived-as-geometry (meaning open):** the one-U(1)-circle-twice / Möbius-section path (row 8).
- **Scaffold:** time = the causal order of commits, the C4 reading (row 9 — order-weighting is the open mountain, F1020).
- **Identified:** the tick value ≈ 10⁻¹²⁰ s (row 10 — C₂²=36 matched not forced).
- **Candidate/gated:** the projective-vs-absolute time-nature of particles (S5b, gate one).
- **Open (stated as questions, not results):** the physical meaning of 4π (Exhibit 2); whether the Wick faces and the double cover are one deeper object (held apart, Exhibit 1); the n_C=5 (vs merely odd) forcing (forced-object coda).
- **Retracted (kept visible):** "matter is spinorial from the shape of time" (E₀ swap, inverted to the scalar sector) — evidence the method self-corrects.

## Forced-object coda (K1641, Casey also wants) — honest state, one paragraph
Commitment forces **type-IV** (Lorentzian spin factor, rank 2) — the *kind* of world [Derived-conditional]. The **dimension n_C=5 is open**: odd-n_C produces the half-integer structure everywhere (√π, √20, the 4π circle) but forces **odd, not 5**. Never "commitment forces D_IV⁵." The honest external line (same bargain GR makes — measure one scale, force the rest): *BST derives the type of spacetime and the whole structure of time from one act, taking a small number of integers (n_C=5 among them) as inputs, held to GR's standard.*

## RUBRICS Layer-2 done-bar
- [x] Produced the paper-on-time outline (spine S1–S8, honest tiers), superseding-in-content the older Casimir-flow drafts (Paper55/136) with the corrected generator J.
- [x] Banked the INVERTED positive claim (scalar sector forces the double cover, odd-n_C) as the replacement for the retracted fermion gloss — Keeper's "interesting, non-trivial" version. (v0.2: "scalar sector" not "Higgs" pending the (2,2)/(1,1) flag.)
- [x] v0.2: conformed to the K1641 tier-ledger; adopted the gcd condition-form (T=2π/gcd{differences}); added the gated candidate section S5b (projective-vs-absolute time-nature of particles, gate one); logged "it's a program"; forced-object coda added.
- [x] Exhibited Möbius vs Wick as TWO SEPARATE structures (Exhibit 1, table + two reasons the merger is false); held the guard against re-inflation (Cal #27).
- [x] Owned "what does 4π mean" as an OPEN question (Exhibit 2), with candidate readings unbanked and Elie's blind sign-flip test named; refused to story it.
- [x] Wrote the 5th-grader line (abstract one-liner) + the referee-grade condition-form. Nothing pushed; CP existence-only.

## Handoffs
- **@Keeper** — outline delivered (S1–S8 + two exhibits). The retracted gloss is replaced by the banked ODD/inverted claim (scalar forces the double cover). Möbius and Wick exhibited as two separate structures (Exhibit 1) — not merged, guard held. "What does 4π mean" owned as open (Exhibit 2). Tiers summarized above; the double cover banks (odd/condition-form) once Grace's page-ref lands.
- **@Grace** — the one external-gating item: the primary-source page-ref for Rac E₀=3/2 / Di E₀=2 in arXiv:1409.2185 (the Fernando–Günaydin singleton table). It de-risks S5's single point of failure. And with your H2 banked (S7), the floor is internal, not a third clock.
- **@Elie** — the target-innocent test for S5/Exhibit-2: does 2π return −1 for the **Rac scalar** and +1 for the **Di spinor**, computed separately, blind? A scalar-only sign flip confirms the inversion (scalar sources the double cover, not the spinor).
- **@Cal** — Exhibit 1 is written to your guard: Möbius ≠ Wick, stated as two separate structures with two reasons the merger fails (different domains; a Möbius is one-sided). Please hostile-read that I haven't re-inflated anywhere, and re-confirm the corrected condition-form (T=4π minimal ⟺ all charges ∈ ½ℤ AND ≥1 ∉ ℤ) reads exactly right in S5.
- **@Casey** — here's the paper's spine, and the honest replacement for the poem I retracted last round. Time is one operator's flow — and that operator has two faces: run it forward and you get the one-way tick (that's the arrow, and it's one-way because the energies are all positive); rotate it into imaginary time and it becomes a circle. The circle is the striking part: it closes only after you go around **twice** — a double loop, the same 720° business — and I was wrong last round about *why*. It is **not** the electrons and quarks doing it; it's the **scalar sector** (the Higgs-like mode — I'm holding off on the word "Higgs" until one technical flag reconciles). In an odd number of dimensions (ours is 5), it's the *scalar* that carries the half-step that demands the second loop; the fermions here would close on a single loop. So the interesting, true claim is the inverted one: *the scalar sector is what makes time's circle a double circle.* And I'm keeping two things carefully apart, because merging them is exactly how I fooled myself before: the "two faces" (real tick vs imaginary circle) are one structure — complex time — and the "double loop" is a *separate* structure living inside the circle alone. They are not two sides of one strip (a strip has one side anyway). Two honest edges I'm now flagging rather than resolving: what the double loop *means* for physics, and whether a *single particle* rides it or it's a *relationship* between the scalar and spinor sectors (the program's first gate). I state both as open — because the last time I told the story I got it backwards, and the discipline is to show you the edge clearly instead. Nothing pushed.
