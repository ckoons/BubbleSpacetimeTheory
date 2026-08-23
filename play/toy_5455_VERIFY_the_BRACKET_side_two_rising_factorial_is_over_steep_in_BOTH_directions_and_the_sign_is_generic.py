# TOY 5455 -- VERIFY the BRACKET, SIDE TWO (Keeper, R63 Section 1).
# Elie, 2026-08-23. Rubric cell: External 3 (SM params) / lepton hierarchy.
#
# SCOPE: I verify Keeper's numbers and test the ROBUSTNESS OF HIS SIGN. I do NOT touch the
# residue gate -- that is pinned behind Lyra's object+exponent pin (R63 Sec 1 rule 1), and I
# compute only after the pin is filed.
#
# WHY THIS, NOW: Keeper's SIDE TWO is a NEW banked claim carrying load-bearing numbers
# (nu_lep = 12.888130, predicted m_tau/m_e = 55,480.23, miss 16.0x). My 5454 supplies SIDE ONE.
# A bracket is only as good as its weaker side, and nobody has checked side two.
#
# THREE THINGS I OWE IT:
#   (A) reproduce his numbers exactly;
#   (B) run the test in the OTHER DIRECTION -- he fixed nu on the muon and predicted the tau.
#       Reporting one direction of a two-target test is a SELECTION unless the other is shown.
#   (C) test whether "OVER-steep" is GENERIC to the rising factorial or specific to degrees {1,3,5}.
#       If it flips sign on some admissible pattern, the bracket's second side is scoped to {1,3,5},
#       not to "the degree axis" -- and the claim's wording must carry that.
#       *** This is a SCOPE CHECK on a banked claim, NOT a hunt for a hit (K1684). I report the
#           FULL enumeration and I claim NO pattern as a result, whatever lands. ***

from mpmath import mp, mpf, findroot
import itertools
mp.dps = 40

BAR="="*104
def head(s): print("\n"+BAR); print(s); print(BAR)

# --- measured inputs, stated plainly as inputs (PDG) ---
M_E   = mpf('0.51099895000')     # MeV
M_MU  = mpf('105.6583755')       # MeV
M_TAU = mpf('1776.86')           # MeV
R_MU  = M_MU/M_E
R_TAU = M_TAU/M_E

print(BAR)
print("TOY 5455 -- VERIFYING THE BRACKET, SIDE TWO. Keeper's rising-factorial forward test.")
print("  I supply SIDE ONE (5454). Nobody has checked SIDE TWO. A bracket is only as good as")
print("  its weaker side. Not touching the residue gate -- that waits on Lyra's pin.")
print(BAR)
print("\n  MEASURED INPUTS (stated as inputs, not derived):")
print("     m_e   = %s MeV     m_mu = %s MeV     m_tau = %s MeV"%(M_E,M_MU,M_TAU))
print("     m_mu/m_e  = %s"%mp.nstr(R_MU,10))
print("     m_tau/m_e = %s"%mp.nstr(R_TAU,10))

def poch(nu, lam):
    """rising factorial (nu)_lam = nu(nu+1)...(nu+lam-1)"""
    v = mpf(1)
    for i in range(int(lam)): v *= (nu + i)
    return v

# =====================================================================
head("PART A -- REPRODUCE THE QUARK ANCHOR, then Keeper's lepton forward test")
print("  Quark ladder (T2529/T2572): nu_W = N_c = 3 FIXED, degrees lambda in {1,3,5}.")
for lam in (1,3,5):
    print("     (3)_%d = %s"%(lam, int(poch(mpf(3),lam))))
q1,q3,q5 = poch(mpf(3),1), poch(mpf(3),3), poch(mpf(3),5)
print("     -> %s : %s : %s  =  1 : %s : %s     m_s/m_d = %s  ANCHOR REPRODUCED"
      %(int(q1),int(q3),int(q5),int(q3/q1),int(q5/q1),int(q3/q1)))

print("\n  Same STRUCTURE on leptons, nu floating. Ratios at degrees {1,3,5}:")
print("     r2(nu) := (nu)_3/(nu)_1 = (nu+1)(nu+2)")
print("     r3(nu) := (nu)_5/(nu)_1 = (nu+1)(nu+2)(nu+3)(nu+4)")
def r2(nu): return poch(nu,3)/poch(nu,1)
def r3(nu): return poch(nu,5)/poch(nu,1)

nu_from_mu = findroot(lambda n: r2(n)-R_MU, mpf('12'))
pred_tau   = r3(nu_from_mu)
print("\n  *** KEEPER'S DIRECTION -- fix nu on the MUON, predict the TAU: ***")
print("     nu_lep from (nu+1)(nu+2) = %s   ->  nu = %s"%(mp.nstr(R_MU,10), mp.nstr(nu_from_mu,10)))
print("        Keeper reported 12.888130   -> %s"%("MATCH" if abs(nu_from_mu-mpf('12.888130'))<mpf('1e-5') else "MISMATCH"))
print("     PREDICTED m_tau/m_e = %s"%mp.nstr(pred_tau,10))
print("        Keeper reported 55,480.23   -> %s"%("MATCH" if abs(pred_tau-mpf('55480.23'))<mpf('1') else "MISMATCH (see below)"))
print("     OBSERVED  m_tau/m_e = %s"%mp.nstr(R_TAU,10))
print("     MISS FACTOR = %s x   (Keeper reported 16.0x)"%mp.nstr(pred_tau/R_TAU,6))

# =====================================================================
head("PART B -- THE OTHER DIRECTION. One direction of a two-target test is a SELECTION.")
print("  Keeper fixed nu on the muon. The test is equally well run the other way, and an honest")
print("  two-target report shows BOTH -- otherwise the reported miss is the one that was looked at.")
nu_from_tau = findroot(lambda n: r3(n)-R_TAU, mpf('3'))
pred_mu     = r2(nu_from_tau)
print("\n  *** REVERSE -- fix nu on the TAU, predict the MUON: ***")
print("     nu_lep from (nu+1)(nu+2)(nu+3)(nu+4) = %s  ->  nu = %s"
      %(mp.nstr(R_TAU,10), mp.nstr(nu_from_tau,10)))
print("     PREDICTED m_mu/m_e = %s"%mp.nstr(pred_mu,10))
print("     OBSERVED  m_mu/m_e = %s"%mp.nstr(R_MU,10))
print("     MISS FACTOR = %s x"%mp.nstr(pred_mu/R_MU,6))
print("\n  *** BOTH DIRECTIONS MISS, AND BOTH MISS IN THE SAME SENSE (the model is too steep):")
print("      forward  over-predicts the FAR rung by %sx"%mp.nstr(pred_tau/R_TAU,6))
print("      reverse  under-predicts the NEAR rung by %sx (= too steep, read from the far end)"
      %mp.nstr(R_MU/pred_mu,6))
print("      A two-sided miss with a CONSISTENT SENSE is a real structural statement. ***")

print("\n  Best simultaneous fit (the kindest possible reading -- minimize max log-ratio error):")
def maxerr(nu):
    if nu<=0: return mpf(1e9)
    e1 = abs(mp.log(r2(nu)/R_MU)); e2 = abs(mp.log(r3(nu)/R_TAU))
    return max(e1,e2)
best=None
for k in range(1,4000):
    nu=mpf(k)/mpf(200)
    e=maxerr(nu)
    if best is None or e<best[1]: best=(nu,e)
nb=best[0]
print("     nu_best = %s  ->  m_mu/m_e = %s (obs %s), m_tau/m_e = %s (obs %s)"
      %(mp.nstr(nb,6), mp.nstr(r2(nb),8), mp.nstr(R_MU,8), mp.nstr(r3(nb),8), mp.nstr(R_TAU,8)))
print("     best achievable worst-case miss = %s x   *** EVEN THE BEST FIT CANNOT RESCUE IT ***"
      %mp.nstr(mp.e**best[1],6))

# =====================================================================
head("PART C -- IS 'OVER-STEEP' GENERIC, OR SPECIFIC TO DEGREES {1,3,5}?")
print("  SCOPE CHECK on a banked claim, NOT a hunt (K1684). Full enumeration reported; I claim")
print("  NO pattern as a result whatever lands. The question is only whether Keeper's wording")
print("  ('at the quark's odd-degree pattern') is doing real work or is decoration.")
print()
print("  For an increasing degree triple {a<b<c} the model is: fix nu on m_mu/m_e via")
print("  (nu)_b/(nu)_a, then predict m_tau/m_e via (nu)_c/(nu)_a. Report the miss factor.")
print()
print("   degrees      nu solved      predicted m_tau/m_e   miss factor    direction")
rows=[]
for a,b,c in itertools.combinations(range(1,10),3):
    try:
        f = lambda n: poch(n,b)/poch(n,a) - R_MU
        nu = findroot(f, mpf('5'))
        if nu <= 0: continue
        pt = poch(nu,c)/poch(nu,a)
        mf = pt/R_TAU
        rows.append((a,b,c,nu,pt,mf))
    except Exception:
        continue
for a,b,c,nu,pt,mf in rows:
    d = "OVER-steep" if mf>1 else "UNDER-steep"
    star = " <-- quark pattern" if (a,b,c)==(1,3,5) else ""
    print("   {%d,%d,%d}%s   %-13s %-21s %-14s %s%s"
          %(a,b,c," "*(2), mp.nstr(nu,7), mp.nstr(pt,8), mp.nstr(mf,6), d, star))
over  = [r for r in rows if r[5]>1]
under = [r for r in rows if r[5]<=1]
print("\n   FULL SWEEP: %d admissible triples from degrees 1..9. OVER-steep: %d. UNDER-steep: %d."
      %(len(rows), len(over), len(under)))
if under:
    print("   *** THE SIGN IS NOT GENERIC. Keeper's scope ('at the quark's odd-degree pattern') is")
    print("       LOAD-BEARING and must stay in the claim. Under-steep patterns exist: %s"
          %", ".join("{%d,%d,%d}"%(a,b,c) for a,b,c,_,_,_ in under[:8]))
else:
    print("   *** THE SIGN IS GENERIC across every admissible triple tested: the rising factorial")
    print("       CANNOT be flat enough for the lepton pair, at ANY degree pattern in 1..9. ***")
    print("       That STRENGTHENS side two from a statement about {1,3,5} to a statement about")
    print("       the rising factorial itself -- which is what the bracket actually needs.")
best_mf = min(rows, key=lambda r: abs(mp.log(r[5])))
print("\n   closest any triple gets: {%d,%d,%d} at miss %s x  (still not a fit, and NOT claimed as one)"
      %(best_mf[0],best_mf[1],best_mf[2],mp.nstr(best_mf[5],6)))

# =====================================================================
head("VERDICT -- SIDE TWO of the bracket")
print(" (1) KEEPER'S NUMBERS REPRODUCE. nu_lep = %s (he reported 12.888130);"%mp.nstr(nu_from_mu,10))
print("     predicted m_tau/m_e = %s (he reported 55,480.23); miss %s x (he reported 16.0x)."
      %(mp.nstr(pred_tau,9), mp.nstr(pred_tau/R_TAU,5)))
print()
print(" (2) THE TEST SURVIVES BEING RUN BACKWARDS, which he did not report and which it owed.")
print("     Reverse direction misses by %s x, in the SAME SENSE (too steep)."%mp.nstr(R_MU/pred_mu,6))
print("     Best simultaneous fit still misses by %s x. *** The miss is not a direction artefact. ***"
      %mp.nstr(mp.e**best[1],6))
print()
print(" (3) SCOPE: sign is %s across the %d-triple enumeration."
      %("GENERIC" if not under else "NOT generic", len(rows)))
print()
print(" (4) SIDE TWO STANDS. Combined with 5454's side one (nu axis bounded, amplitude ratio 22.96")
print("     needed, 8/8 miss HIGH), the bracket is real and has numbers on both sides.")
print()
print(" (5) WHAT I DID NOT DO: the residue gate. It is pinned behind Lyra's {object} x {exponent}")
print("     pin (R63 Sec 1 rule 1) and I compute only after that pin is FILED. No degree pattern")
print("     above is claimed as a mechanism -- Part C is a scope check on a banked claim, and its")
print("     full enumeration is printed precisely so nobody (including me) can pick the closest.")
print("     Nothing pushed. CP existence-only.")
