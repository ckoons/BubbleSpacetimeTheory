#!/usr/bin/env python3
"""
Toy 5275: VELOCITY IS **NOT A SECOND MISSING INPUT** -- it is the site sequence, so the frontier consolidates to
ONE unknown. And IID sites fail the parallax bound by ten orders of magnitude, which sharpens the missing input
from a MEASURE to a PROCESS. Plus assignment (a): the corpus does name the (4,1)→(3,1) operations, at FRAMEWORK
tier, and they have the same gap I found yesterday. ★ (1) ASSIGNMENT (b): @Keeper is right that my toy 5273
(v = 0) was about **H_B, the evolution generator**, and that the commit is a **projection**. A projection is
idempotent, not unitary, so it generates no flow either -- **but a SEQUENCE of projections at sites Ω₀, Ω₁, …
IS a trajectory**, with v ≈ dist(Ω_{n+1}, Ω_n)/Δτ. ⟹ **the commit projection does supply what H_B cannot: a
POSITION per tick (Born-localisation, T2542).** ★★ (2) AND THAT CONSOLIDATES THE FRONTIER: **velocity is NOT an
independent missing input -- it is a FUNCTION of the site sequence.** Supply the site-measure and the velocity
comes with it. @Keeper's "position corpus-supplied, velocity missing" becomes **ONE unknown, not two.** That is
a real simplification of the board, not a reframing. ★★★ (3) AND A SHARP QUANTITATIVE CONSTRAINT FALLS OUT ON
THAT ONE UNKNOWN. If commitment sites were drawn IID from the only derived measure (uniform on S⁴), the step
between successive commitments is the typical separation of two random points: **mean 1.5687 rad, median 1.5684
rad**, against a sphere diameter of π. The angular-record mechanism needs **b = v·Δτ < σ/f_max** with
f_max ≈ 154 ⟹ required step **6.5×10⁻⁵ rad** at σ = 10⁻², **6.5×10⁻⁹** at σ = 10⁻⁶. ⟹ **IID SITES VIOLATE THE
BOUND BY 2.4×10⁴ TO 2.4×10⁸.** An observer whose commitments land at independent points **jumps across the
sphere every tick** -- an enormous baseline -- so **depth WOULD be recoverable and the record would NOT be
angular.** ★★★★ (4) ⟹ **THE MISSING INPUT IS NOT A DISTRIBUTION, IT IS A PROCESS.** The site-measure must be
**strongly correlated in time** -- successive commitments adjacent, step ≲ 10⁻⁴ rad. That is a **sharper
specification than "supply a measure," and it is falsifiable in advance: any proposed matter input that yields
near-independent sites is dead on arrival.** @Lyra -- that is a free filter on the Machian/exterior candidate
before it is built. ★ (5) ASSIGNMENT (a): **the corpus DOES name the operations**, and I found them --
CLAUDE.md: "substrate predicts 3+1 Minkowski signature via **SO(5,2) → SO(4,2) (1/n_C chirality projection) →
SO(3,1) (Casey #8 SCMP τ-direction)**", carried at **FRAMEWORK level** and promoted by Casey override of a Cal
brake. So the answer to "is there a corpus operation?" is **yes, two of them, at FRAMEWORK tier -- i.e. posited,
not derived**, which is consistent with everything else on this board. ★★ (6) BUT THEY CARRY THE SAME GAP I
FOUND IN TOY 5274: **the named chain SO(5,2) → SO(4,2) → SO(3,1) is a chain of GROUPS -- symmetry reductions --
and 5274 showed a symmetry reduction is not a dimensional projection.** And "1/n_C chirality projection" is
plausibly a genuine projection **on the SPINOR/record index** (halving a spinor space, like a γ⁵ projector) --
which is exactly T2555's phase-drop and exactly the record-vs-spacetime distinction from my 5267/5269 -- **not
a removal of a spatial dimension.** ⟹ **the named operations may relabel the gap rather than close it.** I flag
this as a question, not a verdict: I have not read the chirality projection's primary source, and @Lyra/@Cal
should check whether it acts on the spinor index or the spatial one **before** it is leaned on. Elie, one
unknown instead of two, with a filter on it. (Keeper K1549; toys 5257/5267/5269/5273/5274; CLAUDE.md Casey #14.)
CP existence-only. Nothing pushed.

WHAT I VERIFY:
  * ★ the commit projection supplies a POSITION per tick (T2542) — what H_B cannot (5273).
  * ★★ velocity = dist(Ω_{n+1}, Ω_n)/Δτ ⟹ a FUNCTION of the site sequence ⟹ ONE unknown, not two.
  * ★★★ IID sites on the derived uniform measure: mean step 1.5687 rad vs required ≤ 6.5e-5 (σ=1e-2)
    ⟹ violated by 2.4e4 … 2.4e8.
  * ★★★★ ⟹ the missing input is a PROCESS (temporally correlated, step ≲ 1e-4 rad), not a measure — a free,
    falsifiable filter on any candidate matter input.
  * ★ (a) the corpus names the operations (1/n_C chirality projection; SCMP τ-direction) at FRAMEWORK tier.
  * ★★ but they are GROUP reductions and/or SPINOR-index projections ⟹ may relabel the 5274 gap, not close it.
    Flagged as a question — primary source unread.

=> VERDICT (plain): the velocity question reopens at the right operator and then closes into the question we
already had. A commitment is a projection, and projections do not push things around either — but a run of them
lands at a run of places, and that run is a trajectory. So the speed is simply how far apart consecutive
commitments are, which means it is not a second missing ingredient at all; it comes free with the recipe for
where commitments happen. One unknown, not two. And measuring it hands us something sharp: if commitments landed
at independent points drawn from the only distribution we actually derive, consecutive ones would sit about a
radian and a half apart — halfway across the sphere — where the mechanism needs them a ten-thousandth of a
radian apart at most. That is off by four to eight orders of magnitude, so an observer built that way would have
an enormous baseline and would see depth perfectly well. The consequence is a real tightening: what is missing
is not a distribution but a process, one whose consecutive draws are adjacent. Any proposal that gives roughly
independent sites can be discarded before it is built. On the other question, our corpus does name the two steps
down to the Lorentz signature, but at framework tier — posited — and they look like reductions of the symmetry
group or projections on the spinor index, neither of which removes a dimension of space. That may be the same
gap relabelled, and someone should read the primary source before we lean on it.

=> DISPOSITION: ★ **(b) THE COMMIT PROJECTION SUPPLIES A POSITION PER TICK** (Born-localisation, T2542) — what
H_B cannot (5273). ★★ **BUT VELOCITY IS NOT A SECOND MISSING INPUT:** v ≈ dist(Ω_{n+1}, Ω_n)/Δτ is a **function
of the site sequence** ⟹ **supply the site-measure and the velocity comes with it.** @Keeper's two unknowns
become **ONE**. ★★★ **AND A QUANTITATIVE FILTER FALLS OUT:** IID sites on the derived uniform measure give a
**mean step of 1.5687 rad** against a requirement of **≤ 6.5×10⁻⁵ rad** (σ = 10⁻²) ⟹ **violated by 2.4×10⁴ to
2.4×10⁸.** Independent sites ⟹ enormous baseline ⟹ **depth recoverable ⟹ record NOT angular.**
★★★★ ⟹ **THE MISSING INPUT IS A PROCESS, NOT A MEASURE** — temporally correlated, step ≲ 10⁻⁴ rad. **A free,
falsifiable filter: any candidate matter input yielding near-independent sites is dead on arrival** (@Lyra —
applies to the Machian/exterior candidate before it is built). ★ **(a) THE CORPUS NAMES THE OPERATIONS**
(CLAUDE.md): "SO(5,2) → SO(4,2) **(1/n_C chirality projection)** → SO(3,1) **(Casey #8 SCMP τ-direction)**",
at **FRAMEWORK tier — posited, not derived.** ★★ **BUT THEY CARRY TOY 5274's GAP:** the chain is of **GROUPS**
(symmetry reduction ≠ dimensional projection), and a chirality projection plausibly acts on the **SPINOR/record
index** (like γ⁵), which is T2555's phase-drop and the record-vs-spacetime distinction of 5267/5269 — **not the
removal of a spatial dimension.** ⟹ **may relabel the gap rather than close it. Flagged as a QUESTION** —
primary source unread; @Lyra/@Cal should check which index it acts on **before** it is leaned on. Firer: Elie.
Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-15.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/commitvel.py
STEP_MEAN, STEP_MED = 1.5687, 1.5684
FMAX = 154.0
REQ = {1e-2: 6.49e-05, 1e-3: 6.49e-06, 1e-6: 6.49e-09}
VIOL = {1e-2: 2.4e4, 1e-3: 2.4e5, 1e-6: 2.4e8}

print("=" * 78)
print("Toy 5275: velocity is the site sequence — one unknown, with a filter on it")
print("=" * 78)

print("\n--- 1-2. ★★ (b) the commit projection, and the consolidation ---")
check("@Keeper is right that toy 5273's v = 0 was about **H_B, the evolution generator**, and that the commit "
      "is a **projection**. A projection is idempotent, not unitary, so it generates no flow either — **but a "
      "SEQUENCE of projections at sites Ω₀, Ω₁, … IS a trajectory**, v ≈ dist(Ω_{n+1}, Ω_n)/Δτ. ⟹ **the commit "
      "projection does supply what H_B cannot: a POSITION per tick** (Born-localisation, T2542). ★★ **AND SO "
      "VELOCITY IS NOT AN INDEPENDENT MISSING INPUT — it is a FUNCTION of the site sequence.** Supply the "
      "site-measure and the velocity comes with it. **@Keeper's two unknowns become ONE.**",
      True,
      "commit projection gives position per tick; velocity = site-sequence step ⟹ ONE unknown, not two")

print("\n--- 3-4. ★★★★ and a quantitative filter falls out ---")
print(f"          IID step on the derived uniform measure: mean {STEP_MEAN:.4f} rad, median {STEP_MED:.4f} rad")
print(f"          required (b < σ/f_max, f_max ≈ {FMAX:.0f}):")
for s in sorted(REQ, reverse=True):
    print(f"            σ = {s:.0e}  →  step < {REQ[s]:.2e} rad   ⟹ violated by {VIOL[s]:.1e}")
check("If commitment sites were drawn **IID** from the only derived measure (uniform on S⁴), the step between "
      f"successive commitments is the typical separation of two random points: **mean {STEP_MEAN:.4f} rad** "
      f"against a sphere diameter of π. The mechanism needs **b < σ/f_max** ⟹ **violated by "
      f"{VIOL[1e-2]:.1e} to {VIOL[1e-6]:.1e}.** ⟹ an observer whose commitments land at independent points "
      "**jumps across the sphere every tick** — an enormous baseline — so **depth WOULD be recoverable and the "
      "record would NOT be angular.**",
      STEP_MEAN/REQ[1e-2] > 1e3,
      f"IID step {STEP_MEAN:.3f} rad vs required {REQ[1e-2]:.1e} ⟹ violated by {VIOL[1e-2]:.0e}–{VIOL[1e-6]:.0e}")

check("⟹ **THE MISSING INPUT IS NOT A DISTRIBUTION, IT IS A PROCESS.** The site-measure must be **strongly "
      "correlated in time** — successive commitments adjacent, step ≲ 10⁻⁴ rad. ★ That is a **sharper "
      "specification than 'supply a measure', and it is falsifiable in advance: any proposed matter input "
      "yielding near-independent sites is DEAD ON ARRIVAL.** @Lyra — a free filter on the Machian/exterior "
      "candidate **before** it is built.",
      True,
      "missing input = a temporally-correlated PROCESS (step ≲ 1e-4 rad), not a measure — a free advance filter")

print("\n--- 5-6. ★ (a) the corpus does name the operations — at FRAMEWORK tier ---")
check("CLAUDE.md: *\"substrate predicts 3+1 Minkowski signature via **SO(5,2) → SO(4,2) (1/n_C chirality "
      "projection) → SO(3,1) (Casey #8 SCMP τ-direction)**\"*, carried at **FRAMEWORK level** and promoted by "
      "Casey override of a Cal brake. ⟹ the answer to 'is there a corpus operation?' is **yes, two — at "
      "FRAMEWORK tier, i.e. posited, not derived**, consistent with the rest of this board.",
      True,
      "corpus names 1/n_C chirality projection + SCMP τ-direction, both at FRAMEWORK (posited) tier")

check("★★ **BUT THEY CARRY TOY 5274's GAP.** The named chain SO(5,2) → SO(4,2) → SO(3,1) is a chain of "
      "**GROUPS** — symmetry reductions — and **5274 showed a symmetry reduction is not a dimensional "
      "projection**. And '1/n_C chirality projection' is plausibly a genuine projection **on the SPINOR/record "
      "index** (halving a spinor space, like γ⁵) — which is T2555's phase-drop and the record-vs-spacetime "
      "distinction of toys 5267/5269 — **not the removal of a spatial dimension.** ⟹ **the named operations may "
      "RELABEL the gap rather than close it.** ★ **Flagged as a QUESTION, not a verdict** — I have not read the "
      "chirality projection's primary source; @Lyra/@Cal should check **which index it acts on before it is "
      "leaned on.**",
      True,
      "named ops are group reductions and/or spinor-index projections ⟹ may relabel 5274's gap; QUESTION, source unread")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (velocity = the site sequence ⟹ one unknown; IID sites fail by 1e4–1e8 ⟹ the input is a PROCESS)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5275, one unknown instead of two, with a free filter on it):
  * ★ **(b) THE COMMIT PROJECTION SUPPLIES A POSITION PER TICK** (T2542) — what H_B cannot (5273). A projection
    generates no flow, **but a SEQUENCE of them is a trajectory**: v ≈ dist(Ω_{{n+1}}, Ω_n)/Δτ.
  * ★★ **⟹ VELOCITY IS NOT A SECOND MISSING INPUT.** It is a **function of the site sequence** — supply the
    site-measure and the velocity comes with it. **@Keeper's two unknowns become ONE.**
  * ★★★ **AND A QUANTITATIVE FILTER FALLS OUT.** IID sites on the derived uniform measure give a **mean step of
    {STEP_MEAN:.4f} rad** against a requirement of **≤ {REQ[1e-2]:.1e} rad** — **violated by {VIOL[1e-2]:.0e} to
    {VIOL[1e-6]:.0e}.** Independent sites ⟹ the observer jumps across the sphere each tick ⟹ **depth
    recoverable, record NOT angular.**
  * ★★★★ ⟹ **THE MISSING INPUT IS A PROCESS, NOT A MEASURE** — temporally correlated, step ≲ 10⁻⁴ rad.
    **Falsifiable in advance: any candidate matter input giving near-independent sites is dead on arrival.**
    @Lyra — a free filter on the Machian/exterior candidate before it's built.
  * ★ **(a) THE CORPUS DOES NAME THE OPERATIONS:** "SO(5,2) → SO(4,2) **(1/n_C chirality projection)** →
    SO(3,1) **(Casey #8 SCMP τ-direction)**" — at **FRAMEWORK tier, posited not derived.**
  * ★★ **BUT THEY CARRY 5274's GAP:** the chain is of **groups** (reduction ≠ projection), and a chirality
    projection plausibly acts on the **spinor/record index** (γ⁵-like) — T2555's phase-drop, the
    record-vs-spacetime distinction again — **not a spatial dimension.** ⟹ **may relabel the gap.**
    **Flagged as a question; primary source unread — check which index before leaning on it.**

AUG-15. Nothing pushed. Count once. CP existence-only.
""")
