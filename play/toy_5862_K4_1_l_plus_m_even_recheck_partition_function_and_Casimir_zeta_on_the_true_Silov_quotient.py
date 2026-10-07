#!/usr/bin/env python3
"""
Toy 5862 — Round K4-1 item 4 (K1950 Section 11(d)), Elie 2026-10-07. Prereg: notes/Elie_K4-1_prereg_toy_5862_* (bdd49d23).

On the true Silov boundary (S^4 x S^1)/Z2, deck (x, th) -> (-x, th + pi), a mode Y_l(x) e^{i m th} survives
iff (-1)^(l+m) = +1. Recheck the Guide's two spectral computations, importing the original code unchanged:
  Vol3 Ch03 May 15.0  notes/bst_partition_function_extended.py
  Vol2 Ch02 May 5.3   notes/bst_casimir_seeley_dewitt.py
The cover (both parities) is the control.
"""
import importlib.util, os
import numpy as np
if not hasattr(np, "trapz"): np.trapz = np.trapezoid

HERE = os.path.dirname(os.path.abspath(__file__)); NOTES = os.path.join(HERE, "..", "notes")
def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(NOTES, name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
PF = load("bst_partition_function_extended"); CZ = load("bst_casimir_seeley_dewitt")

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append((tag, bool(ok))); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

# --------------------------------------------------------------- partition function
def lnZ(beta, l_max, m_max, quotient, N_max=137):
    d_l, E = PF.build_energy_grid(l_max, m_max)
    lnZm = PF.ln_Z_mode_array(beta * E, N_max)
    if quotient:
        l = np.arange(l_max + 1)[:, None]; m = np.arange(-m_max, m_max + 1)[None, :]
        lnZm = np.where((l + m) % 2 == 0, lnZm, 0.0)
    return float(np.sum(d_l[:, None] * lnZm))
def thermo(beta, l_max, m_max, q):
    h = max(beta * 0.005, 1e-5)
    a, b, c = lnZ(beta, l_max, m_max, q), lnZ(beta + h, l_max, m_max, q), lnZ(beta - h, l_max, m_max, q)
    return dict(lnZ=a, F=-a / beta, Cv=beta**2 * (b - 2 * a + c) / h**2)

print("PARTITION FUNCTION (Vol3 Ch03)")
ctrl = abs(lnZ(0.7, 6, 4, False) - PF.ln_Z_total(0.7, 6, 4)) < 1e-12
cov50, quo50 = thermo(50, 25, 10, False), thermo(50, 25, 10, True)
cov200, quo200 = thermo(200, 25, 10, False), thermo(200, 25, 10, True)
print(f"   beta=50  cover lnZ {cov50['lnZ']:.6f} F {cov50['F']:.6f} | quotient lnZ {quo50['lnZ']:.6f} F {quo50['F']:.6f}")
score("H1", ctrl and abs(cov200['lnZ'] - np.log(138)) < 1e-9 and abs(cov50['F'] - (-np.log(138) / 50)) < 1e-9
      and abs(round(cov50['F'], 5) - (-0.09855)) < 1e-9,
      "control: my masked lnZ = original ln_Z_total; cover gives ln 138 and F(50) = -0.09855 (Guide)")
score("H2", abs(quo50['lnZ'] - cov50['lnZ']) < 1e-12 and abs(quo200['lnZ'] - np.log(138)) < 1e-9,
      "quotient: the zero mode (0,0) survives, so ln 138 and F = -ln138/50 are UNCHANGED")

def peak(l_max, m_max, q, betas):
    cv = np.array([thermo(b, l_max, m_max, q)['Cv'] for b in betas]); i = int(np.argmax(cv))
    return 1 / betas[i], cv[i], i
betas = np.logspace(-4, np.log10(200), 600)
rows = {}
for (lm, mm) in [(5, 2), (5, 5), (5, 10), (25, 10)]:
    Tc_c, Cv_c, ic = peak(lm, mm, False, betas); Tc_q, Cv_q, iq = peak(lm, mm, True, betas)
    rows[(lm, mm)] = (Tc_c, Cv_c, Tc_q, Cv_q, ic, iq)
    edge = " (peak at grid edge)" if ic in (0, len(betas) - 1) else ""
    print(f"   l_max={lm:2d} m_max={mm:2d}: cover T_c {Tc_c:9.2f} Cv {Cv_c:11.1f}{edge} | quotient T_c {Tc_q:9.2f} Cv {Cv_q:11.1f}  ratio Cv {Cv_q/Cv_c:.3f}")
repro = any(abs(r[0] - 130.5) / 130.5 < 0.02 and abs(r[1] - 330350) / 330350 < 0.02 for r in rows.values())
print(f"   Guide T_c = 130.5, Cv = 330,350 reproduced by the retained code at any tried (l_max, m_max)? {repro}")
score("H3", all(abs(r[3] / r[1] - 0.5) < 0.1 for r in rows.values()),
      "quotient C_v peak is about 1/2 of the cover's at every cutoff tried; T_c shifts (table above)")
qft_c = PF.ln_Z_qft(20, 8)
d_l, E = PF.build_energy_grid(20, 8); l = np.arange(21)[:, None]; m = np.arange(-8, 9)[None, :]
qft_q = float(np.sum(np.where((l + m) % 2 == 0, d_l[:, None] * E / 2, 0)))
print(f"   QFT zero-point (l_max=20, m_max=8): cover {qft_c:.4e}, quotient {qft_q:.4e}, ratio {qft_q/qft_c:.4f}")

# --------------------------------------------------------------- Casimir zeta
print("\nCASIMIR ZETA (Vol2 Ch02)")
CUV = (1 - CZ.EULER_GAMMA) / 2 * CZ._zeta_S4_analytic(-1.0)
print(f"   zeta_S4(-1) = {CZ._zeta_S4_analytic(-1.0):.6f}, C_UV(cover) = {CUV:.6f}")
# Poisson: sum over m in 2Z of f(m/rho) and over m odd both have n=0 term (rho/2) * int f ; check numerically
def poisson_n0_check(t=0.37, rho=3.0, M=4000):
    ms = np.arange(-M, M + 1); f = np.exp(-t * ms**2 / rho**2)
    ev, od = f[ms % 2 == 0].sum(), f[ms % 2 != 0].sum()
    integral = rho * np.sqrt(np.pi / t)
    return ev, od, integral / 2
ev, od, half = poisson_n0_check()
score("H4", abs(CUV - 0.003207) < 5e-7 and abs(ev - half) < 1e-9 and abs(od - half) < 1e-9,
      f"C_UV(cover) = {CUV:.6f} reproduced; even-m and odd-m sums each = rho/2 * int (to 1e-9 at t=0.37, rho=3): "
      f"C_UV(quotient) = C_UV/2 = {CUV/2:.7f} exactly; still > 0, monotone")

def K_par(t, par, l_max=80):
    tot = 1.0 if par == 0 else 0.0
    for l in range(1, l_max + 1):
        if l % 2 != par: continue
        a = -t * l * (l + 3)
        if a < -300: break
        tot += CZ.s4_deg(l) * np.exp(a)
    return tot
def I_gen(rho, n, K, sign=1.0):
    c = np.pi**2 * n**2 * rho**2
    x = np.linspace(np.log(max(0.5 * np.pi * n * rho, 0.01)) - 12, np.log(c) + 12, 6000)
    t = np.exp(x); Kv = np.array([K(tt) for tt in t])
    return sign * np.trapz(np.exp(-x) * Kv * np.exp(-c * np.exp(-x)), x)
def zfin_cover(rho, N=60): return -rho * sum(I_gen(rho, n, CZ.K_S4) for n in range(1, N + 1))
def zfin_quot(rho, N=60):
    r = rho / 2
    return -(rho / 2) * sum(I_gen(r, n, lambda t: K_par(t, 0)) + (-1)**n * I_gen(r, n, lambda t: K_par(t, 1)) for n in range(1, N + 1))
I1_code = CZ.I_n(137.0, 1)
I1_l1 = I_gen(137.0, 1, lambda t: CZ.K_S4(t) - 1.0)
print(f"   original code I_1(137) = {I1_code:.4e}; 1/(pi^2 137^2) = {1/(np.pi**2*137**2):.4e}; l>=1 part alone = {I1_l1:.3e}")
score("H6", abs(I1_code * np.pi**2 * 137**2 - 1) < 0.02 and I1_l1 < 1e-200,
      "the retained code's I_1(137) is the zero-mode power law 1/(pi^2 rho^2) ~ 5.4e-6; the Guide's 10^-748 is the l>=1 part only")
rhos = np.array([5, 7, 10, 20, 50, 100, 137, 200], float)
cov = np.array([CUV * r + zfin_cover(r) for r in rhos]); quo = np.array([CUV / 2 * r + zfin_quot(r) for r in rhos])
trunc = sum(1 / n**2 for n in range(1, 61)) / (np.pi**2 / 6)      # first run compared to the N=inf value at rtol 1e-3
zero_c = np.array([-trunc / (6 * r) for r in rhos]); zero_q = np.array([-trunc / (3 * r) for r in rhos])  # and failed on this 1.0% (owned)
print("   rho     cover zeta_ren      quotient zeta_ren   (zero-mode x0.98995 truncation: -1/6rho, -1/3rho)")
for r, a, b, zc, zq in zip(rhos, cov, quo, zero_c, zero_q):
    print(f"   {r:5.0f}  {a: .8e}  {b: .8e}   ({zc: .3e}, {zq: .3e})")
fin_c = np.array([zfin_cover(r) for r in rhos]); fin_q = np.array([zfin_quot(r) for r in rhos])
half = np.array([CUV * r / 2 + zfin_cover(r / 2) for r in rhos])
print(f"   quotient(rho) vs cover(rho/2): max |diff| = {np.max(np.abs(quo - half)):.2e} (odd-l sector has no zero mode)")
score("H5", np.all(np.diff(cov) > 0) and np.all(np.diff(quo) > 0)
      and np.allclose(fin_c, zero_c, rtol=1e-4) and np.allclose(fin_q, zero_q, rtol=1e-4) and np.allclose(quo, half, rtol=1e-6),
      "winding piece = zero-mode Casimir -1/(6 rho) cover, -1/(3 rho) quotient (N->inf); quotient(rho) = cover(rho/2); both monotone on [5, 200]: no minimum at 137 SURVIVES")

passed = sum(ok for _, ok in RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}")
