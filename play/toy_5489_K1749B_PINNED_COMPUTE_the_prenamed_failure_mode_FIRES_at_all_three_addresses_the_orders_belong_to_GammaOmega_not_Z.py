# TOY 5489 -- THE K1749-B PINNED COMPUTATION. Elie, 2026-08-24. Lane: External 3 (5487's target).
# Pin (Lyra, filed before any number): object = residues of ONE FK family; functional = K_j(0,0);
# rescaling EXPONENTS = the Gamma_Omega pole orders from MY 5456 (computed, not chosen);
# claim ORDINAL; ZERO per-support coefficients; failure modes PRE-NAMED, incl.
# "K_j(0,0) = 0 or infinity => report and stop -- a finding about the ORDERS, not a license to re-rescale."
from mpmath import mp, mpf, gamma, rf
import numpy as np
mp.dps=30
BAR="="*100
print(BAR); print("TOY 5489 -- K1749-B pinned compute: kernel-at-base of the residue measures"); print(BAR)

head=lambda s:(print("\n"+BAR),print(s),print(BAR))
head("PART A -- THE ONE-FAMILY MASS FUNCTION, and its GATE (everything hangs on this formula)")
print("  FK family, RAW (no coefficients anywhere): d mu_nu = h(z,zbar)^(nu-p) dV on D_IV^5,")
print("  p = genus = 5. Total mass Z(nu) = integral, FK closed form (tube type, r=2, a=3, d=5):")
print("     Z(nu) = pi^5 * Gamma_Om(nu - d/r)/Gamma_Om(nu),   Gamma_Om(x) ~ Gamma(x)Gamma(x - 3/2), d/r = 5/2")
print("  => Z(nu) = pi^5 [Gamma(nu-5/2)Gamma(nu-4)] / [Gamma(nu)Gamma(nu-3/2)]")
print("\n  GATE A1 (direction): h <= 1 on D with h(0)=1, so Z must DECREASE in nu. Formula ratio")
print("     Z(nu+1)/Z(nu) = (nu-5/2)(nu-4)/[nu(nu-3/2)] -- at nu=5: (2.5*1)/(5*3.5) = 1/7 < 1. OK")
print("  GATE A2 (MONTE CARLO on the actual Lie ball, the F740 integrand):")
rng=np.random.default_rng(5489)
N=4_000_000
z=(rng.uniform(-1,1,(N,5))+1j*rng.uniform(-1,1,(N,5)))
zz=np.abs((z*z).sum(1)); nz=(np.abs(z)**2).sum(1)
h=1-2*nz+zz**2
inD=(h>0)&(zz<1)&(nz<1)          # the Lie ball
hin=h[inD]
mc=hin.mean()                     # = Z(6)/Z(5) since ratio of integrals over same domain
print("     samples in domain: %d of %d (%.2f%%)"%(inD.sum(),N,100*inD.sum()/N))
print("     MC  Z(6)/Z(5) = mean h over Lie ball = %.4f"%mc)
print("     FORMULA        = 1/7               = %.4f   -> %s"%(1/7.0,"GATE PASS" if abs(mc-1/7)<0.02 else "*** GATE FAIL ***"))
if abs(mc-1/7)>=0.02: raise SystemExit("mass-formula gate failed; nothing below is read")

head("PART B -- THE PINNED EXPONENTS (from my 5456, reproduced here) vs Z's OWN orders")
def ord_at(f,x0):
    # numeric order of f at x0: f ~ C (x-x0)^(-k); estimate k from two epsilons
    e1,e2=mpf('1e-6'),mpf('1e-8')
    try:
        v1,v2=f(x0+e1),f(x0+e2)
        import math
        k=float(mp.log(abs(v1)/abs(v2))/mp.log(e2/e1))
        return round(k)
    except Exception: return None
GO=lambda nu: gamma(nu)*gamma(nu-mpf(3)/2)
Z =lambda nu: gamma(nu-mpf(5)/2)*gamma(nu-4)/(gamma(nu)*gamma(nu-mpf(3)/2))   # pi^5 dropped (ordinal claim)
print("   address    ord Gamma_Om(nu)  [5456 -> PINNED k_j]     ord Z(nu)  [NOT pinned]")
for nu,name in ((mpf(5)/2,"electron 5/2"),(mpf(3)/2,"muon 3/2"),(mpf(0),"tau 0")):
    kGO=ord_at(GO,nu); kZ=ord_at(Z,nu)
    print("   %-10s pole order %-2s -> k_j = %-2s              pole order %s"%(name,kGO,kGO,kZ))
print("   *** THE TWO ORDER SETS DISAGREE AT EVERY ADDRESS: Gamma_Om orders (0,1,1) vs Z orders (1,0,0). ***")

head("PART C -- THE PINNED EVALUATION. K_j(0,0) = 1/mass_j, mass_j = lim (nu-nu_j)^{k_j} Z(nu), k_j PINNED")
for nu,k,name in ((mpf(5)/2,0,"electron"),(mpf(3)/2,1,"muon"),(mpf(0),1,"tau")):
    e=mpf('1e-10')
    m=(e**k)*Z(nu+e)
    if abs(m)>mpf('1e6'): K="0 (mass diverges)"
    elif abs(m)<mpf('1e-6'): K="INFINITY (mass -> 0 under the pinned rescale)"
    else: K=mp.nstr(1/m,8)
    print("   %-9s k_j = %d :  mass ~ %-12s =>  K_j(0,0) = %s"%(name,k,mp.nstr(m,4),K))
print("\n   *** K = (0, inf, inf). THE PIN'S PRE-NAMED FAILURE MODE FIRES AT ALL THREE ADDRESSES. ***")

head("VERDICT -- per the pin's own clause: REPORT AND STOP")
print(""" (1) The lane STOPS here. No ordering was computed; the ordinal claim is NOT scored; the
     down-quark must-fail was NOT run (the pipeline died upstream of it); the tripwire was NOT
     tripped (zero coefficients were introduced -- the failure is in the pinned EXPONENTS).
 (2) THE FINDING, which the failure mode names: the pinned exponents are the pole orders of
     Gamma_Om(nu) -- the NORM/K-type degeneration function (my 5456). The MASS continuation
     Z(nu) = pi^5 Gamma_Om(nu-5/2)/Gamma_Om(nu) carries Gamma_Om at TWO shifted arguments, and
     ITS orders at the addresses are (1, 0, 0) -- disagreeing with (0, 1, 1) EVERYWHERE.
     *** "THE Gamma_Om POLE ORDER" WAS ONE NAME DOING TWO JOBS -- ord_GO(nu) vs ord_Z(nu).
     The nineteenth same-name-collision shape, caught by the failure mode the pin pre-named. ***
 (3) What I did NOT do, on pain of voiding the pin: I did NOT re-rescale with Z's own orders and
     compute "fixed" kernels -- that is exactly "revised after numbers return." Z's orders are
     REPORTED as the diagnosis; using them is a NEW pin, Lyra's to file or decline.
 (4) One physical note for her refile decision, stated as observation not advocacy: Z's order-1
     pole at nu = 5/2 = d/r is the CLASSICAL Hardy transition -- the residue there is the Shilov
     SURFACE measure. Under Z-orders the electron would itself be a boundary-residue object.
     Whether that is the right family is precisely what a fresh pin would decide.
 (5) 5487's shot: STILL A SHAPE, neither landed nor dead -- the mechanism test never ran.
     Nothing banked. One CI (me); Grace is the named second on whatever Lyra refiles.""")
