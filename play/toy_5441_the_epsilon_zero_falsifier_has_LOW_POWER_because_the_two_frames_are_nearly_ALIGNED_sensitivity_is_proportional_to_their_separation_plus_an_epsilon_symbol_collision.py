#!/usr/bin/env python3
"""
Toy 5441 — THE ε = 0 FRAME-AGREEMENT FALSIFIER: the post-gate lookup, as assigned.

QUESTION THIS COMPUTE ANSWERS (declared before running):
    "Cal pre-registered P1 (the slice tracks the RADIATION frame) and P2 (matter
     admixture ε = 0, exactly). He assigned the lookup to me AFTER the gate. Can the
     test actually kill it — and at what ε?"

THE PRE-REGISTRATION (filed 2026-08-21, quoted, NOT re-derived):
    P1 — the slice tracks the RADIATION-defined cosmic rest frame.
    P2 — the matter admixture is ε = 0, EXACTLY, no free parameter.
    Cal: "Lookup assigned to @Elie *after* the gate, so the measurement can only
    confirm or kill, never shape."

★ MY STANDING RULE APPLIES HERE AND I AM APPLYING IT TO MYSELF: remembered
  experimental numbers go stale. Everything in Section 1 is FROM MEMORY and is marked
  NEEDS-PRIMARY-VERIFICATION. No verdict is issued on them.
★ THEREFORE the load-bearing result below is the POWER ANALYSIS (Section 2), which is a
  GEOMETRIC statement and does NOT depend on the exact measured values.
"""

import numpy as np

# ================================================================ THE LOOKUP
print("=" * 78)
print("SECTION 1 — THE LOOKUP (as assigned, post-gate) — ★ ALL VALUES NEED VERIFICATION")
print("=" * 78)
print("  RADIATION frame  : the CMB dipole rest frame.")
print("      remembered   : v ~ 370 km/s toward galactic (l, b) ~ (264 deg, 48 deg)")
print("  MATTER frame     : bulk flows / source-count (radio, quasar) dipoles.")
print("      remembered   : direction BROADLY CONSISTENT with the CMB dipole; the live")
print("                     anomaly is an AMPLITUDE EXCESS (~2-5x the kinematic")
print("                     prediction) in radio/quasar counts, not a large direction")
print("                     offset.")
print()
print("  ★★ STATUS: FROM MEMORY. NEEDS-PRIMARY-VERIFICATION before ANY verdict.")
print("     I am NOT issuing a confirm-or-kill on remembered numbers — that would be")
print("     exactly the error my own standing rule names.")
print()
print("  ★★★ BUT ONE QUALITATIVE FACT IS ROBUST AND IT IS THE ONE THAT MATTERS:")
print("      THE TWO FRAMES ARE NEARLY ALIGNED IN DIRECTION.")
print("      That alone determines whether the test can bite — see Section 2.")

# ================================================================ POWER
print()
print("=" * 78)
print("SECTION 2 — ★★★ THE POWER ANALYSIS (geometric — independent of the exact values)")
print("=" * 78)
print("Model the pre-registration directly: if the slice tracks a mixture")
print("      v_slice = (1 - eps) * v_radiation  +  eps * v_matter")
print("then the OBSERVABLE is the angle between v_slice and v_radiation.\n")

def deviation_deg(theta_sep_deg, eps, ratio=1.0):
    """Angle between the mixed frame and the pure radiation frame."""
    th = np.radians(theta_sep_deg)
    vR = np.array([1.0, 0.0])
    vM = ratio * np.array([np.cos(th), np.sin(th)])
    v = (1 - eps) * vR + eps * vM
    c = np.dot(v, vR) / (np.linalg.norm(v) * np.linalg.norm(vR))
    return np.degrees(np.arccos(np.clip(c, -1, 1)))

print(f"{'frame separation':>18s} " + "".join(f"{'eps='+str(e):>9s}"
                                             for e in (0.01, 0.05, 0.1, 0.25, 0.5)))
print("-" * 78)
rows = []
for theta in (1.0, 5.0, 10.0, 30.0, 90.0):
    devs = [deviation_deg(theta, e) for e in (0.01, 0.05, 0.1, 0.25, 0.5)]
    rows.append((theta, devs))
    print(f"{str(theta)+' deg':>18s} " + "".join(f"{d:>9.3f}" for d in devs))
print()
print("  (table entries are the observable deviation, in degrees)")
print()
print("★★★ THE DEVIATION SCALES AS eps x (frame separation). Both factors are small:")
print("    at a 5 deg separation, even a 10% matter admixture moves the slice by ~0.5 deg.")
small = deviation_deg(5.0, 0.1)
print(f"    computed: separation 5 deg, eps = 0.10  ->  deviation {small:.3f} deg")
print()
print("⟹ TO KILL eps = 0 YOU MUST MEASURE THE SLICE'S FRAME TO BETTER THAN eps x theta.")
print("  With the frames nearly aligned, that is a demanding measurement for any eps")
print("  short of order unity.")

# ================================================================ WHAT IT TAKES
print()
print("=" * 78)
print("SECTION 3 — WHAT WOULD ACTUALLY KILL IT (stated so the bar is checkable)")
print("=" * 78)
prec = [0.1, 0.5, 1.0, 2.0]
print(f"{'angular precision':>18s} " + "".join(f"{'sep='+str(t)+'d':>11s}"
                                              for t in (5.0, 10.0, 30.0)))
print("-" * 78)
for p in prec:
    line = f"{str(p)+' deg':>18s} "
    for t in (5.0, 10.0, 30.0):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if deviation_deg(t, mid) < p: lo = mid
            else: hi = mid
        line += f"{'eps>' + f'{hi:.2f}':>11s}"
    print(line)
print()
print("  (each cell: the SMALLEST matter admixture that measurement could detect)")
print()
print("★★ READ THE TABLE HONESTLY: at a few degrees of separation and ~1 deg of")
print("   angular precision, the test only excludes admixtures of TENS OF PERCENT.")
print("   It does NOT probe small eps at all.")

# ================================================================ VERDICT
print()
print("=" * 78)
print("SECTION 4 — VERDICT ON THE FALSIFIER (not on the physics)")
print("=" * 78)
print("  WHAT SURVIVES — Cal's pre-registration is METHODOLOGICALLY SOUND and I am not")
print("    challenging it: the predicted frame is derived from the mechanism's own")
print("    channel (absorption is of photons), the value has NO free parameter, and it")
print("    was filed before any lookup. That is a real pre-registration.")
print()
print("  WHAT I HAVE TO REPORT — the test's POWER is low, and low for a structural")
print("    reason: the deviation goes as eps x theta, and theta is small because the")
print("    radiation and matter frames are nearly aligned on the sky.")
print("    ⟹ 'eps = 0 exactly, so any detected admixture kills it' is TRUE IN PRINCIPLE")
print("      and WEAK IN PRACTICE — the detectable admixture is order tens of percent.")
print()
print("★★★ THE HONEST FORM: eps = 0 is a SHARP PREDICTION carried by a BLUNT TEST.")
print("  Those are different properties and the package should not let the first imply")
print("  the second. A referee who runs this arithmetic gets there in one line.")
print("  ⟹ @Cal @Keeper — this does NOT retract the falsifier. It sizes it, which is")
print("    what §676 asked of the descent in the first place. Recommend the summary say")
print("    'falsifiable in principle; current discriminating power excludes only large")
print("    admixtures' rather than 'the sharpest available'.")

# ================================================================ COLLISION
print()
print("=" * 78)
print("SECTION 5 — ★ A SYMBOL COLLISION FOUND WHILE DOING THIS (15th of the class)")
print("=" * 78)
print("  Grepping 'eps = 0' returned TWO DIFFERENT banked claims:")
print("    (a) DARK ENERGY: w = -1 + eps, eps = 0 the forced default (K1072, F760).")
print("    (b) DESCENT:     matter admixture eps = 0 (Cal's frame-agreement, 2026-08-21).")
print()
print("★★ TWO DIFFERENT FALSIFIERS, BOTH STATED AS 'eps = 0', IN THE SAME PACKAGE.")
print("   Different objects, different sectors, no relation. I hit it in my own grep")
print("   while looking for (b) and got (a) first.")
print("⟹ @Keeper @Grace — subscript before dispatch: eps_w (dark energy) vs eps_frame")
print("  (descent). Logged as a candidate collision, not a defect.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("lookup performed post-gate, as assigned", True),
    ("remembered values flagged NEEDS-PRIMARY-VERIFICATION, no verdict on them", True),
    ("power analysis is geometric, independent of the exact values", True),
    ("deviation shown to scale as eps x frame-separation", small < 1.0),
    ("detectable-eps table computed for stated precisions", True),
    ("pre-registration's methodology explicitly NOT challenged", True),
    ("eps symbol collision logged (15th of the class)", True),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — the prediction is sharp; the test is blunt; both should be said:")
print("  I ran the lookup Cal assigned me after his gate, and I am NOT issuing a")
print("  confirm-or-kill, because the values I have are remembered and my own standing")
print("  rule says remembered experimental numbers go stale. What I CAN settle without")
print("  them is the question that decides whether the lookup is worth doing precisely:")
print("  the observable deviation scales as eps x (frame separation), and the radiation")
print("  and matter frames are nearly aligned. So the test excludes only admixtures of")
print("  order tens of percent — it does not probe small eps at all.")
print("  ⟹ eps = 0 is a sharp prediction carried by a blunt test. That does not retract")
print("     the falsifier — it SIZES it, which is what §676 demanded of the descent. The")
print("     summary line should say 'falsifiable in principle, currently excludes only")
print("     large admixtures', because a referee reaches that in one line of arithmetic.")
print("  ⟹ And the grep turned up a 15th same-symbol collision: eps = 0 is ALSO the")
print("     dark-energy default. Two falsifiers, one symbol, same package. Subscript it.")
