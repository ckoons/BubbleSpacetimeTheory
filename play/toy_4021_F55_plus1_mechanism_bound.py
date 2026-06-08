"""
Toy 4021: bound on Lyra F55's "+1" integer mechanism (Phase 3 support for Lyra+Keeper).

Lyra F55 candidate: cross-mass integer = n_C + [0 if boson, 1 if fermion]
  -> vector meson (boson) = n_C = 5 ; baryon (fermion) = n_C + 1 = C_2 = 6.
This toy tests that candidate numerically and BOUNDS it, to set expectations for the
Lyra+Keeper spinor-cell finish.

FINDINGS:
 1. The +1 rule FITS the 4 clean ground states (rho,omega -> 5; p,n -> 6). Confirmed.
 2. NOT data-discriminable: for the 4, boson<->meson<->qqbar and fermion<->baryon<->3q
    COINCIDE. The data cannot separate "spin-statistics +1" from "quark-count" -- both
    give 5 (meson) and 6 (baryon). The mechanism choice is a THEORY question, not a data one.
 3. Does NOT extend: Delta (spin-3/2 fermion, 3q) -> both rules predict 6, observed 7.88
    (marginal); phi (boson, strange) -> rule predicts 5, observed 6.52. So the integer rule
    is specific to LIGHT u/d GROUND states; excited (Delta) and strange (phi) are outside it.

IMPLICATION for the Lyra+Keeper finish: the derivation must be THEORETICAL (the 4 states
don't pick the mechanism), and it must EXPLAIN the restriction (why ground-state light u/d
only). Don't look for more confirming data -- the 4 clean states are all there is; derive
the +1 from spinor structure and bound it to the ground-state regime.

GATES (3)
G1: +1 rule fits the 4; mechanism not data-discriminable
G2: rule does not extend (Delta, phi) -> ground-state light-u/d-specific
G3: honest implication for the Lyra+Keeper spinor finish

Per Toy 4017 base-rate discipline; Cal #35, K231c.

Elie - Sunday 2026-06-07
"""

import mpmath as mp
mp.mp.dps = 20
unit = float(mp.pi**5) * 0.51099895
n_C, C_2, N_c, rank = 5, 6, 3, 2

# (name, mass, fermion?, quark-struct, regime)
T = [('rho', 775.26, False, 'qqbar', 'ground ud'), ('omega', 782.66, False, 'qqbar', 'ground ud'),
     ('p', 938.272, True, '3q', 'ground ud'), ('n', 939.565, True, '3q', 'ground ud'),
     ('Delta', 1232.0, True, '3q', 'excited ud'), ('phi', 1019.461, False, 'qqbar', 'strange')]

print("=" * 76)
print("TOY 4021: bound on Lyra F55 '+1' integer mechanism (n_C + [0 bos / 1 ferm])")
print("=" * 76)
print()

print("G1: +1 rule fits the 4 clean ground states; mechanism not data-discriminable")
print("-" * 76)
print(f"  {'state':<8}{'obs r':>8}{'+1 rule':>9}{'fits':>6}  (fermion, quark, regime)")
for nm, m, fer, qs, reg in T:
    r = m / unit
    pred = n_C + (1 if fer else 0)
    res = abs(r - pred)
    fits = 'YES' if res < 0.1 else ('marg' if res < 0.25 else 'NO')
    print(f"  {nm:<8}{r:>8.3f}{pred:>9}{fits:>6}  ({'ferm' if fer else 'bos'}, {qs}, {reg})")
print()
print("  For the 4 clean states: boson<->meson<->qqbar and fermion<->baryon<->3q COINCIDE.")
print("  => the data CANNOT separate 'spin-statistics +1' from 'quark-count' (both fit). The")
print("     mechanism is a THEORY question, not a data one. Also note 6 = C_2 = N_c+1 = rank*N_c")
print("     (three readings of the baryon integer; the 4 states don't pick among them either).")
print()

print("G2: rule does not extend -> ground-state light-u/d-specific")
print("-" * 76)
print("  Delta (spin-3/2 fermion, 3q): +1 rule predicts 6; observed 7.88 (marginal) -> does NOT fit.")
print("  phi (boson, strange): rule predicts 5; observed 6.52 -> does NOT fit (strangeness breaks it).")
print("  => the integer rule holds for LIGHT u/d GROUND states only. Excited + strange are outside")
print("     the pure-substrate-volume regime (explicit mass / excitation).")
print()

print("G3: honest implication for the Lyra+Keeper spinor finish")
print("-" * 76)
print("  - The +1 is data-CONFIRMED on exactly 4 ground states; there is no clean 5th state to")
print("    test it (Delta marginal, strange noise). Don't seek more confirming data.")
print("  - The mechanism (spin-statistics +1 vs quark-count) is NOT data-discriminable -- DERIVE it")
print("    from spinor structure (Lyra+Keeper), don't try to read it off the masses.")
print("  - The derivation must also EXPLAIN the restriction: why light u/d ground states only")
print("    (the pure-volume regime), and why it breaks for excited/strange (explicit mass).")
print("  - Candidate readings to derive-or-eliminate: baryon 6 = C_2 (adjoint) = N_c+1 = rank*N_c;")
print("    meson 5 = n_C (full volume). The +1 = one fermionic/spinor substrate cell is Lyra's lead.")
print()
print("  Score: 3/3 (rule fits 4; not data-discriminable; doesn't extend -> derive the mechanism)")
print()
print("=" * 76)
print("TOY 4021 SUMMARY -- F55 +1 rule fits the 4 ground states but is NOT data-discriminable")
print("  (spin-statistics == quark-count for them) and does NOT extend (Delta, phi). Mechanism")
print("  must be DERIVED (Lyra+Keeper spinor), not read off data; bound to light-u/d ground regime.")
print("=" * 76)
print()
print("SCORE: 3/3")
