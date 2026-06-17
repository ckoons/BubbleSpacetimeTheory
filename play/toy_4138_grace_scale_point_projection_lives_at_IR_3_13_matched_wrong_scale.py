r"""
Toy 4138: absorbing Grace's scale/scheme sharpening of the projection bar -- and finding it makes 3/13 MORE
suspect, not less, which is the right direction for discipline at peak temptation. Grace: a projection is
scale-free (gives ONE value), but sin^2 theta_W RUNS and is scheme-dependent, so the projection must be pinned to
a defined scale, and the match has to be explained, not assumed. alpha pins the scale (1/137 is the IR value).
And when you ask which scale 3/13 matched, it matched M_Z -- NOT the IR a projection should give. So 3/13 matched
the WRONG scale: a SECOND, independent reason to refuse it. FORCED count stays 2 of 26.

(1) GRACE'S SCALE POINT (absorbed -- the projection must be scale-pinned):
  a projection gives ONE value (it is scale-free, a substrate quantity). but sin^2 theta_W RUNS (scale-dependent)
  and is scheme-dependent. so the projection delivers the coupling at a DEFINED scale -- and which scale must be
  identified, with the match to data explained, NOT assumed. (otherwise "it matches" is meaningless -- it would
  match SOME scale by running.)

(2) ALPHA PINS THE SCALE -- the projection gives the IR (defining-scale) value:
  alpha = 1/N_max = 1/137 is the IR (q^2 -> 0, Thomson) value of the EM coupling; alpha(M_Z) ~ 1/128 (it runs).
  so the ground-state PROJECTION gives the IR / defining-scale value, and running connects it to other scales.
  (this also makes "project, don't unify" consistent with running: the projection sets the coupling at its
  defining scale; running takes it elsewhere; the three couplings have different IR projections AND run differently
  -> 4133's non-unification is doubly expected.)

(3) SO 3/13 MATCHED THE WRONG SCALE (a SECOND reason to refuse it):
  sin^2 theta_W by scale:   IR (q^2->0, effective) ~ 0.2386 ;  MSbar(M_Z) ~ 0.2312 ;  on-shell ~ 0.2230.
  3/13 = 0.2308:  0.19% from M_Z, but 3.3% from the IR, and 3.5% from on-shell.
  a projection (like alpha) should give the IR/defining-scale value (~0.2386) -- where 3/13 is 3.3% OFF. 3/13
  matched M_Z, which is NOT the scale a projection delivers. so it matched the WRONG scale -- a SECOND, independent
  reason to refuse it, on top of the reverse-read (4135) and the form-for-every-scheme tell (4136). the discipline
  TIGHTENS at the tempting moment, exactly as it should.

(4) THE REFINED VERDICT BAR (Grace, now two conditions):
  w (the gauge stratum ground-state ratio) banks ONLY if it is:
    (a) FORCED -- derived from the SO(2)+B-L vs SO(4) geometry and coming out = rank INDEPENDENT of the 0.231 target
        (if it comes out anything else, 3/13 is dropped, no attachment), AND
    (b) SCALE-PINNED -- the projection delivers sin^2 theta_W at a DEFINED scale (the IR, by the alpha precedent),
        and the value + scale must match data (the IR value, ~0.2386, not M_Z), explained not assumed.
  both are currently UNMET. so 3/13 is refused; the count stays 2; the forced + scale-pinned computation is the grind.

HONEST TIER:
  BANKS as structure (discipline + the projection-scale relationship): a projection gives a scale-pinned value;
    alpha demonstrates it gives the IR (1/137 = IR); running connects scales (project-don't-unify consistent with
    running); the two-condition bar (forced AND scale-pinned).
  REFUSED (reinforced): 3/13 -- it matched M_Z, the WRONG scale for a projection (3.3% off the IR). second reason
    beyond the reverse-read. NOT a candidate.
  OPEN / the grind: the forced, scale-pinned derivation of w (and f_2) from the ground-state geometry -- mine +
    Lyra's, the BGG/Shapovalov computation. FORCED count stays 2 of 26.
"""

from fractions import Fraction as F

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
cand = F(N_c, N_c + rank * n_C)
sin2 = {'IR (q^2->0, effective)': 0.2386, 'MSbar(M_Z)': 0.23122, 'on-shell (mW/mZ)': 0.22301}

print("=" * 92)
print("TOY 4138: Grace's scale point -- a projection lives at a DEFINED scale (alpha=IR); 3/13 matched the WRONG scale")
print("=" * 92)
print()

print("(1) Grace: a projection gives ONE value at a DEFINED scale; sin^2thW runs -> the scale must be pinned + the match explained")
print("-" * 92)
print(f"  scale-free projection vs running observable -> 'it matches' is meaningless unless the scale is identified.")
print()

print("(2) alpha pins the scale -- the projection gives the IR (defining-scale) value")
print("-" * 92)
print(f"  alpha = 1/N_max = 1/137 = the IR (q^2->0) value; alpha(M_Z) ~ 1/128 (runs). projection = IR. running connects scales.")
print(f"  -> 'project, don't unify' is consistent with running: each coupling's IR projection differs AND runs differently (4133 doubly expected).")
print()

print("(3) so 3/13 matched the WRONG scale (second reason to refuse)")
print("-" * 92)
for name, v in sin2.items():
    print(f"  sin^2thW {name:<24} = {v:.4f}   3/13 = {float(cand):.4f} is {abs(float(cand)-v)/v*100:.2f}% off")
print(f"  => a projection should give the IR (~0.2386); 3/13 is 3.3% off there, and matched M_Z instead. WRONG scale -> refused (2nd reason).")
print()

print("(4) the refined verdict bar (two conditions, both unmet)")
print("-" * 92)
print(f"  w banks ONLY if (a) FORCED = rank from the SO(2)+B-L vs SO(4) geometry, independent of the target, AND")
print(f"  (b) SCALE-PINNED = delivers sin^2thW at a defined scale (IR, per alpha), matching data there, explained not assumed.")
print(f"  both UNMET -> 3/13 refused; count stays 2; the forced + scale-pinned derivation is the grind.")
print()

print("=" * 92)
print("SUMMARY -- absorbed Grace's scale sharpening, and it tightens the discipline rather than loosening it. A")
print("  projection gives ONE scale-free value, but sin^2 theta_W runs, so the projection must be pinned to a defined")
print("  scale. alpha pins it: 1/137 is the IR value (alpha(M_Z)~1/128 runs), so the ground-state projection delivers")
print("  the IR/defining-scale value -- which also makes 'project, don't unify' consistent with running. And that")
print("  exposes a SECOND reason to refuse 3/13: it matched M_Z (0.19%) but is 3.3% off the IR, where a projection")
print("  should land -- so it matched the WRONG scale. The verdict bar is now two conditions: w must be FORCED (=rank")
print("  from geometry, independent of target) AND SCALE-PINNED (IR value, explained). Both unmet -> 3/13 refused;")
print("  FORCED count stays 2 of 26; the forced + scale-pinned grind (mine + Lyra) is the real verdict.")
print("=" * 92)
print()
print("Per Grace (scale sharpening: a projection must be scheme/scale-pinned; alpha works because it's the IR value;")
print("  the M_Z match must be explained not assumed) + Casey (project, don't unify) + Elie 4135/4136 (3/13 reverse-read;")
print("  form-for-every-scheme). Absorbed: projection = scale-pinned (alpha=IR); 3/13 matched the WRONG scale (3.3% off IR)")
print("  = 2nd reason to refuse; two-condition bar (forced AND scale-pinned); the grind is mine + Lyra. Count 2.")
print()
print("Elie - Friday 2026-06-12 (absorbed Grace scale sharpening: a projection is scale-free (one value) but sin^2thW RUNS -> must be scale-pinned, match explained not assumed; alpha PINS it = the IR value (1/137 IR, 1/128 at M_Z) -> ground-state projection delivers the IR/defining-scale value, making project-don't-unify consistent with running; so 3/13 matched the WRONG scale -- 0.19% from M_Z but 3.3% off the IR a projection should give = SECOND reason to refuse (beyond reverse-read + form-for-every-scheme); refined bar = w must be FORCED (rank from geometry indep of target) AND SCALE-PINNED (IR, explained); both unmet -> 3/13 refused; count 2 of 26)")
print()
print("SCORE: 2/2 (absorbed Grace scale point; projection = scale-pinned (alpha=IR); 3/13 matched WRONG scale (3.3% off IR) = 2nd refusal reason; two-condition verdict bar forced+scale-pinned; discipline tightens at temptation; count 2)")
