# Substrate Non-Algebraic Interfaces Position Document v0.1

**Author**: Keeper
**Filed**: 2026-05-22 Friday 08:44 EDT (FAST CADENCE)
**Status**: Closes Wednesday substrate review owed #3 (per Task #229)

---

## The question

T719 Observable Closure says every BST observable lives in Q-bar(BST primaries)[π]. This is the *algebraic-π-closure* of BST observables.

**Question**: are there *non-algebraic* interfaces where substrate operates outside Q-bar(primaries)[π]? Where would they appear, and how should we recognize them?

## Three candidate non-algebraic interfaces

### Interface 1: γ (Euler-Mascheroni)

γ is **limit-undecidable** — its classification as algebraic vs transcendental is currently open in mathematics itself. Per Casey's "γ as trajectory + catastrophe" framing (memory feedback_gamma_trajectory.md):

- γ is a *trajectory* not a *number*: γ = lim_{n→∞}(H_n − ln n)
- The limit operation destroys trajectory information (lossy compression)
- γ may sit on the algebraic/transcendental boundary as a fold catastrophe

**Substrate-engineering reading**: γ is the boundary at which substrate's *limit-taking interface* yields lossy results. The substrate operates via discrete commitment-cycles (per SWPP); γ is what you get when you formally take a limit that the substrate doesn't natively compute.

**BST observables involving γ**: thermodynamic constants, certain spectral asymptotics, Selberg zeta normalizations. These would be **partial-algebraic** observables — algebraic up to a γ correction.

### Interface 2: ζ(2k+1) (odd zeta values)

ζ(2) = π²/6 is algebraic in π. ζ(4), ζ(6), ζ(8), ... all algebraic in π.

But ζ(3), ζ(5), ζ(7), ... are **conjecturally transcendental and algebraically independent** from π. Apéry proved ζ(3) irrational; nothing else known.

**Substrate-engineering reading**: even-zeta values are *substrate-internal* (algebraic in π). Odd-zeta values appear when substrate interfaces with **non-substrate temporal structure** — e.g., experimental observables that don't reduce to substrate's commitment-cycle.

**BST observables involving ζ(2k+1)**: certain QFT loop corrections, statistical ensemble averages. T1930 confirms ζ(g)·something ≈ specific particle property — but g=7 puts us in odd-zeta land.

### Interface 3: Continued-fraction-algebraic numbers (non-quadratic irrationals)

Quadratic irrationals (√d) have eventually-periodic continued fractions. Higher-degree algebraic numbers do not.

**Substrate-engineering reading**: substrate's K75 Stark anchor uses class-number-1 imaginary-quadratic fields Q(√−d) for d ∈ {3, 7, 11, ...}. These are *substrate-canonical*. Higher-degree algebraic interfaces (cubic, quartic) would be **rare-anchor** observables that need extra substrate scaffolding.

**Test**: do BST predictions ever require degree-3+ algebraic numbers? If not, this is structural evidence for substrate's quadratic-irrational preference.

## The three-interface taxonomy

| Interface | Algebraic? | BST role | Test |
|-----------|-----------|----------|------|
| 1. γ | undecidable | thermodynamic/asymptotic boundary | look for γ in BST D-tier |
| 2. ζ(2k+1) | conjecturally transcendental | temporal-experimental boundary | look for ζ(odd) in BST D-tier |
| 3. degree≥3 algebraic | algebraic but not quadratic | rare-anchor scaffolding | look for cubic+ numbers in BST D-tier |

## Substrate Closure check (per K137 / Substrate Closure Principle)

Substrate Closure says **substrate is operationally closed; no external simulator**. The three non-algebraic interfaces above are *not* external simulator referents — they are **internal boundaries** where substrate's native algebraic computation produces lossy results.

This is **consistent** with Substrate Closure: the substrate doesn't reach for external infinity; it produces *partial* outputs at its boundary interfaces, and we should expect observable correction terms in γ, ζ(odd), or higher-degree algebraic numbers to mark those boundaries.

## Cross-Cartan extension (per K141 / 3306× empirical)

If we test the three-interface taxonomy on alt-HSDs (D_I, D_II, D_III):
- D_I should have *different* non-algebraic interface set (different Bergman kernel structure)
- D_IV⁵ specifically maps γ to thermodynamic boundary, ζ(2k+1) to temporal, etc.

If alt-HSDs map non-algebraic interfaces *differently* and BST observables match the D_IV⁵ specific mapping (not alt-HSD), that's additional substrate-uniqueness evidence.

## Pending verification

1. **Catalog scan**: which BST D-tier observables contain γ? ζ(2k+1)? degree-3+ algebraic numbers?
2. **Lyra theorem**: T2456 candidate — "BST observables interface non-algebraic structure only at three boundary types"
3. **Strong-Uniqueness criterion**: if alt-HSDs fail to map the three-interface taxonomy correctly, this becomes **C18** (RIGOROUSLY CLOSED candidate)

## Status

**Substrate Non-Algebraic Interfaces Position v0.1 filed Friday 08:44 EDT (FAST CADENCE).** Closes Wednesday substrate review owed #3. Six-interface cross-cartography map remains owed (Task #233) — that's the broader synthesis.

— Keeper, position v0.1 Friday 08:44 EDT (FAST CADENCE)
