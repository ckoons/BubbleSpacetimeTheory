# TOY 5460 -- the natural-object DIMENSION POOL for D_IV^5, derived from GENERATORS not by hand.
# Elie, 2026-08-23. R67: score the five -1's. Rubric cell: External 3 / flavor structure.
# NO CKM VALUE IS COMPUTED. Dimensions and multiplicities only. Inside the boundary I drew.
#
# THE TEST (Cal, via R67): a vacuum subtraction is legitimate IFF N is the DIMENSION of a natural
# object on D_IV^5 WHOSE UNIQUE CONSTANT/TRIVIAL SUBREPRESENTATION IS REMOVED. If N is not a
# dimension of anything, the -1 is an adjacency.
#
# ★ THE TWO THINGS KEEPER'S HAND-BUILT POOL CANNOT HAVE, and which decide the answer:
#   (1) THE CONTROL MUST GATE THE READ. Not run-then-look. Gate.
#   (2) *** POOL DENSITY. *** If the generated pool contains a large fraction of small integers,
#       then "N is a dimension" IS NOT EVIDENCE -- it is what chance supplies. This is the exact
#       alpha lesson (5457) applied to a membership test instead of an expressibility test, and a
#       hand-built pool CANNOT be density-checked because its size is set by the builder's memory.
#   (3) ★ AND THE DISTINCTION THE TEST ACTUALLY TURNS ON: an IRREP HAS NO TRIVIAL SUBREP. Only a
#       REDUCIBLE object (a function space, a partial sum, an exterior power) can have a UNIQUE
#       trivial summand to remove. So "N is some dimension" is NOT the test. The test is
#       "N is the dimension of an object with exactly one trivial summand."

from math import comb
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5460 -- natural dimension pool, DERIVED. Control gates the read. Density reported.")
print("  Scope: dimensions/multiplicities only. NO CKM VALUE COMPUTED."); print(BAR)

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7

# ---------- generators, all from the D_IV^5 structure -------------------------------------------
def so_dim(n): return n*(n-1)//2
DIM_G   = so_dim(7)          # SO(5,2)
DIM_K   = so_dim(5) + 1      # SO(5) x SO(2)
DIM_P   = DIM_G - DIM_K      # tangent space
def so5_irrep(a,b):          # Weyl dim, B2/C2 Dynkin labels
    return (a+1)*(b+1)*(a+b+2)*(2*a+b+3)//6
def H_k_S4(k):               # degree-k spherical harmonics on S^4
    return comb(k+4,4) - (comb(k+2,4) if k>=2 else 0)

POOL = {}   # dim -> list of (witness, has_unique_trivial?)
def add(d, w, triv):
    if 1 <= d <= 400: POOL.setdefault(d, []).append((w, triv))

# (1) SO(5) irreps -- IRREPS HAVE NO TRIVIAL SUBREP (except the trivial itself)
for a in range(0,9):
    for b in range(0,9):
        d = so5_irrep(a,b)
        add(d, "SO(5) irrep (%d,%d)"%(a,b), (a==0 and b==0))
# (2) S^4 harmonics: each H_k is irreducible (no trivial for k>=1); PARTIAL SUMS have exactly one
for k in range(0,12): add(H_k_S4(k), "H_%d(S^4)"%k, k==0)
s = 0
for K in range(0,12):
    s += H_k_S4(K)
    add(s, "sum_{k<=%d} H_k(S^4)  [polys deg<=%d on S^4]"%(K,K), True)   # contains exactly one constant
# (3) algebra dims
for d,w in ((DIM_G,"dim SO(5,2) = so(7)"),(so_dim(5),"dim SO(5)"),(1,"dim SO(2)"),
            (DIM_K,"dim K = SO(5)xSO(2)"),(DIM_P,"dim p (tangent)"),(so_dim(6),"dim SO(6)"),
            (so_dim(10),"dim SO(10)"),(so_dim(4),"dim SO(4)")):
    add(d, w, False)
# (4) exterior / symmetric powers of p (dim 10) and of the vector 5
for j in range(1,11):
    add(comb(10,j), "Lambda^%d(p), p=10"%j, j==2)      # Lambda^2(p) contains the Kahler form: ONE trivial
    add(comb(10+j-1,j), "Sym^%d(p)"%j, j==2)           # Sym^2 contains the metric: ONE trivial
for j in range(1,9):
    add(comb(5,j), "Lambda^%d(R^5)"%j, False)
    add(comb(5+j-1,j), "Sym^%d(R^5)"%j, j==2)          # Sym^2(R^5) contains the trace: ONE trivial
# (5) Shilov boundary S^4 x S^1 : products H_k x (characters)
add(5, "dim Shilov S^4 x S^1", False)

# ---------- POSITIVE CONTROL -- GATES THE READ ---------------------------------------------------
head("PART A -- POSITIVE CONTROL. It GATES the read; nothing below is reported if it fails.")
MUST_CATCH = {5:"SO(5) vector", 10:"dim SO(5) = dim p", 11:"dim K", 14:"sym traceless 5x5", 21:"dim so(7)"}
MUST_REJECT = {13:"prime, no natural D_IV^5 object", 19:"prime", 23:"prime"}
ok = True
print("  MUST-CATCH:")
for d,label in MUST_CATCH.items():
    hit = d in POOL
    print("     %-4d %-24s %s"%(d,label,"FOUND: "+POOL[d][0][0] if hit else "*** MISSING ***"))
    ok = ok and hit
print("  MUST-REJECT (a pool containing these is too coarse to mean anything):")
for d,label in MUST_REJECT.items():
    hit = d in POOL
    print("     %-4d %-24s %s"%(d,label,"*** PRESENT (%s) -- BAD ***"%POOL[d][0][0] if hit else "absent, correct"))
    ok = ok and (not hit)
print("\n  *** GATE: %s ***"%("PASS -- proceeding to read" if ok else "FAIL -- COUNTS NOT READ"))
if not ok:
    print("  Instrument not validated. No scores reported."); raise SystemExit

# ---------- POOL DENSITY -- the real test --------------------------------------------------------
head("PART B -- ★ POOL DENSITY. If the pool is dense, 'N is a dimension' is NOT evidence.")
for lo,hi in ((1,50),(1,100),(1,200),(50,150)):
    inpool = sum(1 for d in range(lo,hi+1) if d in POOL)
    print("   integers in [%3d,%3d]: %3d of %3d in pool = %5.1f%%"%(lo,hi,inpool,hi-lo+1,100.0*inpool/(hi-lo+1)))
triv = {d for d in POOL if any(t for _,t in POOL[d])}
for lo,hi in ((1,50),(1,100),(1,200)):
    n = sum(1 for d in range(lo,hi+1) if d in triv)
    print("   ...of which have a UNIQUE TRIVIAL summand [%3d,%3d]: %3d = %5.1f%%"%(lo,hi,n,100.0*n/(hi-lo+1)))
print("\n  *** THE SECOND ROW IS THE ONE THAT MATTERS. Only an object with a unique trivial summand")
print("      can HAVE a vacuum subtraction. An irrep cannot -- it has no trivial to remove. ***")

# ---------- SCORE THE FIVE -----------------------------------------------------------------------
head("PART C -- SCORE ALL FIVE -1's. N = pre-subtraction; N-1 = the quoted integer.")
FIVE = [("2/sqrt(79)", 80, 79, "rank^4 n_C"),
        ("9/11",       12, 11, "2 C_2"),
        ("17 (dressed Casimir)", 18, 17, "N_c C_2"),
        ("136 = N_max-1", 137, 136, "N_max"),
        ("44/45",       45, 44, "N_c^2 n_C")]
print("   quoted        N     N in pool?                          N has UNIQUE TRIVIAL?   verdict")
for name,N,Nm1,src in FIVE:
    inp = N in POOL
    wit = POOL[N][0][0] if inp else "-"
    tv  = N in triv
    twit = next((w for w,t in POOL[N] if t), "-") if tv else "-"
    if tv:   v = "*** LEGITIMATE SHAPE ***"
    elif inp: v = "dim, but NO trivial to remove"
    else:    v = "NOT A DIMENSION -> ADJACENCY"
    print("   %-13s %-5d %-34s %-23s %s"%(name,N,(wit[:33] if inp else "NO"),(twit[:22] if tv else "no"),v))
print("\n   and the quoted integers themselves (N-1), for the 'it IS a dimension' reading:")
for name,N,Nm1,src in FIVE:
    inp = Nm1 in POOL
    print("   %-13s N-1 = %-5d %s"%(name,Nm1,("IS a dimension: "+POOL[Nm1][0][0]) if inp else "not a dimension"))

# ---------- verdict ------------------------------------------------------------------------------
head("VERDICT")
print(" (1) The gate passed: pool catches all five known dimensions and rejects three primes.")
print(" (2) DENSITY is the finding -- see Part B. Read the unique-trivial row, not the any-dimension row.")
print(" (3) Scores in Part C. A subtraction is only well-shaped where N carries a UNIQUE TRIVIAL summand.")
print(" (4) I did NOT compute a single CKM value. This is mode/dimension structure only.")
print("     Nothing pushed. CP existence-only.")
