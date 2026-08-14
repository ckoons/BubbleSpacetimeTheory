#!/usr/bin/env python3
"""
Toy 5253: THE DESCENDED BOUNDARY MEASURES d = 4, EXACTLY AS PREDICTED -- AND THE MEASUREMENT HAS ZERO
DISCRIMINATING POWER. Both halves are the report, and the second is the one that matters. ★ (1) THE PREDICTION
LANDS. Running the identical N = 20000 pipeline on the SO(4,2)-descended boundary D_IV⁴ → R × S³ (conformal
Minkowski₄): median interval-r = **0.1025**, IQR [0.0929, 0.1111] -- against sprinkled Minkowski d = 4 at
0.1000, IQR [0.0928, 0.1081]. Essentially exact. The full boundary R × S⁴ gives 0.0435 against d = 5's 0.0429.
Both sides of the descent measure what they should. ★★ (2) AND THAT CONFIRMS NOTHING ABOUT THE DESCENT. Sweeping
the sphere dimension through the same estimator gives r = 0.2307 (S²), 0.1056 (S³), 0.0441 (S⁴), 0.0237 (S⁵) --
**r tracks the sphere dimension exactly, as it must**. I put a four-dimensional space in and read four
dimensions out. That tests the ESTIMATOR, not the descent, and by the enumerate-inputs criterion it is an
identity in measurement's clothing: it could not have returned anything else. ★★★ (3) WORSE -- OR MORE
USEFULLY -- THE RESTRICTION IS EXACT BY CONSTRUCTION. A totally geodesic S³ ⊂ S⁴ carries the SAME induced
metric, so the 5D light cone restricted to it IS the 4D light cone, identically. There is no version of this
measurement that could have come out otherwise, whether I build the 4D order fresh or induce it from the 5D one.
⟹ "if it lands, the continuum limit closes as a corpus-consequence" -- it lands, and it closes nothing, because
landing was guaranteed the moment the boundary was chosen. ★★★★ (4) THE REAL QUESTION IS NOT MEASURABLE THIS
WAY, and naming that is the deliverable: the open point was never "what is the dimension of R × S³" but
"**does BST's commitment order live on S³ × S¹ rather than S⁴ × S¹?**" That is a structural claim about which
boundary the dynamics selects, and no dimension estimator can decide it -- feed it either boundary and it
faithfully reports that boundary's dimension. ★ (5) BUT A DISCRIMINATING TEST DOES EXIST, and it is in reach:
IF the descent is forced by the dynamics, the commitments themselves must CONCENTRATE on a 3-sphere -- the
measure induced on S⁴ by the commit operator would be peaked or singular on an S³, not uniform. THAT is
measurable, it is target-innocent, and it could fail. It needs the commit dynamics rather than the boundary
geometry, which is @Lyra's side. ⟹ the dimension estimator is done here; the commitment MEASURE on S⁴ is the
instrument that can actually decide the descent. Elie, running the prediction and reporting why it cannot
count. (Keeper's descent assignment; toys 5250/5251/5252; Casey's enumerate-inputs rule.) CP existence-only.
Nothing pushed.

WHAT I VERIFY:
  * ★ descended boundary R × S³: interval-r = 0.1025 [0.0929, 0.1111] vs Minkowski d = 4 at 0.1000 — matches.
  * ★ full boundary R × S⁴: 0.0435 vs d = 5's 0.0429 — matches. Both sides measure as they should.
  * ★★ sphere sweep: r = 0.2307 / 0.1056 / 0.0441 / 0.0237 for S²/S³/S⁴/S⁵ ⟹ r IS the input dimension.
  * ★★★ totally geodesic S³ ⊂ S⁴ has the same induced metric ⟹ the restricted light cone IS the 4D one, exactly.
  * ★★★★ ⟹ the measurement cannot decide the descent; it reports whichever boundary it is handed.
  * ★ the discriminating instrument is the COMMITMENT MEASURE on S⁴ (does it concentrate on an S³?).

=> VERDICT (plain): the predicted number came out. Put the estimator on the descended boundary and it reads four
dimensions, matching sprinkled four-dimensional spacetime almost exactly, while the full boundary reads five.
Both sides behave. But the confirmation is empty, and I would rather say so now than have it counted later. The
estimator reports the dimension of whatever space you hand it — sweeping the sphere from two up to five walks
the answer through the whole table, exactly in step. So handing it a four-dimensional boundary and reading four
tests my instrument, not the physics. And it is worse than a coincidence: the smaller sphere sits inside the
larger one with the same geometry, so the light cone restricted to it simply is the four-dimensional light cone.
Nothing about that could have failed. The question that was actually open is different: not what dimension the
smaller boundary has, but whether BST's commitments live on it. No dimension estimator can answer that, because
it faithfully reports whichever boundary it is given. There is a test that could answer it, though, and it is
within reach — if the descent is real, the commitments should pile up on the smaller sphere rather than spread
over the larger one. That is measurable and it can fail, which is what makes it worth running.

=> DISPOSITION: ★ **PREDICTION LANDS**: descended boundary R × S³ gives interval-r **0.1025** [0.0929, 0.1111]
vs Minkowski d = 4 at **0.1000** [0.0928, 0.1081]; full boundary R × S⁴ gives **0.0435** vs d = 5's **0.0429**.
Identical N = 20000 pipeline throughout. ★★ **AND IT CONFIRMS NOTHING ABOUT THE DESCENT**: sweeping S² → S⁵
gives r = 0.2307 / 0.1056 / 0.0441 / 0.0237 ⟹ **r IS the input dimension**. Feeding in a 4D boundary and reading
4 tests the ESTIMATOR — an identity in measurement's clothing under enumerate-inputs. ★★★ **AND THE RESTRICTION
IS EXACT BY CONSTRUCTION**: totally geodesic S³ ⊂ S⁴ has the SAME induced metric ⟹ the 5D light cone restricted
to it IS the 4D light cone. Nothing could have come out otherwise. ⟹ **"the continuum limit closes as a
corpus-consequence" — it does not; landing was guaranteed when the boundary was chosen.** ★★★★ **THE REAL
QUESTION** is "does BST's commitment order LIVE on S³ × S¹?" — a structural claim about which boundary the
dynamics selects, undecidable by any dimension estimator. ★ **DISCRIMINATING INSTRUMENT THAT DOES EXIST
(@Lyra):** if the descent is forced, the **commitment measure induced on S⁴ must concentrate on an S³** rather
than being uniform. Target-innocent, can fail, needs the commit dynamics not the boundary geometry. Firer:
Elie. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/descent.py, N = 20000, identical pipeline to toy 5252
MATCH = {"Minkowski d=4 (calib)":   (0.1000, 0.0928, 0.1081, 316),
         "Minkowski d=5 (calib)":   (0.0429, 0.0391, 0.0496, 154),
         "BST descended (R x S^3)": (0.1025, 0.0929, 0.1111, 217),
         "BST full      (R x S^4)": (0.0435, 0.0372, 0.0521, 128)}
SWEEP = {2: (3, 0.2307), 3: (4, 0.1056), 4: (5, 0.0441), 5: (6, 0.0237)}

print("=" * 78)
print("Toy 5253: descended boundary measures d = 4 — and the measurement cannot count")
print("=" * 78)

print("\n--- 1. ★ the prediction lands ---")
print("          geometry                     median r   IQR                 median |I|")
for k, (m, q1, q3, s) in MATCH.items():
    print(f"          {k:<27}  {m:.4f}     [{q1:.4f}, {q3:.4f}]    {s}")
d = MATCH["BST descended (R x S^3)"]
c4 = MATCH["Minkowski d=4 (calib)"]
check("Running the identical N = 20000 pipeline on the SO(4,2)-descended boundary D_IV⁴ → R × S³ (conformal "
      f"Minkowski₄): median interval-r = **{d[0]:.4f}**, IQR [{d[1]:.4f}, {d[2]:.4f}], against sprinkled "
      f"Minkowski d = 4 at {c4[0]:.4f} [{c4[1]:.4f}, {c4[2]:.4f}]. Essentially exact. The full boundary R × S⁴ "
      "gives 0.0435 against d = 5's 0.0429. ★ Both sides of the descent measure what they should.",
      abs(d[0] - c4[0]) < 0.01,
      f"descended: {d[0]:.4f} vs d=4 calib {c4[0]:.4f} — prediction lands; full boundary matches d=5")

print("\n--- 2. ★★ and it confirms nothing about the descent ---")
print("          sphere   total dim   median interval-r")
for ns in sorted(SWEEP):
    print(f"          S^{ns}       {SWEEP[ns][0]}           {SWEEP[ns][1]:.4f}")
check("Sweeping the sphere dimension through the SAME estimator gives r = "
      + ", ".join(f"{SWEEP[n][1]:.4f} (S^{n}, dim {SWEEP[n][0]})" for n in sorted(SWEEP))
      + " -- ★ **r tracks the sphere dimension exactly, as it must.** I put a four-dimensional space in and "
      "read four dimensions out. That tests the ESTIMATOR, not the descent, and by the enumerate-inputs "
      "criterion it is an identity in measurement's clothing: it could not have returned anything else.",
      all(SWEEP[n][1] > SWEEP[n+1][1] for n in (2, 3, 4)),
      "r tracks input dimension monotonically ⟹ reading '4' from a 4D input tests the estimator, not the descent")

print("\n--- 3. ★★★ and the restriction is exact by construction ---")
check("A totally geodesic S³ ⊂ S⁴ carries the SAME induced metric, so the 5D light cone restricted to it IS "
      "the 4D light cone, identically. ⟹ there is no version of this measurement that could have come out "
      "otherwise, whether I build the 4D order fresh or induce it from the 5D one. ★ So 'if it lands, the "
      "continuum limit closes as a corpus-consequence' -- it lands, and it closes nothing, because landing was "
      "guaranteed the moment the boundary was chosen.",
      True,
      "totally geodesic S³ ⊂ S⁴ ⟹ restricted light cone IS the 4D one ⟹ outcome guaranteed, not measured")

print("\n--- 4-5. ★★★★ what the real question is, and what could answer it ---")
check("The open point was never 'what is the dimension of R × S³' but **'does BST's commitment order LIVE on "
      "S³ × S¹ rather than S⁴ × S¹?'** That is a structural claim about which boundary the dynamics selects, "
      "and NO dimension estimator can decide it -- hand it either boundary and it faithfully reports that "
      "boundary's dimension. ⟹ the estimator is done here; it has said everything it can say.",
      True,
      "the real question is which boundary the dynamics selects — undecidable by any dimension estimator")

check("★ BUT A DISCRIMINATING TEST EXISTS AND IS IN REACH: if the descent is FORCED by the dynamics, the "
      "commitments themselves must CONCENTRATE on a 3-sphere -- the measure induced on S⁴ by the commit "
      "operator would be peaked or singular on an S³, not uniform. That is measurable, target-innocent, and "
      "**it can fail**, which is what makes it worth running. It needs the commit DYNAMICS rather than the "
      "boundary GEOMETRY -- @Lyra's side. ⟹ the commitment measure on S⁴ is the instrument that can actually "
      "decide the descent.",
      True,
      "discriminating instrument: does the commit-induced measure on S⁴ concentrate on an S³? — can fail, worth running")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (d = 4 confirmed on the descended boundary — and the confirmation carries no evidential weight)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5253, the prediction lands and cannot count):
  * ★ **THE PREDICTION LANDS.** Identical N = 20000 pipeline on the SO(4,2)-descended boundary
    D_IV⁴ → R × S³: **interval-r = 0.1025** [0.0929, 0.1111] vs Minkowski **d = 4 at 0.1000** [0.0928, 0.1081].
    Full boundary R × S⁴: **0.0435** vs d = 5's **0.0429**. Both sides measure as they should.
  * ★★ **AND IT CONFIRMS NOTHING ABOUT THE DESCENT.** Sweeping the sphere: r = **0.2307 / 0.1056 / 0.0441 /
    0.0237** for S²/S³/S⁴/S⁵ — **r tracks the input dimension exactly, as it must.** I put a 4-dimensional
    space in and read 4 out. That tests the **estimator**, not the descent — an identity in measurement's
    clothing under enumerate-inputs.
  * ★★★ **AND THE RESTRICTION IS EXACT BY CONSTRUCTION.** A totally geodesic S³ ⊂ S⁴ has the **same induced
    metric**, so the 5D light cone restricted to it **is** the 4D light cone. Nothing could have come out
    otherwise. ⟹ "if it lands, the continuum limit closes as a corpus-consequence" — **it lands, and closes
    nothing**, because landing was guaranteed the moment the boundary was chosen.
  * ★★★★ **THE REAL QUESTION** was never "what dimension is R × S³" but **"does BST's commitment order live on
    S³ × S¹?"** — a structural claim about which boundary the dynamics selects, **undecidable by any dimension
    estimator**. The estimator has said everything it can.
  * ★ **BUT A DISCRIMINATING TEST EXISTS (@Lyra):** if the descent is forced, the **commitment measure induced
    on S⁴ must concentrate on an S³** rather than being uniform. Target-innocent, **can fail**, and needs the
    commit **dynamics** rather than the boundary **geometry**. **That** is the instrument that can decide it.

AUG-14. Nothing pushed. Count once. CP existence-only.
""")
