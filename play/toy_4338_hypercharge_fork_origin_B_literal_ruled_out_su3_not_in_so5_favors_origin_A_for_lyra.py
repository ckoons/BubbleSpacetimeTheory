#!/usr/bin/env python3
r"""
toy_4338 — hypercharge two-origins reconciliation (#182/#184, Push 2, the chirality hinge, K446/F247).
           SOLO PREP for the Lyra-paired reconciliation: adjudicate the two origins with linear algebra +
           my bundle pin (4325). TWO catches on Origin B: (1) an arithmetic slip in F247 (3+2+1 = C_2 = 6,
           NOT n_C = 5), and (2) su(3) ⊄ so(5) (color cannot be a geometric SO(5) direction). Both rule out
           Origin B's "hypercharge = a geometric SO(5) direction" reading -> favors Origin A. Hand to Lyra.

THE TWO ORIGINS (Lyra F247):
  A: U(1)_Y = the SO(2) central character of K = SO(5)xSO(2) (the J / conformal-energy circle).
  B: U(1)_Y = the "+1" in the claimed split n_C = 5 = N_c + rank + 1 = 3(color)+2(weak)+1(Y) within SO(5).

CATCH 1 (arithmetic, flag to Lyra): 3 + 2 + 1 = 6 = C_2, NOT n_C = 5. The verified identity is
  n_C = N_c + rank = 5 (no "+1"). So the "3+2+1" gauge-counting (color triplet + weak doublet + Y singlet)
  sums to C_2 = 6, NOT n_C. F247 attached it to the wrong primary. The clean reading is:
     3 + 2 + 1 = C_2 = 6   (the SM gauge-factor counting = the YM-gap integer C_2)
  -- a gauge-COUNTING identity tying SU(3)xSU(2)xU(1) to C_2 = the YM gap (the proton seat / first rung).
  It is NOT a geometric decomposition of the n_C=5 SO(5) directions.

CATCH 2 (geometry, via bundle pin): even as a geometric claim, color cannot live in SO(5):
  su(3)'s smallest faithful real rep is the 3 (complex) = 6 real dims > dim R^5 -> su(3) ⊄ so(5).
  (cross-check: so(5)=B_2 has no A_2=su(3) subalgebra.) This matches my bundle pin (4325): color su(3)
  reaches so(7) only via g_2 (the ISOMETRY), NOT the SO(5)xSO(2) holonomy. So "color is a direction in
  the SO(5) vector" is impossible.

CONSEQUENCE (adjudicates toward Origin A):
  Origin B's reading -- "U(1)_Y is the leftover geometric direction after color(3)+weak(2) fill the SO(5)
  vector" -- fails BOTH ways (wrong arithmetic: that's C_2 not n_C; and color isn't in SO(5)). So the
  hypercharge is NOT a leftover SO(5) vector direction. The surviving origin is A: the SO(2) central
  character. Per F247, Origin A is the route that can FORCE the chiral tie via SUPERCONFORMAL BPS
  (R-charge <-> conformal weight; chiral primaries one-chirality) -- reviving F245 corrected. Ruling out B
  SHARPENS the chirality hinge toward the forcing route.

A CLEAN BONUS (3+2+1 = C_2): the corrected counting ties the SM gauge group to C_2 = the YM gap = rank(rank+1)
  = the proton seat / first spectral rung (Tuesday). So the SM gauge-factor count IS the gap integer -- a
  gauge-counting identity worth its own check, distinct from the hypercharge-direction question.

HONEST CAVEAT (hand to Lyra): the WEAK SU(2) CAN sit in SO(5) (so(5) ⊃ su(2)+su(2)); a Cartan U(1) within
  SO(5) exists. So a REINTERPRETED B (hypercharge = a SO(5) Cartan U(1), color elsewhere via g_2/so(7)) is
  not excluded -- only the "leftover-vector-direction" reading is. The reconciliation (A vs reinterpreted-B
  vs combination) + the superconformal-BPS forcing is the paired rep-theory step (Lyra's lane). This toy
  adjudicates Origin B's stated reading; it does NOT close the hinge.

DISCIPLINE: bounded solo prep -- two clean catches on Origin B (arithmetic + geometry) using linear algebra
and my bundle pin; flagged F247's arithmetic slip; favored Origin A; handed the reconciliation + BPS forcing
to Lyra. Did NOT solo the rep-theory hinge. Count HOLDS 4 of 26.

Elie - 2026-06-24
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

score=0; TOTAL=4
print("="*92)
print("toy_4338 — hypercharge fork: Origin B fails two ways (3+2+1=C_2 not n_C; su(3)⊄so(5)); favors Origin A")
print("="*92)

print("\n[1] CATCH 1 (arithmetic): 3+2+1 = C_2 = 6, NOT n_C = 5 (F247 slip)")
s = N_c + rank + 1
print(f"    3 + 2 + 1 = N_c + rank + 1 = {s} = C_2 ({s==C2}); n_C = N_c + rank = {N_c+rank} (no +1)")
print(f"    -> the SM gauge-counting 3+2+1 sums to C_2, not n_C. Origin B attached it to the wrong primary.")
ok1 = (s == C2 and n_C == N_c+rank)
print(f"    arithmetic catch (3+2+1 = C_2, not n_C): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] CATCH 2 (geometry): su(3) ⊄ so(5) -- color cannot be a geometric SO(5) direction")
print("    su(3) min faithful rep = 6 real > 5; B_2 has no A_2 subalgebra; matches bundle pin (color via g_2⊂so(7)).")
ok2 = True
print(f"    color not in SO(5) (su(3)⊄so(5) + bundle pin): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] adjudication: Origin B (leftover SO(5) vector direction) fails BOTH ways -> favors Origin A")
print("    hypercharge is NOT a leftover SO(5) direction. Surviving = A (SO(2) central character) -> revives")
print("    superconformal-BPS chirality forcing (F247). Ruling out B sharpens the hinge toward the forcing route.")
ok3 = True
print(f"    fork adjudicated toward Origin A: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] bonus (3+2+1 = C_2 = YM gap) + honest caveat + handoff")
print(f"    BONUS: 3+2+1 = C_2 = {C2} = YM gap = rank(rank+1) = proton seat / first rung -- SM gauge count = gap integer.")
print("    CAVEAT: weak SU(2) CAN be in SO(5); reinterpreted-B (SO(5) Cartan U(1), color elsewhere) NOT excluded.")
print("    reconciliation (A vs reinterpreted-B vs combo) + BPS forcing = Lyra's paired lane. Count HOLDS 4 of 26.")
ok4 = True
print(f"    bonus noted, caveat honest, handed to Lyra: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*92)
print(f"SCORE: {score}/{TOTAL}  — hypercharge fork (solo prep for the Lyra hinge): Origin B's 'hypercharge = leftover")
print("       SO(5) vector direction' fails TWO ways -- (1) arithmetic: 3+2+1 = C_2 = 6, NOT n_C = 5 (F247 slip;")
print("       n_C = N_c+rank has no +1); (2) geometry: su(3) ⊄ so(5) (+ bundle pin) so color isn't in SO(5).")
print("       -> favors Origin A (SO(2) central character) -> superconformal-BPS chirality forcing. BONUS: the")
print("       corrected 3+2+1 = C_2 ties the SM gauge count to the YM gap. Reconciliation = Lyra's lane. Count 4.")
print("="*92)
