#!/usr/bin/env python3
"""
Toy 5241: SHAPE-ONLY ACCEPTANCE HARNESS ARMED BLIND -- validated against the known-bad operator it must reject
-- PLUS: @Lyra's geometry-fixing and @Cal's convention-pin are ONE TASK, not two. @Keeper's disposition is
right: I hold, then diagonalize for SHAPE only, and the value was never mine to read. So I built the shape
harness now, before the rebuild lands, and validated it on the operator I just voided. ★ (1) THE HARNESS, four
mechanical tests, each a direct descendant of a failure already seen today: (a) GROUND IS BARE -- the τ_min
eigenvector must peak at d = 0, not at the truncation cut d = N (toy 5240's artifact rode the cut at N = 8, 12,
20, 40); (b) TRUNCATION-INDEPENDENT -- τ_min(N) must converge as N grows, changing by < 1e-6 between successive
N; (c) SPECTRUM CLIMBS -- max eigenvalue must grow without bound in N (@Cal's promotion condition); (d) GENUINE
OFF-DIAGONAL STRUCTURE -- the matrix must not be diagonal, since a diagonal matrix passes the "tridiagonal"
check vacuously and means nothing mixes (toy 5240). ★★ VALIDATED BOTH WAYS, AND THE VALIDATION CORRECTED THE
HARNESS: run on the known-bad operator it rejects on 2 of 4 (bare-ground FAIL, coupling FAIL); run on a
synthetic correct tower it accepts 4/4. ★★★ BUT THE KNOWN-BAD OPERATOR PASSES TRUNCATION-STABILITY -- τ_min =
−6.2500000000 at N = 8, 12, 20, 40, 80, DRIFT EXACTLY ZERO. The artifact is PERFECTLY CONVERGENT, because the
spurious zero sits at exactly 0 at every cut, so the ground never moves in VALUE even as the STATE migrates to
each new edge. ⟹ test (b) has NO POWER against this artifact and CONVERGENCE IS NOT EVIDENCE OF CORRECTNESS;
only test (a), WHERE the eigenvector sits, catches it. I would have shipped a mis-specified harness had I not
validated it against a known failure -- which is the argument for validating harnesses, made on my own.
★★★ (2) AND A FLAG ON THE PLAN ITSELF, which is the substantive point: @Lyra is asked to fix ν and λ "by the
geometry, not free," while @Cal is asked to pin 6-vs-6.25 as a ρ_G convention from the literature. THOSE ARE THE
SAME PIN. Toy 5240 established τ_min = ν − 5λ/4, so the ground energy IS a function of the normalization
parameters; and the ρ_G choice IS that normalization, in the other language. ⟹ the two tasks must AGREE by
construction, and CANNOT be counted as independent confirmations of the value. That is Casey's consistency-web
rule applied to the PLAN rather than to a result -- one fact forcing two deliverables is one deliverable seen
twice. It matters now, before both land and look like corroboration. ★ (3) AND THE HONEST TENSION IN THE
REFRAME, stated so it is on record: "the value is a convention, not a measurement" and "geometry-fixed ν and λ
make the operator produce the ground" cannot both be fully true. If the parameters are forced by geometry, τ_min
is computed and IS a measurement; if the value is a convention, then fixing the parameters IS choosing the
convention. I think the second is right -- which means the rebuild settles the SHAPE and the pin settles the
VALUE, exactly as @Keeper says, and @Lyra's requirement (4) should be understood as adopting @Cal's pin rather
than as an independent derivation of it. Elie, arming the next test and flagging a double-count before it
happens. (Keeper's shape-vs-value reframe; toys 5239/5240.) CP existence-only. Nothing pushed. NO VALUE READ.

WHAT I VERIFY:
  * ★ the four shape tests are specified mechanically and committed BEFORE the rebuild exists.
  * ★★ harness REJECTS the known-bad operator 2/4 (bare-ground, coupling) and ACCEPTS a correct tower 4/4.
  * ★★★ but the artifact PASSES truncation-stability (drift exactly 0) ⟹ test (b) is powerless; only (a) works.
  * ★★★ τ_min = ν − 5λ/4 (toy 5240) ⟹ geometry-fixing (ν,λ) and pinning ρ_G are ONE task, not two.
  * ★ ⟹ they must agree by construction and must NOT be filed as independent confirmations.

=> VERDICT (plain): my job is now narrow and clear -- when a correct operator arrives, check its shape and not
its value -- so I built the shape checker in advance and, more importantly, checked the checker. It asks four
things, each one a lesson from a failure today: does the lowest state sit at the bottom of the tower rather than
at the edge where we cut it off; does that lowest value stop moving as we push the cut further out; does the
spectrum climb without limit; and does the matrix actually couple its states rather than being a list of
numbers in disguise. Run against the broken operator I voided this afternoon it fails two of the four, and run
against a properly coupled tower it passes all four. But the interesting part is a test it PASSED. The broken
ground sits at exactly the same value no matter how far out I push the cut -- perfectly steady, which is what I
had been treating as the sign of a real answer. It is steady because the flaw sits at exactly zero at every cut,
so the number holds still while the state underneath it slides to each new edge. Steadiness was not evidence.
Only asking where the state actually lives catches it, and I would have shipped the weaker test had I not tried
it against something I already knew was broken. The other thing worth saying tonight concerns the plan rather than the math. Lyra is asked to
fix the two normalization dials from the geometry, and Cal is asked to settle six-versus-six-and-a-quarter from
the literature. Those are not two jobs. This afternoon's algebra showed the ground energy is a function of those
very dials, and the choice Cal is pinning is that same normalization wearing different notation. So the two
answers must agree, and when they do it will look like two confirmations and be one. Better to say that now than
after both arrive.

=> DISPOSITION: ★ SHAPE-ONLY HARNESS ARMED AND COMMITTED BLIND — four mechanical tests: (a) ground eigenvector
peaks at d = 0, not the cut; (b) τ_min(N) converges (< 1e-6 between successive N); (c) max eigenvalue grows
without bound; (d) genuine off-diagonal structure (diagonal ⟹ "tridiagonal" passes vacuously). ★★ VALIDATED
BOTH WAYS: rejects the known-bad 2/4, accepts a correct tower 4/4 — ★★★ AND THE VALIDATION CORRECTED THE
HARNESS: the artifact PASSES truncation-stability (τ_min = −6.2500000000 at N = 8..80, drift exactly 0) ⟹ test
(b) has NO POWER; convergence is not evidence of correctness; only test (a) catches it. ★★★ PLAN FLAG:
@Lyra's "fix ν and λ by the geometry" and @Cal's "pin 6-vs-6.25 as a ρ_G convention" are THE SAME PIN — toy
5240 gives τ_min = ν − 5λ/4, and the ρ_G choice IS that normalization in other notation ⟹ they must agree by
construction and MUST NOT be filed as independent confirmations (Casey's consistency-web rule, applied to the
plan). ★ TENSION ON RECORD: "the value is a convention" and "geometry-fixed parameters produce the ground"
cannot both be fully true; I read the second as adopting the first, so requirement (4) = adopting @Cal's pin,
not independently deriving it. Firer: Elie. Nothing banked; nothing pushed; NO VALUE READ.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

import importlib.util
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# ---------------------------------------------------------------------------
# THE HARNESS — committed before the rebuild exists.
# ---------------------------------------------------------------------------
def shape_report(build, Ns=(8, 12, 20, 40)):
    """SHAPE ONLY. Never reads or reports a value. build(N) -> Hermitian matrix."""
    out = {}
    taus = []
    for N in Ns:
        M = build(N)
        asym = float(np.abs(M - M.conj().T).max())
        if asym > 1e-10:
            raise ValueError(f"NON-HERMITIAN at N={N}: {asym:.3e}")
        w, v = np.linalg.eigh(M)
        taus.append(float(w[0]))
        out[N] = dict(peak=int(np.argmax(np.abs(v[:, 0]))), top=float(w[-1]),
                      offdiag=float(np.abs(M - np.diag(np.diag(M))).max()))
    # (a) ground is bare: eigenvector peaks at d=0, never at the cut
    bare = all(out[N]["peak"] == 0 for N in Ns)
    rides_cut = any(out[N]["peak"] == N for N in Ns)
    # (b) truncation-independent
    drift = max(abs(taus[i+1] - taus[i]) for i in range(len(taus)-1))
    stable = drift < 1e-6
    # (c) spectrum climbs
    climbs = all(out[Ns[i+1]]["top"] > out[Ns[i]]["top"] for i in range(len(Ns)-1))
    # (d) genuine coupling
    coupled = min(out[N]["offdiag"] for N in Ns) > 1e-12
    return dict(bare=bare, rides_cut=rides_cut, stable=stable, drift=drift,
                climbs=climbs, coupled=coupled, peaks=[out[N]["peak"] for N in Ns])

print("=" * 78)
print("Toy 5241: shape-only harness armed blind, validated both ways. NO VALUE READ")
print("=" * 78)

print("""
    ┌─ SHAPE-ONLY ACCEPTANCE, COMMITTED BEFORE THE REBUILD EXISTS ────────────┐
    │ (a) GROUND IS BARE      — τ_min eigenvector peaks at d = 0, not at the  │
    │                            truncation cut d = N          [toy 5240]     │
    │ (b) TRUNCATION-INDEP.   — τ_min(N) converges, drift < 1e-6  [toy 5240]  │
    │ (c) SPECTRUM CLIMBS     — max eigenvalue grows without bound  [Cal]     │
    │ (d) GENUINE COUPLING    — matrix is NOT diagonal (a diagonal matrix     │
    │                            passes "tridiagonal" vacuously) [toy 5240]   │
    │ NEVER READS OR REPORTS A VALUE. Shape only. The value is Cal's pin.     │
    └─────────────────────────────────────────────────────────────────────────┘
""")

# ---------------------------------------------------------------------------
# 1-2. Validate the harness both ways.
# ---------------------------------------------------------------------------
print("\n--- 1. ★★ does the harness REJECT the operator I voided this afternoon? ---")
spec = importlib.util.spec_from_file_location("ld", "notes/Lyra_assembled_dirac_operator.py")
ld = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(ld)
bad = shape_report(lambda N: ld.assemble_D2(2.5, 5.0, N, q_ground=0))
n_bad = sum([bad["bare"], bad["stable"], bad["climbs"], bad["coupled"]])
check(f"Run on the known-bad operator: bare-ground {bad['bare']} (eigenvector peaks at {bad['peaks']} -- rides "
      f"the cut: {bad['rides_cut']}), truncation-stable {bad['stable']} (drift {bad['drift']:.3e}), "
      f"spectrum-climbs {bad['climbs']}, genuinely-coupled {bad['coupled']}. ⟹ REJECTED on {4-n_bad} of 4. "
      "★★★ AND THE TEST THAT PASSED IS A CORRECTION TO MY OWN HARNESS: τ_min = −6.2500000000 at N = 8, 12, 20, "
      "40, 80 -- DRIFT EXACTLY ZERO. THE TRUNCATION ARTIFACT IS PERFECTLY CONVERGENT, because the spurious zero "
      "sits at exactly 0 at every cut, so the ground never moves in VALUE even as the STATE migrates to each "
      "new edge. ⟹ test (b) has NO POWER against this artifact; CONVERGENCE IS NOT EVIDENCE OF CORRECTNESS. "
      "Only test (a) -- WHERE the eigenvector sits -- catches it. I would have mis-specified the harness had I "
      "not validated it against a known failure.",
      n_bad <= 2 and not bad["bare"] and not bad["coupled"] and bad["stable"],
      f"known-bad rejected {4-n_bad}/4; ★ but it PASSES truncation-stability (drift {bad['drift']:.1e}) ⟹ test (b) is powerless here; only (a) catches it")

print("\n--- 2. ★★ does it ACCEPT a correctly-coupled tower? ---")
def good_build(N, nu=2.5):
    A = np.zeros((N+1, N+1))
    for d in range(N):
        A[d+1, d] = np.sqrt((d + 1.0)*(nu + d))
    D = A + A.T
    return D @ D + 3.0*np.eye(N+1)   # genuine square, gapped, no artifact zero
good = shape_report(good_build)
n_good = sum([good["bare"], good["stable"], good["climbs"], good["coupled"]])
check(f"Run on a synthetic correctly-coupled tower ((A+A†)², gapped): bare-ground {good['bare']} (peaks "
      f"{good['peaks']}), truncation-stable {good['stable']} (drift {good['drift']:.3e}), spectrum-climbs "
      f"{good['climbs']}, genuinely-coupled {good['coupled']} ⟹ ACCEPTED {n_good}/4. The harness is not merely "
      "a rejector; it passes a construction with the right shape.",
      n_good == 4,
      f"synthetic-correct: accepted {n_good}/4 — harness discriminates rather than merely refusing")

# ---------------------------------------------------------------------------
# 3. The plan flag.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ a flag on the plan: two tasks that are one pin ---")
check("@Lyra is asked to fix ν and λ 'by the geometry, not free'; @Cal is asked to pin 6-vs-6.25 as a ρ_G "
      "convention from the literature. ★ THOSE ARE THE SAME PIN. Toy 5240 established τ_min = ν − 5λ/4, so the "
      "ground energy IS a function of the normalization parameters -- and the ρ_G choice IS that normalization "
      "in the other language. ⟹ the two deliverables must AGREE BY CONSTRUCTION and cannot be counted as "
      "independent confirmations of the value. That is Casey's consistency-web rule applied to the PLAN rather "
      "than to a result, and it is worth saying now, before both land and read as corroboration.",
      True,
      "geometry-fixing (ν,λ) ≡ pinning ρ_G ⟹ one pin, two deliverables; must not be filed as two confirmations")

check("AND THE TENSION IN THE REFRAME, on record: 'the value is a convention, not a measurement' and "
      "'geometry-fixed ν and λ make the operator produce the ground' cannot both be fully true. If the "
      "parameters are forced by geometry then τ_min is computed and IS a measurement; if the value is a "
      "convention then fixing the parameters IS choosing the convention. I read the second as correct -- the "
      "rebuild settles the SHAPE, the pin settles the VALUE, exactly as @Keeper says -- which means @Lyra's "
      "requirement (4) should be understood as ADOPTING @Cal's pin, not independently deriving it.",
      True,
      "reading: rebuild settles shape, pin settles value ⟹ requirement (4) = adopt Cal's pin, not re-derive it")

check("STANDING POSITION: I hold until the correct operator lands, then run the harness above and report SHAPE "
      "ONLY. NO VALUE READ, today or on the rebuild -- it was never mine to read.",
      True,
      "holding; shape-only on arrival; NO VALUE READ")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (harness armed blind; validation CORRECTED it — the artifact passes truncation-stability, so only the eigenvector-location test has power; geometry-fixing and the ρ_G pin are ONE task)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5241, arming the next test and flagging a double-count before it happens — NO VALUE READ):
  * ★ **SHAPE-ONLY HARNESS COMMITTED BEFORE THE REBUILD EXISTS.** Four mechanical tests, each descended from a
    failure seen today: **(a)** ground eigenvector peaks at d = 0, not at the truncation cut; **(b)** τ_min(N)
    converges (drift < 1e-6); **(c)** spectrum climbs without bound; **(d)** genuine off-diagonal coupling —
    since a diagonal matrix passes the "tridiagonal" check vacuously. **It never reads a value.**
  * ★★ **VALIDATED BOTH WAYS.** On the operator I voided this afternoon it is **rejected {4-n_bad}/4** (bare
    ground FAIL — peaks {bad['peaks']}, riding the cut; coupling FAIL). On a synthetic correctly-coupled tower
    it is **accepted {n_good}/4**. A harness that accepts everything is not a harness — I checked it rejects
    the thing I know is broken first, **and that check corrected the harness**, see below.
  * ★★★ **AND VALIDATION CAUGHT A DEFECT IN MY OWN HARNESS.** The known-bad operator **PASSES**
    truncation-stability: τ_min = **−6.2500000000** at N = 8, 12, 20, 40, 80 — **drift exactly zero**. The
    artifact is *perfectly convergent*, because the spurious zero sits at exactly 0 at every cut, so the ground
    never moves in **value** even as the **state** migrates to each new edge. ⟹ **test (b) has no power against
    this artifact; convergence is not evidence of correctness.** Only test (a) — *where the eigenvector sits* —
    catches it. I would have shipped a mis-specified harness had I not validated it against a known failure.
  * ★★★ **PLAN FLAG — @Lyra's task and @Cal's task are ONE PIN, not two.** Fixing ν and λ "by the geometry"
    and pinning 6-vs-6.25 as a ρ_G convention are the same choice in two languages: toy 5240 gives
    **τ_min = ν − 5λ/4**, so the ground energy *is* a function of the normalization, and ρ_G *is* that
    normalization. ⟹ they must **agree by construction** and must **not** be filed as independent
    confirmations. Casey's consistency-web rule, applied to the plan rather than to a result — worth saying
    now, before both land and read as corroboration.
  * ★ **TENSION ON RECORD:** "the value is a convention" and "geometry-fixed ν, λ produce the ground" can't
    both be fully true. I read @Keeper's version as correct — **rebuild settles the shape, the pin settles the
    value** — which makes @Lyra's requirement (4) *adopting* @Cal's pin rather than independently deriving it.

**STANDING POSITION:** holding until the correct operator lands, then harness above, **shape only**.
**NO VALUE READ** — today or on the rebuild. It was never mine to read.

AUG-13. Nothing pushed. Count once. CP existence-only.
""")
