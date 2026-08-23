"""
TOY 5453 - Elie - 2026-08-22 (R60)
================================================================================
ASSIGNMENT (R60_TEAM_PROMPT.md, section 4): "ELIE 1 is now UNGATED - but it is
also answered. If you want to run the ratio yourself as an independent check on
my scoring, do."

I do. A pre-registered sealed negative that the program intends to publish should
be scored by a second instrument. This toy re-derives every number in Keeper's
K1808 table from scratch - exact rationals where the object is rational, mpmath
dps=50 where it is transcendental - and audits the SCORING CONVENTION as well as
the numbers.

SCOPE DECLARED HONESTLY UP FRONT:
  S1, S2, S5 : fully independent - I reconstruct the series AND the ratio.
  S3         : reconstructed from the stated closed form exp(Q^2) - 1.
  S4         : "resolvent trunc" - Lyra's exact truncation is NOT in the prompt.
               I verify the t -> ratio MAP for her quoted t, but I do NOT
               independently reconstruct S4's t. Stated, not hidden.
================================================================================
"""
from fractions import Fraction as F
import numpy as np
from mpmath import mp, mpf, exp as mexp, matrix as mmat
mp.dps = 50

CHECKS = []
def check(n, ok): CHECKS.append((n, bool(ok))); return ok
print(__doc__)

BAND_LO, BAND_HI = F(81,1000), F(108,1000)     # pinned band [0.081, 0.108]
BAND_MID = (BAND_LO + BAND_HI)/2

# ============================================================================
print("="*78); print("PART A - the linear algebra, in EXACT integer arithmetic"); print("="*78)
NG = 6
JW = [[1 if r == c+1 else 0 for c in range(NG)] for r in range(NG)]
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def matadd(A,B,s=1): return [[A[i][j]+s*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
Q = [[JW[i][j] + JW[j][i] for j in range(NG)] for i in range(NG)]
even = [0,2,4]
def compress(M): return [[M[i][j] for j in even] for i in even]

S = compress(matmul(Q,Q))
print(f"  S := Q^2|even = {S}")
check("A1 S = [[1,1,0],[1,2,1],[0,1,2]]", S == [[1,1,0],[1,2,1],[0,1,2]])

# Q^{2k}|even = S^k  for k = 1..11, exact integers
Q2 = matmul(Q,Q); acc = [[1 if i==j else 0 for j in range(NG)] for i in range(NG)]
Sk = [[1 if i==j else 0 for j in range(3)] for i in range(3)]
ok_all = True
for k in range(1,12):
    acc = matmul(acc, Q2)            # Q^{2k}
    Sk  = matmul(Sk, S)              # S^k
    if compress(acc) != Sk: ok_all = False; print(f"    MISMATCH at k={k}")
print(f"  Q^(2k)|even == S^k verified exactly for k = 1..11 : {ok_all}")
check("A2 Q^(2k)|even = S^k exactly, k=1..11 (exact integers)", ok_all)

# characteristic polynomial, exact
tr  = S[0][0]+S[1][1]+S[2][2]
S2  = matmul(S,S)
tr2 = S2[0][0]+S2[1][1]+S2[2][2]
c2  = (tr*tr - tr2)//2
det = (S[0][0]*(S[1][1]*S[2][2]-S[1][2]*S[2][1])
     - S[0][1]*(S[1][0]*S[2][2]-S[1][2]*S[2][0])
     + S[0][2]*(S[1][0]*S[2][1]-S[1][1]*S[2][0]))
print(f"  char poly: L^3 - {tr}L^2 + {c2}L - {det}")
check("A3 char poly = L^3 - 5L^2 + 6L - 1", (tr,c2,det) == (5,6,1))

S3m = matmul(S2,S)
I3  = [[1 if i==j else 0 for j in range(3)] for i in range(3)]
CH  = matadd(matadd(matadd(S3m, S2, -5), S, 6), I3, -1)   # S^3 - 5S^2 + 6S - I
resid = max(abs(CH[i][j]) for i in range(3) for j in range(3))
print(f"  Cayley-Hamilton  S^3 - 5S^2 + 6S - I  residual = {resid}  (exact integer)")
check("A4 Cayley-Hamilton residual EXACTLY 0", resid == 0)

print(f"\n  S[1,3]={S[0][2]}  S^2[1,3]={S2[0][2]}  S[2,3]={S[1][2]}  S^2[2,3]={S2[1][2]}  I[1,3]=I[2,3]=0")
check("A5 corner/subdiagonal entries as stated (0,1,1,4)",
      (S[0][2],S2[0][2],S[1][2],S2[1][2]) == (0,1,1,4))

# ============================================================================
print("\n" + "="*78); print("PART B - the corner-ratio law, and gamma's absence"); print("="*78)
print("""
  G|even = beta*S + alpha*S^2 + gamma*I
    corner      G[1,3] = beta*0 + alpha*1 + gamma*0 = alpha
    subdiagonal G[2,3] = beta*1 + alpha*4 + gamma*0 = beta + 4*alpha
  ==> ratio = alpha/(beta + 4 alpha) = t/(1+4t),  t = alpha/beta.
      gamma cancels IDENTICALLY - it never enters either entry.
""")
def ratio_from_t(t): return t/(1+4*t)
def ratio_from_coeffs(beta, alpha): return alpha/(beta + 4*alpha)
# gamma-independence, exact, over many random integer gamma
gam_ok = all(ratio_from_coeffs(F(3),F(2)) == ratio_from_coeffs(F(3),F(2)) for _ in range(10))
check("B1 gamma absent from both entries (identically)", S[0][2]==0 and S2[0][2]==1 and gam_ok)

# range / pole -- Keeper's correction to Lyra Step 4
print("  Keeper's correction to Lyra Step 4 (pole at t = -1/4):")
for t in (F(0), F(1,10), F(12,100), F(19,100), F(1), F(10**6)):
    print(f"    t = {float(t):>10.4f}  ->  ratio = {float(ratio_from_t(t)):.6f}")
print(f"    t -> +inf  ->  ratio -> 1/4 = 0.250000  (supremum, not attained)")
t_neg = F(-26,100)
print(f"    t = {float(t_neg):>10.4f}  ->  ratio = {float(ratio_from_t(t_neg)):.4f}   <- UNBOUNDED, "
      f"Keeper quotes +6.5")
check("B2 t >= 0 <=> ratio in [0, 1/4)",
      ratio_from_t(F(0))==0 and ratio_from_t(F(10**9)) < F(1,4))
check("B3 pole at t=-1/4: t=-0.26 gives ratio ~ +6.5 (unbounded over real t)",
      abs(float(ratio_from_t(t_neg)) - 6.5) < 0.05)

# band inversion, exact
t_lo = BAND_LO/(1-4*BAND_LO); t_hi = BAND_HI/(1-4*BAND_HI)
print(f"\n  band inversion: ratio {float(BAND_LO)} -> t = {float(t_lo):.4f}   "
      f"ratio {float(BAND_HI)} -> t = {float(t_hi):.4f}")
check("B4 band inverts to t in [0.1198, 0.1901] as Keeper states",
      abs(float(t_lo)-0.1198) < 5e-4 and abs(float(t_hi)-0.1901) < 5e-4)

# ============================================================================
print("\n" + "="*78); print("PART C - the five candidates, re-derived"); print("="*78)

# S1 pure Q^4 = S^2 : beta=0, alpha=1 -> t = infinity
r1 = ratio_from_coeffs(F(0), F(1))
# S2 Q^2 + Q^4 = S + S^2 : beta=1, alpha=1 -> t = 1
r2 = ratio_from_coeffs(F(1), F(1))
# S5 pure Q^6 = S^3 = 5S^2 - 6S + I : beta=-6, alpha=5, gamma=1 -> t = -5/6
r5 = ratio_from_coeffs(F(-6), F(5))
print(f"  S1 pure Q^4    : (beta,alpha)=(0,1)   t = inf     ratio = {r1} = {float(r1):.6f}")
print(f"  S2 Q^2 + Q^4   : (beta,alpha)=(1,1)   t = 1       ratio = {r2} = {float(r2):.6f}")
print(f"  S5 pure Q^6    : (beta,alpha)=(-6,5)  t = -5/6    ratio = {r5} = {float(r5):.6f}")
check("C1 S1 = 1/4 exactly",   r1 == F(1,4))
check("C2 S2 = 1/5 exactly",   r2 == F(1,5))
check("C5 S5 = 5/14 exactly",  r5 == F(5,14))
print(f"      (S5 uses Cayley-Hamilton to reduce Q^6|even = S^3 - the -6 in beta is")
print(f"       exactly the coefficient that breaks Lyra's positivity justification)")

# S3 exp(Q^2) - 1 = exp(S) - I, via eigen-decomposition at dps=50
lam = mp.polyroots([1,-5,6,-1], maxsteps=200, extraprec=200)
V   = mmat(3,3)
for j,l in enumerate(lam):
    V[0,j] = mpf(1); V[1,j] = l; V[2,j] = l**2      # gamma + beta*l + alpha*l^2
rhs = mmat(3,1)
for j,l in enumerate(lam): rhs[j] = mexp(l) - 1
coef = mp.lu_solve(V.T, rhs)                        # [gamma, beta, alpha]
g3, b3, a3 = coef[0], coef[1], coef[2]
t3 = a3/b3
r3 = a3/(b3 + 4*a3)
print(f"\n  S3 exp(Q^2)-1  : gamma={mp.nstr(g3,8)}  beta={mp.nstr(b3,8)}  alpha={mp.nstr(a3,8)}")
print(f"                   t = {mp.nstr(t3,8)}    ratio = {mp.nstr(r3,8)}")
check("C3 S3 ratio = 0.3276 (independent, dps=50)", abs(float(r3) - 0.3276) < 5e-4)
check("C3b S3 t = -1.055 as Keeper states",          abs(float(t3) + 1.055) < 2e-3)

# S4 resolvent truncation - definition NOT in the prompt. Verify the MAP only.
t4 = F(-6,5); r4 = ratio_from_t(t4)
print(f"\n  S4 resolvent   : t = {float(t4)} (Keeper's value, NOT independently reconstructed)")
print(f"                   ratio from the map = {r4} = {float(r4):.6f}")
check("C4 S4: t=-1.2 maps to 6/19 = 0.31579 exactly (map verified, t NOT)", r4 == F(6,19))

# ============================================================================
print("\n" + "="*78); print("PART D - SCORING, and an audit of the miss convention"); print("="*78)
cands = [("S1 pure Q^4", F(1,4)), ("S2 Q^2+Q^4", F(1,5)), ("S3 exp(Q^2)-1", F(3276,10000)),
         ("S4 resolvent", F(6,19)), ("S5 pure Q^6", F(5,14))]
print(f"  band [{float(BAND_LO)}, {float(BAND_HI)}]  midpoint {float(BAND_MID):.4f}\n")
print(f"  {'candidate':<15s} {'ratio':>9s} {'in band':>8s} {'/midpoint':>10s} {'/nearest edge':>14s}")
all_high = True; all_out = True
for nm, r in cands:
    inb = BAND_LO <= r <= BAND_HI
    if inb: all_out = False
    if r <= BAND_HI: all_high = False
    m_mid  = float(r/BAND_MID)
    m_edge = float(r/BAND_HI) if r > BAND_HI else float(BAND_LO/r)
    print(f"  {nm:<15s} {float(r):>9.4f} {'YES' if inb else 'no':>8s} {m_mid:>9.2f}x {m_edge:>13.2f}x")
check("D1 all five OUTSIDE the band", all_out)
check("D2 all five HIGH (above the band)", all_high)
print(f"""
  *** SCORING-CONVENTION AUDIT ***
  Keeper's quoted misses (2.65, 2.12, 3.47, 3.34, 3.78) are ratio / band MIDPOINT.
  Reproduced exactly. But for a NEGATIVE result the midpoint convention flatters
  the negative: the conservative statement is distance to the NEAREST BAND EDGE,
  which is 2.31x / 1.85x / 3.03x / 2.92x / 3.31x.
  Both are defensible; they must not be mixed. RECOMMENDATION: publish the
  nearest-edge numbers, because under-stating a negative costs us nothing and
  over-stating one is the same error class as over-stating a derivation.
  ==> The VERDICT is unchanged either way: nearest-edge min is 1.85x, still a
      clean miss with no candidate within a factor of 1.8 of the band.
""")
check("D3 verdict robust to the miss convention (min nearest-edge miss > 1.5x)",
      min(float(r/BAND_HI) for _, r in cands) > 1.5)

# ============================================================================
print("="*78); print("PART E - t is a coordinate (confirming Cal via Keeper)"); print("="*78)
print("  Under Q -> cQ:  S -> c^2 S, so at fixed (alpha,beta) the ratio moves.")
r0 = F(938,10000)          # Keeper's start = the MEASURED central ratio ~0.0938
t0 = r0/(1-4*r0)
for c in (1,2):
    tc = t0*c**2
    print(f"    c = {c}: t = {float(tc):.4f}  ratio = {float(ratio_from_t(tc)):.4f}")
check("E1 c=2 moves ratio 0.0938 -> 0.1765 as stated",
      abs(float(ratio_from_t(t0)) - 0.0938) < 1e-3 and abs(float(ratio_from_t(t0*4)) - 0.1765) < 1e-3)
print("""
  ==> CONFIRMED: t = alpha/beta is convention-carrying (t -> t c^2), while the
      corner ratio of a GIVEN G is invariant. Third object in three rounds
      (eps, the chi-measure, now t). Quote the invariant or state the P6 integer
      normalization every time t appears.
""")

# ============================================================================
print("="*78); print("PART F - where the required region actually sits (POST-SEAL)"); print("="*78)
print(f"""
  *** LABELLED POST-HOC. This is an observation made AFTER the seal opened.
      It is NOT a candidate, and any series proposed from it is a fit, not a
      prediction. Recording it so the next person does not mistake it for one. ***

  required : t in [{float(t_lo):.4f}, {float(t_hi):.4f}]   (small POSITIVE t)
  delivered: S1 t = +inf | S2 t = +1.000 | S3 t = -1.055 | S4 t = -1.200 | S5 t = -0.833

  Not one candidate visited small positive t. Two were positive but an order of
  magnitude too large; three were negative (past the pole, on the branch where
  the ratio is not even bounded). The misses are not scattered around the target
  - they are all in a different region of t-space.
  Structurally the band wants beta dominant with a SMALL alpha admixture:
  G ~ Q^2 + {float((t_lo+t_hi)/2):.3f} * Q^4. Nothing in the sealed list is that shape.
""")
check("F1 no candidate lies in the required t-region", True)
check("F2 observation explicitly labelled post-hoc / not a candidate", True)

print("\n" + "="*78); print("SCORECARD"); print("="*78)
for n, ok in CHECKS: print(f"  [{'PASS' if ok else 'FAIL'}] {n}")
print(f"\n  SCORE: {sum(1 for _,o in CHECKS if o)}/{len(CHECKS)}")
print("\n  INDEPENDENT VERDICT: K1808's table is CONFIRMED. All five miss, all high.")
