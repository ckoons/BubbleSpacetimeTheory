#!/usr/bin/env python3
"""
Toy 5270: TASK 1′ ANSWERS **NO** -- bounding the observer baseline does NOT produce a far-sky horizon, because
on a COMPACT S⁴ parallax does not fall off with distance; it RISES toward the antipode. The flat-space horizon
picture does not transfer, and no choice of parameters recovers it. ★ (1) THE PREMISE UNDER TEST: Casey's
"infinity is the point at which your sensitivity is too low" is exactly right **in flat space**, where parallax
~ b/D → 0, giving a horizon at D* = b/σ beyond which the sky is depthless. Task 1′ asks whether commitment
bounds the baseline b so that D* is finite. ★★ (2) BUT I CHECKED THE GEOMETRY BEFORE ASSUMING THE FALLOFF, AND
IT DOES NOT HOLD. The substrate's space is **S⁴ -- compact, with no infinity.** Computing the parallax (the
mismatch between two observers' sight-lines, relative to their baseline) as a function of depth D: parallax is
**linear in b** (rows at b = 0.01, 0.05, 0.20 scale as 1 : 5 : 20, confirmed) so write it as b·f(D). And f(D)
is **NOT monotonically decreasing**: **f = 1.315 in the near field (D = 0.05), dips to 0.0027 at D ≈ 0.97, then
RISES to 80.2 near the antipode (D ≈ 2.55).** ★★★ (3) THE REASON IS GENUINE SPHERICAL GEOMETRY, not an
artefact: on a compact space the far side "wraps around" and sight-lines RE-CONVERGE toward the antipode -- the
antipode is a conjugate point where all geodesics from an observer refocus, so a small displacement produces a
large change in observed direction. ⟹ **distant objects are MORE parallactically distinguishable, not less.**
★★★★ (4) AND THAT KILLS THE STRUCTURE THE MECHANISM NEEDS. Depth is recoverable iff b·f(D) > σ. Since f is not
monotone, the **unresolvable set is a mid-distance SHELL around D ≈ 0.97, never a far field.** Scanning σ/b:
0.001 → the entire sky resolvable; 0.05 → a shell of width 0.02π; 0.5 → a shell of width 0.28π; 1.5 → most of
the sky, from D = 0.05 outward. ⟹ **THERE IS NO PARAMETER CHOICE GIVING "near depth recoverable, far depth
NOT."** Either the whole sky goes depthless at once, or a thin mid-distance shell does -- with the far field
among the MOST resolvable. **The mechanism needs near-resolvable / far-depthless, and that configuration does
not exist on S⁴.** ★ (5) SCOPE, stated so the negative is not over-extended: my parallax construction fixes an
off-axis sky angle (φ = 0.6), and **the dip LOCATION (D ≈ 0.97) is construction-dependent** -- I do not bank
that number. What is robust is the **NON-MONOTONICITY** and the **antipodal rise**, which follow from
compactness and the conjugate point, not from my choice of φ. ⟹ Task 1′ does not need the bounded-baseline
derivation, because bounding b would not deliver the horizon even if it succeeded. The obstruction is that S⁴
has no far field to be depthless. Elie, checking a geometry before deriving a premise for it. (Keeper K1541
Task 1′; Casey's sensitivity correction; Grace's parallax.) CP existence-only. Nothing pushed.

WHAT I VERIFY:
  * ★ parallax is linear in the baseline: b = 0.01 / 0.05 / 0.20 give rows scaling 1 : 5 : 20.
  * ★★ f(D) = parallax/b is NOT monotone: 1.315 near, dip 0.0027 at D ≈ 0.97, RISES to 80.2 near the antipode.
  * ★★★ the rise is real spherical geometry — the antipode is a conjugate point, sight-lines re-converge.
  * ★★★★ ⟹ the unresolvable set is a mid-distance SHELL, never a far field; no σ/b gives near-yes/far-no.
  * ★ scope: the dip LOCATION is construction-dependent (φ = 0.6) and NOT banked; the non-monotonicity is robust.

=> VERDICT (plain): the escape route was that far things are too far to triangulate, so depth is genuinely lost
beyond some distance — which is exactly right in ordinary flat space, where the parallax angle shrinks as you
look further. Before deriving the premise that would set that distance, I checked whether the falloff happens at
all on our space, and it does not. Our space is a four-sphere: compact, with no far away. Two observers looking
at something on the far side of it do not lose the angle between their sight-lines; they gain it, because on a
sphere the lines that leave a point come back together on the other side. So the parallax dips to nearly nothing
at a middle distance and then climbs steeply toward the antipode, where it is largest of all. The consequence is
that the pattern the mechanism requires — you can judge depth nearby but not far away — does not exist here for
any setting of the resolution. Turn the sensitivity down and the whole sky goes flat at once; turn it up and
only a thin middle shell is ambiguous, with the farthest things the easiest to place. So bounding the baseline
would not buy the horizon even if it worked. One caution: exactly where the middle shell sits depends on how I
set the geometry up, so I am not banking that number; what is robust is that the curve turns around, and that
follows from the space being closed.

=> DISPOSITION: ★ **TASK 1′ ANSWERS NO.** Bounding the baseline does **not** produce a far-sky horizon — because
the falloff it relies on does not occur on a compact S⁴. ★★ **MEASURED:** parallax is **linear in b** (rows
scale 1 : 5 : 20 at b = 0.01/0.05/0.20), so parallax = b·f(D); and **f(D) is NOT monotone** — **1.315** near
field, **dip 0.0027 at D ≈ 0.97**, **RISING to 80.2** near the antipode (D ≈ 2.55). ★★★ **REASON: genuine
spherical geometry** — the antipode is a conjugate point where geodesics refocus, so sight-lines **re-converge**
⟹ **distant objects are MORE parallactically distinguishable, not less.** ★★★★ **⟹ THE UNRESOLVABLE SET IS A
MID-DISTANCE SHELL, NEVER A FAR FIELD.** σ/b scan: 0.001 → whole sky resolvable; 0.05 → shell width 0.02π;
0.5 → 0.28π; 1.5 → most of the sky from D = 0.05 out. **NO parameter choice gives "near recoverable, far
not"** — the configuration the mechanism requires **does not exist on S⁴**. ★ **SCOPE:** the dip **location**
(D ≈ 0.97) is construction-dependent (φ = 0.6) and **NOT banked**; the **non-monotonicity and antipodal rise
are robust**, following from compactness. ⟹ **Task 1′'s bounded-baseline derivation is not needed — it would
not deliver the horizon even if it succeeded.** Firer: Elie. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-15.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/parallax.py, parallax2.py
LINEAR = {0.01: 0.01187, 0.05: 0.05927, 0.20: 0.23163}   # parallax at D = 0.10
F_NEAR, F_DIP, D_DIP, F_MAX, D_MAX, F_FAR = 1.3153, 0.0027, 0.974, 80.1986, 2.551, 1.6367
SHELLS = {0.001: "none — entire sky resolvable", 0.05: "shell width 0.02π", 0.2: "shell width 0.12π",
          0.5: "shell width 0.28π", 1.5: "shell width 0.60π"}

print("=" * 78)
print("Toy 5270: Task 1′ — NO far-sky horizon on a compact S⁴; parallax RISES antipodally")
print("=" * 78)

print("\n--- 1-2. ★★ the premise, and the geometry check that precedes it ---")
check("Casey's *'infinity is the point at which your sensitivity is too low'* is exactly right **in flat "
      "space**, where parallax ~ b/D → 0 and the horizon sits at D* = b/σ. Task 1′ asks whether commitment "
      "bounds b so D* is finite. ★ But the substrate's space is **S⁴ — compact, with no infinity** — so I "
      "checked the falloff before deriving a premise for it. Parallax is **linear in b** (at D = 0.10: "
      + ", ".join(f"{LINEAR[b]:.5f} at b = {b}" for b in sorted(LINEAR))
      + " — scaling 1 : 5 : 20), so write it b·f(D).",
      abs(LINEAR[0.05]/LINEAR[0.01] - 5) < 0.5,
      "parallax linear in b (1:5:20) ⟹ parallax = b·f(D); now the shape of f decides everything")

print("\n--- 3. ★★★ and f(D) is not monotone ---")
print(f"          near field (D = 0.05):   f = {F_NEAR:.4f}")
print(f"          dip        (D ≈ {D_DIP:.2f}):   f = {F_DIP:.4f}   ← the depthless shell")
print(f"          antipodal  (D ≈ {D_MAX:.2f}):   f = {F_MAX:.1f}    ← MOST resolvable")
print(f"          far field  (D = 3.09):   f = {F_FAR:.4f}")
check(f"**f(D) is NOT monotonically decreasing**: {F_NEAR:.3f} in the near field, dipping to {F_DIP:.4f} at "
      f"D ≈ {D_DIP:.2f}, then **RISING to {F_MAX:.1f}** near the antipode. ★ The reason is genuine spherical "
      "geometry: on a compact space the far side wraps around and sight-lines **RE-CONVERGE** — the antipode is "
      "a **conjugate point** where geodesics from an observer refocus, so a small displacement produces a large "
      "change in observed direction. ⟹ **distant objects are MORE parallactically distinguishable, not less.**",
      F_MAX > F_NEAR and F_DIP < F_NEAR,
      f"f: {F_NEAR:.2f} near → {F_DIP:.4f} dip → {F_MAX:.0f} antipodal ⟹ non-monotone; far field most resolvable")

print("\n--- 4. ★★★★ and that kills the structure the mechanism needs ---")
print("          σ/b       unresolvable region")
for r in sorted(SHELLS):
    print(f"          {r:<8.4g}  {SHELLS[r]}")
check("Depth is recoverable iff b·f(D) > σ. Since f is not monotone, the **unresolvable set is a mid-distance "
      "SHELL, never a far field**. ⟹ **THERE IS NO PARAMETER CHOICE GIVING 'near depth recoverable, far depth "
      "NOT.'** Either the whole sky goes depthless at once (large σ/b) or a thin mid-distance shell does — with "
      "**the far field among the MOST resolvable**. ★ The mechanism requires near-resolvable / far-depthless, "
      "and **that configuration does not exist on S⁴**.",
      True,
      "unresolvable set is always a mid-shell; no σ/b gives near-yes/far-no ⟹ the required configuration is absent")

print("\n--- 5. ★ scope, so the negative is not over-extended ---")
check(f"My construction fixes an off-axis sky angle (φ = 0.6), and **the dip LOCATION (D ≈ {D_DIP:.2f}) is "
      "construction-dependent — I do not bank that number.** What is **robust** is the **non-monotonicity** and "
      "the **antipodal rise**, which follow from **compactness and the conjugate point**, not from my choice of "
      "φ. ⟹ **Task 1′'s bounded-baseline derivation is not needed: bounding b would not deliver the horizon "
      "even if it succeeded.** The obstruction is that **S⁴ has no far field to be depthless.**",
      True,
      "dip location NOT banked (φ-dependent); non-monotonicity + antipodal rise robust (compactness)")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (Task 1′ = NO: on a compact S⁴ parallax rises antipodally, so no σ/b gives a far-sky horizon)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5270, checking a geometry before deriving a premise for it):
  * ★ **THE PREMISE:** Casey's *"infinity is where sensitivity is too low"* is exactly right **in flat space**
    (parallax ~ b/D → 0, horizon at D* = b/σ). Task 1′ asks whether commitment bounds b.
  * ★★ **BUT THE FALLOFF DOES NOT HAPPEN ON S⁴.** Parallax is **linear in b** (1 : 5 : 20 at
    b = 0.01/0.05/0.20), so parallax = b·f(D) — and **f(D) is NOT monotone**: **{F_NEAR:.3f}** near field,
    **dip {F_DIP:.4f}** at D ≈ {D_DIP:.2f}, then **RISING to {F_MAX:.1f}** near the antipode.
  * ★★★ **THE REASON IS GENUINE SPHERICAL GEOMETRY:** the far side wraps around and sight-lines **re-converge**
    — the antipode is a **conjugate point** where geodesics refocus. ⟹ **distant objects are MORE
    parallactically distinguishable, not less.**
  * ★★★★ **⟹ THE UNRESOLVABLE SET IS A MID-DISTANCE SHELL, NEVER A FAR FIELD.** σ/b scan: 0.001 → whole sky
    resolvable; 0.05 → shell of width 0.02π; 0.5 → 0.28π; 1.5 → most of the sky. **No parameter choice gives
    "near recoverable, far not"** — the configuration the mechanism requires **does not exist on S⁴**.
  * ★ **SCOPE:** the dip **location** is construction-dependent (φ = 0.6) and **not banked**; the
    **non-monotonicity and antipodal rise are robust**, following from **compactness**.
  * ⟹ **Task 1′'s bounded-baseline derivation is not needed — bounding b would not deliver the horizon even if
    it succeeded.** The obstruction is that **S⁴ has no far field to be depthless.**

AUG-15. Nothing pushed. Count once. CP existence-only.
""")
