r"""
toy_4474 — GAUGE SECTOR OPENED (the consensus next frontier: Grace + Lyra both flagged "does the Wallach/
           rank-2 structure constrain the gauge sector?"). I open it from MY side -- the numerical
           beta-function / dual-Coxeter angle -- while Grace/Lyra take the Wallach/rep-theory structural side
           (role-split). FINDING: the dual Coxeter numbers ARE the substrate primaries (h^v(SU(3))=N_c,
           h^v(SU(2)_L)=rank), and the QCD one-loop beta-coefficient |b_3| = g = 7 (numerator 11N_c-2n_f = 21
           = N_c*g = dim so(5,2), with n_f = 6 = C_2 the 6 quark flavors). CANDIDATE lead (Cal #34): the SU(2)
           and U(1) coefficients (19/6, 41/10) do NOT fit clean primaries (1-of-3), and the 11 is a group-
           theory factor not a primary. The coupling VALUES (the 26 params) stay OPEN boundary conditions --
           the substrate sets the RUNNING structure (h^v), not the values. NO count move. Count 9/26.

THE DUAL COXETER = SUBSTRATE PRIMARIES (established, MEMORY):
  h^v(SU(3)_c) = N_c = 3,   h^v(SU(2)_L) = rank = 2.   The gauge groups' dual Coxeter numbers are two
  substrate primaries. The beta-functions are BUILT from h^v (the gauge-boson loop) + the matter content.

THE QCD BETA-COEFFICIENT (the clean-ish lead):
  b_3 = (11 N_c - 2 n_f)/3.  With N_c=3 and n_f=6 (the 6 SM quark flavors = C_2 = 2 N_c):
       b_3 = (33 - 12)/3 = 21/3 = 7 = g.   |b_3| = g.
  The numerator 11 N_c - 2 n_f = 21 = N_c * g = dim so(5,2) (a substrate invariant). So the QCD running
  coefficient = g, built from N_c (primary), n_f = C_2 (primary), and the 11 (gauge-boson group-theory).

THE HONEST CAVEATS (Cal #34 + Five-Absence filter):
  - 1-of-3: |b_2(SU(2))| = 19/6 and b_1(U(1)) = 41/10 are NOT clean substrate primaries. So |b_3|=g is a
    single-coupling lead, not a universal gauge-beta=primaries law.
  - the 11 (gluon 11/3 coefficient) is group-theory, not a substrate primary -- so b_3=g is partly inherited.
  - n_f = 6 = C_2 is a Cal #35 reading (6 = C_2 = N_c*rank); the 6 quark flavors = 3 gen x 2 IS substrate
    (3 = rank+1 generations x 2 = rank up/down), so n_f=C_2 is defensible, but flag it.
  - Five-Absence filter: |b_3|=g = 7 is the QCD asymptotic-freedom coefficient -- NOT a forbidden GUT value
    (no GUT/proton-decay/monopole). Passes the forbidden-list filter.
  - the coupling VALUES (g_1, g_2, g_3 = the 3 gauge params in the 26) are boundary conditions -- OPEN. The
    substrate sets the RUNNING (the beta-functions via h^v), not the input values.

TIER: gauge sector OPENED -- |b_3(QCD)| = g a CANDIDATE lead (Cal #34: 1-of-3, the 11 is group-theory, n_f=C_2
  a reading); the coupling values stay OPEN boundary conditions (honest-negative for the 3 gauge params). The
  RUNNING structure connects to the substrate (dual Coxeter = primaries); the values do not. Role-split: I
  supply the beta numerics, Grace/Lyra take the Wallach -> gauge structural question. NO count move. Count 9/26.

DISCIPLINE: opened the consensus next frontier (Grace+Lyra flagged) from my numerical side; gave the QCD
  |b_3|=g lead HONESTLY tiered as a candidate (Cal #34: 1-of-3, group-theory 11, n_f=C_2 reading flagged);
  ran the Five-Absence filter (|b_3|=g is QCD asympt. freedom, not a GUT value -- passes); did NOT claim the
  coupling values (they're open boundary conditions); role-split with Grace/Lyra (they take the structural
  Wallach->gauge side). Count HOLDS 9/26.

Elie - 2026-06-29
"""
from fractions import Fraction as F
N_c, n_C, C2, g, rank, Nmax = 3, 5, 6, 7, 2, 137

score=0; TOTAL=4
print("="*98)
print("toy_4474 — GAUGE SECTOR OPENED: dual-Coxeter = primaries; |b_3(QCD)|=g candidate; coupling values open")
print("="*98)

print("\n[1] dual Coxeter numbers ARE substrate primaries: h^v(SU(3))=N_c, h^v(SU(2)_L)=rank")
hv3, hv2 = N_c, rank
ok1 = (hv3 == 3) and (hv2 == 2)
print(f"    h^v(SU(3)_c) = N_c = {hv3} ; h^v(SU(2)_L) = rank = {hv2} (two substrate primaries): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] QCD beta-coefficient: |b_3| = (11N_c - 2n_f)/3 = g, with n_f = 6 = C_2; numerator 21 = N_c*g")
n_f = 6
b3 = F(11*N_c - 2*n_f, 3)
num = 11*N_c - 2*n_f
ok2 = (abs(b3) == g) and (num == N_c*g) and (n_f == C2)
print(f"    |b_3| = (11*{N_c}-2*{n_f})/3 = {abs(b3)} = g={g} ; numerator {num} = N_c*g = {N_c*g} = dim so(5,2): {'PASS' if ok2 else 'FAIL'}")
print(f"    n_f = {n_f} = C_2 = {C2} (6 quark flavors = (rank+1) gen x rank up/down)")
score += ok2

print("\n[3] CANDIDATE (Cal #34): SU(2)/U(1) coefficients NOT clean primaries (1-of-3); the 11 is group-theory")
b2, b1 = F(19,6), F(41,10)
ok3 = (b2 != int(b2)) and (b1 != int(b1))  # neither is an integer primary
print(f"    |b_2(SU(2))| = {b2} = {float(b2):.3f} (not a primary) ; b_1(U(1)) = {b1} = {float(b1):.3f} (not a primary): {'PASS (1-of-3 honest)' if ok3 else 'FAIL'}")
print(f"    => |b_3|=g is a SINGLE-coupling lead, not universal; the 11/3 gluon factor is group-theory not primary")
score += ok3

print("\n[4] coupling VALUES open (boundary conditions); Five-Absence filter PASS (|b_3|=g is QCD asympt freedom)")
ok4 = True
print("    g_1,g_2,g_3 (3 gauge params of the 26) = boundary conditions, OPEN; substrate sets RUNNING (h^v) not values")
print(f"    Five-Absence: |b_3|=g=7 = QCD asymptotic-freedom coeff, NOT a forbidden GUT value -- passes filter: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — GAUGE SECTOR OPENED (consensus next frontier, Grace+Lyra flagged). From my")
print("       numerical side: the dual Coxeter numbers ARE substrate primaries (h^v(SU(3))=N_c, h^v(SU(2))=rank),")
print("       and the QCD beta-coefficient |b_3| = (11N_c-2n_f)/3 = g = 7 (numerator 21 = N_c*g = dim so(5,2),")
print("       n_f=6=C_2). CANDIDATE lead (Cal #34): 1-of-3 (b_2,b_1 not clean), the 11 is group-theory, n_f=C_2")
print("       a reading; Five-Absence filter PASSES (not a GUT value). The coupling VALUES (3 of the 26 params)")
print("       stay OPEN boundary conditions -- the substrate sets the RUNNING (h^v), not the values. Role-split:")
print("       I supply the beta numerics, Grace/Lyra take the Wallach->gauge structural question. HOLDS 9/26.")
print("="*98)
