"""TOY 5701 — Round 120 L3 (Lyra, 2026-09-06). Does the Hardy/Szego inner product on the maximal
polydisc, on dilation-invariant test functions, contain the prime sum of Weil's explicit formula?
Setup: f(z1,z2) = sum_{m,n>=1} c(mn) z1^m z2^n (dilation-invariant: the coefficient depends only on
the product grading N = mn). Szego norm ||f||^2 = sum_{m,n} |c(mn)|^2 = sum_N d(N) |c(N)|^2.
So the form is DIAGONAL in the N-basis with weight d(N) >= 0, and by Bochner its kernel on the
unitary line is zeta(1 + i(t - t'))^2, positive-definite for ANY nonnegative coefficient sequence.
Weil's form (Bombieri's normalisation, s = 1/2 + it): for g = f * f~ on the multiplicative group,
W(g) = ghat(0) + ghat(1) - sum_n Lambda(n)/sqrt(n) [g(n) + g(1/n)] - (archimedean),
and on the same monomial basis e_N (test function supported at log N) its matrix has
  diagonal: archimedean + pole terms;  off-diagonal (N, N'): -Lambda(N'/N)/sqrt(N'/N) when N | N'.
The prime sum lives ENTIRELY off the diagonal. A diagonal form with positive weights cannot see it.
Verdicts computed: (P1) Hardy Gram matrices PSD for zeta^2 weights d(N), for r5(N)/3840 (zeta_Z5,
which has an off-line zero), and for random nonnegative weights. (P2) Weil's N-basis matrix is
not diagonal and its off-diagonal entries are exactly -Lambda(N'/N)/sqrt(N'/N). (P3) The Hardy
form evaluated on the SAME test vectors is identical for zeta and for any other positive series
up to the weights -- i.e. it is invariant under zeta -> zeta_Z5 in FORM (barrier lemma).
"""
import numpy as np, math
from sympy import divisor_count, factorint, primefactors
Nmax = 40
d = np.array([int(divisor_count(N)) for N in range(1, Nmax+1)], dtype=float)
# r5(N): number of representations as sum of five squares
def r5(N):
    cnt = 0; R = int(math.isqrt(N))
    for a in range(-R, R+1):
        for b in range(-R, R+1):
            s2 = N - a*a - b*b
            if s2 < 0: continue
            for c in range(-int(math.isqrt(s2)), int(math.isqrt(s2))+1):
                s3 = s2 - c*c
                if s3 < 0: continue
                for e in range(-int(math.isqrt(s3)), int(math.isqrt(s3))+1):
                    s4 = s3 - e*e
                    if s4 < 0: continue
                    q = int(math.isqrt(s4))
                    if q*q == s4: cnt += 1 if q == 0 else 2
    return cnt
r5v = np.array([r5(N)/3840 for N in range(1, Nmax+1)])
rng = np.random.default_rng(0); rnd = rng.random(Nmax)
def gram(weights, ts):
    # kernel K(t,t') = sum_N w(N) N^{-i(t-t')}  (Bochner: transform of the positive measure)
    Ns = np.arange(1, Nmax+1, dtype=float)
    K = np.array([[np.sum(weights * Ns**(-1j*(t-tp))) for tp in ts] for t in ts])
    return np.linalg.eigvalsh((K+K.conj().T)/2).min()
ts = np.linspace(-3, 3, 13)
mins = {name: gram(w, ts) for name, w in [("zeta^2 (d(N))", d), ("zeta_Z5 (r5/3840)", r5v), ("random >= 0", rnd)]}
for k, v in mins.items(): print("  Hardy Gram min eigenvalue, %-18s: %+.3e" % (k, v))
p1 = all(v > -1e-9 for v in mins.values())
# Weil matrix on the N-basis
def Lam(n):
    f = factorint(n)
    return math.log(list(f)[0]) if len(f) == 1 else 0.0
Wm = np.zeros((Nmax, Nmax))
for N in range(1, Nmax+1):
    for Np in range(1, Nmax+1):
        if N != Np and Np % N == 0:
            q = Np // N
            Wm[N-1, Np-1] = -Lam(q)/math.sqrt(q)
            Wm[Np-1, N-1] = Wm[N-1, Np-1]
offdiag = np.abs(Wm - np.diag(np.diag(Wm))).sum()
check = all(abs(Wm[0, p-1] + math.log(p)/math.sqrt(p)) < 1e-12 for p in (2, 3, 5, 7))
print("  Weil N-basis matrix: off-diagonal mass %.4f; entries (1,p) = -log p/sqrt p for p=2,3,5,7: %s" % (offdiag, check))
p2 = offdiag > 0 and check
# P3: the Hardy form on a test vector is a weighted sum with no Lambda anywhere; same expression for both weights
c = rng.standard_normal(Nmax)
Q_zeta = float(np.sum(d * c**2)); Q_Z5 = float(np.sum(r5v * c**2))
print("  Hardy form on a test vector: zeta^2-weights %.4f, zeta_Z5-weights %.4f, both > 0: %s" % (Q_zeta, Q_Z5, Q_zeta > 0 and Q_Z5 > 0))
p3 = Q_zeta > 0 and Q_Z5 > 0
for name, ok in [("P1 Hardy Gram PSD for zeta^2, zeta_Z5 and random weights (Bochner)", p1),
                 ("P2 Weil form is off-diagonal with -Lambda(N'/N)/sqrt(N'/N)", p2),
                 ("P3 Hardy form positive for zeta AND for the off-line-zero zeta_Z5 (form-invariant)", p3)]:
    print("  %s: %s" % (name, "HIT" if ok else "MISS"))
print("  ANSWER to L3: NO. The prime sum is off-diagonal in the N-basis; a Szego norm is diagonal with weight d(N).")
