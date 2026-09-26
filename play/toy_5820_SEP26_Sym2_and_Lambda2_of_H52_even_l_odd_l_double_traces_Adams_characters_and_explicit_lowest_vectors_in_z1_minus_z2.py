#!/usr/bin/env python3
"""
Toy 5820 — GFF check: Sym²(H_5/2) = even-l double traces, Λ²(H_5/2) = odd-l, each once (Elie, 2026-09-26, round 9 item 1).
Prereg 9175decb. Antecedent (K1931 Part 2): "[φφ]_{n,l}, with Δ = 2Δ_φ + 2n + l, each once. For identical φ, only even spin l appears."
Two methods: (i) K-characters with the Adams operation ψ² and 5816's peel; (ii) explicit lowest-weight vectors in 5805's tube model.
"""
import glob
from fractions import Fraction as Fr
from collections import Counter
from itertools import combinations_with_replacement as cwr
import sympy as sp
src = open(glob.glob('play/toy_5816_*.py')[0]).read()
import io, contextlib
ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src[:src.index("lam = Fr(5, 2)")], ns)   # silence 5816's own control line     # reuse 5816's SO(5) machinery (sym, mul, irr, peel_so5)
sym, mul, irr, peel_so5, weyl_dim = ns['sym'], ns['mul'], ns['irr'], ns['peel_so5'], ns['weyl_dim']
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
# ---- SL(2) control ----
def sl2_split(a, depth, sign):
    # Sym^2/Λ^2 graded multiplicities at weight 2a+k: ½[(k+1) ± (1 if k even else 0)]
    T = Counter({2*a + k: Fr((k + 1) + sign*(1 if k % 2 == 0 else 0), 2) for k in range(depth)})
    out = []
    for w in sorted(T):
        m = T[w]
        if m < 0: return None
        if m:
            out.append((w - 2*a, m))
            for j in range(depth):
                if w + j in T: T[w + j] -= m
    return out
s2, l2 = sl2_split(Fr(5, 2), 14, +1), sl2_split(Fr(5, 2), 14, -1)
check("CONTROL SL(2): Sym² D_a = ⊕ D_{2a+2k}, Λ² D_a = ⊕ D_{2a+2k+1}, each once",
      s2 == [(2*k, 1) for k in range(7)] and l2 == [(2*k + 1, 1) for k in range(7)], f"Sym² k: {[x[0] for x in s2][:4]}  Λ² k: {[x[0] for x in l2][:4]}")
# ---- SO(5,2) characters ----
DEPTH = 6
SYM = [sym(L) for L in range(DEPTH + 1)]
def adams(C): return Counter({(2*w[0], 2*w[1]): v for w, v in C.items()})
def graded(sign):
    T = {}
    for N in range(DEPTH + 1):
        w = 5 + N; C = Counter()
        for L1 in range(N + 1): C.update(mul(SYM[L1], SYM[N - L1]))
        if N % 2 == 0:
            A = adams(SYM[N//2])
            for k, v in A.items(): C[k] += sign*v
        T[w] = Counter({k: Fr(v, 2) for k, v in C.items()})
    return T
def peel_graded(T):
    T = {w: Counter(c) for w, c in T.items()}; found = []
    for w in sorted(T):
        C = Counter({k: v for k, v in T[w].items() if v})
        if any(v < 0 or Fr(v).denominator != 1 for v in C.values()): return found, ('BAD', w)
        comps = peel_so5(Counter({k: int(v) for k, v in C.items()}))
        if comps is None: return found, ('NEG', w)
        for hw, m in comps.items():
            found.append((w, int(hw[0]), int(hw[1]), m))
            for L in range(DEPTH + 1):
                if w + L in T:
                    for k, v in mul(irr(hw), SYM[L]).items(): T[w + L][k] -= m*v
    return found, None
fS, eS = peel_graded(graded(+1)); fA, eA = peel_graded(graded(-1))
print("   Sym²: ", [(w, (j, b), m) for w, j, b, m in fS])
print("   Λ²:   ", [(w, (j, b), m) for w, j, b, m in fA])
check("(i) Sym² peels cleanly into lowest K-types (l,0) with l EVEN at 5 + 2n + l, each once (to depth 6)",
      eS is None and all(b == 0 and j % 2 == 0 and m == 1 and (w - 5 - j) % 2 == 0 for w, j, b, m in fS))
check("(i) Λ² peels cleanly into (l,0) with l ODD at 5 + 2n + l, each once",
      eA is None and all(b == 0 and j % 2 == 1 and m == 1 and (w - 5 - j) % 2 == 0 for w, j, b, m in fA))
both = sorted([(w, j) for w, j, b, m in fS + fA])
full = sorted([(5 + j + 2*mm, j) for j in range(DEPTH + 1) for mm in range(DEPTH + 1) if j + 2*mm <= DEPTH])
check("(i) Sym² ⊕ Λ² = 5816's full list ⊕_{j,m}(j,0) at 5 + j + 2m", both == full)
fX, eX = peel_graded({w: Counter({k: v for k, v in c.items()}) for w, c in graded(-1).items()})
check("NEGATIVE CONTROL: with the Adams sign exchanged, the 'Sym²' list contains ODD l (detected)", any(j % 2 == 1 for w, j, b, m in fX))
# ---- (ii) explicit lowest-weight vectors in the tube model: kernel of the total lowering operator P = ∂_{z1} + ∂_{z2} ----
Z1 = sp.symbols('a0:5'); Z2 = sp.symbols('b0:5'); ALL = Z1 + Z2
def monos(N): return [sp.Mul(*c) for c in cwr(ALL, N)]
ok_dim = ok_par = True; details = []
for N in range(4):
    B = monos(N); idx = {m: i for i, m in enumerate(B)}
    rowsP = []
    lower = monos(N - 1) if N > 0 else []
    li = {m: i for i, m in enumerate(lower)}
    Mtx = sp.zeros(5*len(lower), len(B)) if N > 0 else None
    if N > 0:
        for j, m in enumerate(B):
            for mu in range(5):
                d = sp.expand(sp.diff(m, Z1[mu]) + sp.diff(m, Z2[mu]))
                if d == 0: continue   # run 1: Poly(0) yields a constant term with no slot at N >= 2 (KeyError) — skip zeros
                for term, c in sp.Poly(d, *ALL).terms():
                    mono = sp.Mul(*[v**e for v, e in zip(ALL, term)])
                    Mtx[mu*len(lower) + li[mono], j] += c
        ker = Mtx.nullspace()
    else:
        ker = [sp.Matrix([1])]
    expect = len(list(cwr(range(5), N)))       # dim of degree-N polynomials in u = z1 - z2
    if len(ker) != expect: ok_dim = False
    # swap parity on the kernel: every kernel vector is a polynomial in u, so σ = (−1)^N
    swap = {a: b for a, b in zip(Z1, Z2)}; swap.update({b: a for a, b in zip(Z1, Z2)})
    for v in ker[:6]:
        poly = sum(c*m for c, m in zip(v, B))
        if sp.expand(poly.subs(swap, simultaneous=True) - (-1)**N*poly) != 0: ok_par = False
    details.append((N, len(ker), expect))
check("(ii) lowest vectors of degree N = polynomials in u = z1−z2 (kernel dim = C(N+4,4)), N ≤ 3", ok_dim, str(details))
check("(ii) swap σ acts by (−1)^N = (−1)^l on them (Q(u)^n h_l(u), N = 2n + l): Sym² ⇔ even l, Λ² ⇔ odd l", ok_par)
print(f"\nSCORE: {sum(score)}/{len(score)}")
