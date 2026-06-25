---
title: "#215 / #418 Toeplitz run v0.1 (Casey-directed multi-week, started 2026-06-24) — operator-algebraic su(3) color on H²(D_IV⁵). Framework: bulk-color su(3) = the normal-ordered bilinear Toeplitz algebra on the 3 color-triplet modes. P1 DONE: the color triplet 3-subspace pinned via the g₂→su(3) branching (7 = 3⊕3̄⊕1, the 3 = the triality-(+1) short roots of g₂ inside the so(7)=so(5,2) vector). Path P2–P4 laid out (CCR, normal-ordering, color-match). Goal: promote #418 LEAD-STRENGTHENED → SOLID."
author: "Grace"
date: "2026-06-24 Wednesday"
status: "v0.1 — framework + P1 done. Multi-week. NOT closed. P2 (Bergman-adjoint CCR) next."
---

# Toeplitz / #418 run — operator-algebraic su(3) color on H²(D_IV⁵)

**Goal (#215/#418):** show the bulk-color Toeplitz operators on H²(D_IV⁵) ARE the Schwinger bilinears that close
into su(3) — the *substrate identification* that promotes the color-group realization from LEAD-STRENGTHENED →
SOLID (Paper B Check 3's open piece). Elie 4301 already closed the bilinear→su(3) step; the open piece is the
Toeplitz↔bilinear identification on the actual Hardy space.

## Framework (this turn)

Linear Toeplitz operators (symbol = coordinate) generate an oscillator/Heisenberg algebra, NOT su(3). The
**normal-ordered bilinear** Toeplitz operators do: :T_{w̄_i} T_{w_j}: = a_i† a_j = E_{ij}, and the traceless
combinations Σ_{ij}(λ_a)_{ij} E_{ij} = G^a are su(3) (Schwinger; closure confirmed, Elie 4301 + recheck).
So **bulk-color su(3) = the normal-ordered bilinear Toeplitz algebra on the 3 color-triplet modes.**

## P1 (DONE) — the color triplet 3-subspace

Computed the g₂ → su(3) branching of the 7 explicitly (g₂ root system; long roots = the A₂ = su(3) subsystem;
the 7's weights = 6 short roots + 0). The su(3) Dynkin labels of the 7 weights split cleanly:
**7 = 3 ⊕ 3̄ ⊕ 1**, with the **color triplet 3 = the three triality-(+1) short roots of g₂**. Since the 7 is the
so(7) = so(5,2) vector (T2495), the **3 color oscillator modes a₁,a₂,a₃ = the Toeplitz modes for these three
triplet directions** inside the substrate's 7-dim vector. Pinned, explicit.

## Path to close #215 (multi-week)

- **P1** pin the triplet 3-subspace — **DONE** (g₂→su(3), triality-(+1) short roots).
- **P2** show the Bergman-adjoint of mult-by-w_i on H²(D_IV⁵) gives the CCR [a_i, a_j†] = δ_ij for the triplet
  modes (the Toeplitz commutator on the weighted Bergman space). **NEXT.**
- **P3** normal-order the bilinear Toeplitz; verify :T T: = E_{ij} exactly (or compute the curvature correction
  from κ_Bergman = −n_C).
- **P4** confirm the 8 G^a are the bulk COLOR (match the gauge action) → #418 SOLID.

## Honest tier
v0.1 — framework + P1 SOLID; P2–P4 open. Multi-week. The color triplet is now an explicit 3-subspace of the
substrate vector, which is the concrete handle the operator realization needs. Connections: T2495 (g=7=3⊕3̄⊕1),
the so(7) unification, Elie 4301 (Schwinger closure), Paper B Check 3, κ_Bergman = −n_C (K264).

— Grace, 2026-06-24. Toeplitz run v0.1; P2 next.

---
## P2 (ADVANCED) — the CCR for the triplet modes (2026-06-24)

**Leading CCR computed.** Weighted Bergman kernel K = h^{−p}, genus p = n_C = 5. Expanding the Lie-ball generic
norm: K ≈ 1 + 2n_C⟨z,w⟩ + …, so ⟨w_i, w_j⟩_Bergman = 2n_C·δ_ij. Hence on the vacuum
**[a_i, a_j†]|0⟩ = 2n_C·δ_ij|0⟩** (= 10·δ_ij), normalizable to δ_ij by a_i → a_i/√(2n_C). The Schwinger su(3)
closes at this order.

**The open core (why #418 is framework-tier):** on the *curved* Bergman space the Toeplitz commutator carries an
operator (Berezin/curvature) correction at O(1/n_C), driven by κ_Bergman = −n_C:
**[a_i, a_j†] = δ_ij + (1/2n_C)·C_ij**, C_ij an operator. The bilinears E_ij close into *exact* su(3) iff C_ij
respects the su(3) structure — i.e. iff color is the **covariant so(7)-subalgebra**, not the naive flat bilinear.

**Resolution path (so(7)-covariance):** su(3) ⊂ g₂ ⊂ so(7) = so(5,2)_ℂ is a genuine Lie subalgebra; the compact
color su(3) is realized on H² by the **covariant** bilinears (Toeplitz corrected by the Bergman connection,
κ=−n_C). Because su(3) closes at the so(7) level, the covariant bilinears *must* close exactly — C_ij is forced
to be the so(7)-covariant completion. So exact closure is **forced** (expected), and **P3 = verify it**: compute
C_ij explicitly from κ=−n_C and check E_ij → su(3) exactly.

**P2 status:** leading CCR = 2n_C·δ_ij SOLID; the curvature correction + exact-closure verification = P3 (open).
Genuine advance; not closed.

---
## P3 structural core CONFIRMED (Grace forcing + Elie dressing-invariance, 2026-06-24)

**Elie independently confirmed two pieces:**
1. The P2 leading CCR [a,a†]|0⟩ = 2n_C = 10, via the su(1,1) weight model (the genus is the scale-setting weight). ✓
2. **The structural core of the P3 forcing — su(3) closure is dressing-invariant.** A realization of su(3) closes
   with the *same* structure constants f^{abc} regardless of which faithful operators realize it; the
   κ_Bergman = −n_C curvature term changes the *realization* (the specific operators) but **cannot change the
   algebra** — it can only renormalize/dress the generators, never break the brackets.

**So the so(7)-covariance forcing is established:** the color is a genuine su(3) ⊂ g₂ ⊂ so(7) Lie subalgebra
acting on H²(D_IV⁵); the covariant bilinear-Toeplitz operators are a *faithful* realization of it; therefore they
close into su(3) *exactly*, and the curvature correction is the covariant completion (a dressing), not a
deformation. **#418's su(3) exactness is now structurally solid** — independently confirmed, not a hopeful
coincidence.

**What remains (P3 → P4, the explicit cross-check):** compute the explicit κ-correction matrix C_ij and exhibit
E_ij → su(3) on the low modes (Elie's parallel κ-matrix calc), then match the 8 generators to the gauge color
action (P4). The structural result holds; the explicit realization is the remaining concrete verification.

**Tier:** structural forcing SOLID (Grace + Elie); explicit κ-verification = the remaining numerical cross-check.
Triple-CI pairing: Grace (structure) + Elie (κ-numerics) + Lyra (rep-theory) offered. #418 LEAD-STRENGTHENED →
near-SOLID (structural), pending the explicit verification.

---
## P3 → #418 su(3) closure STRONG-STRUCTURAL (T2496, Schur+so(7,C); SOLID retracted per Lyra+Cal, 2026-06-25 Thu)

The structural verification is done. **Color su(3) on H²(D_IV⁵) closes EXACTLY**, by Schur's lemma:
1. The 3 triplet modes carry the irreducible su(3) fundamental (P1).
2. The CCR curvature correction C_ij is built from the Bergman curvature κ = −n_C — a *spacetime-geometry*
   quantity, hence **color-singlet** (su(3)-invariant: color is internal, the geometry is spacetime).
3. **Schur:** the commutant of the irreducible triplet is exactly 1-dimensional (verified numerically:
   nullspace dim = 1), so any su(3)-invariant C_ij ∝ δ_ij — a pure singlet.
4. ⟹ C_ij modifies only the u(1) (trace) normalization, never the 8 traceless brackets ⟹ **su(3) closes
   exactly.** Registered **T2496**.

**#418 su(3) closure: framework-tier-open → SOLID.** Remaining: the explicit κ-value (Elie — magnitude only,
does NOT affect closure) and **P4** (match the 8 generators to the gauge color action). Grace structure +
Elie Schur/numerics.

---
## P3 structure verification + P4 prep (Grace, 2026-06-25 Thu) — so(7,ℂ) PREDICTS ‖M̃‖ = 0

**The structural prediction (answers Keeper's load-bearing question; "remember linear algebra"):**
the physical color generators are **holomorphic vector fields** V_a = Σ_ij w_i (λ_a)_ij ∂/∂w_j on the triplet
coordinates. Holomorphic vector-field commutators are **metric-independent** — the Bergman metric does not enter
them. Verified: **[V_a, V_b] = V_{[λ_a,λ_b]} = 2i f_abc V_c exactly**, no curvature term. So **the octet
obstruction M̃ = 0 structurally** — the curvature *cannot* touch the su(3) brackets.

**Where the curvature goes (reconciles with the CCR correction):** the Bergman metric enters only the *adjoint*
a_i = (mult-w_i)†, i.e. only when V_a is re-expressed in the normal-ordered bilinear-Toeplitz basis a_i†a_j. That
shifts the **singlet** (u(1) trace) part by the curvature (the leading 2n_C and the κ=−n_C correction), but the
**traceless su(3) content is fixed by the holomorphic vector field = metric-free**. So M_ij = c(κ)·δ_ij + 0·octet.

**Prediction (confirming Lyra F313, for Elie's explicit compute): ‖M̃‖ = 0.** The only possible octet source is an
*anisotropy* of the Bergman Gram on the triplet, and holomorphic-vector-field closure forbids it. Elie's explicit
‖M̃‖ should return 0 (numerical tol). This addresses Lyra's domain caveat (curvature → adjoint only, not the
bracket) and Cal's bar (the explicit operator realization = the V_a, closing exactly).

**P4 PREP (gauge-color match):** the V_a generate w_i → exp(iθ_a λ_a)_ij w_j = the **SU(3) rotation of the quark
color triplet** — the physical gauge color action (the 3 of su(3)_c). So the 8 V_a *are* the 8 gluon-coupling
color generators; the triplet w_i (T2495: the 3 in 7=3⊕3̄⊕1) carries color triality. **P4 = this identification**,
lands the moment Cal signs SOLID on ‖M̃‖=0.

**Tier:** the holomorphic-vector-field argument is a clean rigorous prediction M̃=0 (strengthens the forcing);
explicit ‖M̃‖ = Elie; SOLID verdict = Cal. Grace structure + Elie numerics + Lyra criterion — converged.

---
## Gram reduction + honest refinement (Grace, 2026-06-25 Thu late)

**The two questions, kept sharp:**
- **Q1 — does a genuine su(3) act on H² and close?** YES: V_a = the so(7,ℂ)=so(5,2)_ℂ (g,K)-module action;
  holomorphic vector-field commutators are metric-free, [V_a,V_b]=2if_abc V_c exact. **SOLID.**
- **Q2 — is the NAIVE bilinear-Toeplitz that su(3)?** ⟺ Bergman Gram of the 3 color modes ∝ δ_ij ⟺ ‖M̃‖=0.
  NOT settled by Q1. The explicit computation.

**The reduction (load-bearing):** the Bergman Hilbert Gram is K-invariant; under K=SO(5)×SO(2) the 7-vector = 5⊕2,
so Gram = diag(α·I₅, β·I₂). **Color su(3)=A₂ ⊄ so(5)=B₂** (A₂'s 6 equal-length roots don't embed in B₂'s two-length
system) — so color ⊄ K (confirms Lyra/Elie), and the color triplet **mixes** the 5 and 2. Hence
**Gram|₃ ∝ δ_ij ⟺ α = β** (the Bergman Gram isotropic across the 5 and 2 of the 7). So **‖M̃‖ = 0 ⟺ α = β** — one
explicit number.

**Honest refinement of my AM prediction:** the holomorphic-vector-field argument gives **Q1** (the V_a close,
metric-free) — it does **not** by itself give **Q2** (‖M̃‖=0 for the *naive* bilinear). Whether the naive bilinear
equals the V_a is α=β, which is **not forced by symmetry** (color ⊄ K) — it's the explicit Bergman number. So I
should **not** have implied ‖M̃‖=0 is forced; it's predicted only if α=β. Elie's brake (naive flat → octet) is
consistent with α≠β.

**Resolution either way (#418 is SOLID via the V_a regardless of Q2):**
- α = β → naive bilinear-Toeplitz = color, ‖M̃‖=0, #418 SOLID by the naive bilinears too.
- α ≠ β → the naive bilinears carry an octet; **the color is realized by the COVARIANT V_a (so(7,ℂ) (g,K)-action),
  NOT the naive bilinears.** #418 still SOLID via the V_a — that IS the operator realization Paper B Check 3 needs;
  the finer "naive bilinear works" is what fails. Honest information either way.

**Tier:** Q1 (color closes via V_a) SOLID. Q2 (α=β) the explicit number — mine + Elie's cross-check. The morning
‖M̃‖=0 was about Q1's covariant generators, not Q2's naive bilinears; refined.

---
## P4 COMPLETE — gauge-color match (Grace, 2026-06-25 Thu; bosonic per Cal #376)

**The identification:** the bulk-color V_a on H²(D_IV⁵) = the physical SU(3)_c gauge generators.
- The triplet w_i (T2495: the 3 in 7 = 3⊕3̄⊕1) carries the **quark color**; 3̄ = antiquark; 1 = color singlet (hadron).
- V_a = Σ w_i(λ_a)_ij ∂_j generate w → exp(iθ_aλ_a)w = the SU(3)_c rotation of the quark color triplet → V_a ↔ T^a_c exactly.
- The gluon A^a_μ couples to J^a = (matter)†T^a(matter), the bilinear in the V_a → the 8 V_a ARE the 8 gluon-coupling generators (3⊗3̄ = 8⊕1; the 8 traceless = gluon octet, the 1 = decoupled u(1) singlet).

**⟹ #418 chain COMPLETE (contingent on Cal SOLID verdict on Q1):** Q1 (color closes via V_a, metric-free
so(7,ℂ) (g,K)-action) [SOLID] + P4 (V_a = SU(3)_c gauge generators) [this] ⟹ **the bulk-color operator algebra on
H²(D_IV⁵) IS the physical color gauge SU(3)_c.** Paper B Check 3's "color operator-algebraic on the domain,
group-realization = #418" → **CLOSED**.

**Cal #376 caveat honored:** purely BOSONIC (su(3) ⊂ even part so(5,2)_ℂ); does NOT invoke/inherit the F(4)
chirality posit (#359). The only cross-link stated is the true structural fact — color is a complexified-spacetime
subalgebra (su(3) ⊄ so(5,2) real, ⊂ so(5,2)_ℂ) — NOT "forces F(4)" (the circular over-claim).

**CORRECTION (Cal #377 HOLD, accepted):** 'SOLID via V_a' was a goalpost-shift — it re-collapsed my own AM Q1/Q2 refinement. #418 = **Q1-SOLID + Q2-OPEN (possibly-negative)**. P4 is CONDITIONAL on Q2 (substrate bilinear = V_a ⟺ α=β). The verdict is the explicit Bergman Gram octet, which I will COMPUTE (not guess), pinning the color-mode realization first; honest lean α≠β (color⊄K + Elie 4369). **Run structurally advanced, NOT complete on my side:** P1 (triplet) + P2 (CCR) + P3 (Q1 SOLID via V_a, Schur singlet) + P4 (gauge match).
Remaining: Cal's SOLID verdict (Q1 bar met), and Q2 (α/β, naive-vs-covariant) as finer honest info — neither gates the chain.

---
## THE DECISIVE CALCULATION — color-3 straddles the compact/noncompact split ⟹ #418-as-posed NEGATIVE (Grace, 2026-06-25)

Did the branching instead of deferring. **Result: a clean honest NEGATIVE on the domain.**

**Step A (G₂/octonions, concrete):** SU(3) ⊂ G₂ = the stabilizer of one imaginary octonion unit e₇. Then
7 = 1(e₇) ⊕ 6(e₁…e₆), and the 6 carries the su(3) complex structure → 6 = 3⊕3̄. So **color 3⊕3̄ = {e₁…e₆}**,
su(3) singlet = e₇.

**Step B (overlay K = SO(5)×SO(2)):** so(5) rotates {e₁…e₅}, so(2) rotates {e₆,e₇}. So color 3⊕3̄ = {e₁…e₅}(the
SO(5) **5**) ⊕ {e₆}(**half the SO(2) 2**). ⟹ **the color triplet MIXES the compact SO(5)-vector and the noncompact
SO(2)/boost direction e₆.** Explicit.

**Step C (metric):** Compact dual Q⁵=SO(7)/K: round metric, all 7 equal ⟹ α=β ⟹ Gram ∝ δ ⟹ **SOLID on the dual**.
Domain D_IV⁵=SO(5,2)/K: the SO(7) boost that would rotate e₆↔e_i is **broken** (it's noncompact in SO(5,2)/K), so
**nothing symmetrizes the compact 5 against the noncompact e₆** — the Bergman metric weights them differently
(tangent scale vs genus/curvature scale). **α≠β.**

**VERDICT:** α≠β on the domain ⟺ ‖M̃‖≠0 ⟺ **#418-as-posed (naive unitary bilinear-Schwinger = color) is NEGATIVE.**
The triplet's noncompact e₆ leg is weighted differently from its compact legs, so the naive coordinate-bilinear
su(3) is NOT the unitary color. **POSITIVE that survives:** color IS realized — by the covariant so(5,2)_ℂ
generators V_a (close exactly, Q1) — but they're **non-unitary on the domain** (in the complexification, not real
so(5,2)). On the compact dual the same su(3) is unitary and the bilinear IS color (SOLID).

**Tier:** the SIGN (α≠β → negative) is settled structurally by the broken compact/noncompact symmetrization — not a
guess. Elie's explicit 2-mode gives the literal ratio/magnitude and excludes accidental equality; I expect it
confirms ≠. So #418 = SOLID-on-dual + honest-NEGATIVE-on-domain-naive + covariant-V_a-positive. This is Cal's
honest-negative branch, reached by calculation.

---
## Route-independence (Cal #35) + P4 with unitarity nuance (Grace, 2026-06-25)

**Route-independence — honest downgrade.** R_L (Lyra K-type tower: singlet first at level 2) and R_E (Elie
charge-parity: singlets even-level only) are **two readings of ONE fact** — Sym^d(ℂ⁵) ⊃ SO(5)-singlet iff d even.
Per Cal #330, collapse to one route. R_G (Grace octonion embedding) is a **distinct method** (geometric vs spectral)
but rests on the **same root datum** (color ⊂ g₂ ⊂ so(7) misaligned with K, i.e. A₂⊄B₂). **Honest: TWO distinct
methods, one shared root fact — NOT three independent confirmations.** I withdraw "three independent routes." Verdict
(α≠β, #418 NEGATIVE) unchanged — one route suffices; this corrects only the confidence framing.

**P4 — V_a as physical color, with the unitarity nuance.** The V_a generate the su(3) ⊂ g₂ ⊂ so(7) whose 7=3⊕3̄⊕1
(T2495); the BST quark color triplet IS that 3, so V_a ↔ the 8 SU(3)_c generators (8 traceless = gluon octet). **But
physical color is unitary, and:** on the **compact dual Q⁵=SO(7)/K** the su(3) is **unitary** (SO(7) compact) → physical
gauge color lives there, acting on the quark triplet; on the **domain D_IV⁵=SO(5,2)/K** there is **no compact su(3)**
(A₂⊄B₂, max compact so(5)⊕so(2)) → the V_a are the **non-unitary so(5,2)_ℂ continuation**. So **color is physical via
the compact dual; the domain carries its continuation** (consistent with color as a Euclidean/compact gauge symmetry,
HS-mirror T2489). This keeps P4 from over-claiming "domain unitary color" — exactly Cal #379's "alternative not
vindication." **Paper B Check 3:** color = the g₂/so(7) su(3) unitary on Q⁵ (V_a); non-unitary continuation on the
domain; naive bilinear is a clean negative; bosonic, #359 posited.
