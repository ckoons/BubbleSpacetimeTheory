#!/usr/bin/env python3
"""
BST Derivation Ledger  -- per-value list of derivation attempts, scored on dev% AND sigma.
==========================================================================================
Casey's directive (2026-07-02): for every one of the 26, keep a LIST of derivation attempts
under that value (form + computed value + HOW it derives from the substrate + provenance).
Compute each; keep improving until we hit tolerance; never repeat a form we already tried.

TWO axes, because dev% alone fooled us in both directions (Elie's m_s/m_d, Grace's theta13):
  dev%  = |bst-obs|/obs*100         -- Casey's engineering tolerance (<0.1% target)
  sigma = |bst-obs|/measurement_err -- statistical significance (is it consistent with data?)
Verdict:
  MATCH   : sigma <= 2                      (consistent with data -- the physicist's 'derived')
  APPROX  : sigma > 2 but dev% < 1          (good closed form, but a many-sigma APPROXIMATION)
  MISS    : sigma > 2 and dev% >= 1
  (a value's status = its BEST attempt.)  'tol' flag = dev% <= 0.1 (Casey's tolerance met).

Lesson baked in: muon (24/pi^2)^6 is 0.003% but ~1500 sigma -> APPROX, not exact.
theta_QCD=0 is the only sigma=0 exact derivation today. theta13=1/45 is 1.24% but 0.4 sigma -> MATCH.

Run:  python3 play/bst_derivation_ledger.py            # scoreboard
      python3 play/bst_derivation_ledger.py --ledger   # per-value attempt ledger -> notes/BST_Derivation_Ledger.md
PDG 2024 where pinned; UNPINNED marked -- Pass-1 re-pin fills these.
"""
import math, sys
pi=math.pi
rank,Nc,nC,C2,g,Nmax = 2,3,5,6,7,137
v=246.22

# LEDGER[value] = { sector, obs:(value,err,source), attempts:[ {form,val,how,prov} ... ] }
LEDGER = {
 "theta_QCD": dict(sector="CP", obs=(0.0, 1e-10, "PDG |theta|<1e-10"),
   attempts=[dict(form="0", val=0.0, how="pi_1(D_IV^5)=0: domain contractible => no theta-vacuum", prov="K222/T1638")]),
 "m_mu/m_e": dict(sector="lepton", obs=(206.7682830, 4.6e-6, "PDG 2024"),
   attempts=[dict(form="(24/pi^2)^{C_2}", val=(24/pi**2)**C2, how="24=N_c|W(B_2)|, C_2=6; deposit-locus curvature det on compact-sphere stratum", prov="K557/F118")]),
 "m_tau/m_e": dict(sector="lepton", obs=(3477.23, 0.23, "PDG 2024"),
   attempts=[dict(form="g^2*(2^{C_2}+g)=49*71", val=(g**2)*(2**C2+g), how="product of two substrate forms; mechanism NOT forced", prov="T2003")]),
 "alpha_inv": dict(sector="gauge", obs=(137.035999177, 2.1e-8, "PDG 2024"),
   attempts=[dict(form="N_max=137", val=137.0, how="flat integer N_max=N_c^3 n_C+rank", prov="founding"),
             dict(form="Wyler closed form", val=None, how="Wyler measure ratio (137.036...) -- pin the exact expression", prov="F441 UNPINNED")]),
 "m_t": dict(sector="quark", obs=(172.69, 0.30, "PDG 2024 pole"),
   attempts=[dict(form="v/sqrt(2)  (y_t=1)", val=v/math.sqrt(2), how="single-K-orbit forces Yukawa y_t=1; rests on v (FLOOR)", prov="K591/F387")]),
 "sin2_th13(PMNS)": dict(sector="PMNS", obs=(0.02195, 0.0007, "NuFIT 6.0 no-SK"),
   attempts=[dict(form="1/(N_c^2*n_C)=1/45", val=1/45, how="color^2 x bulk-dim; boundary-reaching mixing", prov="K632")]),
 "sinTh_C(Cabibbo)": dict(sector="CKM", obs=(0.2245, 0.0008, "PDG |V_us|"),
   attempts=[dict(form="N_c^2/(2^{N_c}*n_C)=9/40", val=Nc**2/(2**Nc*nC), how="two-point color trace (irreducible N_c^2)", prov="F50")]),
 "m_s/m_d": dict(sector="quark", obs=(20.0, 2.4, "PDG 2024 ratio"),
   attempts=[dict(form="rank^2*n_C=20", val=rank**2*nC, how="little-group mode count on rank-1 stratum (RG-invariant target)", prov="F444/lead"),
             dict(form="(muon x down-row banks) => 22.97", val=(24/pi**2)**C2*(1/3)/3, how="FORCED by 3 banks; internal-consistency probe (1.24 sigma)", prov="Elie4540")]),
 # ---- down-row (STRUCTURAL-MISS, K642) ----
 "m_d/m_e": dict(sector="quark", obs=(9.14, 0.5, "PDG 2024"),
   attempts=[dict(form="N_c^{+1}=3 (GJ)", val=3.0, how="color-root-crossing parity; GUT-FREE mech but GUT-SCALE value", prov="K582/K641")]),
 "m_s/m_mu": dict(sector="quark", obs=(0.884, 0.05, "PDG 2024"),
   attempts=[dict(form="N_c^{-1}=1/3 (GJ)", val=1/3, how="GUT-scale texture; 6.8 sigma MISS", prov="K582/K641")]),
 "m_b/m_tau": dict(sector="quark", obs=(2.352, 0.02, "PDG 2024"),
   attempts=[dict(form="N_c^{0}=1 (GJ)", val=1.0, how="b-tau unif GUT-scale; 80 sigma MISS", prov="K582/K641")]),
}

def dev(b,o): return 0.0 if (o==0 and b==0) else (float('inf') if o==0 else abs(b-o)/abs(o)*100)
def sig(b,o,e): return abs(b-o)/e if e else 0.0
def score(b,o,e):
    if b is None: return ("--", None, None)
    d=dev(b,o); s=sig(b,o,e)
    v = "MATCH" if s<=2 else ("APPROX" if d<1 else "MISS")
    return (v, d, s)

def best(entry):
    o,e,_=entry["obs"]; bestv="--"; rank_={"MATCH":0,"APPROX":1,"MISS":2,"--":3}
    bd=bs=None
    for a in entry["attempts"]:
        v,d,s=score(a["val"],o,e)
        if bestv=="--" or rank_[v]<rank_[bestv]:
            bestv,bd,bs=v,d,s
    return bestv,bd,bs

def scoreboard():
    print("="*96)
    print("BST DERIVATION LEDGER -- scoreboard (best attempt per value; MATCH=<=2sigma, APPROX=<1%% many-sigma, MISS)")
    print("="*96)
    print(f"{'value':16s} {'best form':22s} {'dev%':>7s} {'sigma':>10s}  {'verdict':7s} tol")
    print("-"*96)
    from collections import Counter; tc=Counter()
    for name,e in LEDGER.items():
        o,er,_=e["obs"]
        # find the best attempt's form
        bv,bd,bs=best(e); tc[bv]+=1
        bf=next((a["form"] for a in e["attempts"] if score(a["val"],o,er)[0]==bv), e["attempts"][0]["form"])
        ds=f"{bd:6.3f}" if bd is not None else "   -  "
        ss=f"{bs:10.1f}" if bs is not None else "     -    "
        tol="tol" if (bd is not None and bd<=0.1) else ""
        print(f"{name:16s} {bf[:22]:22s} {ds} {ss}  {bv:7s} {tol}")
    print("-"*96)
    print("TALLY (best-per-value):", dict(tc))
    print("  MATCH = statistically consistent with data (the honest 'derived').")
    print("  APPROX = good closed form but many-sigma off (an approximation, not the exact relation).")
    print("  Only theta_QCD is a 0-sigma exact derivation today.")

def ledger_md():
    L=["# BST Derivation Ledger — every attempt at every value, dev%% + σ",
       "",
       "*From `play/bst_derivation_ledger.py` (single source of truth). Substrate: rank=2,N_c=3,n_C=5,C_2=6,g=7,N_max=137. "
       "Per value: the accumulating list of derivation attempts. MATCH=σ≤2 (consistent), APPROX=<1%% but many-σ (approximation), MISS. "
       "`tol` = dev ≤0.1%% (Casey tolerance). Never delete an attempt — a tried-and-failed form is recorded so we don't repeat it.*",
       ""]
    for name,e in LEDGER.items():
        o,er,src=e["obs"]; bv,bd,bs=best(e)
        L.append(f"## {name}   ·   best: **{bv}**")
        L.append(f"- **Observed:** {o} ± {er}  ({src})")
        L.append(f"- **Attempts:**")
        for a in e["attempts"]:
            v,d,s=score(a["val"],o,er)
            vs=f"{a['val']:.6g}" if a["val"] is not None else "—"
            ds=f"{d:.3f}%" if d is not None else "—"
            ss=f"{s:.1f}σ" if s is not None else "—"
            L.append(f"    - `{a['form']}` = {vs}  →  {ds}, {ss}  [{v}]  — *{a['how']}*  ({a['prov']})")
        L.append("")
    import os
    out=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"notes","BST_Derivation_Ledger.md")
    open(out,"w").write("\n".join(L)); print("wrote",out,f"({len(LEDGER)} values seeded)")

if __name__=="__main__":
    if "--ledger" in sys.argv: ledger_md()
    else: scoreboard()
