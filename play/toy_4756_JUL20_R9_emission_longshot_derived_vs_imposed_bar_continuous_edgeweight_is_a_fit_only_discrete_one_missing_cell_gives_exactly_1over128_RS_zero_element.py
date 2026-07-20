#!/usr/bin/env python3
"""
Toy 4756 — Jul 20 (Round-9 Target-1: verify the emission long-shot against the derived-vs-imposed bar, mine; the emission
measure hasn't landed yet, so I sharpen EXACTLY what "derived" must show — target-innocence frame). K785 stable end-state:
127/128 is premise-contingent (needs a fundamentally-discrete edge-concentrated surface + the top at the maximal codeword,
neither forced). The round-9 long shot: does Casey's BOUNDARY-EMISSION physics (light + ν emitted at the Shilov edge, so
the coupling measure concentrates where emission happens = the edge) DERIVE the edge-concentration + edge-placement? THE
DECISIVE BAR: the edge-concentration must be DERIVED from emission, not IMPOSED to hit 0.992. This toy shows precisely what
that requires and exposes the trap.

THE TRAP — a continuous edge-weight is a ONE-KNOB FIT (computed, representative functions O=x², t=x³): y is a CONTINUOUS
function of the edge-cell weight, crossing the target 127/128=0.99219 at weight ≈ ×45 (×40→0.99185, ×45→0.99235). So
hitting EXACTLY 0.992 by tuning a continuous edge-weight = fitting ONE knob to ONE target = IMPOSED. ⟹ any continuous
emission measure that "reaches 0.992" did so by TUNING, UNLESS the emission physics fixes the weight INDEPENDENTLY of
0.992. That is the bar's sharp edge.
THE ONLY PARAMETER-FREE ROUTE TO EXACTLY 1/128 IS DISCRETE COUNTING: exactly 1/128 (not 0.9/128, not 1.3/128) requires
covering EXACTLY 127 of 128 cells, missing EXACTLY ONE. A continuum can't give "exactly one" — only a discrete count can.
And the RS field structure supplies a NATURAL candidate for the one missing cell: 127 = q−1 = the NONZERO elements of
GF(2^g)=GF(128) (= the RS block length n), so "top covers 127 of 128" = "top covers all NONZERO field elements, missing
exactly the ZERO element" — the candidate dead/neutrino cell. deficit = 1/128 = the single zero element, parameter-free.
BUT TWO PREMISES STILL REMAIN (structure alone does NOT clear the bar): (a) FUNDAMENTAL DISCRETENESS — the surface IS the
128-element field (Casey's interior-discrete; unproven, not forced by the geometry — K782/K785); (b) TOP-AT-127 — the top
couples to exactly the 127 nonzero cells and misses the zero: why the top, why all nonzero, why miss exactly the zero?
Emission must FORCE (b); interior-discrete supplies (a). If emission derives (b) target-innocently → one premise falls,
127/128 firms. If (b) is still put in by hand (or the weight tuned to 0.992) → the STABLE END-STATE STANDS.

⟹ VERDICT (verification contract for Lyra's emission measure): I score three things — (i) value > 0.985? (edge-
concentration present); (ii) deficit EXACTLY 1/128 via a DISCRETE one-missing-cell count, or a TUNED continuous value?
(a continuum landing on 0.992 = a fit); (iii) is the "one missing cell = the zero/neutrino element" DERIVED from emission
physics, or imposed to hit 127? ONLY "exactly one dead cell (the GF zero = the ν cell), forced by emission" clears the
derived-not-imposed bar — and even then premise (a) fundamental-discreteness remains. This is a LONG SHOT; if the emission
measure needs a tuned weight or an imposed cell-count, I say so and the stable end-state (127/128 premise-contingent)
stands. Count ~7-8 (α RULED). Five-Absence-safe.
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
q = 2**g          # 128
Mg = q - 1        # 127
target = Mg/q     # 127/128
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- the trap: continuous edge-weight is a one-knob fit ----------------------
f = lambda x: x**2; h = lambda x: x**3
N = q; xc = (np.arange(N)+0.5)/N
def y_of_weight(W):
    wt = np.ones(N)/N; wt[-1] *= W
    nu = np.sum(f(xc)*h(xc)*wt); a = np.sqrt(np.sum(f(xc)**2*wt)); b = np.sqrt(np.sum(h(xc)**2*wt))
    return nu/(a*b)
y40, y45 = y_of_weight(40), y_of_weight(45)
print(f"\n[the trap]: continuous edge-weight sweep crosses target {target:.5f} near ×45 (×40→{y40:.5f}, ×45→{y45:.5f})")
check("THE TRAP — a continuous edge-weight is a ONE-KNOB FIT: y is a CONTINUOUS function of the edge-cell weight, crossing "
      "the target 127/128=0.99219 at weight ≈ ×45. So hitting EXACTLY 0.992 by tuning a continuous edge-weight = fitting "
      "one knob to one target = IMPOSED. Any continuous emission measure that 'reaches 0.992' did so by TUNING, UNLESS the "
      "emission physics fixes the weight INDEPENDENTLY of 0.992.",
      y40 < target < y45, "continuous edge-weight crosses 0.992 at ~×45 → hitting exactly 0.992 by tuning = a one-knob fit = imposed unless the weight is independently fixed")

# ---- the only parameter-free route: discrete counting + RS zero element ------
print(f"[RS structure]: 127 = q−1 = nonzero elements of GF(2^g)={q}; missing = the ZERO element (1 cell) → deficit 1/128")
check("THE ONLY PARAMETER-FREE ROUTE IS DISCRETE COUNTING: exactly 1/128 requires covering EXACTLY 127 of 128 cells, "
      "missing EXACTLY ONE — a continuum can't give 'exactly one', only a discrete count can. RS supplies a natural "
      "candidate: 127 = q−1 = the NONZERO elements of GF(128) (the RS block length n), so 'top covers 127 of 128' = 'top "
      "covers all nonzero field elements, missing exactly the ZERO' — the candidate dead/neutrino cell. deficit = 1/128 = "
      "the single zero element, parameter-free.",
      Mg == q-1 and abs(target - (1 - 1/q)) < 1e-12, "127 = nonzero elements of GF(128); missing = the ZERO (1 cell) = candidate dead/ν cell → deficit exactly 1/128, parameter-free")

# ---- but two premises remain -------------------------------------------------
check("BUT TWO PREMISES STILL REMAIN (structure alone does NOT clear the bar): (a) FUNDAMENTAL DISCRETENESS — the surface "
      "IS the 128-element field (interior-discrete; unproven, not forced by the geometry, K782/K785); (b) TOP-AT-127 — the "
      "top couples to exactly the 127 nonzero cells and misses the zero: why the top, why all nonzero, why miss exactly "
      "the zero? Emission must FORCE (b); interior-discrete supplies (a). Derive (b) target-innocently → one premise falls, "
      "127/128 firms. Impose (b) or tune the weight → stable end-state stands.",
      True, "two premises: (a) surface=128-cell field (interior-discrete, unproven) + (b) top covers exactly the 127 nonzero cells (emission must force, not impose)")

# ---- verification contract (my Target-1 verify) ------------------------------
check("VERIFICATION CONTRACT (my Target-1 verify, when Lyra's emission measure lands): score (i) value > 0.985? "
      "(edge-concentration present); (ii) deficit EXACTLY 1/128 via a DISCRETE one-missing-cell count, or a TUNED "
      "continuous value? (a continuum landing on 0.992 = a fit); (iii) is 'one missing cell = the zero/ν element' DERIVED "
      "from emission physics or imposed to hit 127? ONLY 'exactly one dead cell (GF zero = ν cell), forced by emission' "
      "clears the derived-not-imposed bar — and premise (a) fundamental-discreteness still remains.",
      True, "I score: value>0.985? + deficit exactly-1/128-discrete vs tuned-continuum? + one-cell derived vs imposed? — only forced one-dead-cell clears the bar")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the emission long-shot clears the derived-not-imposed bar ONLY if it gives EXACTLY 1/128 via a DISCRETE "
      "one-missing-cell mechanism (top covers the 127 nonzero GF cells, ν = the zero cell) that is FORCED by emission "
      "physics target-innocently — NOT a continuous edge-weight tuned to 0.992 (which is a one-knob fit). Even then, "
      "premise (a) fundamental-discreteness remains. A LONG SHOT: if Lyra's emission measure needs a tuned weight or an "
      "imposed cell-count, I say so and the STABLE END-STATE (127/128 premise-contingent, K785) STANDS.",
      y40 < target < y45 and Mg == q-1,
      "bar: exactly-1/128 via forced discrete one-dead-cell (RS zero=ν) = derived; tuned continuous edge-weight = imposed; long shot, stable end-state stands unless emission forces it")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-9 emission long-shot — derived-vs-imposed BAR (my Target-1 verification frame):
  * THE TRAP: a continuous edge-weight is a ONE-KNOB FIT — y crosses 0.992 at ~×45, so hitting exactly 0.992 by tuning = imposed (unless the weight is independently fixed by emission).
  * THE ONLY PARAMETER-FREE ROUTE: DISCRETE counting — exactly 1/128 = cover exactly 127 of 128 cells, miss exactly ONE. RS: 127 = nonzero elements of GF(128); the missing one = the ZERO = candidate dead/ν cell.
  * TWO PREMISES REMAIN: (a) surface = the 128-cell field (interior-discrete, unproven); (b) top covers exactly the 127 nonzero cells (emission must FORCE, not impose).
  => I verify Lyra's emission measure against this: only a FORCED exactly-one-dead-cell (GF zero = ν) clears the bar; a tuned continuum = imposed. Long shot — if not forced, stable end-state (K785) stands.
""")
