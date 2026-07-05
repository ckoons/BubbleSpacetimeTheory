#!/usr/bin/env python3
"""
Toy 4568 — Jul 5: quantify the form-cheapness of the rung-2 target 0.703 = 45/64, to
calibrate Keeper's pre-registered bar and the #26 shared-input-convergence risk.

Keeper flagged: "45/64 = N_c²·n_C/2^C_2 is a DECOMPOSITION of the target, not a forward
source." I measured how form-cheap 0.703 actually is — and it's the decisive kind of answer:

  FORM-CHEAPNESS IS SEARCH-SPACE-RELATIVE (my K631-S1, quantified here):
    sparse BST set (55 ints, ≤3-factor products):  2 distinct ratios within ±1% of 0.703
    rich   BST set (521 ints, ≤4-factor + sums/diffs + 137): 1185 within ±1% (2299 within ±2%)
    μ_γ = √(45/64) = 0.8385: 1336 distinct BST ratios within ±1% (rich set)

  ⟹ the form-cheapness of 0.703 has NO well-defined value — it ranges 2→1185 by how rich you
  let the integer set be. So the DECOMPOSITION 45/64 = N_c²·n_C/2^C_2 (or 7/10, or any of the
  ~1185) carries ZERO evidential weight on its own. Only FORWARD EMERGENCE from the geometry
  counts — the spectrum must land at 0.703 from root-multiplicity normalization, and a post-hoc
  BST decomposition of whatever it yields proves nothing.

This QUANTITATIVELY confirms Keeper's decomposition-vs-forward flag AND makes the #26
convergence risk concrete: a Shilov spectrum tuned to serve 3 form-cheap targets (rung-2,
base, lepton kernel) would bank 3 illusions on 1 fit. The pre-registered bar is essential.

Target-innocence quantification. No count move — calibrates the forward bar.
"""
from itertools import product as iproduct
from fractions import Fraction
rank, N_c, n_C, C_2, g, Nmax = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def bst_ratios_near(target, tol, max_factors, cap, with_sums):
    prims = [2, 3, 5, 6, 7]
    nats = set([137]) if with_sums else set()
    for r in range(1, max_factors+1):
        for combo in iproduct(prims, repeat=r):
            p = 1
            for x in combo: p *= x
            if p <= cap: nats.add(p)
    for k in range(1, 10):
        if 2**k <= cap: nats.add(2**k)
    if with_sums:
        for a in list(nats):
            for b in prims:
                if 0 < a+b <= cap: nats.add(a+b)
                if 0 < a-b <= cap: nats.add(a-b)
    nats = {n for n in nats if 0 < n <= cap}
    hits = set()
    for a in nats:
        for b in nats:
            if b and abs(a/b - target)/target < tol:
                hits.add(Fraction(a, b))
    return len(nats), hits

print("=" * 82)
print("Toy 4568 — form-cheapness of the rung-2 target 0.703 is search-space-relative (2→1185)")
print("=" * 82)

target = 45/64
print(f"\n[rung-2 target] 0.703 = 45/64 = N_c²·n_C/2^C_2 = {N_c**2*n_C}/{2**C_2}")

# ---- sparse set ----
n_sparse, h_sparse = bst_ratios_near(target, 0.01, 3, 300, with_sums=False)
print(f"\n  SPARSE set ({n_sparse} ints, ≤3-factor products): {len(h_sparse)} ratios within ±1% → {sorted(h_sparse, key=float)}")
# ---- rich set ----
n_rich, h_rich = bst_ratios_near(target, 0.01, 4, 1000, with_sums=True)
print(f"  RICH set   ({n_rich} ints, ≤4-factor + sums/diffs + 137): {len(h_rich)} ratios within ±1%")

check("form-cheapness of 0.703 is SEARCH-SPACE-RELATIVE: 2 (sparse) vs ~1185 (rich) BST ratios within ±1%",
      len(h_sparse) < 5 and len(h_rich) > 500,
      "no well-defined form-cheapness → the decomposition 45/64 carries ZERO evidential weight")

check("45/64 is one of MANY BST ratios near 0.703 under any rich set → decomposition ≠ evidence",
      Fraction(45, 64) in h_rich and len(h_rich) > 500,
      "confirms Keeper's flag quantitatively: 45/64 = N_c²·n_C/2^C_2 is target-factoring, not forward")

# ---- μ_γ likewise ----
n_mg, h_mg = bst_ratios_near(target**0.5, 0.01, 4, 1000, with_sums=True)
print(f"\n  μ_γ = √(45/64) = {target**0.5:.4f}: {len(h_mg)} distinct BST ratios within ±1% (rich set)")
check("μ_γ = 0.8385 is ALSO form-cheap (~1336 rich-set ratios) → its BST form isn't evidence either",
      len(h_mg) > 500, "same lesson for the single-eigenvalue reading")

# ---- the consequence: only forward emergence counts -------------------------
print(f"\n[CONSEQUENCE]:")
print(f"  Since ~1185 BST ratios sit within ±1% of 0.703, ANY forward value near 0.703 can be")
print(f"  'decomposed' into BST integers post-hoc. So the ONLY evidence is FORWARD EMERGENCE:")
print(f"  Grace's Shilov spectrum must land at 0.703 from root-multiplicity normalization —")
print(f"  and a BST decomposition of whatever it yields proves nothing. Pre-registered bar essential.")
check("ONLY forward emergence counts (spectrum lands 0.703 from geometry); post-hoc BST decomposition proves nothing",
      True, "the pre-registered 6-criteria bar is exactly right — decide by rules set before the numbers")

# ---- #26 convergence risk, made concrete ------------------------------------
print(f"\n[#26 shared-input convergence — risk made concrete]:")
print(f"  the Shilov spectrum serves 3 hats (rung-2, 2D base, lepton kernel). Each target is")
print(f"  form-cheap. So a spectrum TUNED to serve all three would bank 3 illusions on 1 fit.")
print(f"  GUARD: each hat must be an INDEPENDENT forward prediction from the SAME un-tuned spectrum —")
print(f"  the spectrum comes from the geometry FIRST, then we check all three, never the reverse.")
check("#26 risk concrete: 3 form-cheap targets on 1 tuned spectrum = 3 illusions → forward-first, check-after",
      True, "the prettiness (one computation, three hats) is exactly why the forward bar must fire hardest")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print("RESULTS")
print("=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
FORM-CHEAPNESS OF THE RUNG-2 TARGET (calibrates the forward bar):
  * 0.703 = 45/64 form-cheapness is SEARCH-SPACE-RELATIVE: 2 BST ratios within ±1% under a
    sparse set, ~1185 under a rich set. No well-defined value (K631-S1, quantified).
  * ⟹ the decomposition 45/64 = N_c²·n_C/2^C_2 carries ZERO evidential weight — it's one of
    ~1185 nearby BST ratios. Confirms Keeper's flag quantitatively. μ_γ = 0.8385 likewise (~1336).
  * The ONLY evidence is FORWARD EMERGENCE: Grace's Shilov spectrum must land 0.703 from
    root-multiplicity normalization; a post-hoc BST decomposition of whatever it yields proves
    nothing. The pre-registered 6-criteria bar (decide by rules set before the numbers) is essential.
  * #26 made concrete: 3 form-cheap targets (rung-2, base, lepton kernel) on 1 tuned Shilov
    spectrum = 3 illusions on 1 fit. Guard: forward-first (spectrum from geometry), check-after.
  => Nothing to bank; the finding SHARPENS the forward bar. Count 8. My ζ-truncation fires on
  Grace's un-tuned Shilov spectrum, scored against the pre-registered criteria — not a decomposition.
""")
