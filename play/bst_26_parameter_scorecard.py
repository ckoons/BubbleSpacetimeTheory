#!/usr/bin/env python3
"""
BST 26-Parameter Scorecard  (Casey mid-year directive: fast pass over all 26, then verify the misses)
=====================================================================================================
One honest row per SM free parameter (26 = 9 fermion masses + 4 CKM + 3 gauge + 2 Higgs
+ 1 theta_QCD + 3 nu masses + 4 PMNS). For each: BST's claim, the PDG observable, the
precision, and a tier. The MISSES (large deviation / no mechanism / honest-negative / open)
are what we build verify-tools for next.

Run:  python3 play/bst_26_parameter_scorecard.py
PDG values are 2024-ish; RE-PIN before external use. This is the landscape, not a bank ledger.
"""
import math
pi = math.pi
Nc, nC, C2, g, rank, Nmax = 3, 5, 6, 7, 2, 137

# each: (sector, param, bst_form, bst_val, obs_val, tier, note)
#   tier in FIRM / COND / CAND / PARTIAL / PRINCIPLE / NEG(honest-negative) / FLOOR(pure scale) / OPEN
R = [
 # ---- charged fermion masses (9) ----
 ("mass","m_e","anchor / 6*pi^5*alpha^12*m_Pl (grav)", None, None, "CAND","quoted as unit; gravity-route ~0.03% claim, not independently firm"),
 ("mass","m_mu","(24/pi^2)^6 * m_e", (24/pi**2)**6*0.5109989, 105.6584, "PRINCIPLE","principle-gated (F118); 0.004%"),
 ("mass","m_tau","49*71 * m_e", 49*71*0.5109989, 1776.86, "CAND","product-mechanism not forced; demoted from bank"),
 ("mass","m_u","up=g-ladder", None, 2.16, "NEG","up-sector forms convention-contaminated (Elie 4526)"),
 ("mass","m_d","N_c^+1 * m_e (GJ)", 3*0.5109989, 4.67, "COND","K641: GJ GUT-SCALE value; ~3x off observed; scale-gated"),
 ("mass","m_s","N_c^-1 * m_mu (GJ)", (1/3)*105.6584, 93.4, "COND","K641: GJ GUT-scale; ~2.6x off; scale-gated"),
 ("mass","m_c","-", None, 1270.0, "NEG","charm explicitly NOT banked (scheme-trap, K639)"),
 ("mass","m_b","N_c^0 * m_tau (GJ)", 1*1776.86, 4180.0, "COND","K641: GJ GUT-scale (b-tau unif); ~2.35x off; scale-gated"),
 ("mass","m_t","y_t=1 -> v/sqrt2", 246.22/math.sqrt(2), 172.69, "FIRM","0.7-0.8% to pole (K591)"),
 # ---- CKM (4) ----
 ("CKM","sinTh12_C","9/40 (=lambda)", 9/40, 0.2245, "CAND","Cabibbo; 0.2%; mechanism (two-point) but held candidate"),
 ("CKM","V_ub(th13)","(1/3)^5", (1/3)**5, 0.00369, "CAND","structural ~12%"),
 ("CKM","V_cb(th23)","dual-rho form", 0.0412, 0.0409, "CAND","structural (F437)"),
 ("CKM","delta_CKM","Jarlskog form", 3.0e-5, 3.08e-5, "CAND","J~0.3% (Vol2); phase itself not firm"),
 # ---- gauge (3) ----
 ("gauge","alpha_EM","1/N_max (Wyler)", 1/137.0, 1/137.036, "PARTIAL","value-banked; EM-identification NOT forced (K635/637)"),
 ("gauge","alpha_s","-", None, 0.1179, "NEG","runs; honest-negative"),
 ("gauge","sin2thW","-", None, 0.23122, "NEG","runs; 3/8 was a forbidden GUT value (retracted)"),
 # ---- Higgs (2) ----
 ("Higgs","vev_v","pure scale", None, 246.22, "FLOOR","principled floor (Casey #9); open by scale-invariance"),
 ("Higgs","m_H(lambda)","lambda_H structural", None, 125.25, "CAND","D-tier ~0.1% claim (INV-4833); structural"),
 # ---- strong CP (1) ----
 ("CP","theta_QCD","pi_1(D_IV^5)=0", 0.0, 0.0, "FIRM","forced: contractible -> no theta-vacuum (K222)"),
 # ---- neutrino masses (3) ----
 ("nu-mass","m_nu1","-", None, None, "OPEN","forward falsifier only (K636 m3/m1 pi-free); scale=floor"),
 ("nu-mass","m_nu2","-", None, None, "OPEN","pi-ful (K636 forced form); not banked"),
 ("nu-mass","m_nu3","-", None, None, "OPEN","pi-free; testable when masses pin"),
 # ---- PMNS (4) ----
 ("PMNS","sin2th12","-", None, 0.307, "CAND","5/16=0.3125 (1.8%) or 3/10; measurement-limited"),
 ("PMNS","sin2th13","1/(N_c^2*n_C)=1/45", 1/45, 0.02219, "FIRM","0.1%; convention-robust (K632) -- BANKED"),
 ("PMNS","sin2th23","upper octant", 0.5, 0.545, "CAND","BST predicts upper octant; form ~structural"),
 ("PMNS","delta_PMNS","-", None, None, "OPEN","not addressed; PDG poorly known"),
]

def prec(b,o):
    if b is None or o is None or o==0: return None
    return abs(b-o)/abs(o)*100

order={"FIRM":0,"COND":1,"PARTIAL":2,"PRINCIPLE":3,"CAND":4,"FLOOR":5,"OPEN":6,"NEG":7}
R.sort(key=lambda r: (order[r[5]], r[0]))

print("="*94)
print("BST 26-PARAMETER SCORECARD  (fast pass; PDG re-pin before external use)")
print("="*94)
print(f"{'sector':8s} {'param':12s} {'BST form':22s} {'prec%':>7s}  tier       note")
print("-"*94)
from collections import Counter
tc=Counter()
misses=[]
for sec,par,form,bv,ov,tier,note in R:
    tc[tier]+=1
    p=prec(bv,ov)
    ps = f"{p:6.2f}" if p is not None else "   -  "
    print(f"{sec:8s} {par:12s} {form[:22]:22s} {ps:>7s}  {tier:10s} {note[:34]}")
    if tier in ("COND","CAND","NEG","OPEN") or (p is not None and p>2):
        misses.append((par,tier,p,note))
print("-"*94)
print("TALLY over 26:", dict(tc))
firmish = tc['FIRM']
print(f"\n  FIRM (clean, forced, <1%):        {tc['FIRM']}   (theta_QCD, m_t, PMNS th13)")
print(f"  CONDITIONAL (scale-gated, K641):  {tc['COND']}   (down-row m_d,m_s,m_b -- GJ GUT-scale)")
print(f"  PARTIAL / PRINCIPLE-gated:        {tc['PARTIAL']+tc['PRINCIPLE']}   (alpha; muon)")
print(f"  CANDIDATE (in play, needs mech):  {tc['CAND']}")
print(f"  PURE-SCALE FLOOR (open by #9):    {tc['FLOOR']}   (Higgs vev)")
print(f"  OPEN (nu masses, PMNS delta):     {tc['OPEN']}")
print(f"  HONEST NEGATIVE (runners/traps):  {tc['NEG']}   (alpha_s, sin2thW, m_u, m_c)")
print(f"\n  => Certified-FIRM against observation: {firmish} of 26. Everything else is a MISS to verify/build.")
print("\nMISSES to build verify-tools for (Casey: 'then build tools to verify the misses'):")
for par,tier,p,note in misses:
    pj = f"{p:.1f}%" if p is not None else " -- "
    print(f"   [{tier:5s}] {par:12s} {pj:>6s}  {note[:52]}")
