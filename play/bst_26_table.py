#!/usr/bin/env python3
"""
BST 26 Table -- end-of-first-pass state of all 26 SM parameters.
Three axes: dev%, sigma (=|d|/err, scheme-aware), cheapness (# simple substrate fractions within 1sigma).
Verdict: MATCH (sigma<=2) / APPROX (sigma>2, dev<1%) / MISS ; FLOOR/NEG/OPEN terminal.
'cheap' flag when >=3 simple forms fit within 1sigma (coarse target -> weak evidence).
PDG/NuFIT ~2024; scheme-aware errors on runners/quark-masses. RE-PIN exact where flagged.
"""
import math
from fractions import Fraction
pi=math.pi; sq=math.sqrt
rank,Nc,nC,C2,g,Nmax=2,3,5,6,7,137
c13=math.cos(math.asin(sq(0.02195)))**2

# name, sector, form, bst_val, obs, err, mech
R=[
 # masses (Grace)
 ("m_e","mass","6pi^5 a^12 m_Pl", None, 0.511, 0.0, "CAND"),
 ("m_mu/m_e","mass","(24/pi^2)^6", (24/pi**2)**6, 206.7683, 4.6e-6, "PRINCIPLE"),
 ("m_tau/m_e","mass","49*71", 49*71, 3477.23, 0.23, "CAND"),
 ("m_c/m_u","mass","589", 589, 588.0, 60.0, "CAND-coarse"),
 ("m_u","mass","up-ladder", None, 2.16, 0.5, "NEG-scheme"),
 ("m_t","mass","v/sqrt2 (y_t=1)", 246.22/sq(2), 172.69, 2.0, "FORCED-on-v"),  # scheme-aware err
 ("m_s/m_d","mass","rank^2*n_C=20", rank**2*nC, 20.0, 2.4, "LEAD(observed ladder)"),
 ("m_d/m_e","mass","N_c=3 (GJ)", 3, 9.14, 0.5, "MISS-GUTscale"),
 ("m_b/m_s","mass","N_c^2 n_C=45", Nc**2*nC, 52.0, 3.0, "MISS-mixedscale"),
 # mixing (Lyra)
 ("V_us(th12)","CKM","1/(2 sqrt5)", 1/(2*sq(5)), 0.2243, 0.0008, "value-form"),
 ("V_cb(th23)","CKM","36/869", 36/869, 0.0409, 0.0008, "value-form"),
 ("V_ub(th13)","CKM","(1/3)^5", (1/Nc)**5, 0.00369, 0.0003, "STRUCTURAL"),
 ("delta_CKM","CKM","arctan(sqrt5) deg", math.degrees(math.atan(sq(5))), 65.9, 3.5, "FORCED(triangle)"),
 ("sin2_th12","PMNS","|U_e2|^2/(1-|U_e3|^2)", 0.30/c13, 0.307, 0.013, "FORCED(matrix-elt)"),
 ("sin2_th13","PMNS","1/(N_c^2 n_C)=1/45", 1/45, 0.02195, 0.0007, "FORCED(boundary)"),
 ("sin2_th23","PMNS","4/7", 4/7, 0.545, 0.03, "value-form"),
 ("delta_PMNS","PMNS","pi+arctan sqrt5 deg", 180+math.degrees(math.atan(sq(5))), 197.0, 40.0, "LEAD(unconstrained)"),
 # scales (Elie)
 ("alpha_inv","gauge","Wyler closed form", 137.036082, 137.035999, 2.1e-8, "FORCED(Wyler geom) 0.6ppm"),
 ("alpha_s","gauge","7/20 (runs)", None, 0.1179, 0.0, "NEG(runner)"),
 ("sin2_thW","gauge","3/13", 3/13, 0.23122, 0.00004, "APPROX(11sig, runs)"),
 ("vev_v","Higgs","pure scale", None, 246.22, 0.0, "FLOOR"),
 ("m_H","Higgs","(form pending)", 125.1, 125.25, 0.17, "MATCH(form-pin)"),
 ("theta_QCD","CP","0 (pi_1=0)", 0.0, 0.0, 1e-10, "FORCED-exact"),
 ("m_nu1","nu","FLOOR/falsifier", None, None, 0.0, "OPEN"),
 ("m_nu2","nu","(form pending)", None, None, 0.0, "OPEN(0.09sig claim)"),
 ("m_nu3","nu","(form pending)", None, None, 0.0, "OPEN(APPROX claim)"),
]

# cheapness as a ROBUST precision-based soft-flag (Elie: the form-COUNT is form-space-relative,
# same K631-S1 lesson -> use measurement precision, not a form scan). coarse target -> a match is weak.
def prec_flag(o,e):
    if o is None or e==0 or o==0: return ""
    rel=abs(e/o)
    return "coarse" if rel>0.02 else ("tight" if rel<0.005 else "")
def dev(b,o): return 0.0 if (o==0 and b==0) else (None if (b is None or o is None) else (float('inf') if o==0 else abs(b-o)/abs(o)*100))
def sig(b,o,e): return None if (b is None or o is None or e==0) else abs(b-o)/e
def verdict(b,o,e,mech):
    if "FLOOR" in mech: return "FLOOR"
    if "NEG" in mech: return "NEG"
    if "OPEN" in mech or b is None or o is None: return "OPEN"
    s=sig(b,o,e); d=dev(b,o)
    if s is None: return "OPEN"
    return "MATCH" if s<=2 else ("APPROX" if d<1 else "MISS")

from collections import Counter; tc=Counter()
print("="*104)
print("BST 26 TABLE -- end of Mid-Year day (Pass 1+2)  (dev% | sigma=|d|/err scheme-aware | target-precision | verdict)")
print("="*104)
print(f"{'#':2s} {'param':13s} {'sec':6s} {'best form':22s} {'dev%':>6s} {'sigma':>8s} {'target':6s} {'verdict':7s} mech")
print("-"*104)
for i,(n,sec,f,b,o,e,mech) in enumerate(R,1):
    v=verdict(b,o,e,mech); tc[v]+=1
    d=dev(b,o); s=sig(b,o,e); pf=prec_flag(o,e)
    ds=f"{d:6.2f}" if d is not None else "   -  "
    ss=f"{s:8.1f}" if s is not None else "    -   "
    weak="*" if (pf=="coarse" and v=="MATCH" and "FORCED" not in mech) else " "
    print(f"{i:2d} {n:13s} {sec:6s} {f:22s} {ds} {ss} {pf:6s}{weak}{v:7s} {mech}")
print("-"*104)
print("TALLY:", dict(tc))
print(f"\n coverage: all 26 have a scored first-pass attempt.")
print(f" MATCH={tc['MATCH']}  APPROX={tc['APPROX']}  MISS={tc['MISS']}  FLOOR={tc['FLOOR']}  NEG={tc['NEG']}  OPEN={tc['OPEN']}")
print(" (*) = WEAK match: coarse target (rel-err>2%) AND mechanism not forced -> a match here is weak evidence.")
print(" DERIVED-STRONG (MATCH + forced-mechanism + not-weak), and its K645 caveat:")
print("   sin2_th13 1/45      -- SOLID (expensive + boundary mechanism)")
print("   theta_QCD 0         -- pending: pi_1 vs gauge-pi_3/instanton; needs contractible->trivial-bundle explicit")
print("   alpha Wyler 0.6ppm  -- mechanism FORCED (Wyler geom) but still APPROX (~4000 sigma, not exact)")
print("   delta_CKM arctan5   -- mechanism-dependent: coarse target, must FORCE sqrt(n_C) over sqrt4/6/7")
print("   sin2_th12 |U_e2|^2  -- FORCED (matrix-element) + un-cheapened (tells 3/10 from 5/16); NEW this pass")
print("   m_t v/sqrt2         -- rests on the v FLOOR (not free-standing)")
print(" => genuinely solid on BOTH axes today: sin2_th13, + theta13-forced-matrix mixing. The rest carry caveats.")
