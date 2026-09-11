---
title: "Lecture 6 — Three Generations, at the Floor"
spine: "D_IV⁵: QM, GR and the SM — the derivations, tiered"
author: "Keeper, for Casey Koons and the team"
date: "2026-09-11 — v0.1"
sources: "The 3-vs-2 asymmetry theorem (Lyra v3 item 5, Elie 5494 as second CI; rubric 2026-08-24); the internal-SM paper (three generations as rank+1, Lecture 5); K1827/K1828 with toys 5497/5498 and Grace's cross half (the thermal-generations mechanism refuted at the order level); the W3-floor theorem (Lane P, 2026-08-26, two-CI toy 5502; Cal Section 772 scoping); K1812 (the FK Pochhammer ladder closed three ways; F820) with K1749-B (the one named untested alternative); K1830 (the three External-3 at-floor closures — Koide's source, mixing values, mass tower — with reopen conditions named); Elie 5454 (the ν axis is uniformly under-hierarchical: 22.96 demanded, [1.79, 2.78] delivered)"
tier_line: "DERIVED: three generations as the rank+1 strata of one Jordan invariant — the rank read twice; m₁ = 0 and the ν_R pair's degeneracy. FIRED AND LOST (certified): the thermal ordering mechanism — two independent computations, identical exact exponents (0, 9/4, 25/4) = ν², the strict reverse of the required order. FLOORED (theorems, reopen conditions named): every measure_int-derived weight on the strata (0-or-∞ by construction); the FK Pochhammer ladder (144/144 fail on the forced odd grid); Koide's source (uniformly under-hierarchical norms); the mass tower as a patchwork. INPUT: the charged-lepton and quark masses. NOT CLAIMED: any mass value; 'the mass tower is derived'."
---

# Lecture 6 — Three Generations, at the Floor

## The question

Why three copies of everything — and why can we not yet say how heavy each is?

Every fermion in the Standard Model comes in three generations that differ only in mass, and the masses span five orders of magnitude with no pattern anyone has derived. A theory that produced the count and the masses together would have done something no theory has done. This program produced the count. It then tried, seriously and with the numbers hidden, to produce the masses — and failed in a way that turned into a theorem about *why* that family of attempts must fail. This lecture tells both halves in the same voice, because the second is the program's best evidence that the first is not a coincidence dressed up.

## For the reader in a hurry

Count the ways the shape's boundary can be approached: there are three, and there are three however you count them, because the count is the shape's rank plus one. That is why there are three generations. Now ask the shape which generation is heaviest and by how much. We tried the natural mechanism — the generations "freeze out" in a thermal order — and computed it two ways with the answer hidden; it came out exactly backwards. Then we proved that *no* mechanism of that whole family can work, because the very thing that defines the three levels makes every such weight either zero or infinite on them. So the count is derived and the masses sit at a floor: closed by a theorem, reopenable only by a kind of idea we can name.

## The count is the rank, read twice

The object has rank two. Rank is the number of independent directions to the boundary, and it shows up in two different countings of the same Jordan invariant.

Index the states by *orbit*: which orbit of the structure group they lie on. Orbit-indexed quantities are invariant under the automorphism-vector (AV) action and get swept along it; there are $r + 1 = 3$ orbit classes — the interior and the two boundary strata, the second of which is the Šilov boundary.

Index them instead by *frame*: the position relative to a Jordan frame. Frame-indexed quantities are Weyl-covariant and exactly degenerate under the Weyl group; there are $r = 2$ frame slots.

So the same invariant, read as an orbit count, gives three; read as a frame count, gives two. **Three generations and two weak-isospin slots are the rank, read twice** (the 3-vs-2 asymmetry theorem; two CIs, riders attached). The asymmetry is not a coincidence between two unrelated integers; it is $r + 1$ versus $r$ for $r = 2$. Lecture 5's theorem carries the same count as "three generations as rank$+1$ strata," and the two are the same statement.

Two corollaries come with it. The lightest neutrino is massless, $m_1 = 0$ — it *is* the vacuum stratum, not merely a light state on it. And the $\nu_R$ pair's thermal degeneracy follows from the same strata structure. (The physical map from strata to named particles stays the banked identification F588 — a seam we audited and left labelled.)

Lecture 2's caveat travels here too: once $a = 3$ fixes the domain, rank $2$ follows, so "three generations equal rank plus one" is a *check that passes*, not a second leg for the object's selection. It is a derivation *from* the object, not evidence *for* it.

## The negative, told as the result it is

If the three generations are three strata, the natural mechanism for their mass order is thermal: the strata freeze out in sequence, and the first to freeze is heaviest. The program formulated this as a zero-knob condition — the freeze-out order is the order of leadership-switch times, which is reparametrisation-invariant, so no map from the theory's parameter to temperature is owed — and pre-registered the required order: Šilov-first.

Then two of us computed the exponents independently, numbers unseen (K1827/K1828; toys 5497/5498 and Grace's cross half). The results were identical to the digit: $E = (0,\ 9/4,\ 25/4) = \nu^2$ for the three strata, under both weight conventions. And that is the **exact strict reverse** of the frozen order. The mechanism did not miss by a little; it produced the opposite of what it had to produce, on first contact with numbers, after surviving every prior audit.

We regard this as a result. It could have succeeded — the order was frozen before the computation, the computation was blind, the two halves agreed — and it did not. A theory that can fail this way is a theory whose successes mean something.

## The floor theorem: why the whole family fails

The refutation raised the obvious question: was it *this* weight, or *any* weight of its kind? The answer is a theorem (Lane P, 2026-08-26; two CIs, toy 5502), and it is the reason this lecture's title says *floor*.

The three strata are *defined* by the degeneration of the invariant measure: the Pochhammer zeros of the Faraut–Korányi measure *are* the strata. So any channel weight derived from that measure is, on the strata, structurally either $0$ or $\infty$ — the $\Gamma_\Omega$ poles sit at $\nu = 3/2$ and $0$, and the AV formal degree there is $w_\tau = 0$. There is no measure-derived weight that is finite and non-trivial on the very levels it would have to order. Not "we have not found the weight" — *no weight of this family exists*.

That is what a floor is: a theorem that closes a class, with the door named. Here the door is a weight **not** derived from the invariant measure. One candidate is drafted and held — the Šilov surface measure, finite exactly where the interior measure dies — and it runs only under a new pre-registration, on Casey's word.

## Three more closures with their doors

**The Pochhammer ladder** (K1812). The lepton masses were once read as a ladder of Faraut–Korányi Pochhammer symbols. Closed three ways: a curvature-sign theorem composed with a parity forcing (F820) gives $144/144$ failures on the forced odd grid — the flattest allowed triple still over by $2.86\times$; the "lepton index" $\nu_{\text{lep}} = 12.888$ is not forced and not a number of the theory; the zero-parameter residue test dies on the $(\mu,\tau)$ pair at $42$ against $16.8$. F820 is what *restored* falsifiability — the continuum family fits anything, the forced discrete set fits nothing. What survives as a boundary: **the quarks are equally spaced on the ladder and the leptons cannot be.** One named alternative was never tested (K1749-B): norms taken at the two degenerate addresses on their *own* degenerate measures — a spread source no analytic family can see. It stays named, not worked.

**Koide's relation** (K1830). $Q = 2/3$ for the charged leptons is one of the prettiest empirical facts in the sector, and the program's overlap-norm route to it is closed permanently: the norms at the forced addresses are *uniformly under-hierarchical* — the relation demands a max/min amplitude ratio of $22.96$, and every finite form delivers between $1.79$ and $2.78$, all eight evaluations missing high (Elie 5454). Reopens only on a non-overlap-norm object class. One further honesty: the $45°$ in Koide's parametrisation (which is $Q = 2/3$ itself) is *free* — any right-shaped amplitude yields it — so matching it proves nothing; the only informative angle is the $\sim 12.7°$ that says *which* masses, and that is read off the data.

**The mass tower** as a whole (K1830): a patchwork of identifications, each at its own tier, no unifying slope mechanism. Reopens on one.

## Tier line

- **Derived:** the count, as the rank read twice; $m_1 = 0$; the $\nu_R$ degeneracy.
- **Fired and lost, certified:** the thermal ordering.
- **Floored, doors named:** measure-derived weights (door: a non-measure weight — the Šilov surface measure, held); the Pochhammer ladder (door: degenerate-address norms, K1749-B); Koide's source (door: a non-overlap-norm class); the tower (door: a unifying slope).
- **Input:** the masses.
- **Not claimed:** any mass value; that the tower is derived; that the count is evidence for the object.

## What would make this lecture wrong

A fourth generation would falsify the count outright, and it is excluded to high confidence by the $Z$ width — a falsifier of exactly the kind we prefer, sharp and not ours to tune. A massive lightest neutrino would break the corollary. The floors cannot be falsified; they can be *opened*, and each door above says by what.

## Where to look

Lyra v3 item 5 and Elie 5494; K1827/K1828 with 5497/5498; the Lane P theorem entry (rubric, 2026-08-26) and toy 5502; K1812, K1749-B; K1830 for the three closures with their reopen conditions; Elie 5454; K1689 for the free-angle note on Koide.
