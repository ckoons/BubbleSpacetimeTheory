---
node_type: working_note
title: Forcing — the Classification / Elimination Table (horizontal argument)
author: Keeper
status: living document (first pass 2026-08-06, K1235)
---

# The Classification / Elimination Table — the horizontal forcing argument

*Living document. The forcing program (K1235) has two halves: the **horizontal** (this table — among the finite list of bounded symmetric domains, only D_IV⁵ survives the prioritized criteria) and the **vertical** (the necessity table — every sub-manifold of D_IV⁵ is load-bearing). This is the horizontal half.*

**Honesty control (K1235):** each criterion must be **independently motivated** — a feature *any* physics-capable universe needs — NOT reverse-engineered from D_IV⁵. Each elimination must be **exhibited** (the specific failure shown), not asserted. Rows marked OPEN are the work; rows marked SOLID are exhibited.

## The "necessary" column IS "what physics needs" — and it splits in two (Casey, 2026-08-06)

Casey: *"our 'necessary' column is what physics needs."* Right — and the honesty of the whole argument lives in a distinction inside that phrase. "What physics needs" has two readings, and every necessity row must be labeled which one it is:

- **STRUCTURAL requirement (strong / independent):** what *any* physics-capable reality needs, argued from the concept of a universe that can host dynamics, records, and observers — a **time direction** (irreversibility), **records/fermions** (stable distinguishable states), **commitment/measurement** (projection), **interaction** (coupling), **stability** (bounded states). These are independently motivated; they do not look at D_IV⁵.
- **OBSERVED specific (weak until derived):** what *our* physics happens to have — N_c = 3, 4D, the specific integers. Asserting "physics needs N_c = 3" from observation alone is **fitting**, not forcing.

**The forcing STRENGTH = how much of the OBSERVED column we can DERIVE from the STRUCTURAL column.** A necessity row is **forcing-grade** iff its feature is either (a) a structural requirement, or (b) an observed specific *derived* from structural requirements. It is **fitting-grade** (weak, honestly flagged) if it is an observed specific merely *asserted*.

**T2545 is the template:** "3 spatial directions" (an observed specific) was **derived** from "irreducible Peirce component + Jordan simplicity" (structural) — so the (3,1) signature moved from *observed* to *structural-necessity*. Every row's job is that move: convert an observed specific into a consequence of a structural requirement. Whatever cannot be moved stays labeled "observed requirement" — that is the honest residual (Casey's relief valve), and the documented challenge to the next researcher.

## The candidate space (finite — Cartan's classification of irreducible bounded symmetric domains)

| Type | Domain | dim_ℂ | rank | Group |
|---|---|---|---|---|
| I_{p,q} | SU(p,q)/S(U(p)×U(q)) | pq | min(p,q) | SU(p,q) |
| II_n | SO*(2n)/U(n) | n(n−1)/2 | ⌊n/2⌋ | SO*(2n) |
| III_n | Sp(n,ℝ)/U(n) | n(n+1)/2 | n | Sp(n,ℝ) |
| **IV_n** | **SO₀(n,2)/[SO(n)×SO(2)]** | **n** | **2** | **SO₀(n,2)** |
| V | E6/[Spin(10)·U(1)] | 16 | 2 | E6(−14) |
| VI | E7/[E6·U(1)] | 27 | 3 | E7(−25) |

**D_IV⁵ = Type IV₅.** Everything outside this table (E8, F4, G2, and all non-Hermitian-symmetric structures) is eliminated at Stage 0.

## The prioritized criteria (most-critical-first, per Casey)

### Stage 0 — COMMITMENT (= Hermitian symmetric structure) — SOLID
*Independent motivation:* a physics-capable universe needs time, measurement, and projection — i.e. a contractive commit operator exp(−τH_B), which requires a Bergman kernel and a compact time-circle, i.e. a **Hermitian symmetric** structure.
*Eliminates:* **E8, F4, G2**, and every non-BSD structure — their maximal compacts have **no U(1) center**, so **no complex/Hermitian structure, no Bergman kernel, no commit operator.** (Web-confirmed: among exceptionals only E6, E7 are Hermitian symmetric.)
*Survivors:* the six domain types above.
**⟹ E8 is the EASY no-go. It never had commitment.** Casey's "between D_IV⁵ and E8" memory is right that E8 was ruled out — but the *careful* competitors that survive Stage 0 are **E6 (Type V) and E7 (Type VI)**, the exceptional domains that DO have commitment. Ruling those out is the real Stage-1+ work.

### Stage 1 — LORENTZIAN CONFORMAL STRUCTURE (boundary = Minkowski) — STRONG LEVER, to firm up
*Independent motivation:* a physics-capable universe needs **Lorentzian spacetime** (one time, space).
*The lever:* **SO(n,2) is the conformal group of (n−1,1) Minkowski space** — Type IV_n's boundary/conformal structure IS Lorentzian spacetime (BST-Rehren holography, T2113). This is the reason BST uses SO(5,2): its Shilov boundary carries 4D Lorentzian conformal structure.
*Eliminates (candidate — needs each exhibited):* Type I_{p,q} (SU(p,q) — no Lorentzian-conformal reading of the boundary); Type II_n (SO*(2n)); Type III_n (Sp — the Siegel domain, related to phase space not spacetime); **Type V = E6 and Type VI = E7** (their boundaries are octonionic/Jordan-algebraic, not (n−1,1) Minkowski).
*Status:* the **strongest distinguishing criterion**, and independently motivated. Each non-IV elimination is **OPEN — to be exhibited** (which specific spacetime feature each fails). This is where Grace's Jordan/Peirce math + the boundary-structure analysis lands.
*Survivors (target):* **Type IV_n.**

### Stage 2 — THE INTEGERS pin n = 5 — the PEIRCE ROUTE (candidate repair, K1237), replaces the broken holography step
*Independent motivation:* N_c = 3 colors (SU(3)) — the color structure a physics-capable universe with our matter needs.
*The lever (Peirce, riding BANKED T2545 — NOT holography):* T2545 says the off-diagonal Peirce component **V₁₂ of D_IV^n has dim = n − 2** (= the short-root multiplicity), and it IS the irreducible **color triplet** = the 3 spatial directions. Reversed: **N_c colors = n − 2 ⟹ n = N_c + 2 ⟹ for N_c=3, n = 5 = n_C.** So n_C=5 **would be** a consequence of N_c=3 — an **integer-collapse** (2 inputs → 1) that also closes the rank-2 residual — **IF the open premise below holds.** Rides **banked T2545**, sidesteps the broken holography lift entirely.
*THE OPEN PREMISE (Grace, K1238 — sharper than the dimension formula):* T2545 was banked *given* n=5, so reading it backward needs **"color IS the short-root space" independently forced, NOT recognized post-hoc.** Sub-check: is **dim V₁₂(D_IV^n) = n − 2** a general-n identity? (I do NOT bank it — Grace owns the exact spin-factor bookkeeping; n−1 vs n−2 conventions differ.) Until "color=short-root" is exhibited, this is a **LEAD, not a forcing.**
*Scope:* would force n_C **given** N_c; does NOT force N_c=3 (residual input, labeled).
*Status:* **CANDIDATE lead** (Route A), stronger *anchor* than the dead holography route, but gated on the "color=short-root" premise — narrowed-not-forced (see also Route B, generations/Hopf, → n∈{5,6}).

## The rank-2 residual family (Elie, 2026-08-06 — honest: commitment + rank-2 does NOT isolate D_IV⁵)

Elie source-pinned two facts that matter:
- **D_IV⁵'s two integers ARE the domain's own geometry:** Type IV₅ has **complex dimension n = 5 = n_C** and **rank = 2 = the BST rank.** So n_C and rank are NOT fitted — they are the *defining data* of the domain. **Forcing "Type IV₅" therefore forces two of the five integers structurally.**
- **Commitment + rank-2 leaves a RESIDUAL FAMILY** (not yet unique). The rank-2 bounded symmetric domains are: **I_{2,q}** (SU(2,q)), **II_{4,5}** (SO*(8), SO*(10)), **III_2** (Sp(2,ℝ)), **IV_n** (all n≥3), and **V = E6**. So "commitment + rank-2" cuts hard but does not close — the residual is a **documented challenge**, not a claim of uniqueness. Two clean independently-motivated filters, a finite residual — partial forcing, the honest posture.

## The interlock — how the two legs meet (the NAIVE chain below is BROKEN; see the ⚠ correction)

The naive attempt connected the two legs through the holographic descent — **but it is broken** (off-by-one, ⚠ below); shown here only as the superseded reasoning:
- **N_c = 3 (color) → 3 spatial directions** (T2545, banked) **→ 3+1 = 4D Lorentzian** (needs the "+1 time" row exhibited).
- **4D Lorentzian spacetime → its conformal group SO(4,2)** (standard: SO(4,2) = conformal group of 4D Minkowski).
- **SO(4,2) sits as the boundary of SO(5,2)** via the BST-Rehren holography (**T2113, registry tier-I Identified — NOT proved**) — *claimed* one bulk dimension over the 4D boundary.
- **⟹ [BROKEN] the bulk is Type IV₅ ⟹ n_C = 5.** — this step is exactly the smuggled +1.

**⚠ OFF-BY-ONE — Cal §323 + Keeper K1236 (the chain does NOT currently force n_C=5):** the group bookkeeping breaks the naive chain. **D_IV^n = SO(n,2)**, so SO(4,2) = D_IV⁴ = **n_C=4**, and SO(5,2) = D_IV⁵ = n_C=5. The chain's 4D boundary has conformal group SO(4,2) = **n_C=4**. **Standard holography (AdS/CFT and Rehren) SHARES the group** — a 4D CFT (SO(4,2)) has bulk AdS₅ with isometry SO(4,2) = D_IV⁴-worth (n_C=4), NOT SO(5,2)=D_IV⁵. So the jump **SO(4,2) → SO(5,2)** is exactly where the +1 lives, and standard holography does NOT provide it → the naive chain gives **n_C=4**, and the +1 was smuggled. **And T2113 is registry tier-I (Identified), "pending operator algebra" — NOT proved** (K1224's "PROVED" was an over-statement; grepped, not cited) — a *same-group* duality, so it doesn't even go the forcing direction.

**⟹ n_C=5 is NOT currently forced by N_c=3; it remains an independent input.**

**⚠ CORRECTION (Grace's catch, K1238) — the "+1" is NOT the commitment circle.** The off-by-one lives entirely in the **n** (the space count), never in the **2** (the time factor): SO(4,2) and SO(5,2) have the **same SO(2)**. So the compact SO(2) **commitment circle is already present at n=4** — it *cannot* be the extra dimension. The **+1 (n: 4→5) is a NON-COMPACT, holographic/radial SPACE direction.** (An earlier framing "the +1 = the commitment circle" fused two different objects — do not re-fuse them.) So the honest crux is NOT "why does recording add the circle" (already there) but **"why a 5th non-compact SPACE direction (n: 4→5)?"** — answered, if at all, by color/generation structure, not recording.

**TWO candidate routes to n=5 (both narrowed, neither closed; holography DEAD):**
- **Route A — color / short-root (Grace = K1237):** short-root mult(D_IV^n) = n−2; T2545 identifies it with the N_c=3 color triplet; backward, n−2=3 ⟹ n=5. *Open premise:* "color IS the short-root space" must be **independently forced, not recognized post-hoc** (T2545 was banked given n=5).
- **Route B — generations / Hopf (Lyra):** 3 generations fit n ∈ **{5,6}** (not just 5); picking 5 over 6 needs a **Hopf/spinor-fibration** fact (works at 5, fails at 6). *Open.*

**Three-tier honest picture:** record → Type IV (family); generations → {5,6}; a third fact (color=short-root, or the Hopf condition) → 5. **n_C=5 narrowed hard, not forced.**

**Three guards** (K1238): (Cal) derive the +1 from the 4D side, don't input any 5D structure; (Grace) don't fuse the compact SO(2) circle with the non-compact +1; (premise) a backward-read needs its premise independently forced.

**What survives:** the **Lorentzian-conformal filter** still cleanly cuts the rank-2 residual family (E6, I/II/III) down to the **family** Type IV_n (only Type IV has an SO(n,2)-Lorentzian boundary; some competitors are Type IV in disguise: Sp(4,ℝ)≅SO(3,2), SU(2,2)≅SO(4,2)) — but it selects the FAMILY, **not the dimension n.** Fixing n=5 is the same open group-lift step. And "n_C, rank are **structural** (the domain's defining data, not fitted)" stands — distinct from "the values 5,2 are **forced**" (open = forcing which domain).

## ★ THE ACTUAL FORCING ALREADY EXISTS — Paper B (K1247 reconnect), holography-free

The holography route to n=5 broke (Cal), and the Peirce route (Route A) is K1237's fragment — but the corpus already has the **completed, holography-free forcing** in **Paper B (Cartan-elimination v0.2, 2026-06-21, K453 CONDITIONAL PASS)**. It survives everything caught today (it uses no holography):

- The criteria collapse to **two root-system invariants — (rank = 2, short-root multiplicity m_s = 3)** — which force **both** dim_C = 5 **and** N_c = 3, since for type IV **dim_C = m_s + rank** and **N_c = m_s**. Neither "5" nor "3" is in the criteria. **Elie Toy 4290 verified** rank=2 ∧ dim_C=5 ⟹ D_IV⁵ across all six families.
- **m_s = 3 is itself forced:** **R3 (spherical-transform/c-function CONVERGENCE ⟹ m_s ≥ 3) ∧ R5 (SELBERG-class d_F ≤ 2 ⟹ m_s ≤ 3)** meet at exactly 3. So (rank=2) ∧ R3 ∧ R5 ⟹ m_s=3 ⟹ D_IV⁵ ⟹ n_C=5, N_c=3 — from three criteria none of which name a dimension or a color.

**This corrects the "narrowed to {5,6}, not forced" state above** (that reflected the *broken holography route*, not the corpus). **Honest tier — a CONDITIONAL forcing.** The criteria-innocence audit (K1251) sharpens the open items to **THREE concrete checks** (R2/R4 are solid; R1's rank=2 is the paper's own framework-tier input, depth-2 T316):
1. **Verify the m_s=3 n-scan** (R3∧R5 → n=5) — "computed but awaiting independent harness verification" (Paper B Δ5). *(Grace/Elie.)*
2. **R3 circularity check** — its bound "m_s ≥ 3" rests on "convergence needs order ≥ 6, so ⌊n_C/2⌋ = 2 seminorms converge," which invokes **n_C** (the conclusion). Show the convergence order is **rank-determined (R1, prior), not n_C-determined.** *(R3 excludes n=3.)*
3. **R5 prior-degree check** — "d_F ≤ 2" is **stronger than "lies in the Selberg class"** (which admits all degrees). Exhibit a **prior** reason the substrate's zeta must be degree ≤ 2 — not tractability, not reverse-engineered (≤2 is exactly the bound giving n ≤ 5). *(R5 excludes n ≥ 7.)*

If (2) and (3) firm up, the forcing is tight (R2/R4 solid, R3/R5 innocent, n-scan verified), residual = only R1's depth-2. **These three named checks ARE the honest "criteria-innocence open," not a vague worry.**

**⚠ SHARPENED (K1255) — the n-scan is a two-bound PINCER, and both bounds' innocence is the whole ballgame.** The logic is verified (n=5 unique; d_F=(n−1)/2 reproduces Paper B). But the two criteria are **opposite bounds meeting at 5**: **R3 ⟺ m_s ≥ 3 ⟺ n ≥ 5** (lower, convergence) and **R5 ⟺ d_F ≤ 2 ⟺ n ≤ 5** (upper, Selberg). That's elegant *if* both are independently prior — but it's **exactly the shape a reverse-engineered lower+upper pair would take.** Both carry a real, named risk:
- **R3 risk (multiplicity-circularity):** the inverse spherical transform must beat the Plancherel density |c(λ)|^{−2}, whose growth degree = 2·(roots *with multiplicity*) = dim−rank — which **involves m_s** — so the convergence order plausibly depends on the multiplicities (n-dependent → "m_s≥3" partly circular). The ⌊n_C/2⌋=rank coincidence holds *only* at n∈{4,5}, so rank-vs-n_C is indistinguishable at n=5. **Check:** is the threshold dim(a*)=rank (prior→innocent) or the multiplicity-growth (circular)? — the Harish-Chandra estimate.
- **R5 risk:** d_F≤2 ⟺ n≤5 *exactly*; the Selberg class admits all degrees, so ≤2 needs a **prior reason** beyond "gives n=5."

I resisted declaring R3 innocent (the one-line check on the Plancherel growth caught the temptation). Paper B stays **conditional**; the pincer + both risks go in the paper so a referee sees the exact risk.

The forcing lane's real next target is **those two concrete items**, NOT "why 5 not 6." The Forcing+Evidence paper (#31) builds its Forcing half on this spine (extend Paper B v0.2).

## Honest current state
- **Stage 0 (commitment): SOLID** — E8/F4/G2/non-BSD eliminated, exhibited (no U(1) center → no Hermitian structure → no commit operator).
- **Stage 1 (Lorentzian conformal): STRONG LEVER, eliminations OPEN** — the criterion is right and independently motivated (SO(n,2) = conformal group of Minkowski); each non-IV domain's failure needs exhibiting. This is the load-bearing horizontal work, and the real competitors are E6/E7 (not E8).
- **Stage 2 (integers → n=5): PARTLY IN HAND** — T2545 is one exhibited row; the rest is the vertical necessity table.

## What this does NOT claim (scope)
It does not yet force D_IV⁵ — Stages 1–2 have exhibited rows and open rows. It is a **living argument**: it strengthens as each non-IV elimination is exhibited and each integer-necessity is banked. Partial completion is valuable; the residual is a documented challenge (Casey's relief valve).

*Next: Grace exhibits the Stage-1 boundary-structure failures (why E6/E7/I/II/III boundaries aren't Lorentzian 4D) via the Jordan/Peirce structure; Keeper audits each exhibited elimination against the independence control.*
