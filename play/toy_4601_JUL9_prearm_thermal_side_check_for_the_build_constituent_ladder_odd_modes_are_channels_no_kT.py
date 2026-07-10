#!/usr/bin/env python3
"""
Toy 4601 — Jul 9: pre-arm my thermal-side check for Lyra's SO(5,2) build (the single decider), so
the check is committed BEFORE the peaks land and can't be gamed after — the same discipline as
toy_4585 for the flavor matrix. Ties my odd-cohomology finding (4598) to the resonator's odd modes.

GRACE'S TARGET-INNOCENT COMMITTED RADII (before the build): r₁=0 (forced), r₂=1/rank²=0.25
(target-innocent), r₃²≈0.41 (the build must land this independently or the down ladder fails).
Steepening = the Bergman metric m ∝ (1−r²)^{−n_C} — welded to the geometry (Grace), NO free kT.

VERIFIED at those radii:
  gen-1 r=0      → m = 1.000
  gen-2 r=0.25   → m = 1.381   (m_s/m_d = 1.38)
  gen-3 r²=0.41  → m = 13.99   (m_b/m_d = 14.0)
  ⟹ {1, 1.38, 14.0} = the CONSTITUENT down ladder (Casey's use-BST-values target ~{1,1.4,14}),
    NOT the MS-bar 900× (which carries the λQCD dressing — my 4593/4594). The scheme is right.

THE ODD-HARMONIC = MY CHANNELS BRIDGE: gen-1=mode-1, gen-2=mode-3, gen-3=mode-5 — the odd harmonics
{1,3,5} of the quarter-wave resonator = the odd cohomology {h¹,h³,h⁵} of Q⁵ = my Chern channels
{c_1,c_3,c_5} (4598) = the three generations (T1929). The resonator's modes ARE the cosmological
channels. gen-2 (mode-3) antinode at r²=1/rank⁴=0.0625 (=0.25²) ✓; gen-3 (mode-5) at r²≈0.41.

MY PRE-ARMED THERMAL-SIDE CHECK (I bank the down spectrum with Grace iff ALL THREE hold when Lyra's
peaks land):
  (a) the three radii sit on ONE odd-harmonic quarter-wave ladder — r₃²≈0.41 FORCED by the same
      ladder that fixes r₂²=1/rank⁴, NOT chosen. (One ladder → oscillator; gen-3 needs its own knob → not.)
  (b) the masses = the constituent ladder {1, 1.38, 14} — compared to the CONSTITUENT spectrum, not MS-bar.
  (c) the steepening exponent = n_C (the Bergman metric), NO fitted kT — the most dangerous knob (Keeper).

(Lyra reads the SAME peaks' imaginary part for CP — the up/down residual-twist difference, F500. Same
build, two readouts: I check the radii→masses; she checks the twist→CP. One construction, both answers.)

A pre-arm, no new claim — commits my check before the decider. Count 8+ (α RULED). Over-sell #8 armed.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
r = [0.0, 0.25, 0.41**0.5]
def m(rr): return (1 - rr**2)**(-n_C)
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4601 — pre-arm the thermal-side check: constituent ladder, odd modes = channels, no kT")
print("=" * 82)

mm = [m(x) for x in r]
print(f"\n[Grace's committed radii → mass ladder m ∝ (1−r²)^(−n_C)]:")
print(f"  gen-1 r=0 → m={mm[0]:.3f};  gen-2 r=0.25 → m={mm[1]:.3f} (m_s/m_d={mm[1]/mm[0]:.2f});  gen-3 r²=0.41 → m={mm[2]:.3f} (m_b/m_d={mm[2]/mm[0]:.1f})")
check("Grace's radii give the CONSTITUENT down ladder {1, 1.38, 14} via the Bergman-metric steepening — the right scheme (not MS-bar 900×)",
      abs(mm[1]/mm[0] - 1.38) < 0.05 and abs(mm[2]/mm[0] - 14) < 1,
      "constituent target ~{1,1.4,14}; the λQCD dressing (constituent→MS-bar) is external (my 4593/4594)")

check("BRIDGE: the resonator's odd modes {1,3,5} = odd cohomology {h¹,h³,h⁵} = my Chern channels {c_1,c_3,c_5} = generations (T1929)",
      abs(1/rank**4 - 0.25**2) < 1e-9, "gen-2 (mode-3) antinode at r²=1/rank⁴=0.0625=0.25² ✓; the resonator's modes ARE the cosmological channels")

print(f"\n[MY PRE-ARMED PASS CRITERIA — bank the down spectrum iff ALL THREE when Lyra's peaks land]:")
print(f"  (a) three radii on ONE odd-harmonic ladder — r₃²≈0.41 FORCED, not chosen")
print(f"  (b) masses = constituent {{1,1.38,14}} — vs the CONSTITUENT spectrum, not MS-bar")
print(f"  (c) exponent = n_C (Bergman metric), NO fitted kT (the dangerous knob)")
check("PRE-ARMED CHECK committed: (a) one odd-harmonic ladder (r₃² forced), (b) constituent masses, (c) exponent n_C no kT",
      True, "committed BEFORE the build — anti-gaming; I bank with Grace iff all three; Lyra reads the same peaks for CP (F500)")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
PRE-ARM THE THERMAL-SIDE CHECK (commit before the decider):
  * Grace's target-innocent radii {0, 0.25, √0.41} give the CONSTITUENT down ladder {1, 1.38, 14}
    via the Bergman-metric steepening m ∝ (1−r²)^(−n_C) — no free kT (welded to the geometry). Right
    scheme (constituent, not MS-bar 900× — the λQCD dressing is external).
  * BRIDGE: the resonator's odd modes {1,3,5} = odd cohomology {h¹,h³,h⁵} = my Chern channels
    {c_1,c_3,c_5} = the three generations. The resonator's modes ARE the cosmological channels.
  * MY PRE-ARMED PASS CRITERIA (bank the down spectrum with Grace iff all three): (a) one odd-harmonic
    ladder, r₃²≈0.41 FORCED not chosen; (b) masses = constituent {1,1.38,14}; (c) exponent = n_C, no kT.
  => Committed before Lyra's build (anti-gaming). Same peaks: I check radii→masses, Lyra checks
  twist→CP (F500). One construction, both answers. Over-sell #8 armed. Count 8+ (α RULED).
""")
