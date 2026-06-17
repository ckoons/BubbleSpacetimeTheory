---
title: "F119 — HONEST NEGATIVE: the tau -sqrt(pi) correction does NOT derive from the heat-kernel Weyl frame; the pi-powers don't line up. Walking back last night's sqrt(pi)/half-derivative/mean-curvature enthusiasm after doing the actual d=3 heat-kernel bookkeeping. CLAIM TESTED (from the 2026-06-13 night conversation): the tau's missing -1.77 correction = the g^1 boundary mean-curvature heat-kernel term = -sqrt(pi) (a half-derivative, order 1/2). COMPUTATION: the pi-power of each d=3 Weyl coefficient C_k=(4pi)^(-3/2)/Gamma((3-k)/2+1): g^3 volume = pi^-2; g^2 surface = pi^(-3/2); g^1 MEAN CURVATURE = pi^-2 (NOT sqrt(pi)!); g^0 const = pi^(-3/2). VERDICT: -sqrt(pi)=-pi^(+1/2) is NOT the natural pi-power of ANY d=3 Weyl coefficient. The g^1 mean-curvature term carries pi^-2, not sqrt(pi); the half-integer terms are g^2 and g^0 carrying pi^(-3/2), not pi^(+1/2). Last night's specific claim ('g^1 mean curvature = the sqrt(pi) half-derivative') is WRONG. Getting +sqrt(pi) would require the geometric integral to supply pi^2 (an S^4-like factor) against a g^0 term, which a 3D region's 2-surface boundary does not provide -> unforced pi-compensation. So the -1.77 does NOT derive as -sqrt(pi). CONFIRMS F114's 'form-analogy' caution: tau-as-d=3-Weyl-count was never a clean heat-kernel object, now the pi-powers say so explicitly. sqrt(pi)=1.7725 vs gap 1.7717 stays a NUMERICAL near-miss; the gap is 1.77+/-0.23 (13% experimental from m_tau +/-0.12 MeV), so the target can't distinguish sqrt(pi) from 16/9 from 7/4 anyway. CONTRAST with F118 (muon weighting DID derive cleanly via concentration=density/volume): the muon is a BOUNDARY object where concentration=density/volume is exact; the tau is a BULK object whose subleading structure the Weyl frame doesn't capture -> the tau may need a different frame, not a sqrt(pi) patch. STRICT: this is an HONEST NEGATIVE (the clean derivation fails; NOT an absolute impossibility -- unforced pi-compensation could force-fit it, which is exactly what we DON'T do). Tau stays OPEN. Casey's sqrt(pi) instinct was worth testing (had a TYPE, unlike 16/9) but the type doesn't survive the bookkeeping. Count stays HONESTLY 2."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-14 Sunday 07:45 EDT"
status: "v0.1 -- testing the tau -sqrt(pi) from the 6/13 night conversation. NEGATIVE: d=3 Weyl coefficient pi-powers are g^3:pi^-2, g^2:pi^(-3/2), g^1(mean curv):pi^-2, g^0:pi^(-3/2). NONE is pi^(+1/2)=sqrt(pi). Last night's 'g^1 mean curvature = sqrt(pi) half-derivative' is WRONG (g^1 carries pi^-2). -sqrt(pi) doesn't derive without unforced pi-compensation. Confirms F114 form-analogy. sqrt(pi) stays numerical near-miss to a 1.77+/-0.23 (13%) gap that can't distinguish it from 16/9/7/4. CONTRAST: muon (F118) DID derive (boundary, concentration=density/vol exact); tau is BULK, Weyl frame doesn't capture subleading -> needs different frame. HONEST NEGATIVE; tau OPEN; count 2."
---

# F119 — The tau -sqrt(pi) does not derive: the heat-kernel pi-powers don't line up

Casey said *continue*. The next link in the chain (from the 2026-06-13 night conversation) was the tau's `-1.77 ~ -sqrt(pi)` correction, claimed to be the `g^1` boundary mean-curvature heat-kernel term (a half-derivative). I owed it the actual bookkeeping before believing it. It does not hold.

## The test

`d=3` Weyl count: `N(lambda) ~ sum_k C_k lambda^((3-k)/2)`, `C_k = a_k (4pi)^(-3/2)/Gamma((3-k)/2+1)`, with `lambda = g^2` so term `k` is `g^(3-k)`. The pi-power of each coefficient:

| term | geometry | pi-power |
|---|---|---|
| `g^3` | volume | `pi^-2` |
| `g^2` | surface | `pi^(-3/2)` |
| `g^1` | **mean curvature** `∫H` | `pi^-2` |
| `g^0` | Euler/const | `pi^(-3/2)` |

## The verdict

`-sqrt(pi) = -pi^(+1/2)` is **not** the natural pi-power of any `d=3` Weyl coefficient. Specifically:
- Last night's claim that the `g^1` mean-curvature term is the `sqrt(pi)` half-derivative is **wrong**: the `g^1` term carries `pi^-2`.
- The half-integer terms are `g^2` and `g^0`, and they carry `pi^(-3/2)`, not `pi^(+1/2)`.
- Forcing a `+sqrt(pi)` would require the geometric integral to supply a `pi^2` (an `S^4`-like factor) against a `g^0` term -- which a 3D region's 2-surface boundary does not provide. That's unforced pi-compensation.

So the `-1.77` correction does **not** derive as `-sqrt(pi)`. This **confirms F114's "form-analogy" caution**: the tau-as-`d=3`-Weyl-count was never a clean heat-kernel object, and the pi-powers now say so explicitly. `sqrt(pi) = 1.7725` vs the gap `1.7717` stays a **numerical near-miss** -- and the gap is `1.77 +/- 0.23` (13% experimental, from `m_tau +/- 0.12 MeV`), so the target itself can't distinguish `sqrt(pi)` from `16/9` from `7/4`.

## Why the muon closed and the tau didn't

The contrast with F118 (same morning) is the lesson:
- **Muon = boundary object.** The concentration = density/volume picture is *exact* there, so the weighting derived cleanly (F118).
- **Tau = bulk object.** Its subleading structure is not captured by the `d=3` Weyl/heat-kernel frame -- the pi-powers don't even allow the `sqrt(pi)` the gap suggested. The tau likely needs a **different frame**, not a `sqrt(pi)` patch.

## Strict tiering

- **HONEST NEGATIVE:** the clean derivation of `-sqrt(pi)` fails (pi-powers don't line up). This is not an absolute impossibility -- unforced pi-compensation could force-fit it -- which is exactly what we do NOT do.
- **Casey's `sqrt(pi)` instinct** was worth testing: it had a *type* (`sqrt(pi)`, half-derivative) that `16/9` lacked. But the type doesn't survive the bookkeeping. Tested, not assumed; reported, not dressed.
- Tau stays **OPEN** (needs a different frame). Count stays **HONESTLY 2**.

## Closure

Continuing the chain meant testing the tau `-sqrt(pi)`, and the actual `d=3` heat-kernel bookkeeping kills it: no Weyl coefficient carries `pi^(+1/2)`, the `g^1` mean-curvature term I'd pinned it on carries `pi^-2`, and forcing `sqrt(pi)` needs unforced pi-compensation. That confirms F114's form-analogy verdict and leaves the tau genuinely open -- it is a bulk object the Weyl frame doesn't capture, and likely needs a different treatment than the muon's boundary concentration. The morning splits cleanly: the muon weighting derived (F118, candidate count->3); the tau did not (F119, open). One close, one honest wall. Count stays 2.

@Casey - continuing meant testing your sqrt(pi), and I have to report it doesn't derive. The d=3 Weyl coefficients carry pi^-2 (g^3, g^1) and pi^(-3/2) (g^2, g^0) -- NONE carries pi^(+1/2)=sqrt(pi). My claim last night that the g^1 mean-curvature term IS the sqrt(pi) half-derivative was wrong: g^1 carries pi^-2. So -1.77 ~ -sqrt(pi) stays a numerical near-miss (and the gap is 1.77+/-0.23, 13% experimental -- can't distinguish sqrt(pi) from 16/9 anyway). Your instinct had a TYPE that 16/9 lacked, which is why it was worth the test -- but the type doesn't survive. Confirms F114. The tau is a BULK object; the Weyl frame doesn't capture its subleading structure; it needs a different frame, not a sqrt(pi) patch. Contrast: the muon (F118) DID close because it's a boundary object. One close, one wall this morning. Count stays 2. @Grace - honest negative: tau -sqrt(pi) doesn't derive (pi-powers don't line up); not banked, not fished; tau open. @Keeper - ledger F119: tau -sqrt(pi) NEGATIVE (d=3 Weyl pi-powers g^3:pi^-2,g^2:pi^(-3/2),g^1:pi^-2,g^0:pi^(-3/2); none sqrt(pi); g^1 mean-curv claim retracted); confirms F114 form-analogy; tau OPEN needs different frame; count 2. @Elie - the tau is NOT a clean d=3 heat-kernel-with-boundary object (pi-powers refute it); your tau-Weyl toy would confirm the lower terms don't land sqrt(pi). Different frame needed for the bulk tau.

-- Lyra, Sun 2026-06-14 07:45 EDT (date-verified). F119: tau -sqrt(pi) does NOT derive. d=3 Weyl coeff pi-powers: g^3:pi^-2, g^2:pi^(-3/2), g^1(mean curv):pi^-2, g^0:pi^(-3/2). NONE = pi^(+1/2)=sqrt(pi). Last night's 'g^1=sqrt(pi) half-derivative' RETRACTED (g^1 is pi^-2). -sqrt(pi) needs unforced pi-compensation -> not derived. Confirms F114 form-analogy. sqrt(pi) stays numerical near-miss to 1.77+/-0.23 (13%) gap. Muon (F118) closed (boundary); tau is bulk, Weyl frame fails subleading -> needs different frame. Honest negative; tau OPEN; count 2.
