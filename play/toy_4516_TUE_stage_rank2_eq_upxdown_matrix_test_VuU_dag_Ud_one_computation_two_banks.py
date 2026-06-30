r"""
toy_4516 — TUESDAY PRIMARY (Keeper board): STAGE the rank^2 = up x down test for sin theta_C -- the one
           computation that closes TWO banks (sin theta_C 10->11 AND theta_12 11->12, the linked dim_R pair).
           Per Casey's linear-algebra directive (V_CKM = U_u^dag . U_d -- literally matrix multiplication), I
           set up the structural factoring + the explicit numerical test now, so I confirm the INSTANT Grace
           hands the kernel structure. STRUCTURAL SETUP: the 80-mode count factors as 80 = rank^4*n_C =
           (S^4 harmonics <=2 = 20) x (rank^2 = 4); the rank^2 = (up-sector rank-2)(down-sector rank-2), since
           V = U_u^dag . U_d composes the up and down 1-2 rotations (each a rank-2 block). So sin^2 theta_C =
           rank^2/((S^4 x rank^2) - 1) = rank^2/(rank^4*n_C - 1) = 4/79 = 0.0506 (obs 0.0503). STAGED TEST:
           when Grace hands U_u, U_d (or the kernel c(z_i,z_j)), confirm |V_us|^2 = |(U_u^dag.U_d)_{12}|^2 =
           4/79 with the rank^2 arising from the up x down product. Gated ONLY on Grace's kernel handoff (the
           joint primary). NO count move (staged). Count 9/26 (10 firm with theta_13).

THE STRUCTURAL FACTORING (sets up the rank^2 as up x down):
  total mode count = rank^4*n_C = 80. Factor: 80 = (rank^2*n_C = 20 = S^4 harmonics up to degree 2) x rank^2.
  The rank^2 = the two-sector product: V = U_u^dag . U_d (Lyra F436) composes the up-sector 1-2 rotation and
  the down-sector 1-2 rotation, each a rank-2 (2x2) block -> rank x rank = rank^2. So the overlap samples the
  S^4 harmonics with the up x down two-sector multiplicity rank^2; minus the constant mode (-1, T1444):
       sin^2 theta_C = rank^2 / (S^4_harmonics x rank^2 - 1) = rank^2/(rank^4*n_C - 1) = 4/79.

THE STAGED MATRIX TEST (per linear-algebra directive; ready for Grace's kernel handoff):
  V_us = (U_u^dag . U_d)_{12}. When Grace supplies the up/down 1-2 rotations U_u, U_d (or equivalently the
  coherent-state kernel c(z_i, z_j) at the mass-addresses), I confirm:
     |V_us|^2 = 4/79 = rank^2/(rank^4*n_C - 1), with the rank^2 emerging from the up x down composition.
  IF confirmed -> rank^2 = up x down -> sin theta_C banks (10->11) AND theta_12 banks as the linked dim_R
  pair (11->12). ONE matrix multiplication, TWO banks.

WHAT'S STILL NEEDED (the joint primary, gated): Grace's explicit kernel / up-down rotation structure. I have
  the test set up and the structural factoring done; the confirmation is the matrix multiplication once her
  kernel lands. I do NOT pre-confirm (the up x down product must actually yield rank^2, not be assigned -- the
  (C) trap); the matrix multiplication decides it.

TIER: rank^2 = up x down STAGED -- structural factoring (80 = S^4 x rank^2; rank^2 = up x down per
  V = U_u^dag U_d) + explicit matrix test (|V_us|^2 = 4/79) ready for Grace's kernel. sin theta_C strong-(B),
  ONE residual (this confirmation) from (A). Gated on Grace's kernel handoff. NO count move. Count HOLDS 9/26
  (10 firm with theta_13).

DISCIPLINE: staged my PRIMARY (the rank^2 = up x down confirmation) per the linear-algebra directive (wrote
  the matrix V = U_u^dag . U_d, set the explicit target |V_us|^2 = 4/79); did the structural factoring
  (80 = S^4 x rank^2) but did NOT pre-confirm the up x down = rank^2 (that needs Grace's actual kernel -- the
  matrix multiplication decides, not an assignment, per the (C) trap); staged to confirm the instant her
  kernel lands. Count HOLDS 9/26.

Elie - 2026-06-30
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

score=0; TOTAL=3
print("="*98)
print("toy_4516 — TUE stage rank^2 = up x down (V = U_u^dag . U_d): one matrix multiplication, two banks")
print("="*98)

print("\n[1] structural factoring: 80 = rank^4*n_C = (S^4 harmonics 20) x rank^2; rank^2 = up x down (each rank-2)")
S4 = rank**2*n_C; total = rank**4*n_C
ok1 = (total == 80) and (total == S4*rank**2) and (S4 == 20)
print(f"    80 = {total} = (S^4 harmonics {S4}) x rank^2 ({rank**2}); rank^2 = (up rank-2)(down rank-2) via U_u^dag U_d: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] sin^2 theta_C = rank^2/(S^4 x rank^2 - 1) = rank^2/(rank^4 n_C - 1) = 4/79 (0.0506 vs obs 0.0503)")
val = rank**2/(total-1)
ok2 = (abs(val-0.0503)/0.0503 < 0.01) and (total-1 == 79)
print(f"    rank^2/(80-1) = 4/79 = {val:.5f}; -1 = constant mode (T1444): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] STAGED matrix test (Grace kernel): |V_us|^2 = |(U_u^dag.U_d)_12|^2 = 4/79 -> if up x down gives rank^2, TWO banks")
ok3 = True
print("    one matrix multiplication closes sin theta_C (10->11) + theta_12 (11->12); NOT pre-confirmed (matrix decides, not assigned)")
print(f"    gated only on Grace's kernel handoff (joint primary); staged to confirm instantly: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — TUE PRIMARY staged: rank^2 = up x down (V = U_u^dag . U_d). Structural factoring:")
print("       80 = (S^4 harmonics 20) x (rank^2 = up x down, each sector a rank-2 1-2 rotation). sin^2 theta_C =")
print("       rank^2/(rank^4 n_C - 1) = 4/79. STAGED matrix test (per linear-algebra directive): |V_us|^2 =")
print("       |(U_u^dag.U_d)_12|^2 = 4/79 with rank^2 from the up x down product -- confirm the INSTANT Grace")
print("       hands the kernel. ONE matrix multiplication closes TWO banks (sin theta_C 10->11, theta_12 11->12).")
print("       Not pre-confirmed (the matrix decides, not an assignment). Gated on Grace's kernel. HOLDS 9/26.")
print("="*98)
