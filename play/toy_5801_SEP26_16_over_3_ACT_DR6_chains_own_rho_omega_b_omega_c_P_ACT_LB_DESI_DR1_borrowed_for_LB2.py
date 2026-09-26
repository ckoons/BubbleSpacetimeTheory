#!/usr/bin/env python3
"""
Toy 5801 — 16/3 on ACT DR6: the fit's OWN corr(omega_b, omega_c) from LAMBDA's public chains (Elie, 2026-09-26).
Prereg notes/Elie_R5_prereg_toy_5801_ACT_chain_rho_2026-09-26.md (sha c2bd0e84; original ad527399).
Chains: LAMBDA ACT DR6.02 lcdm set, p-actbase-l-b_lcdm_camb (P-ACT + CMB lensing + DESI 2024 = DR1 BAO; yaml line
'bao.desi_2024_bao_all', output 'DR6base_P18_CMBlens_DESIbao') and p-actbase_lcdm_camb (P-ACT, control).
Tarball sha256 in data/sources_elie_2026-09-26/. No DR2-BAO chain is on the lcdm page: the DR1 chain's rho is BORROWED
for the P-ACT-LB2 numbers of ACT Table 5 (11.74 ± 0.06, 2.258 ± 0.010) and labelled so.
Usage: python3 toy_5801...py <dir containing the two extracted chain folders>
"""
import sys, glob, math
import numpy as np
from math import erf, sqrt
SP = sys.argv[1] if len(sys.argv) > 1 else '.'
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
T = 16/3
def load(tag, burn):
    W, B, C = [], [], []
    for f in sorted(glob.glob(f"{SP}/{tag}/{tag}.[0-9].txt")):
        hdr = open(f).readline().split()[1:]
        d = np.loadtxt(f)
        n0 = int(len(d)*burn); d = d[n0:]
        W.append(d[:, hdr.index('weight')]); B.append(d[:, hdr.index('ombh2')]); C.append(d[:, hdr.index('omch2')])
    return np.concatenate(W), np.concatenate(B), np.concatenate(C)
def wstats(w, x):
    m = np.sum(w*x)/np.sum(w); return m, math.sqrt(np.sum(w*(x-m)**2)/np.sum(w))
def wcorr(w, x, y):
    mx, sx = wstats(w, x); my, sy = wstats(w, y)
    return np.sum(w*(x-mx)*(y-my))/np.sum(w)/(sx*sy)
def gpull(c, dc, b, db, rho):
    R = c/b; rel = math.sqrt((dc/c)**2 + (db/b)**2 - 2*rho*(dc/c)*(db/b)); return (R-T)/(R*rel)
out = {}
for burn in (0.3, 0.0):
    for tag in ('p-actbase_lcdm_camb', 'p-actbase-l-b_lcdm_camb'):
        w, b, c = load(tag, burn)
        mb, sb = wstats(w, b); mc, sc = wstats(w, c); rho = wcorr(w, b, c)
        R = c/b; mR, sR = wstats(w, R)
        below = np.sum(w[R <= T])/np.sum(w)
        out[(tag, burn)] = (mb, sb, mc, sc, rho, mR, sR, below, np.sum(w), len(w))
        print(f"burn {burn:.1f} {tag:26s} N={len(w):6d} sumw={np.sum(w):8.0f}  100ωb={100*mb:.4f}±{100*sb:.4f}  100ωc={100*mc:.3f}±{100*sc:.3f}"
              f"  ρ={rho:+.3f}  R={mR:.3f}±{sR:.3f}  pull=(R-16/3)/sd={(mR-T)/sR:+.2f}σ  frac(R≤16/3)={below:.2e}")
cm = out[('p-actbase_lcdm_camb', 0.3)]
ok_ctrl = abs(100*cm[2]-11.93) <= 0.2*0.12 and abs(100*cm[0]-2.250) <= 0.2*0.011
check("CONTROL: P-ACT chain reproduces ACT T5 P-ACT row (11.93±0.12, 2.250±0.011) within 0.2 sd", ok_ctrl,
      f"(11.93 vs {100*cm[2]:.3f}; 2.250 vs {100*cm[0]:.4f})")
lb = out[('p-actbase-l-b_lcdm_camb', 0.3)]
ok_ctrl2 = abs(100*lb[2]-11.79) <= 0.2*0.09 and abs(100*lb[0]-2.256) <= 0.2*0.011
check("CONTROL: P-ACT-LB (DR1) chain reproduces ACT T5 P-ACT-LB row (11.79±0.09, 2.256±0.011) within 0.2 sd", ok_ctrl2,
      f"(11.79 vs {100*lb[2]:.3f}; 2.256 vs {100*lb[0]:.4f})")
rho = lb[4]
check("DIRECTION: chain ρ(ω_b,ω_c) negative and in [-0.60, -0.20]", -0.60 <= rho <= -0.20, f"ρ = {rho:+.3f}")
p_lb2 = gpull(11.74, 0.06, 2.258, 0.010, rho)
p_lb2_0 = gpull(11.74, 0.06, 2.258, 0.010, 0.0); p_lb2_A2 = gpull(11.74, 0.06, 2.258, 0.010, -0.606)
print(f"   P-ACT-LB2 (ACT T5 numbers): ρ=0 {p_lb2_0:+.2f}σ; ρ=DESI A2 -0.606 {p_lb2_A2:+.2f}σ; ρ=chain(DR1, BORROWED) {rho:+.3f} -> {p_lb2:+.2f}σ")
check("DIRECTION: LB2 pull at the borrowed chain ρ lies in [3.0, 3.6]σ", 3.0 <= abs(p_lb2) <= 3.6, f"{p_lb2:+.2f}σ")
check("KILL of 'past 3σ' NOT fired: chain ρ > -0.61 (pull > 3.0σ)", rho > -0.61)
# the DR1 combination itself, from its own samples (no Gaussian step)
print(f"   P-ACT-LB (DR1) from its own samples: (R̄-16/3)/sd_R = {(lb[5]-T)/lb[6]:+.2f}σ; Gaussian with chain ρ on T5 row: {gpull(11.79,0.09,2.256,0.011,rho):+.2f}σ")
print(f"   burn-in sensitivity: ρ(0.3) = {out[('p-actbase-l-b_lcdm_camb',0.3)][4]:+.3f}, ρ(0.0) = {out[('p-actbase-l-b_lcdm_camb',0.0)][4]:+.3f}")
# stability (added before reading anything but the 0.3/0.0 rows above): burn 0.5, and each of the 4 chains separately at 0.3
w5, b5, c5 = load('p-actbase-l-b_lcdm_camb', 0.5); r5 = wcorr(w5, b5, c5)
per = []
for f in sorted(glob.glob(f"{SP}/p-actbase-l-b_lcdm_camb/p-actbase-l-b_lcdm_camb.[0-9].txt")):
    hdr = open(f).readline().split()[1:]; d = np.loadtxt(f); d = d[int(len(d)*0.3):]
    per.append(wcorr(d[:, hdr.index('weight')], d[:, hdr.index('ombh2')], d[:, hdr.index('omch2')]))
print(f"   stability: ρ(burn 0.5) = {r5:+.3f}; per-chain ρ (burn 0.3) = {', '.join(f'{x:+.3f}' for x in per)}")
check("STABILITY: ρ(burn 0.5) within 0.05 of ρ(burn 0.3), and per-chain spread < 0.1 (burn 0 is unconverged: fails the T5 control)",
      abs(r5 - rho) < 0.05 and max(per) - min(per) < 0.1)
print(f"\nSCORE: {sum(score)}/{len(score)}")
