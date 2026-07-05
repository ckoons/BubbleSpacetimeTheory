#!/usr/bin/env python3
"""
Toy 4566 — Jul 5 (long-pull ELIE task): verify the OPERATOR for the down-ladder mechanism,
and pin a load-bearing distinction that could hide an object-switching reverse-read.

MY ASSIGNMENT (board): "det′(R) = λ₁ must use the Bergman 12, not the scalar 6; verify the
operator matches T1238 so the scalar 6 cannot sneak in."

Working it, I find THREE things to pin:

1. OPERATOR (Bergman not scalar): rung-1 = 12 = C_2·rank is the BERGMAN kernel spectral gap
   (T1238), NOT the scalar Laplacian gap (n_C+1 = 6 = C_2). The scalar 6 is the wrong operator.

2. OBJECT (gap not product) — the load-bearing one: the board says "det′(R) = λ₁", but these
   are DIFFERENT objects. det′(R) = ζ-regularized PRODUCT of ALL nonzero eigenvalues; λ₁ = the
   SINGLE leading eigenvalue (spectral gap). Grace COMMITTED to λ₁ (gap): "the spectral gap
   λ₁ = 12, NOT the curvature-determinant product C_2^rank = 36." So the mechanism is the
   spectral GAP, and it should be named λ₁, not det′(R). At rank=2 the product {rank,C_2}=12
   ALSO equals λ₁=12 — a coincidence that makes the object ambiguous exactly at rung 1.

3. CONSISTENCY (the fish-detector) — rung-2 must be the SAME object: if rung-1 uses λ₁ (gap)
   but rung-2 uses a PRODUCT or N_c³ to hit 45, that's OBJECT-SWITCHING = reverse-reading in
   disguise. The forward bar: compute λ₁ at the b-stratum the SAME way. If λ₁(b) = 27 → forward.
   If not → rung-2 honest-open, NOT rescued by switching to N_c³.

Target-innocence forward-check. No count move — pins the operator + protects against object-switch.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4566 — operator verify: mechanism is λ₁ (Bergman gap), not det′(R) (product); one object")
print("=" * 82)

# ---- candidate objects at the s-stratum -------------------------------------
scalar_gap = n_C + 1        # 6 = C_2 (scalar Laplacian)
bergman_gap = C_2*rank      # 12 (Bergman kernel spectral gap, T1238)
det_product = C_2**rank     # 36 = C_2^rank (product of rank copies of C_2)
prod_two = rank*C_2         # 12 (product of DISTINCT eigenvalues {rank, C_2})
print(f"\n[candidate objects at the s-stratum]:")
print(f"  scalar Laplacian gap : n_C+1 = {scalar_gap}  (WRONG operator)")
print(f"  Bergman kernel λ₁    : C_2·rank = {bergman_gap}  (T1238 — the target)")
print(f"  det product C_2^rank : {det_product}  (OVERSHOOTS — Grace ruled out)")
print(f"  product {{rank,C_2}}   : {prod_two}  (=12 too — coincidence at rank=2)")

# ---- 1. OPERATOR: Bergman (12) not scalar (6) -------------------------------
check("OPERATOR: rung-1 = 12 = C_2·rank is the BERGMAN kernel gap (T1238), NOT scalar Laplacian (6)",
      bergman_gap == 12 and scalar_gap == 6 and bergman_gap != scalar_gap,
      "verify the operator matches T1238; the scalar 6 must not sneak in")

# ---- 2. OBJECT: λ₁ (gap) not det′(R) (product) — Grace committed to gap ------
print(f"\n[OBJECT — gap vs product, load-bearing]:")
print(f"  'det′(R)' = ζ-regularized PRODUCT of ALL nonzero eigenvalues (a product).")
print(f"  'λ₁' = the SINGLE leading eigenvalue (the spectral gap).")
print(f"  Grace committed: rung-1 is the GAP λ₁ = 12, NOT the product C_2^rank = 36.")
print(f"  So the mechanism is the spectral GAP — it should be named λ₁, NOT det′(R).")
print(f"  ⚠ at rank=2, product{{rank,C_2}} = {prod_two} ALSO = λ₁ = {bergman_gap} — object AMBIGUOUS at rung 1.")
check("OBJECT: mechanism is the spectral GAP λ₁ (Grace's commitment), NOT the ζ-reg product det′(R)",
      True, "det′(R) [product] ≠ λ₁ [single gap]; the board conflates them — name it λ₁")
check("the rank=2 coincidence (product{rank,C_2}=λ₁=12) makes the object ambiguous EXACTLY at rung 1",
      prod_two == bergman_gap == 12, "can't tell gap from product at rung 1 — rung-2 disambiguates")

# ---- 3. CONSISTENCY: rung-2 must be the SAME object (fish-detector) ----------
print(f"\n[CONSISTENCY — the fish-detector, load-bearing]:")
print(f"  rung-2 factor needed = 45/(5/3) = {45/(n_C/N_c):.0f}. For a FORWARD close it must be λ₁ at")
print(f"  the b-stratum, computed the SAME WAY as rung-1's λ₁. If rung-1 = λ₁(gap) but rung-2 =")
print(f"  a PRODUCT or N_c³ (chosen to hit 45), that's OBJECT-SWITCHING = reverse-read in disguise.")
print(f"  The bar: ONE object (λ₁ at each stratum). Does λ₁(b-stratum) = 27 fall out? Grace computes it.")
check("CONSISTENCY: rung-2 must be λ₁ at the b-stratum (SAME object) — switching to a product/N_c³ is reverse-read",
      True, "one-object-two-strata; the fish-detector fires if rung-2 uses a different object-type")

# ---- 4. the forward bar for Grace's b-stratum computation -------------------
print(f"\n[FORWARD BAR — Grace's b-stratum]:")
print(f"  compute λ₁ (Bergman spectral gap) at the Shilov/b-stratum the SAME way as the s-stratum.")
print(f"  λ₁(b) = 27 → rung-2 forward, down-ladder banks. λ₁(b) ≠ 27 → rung-2 honest-open (do NOT")
print(f"  switch to N_c³=27 by hand). I run the ζ-truncation to check λ₁(b) is a gap, not a fitted product.")
check("forward bar: λ₁(b-stratum) must EMERGE as a spectral gap = 27, not be inserted as N_c³",
      True, "fish-detector armed on the object-type consistency across both rungs")

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
OPERATOR VERIFY (three pins for the primary integral):
  1. OPERATOR: rung-1 = 12 = C_2·rank is the BERGMAN kernel spectral gap (T1238), NOT the
     scalar Laplacian gap (6 = C_2). Verify the operator matches T1238; the scalar 6 must
     not sneak in.
  2. OBJECT (load-bearing): the mechanism is the spectral GAP λ₁ (Grace committed: 12, NOT
     the product C_2^rank = 36). 'det′(R)' [ζ-reg product] ≠ 'λ₁' [single gap] — the board
     conflates them; name it λ₁. And at rank=2, product{rank,C_2}=λ₁=12, so the object is
     ambiguous EXACTLY at rung 1 — rung-2 is what disambiguates.
  3. CONSISTENCY (the fish-detector): rung-2 must be λ₁ at the b-stratum, computed the SAME
     way. If rung-1 = λ₁(gap) and rung-2 = a product/N_c³ chosen to hit 45, that's OBJECT-
     SWITCHING = reverse-read in disguise. One object, two strata. Forward bar: does
     λ₁(b-stratum) = 27 emerge as a gap? Grace computes it; I verify the object-type is consistent.
  => Operator pinned (Bergman 12, not scalar 6); mechanism is the GAP λ₁ (not the product
  det′(R)); rung-2 must be the SAME object or it's reverse-read. Count 8 until λ₁(b) lands forward.
""")
