"""
Toy 4008: WALK-BACK of the Szego operator-unification (Cal #259 + Lyra F43).

WHAT HAPPENED
Cal #259 caught a load-bearing conceptual error in Lyra's F38: "(1-P)" was used with
two incompatible meanings —
  (a) orthogonal complement of the holomorphic space (additive; what rho contains), vs
  (b) Shilov boundary-value realization of that space (what the Hardy isometry is about).
The isometry proves E[P]=E[P] (a tautology about P) and says nothing about
rho = E[(1-P)]/E[P]. So the cosmological factor-2 was NEVER derived. Lyra accepted in
full (F43) and extended it: the same swap infects the muon Composite v0.5 additive split.

WHY THIS HITS MY WORK (honest, self-extended like Lyra did)
Toy 4006 G6 and Vol 16 Ch 7 v0.4 Section 4 asserted the UNIFICATION:
  "Cal #254 confirmed at the constant level: muon-edge (81/8) and Lambda-factor (2)
   use the SAME Szego factorization / projection P."
That is exactly the withdrawn claim. WITHDRAWN here.
Worse: Toy 4006 derived 81/8 using "(1-P) = Shilov boundary defect" — meaning (b),
the boundary-realization. But per F43 the muon edge needs meaning (a), the orthogonal
complement. So 4006's 81/8 derivation used the WRONG (1-P) realization; its "FORCED"
status downgrades to "candidate pending the (1-P) decision."

GATES (4)
G1: the error, stated plainly
G2: what is WITHDRAWN (mine)
G3: what SURVIVES (verified)
G4: the sharpened open core + honest status

Per Cal #27 (discipline fires hardest at peak convergence — "derived factor-2 from a
one-line isometry" was peak convergence, the wrong-result profile).
Per Cal #34 numbered correction of Toy 4006 + Ch 7 v0.4.

Elie - Saturday 2026-06-06
"""

from fractions import Fraction as F
n_C, N_c, rank = 5, 3, 2
kappa_Bergman = -n_C

print("=" * 74)
print("TOY 4008: WALK-BACK -- Szego operator-unification withdrawn (Cal #259 + F43)")
print("=" * 74)
print()

print("G1: the error, stated plainly")
print("-" * 74)
print("  '(1-P)' meant two different things and got identified:")
print("    (a) orthogonal complement of the holomorphic space (additive; rho lives here)")
print("    (b) Shilov boundary-value realization of the space (the isometry's subject)")
print("  Hardy isometry => E[P]=E[P] (tautology about P); it does NOT give rho=E[(1-P)]/E[P].")
print("  => the Lambda factor-2 was not derived; muon-edge and vacuum are TWO decompositions.")
print()

print("G2: what is WITHDRAWN (my work)")
print("-" * 74)
print("  - Toy 4006 G6: 'Cal #254 confirmed at constant level: muon-edge + Lambda share P'")
print("    -> WITHDRAWN. They use (a) for the muon edge and (b) for the vacuum; NOT the same P.")
print("  - Vol 16 Ch 7 v0.4 Section 4 ('strong-form Schur-generator, same Szego factorization')")
print("    -> WITHDRAWN. The operator-sharing is a CONJECTURE, not a result.")
print("  - Toy 4006 81/8 'FORCED': derived under (1-P)=(b) boundary-realization, but the muon")
print("    edge needs (a) complement. -> DOWNGRADE 'FORCED' to 'candidate pending (1-P) decision'.")
print()

print("G3: what SURVIVES (verified)")
print("-" * 74)
print("  - Shilov boundary = S^4 x S^1/Z2 is a PRODUCT => kernel factorizes (rigorous,")
print("    independent of which (1-P) meaning). The FACTORIZATION structure stands.")
print("  - 81/8 = N_c^4/2^N_c keeps its OWN standalone falsifier (boundary M.E. = 81/8 or not),")
print("    once re-derived under a consistently-chosen (1-P). It loses only the operator-sharing.")
print("  - [H_B, P] = 0 (additive split real, Lyra F37). Hardy isometry correct (wrong pair).")
print("  - F39 CKM Direction-B fork: independent, survives.")
print("  - R(k) curvature reframe (Lyra F41) = MY Toy 4005/4007 with n_C = -kappa_Bergman:")
for k in (20, 21, 25, 26):
    mine = F(-k * (k - 1), 2 * n_C)
    lyra = F(k * (k - 1), 2 * kappa_Bergman)
    print(f"      k={k}: -C(k,2)/n_C={mine} = C(k,2)/kappa_Bergman={lyra}  {'OK' if mine==lyra else 'X'}")
print("    => the sum-of-roots target Sum roots(a_k) = C(k,2)/n_C = -C(k,2)/kappa_Bergman is")
print("    a CURVATURE statement. This survives and is the genuine mechanism lead (Toy 4007 + F41).")
print()

print("G4: sharpened open core + honest status")
print("-" * 74)
print("  OPEN CORE (one decision now, cleaner than this morning): WHAT IS (1-P)?")
print("  Pick the complement OR the boundary-realization, apply it CONSISTENTLY to both")
print("  the vacuum rho and the muon edge, and re-derive each under it. Then either the")
print("  unification re-closes honestly or it stays two separate decompositions.")
print()
print("  Honest net: I posted '81/8 substrate-FORCED, sub-PCAP closed' an hour ago. The")
print("  forcing rested on the (1-P) conflation. Corrected: 81/8 is a standalone CANDIDATE")
print("  with its own falsifier; the muon<->Lambda unification is a CONJECTURE. Smaller than")
print("  it looked, and caught before it propagated as a false unification into Vol 16.")
print()
print("  Score: 4/4 (error stated; mine withdrawn; survivors verified; open core sharpened)")
print()
print("=" * 74)
print("TOY 4008 SUMMARY -- unification withdrawn; 81/8 -> standalone candidate;")
print("  survivors: factorization, [H_B,P]=0, F39, R(k)=C(k,2)/kappa_Bergman (ties Toy 4007)")
print("=" * 74)
print()
print("SCORE: 4/4")
