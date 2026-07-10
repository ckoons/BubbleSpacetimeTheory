#!/usr/bin/env python3
"""
Toy 4610 — Jul 10 (mode-spread / range-reframe discipline). Grace retracted the light-sector "hit"
(Cal caught a norm-square slip: un-squared (1−r²) instead of (1−r²)² → exponent −n_C/2 instead of
−n_C). With the correct squared norm, s/d = 2.49 (a miss). Casey reframed mass as a FLOOR + a RANGE
(the ribbon width), success = the derived range brackets the physical smear. My fish-detector job
(Casey's own guard: "width must be DERIVED, not fit; a tunable range is peanut butter") is to check
whether the DERIVED width brackets, or whether the huge scheme window is doing the work. It's the latter.

THE NUMBERS:
  s/d: refraction (corrected, squared norm) = 2.49 · odd-ladder = 4.21 · target ~1.5 (constituent)
  physical smear: [1.45 (constituent) .. 20 (current MS-bar)] — a FACTOR ~14 wide window.
  2.49 ∈ [1.45, 20]? YES — but that only says 2.49 sits somewhere in a factor-14 window.

TWO DISTINCT "WIDTHS" (do not conflate — this is the discipline):
  (i) the DERIVED ribbon / mode-spread width = the two-tier precision floor ~10⁻² ≈ 1% (Toy 3648,
      established). This is the INTRINSIC width the ribbon actually has. NARROW.
  (ii) the SCHEME smear [1.45, 20] = the confinement DRESSING (current↔constituent), factor ~14. WIDE.
      This is NOT the ribbon width — it is a separate (dressing) quantity.

THE HONEST TEST (with the DERIVED width, per Casey's guard):
  s/d = 2.49 ± 1% = [2.47, 2.51]. Does it bracket the constituent target ~1.45? NO. Still a MISS
  (2.49 vs 1.45). Only the FACTOR-14 scheme window "brackets" 2.49 — and cashing that as a consistency
  win is exactly the peanut butter Casey warned against (a factor-14 window brackets almost anything).

⟹ VERDICT (Cal's guard held): the DERIVED ribbon width does NOT rescue the miss. Refraction is CLOSER
than the ladder (2.49 vs 4.21, target ~1.5) but still MISSES s/d. The range reframe is legitimate
physics (mass IS smeared — the ribbon has width), but the honest test uses the DERIVED (~1%) width,
which doesn't bracket; the factor-14 scheme smear is dressing, not the ribbon, and must not be cashed.

The exact ribbon width (mode-spread) is FK-gated (needs the Wallach measure) — I use the established
two-tier ~1% estimate and flag the exact value open. My J rep-support (4609) stands. Not a bank; the
mass sector stays open/miss, honestly. Count ~7-8 (α RULED).
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

sd_ref, sd_ladder, sd_const, sd_curr = 2.49, 4.21, 1.45, 20.0
print("=" * 82)
print("Toy 4610 — range-reframe discipline: derived ribbon width (~1%) does NOT bracket; don't cash the factor-14 window")
print("=" * 82)

print(f"\n[the numbers]: s/d refraction(corrected)={sd_ref}; ladder={sd_ladder}; target~1.5; physical smear [{sd_const}..{sd_curr}] (factor {sd_curr/sd_const:.0f})")
check("s/d = 2.49 (squared norm, corrected) is a MISS vs ~1.5 — the un-squared norm gave the retracted 1.58; refraction is closer than the ladder (4.21) but misses",
      sd_ref > 2, "Grace's retraction stands; both ladder and point-refraction miss the ~1.5 target")

# ---- two distinct widths ----------------------------------------------------
print(f"\n[TWO distinct widths — do not conflate]:")
print(f"  (i) DERIVED ribbon/mode-spread width ≈ 1% (two-tier floor, Toy 3648) — the intrinsic width. NARROW.")
print(f"  (ii) SCHEME smear [{sd_const},{sd_curr}] = the confinement DRESSING (factor {sd_curr/sd_const:.0f}). WIDE — NOT the ribbon width.")
check("the DERIVED ribbon width (~1%) and the SCHEME smear (factor 14) are DIFFERENT quantities — the smear is dressing, not the ribbon",
      True, "the ribbon width is the two-tier ~1% floor; the [1.45,20] smear is the current↔constituent confinement dressing")

# ---- the honest test --------------------------------------------------------
lo, hi = sd_ref*0.99, sd_ref*1.01
print(f"\n[the honest test — with the DERIVED width]: s/d = 2.49 ± 1% = [{lo:.2f}, {hi:.2f}]")
print(f"  brackets the constituent target ~{sd_const}? {'YES' if lo <= sd_const <= hi else 'NO'} → still a MISS.")
check("with the DERIVED (~1%) width, s/d=2.49±1% does NOT bracket the ~1.45 target — still a MISS; only the factor-14 window 'brackets' (peanut butter)",
      not (lo <= sd_const <= hi), "Casey's guard: a tunable/huge range is peanut butter; the derived width is the honest one and it misses")

# ---- verdict ----------------------------------------------------------------
check("VERDICT (Cal's guard held): the range reframe is legit (mass IS smeared) but the DERIVED width doesn't rescue the miss; don't cash the scheme window",
      True, "refraction closer than the ladder, still misses s/d; the exact ribbon width is FK-gated; mass sector stays open/miss honestly")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
RANGE-REFRAME DISCIPLINE (holding Casey's own guard — width derived, not the window cashed):
  * Grace's retraction stands: s/d = 2.49 (squared norm), a MISS vs ~1.5 (the un-squared norm gave the
    retracted 1.58). Refraction is closer than the odd-ladder (4.21) but still misses.
  * TWO distinct widths: the DERIVED ribbon/mode-spread width ≈ 1% (two-tier floor) — intrinsic, NARROW;
    the SCHEME smear [1.45,20] = confinement DRESSING, factor 14, WIDE — NOT the ribbon width.
  * HONEST TEST: with the DERIVED (~1%) width, s/d=2.49±1% does NOT bracket the ~1.45 target → still a
    MISS. Only the factor-14 scheme window "brackets" 2.49 — cashing that is peanut butter (Casey's guard).
  * VERDICT: the range reframe is legitimate (mass is smeared), but the derived width doesn't rescue the
    miss; the scheme smear is dressing, not the ribbon. Exact ribbon width FK-gated. Mass sector open/miss.
  Count ~7-8 (α RULED). Cal's guard held on the day's range reframe.
""")
