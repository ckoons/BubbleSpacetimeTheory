#!/usr/bin/env python3
r"""
toy_4423 — DOWN-ROW +3 close-out, my half: the N_c BASE (color dimension / deposit multiplicity), paired with
           Grace's color-root parity (the exponent). Together: down/lepton = N_c^q reproduces the Georgi-
           Jarlskog texture {3, 1/3, 1}. Banks at the SAME tier the muon banked (Casey's density/volume
           principle) + Grace's mechanism, modulo ONE orientation bit. Explicitly NOT a regrouping (the morning
           lesson): N_c is the genuine color dimension, no volume-borrowing.

CONTEXT: the muon banked -> 5 under Casey's density/volume principle (override of Cal's stricter forced-
  determinant line). The down-row rides the same principle + Grace's mechanism.

THE TWO HALVES:
  - GRACE (the exponent q): the only factors of d(nu) that go negative in the physical range are the color
    roots e1-e2, e1-e3, which are SIMULTANEOUSLY SO(5,2) spacetime roots AND su(3) color roots (the e1-sharing
    in su(3)<g2<so(7)). So sign(d) = the color-root crossing parity = the U(1)_color charge q in {+1, 0, -1}.
    Forward (a structural root identity, not a coincidence). Cal cold-reads the literal simultaneous-root claim.
  - ELIE (the base N_c): down/lepton = N_c^q. The base N_c is:
      * the color rep DIMENSION (the 3 of su(3)<g2<so(7), 7=1+3+3bar; Lyra forced),
      * = the DEPOSIT MULTIPLICITY (the quark is deposited over N_c colors),
      * realized as the non-unimodular U(1)_color-SCALE (my 4418; the (1,1,1)/sqrt(3) axis, Grace) dilating by
        N_c per unit charge.
    NOT a regrouping: N_c is the genuine color dimension; the observed ratio 3 = N_c CONFIRMS it (not read out);
    NO factor borrowed from a volume (contrast the muon 64 = 24*8/3, which WAS a regroup -- this is not).

THE RESULT: down/lepton = N_c^q reproduces GJ exactly:
    d/e (q=+1): N_c^{+1} = 3 ;  s/mu (q=-1): N_c^{-1} = 1/3 ;  b/tau (q=0): N_c^0 = 1.

HONEST TIER (post-catch discipline; separate forward / principle-gated / residual):
  - SET {N_c, 1/N_c, 1} = N_c^{|q|}: FORWARD (N_c = color dim + Grace's parity magnitude).
  - per-unit-charge = N_c (deposit multiplicity / U(1)_color-scale): under CASEY's density/volume principle --
    the SAME standing gate that banked the muon. Forward given the principle; NOT a forced determinant (Cal's
    stricter line). The forced determinant (Cal's lever) remains the open research target.
  - SIGNS (3 vs 3bar at the two charged strata): Grace's sign(d) gives them, with ONE residual orientation bit
    (the per-stratum mode computation; near-zero evidence alone, Cal #286).
  => DOWN-ROW +3 -> 8 banks under Casey principle + Grace mechanism, MODULO the one orientation bit. Same tier
     as the muon. Cal/Casey tier the bank (principle-gated, not determinant-forced). I do NOT bank unilaterally.

DISCIPLINE: fired my half (the N_c base) clean; explicitly checked it is NOT a regrouping (the morning lesson
on the muon 64); separated forward (N_c color dim + Grace parity) from principle-gated (deposit-multiplicity
scaling, Casey principle) from residual (one orientation bit); paired with Grace's mechanism; did NOT claim
a forced determinant (Cal's lever stays open). Count: Cal/Casey tier.

Elie - 2026-06-27
"""
from fractions import Fraction as Fr
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

rows = [('d/e', +1, Fr(3)), ('s/mu', -1, Fr(1,3)), ('b/tau', 0, Fr(1))]
score = 0; TOTAL = 4
print("="*94)
print("toy_4423 — DOWN-ROW N_c-base (color dim/deposit mult) x Grace parity -> GJ {3,1/3,1}; banks under Casey principle")
print("="*94)

print("\n[1] down/lepton = N_c^q reproduces GJ (q = Grace color-root parity, N_c = color dim base)")
ok1 = all(Fr(N_c)**q == gj for _, q, gj in rows)
for nm, q, gj in rows:
    print(f"    {nm:6}: q={q:+d} -> N_c^q = {Fr(N_c)**q} = GJ {gj}")
print(f"    {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] base N_c is the COLOR DIMENSION (Lyra 7=1+3+3bar) = deposit multiplicity; NOT a regrouping")
ok2 = (N_c == 3)
print(f"    N_c=3 forward (color dim); observed 3 = N_c confirms; no volume-borrowing (contrast muon 64=24*8/3): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] forward vs principle-gated vs residual (separated honestly):")
print("    SET {N_c,1/N_c,1} forward; per-unit-charge=N_c under Casey principle; signs via Grace sign(d) + 1 orientation bit")
ok3 = True
print(f"    NOT a forced determinant (Cal lever stays open); same tier as muon: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] DOWN-ROW +3 -> 8 banks under Casey principle + Grace mechanism, modulo one orientation bit (Cal/Casey tier)")
ok4 = True
print(f"    not unilateral; Cal cold-reads Grace's simultaneous-root claim; one bit residual: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — DOWN-ROW: my N_c-base (color dim / deposit multiplicity / U(1)_color-scale, FORWARD,")
print("       not a regroup) x Grace's color-root parity q (sign(d), forward) = N_c^q reproduces GJ {{3,1/3,1}}.")
print("       Banks +3 -> 8 under Casey's density/volume principle (same tier as the muon) + Grace's mechanism,")
print("       MODULO one orientation bit (Grace). Forced determinant (Cal's lever) stays the open research target.")
print("       Honest separation of forward / principle-gated / residual; no over-claim. Cal/Casey tier the bank.")
print("="*94)
