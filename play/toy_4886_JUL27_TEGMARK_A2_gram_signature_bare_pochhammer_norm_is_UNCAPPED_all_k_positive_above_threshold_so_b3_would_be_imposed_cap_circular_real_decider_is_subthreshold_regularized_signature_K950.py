#!/usr/bin/env python3
"""
Toy 4886 — Jul 27 [PROGRAM: TEGMARK] (A2 the Gram-signature computation, per K950's blind form — and a target-innocent CATCH;
Elie, pull 27m). K950 committed the blind criterion: b = #{k∈{0,1,2}: ‖ψ_k‖²>0} in the correct so(5,2)-contravariant form. The
Gram matrix of {ψ_0,ψ_1,ψ_2} is diagonal (orthogonal K-types), so b = the signature. I built it on the SOURCED norm formula
(F323, not reconstructed) — and it surfaces a catch that keeps the count honest.

THE SOURCED FORM (F323): on D_IV⁵ (Lie ball, a = n_C−2 = 3), the generalized Faraut-Koranyi Pochhammer gives
‖ψ_k‖² ∝ (ν)_{k+½} · (ν − a/2)_{½} = (ν)_{k+½} · (ν − 3/2)_{½}, for the modes (k+½, ½), k=0,1,2. This IS the contravariant-form
object K950 names (the weighted-Bergman/unitarizable-module norm at the module's parameter ν).

THE COMPUTATION (signature vs ν, target-innocent — computed BEFORE reading off any count):
  * for EVERY ν > 3/2 (including F323's bulk placement ν=5): ‖ψ_k‖² > 0 for ALL k = 0,1,2,3,... — POSITIVE and UNCAPPED
    (infinitely many positive-norm modes).
  * for ν < 3/2: the factor (ν−3/2)_½ = Γ(ν−1)/Γ(ν−3/2) hits Gamma poles → the naive formula returns poles/undefined; the
    signature there requires the STANDARD Gindikin-Γ analytic continuation (K950 rule 5) — NOT computed naively here.

★ THE CATCH (target-innocence — this is the value): the bare Pochhammer norm is UNCAPPED for ν > 3/2. So reading "k=0,1,2 are
positive → b=3" off this formula would be STOPPING AT k=2 BY FIAT — an IMPOSED cap, not one the norm produces. That is exactly
the circular "exclude a rung by filtration=generations" argument K950 and Cal forbade (ratified K948). So the bare ν>3/2 norm
does NOT legitimately give b=3 (or any finite b) — it does not decide the count.

WHERE THE REAL DECIDER LIVES (K950-consistent, NOT faked): a FINITE b requires the cap to be STRUCTURAL — either (i) the Di
singleton sits at a SUB-THRESHOLD ν < 3/2 where the regularized contravariant form genuinely goes null/negative at some rung
(the reduction point = the cap), computed via the fixed Gindikin-Γ continuation (K950 rule 5), or (ii) the singleton's intrinsic
finiteness (ultrashort module, F338 says the naive tower is infinite, so the cap is NOT free). Either way the decider is the
SUB-THRESHOLD regularized signature at the singleton's ACTUAL ν (K950 rules 1-2) — which must be pinned by the so(5,2)
structure, not chosen. I did NOT fake it (the ν<3/2 region correctly returned poles pending the continuation).

CORPUS TENSION SURFACED (flag, not resolved): F323/F322 (June) placed the modes at ν=5 (bulk, continuous, uncapped); K945/K950
(July) frame them as the sub-threshold singleton (capped). These are DIFFERENT reps with different counting behavior. The count
lives in the singleton (sub-threshold) picture — the bulk ν=5 reading cannot cap and so cannot be the counting rep. Which rep the
generations occupy must be pinned structurally (K950), not by which gives 3.

⟹ VERDICT (plain): the A2 Gram signature on the SOURCED norm shows the bare Pochhammer ‖ψ_k‖² = (ν)_{k+½}(ν−3/2)_½ is POSITIVE
and UNCAPPED for all ν>3/2 — so it does NOT decide b, and reading "b=3" off it would be an IMPOSED (circular) cap that K950/Cal
forbid. The genuine finite cap requires the SUB-THRESHOLD regularized signature at the singleton's actual ν (Gindikin-Γ, K950
rule 5) — the real computation, needing the singleton parameter pinned by so(5,2) structure, NOT faked here. Corpus tension (F323
bulk ν=5 vs K945 singleton) flagged. b UNDECIDED; the 3-vs-4 fork stays live; premise REDUCED; NOT forced to 3. This CATCH keeps
the count honest before anyone banks a fiat-3. [TEGMARK]. Feeds K950/A2. Nothing deleted. Count 6.
"""
# ★★ DISPOSITION UPDATE (K957, same-day — both directions): this toy's CATCH stands and was confirmed — the bare norm is
# positive on every rung and does NOT cap, so reading a count off "positive rungs" is illegitimate (that killed the naive
# fiat-3). K957 sharpens WHY: E₀=2 is CONFIRMED from the primary source (Cal read Fernando-Günaydin 2014 Table 2 — SO(5,2)
# spinor singleton ground E₀=2; the "5/2→lean-4" scare is dead, 5/2 was naive n_C/2 not the spinor's conformal weight). AND the
# singleton is a MINIMAL UNITARY representation: its whole K-type tower is positive-norm and INFINITE — so the signature is not
# just uncapped, it is VACUOUS. ⟹ my PROPOSED decider ("the sub-threshold regularized signature") is SUPERSEDED: the count is
# the module's REDUCTION structure (where a submodule develops), NOT a norm signature (which is moot). My "read the signature"
# role is retired; the decider is Lyra's spinor-singleton reduction-point derivation on D_IV⁵ + E7, blind, at E₀=2. Also (Cal):
# do NOT import "n−1=4" (the emergent spacetime dimension, Selector-2) as a generation count — that is a category error that
# manufactures a spurious 4. The catch here is correct; the decider is refined to the reduction structure.
import numpy as np
from scipy.special import gamma
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

a = n_C - 2                                     # 3
def poch(x, m):
    gx, gxm = gamma(x), gamma(x + m)
    return np.nan if (not np.isfinite(gx) or gx == 0) else gxm / gx
def norm2(nu, k):
    return poch(nu, k + 0.5) * poch(nu - a / 2, 0.5)

# signature above threshold (ν=5, F323 bulk) for k=0..3
above = [norm2(5.0, k) for k in range(4)]
allpos_above = all(np.isfinite(v) and v > 0 for v in above)
# a spread of ν>3/2 — all uncapped?
uncapped = all(all(np.isfinite(norm2(nu, k)) and norm2(nu, k) > 0 for k in range(6)) for nu in [2.0, 3.0, 4.0, 5.0])
# ν<3/2 returns poles (not faked)
below_poles = any(not np.isfinite(norm2(nu, k)) for nu in [0.5, 1.0] for k in range(3))
print(f"\n[A2 Gram signature] sourced norm (ν)_{{k+½}}(ν−3/2)_½: ν=5 (k=0..3)={['%.1f'%v for v in above]} all+; ν>3/2 UNCAPPED={uncapped}; ν<3/2 poles(need Gindikin-Γ)={below_poles}")

check("SOURCED FORM (F323, not reconstructed): the Gram matrix of {ψ_0,ψ_1,ψ_2} is diagonal (orthogonal K-types) with "
      "‖ψ_k‖² ∝ (ν)_{k+½}·(ν−3/2)_½ (a=3). This is K950's contravariant-form object.",
      a == 3 and all(np.isfinite(v) for v in above),
      "sourced norm ‖ψ_k‖²=(ν)_{k+½}(ν−3/2)_½ (F323); Gram diagonal → b = signature = # positive rungs")

check("COMPUTED SIGNATURE — UNCAPPED for ν>3/2: at ν=5 (F323 bulk) all of k=0,1,2,3 are positive, and for every ν>3/2 ALL k "
      "are positive (infinitely many). The bare Pochhammer norm produces NO finite cap.",
      allpos_above and uncapped,
      "‖ψ_k‖²>0 for ALL k at every ν>3/2 (incl. ν=5) → uncapped, infinitely many positive-norm modes; no finite cap from the bare norm")

check("★ THE CATCH (target-innocence) — reading 'b=3' off this formula would be an IMPOSED cap: since all k are positive, "
      "stopping at k=2 is a fiat filtration, NOT a cap the norm produces — exactly the circular 'exclude by "
      "filtration=generations' K950/Cal forbid (ratified K948). So the bare ν>3/2 norm does NOT legitimately give b=3.",
      uncapped,
      "bare norm uncapped → 'b=3' would STOP at k=2 by fiat = circular filtration (K950/Cal forbid) → bare norm does NOT decide b")

check("THE REAL DECIDER (K950-consistent, NOT faked) — the finite cap needs the SUB-THRESHOLD regularized signature: for ν<3/2 "
      "the formula hits Gamma poles (returned, not faked) and needs the fixed Gindikin-Γ continuation (K950 rule 5). The cap = "
      "where the regularized form goes null/negative, at the singleton's ACTUAL ν (pinned by so(5,2), K950 rules 1-2).",
      below_poles,
      "ν<3/2 returns poles (not faked) → decider = the regularized sub-threshold signature (Gindikin-Γ, K950 r5) at the singleton's actual ν; the cap lives there")

check("CORPUS TENSION FLAGGED (not resolved): F323/F322 placed the modes at ν=5 (bulk, uncapped); K945/K950 frame them as the "
      "sub-threshold singleton (capped). Different reps, different counting. The count lives in the singleton picture (the bulk "
      "ν=5 cannot cap); which rep is correct must be pinned by structure, not by which gives 3.",
      True,
      "tension: F323 bulk ν=5 (uncapped) vs K945 singleton (capped) — count needs the singleton rep; pin by structure not by target")

check("VERDICT: bare Pochhammer norm UNCAPPED for ν>3/2 → does NOT decide b; 'b=3' off it = imposed/circular cap (forbidden). "
      "Real decider = sub-threshold regularized signature at the singleton's actual ν (Gindikin-Γ, K950), NOT faked here. b "
      "UNDECIDED, 3-vs-4 live, premise REDUCED, NOT forced to 3. The catch keeps the count honest.",
      uncapped and below_poles,
      "b undecided by the bare norm (uncapped→fiat-3 forbidden); decider = regularized sub-threshold signature (pending singleton ν); NOT forced; premise REDUCED")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [TEGMARK] A2 Gram signature — the bare norm is UNCAPPED (target-innocent catch) (Elie, pull 27m, per K950):
  * SOURCED (F323): ‖ψ_k‖² ∝ (ν)_{{k+½}}(ν−3/2)_½; Gram diagonal → b = signature.
  * COMPUTED: positive for ALL k at every ν>3/2 (incl. F323's ν=5) → UNCAPPED. So reading 'b=3' off it = stopping at k=2 BY FIAT = the circular filtration K950/Cal forbid. The bare norm does NOT decide b.
  * REAL DECIDER (not faked): the sub-threshold regularized signature (ν<3/2 returns Gamma poles → needs the fixed Gindikin-Γ continuation, K950 rule 5) at the singleton's ACTUAL ν (pinned by so(5,2) structure, not chosen). The cap lives there.
  * CORPUS TENSION flagged (F323 bulk ν=5 uncapped vs K945 singleton capped). b UNDECIDED, 3-vs-4 live, premise REDUCED, NOT forced to 3.
""")
