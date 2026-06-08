"""
Toy 4031: alpha-tower exponent -- DATA-FORCED to 12, but the DECOMPOSITION 12=rank.C_2 is degenerate.
Reactive-prep numerical input for @Lyra's Thread #1 (alpha-tower derivation; her primary, K231c gate).

Lyra's task: derive the alpha-tower exponent rank.C_2 = 12 in m_e = 6 pi^5 alpha^12 m_Planck
substrate-architecturally, OR honestly report Cal #237 elimination if it's a substrate-natural-
looking FIT rather than a DERIVED mechanism. I do NOT touch the derivation (her lane, numerology
trap). I supply two numerical facts that inform her derive-vs-eliminate decision:

FACT 1 -- the exponent is DATA-FORCED to exactly 12 (sharp):
  6 pi^5 alpha^n vs m_e/m_Planck = 4.1855e-23:
    n=11 -> off by 13608%      n=12 -> 0.032%      n=13 -> off by 99.3%
  Neighbors are off by ~1/alpha ~ 137x. So the integer exponent MUST be 12 -- there IS a real
  target to derive (not a loose/tunable fit on the exponent). Good for Lyra: 12 is real.

FACT 2 -- but the DECOMPOSITION "12 = rank.C_2" is DEGENERATE (the Cal #237 trap):
  12 has MANY substrate-natural decompositions, all equally valid arithmetically:
    rank.C_2 = 2.6        2.C_2 = 2.6 (same)      g + n_C = 7+5
    N_c + g + rank = 3+7+2     N_c.(n_C-1) = 3.4
  So "12 = rank.C_2 because 2x6=12" is NOT a derivation -- ~5 routes hit 12. The sharpness (Fact 1)
  pins the NUMBER; it does NOT privilege rank.C_2 as the MECHANISM. To beat Cal #237, Lyra needs a
  substrate-MECHANISM that forces the rank.C_2 reading specifically (e.g. rank from the chirality/
  spinor doubling x C_2 from the ground-state Casimir, as a CHAIN, not an arithmetic coincidence) --
  and must rule out the competing decompositions, or report elimination if none is forced.

NET for Lyra: the exponent 12 is a genuine data-forced target (derive it), but the rank.C_2 split
is one of ~5 -- the derivation must break that degeneracy by mechanism (K231c "derived not relabeled"),
else Cal #237 elimination is the honest call. Either outcome advances the substrate-architectural state.

GATES (3)
G1: exponent data-forced to exactly 12 (neighbors off by ~137x)
G2: decomposition degeneracy -- ~5 substrate-natural routes to 12 (Cal #237 trap explicit)
G3: honest handoff -- sharpness != mechanism; rank.C_2 needs a degeneracy-breaking CHAIN (Lyra/K231c)

Per Cal #237 (elimination semantics; keep negatives honest); K231c (derived not relabeled);
Cal #265 (status not significance). Reactive-prep; the derivation + verdict are Lyra's.

Elie - Monday 2026-06-08 (assignment #4 reactive-prep for Lyra Thread #1)
"""

import mpmath as mp
mp.mp.dps = 40

n_C, C_2, rank, N_c, g = 5, 6, 2, 3, 7
alpha = mp.mpf('1') / mp.mpf('137.035999084')
target = mp.mpf('9.1093837015e-31') / mp.mpf('2.176434e-8')   # m_e/m_Planck

print("=" * 78)
print("TOY 4031: alpha-tower exponent DATA-FORCED to 12; decomposition 12=rank.C_2 DEGENERATE")
print("=" * 78)
print()

print("G1: exponent is data-forced to exactly 12 (sharp)")
print("-" * 78)
print(f"  m_e/m_Planck = {mp.nstr(target,7)} ; 6 pi^5 alpha^n:")
print(f"  {'n':>5}{'6 pi^5 alpha^n':>17}{'dev':>16}")
for n in range(10, 15):
    val = C_2 * mp.pi**n_C * alpha**n
    dev = abs(val - target) / target * 100
    mark = '  <-- 12 = rank.C_2' if n == 12 else ''
    print(f"  {n:>5}{mp.nstr(val,6):>17}{mp.nstr(dev,5)+'%':>16}{mark}")
print(f"  neighbors n=11,13 off by ~1/alpha ~ 137x  =>  exponent MUST be 12 (real target to derive).")
print()

print("G2: but the decomposition 12 = rank.C_2 is DEGENERATE (Cal #237 trap)")
print("-" * 78)
decomps = [
    ("rank . C_2", rank * C_2), ("2 . C_2", 2 * C_2), ("g + n_C", g + n_C),
    ("N_c + g + rank", N_c + g + rank), ("N_c . (n_C - 1)", N_c * (n_C - 1)),
]
for name, v in decomps:
    print(f"    12 = {name:<16} = {v}   {'OK' if v == 12 else 'NO'}")
print(f"  ~5 substrate-natural routes hit 12. '2x6=12' is arithmetic, not a derivation. Sharpness")
print(f"  pins the NUMBER (Fact 1); it does NOT privilege rank.C_2 as the MECHANISM.")
print()

print("G3: honest handoff to Lyra")
print("-" * 78)
print("  To beat Cal #237: a substrate-MECHANISM CHAIN that forces rank.C_2 specifically (e.g. rank")
print("  = chirality/spinor doubling x C_2 = ground-state Casimir, as a chain), AND rules out the")
print("  competing decompositions -- or report Cal #237 elimination if none is forced. K231c paramount.")
print("  I supply: (1) the exponent IS 12 (data-forced); (2) the rank.C_2 split is 1-of-5 (degeneracy).")
print("  The derivation + the derive-vs-eliminate verdict are Lyra's. @Lyra Thread #1.")
print()
print("  Score: 3/3 (exponent data-forced to 12; decomposition degeneracy explicit; honest handoff)")
print()
print("=" * 78)
print("TOY 4031 SUMMARY -- alpha-tower exponent is DATA-FORCED to exactly 12 (neighbors off ~137x),")
print("  so there's a real target; but ~5 substrate-natural decompositions hit 12, so 'rank.C_2' needs")
print("  a degeneracy-breaking MECHANISM (K231c), else Cal #237 elimination. Reactive-prep for Lyra Thread #1.")
print("=" * 78)
print()
print("SCORE: 3/3")
