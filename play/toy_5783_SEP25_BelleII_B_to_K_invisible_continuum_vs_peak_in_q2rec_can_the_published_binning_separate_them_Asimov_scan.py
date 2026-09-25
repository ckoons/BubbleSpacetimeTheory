#!/usr/bin/env python3
"""
Toy 5783 — B+ -> K+ + invisible: can Belle II's q2_rec binning tell a CONTINUUM from a PEAK?
(Elie, 2026-09-25; instrument for Lyra's round-2 item 1 — ready before her pre-registration.)

PINNED INPUTS (Grace, data/sources_grace_2026-09-25/meson_photon/):
  2311.14647 (Belle II PRD 109 112006): 362 fb^-1; ITA SR bins q2_rec [-1,4,8,25] GeV^2 x eta(BDT2)
      [0.92..1.00]; eta>0.98 slice: SM signal 40, background 977 events; SM BF (5.58+-0.37)e-6;
      ITA BF 2.7e-5, combined 2.3e-5.
  2602.09666 (Gartner et al., PRD 114 032003): best two-body m_X = 2.1(+0.2,-0.1) GeV,
      B(K X)*P_inv = 9.2e-6; Breit-Wigner eq. (3); Gamma_X in {0.1, 0.5} GeV;
      "the coarse q2rec binning ... limits the sensitivity to narrow structures".
  rpp2026 strange mesons: m_K+ = 493.677 MeV.
NOT PINNED (flagged; each scanned or stated so the conclusion is shown not to hinge on it):
  m_B+ = 5.27941 GeV (PDG value; Grace pin owed — enters only q2_max = 22.9 GeV^2);
  f+(q2) = 1/(1 - q2/M^2), M scanned in {5.4, 6.0} GeV (HPQCD not pinned);
  q2_rec resolution sigma (Gaussian on true q2) scanned {0.5, 1, 2} GeV^2;
  background shape across q2 bins (Supplemental, not pinned) scanned {flat per GeV^2, equal per bin, rising};
  efficiency flat in q2 (2311.14647 Fig. 6 not digitised).
Signal yield of the new component: 40 * 9.2e-6/5.58e-6 = 66 events in the eta>0.98 slice.

HYPOTHESES:  PEAK = SM + BW(m_X = 2.1, Gamma = 0.1);  CONT = SM + pair continuum
  dG/dq2 ∝ lambda^{3/2} f+^2 * beta^p, beta = sqrt(1 - 4 m_chi^2/q2), p in {1, 3}; free: m_chi, norm.
MEASURE: Asimov Poisson deviance, truth = PEAK, best-fit CONT (m_chi, norm minimised) with SM+bkg fixed.
   Scales linearly with luminosity. 3 sigma <-> Delta chi2 >= 9 (1 extra dof ignored — optimistic for separation).

DIRECTION, PRINTED BEFORE NUMBERS (prereg lines; the scan decides):
  P1  Published 3 bins, 362 fb^-1: Delta chi2 < 1 in EVERY scanned variant -> not separable today.
  P2  Published 3 bins, 50 ab^-1: still < 9 in at least one variant (3 bins cannot resolve a shape).
  P3  1-GeV^2 bins, sigma <= 1 GeV^2, 50 ab^-1: >= 9 in every such variant -> separable with finer binning.
  P4  (control) PEAK vs itself gives 0; CONT truth vs CONT fit gives ~0.
"""
import numpy as np
from math import erf, sqrt, log

mB, mK = 5.27941, 0.493677
q2max = (mB - mK)**2
L_NOW = 0.362  # ab^-1
N_SM, N_BKG, N_X = 40.0, 977.0, 40.0*9.2e-6/5.58e-6
EDGES3 = np.array([-1.0, 4.0, 8.0, 25.0])
EDGES1 = np.concatenate([[-1.0], np.arange(0.0, 24.0, 1.0), [25.0]])

z = np.linspace(1e-4, q2max - 1e-6, 6000)   # true q2 grid
dz = z[1] - z[0]

def lam(q2):
    return (mB**2 + mK**2 + q2)**2 - 4*mB**2*mK**2 - 4*(mB**2 + mK**2)*q2 + 0*q2 if False else \
           mB**4 + mK**4 + q2**2 - 2*mB**2*mK**2 - 2*mB**2*q2 - 2*mK**2*q2

def ffp(q2, M):
    return 1.0/(1 - q2/M**2)

def sm_shape(M):
    s = np.clip(lam(z), 0, None)**1.5 * ffp(z, M)**2
    return s/(s.sum()*dz)

def bw_shape(mX, G):
    s = mX*G/((z - mX**2)**2 + mX**2*G**2)
    s = s*np.clip(lam(z), 0, None)**0.5          # two-body phase space factor (tiny effect)
    return s/(s.sum()*dz)

def cont_shape(mchi, M, p):
    thr = 4*mchi**2
    beta = np.sqrt(np.clip(1 - thr/np.maximum(z, 1e-12), 0, None))
    s = np.clip(lam(z), 0, None)**1.5 * ffp(z, M)**2 * beta**p
    tot = s.sum()*dz
    return s/tot if tot > 0 else None

def fold(shape, edges, sigma):
    """fraction of events per reconstructed bin, Gaussian smearing of true q2."""
    cdf = lambda x: 0.5*(1 + np.vectorize(erf)((x - z)/(sigma*sqrt(2))))
    fr = np.array([((cdf(edges[i+1]) - cdf(edges[i]))*shape).sum()*dz for i in range(len(edges)-1)])
    return fr

def bkg_frac(edges, kind):
    w = np.diff(edges)
    if kind == "flat/GeV2":
        f = w
    elif kind == "equal/bin":
        f = np.ones_like(w)
    else:  # rising
        c = 0.5*(edges[1:] + edges[:-1]) + 2.0
        f = w*c
    return f/f.sum()

def dev(n, nu):
    nu = np.maximum(nu, 1e-12)
    return 2*np.sum(nu - n + np.where(n > 0, n*np.log(np.maximum(n, 1e-300)/nu), 0))

def best_cont_dev(n_obs, sm, bk, edges, sigma, M, p, scale):
    best = 1e99
    for mchi in np.linspace(0.0, 2.3, 47):
        cs = cont_shape(mchi, M, p)
        if cs is None:
            continue
        fc = fold(cs, edges, sigma)
        # analytic-ish norm scan
        for nx in np.linspace(0.2, 2.5, 47)*N_X*scale:
            d = dev(n_obs, sm + bk + nx*fc)
            if d < best:
                best = d
    return best

print("Toy 5783 — continuum vs peak in B+ -> K+ invisible\n")
print("DIRECTION (before numbers): P1 not separable today (3 bins, <1); P2 3 bins still <9 at 50/ab in some variant;")
print("                            P3 1-GeV^2 bins, sigma<=1, 50/ab: >=9 in every variant; P4 controls ~0.\n")
print(f"q2_max = {q2max:.3f} GeV^2 ; N_X (eta>0.98) = {N_X:.1f} ; m_X^2 = {2.1**2:.2f} GeV^2 (bin edge at 4.0)\n")

results = []
for M in (5.4, 6.0):
    sm_s = sm_shape(M)
    pk_s = bw_shape(2.1, 0.1)
    for sigma in (0.5, 1.0, 2.0):
        for edges, ename in ((EDGES3, "3 bins"), (EDGES1, "1-GeV2")):
            fsm = fold(sm_s, edges, sigma); fpk = fold(pk_s, edges, sigma)
            for bkind in ("flat/GeV2", "equal/bin", "rising"):
                fb = bkg_frac(edges, bkind)
                for p in (1, 3):
                    row = {"M": M, "sigma": sigma, "bins": ename, "bkg": bkind, "p": p}
                    for L in (L_NOW, 50.0):
                        s = L/L_NOW
                        sm = N_SM*s*fsm; bk = N_BKG*s*fb
                        n = sm + bk + N_X*s*fpk
                        row[L] = best_cont_dev(n, sm, bk, edges, sigma, M, p, s)
                    results.append(row)

def show(filt, title):
    print(title)
    for r in results:
        if filt(r):
            print(f"  M={r['M']} sig={r['sigma']} {r['bins']:7s} bkg={r['bkg']:10s} p={r['p']}: "
                  f"dchi2 now={r[L_NOW]:7.3f}   50/ab={r[50.0]:9.2f}")
show(lambda r: r["bins"] == "3 bins" and r["M"] == 5.4, "Published binning (M=5.4 shown; M=6.0 in the checks):")
show(lambda r: r["bins"] == "1-GeV2" and r["M"] == 5.4, "\n1-GeV^2 binning (M=5.4 shown):")

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")
print()
r3 = [r for r in results if r["bins"] == "3 bins"]
r1 = [r for r in results if r["bins"] == "1-GeV2" and r["sigma"] <= 1.0]
check("P1 published bins, 362/fb: dchi2 < 1 in every variant", all(r[L_NOW] < 1 for r in r3))
check("P2 published bins, 50/ab: < 9 in at least one variant", any(r[50.0] < 9 for r in r3))
check("P3 1-GeV2 bins, sigma<=1, 50/ab: >= 9 in every variant", all(r[50.0] >= 9 for r in r1))
# controls
sm_s = sm_shape(5.4); fsm = fold(sm_s, EDGES3, 1.0); fb = bkg_frac(EDGES3, "flat/GeV2")
fpk = fold(bw_shape(2.1, 0.1), EDGES3, 1.0)
n = N_SM*fsm + N_BKG*fb + N_X*fpk
check("P4a PEAK truth vs PEAK model: deviance 0", dev(n, n) < 1e-9, can_fail=False)
fc = fold(cont_shape(1.0, 5.4, 1), EDGES1, 1.0); fsm1 = fold(sm_s, EDGES1, 1.0); fb1 = bkg_frac(EDGES1, "flat/GeV2")
s = 50/L_NOW
nc = s*(N_SM*fsm1 + N_BKG*fb1 + N_X*fc)
check("P4b CONT truth refit by CONT at 50/ab, fine bins: dchi2 < 0.5",
      best_cont_dev(nc, s*N_SM*fsm1, s*N_BKG*fb1, EDGES1, 1.0, 5.4, 1, s) < 0.5, can_fail=False)

mx = max(r[50.0] for r in r3); mn1 = min(r[50.0] for r in r1)
print(f"\n  range, published bins @50/ab: max dchi2 = {mx:.2f};  fine bins (sigma<=1) @50/ab: min = {mn1:.2f}")
n_ = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n_}  (can-fail {kcf}/{len(cf)}; {n_-len(cf)} controls)")
