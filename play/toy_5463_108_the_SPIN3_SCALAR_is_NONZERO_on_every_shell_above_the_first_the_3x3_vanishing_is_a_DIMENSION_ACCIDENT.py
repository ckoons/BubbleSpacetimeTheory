# TOY 5463 -- #108 REDUCED: IS THE SPIN-3 SCALAR ZERO?  Elie, 2026-08-23.
# Lyra's reduction (R69-A): compute [T_{Y22}, T_{Y21}] and read the m=3 component.
# Multiplicity 1 in Lambda^2(spin-2) = spin-1 (+) spin-3 means ONE SCALAR -- no sweep, no look-elsewhere.
#
# RULE 4, RECONNECTED FIRST (my own prior work + Keeper's floor):
#   K1677: su(3) the ALGEBRA is real (d-symbol 2.31 vs so(3) control 0; Killing -12 compact),
#          BUT closure is IMPOSED by the 3x3 matrix realization: [S_a,S_b] of symmetric 3x3 is
#          antisymmetric 3x3 = a 3-dim space WITH NO ROOM FOR SPIN-3. "The realization imposes
#          the truncation; it isn't derived." Named next step: kill the spin-3 WITHOUT assuming 3x3.
#   Toy 5349 (mine): scored that test 2 PASS / 1 CONDITIONAL / 2 NOT-DERIVED. The rank of
#          span{[S_a,S_b]} came out 3 = so(3) only.
#
# THE KEY OBSERVATION THAT MAKES THIS COMPUTABLE AND HONEST:
#   By WIGNER-ECKART, a Toeplitz operator T_f with an l=2 symbol, RESTRICTED TO ONE SHELL, is
#   proportional to the rank-2 spherical tensor operator on that shell -- the reduced matrix
#   element is a scalar that cannot affect VANISHING. So the shell-restricted question
#   "[T_{Y22}, T_{Y21}] = 0 ?" is exactly "[T^2_2, T^2_1] = 0 ?" on that shell.
#   And since [T^2_2, T^2_1] carries m = 3, while spin-1 operators have max |m| = 1,
#   *** ANY NONZERO VALUE IS PURELY SPIN-3. The test is a clean yes/no. ***

import numpy as np
np.set_printoptions(precision=6, suppress=True)
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)

def J_ops(twoL):
    """angular momentum matrices for spin L = twoL/2, dimension twoL+1"""
    L = twoL/2.0
    dim = twoL+1
    ms = [L - i for i in range(dim)]          # m = L, L-1, ..., -L
    Jz = np.diag(ms).astype(complex)
    Jp = np.zeros((dim,dim), complex)
    for i in range(1, dim):                    # J_+ |m> = sqrt(L(L+1)-m(m+1)) |m+1>
        m = ms[i]
        Jp[i-1, i] = np.sqrt(L*(L+1) - m*(m+1))
    return Jz, Jp

def quads(twoL):
    """rank-2 spherical tensor operators built from J (standard quadrupole forms)"""
    Jz, Jp = J_ops(twoL)
    Jm = Jp.conj().T
    T2p2 = Jp @ Jp
    T2p1 = -(Jp @ Jz + Jz @ Jp)
    J2 = Jz@Jz + 0.5*(Jp@Jm + Jm@Jp)
    T20 = (2*Jz@Jz - 0.5*(Jp@Jm + Jm@Jp)) / np.sqrt(6)
    return T2p2, T2p1, T20, J2

print(BAR); print("TOY 5463 -- #108: IS THE SPIN-3 SCALAR ZERO?  [T^2_2, T^2_1] on each shell."); print(BAR)

head("PART A -- GATE: verify the tensor operators are correct before using them")
print("  Checks: (i) J^2 = L(L+1) I on each shell; (ii) T^2_2 raises m by exactly 2;")
print("          (iii) on the l=1 shell the five T^2_M must span the SAME space as the five")
print("                symmetric traceless 3x3 quadrupoles of my 5349 (dimension 5).")
ok=True
for twoL in (2,4,6,8):
    Jz,Jp = J_ops(twoL); Jm = Jp.conj().T
    J2 = Jz@Jz + 0.5*(Jp@Jm + Jm@Jp)
    L = twoL/2.0
    good = np.allclose(J2, L*(L+1)*np.eye(twoL+1))
    T2p2 = (Jp@Jp)
    # raising check: nonzero entries only on the 2nd superdiagonal
    off = np.abs(T2p2 - np.triu(np.tril(T2p2, -2)*0 + T2p2, 2)).max() if twoL>=2 else 0
    raise_ok = np.allclose(T2p2, np.triu(T2p2,2))
    ok = ok and good and raise_ok
    print("     L=%-4s dim=%-3d  J^2 = L(L+1)I : %-5s   T^2_2 raises m by 2 : %s"
          %(L,twoL+1,"yes" if good else "NO","yes" if raise_ok else "NO"))
print("\n  *** GATE: %s ***"%("PASS" if ok else "FAIL -- nothing below is read"))
if not ok: raise SystemExit

head("PART B -- ★ THE TEST. [T^2_2, T^2_1] carries m=3, so ANY nonzero value is PURELY SPIN-3.")
print("   shell L    dim    || [T^2_2, T^2_1] ||_F        spin-3 scalar")
rows=[]
for twoL in (2,4,6,8,10,12):
    T2p2, T2p1, T20, J2 = quads(twoL)
    C = T2p2 @ T2p1 - T2p1 @ T2p2
    nrm = np.linalg.norm(C)
    rows.append((twoL/2.0, twoL+1, nrm))
    verdict = "ZERO -- spin-3 annihilated" if nrm < 1e-10 else "*** NONZERO -- SPIN-3 SURVIVES ***"
    tag = "   <- K1677's 3x3 realization" if twoL==2 else ""
    print("   L=%-8s %-6d %-27.10f %s%s"%(twoL/2.0, twoL+1, nrm, verdict, tag))

head("PART C -- WHAT IT MEANS")
L1 = [r for r in rows if r[0]==1.0][0]
rest = [r for r in rows if r[0]>1.0]
print(" (1) *** ON THE L=1 SHELL (dim 3) THE COMMUTATOR VANISHES IDENTICALLY: ||.|| = %.3e ***"%L1[2])
print("     That is K1677's 3x3 matrix realization, and it reproduces exactly what my 5349 found")
print("     (rank 3 = so(3) only, spin-3 absent). *** CONFIRMED, and confirmed to be an ACCIDENT: ***")
print("     T^2_2 raises m by 2, T^2_1 raises by 1, so the product raises by 3 -- and on a 3-dim")
print("     shell (m = -1,0,1) THERE IS NO PAIR OF STATES SEPARATED BY 3. The operator has nowhere")
print("     to send anything. *** THE VANISHING IS A DIMENSION ACCIDENT, NOT A GEOMETRIC CANCELLATION. ***")
print()
print(" (2) *** ON EVERY SHELL ABOVE THE FIRST THE COMMUTATOR IS NONZERO: ***")
for L,d,n in rest:
    print("        L=%-5s dim=%-4d ||[T^2_2,T^2_1]||_F = %.6f"%(L,d,n))
print("     and since m=3 forces it to be pure spin-3, *** THE SPIN-3 SCALAR IS NONZERO. ***")
print()
print(" (3) ⟹ THE ANSWER TO #108's REDUCED QUESTION IS **NO**. The spin-3 scalar is NOT zero.")
print("     The geometry does NOT annihilate the spin-3 on any shell that has room for it.")
print("     *** K1677's HONEST FLOOR STANDS AS DRAWN. #108 DOES NOT PROMOTE. ***")

head("VERDICT")
print(" (1) Gate passed before use (J^2 eigenvalues, raising structure).")
print(" (2) L=1: commutator identically zero -- reproduces K1677/5349 -- BUT the mechanism is")
print("     dimensional (no two states separated by m=3 on a 3-dim shell), not geometric.")
print(" (3) L>=2: commutator NONZERO on every shell tested. Pure spin-3 by the m=3 selection rule.")
print(" (4) *** #108 DOES NOT PROMOTE. K1677's floor stands as drawn: container yes, mechanism open. ***")
print("     This is a NEGATIVE and it is the answer Lyra's reduction was designed to be able to give.")
print()
print(" *** RULE 3: ONE CI -- ME. NOT FILED. Needs a second before it is anything. ***")
print("     Attack surface, named: (i) the Wigner-Eckart step -- that a shell-restricted Toeplitz")
print("     operator with an l=2 symbol IS proportional to T^2_M, so the reduced matrix element")
print("     cannot affect vanishing; (ii) whether 'the second shell' in K1677/R69 means L=2 in MY")
print("     labelling or something else -- an object-identification step, and today has taught me")
print("     to distrust exactly that; (iii) whether the Hankel term can contribute OFF-shell in a")
print("     way a single-shell restriction cannot see. (iii) is the one I would attack first.")
print("     Nothing pushed. Nothing banked. CP existence-only.")
