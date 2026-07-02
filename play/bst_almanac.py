#!/usr/bin/env python3
"""
BST Almanac + Scorecard  -- one source of truth for all 26 SM parameters.
========================================================================
Casey's rule (2026-07-02): status is COMPUTED from the match, not spoken by a CI.
    dev <= 0.1%  -> DONE      (matches, and tight)
    dev <  1.0%  -> SOLID     (matches)
    dev >= 1.0%  -> MISS      (does not match -- a target, not a bank)
Non-numeric dispositions: OPEN (no BST value yet), FLOOR (pure scale, open by Casey #9),
NEG (RG-runner / scheme-dependent -- not a fixed constant to derive).

Two views, same data (they cannot drift):
    python3 play/bst_almanac.py              # scorecard (did it match)
    python3 play/bst_almanac.py --almanac    # almanac (how it derives), writes notes/BST_Almanac.md

Every 'expected' is PDG-2024-ish and flagged RE-PIN. 'mech' is a SEPARATE axis from match:
a value can match (SOLID) yet have an unforced mechanism (GATED) -- both are shown, because
the down-row taught us match-without-mechanism and mechanism-without-match are both traps.
"""
import math, sys
pi = math.pi
rank, Nc, nC, C2, g, Nmax = 2, 3, 5, 6, 7, 137
v_higgs = 246.22
m_e, m_mu, m_tau = 0.5109989, 105.6584, 1776.86  # MeV, lepton pole

# param, sector, substrate_derivation(how, from the 5 integers), bst_value, expected, unit, mech, provenance
ROWS = [
 ("theta_QCD","CP","pi_1(D_IV^5)=0 (domain contractible) => no theta-vacuum => theta=0",
    0.0, 0.0, "rad", "FORCED", "K222/T1638"),
 ("m_mu/m_e","mass","(24/pi^2)^{C_2}; 24=N_c*|W(B_2)|, C_2=6",
    (24/pi**2)**C2, m_mu/m_e, "ratio", "PRINCIPLE(F118)", "K557"),
 ("m_tau/m_e","mass","g^2*(2^{C_2}+g) = 49*71",
    (g**2)*(2**C2+g), m_tau/m_e, "ratio", "CANDIDATE(product not forced)", "T2003"),
 ("alpha_EM","gauge","1/N_max = 1/137 (Wyler measure value)",
    1/Nmax, 1/137.036, "", "GATED(EM-id not forced)", "K635/637"),
 ("sin2_th13(PMNS)","PMNS","1/(N_c^2*n_C) = 1/45",
    1/(Nc**2*nC), 0.02219, "", "FORCED(boundary-reaching)", "K632"),
 ("m_t","mass","y_t=1 => m_t=v/sqrt2  (v is a FLOOR input)",
    v_higgs/math.sqrt(2), 172.69, "GeV", "FORCED-on-v (rests on vev floor)", "K591"),
 ("sinTh_C(Cabibbo)","CKM","N_c^2/(2^{N_c}*n_C) = 9/40",
    Nc**2/(2**Nc*nC), 0.2245, "", "CANDIDATE(two-point)", "F50"),
 ("V_cb","CKM","dual-rho form",
    0.0412, 0.0409, "", "STRUCTURAL", "F437"),
 ("V_ub","CKM","(1/N_c)^5 = (1/3)^5",
    (1/Nc)**5, 0.00369, "", "STRUCTURAL", "F437"),
 ("J_CKM(delta)","CKM","Jarlskog substrate form",
    3.0e-5, 3.08e-5, "", "CANDIDATE", "Vol2"),
 ("sin2_th12(PMNS)","PMNS","5/16 = n_C/rank^4 (or 3/10)",
    5/16, 0.307, "", "CANDIDATE(measurement-limited)", "L17"),
 ("sin2_th23(PMNS)","PMNS","upper-octant; no single forced form yet",
    0.5, 0.545, "", "STRUCTURAL(octant only)", "Thu-6/4"),
 ("m_d/m_e","mass","N_c^{+1}=3  [GJ GUT-scale texture, color-root parity]",
    Nc**1, 4.67/m_e, "ratio", "GUT-FREE mech / GUT-SCALE value (K641)", "K582/K641"),
 ("m_s/m_mu","mass","N_c^{-1}=1/3  [GJ GUT-scale]",
    Nc**-1, 93.4/m_mu, "ratio", "GUT-FREE mech / GUT-SCALE value (K641)", "K582/K641"),
 ("m_b/m_tau","mass","N_c^{0}=1  [GJ GUT-scale, b-tau unif]",
    Nc**0, 4180.0/m_tau, "ratio", "GUT-FREE mech / GUT-SCALE value (K641)", "K582/K641"),
 ("m_e","mass","6*pi^5*alpha^12*m_Planck (gravity route) OR mass unit",
    None, 0.5109989, "MeV", "CANDIDATE(rests on m_Planck)", "F66"),
 ("m_H","Higgs","lambda_H substrate form (dual route)",
    None, 125.25, "GeV", "CANDIDATE(form not pinned here)", "INV-4833"),
 ("vev_v","Higgs","pure scale -- open by scale-invariance",
    None, 246.22, "GeV", "FLOOR(Casey #9)", "Casey#9"),
 ("m_nu1","nu-mass","absolute scale = FLOOR; m3/m1 pi-free (forward falsifier)",
    None, None, "eV", "OPEN(falsifier only)", "K636"),
 ("m_nu2","nu-mass","pi-ful (K547 locus, forced form)",
    None, None, "eV", "OPEN", "K636"),
 ("m_nu3","nu-mass","pi-free; testable when masses pin",
    None, None, "eV", "OPEN", "K636"),
 ("delta_PMNS","PMNS","not addressed",
    None, None, "rad", "OPEN", "-"),
 ("alpha_s","gauge","RG-runner -- not a fixed constant",
    None, 0.1179, "", "NEG(runs)", "honest-neg"),
 ("sin2_thW","gauge","RG-runner -- not a fixed constant (3/8 was forbidden GUT)",
    None, 0.23122, "", "NEG(runs)", "honest-neg"),
 ("m_u","mass","up-sector convention-contaminated",
    None, 2.16, "MeV", "NEG(scheme)", "Elie4526"),
 ("m_c","mass","charm not banked (scheme-trap)",
    None, 1270.0, "MeV", "NEG(scheme)", "K639"),
]

def dev(b,e):
    if b is None or e is None: return None
    if e==0: return 0.0 if b==0 else None   # exact-zero match (e.g. theta_QCD)
    return abs(b-e)/abs(e)*100

def status(b,e,mech):
    if "NEG" in mech: return "NEG"
    if "FLOOR" in mech: return "FLOOR"
    d = dev(b,e)
    if d is None: return "OPEN"
    if d <= 0.1: return "DONE"
    if d < 1.0: return "SOLID"
    return "MISS"

def scorecard():
    order={"DONE":0,"SOLID":1,"MISS":2,"OPEN":3,"FLOOR":4,"NEG":5}
    rows=sorted(ROWS, key=lambda r: order[status(r[3],r[4],r[6])])
    print("="*100)
    print("BST ALMANAC SCORECARD  (status COMPUTED from match: DONE<=0.1%, SOLID<1%, MISS>=1%; PDG RE-PIN)")
    print("="*100)
    print(f"{'param':16s} {'BST value':>12s} {'expected':>12s} {'dev%':>7s}  {'STATUS':6s} {'mechanism':22s}")
    print("-"*100)
    from collections import Counter
    tc=Counter()
    for par,sec,der,b,e,u,mech,prov in rows:
        st=status(b,e,mech); tc[st]+=1
        d=dev(b,e); ds=f"{d:6.3f}" if d is not None else "   -  "
        bs=f"{b:12.6g}" if b is not None else "     -      "
        es=f"{e:12.6g}" if e is not None else "     -      "
        print(f"{par:16s} {bs} {es} {ds:>7s}  {st:6s} {mech[:22]:22s}")
    print("-"*100)
    print("TALLY:", dict(tc))
    done=tc['DONE']; solid=tc['SOLID']
    print(f"\n  DONE  (<=0.1% match): {tc['DONE']:2d}   SOLID (<1%): {tc['SOLID']:2d}   "
          f"MISS (>=1%): {tc['MISS']:2d}   OPEN: {tc['OPEN']:2d}   FLOOR: {tc['FLOOR']:2d}   NEG: {tc['NEG']:2d}")
    print(f"  => MATCHING (DONE+SOLID): {done+solid} of 26.  But check the mechanism column:")
    print(f"     a SOLID/DONE match with a GATED/CANDIDATE mechanism is not finished -- both axes must be clean.")
    print(f"     Truly finished (DONE match AND FORCED mechanism): only theta_QCD today.")

def almanac():
    order={"DONE":0,"SOLID":1,"MISS":2,"OPEN":3,"FLOOR":4,"NEG":5}
    rows=sorted(ROWS, key=lambda r:(r[1], order[status(r[3],r[4],r[6])]))
    L=["# BST Almanac — where and how every SM value derives from the substrate",
       "",
       "*Generated from `play/bst_almanac.py` (single source of truth with the scorecard). "
       "Substrate primaries: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137. "
       "Status computed from match vs PDG (RE-PIN): DONE ≤0.1%, SOLID <1%, MISS ≥1%. "
       "`mechanism` is a separate axis — a match with an unforced mechanism is not finished.*",
       ""]
    cur=None
    for par,sec,der,b,e,u,mech,prov in rows:
        if sec!=cur:
            L.append(f"\n## {sec}\n"); cur=sec
        st=status(b,e,mech); d=dev(b,e)
        ds=f"{d:.3f}%" if d is not None else "—"
        bs=f"{b:.6g}" if b is not None else "—"
        es=f"{e:.6g}" if e is not None else "—"
        L.append(f"### {par}  ·  **{st}**")
        L.append(f"- **Derivation from substrate:** {der}")
        L.append(f"- **BST value:** {bs} {u}  |  **Expected (PDG):** {es} {u}  |  **Match:** {ds}")
        L.append(f"- **Mechanism:** {mech}  |  **Provenance:** {prov}")
        L.append("")
    import os
    out=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"notes","BST_Almanac.md")
    open(out,"w").write("\n".join(L))
    print("wrote", out, f"({len(rows)} entries)")

if __name__=="__main__":
    if "--almanac" in sys.argv: almanac()
    else: scorecard()
