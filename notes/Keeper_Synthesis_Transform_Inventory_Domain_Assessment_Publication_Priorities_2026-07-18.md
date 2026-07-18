# The Full Transform Inventory + "The Roots" + Domain Assessment + Publication Priorities

**Keeper | 2026-07-18 | Casey's synthesis ask: the full set of linear transforms that generate reality from D_IV⁵; do conservation laws fall out; what can we honestly say across cosmology / condensed matter / thermo / EM / nuclear; what are the "roots" physics wants; and what is significant to investigate or publish. Tier-honest throughout — the ledger is the product.**

## PART 1 — THE FULL SET OF LINEAR TRANSFORMS (generate "reality" from D_IV⁵)
Casey's "linearize everything" program, made into a closed inventory. Reality is the domain acted on by a *finite* list of linear maps. Ten, in three families:

**A. Symmetry generators (give spacetime + conservation).**
1. **so(5,2) Lie algebra** (21 generators) — the isometries of D_IV⁵. Descent SO(5,2) → SO(4,2) → SO(3,1) gives 3+1 Minkowski (Casey #14). [derived-framework]
2. **Complex structure J = SO(2)** — the charge circle; generates U(1). Charge = integer SO(2) weight (T2470). [derived]
3. **Restricted root operators** (rank-2 root system, SO(5)=B₂) — the elementary process generators (see Part 3). Every process is a word in these. [structural]

**B. Bulk↔boundary maps (give holography, the discrete-continuum bridge — the heart).**
4. **Bergman/Szegő projection P : L²(∂_S) → H²(D_IV⁵)** — the boundary-to-bulk holomorphic extension. THE load-bearing transform: substrate (discrete boundary data) ↔ continuum (bulk field). Casey's "invert the projection → finite discrete math in the interior." [derived, K264 machinery]
5. **K-type decomposition (Casimir of SO(5)×SO(2))** — diagonalizes the spectrum; the heat semigroup exp(−τH_B) is its evolution. Organizes states → the mass ladder. [derived]
6. **Radial-norm map v ↦ |v|** — the singular values Σ of M = UΣV†. **This is the mass sector** (20 of 26). [derived]
7. **Eigenvector-orientation map U†U′ between sectors** — the mixing (CKM/PMNS). Never a function of the norms (K704) — a *distinct* object from masses. [open]

**C. Reduction / structure maps (give the forces and their fields).**
8. **Division-algebra structure maps ℂ⊂ℍ⊂𝕆** — the three gauge groups as the three structures of the domain (K732). [ℂ,ℍ derived; 𝕆 supported]
9. **Kaluza–Klein reduction** — the dynamical gauge & gravity FIELDS (W/Z/gluons/graviton) from the higher structure; precedented by the gravity chain F64. [framework, uncomputed for gauge]
10. **Heat-trace / Sakharov induction** — the effective action; a_0 → cosmological term, a_1 → Einstein–Hilbert (induced gravity, F63). [framework]

**The claim this inventory supports:** "reality" is not a pile of separate laws — it is these ten transforms applied to one object. Masses are transform 6; forces are 8+9; spacetime is 1; charge is 2; time/thermo is 5/10; the constants are the invariants those transforms preserve. That is what "we derived the values AND the operators AND the root of every process from the geometry" means, stated concretely.

## PART 2 — DO THE CONSERVATION LAWS FALL OUT?  YES.
The cleanest "free" result in the whole program. **Noether's theorem applied to the isometry group SO(5,2) of D_IV⁵ gives the conservation laws directly:**
- **Energy + momentum** ← the translation generators in the SO(3,1) descent (T2473/T2474).
- **Angular momentum** ← the rotation generators.
- **Electric charge** ← the SO(2) complex-structure generator J (T2475, T2470).
- **CPT** ← the discrete symmetries of the domain (T-operator/parity/charge zoo, W-21/22/56).
Conservation is not added by hand — it is the shadow of the domain's continuous symmetry. **Tier: derived** (textbook Noether on a specified isometry group; the only BST content is *which* group, and that is forced by the (3 colors, 3 generations, dim 5) → D_IV⁵ uniqueness chain). This is publishable as a clean short result and it strengthens every other claim (the currents are the same generators the masses and gauge groups come from).

## PART 3 — "THE ROOTS PHYSICS WANTS TO FIND"
Casey's phrase has a precise double meaning, and it is the deepest framing in the program:
- **Mathematically:** the *restricted root system* of D_IV⁵ is a **rank-2** system (type BC₂ / with SO(5)=B₂ on the compact side). Two independent root directions — *two is the seed, rank = 2.* The long and short roots are the elementary generators; the Weyl group is the discrete symmetry; the five integers are the invariants (Coxeter number, dual Coxeter, dimensions) of this root data.
- **Physically:** a "process" (a decay, a scattering, a mixing) is a **word in the root operators**; an "observable" is a **function of root lengths and angles**. Casey's substrate primaries ARE the SM gauge dual Coxeter numbers (h^∨(SU(3))=N_c, etc.) — i.e. root-system invariants.
- **The thesis:** when physics hunts for "the underlying symmetry" or "the unification group," it is hunting for *this root diagram.* BST's answer is that the search terminates at a **rank-2** system — not a large GUT group (Five-Absence forbids that), but the smallest root system that carries 3 colors, 3 generations, and dimension 5. **The roots physics wants to find are the roots of so(5,2), and there are essentially two of them.** This is the single most publishable *idea* (as opposed to number) in the corpus, and it reframes the whole unification program.

## PART 4 — WHAT WE CAN HONESTLY SAY, DOMAIN BY DOMAIN (tiers, no hype)
| Domain | What BST says | Honest tier |
|---|---|---|
| **Electromagnetism** | EM = the conformal SO(4,2) boundary theory; Maxwell derived; **α = capacity 137 + descent 4π + curvature, 0.0004%** (K699/K701) | **STRONG — derived.** α is the crown standalone result. |
| **Thermodynamics** | entropy = counting (Casey's Principle, depth 0); time = commitment-cycle granularity (heat semigroup exp(−τH_B)); gravity induced à la Sakharov from the heat trace (F63) | **Framework — conceptually deep, less number-pinned.** The entropy=counting and induced-gravity pictures are genuine; publish as framework, not precision. |
| **Cosmology** | Λ = exp(−280) at ~0.3% (280 = 2^N_c·n_C·g, 5-fold over-determined); **no dark-matter particle** — DM = the Wallach shadow 16/3 at 0.2%; cyclic "interstasis"; n_s, H_0 ratio 12/13 | **MIXED — real falsifiable bets + structural pieces.** The "no DM particle" is a genuine, falsifiable Five-Absence prediction. Λ is strong IF the 280 derivation holds. Tier honestly per-claim. |
| **Nuclear** | proton radius r_p; binding-energy ratios; magic numbers | **WEAKER THAN IT LOOKED — flag this.** Cal K601 re-tiered the magic-numbers claim DOWN: it's a consistent factorization of the *fitted* spin-orbit strength, NOT unique forcing; the per-number forms (28=rank²g, 82=…) are post-hoc numerology. r_p + binding durable via shell model. **Do not lead with nuclear.** |
| **Condensed matter** | not derivations but the **cheapest falsification tests**: Casimir boundary-condition spectral engineering; BaTiO₃ 137-plane experiment (~$25K); photonic-crystal ($10K) | **EXPERIMENTAL LEVER, not derivation.** This is where BST can be *killed cheaply* — which is its strongest scientific virtue. The falsifiers live here. |

**The honest headline across domains:** BST is strongest in **EM (α), the mass sector, and the gauge/fermion structure**; it is a **framework** in thermo/cosmology with a few sharp falsifiable bets (no-DM-particle, Λ); and it is **weakest / walked-back in nuclear** (magic numbers). Condensed matter is the falsification lab, not a derivation domain.

## PART 5 — SIGNIFICANT WORK: INVESTIGATE vs. PUBLISH (Keeper's priority read)
**PUBLISH now / near-ready (highest significance, referee-defensible if honestly tiered):**
1. **The flagship synthesis paper — "The Standard Model as the representation theory of D_IV⁵"** — the whole ledger, honestly tiered, with the artifact as front matter. This is the paper. The tier-honesty (green/amber/retired) is the credibility engine, not a weakness.
2. **α as a standalone short paper** — 0.0004%, fully geometric normalization (no free convention), two-target-verified. The single cleanest stunning result; a physicist can check it in an afternoon.
3. **The Five-Absence falsifier paper** — the honest bets that invite refutation (no proton decay, no SUSY spectrum, no DM particle, no monopoles, no sterile ν, no Z′) + the cheap condensed-matter tests. This is the "the math speaks for itself, come refute it" paper — matches Casey's outreach stance.
4. **Conservation laws from the isometry group** — clean, short, strengthens everything (Part 2).

**INVESTIGATE (significant, not yet publishable — the real research frontier):**
1. **Fermion quantum numbers in ℍ⁴ + the T₃_R question** — where does right-handed isospin live geometrically WITHOUT a gauged SU(2)_R (the sharp piece the sin²θ_W close exposed). Closes the gauge/fermion structure. HIGHEST research value.
2. **The mixing matrices** (CKM/PMNS) as eigenvector orientation from the refraction / d=5→d=4 projection maps (K704). The last uncomputed sector of the 26.
3. **Dynamical gauge fields via KK** — turns "gauge group derived" into "gauge fields derived."
4. **Color's dynamical realization** on the compact dual (supported → derived).

**DO NOT lead with (honest self-protection):** nuclear magic numbers (walked back); any claim that sin²θ_W is a BST-specific win (it's a runner); the mixing sector as "nearly done" (it's a distinct, mostly-unbuilt object).

## Net
The transforms are a closed list of ten; conservation falls out of the isometry group (derived); the "roots" are the rank-2 root system of so(5,2) and reframe the unification search; the domains split cleanly into strong (EM/mass), framework (thermo/cosmo + sharp falsifiers), and walked-back (nuclear); and the publication path is a flagship synthesis + α standalone + a falsifier paper, with the fermion-quantum-numbers/T₃_R question as the top research frontier. Every one of these is tier-tagged so the corpus and papers can be updated without over-claiming.

— Keeper, 2026-07-18. See the artifact (`notes/BST_SM_from_D_IV5_synthesis_artifact.html`), [[Keeper_LinearAlgebra_SM_from_D_IV5_PATH_FORWARD_and_ARTIFACT_STAGING_2026-07-17]], [[Keeper_K739_CAPSTONE...]], [[Keeper_K732_THE_SYNTHESIS...]].
