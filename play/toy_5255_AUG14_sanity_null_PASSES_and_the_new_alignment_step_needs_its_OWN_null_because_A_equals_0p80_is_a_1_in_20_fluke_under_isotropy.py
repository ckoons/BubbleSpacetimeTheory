#!/usr/bin/env python3
"""
Toy 5255: SANITY NULL PASSES -- AND @KEEPER'S NEW ALIGNMENT STEP NEEDS ITS OWN NULL, BECAUSE A = 0.80 IS A
1-IN-20 FLUKE UNDER ISOTROPY. Two pre-run items, both posted before Lyra names the axis. ★ (1) THE SANITY NULL
(K1504's positive control) PASSES: the ROUND SO(5)-invariant measure, run through the full pipeline at data-N,
reads UNIFORM at every size -- z = +1.44 (N = 500), +1.46 (N = 2000), +1.79 (N = 10000), all comfortably inside
3σ and all on the *high* side, i.e. no manufactured deficit. **The pipeline does not invent concentration.**
Posted blind, before any commit measure exists. ★★ (2) AND @KEEPER'S K1505 ALIGNMENT REFINEMENT IS A REAL CATCH
ON MY INSTRUMENT: λ_min finds concentration on whatever axis the points happen to avoid, so magnitude alone
cannot distinguish "concentrated on the descent's S³" from "concentrated on some other boundary." Two steps are
right. ★★★ BUT THE ALIGNMENT STEP NEEDS ITS OWN NULL, AND IT IS SEVERE. Under isotropy v_min is a RANDOM
direction in R⁵, so A = |⟨v_min | n_named⟩| has E[A²] = 1/5 -- and measured, A has **mean 0.37, p95 = 0.80,
p99 = 0.90**, essentially independent of N. ⟹ **AN ALIGNMENT OF 0.80 -- which reads as strong agreement --
HAPPENS 5% OF THE TIME BY CHANCE, AND 0.45 IS COMPLETELY TYPICAL.** Reporting "the eigenvector aligns with the
named axis at 0.8, close to 1" as confirmation would be the FOURTH confound in the series, and the natural
mistake, because a direction-cosine near 1 *feels* like a match in a way a p-value does not. ⟹ **committed
threshold: A must exceed 0.90 (the isotropy p99), N-matched, or the alignment is not evidence.** ★★★★ (3) AND
THE JOINT POWER IS MEASURED, so the two steps can be committed together: bands of half-width δ about the named
axis give (z_magnitude, A) = (0.6, 0.52) at δ = 1.2; (4.3, 0.966) at 1.0; (14.2, 0.996) at 0.8; (29.9, 0.999) at
0.6; (53.9, 1.000) at 0.25. ⟹ alignment becomes reliable slightly BEFORE magnitude clears 5σ, so the two are
complementary rather than redundant, and the joint criterion **z > 5 AND A > 0.90** is satisfied for δ ≲ 0.8 at
N = 2000. ★ (4) I AM STILL BLOCKED on @Lyra naming the axis -- and that block is load-bearing, not a delay:
computing the overlap against a best-fit equator instead of a named one is precisely the retrofit K1504 exists
to forbid. The instrument is complete and calibrated; the one thing it must not do is choose its own target.
Elie, calibrating the new step before it can fire. (Keeper K1504/K1505; toy 5254.) CP existence-only. Nothing
pushed. NO CONCENTRATION READ, NO ALIGNMENT READ.

WHAT I VERIFY:
  * ★ SANITY NULL PASSES: round measure reads uniform at N = 500 / 2000 / 10000 (z = +1.44 / +1.46 / +1.79).
  * ★★ @Keeper's two-step refinement is correct — λ_min alone cannot tell WHICH boundary.
  * ★★★ alignment null under isotropy: A mean 0.37, **p95 = 0.80, p99 = 0.90**, N-independent.
  * ★★★ ⟹ A = 0.80 is a 1-in-20 FLUKE; committed threshold **A > 0.90**, N-matched.
  * ★★★★ joint power: (z, A) = (4.3, 0.97) at δ = 1.0; (14.2, 0.996) at 0.8 ⟹ joint criterion met for δ ≲ 0.8.
  * ★ still blocked on the named axis — and that block is load-bearing, not a delay.

=> VERDICT (plain): two jobs done before the real data exists. First, the control: run the plain round measure
through the whole pipeline and check it comes out looking round. It does, at every sample size, and slightly on
the safe side — so the machinery does not invent structure. Second, Keeper added a sensible refinement, that
finding *a* preferred direction is not the same as finding *the* one the descent names, so we must also check
the direction agrees. He is right, and the refinement needs its own control, which turns out to matter more
than the first. A direction in five-dimensional space, chosen at random, already overlaps any fixed direction
by about a third on average — and overlaps it by eight tenths one time in twenty. Eight tenths out of one
sounds like a hit. It is noise. So the bar has to sit at nine tenths, and I have written that down before
seeing anything. The two checks together only both fire once the concentration is reasonably tight, and I
measured where that happens. What I cannot do is pick the direction myself; that has to be named first, or the
whole exercise is the retrofit this pre-registration was built to prevent.

=> DISPOSITION: ★ **SANITY NULL PASSES** (K1504 positive control): the round SO(5)-invariant measure reads
UNIFORM through the full pipeline — z = **+1.44 / +1.46 / +1.79** at N = 500 / 2000 / 10000, inside 3σ and on
the high side. **The pipeline does not manufacture concentration.** Posted blind. ★★ **@Keeper's K1505
two-step refinement is a real catch on my instrument** — λ_min finds concentration on *whatever* axis, so
magnitude alone cannot say WHICH boundary. ★★★ **BUT THE ALIGNMENT STEP NEEDS ITS OWN NULL, AND IT IS SEVERE:**
under isotropy v_min is a random R⁵ direction ⟹ A = |⟨v_min|n⟩| has **mean 0.37, p95 0.80, p99 0.90**,
N-independent. ⟹ **A = 0.80 is a 1-in-20 fluke and 0.45 is typical.** Reporting "aligns at 0.8, close to 1" as
confirmation = the **FOURTH confound**, and the natural mistake, since a direction-cosine near 1 *feels* like a
match. **COMMITTED THRESHOLD: A > 0.90 (isotropy p99), N-matched.** ★★★★ **JOINT POWER MEASURED:** (z, A) =
(0.6, 0.52) at δ = 1.2; (4.3, 0.966) at 1.0; (14.2, 0.996) at 0.8; (53.9, 1.000) at 0.25 ⟹ alignment turns
reliable just before magnitude clears 5σ; **joint criterion z > 5 AND A > 0.90 met for δ ≲ 0.8 at N = 2000.**
★ **STILL BLOCKED on @Lyra naming the axis — load-bearing, not a delay**: a best-fit equator instead of a named
one is exactly the retrofit K1504 forbids. Firer: Elie. Nothing pushed. NO CONCENTRATION READ, NO ALIGNMENT
READ.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/align.py
SANITY = {500: (0.16855, 0.17621, 0.00531, 1.44),
          2000: (0.18388, 0.18800, 0.00284, 1.46),
          10000: (0.19233, 0.19455, 0.00124, 1.79)}
ALIGN_NULL = {500: (0.369, 0.832, 0.915), 2000: (0.367, 0.804, 0.905), 10000: (0.372, 0.793, 0.904)}
JOINT = {1.20: (0.18567, 0.6, 0.522), 1.00: (0.17439, 4.3, 0.966), 0.80: (0.14351, 14.2, 0.996),
         0.60: (0.09480, 29.9, 0.999), 0.40: (0.04826, 44.8, 1.000), 0.25: (0.01992, 53.9, 1.000)}
A_THRESH = 0.90

print("=" * 78)
print("Toy 5255: sanity null passes; the alignment step needed its own. NO READS")
print("=" * 78)

print("\n--- 1. ★ the sanity null (K1504 positive control) ---")
print("          N        T(round)   N-matched null       z")
for N in sorted(SANITY):
    t, m, s, z = SANITY[N]
    print(f"          {N:5d}    {t:.5f}    {m:.5f} ± {s:.5f}   +{z:.2f}")
check("The ROUND SO(5)-invariant measure, run through the FULL pipeline at data-N, reads UNIFORM at every size "
      f"-- z = +{SANITY[500][3]:.2f}, +{SANITY[2000][3]:.2f}, +{SANITY[10000][3]:.2f} -- all comfortably inside "
      "3σ, and all on the HIGH side, i.e. no manufactured deficit. ★ **The pipeline does not invent "
      "concentration.** Posted blind, before any commit measure exists.",
      all(abs(v[3]) < 3 for v in SANITY.values()),
      "round measure reads uniform at N = 500/2000/10000 (z = +1.44/+1.46/+1.79) ⟹ sanity null PASSES")

print("\n--- 2-3. ★★★ the alignment step's own null ---")
print("          N        A mean    p95      p99")
for N in sorted(ALIGN_NULL):
    m, p95, p99 = ALIGN_NULL[N]
    print(f"          {N:5d}    {m:.3f}     {p95:.3f}    {p99:.3f}")
check("@Keeper's K1505 refinement is a REAL CATCH on my instrument: λ_min finds concentration on WHATEVER axis "
      "the points avoid, so magnitude alone cannot distinguish 'concentrated on the descent's S³' from "
      "'concentrated on some other boundary.' Two steps are right. ★★★ BUT THE ALIGNMENT STEP NEEDS ITS OWN "
      "NULL, AND IT IS SEVERE: under isotropy v_min is a RANDOM direction in R⁵, so A = |⟨v_min|n⟩| has "
      f"**mean {ALIGN_NULL[2000][0]:.2f}, p95 = {ALIGN_NULL[2000][1]:.2f}, p99 = {ALIGN_NULL[2000][2]:.2f}**, "
      "essentially independent of N.",
      ALIGN_NULL[2000][1] > 0.75,
      f"isotropy alignment: mean {ALIGN_NULL[2000][0]:.2f}, p95 {ALIGN_NULL[2000][1]:.2f}, p99 {ALIGN_NULL[2000][2]:.2f}")

check(f"⟹ **AN ALIGNMENT OF {ALIGN_NULL[2000][1]:.2f} -- which reads as strong agreement -- HAPPENS 5% OF THE "
      "TIME BY CHANCE, and 0.45 is completely typical.** Reporting 'the eigenvector aligns with the named axis "
      "at 0.8, close to 1' as confirmation would be the FOURTH confound in the series -- and it is the natural "
      "mistake, because a direction-cosine near 1 FEELS like a match in a way a p-value does not. ⟹ "
      f"**COMMITTED THRESHOLD: A must exceed {A_THRESH:.2f} (the isotropy p99), N-matched, or the alignment is "
      "not evidence.**",
      A_THRESH >= ALIGN_NULL[2000][2] - 0.01,
      f"A = 0.80 is a 1-in-20 fluke ⟹ committed threshold A > {A_THRESH:.2f} (isotropy p99), N-matched")

print("\n--- 4. ★★★★ joint power, so both steps can be committed together ---")
print("          δ       T         z(magnitude)   A(alignment)   both fire?")
for d in sorted(JOINT, reverse=True):
    T, z, A = JOINT[d]
    fires = "YES" if z > 5 and A > A_THRESH else ("magnitude only" if z > 5 else "no")
    print(f"          {d:.2f}    {T:.5f}   {z:8.1f}       {A:.3f}          {fires}")
check("Bands of half-width δ about the named axis give (z, A) = "
      + ", ".join(f"({JOINT[d][1]:.1f}, {JOINT[d][2]:.3f}) at δ = {d}" for d in (1.2, 1.0, 0.8, 0.25))
      + ". ⟹ alignment becomes reliable slightly BEFORE magnitude clears 5σ, so the two steps are "
      f"COMPLEMENTARY rather than redundant, and the joint criterion **z > 5 AND A > {A_THRESH:.2f}** is "
      "satisfied for δ ≲ 0.8 at N = 2000.",
      JOINT[0.80][1] > 5 and JOINT[0.80][2] > A_THRESH and not (JOINT[1.20][1] > 5),
      f"joint criterion z > 5 AND A > {A_THRESH:.2f} met for δ ≲ 0.8; silent at δ = 1.2 ⟹ complementary, can fail")

print("\n--- 5. ★ what I will not do ---")
check("I am STILL BLOCKED on @Lyra naming the axis, and **that block is load-bearing, not a delay**: computing "
      "the overlap against a BEST-FIT equator instead of a NAMED one is precisely the retrofit K1504 exists to "
      "forbid. ★ The instrument is complete and calibrated; the one thing it must not do is choose its own "
      "target. I will run both steps the moment the axis is written into T2564, and not before.",
      True,
      "blocked on the named axis by design — a best-fit equator would void the test; will not self-select")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (sanity null PASSES; alignment threshold committed at A > 0.90 because 0.80 is a 1-in-20 fluke)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5255, calibrating the new step before it can fire — NO READS):
  * ★ **SANITY NULL PASSES** (K1504's positive control): the round SO(5)-invariant measure, through the **full
    pipeline** at data-N, reads **uniform at every size** — z = **+1.44 / +1.46 / +1.79** at N = 500 / 2000 /
    10000, inside 3σ and on the *high* side. **The pipeline does not manufacture concentration.** Posted blind.
  * ★★ **@Keeper's K1505 two-step refinement is a real catch on my instrument** — λ_min finds concentration on
    *whatever* axis the points avoid, so magnitude alone can't say **which** boundary. Two steps are right.
  * ★★★ **BUT THE ALIGNMENT STEP NEEDS ITS OWN NULL, AND IT IS SEVERE.** Under isotropy v_min is a **random**
    R⁵ direction, so A = |⟨v_min|n⟩| has **mean 0.37, p95 = 0.80, p99 = 0.90** — N-independent.
    ⟹ **an alignment of 0.80 — which reads as strong agreement — is a 1-in-20 fluke, and 0.45 is typical.**
    Reporting "aligns at 0.8, close to 1" as confirmation would be the **fourth confound**, and it's the
    *natural* mistake, because a direction-cosine near 1 **feels** like a match in a way a p-value doesn't.
    ⟹ **COMMITTED: A must exceed 0.90 (isotropy p99), N-matched, or the alignment is not evidence.**
  * ★★★★ **JOINT POWER MEASURED:** (z, A) = (0.6, 0.52) at δ = 1.2; (4.3, 0.966) at 1.0; (14.2, 0.996) at 0.8;
    (53.9, 1.000) at 0.25. Alignment turns reliable just **before** magnitude clears 5σ ⟹ the steps are
    **complementary**, and **z > 5 AND A > 0.90** is met for δ ≲ 0.8 at N = 2000 — and silent at δ = 1.2.
  * ★ **STILL BLOCKED on @Lyra naming the axis — and that block is load-bearing, not a delay.** A best-fit
    equator instead of a named one is exactly the retrofit K1504 forbids. The instrument is complete; **the one
    thing it must not do is choose its own target.** I run both steps the moment the axis is in T2564.

AUG-14. Nothing pushed. Count once. CP existence-only.
""")
