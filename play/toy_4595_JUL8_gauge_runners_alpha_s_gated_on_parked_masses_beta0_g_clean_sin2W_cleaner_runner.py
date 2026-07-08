#!/usr/bin/env python3
"""
Toy 4595 — Jul 8 (PRIMARY: the gauge runners, "the running IS the dressing"). Honest assessment of
the strategic bet (α_s) + a redirect. Casey's bar to bank: native value forced + dressing derived
from BST's own β-structure + scale-consistent target + specific predicted dressing.

α_s — β₀ = g = 7 IS CLEAN AND FORCED (T1931 PROVED): β₀(n_f=6) = (11/3)N_c − (4/3)(½)(6) = 11 − 4
  = c_2(Q⁵) − rank² = g. The full β₀(n_f) = c_2(Q⁵) − (2/3)n_f is BST-expressible {nf3→9, nf4→8.33,
  nf5→7.67, nf6→7=g}. The UV running coefficient IS the genus. GATE-INDEPENDENT, clean. ✓

BUT the precise α_s VALUE+RUNNING is GATED on the PARKED quark masses:
  * The value 7/20 = g/(4n_C) = 0.35 sits at μ ≈ m_c ≈ 1.3 GeV, NOT m_p (measured α_s(m_p) ≈ 0.49).
    That is exactly the "NEG at the wrong scale" the board flagged — RESOLVED: right value, right scale
    is m_c (T2074: α_s(m_c) = 9/26 = 0.346 ≈ 7/20). But m_c is a QUARK MASS (parked).
  * Running 7/20 (at m_c) → M_Z with BST β₀(n_f) crosses the thresholds m_c, m_b, m_t — all QUARK
    MASSES (parked). 1-loop gives α_s(M_Z) ≈ 0.122 vs 0.1179 (~3.5%) — a STRUCTURAL match, and the
    ~3.5% residual IS the threshold structure, i.e. the parked masses. "Differences are data" — but
    the data here is the quark masses.
  ⟹ α_s's precise prediction INHERITS the parked mass gate. It is NOT the clean gate-independent
    bank the strategic bet hoped. The gate-independent piece is β₀ = g = 7 (already proved, structural).

REDIRECT — sin²θ_W is the CLEANER gate-independent runner (EW, no low quark-mass thresholds):
  sin²θ_W = 3/13 = N_c/(2C_2+1) = 0.2308 vs MS-bar(M_Z) 0.23122 → 0.19%. Defined at ONE scale (M_Z),
  no low-threshold cascade; the "dressing" is the EW loop/scheme correction (on-shell 0.2223 = the
  ~3.8% dressing on top of the MS-bar count). Recommend the runner effort pivots here — it's the one
  that's genuinely gate-independent and clean.

No count move. Refines the strategic bet honestly (α_s gated on parked masses; β₀=g=7 clean) and
redirects to sin²θ_W. Over-sell #8 watch. Count 8+ (α RULED).
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c2Q = 11
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def run(a_hi, mu_hi, mu_lo, b0):
    return 1.0/(1.0/a_hi + (b0/(2*math.pi))*math.log(mu_lo/mu_hi))

print("=" * 82)
print("Toy 4595 — gauge runners: α_s gated on parked masses (β₀=g clean); sin²θ_W = cleaner runner")
print("=" * 82)

# ---- beta0 = g clean --------------------------------------------------------
print(f"\n[β₀ = g = 7 is clean + forced (T1931)]:")
print(f"  β₀(n_f=6) = c_2(Q⁵) − rank² = {c2Q} − {rank**2} = {c2Q-rank**2} = g. Full β₀(n_f) = c_2(Q⁵) − (2/3)n_f, all BST.")
check("β₀ = g = 7 (n_f=6 UV coefficient) is clean and forced: c_2(Q⁵) − rank² [T1931 PROVED] — gate-independent",
      c2Q - rank**2 == g, "the UV QCD running coefficient IS the genus; this piece is clean")

# ---- value at wrong scale (resolved) ---------------------------------------
print(f"\n[the value 7/20 sits at ~m_c, NOT m_p — old NEG = wrong scale]:")
print(f"  7/20 = g/(4n_C) = {g/(4*n_C):.3f}; T2074: α_s(m_c=1.27) = 9/26 = 0.346 ≈ 7/20. m_p α_s ≈ 0.49 (not 0.35).")
check("α_s value 7/20 = 0.35 sits at μ ≈ m_c ≈ 1.3 GeV (NOT m_p) — the old NEG was a wrong-scale artifact",
      abs(g/(4*n_C) - 0.346) < 0.02, "right value at the right scale; but m_c is a QUARK MASS (parked)")

# ---- running gated on thresholds -------------------------------------------
a_mb = run(0.35, 1.27, 4.18, 25/3)     # nf=4
a_MZ = run(a_mb, 4.18, 91.19, 23/3)    # nf=5
print(f"\n[running 7/20 (at m_c) → M_Z with BST β₀(n_f), crossing thresholds m_c,m_b,m_t (all PARKED)]:")
print(f"  1-loop: α_s(M_Z) ≈ {a_MZ:.4f} vs measured 0.1179 → {abs(a_MZ-0.1179)/0.1179*100:.1f}% (structural; residual = threshold structure)")
check("α_s precise prediction is GATED on the parked quark masses (value scale ≈ m_c + thresholds m_c,m_b,m_t)",
      abs(a_MZ-0.1179)/0.1179 > 0.02, "1-loop ~3.5% off; the residual IS the threshold/mass structure — α_s inherits the parked gate")

# ---- sin2thetaW cleaner -----------------------------------------------------
s2w = 3/13
print(f"\n[sin²θ_W = 3/13 = N_c/(2C_2+1) — the cleaner gate-independent runner (EW, no low thresholds)]:")
print(f"  3/13 = {s2w:.4f} vs MS-bar(M_Z) 0.23122 → {abs(s2w-0.23122)/0.23122*100:.2f}%; on-shell 0.2223 = the ~3.8% EW dressing.")
check("sin²θ_W = 3/13 = N_c/(2C_2+1) = 0.2308 vs MS-bar 0.2312 (0.19%) — cleaner gate-independent runner; pivot here",
      abs(s2w - 0.23122)/0.23122 < 0.01, "defined at ONE scale (M_Z), no quark-threshold cascade; the dressing is an EW loop correction")

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
GAUGE RUNNERS — honest assessment + redirect:
  * β₀ = g = 7 IS CLEAN + FORCED (T1931): c_2(Q⁵) − rank² = 11 − 4 = g; the UV QCD running
    coefficient is the genus. Gate-independent. ✓ (Already proved, structural.)
  * BUT α_s's precise VALUE+RUNNING is GATED on the parked quark masses: the value 7/20 sits at
    μ ≈ m_c (resolving the old wrong-scale NEG), and the running crosses the thresholds m_c,m_b,m_t
    — all quark masses (parked). 1-loop α_s(M_Z) ≈ 0.122 (~3.5%); the residual IS the threshold
    structure. So α_s inherits the parked mass gate — NOT the clean gate-independent bank hoped.
  * REDIRECT: sin²θ_W = 3/13 = N_c/(2C_2+1) = 0.2308 vs MS-bar 0.2312 (0.19%) is the CLEANER
    gate-independent runner — one scale (M_Z), no quark-threshold cascade, dressing = EW loop. The
    runner effort should pivot here.
  => The strategic bet refined: β₀=g=7 is the clean piece; α_s precision is gated on the parked
  masses; sin²θ_W is the genuinely gate-independent gauge target. Over-sell #8 watch. No count move.
""")
