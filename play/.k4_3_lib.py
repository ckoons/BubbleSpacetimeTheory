"""K4-3 Lane B shared instruments (Elie, 2026-10-09). Built from prereg 976951e1 BEFORE Cal's hash; read no data.

w_of_a(f, reading, ...) : equation of state of a ledger whose committed fraction is f(a) (Lyra FILLING_LAW Sec. 3 objects).
fermi_f(W0, Z, R)       : beta-decay phase-space integral in m_e = c = 1 units, with the Coulomb factor F(Z, W).
"""
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp

LN2 = float(np.log(2.0))

# ---------------------------------------------------------------- the ledger
def w_of_a(f, reading, a_grid, era="matter", Omega_coeff=4 * LN2):
    """w(a) = -1 - (1/3) dln rho_DE / dln a for rho_DE = E_commit * f * N_H / V_H = f * (3 ln2/2pi)(hbar/l_P^2) H^2.
    reading 'T': H^2 is the fixed background (matter a^-3, radiation a^-4); f does not feed back.
    reading 'S': 3H^2/8piG = rho_m + rho_DE with rho_DE = Omega(a) 3H^2/8piG, Omega = Omega_coeff * f (rule R: 4 ln2 f).
    Returns (w on a_grid, Omega on a_grid). Pure continuity; no sign is printed by this function."""
    a = np.asarray(a_grid, float)
    n = {"matter": 3.0, "radiation": 4.0}[era]
    fv = np.array([float(f(x)) for x in a])
    if reading == "T":
        rho = fv * a ** (-n)
        Om = Omega_coeff * fv
    elif reading == "S":
        Om = Omega_coeff * fv
        if np.any(Om >= 1):
            raise ValueError("Omega >= 1: the fraction saturates the Friedmann budget (the wall)")
        rho = Om * a ** (-n) / (1 - Om)          # rho_DE = Omega rho_m/(1-Omega), rho_m ~ a^-n
    else:
        raise ValueError(reading)
    # local central difference in ln a at each grid point (np.gradient on the grid was O(1e-6); owned in 5864's first run)
    h = 1e-6
    def lnrho(x):
        fv = float(f(x)); Om_ = Omega_coeff * fv
        return np.log(fv * x ** (-n)) if reading == "T" else np.log(Om_ * x ** (-n) / (1 - Om_))
    dln = np.array([(lnrho(x * np.exp(h)) - lnrho(x * np.exp(-h))) / (2 * h) for x in a])
    return -1 - dln / 3, Om


def w_ode(f, reading, a0, a1, era="matter", Omega_coeff=4 * LN2, npts=400):
    """Same quantity by integrating dln rho/dln a as an ODE state alongside ln a (an independent numerical route)."""
    n = {"matter": 3.0, "radiation": 4.0}[era]
    def rho(a):
        fv = float(f(a)); Om = Omega_coeff * fv
        return fv * a ** (-n) if reading == "T" else Om * a ** (-n) / (1 - Om)
    def rhs(lna, _y):
        a = np.exp(lna); h = 1e-5
        return [(np.log(rho(a * np.exp(h))) - np.log(rho(a * np.exp(-h)))) / (2 * h)]
    sol = solve_ivp(rhs, [np.log(a0), np.log(a1)], [0.0], rtol=1e-11, atol=1e-13, dense_output=True,
                    t_eval=np.linspace(np.log(a0), np.log(a1), npts))
    lna = sol.t
    dln = np.array([rhs(x, None)[0] for x in lna])
    return np.exp(lna), -1 - dln / 3


# ---------------------------------------------------------------- the Fermi integral
mp.mp.dps = 30
ALPHA = mp.mpf(1) / 137            # the BST namespace value; the Coulomb factor's own sensitivity to 137 vs 137.036 is ~1e-5

def fermi_F(Z, W, R=mp.mpf('2.9e-3'), alpha=ALPHA):
    """Relativistic Coulomb factor F(Z, W) (Fermi 1934 form; electron emission, Z the daughter charge).
    gamma = sqrt(1 - (alpha Z)^2), eta = alpha Z W / p, R the nuclear radius in units hbar/(m_e c) (proton: ~0.87 fm / 386 fm)."""
    W = mp.mpf(W); p = mp.sqrt(W * W - 1)
    if Z == 0:
        return mp.mpf(1)
    g = mp.sqrt(1 - (alpha * Z) ** 2); eta = alpha * Z * W / p
    return 2 * (1 + g) * (2 * p * R) ** (2 * g - 2) * mp.exp(mp.pi * eta) * abs(mp.gamma(g + 1j * eta)) ** 2 / mp.gamma(2 * g + 1) ** 2

def sommerfeld(Z, W, alpha=ALPHA):
    p = mp.sqrt(W * W - 1); x = 2 * mp.pi * alpha * Z * W / p
    return x / (1 - mp.exp(-x))

def fermi_f(W0, Z=0, R=mp.mpf('2.9e-3'), alpha=ALPHA):
    """f(W0) = int_1^W0 F(Z,W) p W (W0-W)^2 dW, m_e = c = 1."""
    W0 = mp.mpf(W0)
    return mp.quad(lambda W: fermi_F(Z, W, R, alpha) * mp.sqrt(W * W - 1) * W * (W0 - W) ** 2, [1, W0])

def fermi_f0_closed(W0):
    """Z = 0 closed form: (p0/60)(2W0^4 - 9W0^2 - 8) + (W0/4) ln(W0 + p0)."""
    W0 = mp.mpf(W0); p0 = mp.sqrt(W0 * W0 - 1)
    return p0 / 60 * (2 * W0 ** 4 - 9 * W0 ** 2 - 8) + W0 / 4 * mp.log(W0 + p0)
