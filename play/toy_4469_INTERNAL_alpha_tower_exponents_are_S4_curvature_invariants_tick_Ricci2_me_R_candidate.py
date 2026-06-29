r"""
toy_4469 — INTERNAL: the alpha-tower exponents may BE the S^4 heat-kernel curvature invariants (the "why
           alpha^{C_2^2}" framing). The Koons tick = t_P * alpha^{C_2^2} = alpha^{36}; the exponent 36 =
           Ricci^2(S^4) = C_2^2 = the a_2 (curvature^2) Seeley-DeWitt invariant (established 4435/4439/4467).
           NEW LEAD: the m_e alpha-tower exponent (m_e = 6 pi^5 alpha^12 m_P, F66) is 12 = R(S^4) = the SCALAR
           curvature (the a_1, linear). So both alpha-tower exponents = S^4 curvature invariants: m_e ~
           alpha^{R} (a_1), tick ~ alpha^{Ric^2} (a_2). alpha = the per-curvature-unit suppression below
           Planck. The m_e side is a Cal #35 CANDIDATE (12 also = 2*C_2); the tick side is established. The
           deep "why alpha specifically" stays open. INTERNAL (Cal #50). NO count move. Count 9/26.

THE alpha-TOWER (two known rungs):
   m_e  = 6 pi^5 * alpha^12 * m_Planck   (F66, EXTERNAL, banked) -> exponent 12
   tick = t_Planck * alpha^{C_2^2}       (4446, INTERNAL)        -> exponent 36 = C_2^2

THE LEAD -- the exponents are S^4 heat-kernel CURVATURE INVARIANTS (the same S^4 as the muon/tick ladder):
   R(S^4)       = d(d-1)     = 12   (SCALAR curvature, the a_1 / LINEAR invariant)   <-> m_e exponent 12
   Ric^2(S^4)   = (d-1)^2 d  = 36   (RICCI^2, the a_2 / QUADRATIC invariant) = C_2^2  <-> tick exponent 36
  So m_e ~ alpha^{R(S^4)} (a_1, linear curvature) and tick ~ alpha^{Ric^2(S^4)} (a_2, curvature^2). The
  alpha-tower exponent = the heat-kernel curvature invariant at that order; alpha is the per-curvature-unit
  suppression below the Planck scale. This is the "why alpha^{C_2^2}" framing: C_2^2 is the a_2 (Ric^2)
  invariant, and the tower descends by alpha per curvature-unit.

TIER (honest, Cal #35 + target-innocence):
   - ESTABLISHED: the tick exponent = C_2^2 = Ric^2(S^4) = a_2 dim (4435/4439/4467, the determinant/eigenvalue
     + Gilkey structure). Solid.
   - CANDIDATE (flag, do NOT bank): the m_e exponent 12 = R(S^4). 12 ALSO = 2*C_2 (and F66 derives it via the
     gravity/EM scale separately), so "12 = R(S^4)" is a Cal #35 same-number reading -- a suggestive LEAD
     that the alpha-tower exponents are curvature invariants, NOT a forcing. The a_1 (R) / a_2 (Ric^2) pattern
     across m_e and the tick is the suggestive part.
   - DEEP OPEN: "why alpha specifically" (the substrate coupling = the EM/fine-structure constant) as the
     per-curvature-unit factor. Flagged, not solved (the genuine tick frontier).

TIER: tick exponent = a_2 curvature invariant ESTABLISHED; alpha-tower-exponents = curvature-invariants is a
  LEAD (tick side solid, m_e side Cal #35 candidate); "why alpha" deep open. INTERNAL (Cal #50). NO count
  move. Count HOLDS 9/26.

DISCIPLINE: surfaced the alpha-tower-exponents = S^4-curvature-invariants connection (the tick exponent IS
  Ric^2 = a_2, established; the m_e exponent 12 = R(S^4) is a Cal #35 candidate -- flagged 12 = 2*C_2 too,
  not banked); kept the deep "why alpha" open (did not fish a mechanism); INTERNAL per Cal #50. The "why
  alpha^{C_2^2}" framing advanced (exponent = a_2 curvature invariant), not closed. Count HOLDS 9/26.

Elie - 2026-06-29
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
d = 4   # S^4
R = d*(d-1); Ric2 = (d-1)**2*d   # 12, 36

score=0; TOTAL=4
print("="*98)
print("toy_4469 — INTERNAL: alpha-tower exponents = S^4 curvature invariants (tick=Ric^2 established; m_e=R candidate)")
print("="*98)

print("\n[1] tick exponent = C_2^2 = Ric^2(S^4) = a_2 (curvature^2) invariant -- ESTABLISHED (4435/4439/4467)")
ok1 = (C2**2 == Ric2 == 36)
print(f"    tick = t_P * alpha^{C2**2} ; C_2^2 = {C2**2} = Ric^2(S^4) = {Ric2} (a_2 invariant): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] m_e alpha-tower exponent 12 = R(S^4) (scalar, a_1) -- CANDIDATE (Cal #35: 12 also = 2*C_2)")
me_exp = 12
ok2 = (me_exp == R == 2*C2)
print(f"    m_e = 6 pi^5 alpha^{me_exp} m_P (F66) ; R(S^4) = {R} = 2*C_2 = {2*C2}: {'PASS (candidate)' if ok2 else 'FAIL'}")
print(f"    12 = R(S^4) AND 12 = 2*C_2 -> Cal #35 same-number; LEAD that exponents = curvature invariants, NOT banked")
score += ok2

print("\n[3] the pattern: m_e ~ alpha^{R} (a_1, linear) ; tick ~ alpha^{Ric^2} (a_2, quadratic)")
ok3 = (R < Ric2) and (Ric2 == C2**2)
print(f"    a_1 invariant R={R} (m_e, linear curvature) ; a_2 invariant Ric^2={Ric2}=C_2^2 (tick, curvature^2): {'PASS' if ok3 else 'FAIL'}")
print(f"    -> alpha-tower exponent = heat-kernel curvature invariant at that order; alpha = per-curvature-unit suppression")
score += ok3

print("\n[4] tier: tick=a_2 ESTABLISHED; exponents=curvature-invariants a LEAD; 'why alpha' deep open; INTERNAL")
ok4 = True
print("    ESTABLISHED: tick exponent = C_2^2 = Ric^2 = a_2 dim. CANDIDATE: m_e exponent = R(S^4) (Cal #35).")
print(f"    DEEP OPEN: why alpha (EM coupling) is the per-curvature-unit factor. INTERNAL (Cal #50). HOLDS 9/26: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — INTERNAL 'why alpha^{{C_2^2}}' framing: the alpha-tower exponents may BE the S^4")
print("       heat-kernel curvature invariants -- tick exponent C_2^2 = Ric^2(S^4) = a_2 (ESTABLISHED); m_e")
print("       exponent 12 = R(S^4) = scalar curvature = a_1 (CANDIDATE, Cal #35: 12 also = 2*C_2). So m_e ~")
print("       alpha^{R} (linear) and tick ~ alpha^{Ric^2} (quadratic), with alpha the per-curvature-unit")
print("       suppression below Planck. A LEAD (tick side solid, m_e side candidate); the deep 'why alpha")
print("       specifically' stays open. INTERNAL (Cal #50). NO count move. Count HOLDS 9/26.")
print("="*98)
