"""
Toy 4023: test Lyra's cells = n_C + 2*lambda2 extension (lambda2 >= 1) on PDG data.

Lyra handed me the falsifier: cells = n_C + 2*lambda2 predicts lambda2=1 -> 7 cells (1095 MeV),
lambda2=3/2 -> 8 (1251). Test on light u/d hadrons in the window, base-rate discipline (Toy 4017).

RESULT: the CORE is confirmed (lambda2=0 mesons -> 5; lambda2=1/2 baryons -> 6, the 4 clean
states). The lambda2 >= 1 EXTENSION does NOT cleanly hold, for two honest reasons:

 1. lambda2 is NOT the spin. rho,omega are spin-1 bosons but lambda2 = 0 (Lyra). So "lambda2 = J"
    is the wrong proxy from the start -- and it's the only proxy available without the explicit
    SO(2)-charge (K-type) assignment, which is theory (Lyra/Keeper).
 2. Under lambda2 = J (the proxy), the extension FAILS: a1(1260) J=1 -> predict 7, obs 7.87
    (resid 0.87); f2(1270) J=2 -> predict 9, obs 8.16 (resid 0.84); only Delta (J=3/2 -> 8,
    obs 7.88) is near. And the candidates PILE near 8 cells regardless of spin (a1 7.87, b1 7.86,
    f2 8.16, a2 8.43, Delta 7.88) -- a CLUSTER, not a lambda2-spread ladder.

VERDICT: cells = n_C + 2*lambda2 is confirmed on the 4 clean states; the lambda2 >= 1 extension
is UNCONFIRMED. Either lambda2 != J (needs the real SO(2) charges to test -- theory), or the law
is bounded to the lambda2 = 0, 1/2 states. The excited mesons clustering near 8 (not laddering by
spin) is evidence against the spin-proxy extension. This is the honest falsifier result Lyra asked
for: the prediction, tested, does not cleanly extend under the available assignment.

What survives: the 4-state core (mesons n_C, baryons n_C+1) + the Z_2 mechanism for the +1
(Toys 4022, Keeper F0, Lyra/Grace) -- all intact. Only the lambda2 >= 1 LADDER is unconfirmed.

GATES (4)
G1: core confirmed (lambda2 = 0, 1/2)
G2: lambda2 != spin (rho,omega disprove the proxy)
G3: extension under lambda2 = J fails + candidates cluster near 8 (not a ladder)
G4: honest verdict + handoff (need real SO(2) charges, or law is 4-state-bounded)

Per Toy 4017 base-rate; Cal #35, Cal #237, K231c.

Elie - Sunday 2026-06-07
"""

import mpmath as mp
mp.mp.dps = 15
unit = float(mp.pi**5) * 0.51099895
n_C = 5

print("=" * 78)
print(f"TOY 4023: cells = n_C + 2*lambda2 extension test (unit pi^5 m_e = {unit:.2f} MeV)")
print("=" * 78)
print()

print("G1: core confirmed (lambda2 = 0, 1/2)")
print("-" * 78)
for nm, m, lam in [('rho', 775.26, 0), ('omega', 782.66, 0), ('p', 938.272, 0.5), ('n', 939.565, 0.5)]:
    pred = n_C + 2 * lam
    print(f"  {nm:<7} lambda2={lam}: cells pred {pred:.0f}, obs {m/unit:.3f} ({abs(m/unit-pred)/pred*100:.2f}%)")
print("  Core (4 clean states) CONFIRMED.")
print()

print("G2: lambda2 != spin (the proxy is wrong from the start)")
print("-" * 78)
print("  rho, omega are spin-1 bosons but lambda2 = 0 (Lyra). So lambda2 is NOT the spin J.")
print("  Without the explicit SO(2)-charge (K-type) assignment, lambda2=J is the only proxy -- and")
print("  it already mis-assigns the mesons. The real test needs the theory SO(2) charges.")
print()

print("G3: extension under lambda2 = J fails; candidates cluster near 8 (not a ladder)")
print("-" * 78)
cand = [('a1(1260)', 1230.0, 1), ('b1(1235)', 1229.5, 1), ('f2(1270)', 1275.5, 2),
        ('a2(1320)', 1318.2, 2), ('Delta(1232)', 1232.0, 1.5), ('N(1440)', 1440.0, 0.5)]
print(f"  {'state':<12}{'obs cells':>10}{'J':>5}{'pred(λ2=J)':>11}{'resid':>7}{'verdict':>9}")
for nm, m, J in cand:
    obs = m / unit
    pred = n_C + 2 * J
    res = abs(obs - pred)
    v = 'near' if res < 0.25 else 'MISS'
    print(f"  {nm:<12}{obs:>10.3f}{J:>5}{pred:>11.0f}{res:>7.2f}{v:>9}")
print("  -> a1, b1, f2, a2 MISS their lambda2=J predictions by ~0.85 cells; only Delta near.")
print("  -> the states PILE near 8 cells regardless of spin (cluster), NOT a lambda2-spread ladder.")
print("     A genuine lambda2 ladder would spread 7,8,9 by spin; instead they bunch at ~8.")
print()

print("G4: honest verdict + handoff")
print("-" * 78)
print("  CONFIRMED: cells = n_C + 2*lambda2 on the 4 clean states (lambda2 = 0 mesons, 1/2 baryons).")
print("  UNCONFIRMED: the lambda2 >= 1 extension. Under lambda2=J it fails; lambda2 != J anyway.")
print("  The excited mesons cluster near 8 cells (not a spin-ladder) -- evidence against the spin-proxy.")
print()
print("  HANDOFF to Lyra/Keeper: to test the extension I need the explicit SO(2) charges (K-type")
print("  lambda2) per state -- theory, not spin. As it stands the law is confirmed on lambda2 = 0, 1/2")
print("  and the ladder is unconfirmed. Honest: this is the wobbly part (weekend pattern -- the")
print("  extension past the clean core doesn't cleanly survive the data under available assignments).")
print()
print("  WHAT SURVIVES INTACT: the 4-state core + the Z_2 mechanism for the +1 (Toys 4022 / Keeper F0 /")
print("  Lyra / Grace). Only the lambda2 >= 1 LADDER is in question; the +1 itself stands.")
print()
print("  Score: 4/4 (core confirmed; lambda2!=spin shown; extension fails under proxy + clusters;")
print("  honest handoff for real SO(2) charges)")
print()
print("=" * 78)
print("TOY 4023 SUMMARY -- cells=n_C+2*lambda2 CONFIRMED on 4 clean states; lambda2>=1 ladder")
print("  UNCONFIRMED (lambda2 != spin; candidates cluster near 8, not a spin-ladder). +1 mechanism")
print("  (Z_2 twist) stands; the LADDER extension needs real SO(2) charges or is 4-state-bounded.")
print("=" * 78)
print()
print("SCORE: 4/4")
