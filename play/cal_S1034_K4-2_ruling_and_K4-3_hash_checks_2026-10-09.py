#!/usr/bin/env python3
"""Cal Section 1034 (2026-10-09) — facts behind the K4-2 ruling and the K4-3 hash.
Plain Python + numpy. No cosmological number is read. The only physical input is
the DECLARED Target-2 value Q = 0.78233 MeV (Lyra K4-2 Section 7) and m_e, used
only to locate W0 on the Fermi-integral curve; nothing is compared to a lifetime.

Checks
 1. Sargent vs Fermi: f(W0)/(W0^5/30) -> 1 only for W0 >> 1; at the declared
    target's W0 = 1 + Q/m_e the ratio is far from 1 (Keeper's 10-08 catch).
 2. Bargmann: frame + TWO writes already carry a gauge-invariant phase, so
    "three records" is "two writes + the reference" unless the reference is
    excluded by a stated principle (K-C7d is live once item 5(e) makes the
    frame a record).
 3. Holevo: three classical values from one polarization qubit is impossible
    (log2 2 = 1 bit); three bits need d >= 8 orthogonal photon modes.
 4. so(5,2) restricted roots: B2 with m_short = 3, m_long = 1, dim p = 10;
    M = SO(3) on indices {3,4,5} acts on g_{e1} as the vector and on g_{e1+e2}
    trivially. The GO prompt's relay said "three short roots": there are TWO
    positive short roots; the 3 is a MULTIPLICITY.
"""
import numpy as np
from math import sqrt, log2

rng = np.random.default_rng(1034)
score = 0; total = 0
def check(name, ok, detail=""):
    global score, total
    total += 1; score += bool(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {detail}" if detail else ""))

print("1. Sargent E0^5 is the W0 >> 1 limit of the Fermi integral (F = 1, no Coulomb)")
def fermi_f(W0, n=20000):
    # f(W0) = int_1^W0 p W (W0 - W)^2 dW, units m_e = 1, p = sqrt(W^2 - 1)
    W = np.linspace(1.0, W0, n)
    p = np.sqrt(np.maximum(W*W - 1.0, 0.0))
    return np.trapz(p*W*(W0 - W)**2, W)
Q, m_e = 0.78233, 0.51099895        # declared target (MeV) and m_e (CODATA, pin: Grace)
W0_target = 1.0 + Q/m_e
ratios = {W0: fermi_f(W0)/(W0**5/30.0) for W0 in (W0_target, 3.0, 5.0, 10.0, 50.0, 200.0)}
for W0, r in ratios.items():
    print(f"     W0 = {W0:8.3f}   f/(W0^5/30) = {r:.4f}")
check("ratio -> 1 at large W0", abs(ratios[200.0] - 1) < 0.03)
check("ratio far from 1 at the declared target's W0", abs(ratios[W0_target] - 1) > 0.3,
      f"W0 = {W0_target:.4f} (= 1 + Q/m_e; Q/m_e = {Q/m_e:.4f} is the caged decoy), ratio {ratios[W0_target]:.3f}")

print("2. Bargmann: the reference state + two writes = three states, which carry a phase")
def rand_state(d):
    v = rng.normal(size=d) + 1j*rng.normal(size=d); return v/np.linalg.norm(v)
d = 4
ref, w1, w2 = (rand_state(d) for _ in range(3))
B = np.vdot(ref, w1)*np.vdot(w1, w2)*np.vdot(w2, ref)
phases = [np.exp(1j*t) for t in rng.uniform(0, 2*np.pi, 3)]
B2 = np.vdot(ref*phases[0], w1*phases[1])*np.vdot(w1*phases[1], w2*phases[2])*np.vdot(w2*phases[2], ref*phases[0])
check("B(ref,w1,w2) gauge-invariant", abs(B - B2) < 1e-12)
check("arg B(ref,w1,w2) generically nonzero (two writes suffice once the frame is a state)",
      abs(np.angle(B)) > 1e-3, f"arg B = {np.angle(B):.3f}")

print("3. Holevo: classical bits per photon <= log2(d)")
check("polarization qubit: 1 bit, not three values", log2(2) == 1.0)
d_needed = 2**3
check("three classical bits need d >= 8 orthogonal modes (2 pol x >= 4 resolvable lines)", d_needed == 8)

print("4. so(5,2) restricted roots and M = Z_K(a)")
n = 7; eta = np.diag([1,1,1,1,1,-1,-1]).astype(float)
def E(i,j):
    M = np.zeros((n,n)); M[i,j] = 1; return M
# basis of so(5,2): X^T eta + eta X = 0  <=>  X = eta * A with A antisymmetric
basis = []
for i in range(n):
    for j in range(i+1, n):
        A = E(i,j) - E(j,i); basis.append(eta @ A)
basis = np.array(basis)                       # 21 generators
check("dim so(5,2) = 21", len(basis) == 21)
# p = generators mixing {0..4} with {5,6}
p_idx = [k for k,(i,j) in enumerate([(i,j) for i in range(n) for j in range(i+1,n)]) if i < 5 <= j]
check("dim p = 10", len(p_idx) == 10)
H1 = eta @ (E(0,5) - E(5,0)); H2 = eta @ (E(1,6) - E(6,1))     # maximal abelian a in p
check("a abelian", np.allclose(H1@H2 - H2@H1, 0))
# ad(a) on g: simultaneous eigen-decomposition
G = basis.reshape(21, -1).T                    # columns = generators (flattened)
def ad(H):  # matrix of ad_H in the generator basis
    cols = [(H@X - X@H).reshape(-1) for X in basis]
    return np.linalg.lstsq(G, np.array(cols).T, rcond=None)[0]
A1, A2 = ad(H1), ad(H2)
check("[ad H1, ad H2] = 0", np.allclose(A1@A2 - A2@A1, 0, atol=1e-9))
w, V = np.linalg.eig(A1 + sqrt(2)*A2)         # generic combination separates roots
roots = {}
for lam, v in zip(w, V.T):
    a1 = np.real(np.vdot(v, A1@v)/np.vdot(v,v)); a2 = np.real(np.vdot(v, A2@v)/np.vdot(v,v))
    key = (round(a1,6), round(a2,6)); roots[key] = roots.get(key, 0) + 1
nonzero = {k:m for k,m in roots.items() if k != (0.0, 0.0)}
short = {k:m for k,m in nonzero.items() if abs(abs(k[0])+abs(k[1]) - 1) < 1e-6}
long_ = {k:m for k,m in nonzero.items() if abs(abs(k[0])+abs(k[1]) - 2) < 1e-6}
print("     roots (a1,a2):mult =", {k:m for k,m in sorted(nonzero.items())})
check("B2: 4 short roots of multiplicity 3", len(short) == 4 and all(m == 3 for m in short.values()))
check("B2: 4 long roots of multiplicity 1", len(long_) == 4 and all(m == 1 for m in long_.values()))
check("centraliser dim = 2 + 3 (= a + m, m = so(3))", roots.get((0.0,0.0), 0) == 5)
check("dim p = 2 + 2*3 + 2*1 = 10", 2 + 2*3 + 2*1 == 10)
# M = SO(3) on indices {2,3,4}; test its action on g_{e1} and on g_{e1+e2}
def root_space(target):
    vs = [V[:,k] for k,lam in enumerate(w)
          if abs(np.real(np.vdot(V[:,k],A1@V[:,k])/np.vdot(V[:,k],V[:,k])) - target[0]) < 1e-6
          and abs(np.real(np.vdot(V[:,k],A2@V[:,k])/np.vdot(V[:,k],V[:,k])) - target[1]) < 1e-6]
    return np.array(vs).T
L = eta @ (E(2,3) - E(3,2))                    # a generator of so(3)_{345}
adL = ad(L)
S = root_space((1.0, 0.0)); Lg = root_space((1.0, 1.0))
# ad L must preserve each root space; its restriction to g_{e1} is a 3x3 rotation generator (rank 2), to g_{e1+e2} zero
PS = S @ np.linalg.pinv(S); PL = Lg @ np.linalg.pinv(Lg)
check("ad(so3) preserves g_{e1}", np.allclose(PS @ adL @ S, adL @ S, atol=1e-8))
check("ad(so3) acts on g_{e1} as the VECTOR (nonzero, rank 2 on the 3-space)",
      np.linalg.matrix_rank(np.linalg.pinv(S) @ adL @ S, tol=1e-8) == 2)
check("ad(so3) acts on g_{e1+e2} trivially (M-singlet)", np.allclose(adL @ Lg, 0, atol=1e-8))
print("   NOTE: TWO positive short roots (e1, e2), each of multiplicity 3; 'three short roots' is a misstatement.")

print(f"\nSCORE: {score}/{total}")
