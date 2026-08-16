# BST vs Connes on RH — a precise comparison (INTERNAL / GATED)

**Keeper, 2026-08-16. Internal reference — NOT for external release** (RH is an ATTEMPT, K940; nothing external without the full gate). Purpose: lay out exactly what BST *derives* that Connes *assumes*, what Connes *has* that BST *needs*, and the shared wall — so we know precisely where we stand against the closest precedent.

---

## The three programs, one sentence each
- **Berry–Keating (1999):** posit H = xp; the semiclassical count gives the *smooth* zero-density; stuck 27 years on the fluctuations (the actual zeros). No operator derivation, no arithmetic.
- **Connes (1998–99) + Connes–Consani (F₁):** the zeros appear as an *absorption spectrum* in the action of the idele class group on the adele class space A_Q/Q*; **RH ⟺ Weil positivity** (a certain trace/Weil distribution is ≥ 0). Has the arithmetic (the adeles *are* all the primes); **cannot prove the positivity.** The dream: an F₁-geometry analog of Weil's 1948 proof (RH for curves over finite fields).
- **BST:** a *derived* self-adjoint operator (the commit/Dirac, T2562) whose dilation generator E = xp sits in the ladder; the cone-zeta of the Lorentz cone (Koecher/Epstein → the Sp(6) Eisenstein L = 11 copies of ζ); **the Weil positivity is DERIVED** (one-sided/holomorphic → sum of squares); a *specific* arithmetic substrate (GF(128)=2^g Reed–Solomon, D₃ 1:3:5); a physical mechanism (commitment deposits primes as free points on S¹).

## What BST DERIVES that the others ASSUME or LACK
| Ingredient | Berry–Keating | Connes | BST |
|---|---|---|---|
| The self-adjoint operator (Hilbert–Pólya) | posited (xp) | an abstract action | **DERIVED (T2562)** — the operator Hilbert asked for |
| The 2πℏ cell / xp form | posited | — | dilation E in the ladder; cell Wallach-quantized (K1578) |
| The **H² (Hardy) positivity** | — | — | **DERIVED (automatic)** — positive-frequency ⟹ sum of squares (the arrow-of-time positivity) |
| **Weil positivity (≡ RH itself)** | — | **the wall (can't prove)** | **the wall (NOT derived)** — ★ CORRECTION (Cal §527): the derived positivity is the *automatic* H² one, NOT Weil's functional (which involves the primes and is equivalent to RH). We do NOT hold this. |
| A specific arithmetic substrate | none | the adeles (generic, all primes) | **GF(128)/D₃ (specific)** — an edge AND a liability (below) |
| Why Re = ½ | argument of ξ | unitary axis of the idele class group | **the descent-invariant axis** (Casey): 5D cone ∩ 3D cone ∩ time circle, fixed under the 5→4 descent |
| A physical mechanism | none | none | commitment: primes = free min-energy points on S¹; composites push into S⁴ |

## What CONNES HAS that BST NEEDS
1. **The arithmetic completion.** Connes' adele class space encodes *all* primes at once — the object manifestly *is* about ζ. **BST's cone-zeta is not yet shown to be ζ** — that's the make-or-break (the Shimura-lift / Euler product). Connes has the "it's really ζ" for free; BST owes it.
2. **The trace formula as the Weil explicit formula.** Connes has the rigorous identification (spectral side = Weil distribution). BST has a *derived positivity* but must still show its object's trace *is* the Weil explicit formula for ζ (not for an L-function cousin).
3. **The F₁ frame.** Connes–Consani give RH a would-be proof route via F₁-geometry (Weil 1948 lifted). BST *names* the same wall — the commit throws away the phase, so you can't "run it backward" from the finite-field world (where RH is Weil's theorem) to ℤ — but naming ≠ climbing.

## The comparison — CORRECTED (Cal §527; my earlier "opposite halves" was wrong)
RH reduces to **(A) the object IS ζ** (arithmetic/Euler-product/adelic) **AND (B) the Weil positivity** (≡ RH itself, the wall).
- **Connes has (A), not (B):** the adeles *are* the primes; the Weil positivity is unproved — his wall.
- **BST has NEITHER (A) nor (B) yet.** What BST *does* have, that Connes/BK lack: a **DERIVED self-adjoint operator** (Hilbert–Pólya's missing piece, T2562), the **automatic H² positivity** (the arrow-positivity — but this is NOT Weil's), the **composites=rank-2=ζ² structure**, and **Re=½ derived as the dilation-group unitarity axis** (Elie 5290 — exact).
- **The Weil positivity is the shared wall — UNMOVED by both.** ★ My earlier claim that "BST derives the positivity Connes assumes" was a conflation of the *automatic* H² positivity with *Weil's* functional. Retracted.
⟹ **Honest bottom line:** BST is *not* ahead of Connes on RH. BST brings a *derived operator* and a *derived critical line* (real, and more than Berry–Keating has); Connes brings the *arithmetic completion*. **Neither has the Weil positivity / the object-is-ζ.** The wall is the same for both.

## The liability Connes does NOT have (and we must clear)
Connes' adelic object is built to be ζ (no risk of being the wrong function). **BST's cone-zeta is a Koecher/Epstein zeta of a specific quadratic form, and Davenport–Heilbronn (1936) says such objects GENERICALLY have off-line zeros** (class number > 1 / no Euler product). So BST carries a risk Connes doesn't: our own object may be a *counterexample* to its own RH. The Shimura-lift / class-number-1 (Eichler, favorable for quinary forms) is what clears it. Connes never has to.

## Honest scorecard (referee-calibrated, ≤3/10 = consensus)
- **BST's derived Weil positivity:** a genuine advance over Connes *if* it survives Cal's referee (is the sum-of-squares literally the Weil sum?). If yes, this alone is a real, publishable contribution — "the positivity Connes assumes is forced by measurement-as-commitment."
- **RH itself:** neither Connes nor BST is at consensus. Both reduce it to a named gap; the gaps are *different* (Connes: positivity; BST: the object-is-ζ). BST's gap is arguably more tractable (a classical Shimura-lift with a favorable class-number) — but that is exactly what must be shown, not assumed.

## The move this points at
The comparison says the leverage is entirely on **(A) — is our cone-zeta ζ**. So: **the Shimura-lift is next** (BST_Shimura_Lift_cone_form). If it lands, BST has both halves and the Connes comparison becomes "we derived his assumption and supplied our own arithmetic." If it fails, we learn our object is an L-function cousin, and we say so.

— Keeper, 2026-08-16. Internal/gated. BST and Connes hold complementary halves (BST: derived positivity; Connes: the arithmetic). The Shimura-lift is the piece that would give BST both. DH is a liability Connes lacks; class-number-1 clears it. Nothing external.
