#!/usr/bin/env python3
"""
Toy 5798 — atomic shells as K-types, STRUCTURE ONLY (Casey 09-25 19:42: energies are 3D dynamics, not claimed).
Different from K1878 (STOP): no Hamiltonian, no 1/n^2 — representation content only. Prereg f3f09274.
Machinery: exact torus characters. SO(4) = SU(2)xSU(2) weights in doubled coordinates (2mL, 2mR);
SO(2) (the J / D_IV circle) weight as Fraction. Scalar holomorphic module of D_IV^n at parameter nu (Schmid):
   K-types P_lam (lam1 >= lam2 >= 0), SO(n)-type = harmonic H_{lam1-lam2}(C^n), SO(2)-weight nu + lam1 + lam2;
   continuous part nu > (n-2)/2: all lam;  Wallach point nu = (n-2)/2: lam2 = 0 only;  nu = 0: trivial.
   (the Schmid rule is INPUT, not tested here; everything else is computed)
Items: (a) H_m(R^4) = (m/2,m/2), dim (m+1)^2 by peeling characters;
       (b) D_IV^4 at nu=1 (the SO(4,2) ladder = hydrogen's representation): one shell per level, SO(2) weight = n;
       (c) H^2(D_IV^5) (Hardy, nu=5/2) restricted to SO(4)xSO(2) (D_IV^4 ⊂ D_IV^5 shares J) and PEELED into
           scalar D_IV^4 modules -> expect (+)_k H_{5/2+k}; KILL: an SO(4)-trivial K'-type at weight 1;
       (d) EXTRA (not in prereg, flagged): D_IV^5 at its Wallach point nu=3/2 restricted, same peeling;
       (e) CONTROL n = 4..8: SO(n) harmonics -> SO(4) contain every shell; D_IV^n Hardy/Wallach restricted to
           D_IV^(n-1) never contain the (n-1) ladder.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr
from collections import Counter
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

def vec_weights(n):
    """weights of C^n under the maximal torus of SO(n), as tuples of length r = n//2"""
    r = n // 2; W = []
    for i in range(r):
        for s in (1, -1):
            w = [0]*r; w[i] = s; W.append(tuple(w))
    if n % 2: W.append(tuple([0]*r))
    return W
def sym_char(n, m):
    C = Counter()
    for combo in cwr(range(n), m):
        W = vec_weights(n)
        C[tuple(sum(W[k][i] for k in combo) for i in range(n//2))] += 1
    return C
def harm_char(n, m):
    C = sym_char(n, m)
    if m >= 2: C.subtract(sym_char(n, m-2))
    return +C
def restrict_to_so4(C, n):
    """SO(n) torus weight -> SO(4) torus weight: keep first two coordinates (C^n = C^4 ⊕ C^(n-4)) and convert to (2mL,2mR)"""
    out = Counter()
    for w, k in C.items():
        a, b = w[0], w[1]
        out[(a+b, a-b)] += k
    return out
def so4_char_irrep(jL2, jR2):
    return Counter({(x, y): 1 for x in range(-jL2, jL2+1, 2) for y in range(-jR2, jR2+1, 2)})
def peel_so4(C):
    C = Counter(C); out = []
    while +C:
        if any(v < 0 for v in C.values()): return None
        hw = max((w for w, v in C.items() if v > 0), key=lambda w: (w[0]+w[1], w[0]))
        out.append(hw); C.subtract(so4_char_irrep(*hw)); C = Counter({k: v for k, v in C.items() if v != 0})
    return sorted(out)

# (a) H_m(R^4) irreducible (m/2, m/2), dim (m+1)^2
ok = True
for m in range(9):
    p = peel_so4(restrict_to_so4(harm_char(4, m), 4))
    if p != [(m, m)] or sum(harm_char(4, m).values()) != (m+1)**2: ok = False
check("(a) H_m(R^4) = (m/2, m/2) irreducible, dim (m+1)^2 = n^2 for n = 1..9 (Fock's shells as SO(4) harmonics)", ok)

# graded K'-characters on the FULL SO(n_sub) torus (run 1 peeled every n with D_IV^4 characters — bug, fixed)
MAXW = 8
def restrict_n_to_nm1(C, n):
    """SO(n) torus -> SO(n-1) torus for C^n = C^(n-1) ⊕ C: n odd keeps all coords; n even drops the last"""
    if n % 2: return Counter(C)
    out = Counter()
    for w, k in C.items(): out[w[:-1]] += k
    return out
def module_char_full(n, nu, levels, kind, restrict=False):
    G = {}
    for L in range(levels+1):
        C = Counter()
        for l2 in range(0, L//2 + 1):
            if kind == 'wallach' and l2 > 0: continue
            h = harm_char(n, L - 2*l2)
            C.update(restrict_n_to_nm1(h, n) if restrict else h)
        G[F(nu) + L] = +C
    return G
def peel_modules(G, n_sub, levels):
    G = {w: Counter(c) for w, c in G.items()}; found = []
    top = min(G) + levels; zero = tuple([0]*(n_sub//2))
    while True:
        ws = [w for w in sorted(G) if +G[w]]
        if not ws: return found
        w = ws[0]; c = +G[w]
        if any(v < 0 for v in G[w].values()) or set(c) != {zero}:
            return found + [('STUCK', w)]          # lowest remaining type is not SO(n_sub)-trivial
        wall = F(n_sub - 2, 2)
        if w < wall: return found + [('NONUNITARY', w)]
        kind = 'wallach' if w == wall else 'cont'
        M = module_char_full(n_sub, w, int(top - w), kind)
        for _ in range(c[zero]):
            for ww, cc in M.items():
                if ww in G: G[ww].subtract(cc)
            found.append((w, kind))
def module_char(n, nu, levels, kind):   # SO(4)-restricted, used for the shell read-outs
    G = module_char_full(n, nu, levels, kind)
    return {w: restrict_to_so4(c, n) for w, c in G.items()}

# (b) D_IV^4 at nu = 1 (Wallach): hydrogen's ladder
Lad = module_char(4, 1, MAXW, 'wallach')
ok = all(peel_so4(Lad[F(1)+m]) == [(m, m)] for m in range(MAXW+1))
check("(b) D_IV^4 at ν=1 (Wallach point = SO(4,2) ladder): K'-types = ONE shell per level, SO(2) weight = n, dim n^2", ok,
      " ".join(f"n={1+m}:{sum(Lad[F(1)+m].values())}" for m in range(6)))
spin = [2*(n*n) for n in range(1, 5)]
print(f"   with a doubling (spin) input — NOT supplied by this module: 2n^2 = {spin} (row lengths); cumulative n^2 = 1,5,14,30,55 = dim H_m(R^5)")
check("(b') dim H_m(R^5) = Σ_{n≤m+1} n^2 (SO(5) harmonics restrict to shells 1..m+1, each once)",
      all(sum(harm_char(5, m).values()) == sum(k*k for k in range(1, m+2)) and
          peel_so4(restrict_to_so4(harm_char(5, m), 5)) == sorted([(l, l) for l in range(m+1)]) for m in range(8)))

# (c) H^2(D_IV^5) at the Hardy point nu = 5/2, restricted and peeled
H2 = module_char(5, F(5, 2), MAXW, 'cont')
pe = peel_modules(module_char_full(5, F(5, 2), MAXW, 'cont', restrict=True), 4, MAXW)
print(f"   H^2(D_IV^5)|SO(4,2) peeled: {[(str(w), k) if not isinstance(w, str) else w for w, *k in pe][:12]}")
check("(c) H^2(D_IV^5) restricted = ⊕_k H_{5/2+k}(D_IV^4), each once (to the computed depth)",
      [w for w, k in pe] == [F(5, 2) + k for k in range(MAXW+1)] and all(k == 'cont' for w, k in pe))
lad_hit = any(w == 1 for w, *_ in pe) or any(G for ww, G in H2.items() if ww == 1)
check("(c) KILL FIRES: no SO(4)-trivial K'-type at weight 1 — hydrogen's ladder is NOT a summand of H^2(D_IV^5)|SO(4,2)",
      not lad_hit and all(w.denominator == 2 for w in H2))
for w in sorted(H2)[:5]:
    print(f"   weight {str(w):>5}: shells present (n, mult) = {sorted(Counter(a//2+1 for a, b in peel_so4(H2[w])).items())}")

# (d) EXTRA: D_IV^5 Wallach point nu = 3/2
Wm = module_char(5, F(3, 2), MAXW, 'wallach')
pw = peel_modules(module_char_full(5, F(3, 2), MAXW, 'wallach', restrict=True), 4, MAXW)
print(f"   [extra, not prereg] D_IV^5 at ν=3/2 restricted peeled: {[(str(w), k) for w, k in pw]}")
check("(d) [extra] D_IV^5 Wallach module restricted = H_{3/2} ⊕ H_{5/2} of D_IV^4 — no ladder (ν'=1) either",
      [w for w, k in pw] == [F(3, 2), F(5, 2)])

# (e) CONTROL n = 4..8
ok_shells = all(peel_so4(restrict_to_so4(harm_char(n, 3), n)) is not None and
                (3, 3) in peel_so4(restrict_to_so4(harm_char(n, 3), n)) for n in range(4, 9))
check("(e) CONTROL: SO(n) harmonics of degree 3 contain the n=4 shell (3/2,3/2) for every n = 4..8 — shells are not a selection of 5", ok_shells)
ctrl = []
for n in range(5, 9):
    lad = F(n - 3, 2)
    hard = peel_modules(module_char_full(n, F(n, 2), 5, 'cont', restrict=True), n - 1, 5)
    wal = peel_modules(module_char_full(n, F(n - 2, 2), 5, 'wallach', restrict=True), n - 1, 5)
    ctrl.append((n, [str(w) for w, _ in hard][:3], [str(w) for w, _ in wal], all(w != lad for w, _ in hard + wal), all(not isinstance(w,str) for w,_ in hard+wal)))
for c in ctrl: print(f"   D_IV^{c[0]} -> D_IV^{c[0]-1}: Hardy -> {c[1]}..., Wallach -> {c[2]}; (n-1)-ladder ν'={F(c[0]-3,2)} absent: {c[3]}; clean peel: {c[4]}")
check("(e) CONTROL: for n = 5..8 neither the Hardy nor the Wallach module of D_IV^n restricted contains the D_IV^(n-1) ladder",
      all(c[3] and c[4] for c in ctrl))
print("\nREADING (structure only): the n^2 shells are the SO(4)-harmonics; they sit inside every D_IV^n K-type for n >= 4")
print("(recapitulation, not selection). Hydrogen's REPRESENTATION (the ladder, one shell per level) is the Wallach point of")
print("D_IV^4 and is not a summand of H^2(D_IV^5) restricted to SO(4,2), nor of D_IV^5's Wallach module: scalar holomorphic")
print("restriction raises ν' by ≥ 1/2 above the ladder. Not tested: vector-valued modules of SO(5,2), non-holomorphic series.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
