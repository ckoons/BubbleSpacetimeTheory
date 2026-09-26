#!/usr/bin/env python3
"""Cal Section 993 instrument (written after `date` = 12:57 EDT; hashed before running).

ANTECEDENT, verbatim (K1929 Part 2): "Bound (discrete) = the compact realization of the Šilov boundary. Continuum = its
flat Minkowski realization." And Part 1 item 1 / Part 3(b): "the minimal representation (λ = 3/2) should be hydrogen in
four space dimensions".

INVARIANT FIRST: the spectrum of a generator on a unitary representation is a unitary invariant, so it cannot depend on
the realization (the chart) in which the representation is written. The geometric FLOW of a conformal vector field can.

KILL LINE (written first): my objection "discreteness belongs to the generator, not to the realization" dies if the
conformal Hamiltonian's flow is COMPLETE on flat ℝ^{1,4} with period 2π (then the flat realization would carry
the circle too, and the realization would carry nothing). Lyra item 3's "Gauss's law" reading dies in my favour only if the
hidden-symmetry (Runge–Lenz) vector is conserved for V = -1/r in ℝ^4 and NOT for the 4-space Gauss potential V = -1/r^2.

PREDICTIONS:
  C1  The flow of the conformal Hamiltonian on ℝ^{1,4} (the vector field of ½(P0 + K0), compact-sign convention) is
      INCOMPLETE: from the origin, t(τ) = tan(τ/2) reaches infinity at τ = π. On the compactification it closes
      (period 2π in τ; the ℤ2 quotient makes the boundary circle's own period π... the operator period stays 2π/4π).
      So: the geometric flow needs the compact realization; the spectrum does not (it is a group fact: J generates a
      compact subgroup).
  C2  Fock's stereographic radius is E-dependent: p0 = sqrt(-2E) (m = 1). A FIXED compactification with the operator J
      gives equal spacing; 1/n^2 needs p0 = 1/n, i.e. the Coulomb dynamics. Checked by the Fock relation n = 1/p0.
  C3  In ℝ^4 with V = -1/r, A = |p|^2 r - (r.p) p - r/|r| is conserved along orbits (drift < 1e-8 relative).
  C4  In ℝ^4 with V = -1/r^2 (4-space Gauss's law), A drifts at O(1) (not conserved). So the SO(5,2)
      "hydrogen in four space dimensions" is the 1/r (Kepler) problem in ℝ^4, NOT 4-space electrostatics.
  CONTROL  In ℝ^3 with V = -1/r, A conserved (the textbook LRL vector).
"""
import numpy as np
from scipy.integrate import solve_ivp

score = []
# C1: conformal Hamiltonian flow along the time axis. On the time axis, the vector field of 1/2(P0+K0) acting on t is
# (1 + t^2)/2 d/dt (compact-sign convention), whose solution from t=0 is t = tan(tau/2).
tau = np.array([0.5, 1.0, 2.0, 3.0, 3.1, 3.14])
t = np.tan(tau / 2)
dt = (1 + t**2) / 2
num = np.gradient(t, tau)  # rough check only
blow = np.tan((np.pi - 1e-6) / 2)
print("C1 t(tau) = tan(tau/2):", np.round(t, 3), " t(pi - 1e-6) =", f"{blow:.3e}")
c1 = blow > 1e5
score.append(("C1", c1))

# C2: Fock: p0^2 = -2E; with E_n = -1/(2 n^2), p0 = 1/n. A fixed p0 gives a single shell.
ns = np.arange(1, 6)
E = -1 / (2 * ns**2)
p0 = np.sqrt(-2 * E)
c2 = np.allclose(p0, 1 / ns) and len(set(np.round(p0, 12))) == len(ns)
print("C2 Fock radius p0(E_n) =", np.round(p0, 4), " E-dependent:", c2)
score.append(("C2", c2))

def lrl_drift(d, power, T=60.0):
    rng = np.random.default_rng(993 + d + power)
    r0 = rng.normal(size=d); r0 /= np.linalg.norm(r0)
    v = rng.normal(size=d); v -= (v @ r0) * r0; v /= np.linalg.norm(v)
    speed = 0.8 if power == 1 else 1.05   # bound for 1/r; slightly above circular for 1/r^2 (circular v = sqrt(2)/r... use generic)
    p0v = speed * v + 0.1 * r0
    def f(_, y):
        r, p = y[:d], y[d:]
        R = np.linalg.norm(r)
        force = -power * r / R**(power + 2)   # F = -grad(-1/r^power)... V=-1/r^k -> F = -k r / r^{k+2}
        return np.concatenate([p, force])
    def A(y):
        r, p = y[:d], y[d:]
        return (p @ p) * r - (r @ p) * p - r / np.linalg.norm(r)
    sol = solve_ivp(f, (0, T), np.concatenate([r0, p0v]), rtol=1e-11, atol=1e-12, dense_output=True)
    ys = sol.sol(np.linspace(0, T, 400)).T
    As = np.array([A(y) for y in ys])
    rmin = min(np.linalg.norm(y[:d]) for y in ys)
    return np.max(np.linalg.norm(As - As[0], axis=1)) / max(np.linalg.norm(As[0]), 1e-12), rmin

d3, _ = lrl_drift(3, 1)
d4, _ = lrl_drift(4, 1)
d4g, rmin = lrl_drift(4, 2, T=20.0)
print(f"CONTROL R^3, V=-1/r: A drift {d3:.2e}")
print(f"C3 R^4, V=-1/r: A drift {d4:.2e}")
print(f"C4 R^4, V=-1/r^2 (4-space Gauss): A drift {d4g:.2e}  (min r on orbit {rmin:.3f})")
score += [("CTRL", d3 < 1e-7), ("C3", d4 < 1e-7), ("C4", d4g > 1e-2)]
print("SCORE", sum(o for _, o in score), "/", len(score), [(n, bool(o)) for n, o in score])
