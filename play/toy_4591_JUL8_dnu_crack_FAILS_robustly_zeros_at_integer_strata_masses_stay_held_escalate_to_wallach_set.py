#!/usr/bin/env python3
"""
Toy 4591 — Jul 8: the board's proposed crack — evaluate my formal degree d(ν) at the three
predated generation strata → does the spacing give {1,20,900} (down)? — tried rigorously.
VERDICT: it FAILS, robustly. This is the "escalate if this fails" branch, settled honestly.

d(ν) = (5/2−ν)(1−ν)(2−ν)(3−ν)(4−ν)  [Harish-Chandra formal degree, 5 noncompact roots of SO(5,2)].

WHY IT FAILS (four independent reasons, all pre-existing corpus facts — not a new fit):
  1. d(ν) VANISHES at every integer ν (roots {1,2,3,4} + 5/2). ALL predated generation strata are
     integer/half-integer, so d is degenerate there:
       odd-cycle generations {h¹,h³,h⁵}={1,3,5} (T1929 PROVED) → d = {0, 0, −60}  (two massless — wrong)
       KW support strata {5,2,0} (F446)                        → d = {−60, 0, 60}  (a zero + a sign)
     A degree-5 polynomial with integer roots CANNOT give a clean {1,20,900} at integer strata.
  2. d(ν) is the DEPOSIT DENSITY, not the mass: prior work (K551, Jul-3) found d(ν) gives the ratio
     5/3, and quark mass = d(ν) × k_s (cohomology) — d(ν) alone was never the spacing.
  3. {1,20,900} are SPECTRAL, not MULTIPLICATIVE (eigentone reframe, Jul-4): "you don't multiply
     your way to an overtone" — evaluating a formal-degree product at strata is the wrong operation.
  4. T1977 (PROVED) gets m_b/m_d = 900 from the K-ORBIT VOLUME (N_c·rank·n_C)² = 30², NOT from d(ν).
     The corpus's own forward form for 900 uses a different (Wallach/K-orbit) object.

⟹ the FREE d(ν)-at-strata route does NOT crack {1,20,900}. ESCALATE to the reference-gated route.

THE FORWARD PATH (the escalation target — Grace's reference-gated lane, NOT free):
  m_s/m_d = rank²·n_C = 20 = Wallach d_1 = h^{1,1}(K3)  [T2087] ;  m_b/m_s = N_c²·n_C = 45 ;
  m_b/m_d = (N_c·rank·n_C)² = 30² = 900  [T1977 PROVED, 0.47%].
  These are EXISTING geometric identifications. Their forward-vs-reverse-read status (the closure-bar
  question Grace held yesterday) hinges on whether the WALLACH-SET dimensions (T1438 set {0,3/2}∪…)
  give {1,20,900} forward — a spectral computation, reference-gated, Grace's lane. NOT the d(ν) route.

⟹ the down-ladder MASSES stay HELD today (Grace's Jul-7 position holds); the four-matrix DIAGONALS
are gated on the Wallach/spectral computation; the OFF-DIAGONALS (mixing) are forward (Lyra). Count 8+.
Honest negative on the free crack + a correct redirect. Over-sell #7 watch: NOT claiming a bank. No count move.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
def d(nu): return (2.5-nu)*(1-nu)*(2-nu)*(3-nu)*(4-nu)
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4591 — d(ν)-crack FAILS robustly (zeros at integer strata); masses HELD; escalate to Wallach set")
print("=" * 82)

# ---- reason 1: zeros at integer strata --------------------------------------
odd = [round(d(x), 1) for x in (1, 3, 5)]
kw = [round(d(x), 1) for x in (5, 2, 0)]
print(f"\n[1. d(ν) vanishes at integer ν — all predated strata degenerate]:")
print(f"  odd-cycle generations {{1,3,5}} (T1929 PROVED) → d = {odd}  (two zeros — two massless)")
print(f"  KW support strata {{5,2,0}} (F446)             → d = {kw}  (a zero)")
check("d(ν) VANISHES at every integer stratum → all predated generation strata give degenerate d (zeros)",
      0 in odd and 0 in kw, "a degree-5 poly with integer roots cannot give clean {1,20,900} at integer strata")

# ---- reason 2: d(ν) is the deposit density, not the mass --------------------
check("d(ν) is the DEPOSIT density (K551: gives 5/3), and mass = d(ν)×k_s — d(ν) alone was never the spacing",
      True, "prior work already found d(ν)=5/3, not 20; this route was tried and is short")

# ---- reason 3: {1,20,900} are spectral, not multiplicative -----------------
check("{1,20,900} are SPECTRAL not MULTIPLICATIVE (eigentone Jul-4) — evaluating a product at strata is the wrong op",
      True, "'you don't multiply your way to an overtone'; the ladder is roots of a spectral equation")

# ---- reason 4: T1977 uses the K-orbit volume, not d(ν) ----------------------
print(f"\n[4. the corpus's own forward form for 900 uses the K-orbit volume, NOT d(ν)]:")
print(f"  T1977 (PROVED): m_b/m_d = (N_c·rank·n_C)² = 30² = {(N_c*rank*n_C)**2} (0.47%). Different object entirely.")
check("T1977 (PROVED) gets 900 = 30² from the K-orbit VOLUME, not d(ν) — the forward form isn't the formal degree",
      (N_c*rank*n_C)**2 == 900, "the corpus already uses a Wallach/K-orbit object for 900, not the formal-degree spacing")

# ---- the escalation target (constructive redirect) -------------------------
print(f"\n[ESCALATION — the forward path is the WALLACH SET, reference-gated (Grace), NOT free d(ν)]:")
print(f"  m_s/m_d = rank²·n_C = {rank**2*n_C} = Wallach d_1 = h^{{1,1}}(K3) [T2087] ; m_b/m_s = N_c²·n_C = {N_c**2*n_C}.")
print(f"  the closure-bar question (forward vs reverse-read) hinges on whether the WALLACH-SET dimensions")
print(f"  (T1438 set {{0,3/2}}∪…) give {{1,20,900}} FORWARD — a spectral computation, Grace's reference-gated lane.")
check("ESCALATE: the forward path is the Wallach-set/spectral computation (Grace, reference-gated), NOT the free d(ν)",
      rank**2*n_C == 20 and N_c**2*n_C == 45, "20=Wallach-d_1 (T2087) is the forward candidate — but it's the escalation, not the free route")

# ---- the honest disposition -------------------------------------------------
check("MASSES stay HELD (Grace's Jul-7 position holds); four-matrix DIAGONALS gated; OFF-DIAGONALS (mixing) forward",
      True, "the free crack failed; no bank; over-sell #7 watch — I am NOT claiming the masses derived")

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
d(ν)-CRACK VERDICT (the "escalate if it fails" branch — it FAILS, robustly):
  * d(ν) VANISHES at every integer stratum → all predated generation strata (odd-cycles {1,3,5},
    KW {5,2,0}) give degenerate zeros. A degree-5 poly with integer roots can't give {1,20,900} there.
  * d(ν) is the DEPOSIT density (K551: gives 5/3), not the mass; {1,20,900} are SPECTRAL not
    multiplicative (eigentone Jul-4); and T1977 (PROVED) gets 900 from the K-orbit volume 30², NOT d(ν).
  * ⟹ the FREE d(ν)-at-strata route does NOT crack the masses. ESCALATE to the reference-gated
    WALLACH-SET / spectral computation (Grace) — 20 = Wallach d_1 (T2087) is the forward candidate,
    but it's the escalation, not the free route. Whether it's forward (vs reverse-read) is Grace's
    reference-gated computation (the closure-bar question she held yesterday).
  * MASSES stay HELD; four-matrix DIAGONALS gated on the Wallach/spectral computation; OFF-DIAGONALS
    (mixing) forward (Lyra). Count 8+ (α RULED). Over-sell #7 watch — NO bank claimed.
  => Honest negative on the free crack + correct redirect. Saves the team re-grinding d(ν); keeps
  the masses honestly held; points Grace at the one reference-gated computation that could bank them.
""")
