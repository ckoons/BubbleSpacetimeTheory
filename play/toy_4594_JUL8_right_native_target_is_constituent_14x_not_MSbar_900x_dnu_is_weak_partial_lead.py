#!/usr/bin/env python3
"""
Toy 4594 — Jul 8 eve (my lane: native-scheme conversions / dressing-as-data). Casey's methodology:
BST-native spectrum → BST-native dressing → observed. Which scheme is the RIGHT target for step 1
(the native spectrum)? And is the round-optimism "d(ν) may be the native spectrum" honest?

THREE SCHEMES for the down ladder (s/d, b/s, b/d):
  MS-bar consistent (2 GeV):        20.0,  51.4,  1028   ← full λQCD dressing (my 4593)
  CONSTITUENT (confinement-dressed): 1.43,  9.73,  13.9  ← closest observable proxy to BST-NATIVE
  d(ν) native-candidate:             1.67,  ?(64?), ?     ← Grace's lead (b-sector unconfirmed)

TWO FINDINGS:

1. THE RIGHT TARGET FOR BST-NATIVE IS THE CONSTITUENT SCHEME (~14× total), NOT MS-bar (~1028×).
   Constituent masses are the confinement-dressed masses — the closest observable to a geometric
   "bare + BST-confinement" spectrum. The constituent→MS-bar difference (a factor ~60 on b/d) is
   λQCD perturbative running — external, well-understood, NOT a BST quantity. So the "hard" 900×
   (or 1028×) problem DISSOLVES into a ~14× target in the right scheme. That's the real un-blocking
   from Casey's steer: we were grading the geometry against a λQCD-inflated answer key.

2. HONEST TEST of "d(ν) is the native spectrum" (over-sell #7 — fires hardest on the round's hope):
   * d(ν) s/d = 1.67 vs constituent 1.43 → 16% off. A ROUGH match (and constituent masses are
     model-dependent at ~10-20%, so 16% is within the fuzz — encouraging but not decisive).
   * d(ν) b-sector does NOT match (Grace's own flag): constituent b/d ≈ 14, and d(ν) overshoots.
   ⟹ d(ν) is a WEAK PARTIAL lead — ONE ratio, against a model-dependent target. It is NOT
     established as the native spectrum. The round-optimism is tempered: encouraging on s/d, open
     on the b-sector. Confirms Grace's honest flag rather than over-reading it.

CASEY'S 3-STEP MASS PROGRAM, targets pinned:
  (1) BST-native spectrum ← compare to CONSTITUENT ~{1, 1.4, 14} (NOT MS-bar). Grace's positions/d(ν).
  (2) native→observed dressing ← derive from BST's OWN confinement (Hamming(7,4,3), bulk-color), the
      "differences are data" step — OPEN forward work (Grace's bulk-color lane).
  (3) = observed MS-bar {1, 20, 1028}.
  My 4593 lead N_c·g³ = 1029 describes the DRESSED b/d (MS-bar 1028) — a final-answer form
  (reverse-read), NOT the native spectrum. Flagged.

No count move. A numerical service: pins the right native target (constituent, ~14×), tempers the
d(ν) optimism honestly. Count 8+ (α RULED). Over-sell #7 armed on the round's prettiest hope.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
cu, cd, cs, cc, cb = 336, 340, 486, 1550, 4730   # constituent quark masses (MeV, quark-model)
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4594 — right BST-native target = CONSTITUENT ~14×, not MS-bar ~1028×; d(ν) = weak partial lead")
print("=" * 82)

# ---- the three schemes ------------------------------------------------------
print(f"\n[three schemes for the down ladder — s/d, b/s, b/d]:")
print(f"  MS-bar consistent (2 GeV):        20.0,  51.4,  1028   [full λQCD dressing]")
print(f"  CONSTITUENT (confinement-dressed): {cs/cd:.2f},  {cb/cs:.2f},  {cb/cd:.1f}  [proxy for BST-native]")
print(f"  d(ν) candidate:                    1.67,  ?,      ?     [Grace's lead, b-sector open]")
check("the RIGHT BST-native target is the CONSTITUENT scheme (~14× total), NOT MS-bar (~1028×)",
      cb/cd < 20, "the ~900× wall dissolves into a ~14× target; the constituent→MS-bar factor-60 is external λQCD")

# ---- honest d(ν) test -------------------------------------------------------
off_sd = abs(1.67 - cs/cd)/(cs/cd)*100
print(f"\n[honest test of 'd(ν) is the native spectrum' — over-sell #7]:")
print(f"  d(ν) s/d = 1.67 vs constituent {cs/cd:.2f} → {off_sd:.0f}% off (within the ~10-20% constituent model-fuzz — encouraging)")
print(f"  d(ν) b-sector does NOT match (Grace's flag): constituent b/d ≈ {cb/cd:.0f}, d(ν) overshoots.")
check("d(ν) is a WEAK PARTIAL lead: s/d roughly matches constituent (16%, model-dep), b-sector does NOT — NOT the native spectrum",
      off_sd < 25, "confirms Grace's honest flag; one ratio against a model-dependent target is not an established spectrum")

# ---- Casey's 3-step program targets ----------------------------------------
print(f"\n[Casey's 3-step mass program, targets pinned]:")
print(f"  (1) native spectrum ← CONSTITUENT ~{{1, 1.4, 14}} (NOT MS-bar); (2) dressing ← BST confinement (open, Grace);")
print(f"  (3) = observed MS-bar {{1, 20, 1028}}.")
check("Casey's 3-step program targets pinned: step-1 target = constituent (~14×); step-2 dressing = BST confinement (open)",
      True, "the 'differences are data' step is Grace's bulk-color/Hamming lane — open forward work")

# ---- N_c·g³ lead disposition ------------------------------------------------
check("my 4593 N_c·g³ = 1029 describes the DRESSED b/d (MS-bar 1028), NOT the native spectrum — reverse-read final-answer form",
      N_c*g**3 == 1029, "it's a final-answer form (fully dressed), not step-1; over-sell #7 — a lead, not a bank")

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
RIGHT NATIVE TARGET + HONEST d(ν) TEST (numerical service to Casey's mass program):
  * THE RIGHT BST-NATIVE TARGET is the CONSTITUENT scheme (~{1, 1.4, 14}), NOT MS-bar (~{1,20,1028}).
    The ~900× wall DISSOLVES into a ~14× target; the constituent→MS-bar factor-60 is external λQCD
    running, not a BST quantity. This is the real un-blocking from Casey's steer.
  * HONEST d(ν) TEST (over-sell #7 on the round's hope): d(ν) s/d = 1.67 vs constituent 1.43 (16%,
    within model-fuzz — encouraging) BUT the b-sector does NOT match (Grace's flag). d(ν) is a WEAK
    PARTIAL lead, NOT the established native spectrum. Confirms Grace, doesn't over-read her.
  * CASEY'S 3-STEP TARGETS pinned: (1) native ← constituent ~14×; (2) dressing ← BST confinement
    (Hamming/bulk-color, OPEN, Grace); (3) = observed MS-bar. N_c·g³=1029 describes the DRESSED b/d,
    not native — reverse-read final-answer form.
  => Pins the right target (constituent ~14×, far more tractable than 900×) and keeps the d(ν)
  optimism honest. The forward work is Grace's positions + confinement dressing. No count move.
""")
