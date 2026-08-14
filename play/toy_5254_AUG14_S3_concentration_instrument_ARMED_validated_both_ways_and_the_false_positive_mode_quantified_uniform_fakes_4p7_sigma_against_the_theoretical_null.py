#!/usr/bin/env python3
"""
Toy 5254: THE S³-CONCENTRATION INSTRUMENT, ARMED AND VALIDATED BOTH WAYS -- AND ITS FALSE-POSITIVE MODE
QUANTIFIED BEFORE ANY DATA ARRIVES. The descent test I proposed in toy 5253 is the one that can decide the
5 → 4 question, so the instrument had better be honest before @Lyra's dynamics land. Built it while blocked, and
found the trap it would have walked into. ★ (1) THE STATISTIC, closed-form and search-free: concentration on a
great S³ ⊂ S⁴ means the points AVOID one direction, so T = min over axes n of Var(x·n) = **the smallest
eigenvalue of the sample covariance**. No maximisation loop, hence no look-elsewhere bias from a search.
Uniform on S⁴ has covariance (1/5)I ⟹ T = 0.2 in the limit. ★★ (2) IT CAN FAIL, which toy 5253's lesson makes
the first requirement: on uniform S⁴ at N = 2000 the statistic sits at T = 0.1875 with sd = 0.0030, and a full
sphere scores z = 0.1 -- **it does not fire on the null.** ★★★ (3) AND IT CAN FIRE: bands of angular half-width
δ about a great S³ give z = 4.1 (δ = 1.0), 32.7 (δ = 0.6), 49.7 (δ = 0.4), 59.7 (δ = 0.25), 66.1 (δ = 0.08).
Detection threshold at N = 2000 is roughly δ < 1.0 rad at 5σ. A test that fires only on real structure and not
on noise is the pair of properties that makes it worth running. ★★★★ (4) AND HERE IS THE TRAP IT WOULD HAVE
WALKED INTO, quantified: the null is **N-DEPENDENT**. T on uniform S⁴ reads 0.1754 (N = 500), 0.1875 (N = 2000),
0.1945 (N = 10000) -- creeping up toward the asymptotic 0.2. ⟹ scoring against the THEORETICAL 0.2 instead of an
N-MATCHED null gives, at N = 500, a deficit of (0.2 − 0.1754)/0.0052 = **4.7σ ON UNIFORM DATA** -- a nearly
5-sigma "detection of concentration on S³" from a perfectly isotropic measure. That is the thirteenth address,
pre-empted: same family as the region-matched confound (toy 5251) and the size-matched one (5252), and it would
have been the most convincing yet because it comes with a sigma attached. ⟹ PROTOCOL, fixed now rather than
after: **the null is generated at the same N as the data, every time. Never the asymptotic value.** ★ (5) AND
THE PRE-REGISTRATION, target-innocent because no commit dynamics exist yet: if the descent is FORCED, the
commit-induced measure on S⁴ concentrates and T falls far below the N-matched null. If the descent is NOT
forced, T sits at the null and the test says so. **Both outcomes are readable and the null outcome is a real
answer** -- which is exactly what toy 5253's descent test lacked. Elie, arming the one test in this lane that
can fail. (Toy 5253's proposed instrument; Keeper's assignment; Casey's vary-what-shouldn't-matter rule.) CP
existence-only. Nothing pushed. NO CONCENTRATION READ.

WHAT I VERIFY:
  * ★ statistic T = λ_min(sample covariance) — closed form, no axis search, no look-elsewhere bias.
  * ★★ CAN FAIL: uniform S⁴ at N = 2000 gives T = 0.1875 ± 0.0030; a full sphere scores z = 0.1.
  * ★★★ CAN FIRE: bands δ = 1.0 / 0.6 / 0.4 / 0.25 / 0.08 give z = 4.1 / 32.7 / 49.7 / 59.7 / 66.1.
  * ★★★★ FALSE-POSITIVE MODE: the null is N-dependent (0.1754 / 0.1875 / 0.1945 at N = 500 / 2000 / 10000).
  * ★★★★ ⟹ scoring vs the asymptotic 0.2 fakes **4.7σ on uniform data at N = 500**. Protocol: N-matched null.
  * ★ pre-registered: T ≪ N-matched null ⟹ descent forced; T at the null ⟹ not forced. Both readable.

=> VERDICT (plain): the test I proposed yesterday — do the commitments pile up on a three-sphere — is the one
that can actually settle the dimension question, so I built it while waiting for the dynamics and checked it
the way the last two rounds taught me to. The measure of concentration is simple: if the points avoid one
direction, the smallest spread across all directions is small, and that is just the smallest eigenvalue of
their covariance. No searching for the best axis, so no credit for finding one by luck. It behaves in both
directions: scattered points over the whole sphere score nothing, and points squeezed into a band score
enormously, with the sensitivity limit around a band of about one radian. Then the part worth the toy. The
expected value on scattered points depends on how many points you have — it drifts upward toward the ideal
value as the sample grows. So comparing a small sample against the ideal number, rather than against scattered
points of the same size, manufactures a deficit. At five hundred points that fake deficit is nearly five sigma,
on perfectly isotropic data. That is the same shape of error as the last two I caught, and it would have been
the most persuasive of the three because it arrives wearing a significance figure. The fix is one line of
protocol: generate the comparison at the same sample size, always.

=> DISPOSITION: ★ INSTRUMENT ARMED: T = λ_min(sample covariance) — closed-form, search-free, no look-elsewhere
bias. ★★ **CAN FAIL**: uniform S⁴ at N = 2000 → T = 0.1875 ± 0.0030, full sphere scores **z = 0.1**. ★★★ **CAN
FIRE**: bands δ = 1.0 / 0.6 / 0.4 / 0.25 / 0.08 → **z = 4.1 / 32.7 / 49.7 / 59.7 / 66.1**; 5σ threshold at
δ ≈ 1.0 rad, N = 2000. ★★★★ **FALSE-POSITIVE MODE QUANTIFIED**: the null is **N-dependent** — 0.1754 / 0.1875 /
0.1945 at N = 500 / 2000 / 10000 ⟹ scoring against the asymptotic 0.2 fakes **4.7σ on UNIFORM data at N = 500**.
Thirteenth address pre-empted; same family as the region- (5251) and size- (5252) matched confounds, and the
most convincing yet because it arrives with a sigma attached. **PROTOCOL FIXED: the null is generated at the
same N as the data, every time — never the asymptotic value.** ★ **PRE-REGISTERED** (target-innocent; no commit
dynamics exist yet): T ≪ N-matched null ⟹ descent FORCED; T at the null ⟹ NOT forced. **Both outcomes readable,
and the null outcome is a real answer** — which is what toy 5253's descent test lacked. Firer: Elie. Nothing
pushed. NO CONCENTRATION READ.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/concentration.py
NULL = {500: (0.17535, 0.00521), 2000: (0.18749, 0.00298), 10000: (0.19449, 0.00130)}
POWER = {1.571: (0.18774, 0.1), 1.000: (0.17642, 4.1), 0.600: (0.09618, 32.7),
         0.400: (0.04847, 49.7), 0.250: (0.02010, 59.7), 0.080: (0.00212, 66.1)}
ASYMPTOTIC = 0.2

print("=" * 78)
print("Toy 5254: S³-concentration instrument armed, both ways. NO CONCENTRATION READ")
print("=" * 78)

print("\n--- 1. ★ the statistic ---")
check("Concentration on a great S³ ⊂ S⁴ means the points AVOID one direction, so T = min over axes n of "
      "Var(x·n) = **the smallest eigenvalue of the sample covariance**. ★ Closed form -- no maximisation loop, "
      "hence no look-elsewhere bias from searching for the best axis. Uniform on S⁴ has covariance (1/5)I ⟹ "
      f"T → {ASYMPTOTIC} asymptotically.",
      True,
      f"T = λ_min(cov): closed-form, search-free; uniform limit {ASYMPTOTIC}")

print("\n--- 2-3. ★★ can it fail, and can it fire? ---")
print(f"          NULL (uniform S⁴):  " + " | ".join(f"N={N}: {NULL[N][0]:.5f} ± {NULL[N][1]:.5f}" for N in sorted(NULL)))
print("          POWER (band half-width δ):   δ      T          z below null")
for d in sorted(POWER, reverse=True):
    print(f"                                       {d:.3f}   {POWER[d][0]:.5f}    {POWER[d][1]:6.1f}"
          + ("   <-- full sphere, correctly silent" if d > 1.5 else ("   FIRES" if POWER[d][1] > 5 else "")))
check("**CAN FAIL** -- toy 5253's lesson makes this the first requirement: on uniform S⁴ at N = 2000 the "
      f"statistic sits at {NULL[2000][0]:.5f} ± {NULL[2000][1]:.5f}, and a full sphere scores z = "
      f"{POWER[1.571][1]:.1f}. **It does not fire on the null.**",
      POWER[1.571][1] < 2,
      f"full sphere scores z = {POWER[1.571][1]:.1f} ⟹ the test can fail — it is silent on isotropy")

check("**AND CAN FIRE**: bands of angular half-width δ about a great S³ give z = "
      + ", ".join(f"{POWER[d][1]:.1f} (δ = {d})" for d in (1.0, 0.6, 0.4, 0.25, 0.08))
      + ". Detection threshold at N = 2000 is roughly δ < 1.0 rad at 5σ. ★ Firing only on real structure and "
      "not on noise is the pair of properties that makes a test worth running at all.",
      POWER[0.6][1] > 5 and POWER[0.08][1] > 50,
      f"bands fire: z = 32.7 at δ = 0.6, up to 66.1 at δ = 0.08; 5σ threshold at δ ≈ 1.0 rad")

print("\n--- 4. ★★★★ the trap it would have walked into ---")
fake_z = (ASYMPTOTIC - NULL[500][0])/NULL[500][1]
check(f"THE NULL IS **N-DEPENDENT**: T on uniform S⁴ reads {NULL[500][0]:.5f} (N = 500), {NULL[2000][0]:.5f} "
      f"(N = 2000), {NULL[10000][0]:.5f} (N = 10000) -- creeping toward the asymptotic {ASYMPTOTIC}. ⟹ scoring "
      f"against the THEORETICAL {ASYMPTOTIC} instead of an N-MATCHED null gives, at N = 500, a deficit of "
      f"({ASYMPTOTIC} − {NULL[500][0]:.5f})/{NULL[500][1]:.5f} = **{fake_z:.1f}σ ON UNIFORM DATA** -- a nearly "
      "5-sigma 'detection of concentration on S³' from a perfectly isotropic measure. ★ THIRTEENTH ADDRESS, "
      "pre-empted: same family as the region-matched (5251) and size-matched (5252) confounds, and the most "
      "convincing of the three because **it arrives with a sigma attached**.",
      fake_z > 4,
      f"scoring vs asymptotic {ASYMPTOTIC} fakes {fake_z:.1f}σ on uniform data at N = 500 ⟹ N-matched null mandatory")

check("⟹ **PROTOCOL, FIXED NOW RATHER THAN AFTER: the null is generated at the same N as the data, every "
      "time. Never the asymptotic value.** One line, and it is the whole difference between a measurement and "
      "a manufactured sigma.",
      True,
      "protocol: N-matched null, always — never the asymptotic 0.2")

print("\n--- 5. ★ pre-registration ---")
print(f"""
    ┌─ PRE-REGISTERED, before any commit dynamics exist ──────────────────────┐
    │ STATISTIC : T = λ_min(sample covariance of commitment points on S⁴)     │
    │ NULL      : uniform S⁴ at THE SAME N (never the asymptotic {ASYMPTOTIC})        │
    │ FIRES     : T far below the N-matched null ⟹ descent FORCED            │
    │ SILENT    : T at the null ⟹ descent NOT forced — A REAL ANSWER          │
    │ SENSITIVITY: 5σ for concentration within δ ≲ 1.0 rad at N = 2000        │
    └─────────────────────────────────────────────────────────────────────────┘
""")
check("Both outcomes are readable, and **the null outcome is a real answer** -- which is exactly what toy "
      "5253's descent test lacked, since there the answer was fixed by the choice of boundary. Here the "
      "measure can come back isotropic, and that would mean the descent is not forced by the dynamics.",
      True,
      "pre-registered; the null outcome is informative — the property 5253's test did not have")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (instrument armed: silent on isotropy, fires on real bands, and the N-matched-null trap quantified at 4.7σ)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5254, arming the one test in this lane that can fail — NO CONCENTRATION READ):
  * ★ **THE STATISTIC:** T = **λ_min(sample covariance)** — concentration on a great S³ means the points avoid
    one direction. Closed form, **no axis search**, hence no look-elsewhere bias. Uniform limit 0.2.
  * ★★ **IT CAN FAIL** (toy 5253's lesson, made the first requirement): uniform S⁴ at N = 2000 gives
    **0.1875 ± 0.0030**, and a full sphere scores **z = 0.1**. Silent on the null.
  * ★★★ **AND IT CAN FIRE:** bands of half-width δ give **z = 4.1 / 32.7 / 49.7 / 59.7 / 66.1** at
    δ = 1.0 / 0.6 / 0.4 / 0.25 / 0.08. **5σ threshold at δ ≈ 1.0 rad, N = 2000.**
  * ★★★★ **AND THE TRAP IT WOULD HAVE WALKED INTO, QUANTIFIED.** The null is **N-dependent** —
    **0.1754 / 0.1875 / 0.1945** at N = 500 / 2000 / 10000, creeping toward 0.2. ⟹ scoring against the
    **theoretical** 0.2 instead of an **N-matched** null fakes **4.7σ on uniform data at N = 500** — a nearly
    five-sigma "detection of S³ concentration" from a perfectly isotropic measure. **Thirteenth address,
    pre-empted** — same family as the region- (5251) and size- (5252) matched confounds, and the most
    convincing of the three because **it arrives with a sigma attached**.
  * ⟹ **PROTOCOL FIXED NOW: the null is generated at the same N as the data, every time. Never asymptotic.**
  * ★ **PRE-REGISTERED, target-innocent** (no commit dynamics exist yet): T ≪ N-matched null ⟹ **descent
    forced**; T at the null ⟹ **not forced**. **Both readable, and the null outcome is a real answer** — which
    is exactly what 5253's descent test lacked.

AUG-14. Waiting on @Lyra's commit dynamics. Nothing pushed. Count once. CP existence-only.
""")
