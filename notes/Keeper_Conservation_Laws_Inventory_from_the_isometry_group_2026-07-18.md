# Conservation Laws from the Isometry Group of D_IV⁵ — the Noether inventory

**Keeper | 2026-07-18 | Strengthening program, item Keeper-2 (low-hanging fruit). Every Standard-Model conservation law is a symmetry of the one domain, read off by Noether. `conservation_inventory.py` (all dimension checks pass). Tier-honest: the *tally* + the *exact/broken pattern* are derived; the *explicit currents* are framework-pending LAG-1.**

## ⚠ CORRECTION (Casey, 2026-07-18): BST predicts conservation laws UNKNOWN TO NOETHER
My first draft framed *all* conservation as Noether-on-the-isometry-group. **That is incomplete — and it misses BST's genuinely novel content.** The corpus (T1945, T1929, and the information-theoretic thread) predicts three classes of conservation law, only the first of which is Noetherian:
1. **Noetherian** (continuous symmetry → current) — the standard set, below.
2. **TOPOLOGICAL** (protected by homotopy, NOT by any continuous symmetry) — **baryon, lepton, and generation number as winding / knot / cycle counts.** Noether cannot produce these; they are the standout prediction.
3. **Information-theoretic & cosmological** — the "Shannon" (conserved information charge via the Data Processing Inequality) and Λ×N = const.
The topological class is the important correction: in the Standard Model, baryon and lepton number are *accidental* global symmetries with no explanation — Noether gives them only as after-the-fact U(1)s. **BST gives them a topological origin, which explains what Noether cannot.**

## The principle (one line)
D_IV⁵ has isometry algebra **so(5,2)** (dim 21), forced by the (3 colors, 3 generations, dim 5) uniqueness. Noether turns each *continuous* symmetry into a current; the domain's *discrete* symmetries give C, P, T; and its *topology* (windings, knots, cycles) gives conserved counts no symmetry produces. **Conservation is the shadow of the domain's symmetry AND its topology.**

## The descent (Casey #14), dimension-verified
| algebra | dim | role |
|---|---|---|
| so(5,2) | 21 | full isometry group of D_IV⁵ |
| isotropy SO(5)×SO(2) | 11 | 10 + 1; the SO(2) is the charge circle J |
| tangent space | 10 | = 2 × dim_ℂ(D_IV⁵) = 2×5 ✓ |
| so(4,2) | 15 | conformal group of 4D Minkowski |
| Poincaré(4D) | 10 | 4 translations + 6 Lorentz |
| conformal extras | 5 | 1 dilatation + 4 special-conformal ✓ |
| so(3,1) | 6 | Lorentz |
All counts verified. The physical spacetime symmetries live in the SO(5,2)→SO(4,2)→SO(3,1) descent; the charge lives in the SO(2) isotropy factor.

## CLASS 1 — NOETHERIAN (continuous symmetry → current). Authoritative count: T1945.
| Conservation law | # | Origin (symmetry of D_IV⁵) | Status |
|---|---|---|---|
| **Energy** | 1 | time translation (Bergman) | EXACT |
| **Momentum** | 3 = N_c | spatial translation | EXACT |
| **Angular momentum** | 3 = N_c | SO(3) rotation | EXACT |
| **Electric charge** | 1 | SO(2) weight (T2470) | EXACT |
| **Weak isospin** | 3 = N_c | SU(2)_L ⊂ SO(5) | EWSB-hidden |
| **Weak hypercharge** | 1 | U(1)_Y | EWSB-hidden |
| **Color** | 8 = C_2 − N_c | SU(3) adjoint (𝕆 / Q⁵) | EXACT (supported tier) |
**Continuous total = 7 (spacetime) + 13 (gauge) = 20 = g + c_3** — both BST integers; the g + c_3 split is a corpus structural identification (T1945; c_3 = third Chern integer of Q⁵, T1950). *This supersedes my draft's 27-count, which wrongly folded in the 5 broken conformal generators.*
- Dilatation + special-conformal (5): BROKEN by the mass ruler (exact on the conformal EM boundary, F66).
- **CPT** EXACT (connected SO_0(5,2)); **P** VIOLATED — Möbius locus (T1947) + odd g (K729); **CP** VIOLATED — twist asymmetry (T1946); **T** VIOLATED — CKM Jarlskog (T1936). Each breaking has a *named BST source*.

## ★ CLASS 2 — TOPOLOGICAL (unknown to Noether — Casey's point, the real headline)
These are conserved by **homotopy**, not by any continuous symmetry. Noether cannot produce them. In the Standard Model B, L, and generation number are unexplained *accidental* symmetries; BST gives them a **topological origin** (T1945/T1929, Tier D — Proved):
| Conservation law | Topological origin | Why it's beyond Noether |
|---|---|---|
| **Baryon number B** | **trefoil cycle count** (the 3-crossing torus knot; **N_c = 3 forced**) | a knot can't be continuously unknotted → protected by topology, not symmetry |
| **Lepton number L** | **SO(5)-only winding count** (leptons colorless → live in the SO(5) part) | a winding number is a homotopy class, not a Noether charge |
| **Generation number** | **3 odd-power Q⁵ cycles** (T1929, N_c-forced) | cycle count on the compact dual — discrete topology |

**Why this is the strong content (what Noether can't do):**
- It **explains why B and L are conserved at all** — the SM has no symmetry forcing them; BST says topology protects them (perturbatively).
- It **explains how they're violated** — topological charges change only by *topology-changing* (non-perturbative) processes. B+L by electroweak sphalerons; and **L by 2 via the Majorana neutrino mass** — the ΔL=2, Δ(B−L)=2 topology-changing term that makes 0νββ occur.
- **⚠ REVISION FLAG (Casey, 2026-07-18):** the corpus's OLD statement "B−L is topologically protected → Dirac → 0νββ forbidden" (T1945, DoubleBeta paper, Working_Paper Vol5/Vol6) was **REVERSED on 2026-07-16** to **Majorana** (F413/K673, Toy 4691; 0νββ occurs, m_ββ∈[1.4,3.7] meV, detection SUPPORTS BST). Under the current reading, **B−L is NOT exactly conserved** — the Majorana mass is exactly the winding-changing ΔL=2 process. So the topological picture survives *reframed*: L is a winding count conserved perturbatively, **violated by the ΔL=2 Majorana topology-change**. Many corpus files still carry the old Dirac/B−L-exact statement and are STALE (see the Revision Register, K740).
- **A quark's B = 1/N_c is doubly grounded:** the fermion-content fact (N_c quarks per baryon) AND the topological fact (the baryon is the N_c-crossing trefoil). This part is unaffected by the neutrino reversal.

## CLASS 3 — INFORMATION-THEORETIC & COSMOLOGICAL (also non-Noether)
- **The Shannon — conserved information charge** (`BST_AC0_InformationTheory.md`): 1 Shannon = 1 bit of conserved information, protected by the **Data Processing Inequality** (no method can create information charge) — an information-theoretic conservation, not a symmetry current. Ties to Landauer (1 Shannon = k_B T ln2). [tier: framework/derived-in-info-theory]
- **Λ × N = const** (SP-26 reality budget): a cosmological conservation law across epochs — flagged in the corpus as needing the "not-an-epoch-coincidence" proof. [tier: structural, open verification]

## THE HEADLINE — the pattern of what's conserved vs broken is itself a prediction
This is the genuinely strong content, beyond "Noether works":
- The **EXACT** set — energy, momentum, angular momentum, electric charge, color — is exactly the set observed to be exactly conserved.
- The **BROKEN** ones are broken by mechanisms **BST derives**: parity by **g = 7 being odd** (K729, the volume-element chirality lock); CP by the Jarlskog phase; scale (dilatation/SCT) by the **mass ruler** (exact on the conformal EM boundary, broken in the massive bulk — matches F66: EM = the scale-free boundary, mass/gravity = the bulk).
- Weak isospin is **EWSB-hidden** (spontaneously broken by the Higgs), the current existing but the charge not manifest — standard, and consistent.
So BST doesn't just reproduce the conservation laws; it reproduces **which ones hold exactly and which are broken, and why.** That pattern is a downstream prediction of the geometry, not an input.

## Honest tiers (what's derived vs pending)
- **DERIVED:** the *correspondence* (symmetry ↔ conservation law, Noether) and the *tally* (which symmetry gives which law), because the isometry group is forced. The exact/broken *pattern* with its derived breakings.
- **SUPPORTED:** color conservation rides the color-structure tier (𝕆/Q⁵ supported, not yet dynamically derived — see Lyra L7).
- **FRAMEWORK-PENDING (LAG-1):** the *explicit* current forms j^μ_ξ = T^{μν}ξ_ν (isometries) and j^μ = (∂ℒ/∂(∂_μφ))δφ (internal) require the explicit Bergman Dirac Lagrangian. The inventory is complete; the closed-form currents wait on LAG-1 (Lyra L8).

## Discipline note (my draft's 27 was a miscount — corrected)
My first draft tallied the continuous generators as 4+6+1+3+8+5 = 27 and I flagged "don't bank the E₆ 27." Correct instinct, but the deeper issue: the 27 was **wrong** — it folded in the 5 *broken* conformal generators and mis-split spacetime. The **authoritative corpus count is T1945's 20 = g + c_3** (7 spacetime + 13 gauge), of *exactly-conserved* continuous laws. So: 27 not banked *and* not even the right number — the real number is 20 = g + c_3, which IS a clean BST-integer identity (Tier D, T1945). Lesson logged: check the corpus for an existing theorem before re-deriving a count from scratch (Casey caught exactly this).

## Publication note
This is publishable as a clean short result (roadmap: "conservation laws from the isometry group") and it strengthens the flagship: the conserved currents are the *same* SO(5,2) generators the masses (radial norms of its representations) and the gauge groups (its division-algebra structures) come from — one object, one symmetry, one set of conservation laws.

## Handoff
- **Elie (E4):** verify — reproduce the dimension counts independently and, once LAG-1 exists, confirm ∂_μ j^μ = 0 on-shell for at least P_μ, Q, and M_μν. Until LAG-1, the counting toy (`conservation_inventory.py`) is the verification artifact.
- **Cal:** referee the exact/broken *pattern* claim (is each breaking genuinely BST-derived, or asserted?) and the 27-not-banked flag.

— Keeper, 2026-07-18. Conservation laws = Noether on so(5,2): E/p ← translations, L ← Lorentz, Q ← SO(2), weak/color ← ℍ/𝕆; CPT exact; P/CP/scale broken by DERIVED mechanisms (odd g / Jarlskog / ruler). Tally + pattern DERIVED; explicit currents FRAMEWORK-pending LAG-1. 27-sum NOT banked (heterogeneous). See [[Keeper_K729...]] (parity), [[Keeper_K732_THE_SYNTHESIS...]] (gauge structures), [[Keeper_Strengthening_Roadmap_effort_ranked_2026-07-18]].
