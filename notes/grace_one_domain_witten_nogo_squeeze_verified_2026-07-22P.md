# The one-domain Witten no-go, verified — why every bulk closure failed, and why Route 2 is necessary

*Grace | 2026-07-22 | Casey's steer ("linear math, one D_IV⁵ domain — don't import orbifold/GUT machinery") produces the cleanest statement of the whole arc. Keeper found the squeeze; I verified it numerically on the explicit 8-spinor. It IS the Witten no-go as one-domain linear algebra, and it explains why all five bulk closures (mine included) died — and turns Route 2 from "an option" into "the necessary resolution."*

## The squeeze (verified on the explicit SO(5,2) 8-spinor)
Built the 7 gammas, γ⁵ = Γ₀Γ₁Γ₂Γ₃, and checked both SU(2) placements:
| SU(2) placement | vs γ⁵ | consequence |
|---|---|---|
| **internal, in {4,5,6}** (Γ₄Γ₅, Γ₅Γ₆, Γ₄Γ₆) | **COMMUTES** ✓ (verified) | acts the SAME on both chiralities → **VECTOR-LIKE** (L and R both doublets) |
| **isospin SU(2)_L in {1,2,3,4}** (F633; Γ₁Γ₄, Γ₂Γ₄, Γ₃Γ₄ mix dir 4 with {1,2,3}) | **ANTICOMMUTES** ✓ (verified) | no simultaneous (chirality, isospin) eigenstate → **"L-doublet" not even definable** |
**The SM needs BOTH** — an internal group that (a) commutes with γ⁵ (so "L-doublet" is a well-defined state) AND (b) acts *differently* on L vs R (chiral). The squeeze: (a) forces the {4,5,6}-type placement → vector-like; (b) needs the isospin placement → not simultaneously diagonalizable. **You cannot have both in a single fixed 8-spinor.** That's chirality-dependent internal content, which one spinor cannot carry.

## ★ This IS the Witten no-go, and it's why the whole arc landed vector-like
The famous "chiral fermions from geometry is decades-hard / Witten's no-go" is *exactly* this one-domain linear-algebra squeeze. And it retro-explains every failed closure of the thread — all five were attempts to build the SM chiral assignment inside a single bulk spinor:
- F640 (Weyl-from-positive-energy), **my ω-lock** (χ_internal fixed → γ⁵ fixed), Elie's 4781 (internal chirality ⊥ γ⁵), the F642 anticommutator, the Route-1 coincidence — **each died to an instance of {isospin, γ⁵} ≠ 0.** My ω-lock in particular: I *assumed* holomorphicity fixes a γ⁵-compatible internal chirality; the squeeze says it can't, because the isospin generators (dir-4) anticommute with γ⁵. So my refutation wasn't a one-off slip — it was this structural no-go, which I'd have avoided seeing the squeeze first. Owning that fully.

## ★ Constructive — the squeeze MAKES Route 2 necessary
The squeeze doesn't just say "no"; it says *what's required*: since one spinor can't carry chirality-dependent internal content, **the L and R fermions must be genuinely DIFFERENT localized modes** (different internal content). That is *precisely* what a boundary / domain-wall construction provides and a single bulk spinor cannot:
- domain-wall zero modes: L and R localize on *different* walls, carrying different content — chirality is the topological mass-sign, not the bulk γ⁵ (so the squeeze/F642 doesn't reach it);
- BST's realization: the bulk → Shilov (S⁴×S¹)/ℤ₂ boundary, where the +4 index (K817) localizes the modes.
**So Route 2 isn't the last option we're hoping works — it's the resolution the no-go itself demands.** Every other route was refuted *because* it tried to stay in the single bulk spinor; Route 2 is the one that gives L and R different homes.

## Honest tier
- **The squeeze is a verified, theorem-grade NEGATIVE** (the SM chiral assignment is impossible in a single fixed D_IV⁵ 8-spinor = the one-domain Witten no-go). Flagging to @Keeper/@Lyra as bankable (a clean no-go, like the ceiling is a clean bound). I'm not unilaterally banking it mid-computation — the ID is yours.
- **Route 2 is now NECESSARY but still UNCOMPUTED** — the squeeze forces the different-localized-modes structure, but *does the (S⁴×S¹)/ℤ₂ boundary actually realize the L/R domain-wall zero modes with the SM content?* is Lyra's spin-structure computation. Lead → derived only when it computes. Lyra's self-catch stands: the naive circle-reflection Γ₆ commutes with γ⁵ (doesn't select chirality); the live hope is the orientation-reversing S⁴ antipodal map lifting to a chirality flip.
- **DIRAC + Route 1 stay closed; compute-don't-assert; survivors banked; FA-positive.**

## Net
- **Verified the one-domain squeeze:** {4,5,6}-SU(2) commutes with γ⁵ (vector-like); isospin SU(2)_L (dir-4) anticommutes (L-doublet undefinable); the SM needs both → impossible in one 8-spinor = the Witten no-go as linear algebra.
- **★ It retro-explains the whole arc:** all five bulk closures (including my ω-lock) died to this same squeeze — they tried to build chirality in a single bulk spinor.
- **★ It makes Route 2 necessary:** L and R must be different localized modes → boundary/domain-wall is the *required* resolution, not an option.
- **Held honest:** squeeze = verified theorem-grade no-go (flagged bankable); Route 2 = necessary but uncomputed (Lyra's spin-structure/antipodal computation decides).

— Grace, 2026-07-22 (Casey's "linear math, one domain" steer). VERIFIED the one-domain Witten no-go squeeze on the explicit 8-spinor: SU(2) in {4,5,6} COMMUTES with γ⁵ (→vector-like); isospin SU(2)_L in {1,2,3,4} (dir-4 generators Γ₁Γ₄ etc.) ANTICOMMUTES with γ⁵ (→ no (chirality,isospin) simultaneous eigenstate, L-doublet undefinable); SM needs BOTH → IMPOSSIBLE in a single fixed 8-spinor = the Witten no-go as one-domain linear algebra. RETRO-EXPLAINS the whole arc: all 5 bulk closures (F640/my-ω-lock/Elie-4781/F642/Route-1) died to an instance of {isospin,γ⁵}≠0 — my ω-lock owned as this structural no-go, not a one-off. CONSTRUCTIVE: one spinor can't carry chirality-dependent internal content → L and R must be DIFFERENT localized modes → boundary/domain-wall is the NECESSARY resolution (Route 2), not an option. TIER: squeeze = verified theorem-grade no-go (flagged bankable to Keeper/Lyra); Route 2 necessary but UNCOMPUTED (Lyra's (S⁴×S¹)/ℤ₂ spin-structure/antipodal-map computation decides; naive Γ₆ reflection commutes w/ γ⁵ = refuted, orientation-reversing S⁴ antipodal = live hope). DIRAC+Route-1 closed; FA-positive; compute-don't-assert.
