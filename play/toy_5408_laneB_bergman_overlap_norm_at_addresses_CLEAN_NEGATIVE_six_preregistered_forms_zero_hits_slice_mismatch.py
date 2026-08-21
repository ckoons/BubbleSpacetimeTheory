import numpy as np
from mpmath import mp, mpf, gamma, beta, isnan, isinf
mp.dps=40
print("="*104)
print("TOY 5408 -- LANE B: the equal-norm gate via the BERGMAN OVERLAP NORM at {5/2, 3/2, 0}.")
print("  SPEC (@Lyra): object = ||f_nu||^2 on H^2(D_IV^5); ground norm ||f_0||^2 = G(5/2)^2/G(5)")
print("  = 3pi/128 = Beta(5/2,5/2). Test (Sum s)^2 / Sum s^2 = 3/2. NO measured masses in the pipeline.")
print("  *** PRE-REGISTERED: every candidate form is listed BEFORE computing, and ALL are reported. ***")
print("="*104)

print("\nTABLE 0 -- reconnect: the VALIDATED convention (T2529/F506), stated before use")
print("  F506: 'the FK generalized Pochhammer (nu)_lambda ... = 1/||kernel section||^2'")
print("  Down sector: nu = N_c = 3 FIXED, degrees lambda in {1,3,5} -> (3)_1,(3)_3,(3)_5")
for lam in (1,3,5):
    v=mpf(1)
    for i in range(lam): v*= (3+i)
    print("     (3)_%d = %s"%(lam,int(v)))
print("     -> 3 : 60 : 2520 = 1 : 20 : 840 ; m_s/m_d = 20. *** VALIDATED SLICE. ***")
print("  ★ NOTE THE SHAPE OF THAT SLICE: nu FIXED, DEGREE varying.")
print("  ★ THE LEPTON PROPOSAL VARIES nu INSTEAD -- a DIFFERENT slice of the same kernel (F741),")
print("    and F506 already records: 'charged LEPTONS do not follow at nu=N_c ... no single forced")
print("    nu fits them, so the down-quark hit is NOT a universal ladder.' Flagged, not fatal.")

g0=gamma(mpf(5)/2)**2/gamma(5)
print("\n  ground-norm check: G(5/2)^2/G(5) = %s ; 3pi/128 = %s -> %s"
      %(mp.nstr(g0,12),mp.nstr(3*mp.pi/128,12),"MATCH" if abs(g0-3*mp.pi/128)<mpf('1e-30') else "MISMATCH"))

nus=[mpf(5)/2, mpf(3)/2, mpf(0)]
r1=mpf(5)/2

def safe(fn):
    try:
        v=fn()
        if isnan(v) or isinf(v) or v<=0: return None
        return v
    except Exception: return None

FORMS={
 "F1  B(r1+nu, r1-nu)      symmetric shift": lambda n: safe(lambda: beta(r1+n, r1-n)),
 "F2  B(r1+nu, r1)         one-sided up":    lambda n: safe(lambda: beta(r1+n, r1)),
 "F3  B(r1-nu, r1)         one-sided down":  lambda n: safe(lambda: beta(r1-n, r1)),
 "F4  G(r1+nu)G(r1)/G(5+nu)":                lambda n: safe(lambda: gamma(r1+n)*gamma(r1)/gamma(5+n)),
 "F5  G(r1)G(r1)/G(5+nu)":                   lambda n: safe(lambda: gamma(r1)**2/gamma(5+n)),
 "F6  B(r1,r1) * (r1)_nu   rising factorial":lambda n: safe(lambda: beta(r1,r1)*gamma(r1+n)/gamma(r1)),
}
print("\nTABLE 1 -- *** THE PRE-REGISTERED FORMS, EVALUATED AT nu = {5/2, 3/2, 0} ***")
print("   (all reduce to B(5/2,5/2) at nu = 0 by construction; check that column)")
print("   form                                    ||f||^2 @5/2      @3/2          @0            @0 = 3pi/128?")
vals={}
for name,fn in FORMS.items():
    v=[fn(n) for n in nus]; vals[name]=v
    ok = (v[2] is not None) and abs(v[2]-g0)<mpf('1e-25')
    show=[("DIVERGES" if x is None else mp.nstr(x,7)) for x in v]
    print("   %-40s %-16s %-13s %-13s %s"%(name,show[0],show[1],show[2],"yes" if ok else "NO"))

print("\nTABLE 2 -- *** THE TEST: (Sum s)^2 / Sum s^2, TARGET 3/2 = 1.5 EXACTLY ***")
print("   Two amplitude conventions, both reported (T2529 has mass = (nu)_lam = 1/||sec||^2):")
print("     conv A: mass = ||f||^2      -> s = ||f||")
print("     conv B: mass = 1/||f||^2    -> s = 1/||f||")
def stat(s):
    s=[float(x) for x in s]
    return (sum(s)**2)/sum(x*x for x in s)
print("   form                                     conv A        conv B        hit 3/2?")
hits=[]
for name,v in vals.items():
    row=[]
    for conv in ("A","B"):
        if any(x is None for x in v): row.append(None); continue
        s=[mp.sqrt(x) for x in v] if conv=="A" else [1/mp.sqrt(x) for x in v]
        row.append(stat(s))
    a="DIVERGES" if row[0] is None else "%.6f"%row[0]
    b="DIVERGES" if row[1] is None else "%.6f"%row[1]
    hit=[c for c,x in zip("AB",row) if x is not None and abs(x-1.5)<1e-6]
    if hit: hits.append((name,hit))
    print("   %-40s %-13s %-13s %s"%(name,a,b,"*** "+",".join(hit)+" ***" if hit else "no"))

print("\n   reference points (no masses used):")
print("     addresses read directly, s = nu      : (Sum)^2/Sum^2 = %.6f   (needs 1.5)"%stat([float(x) for x in nus]))
print("     equal-norm target                    : 1.500000")

print("\nTABLE 3 -- why nu = 5/2 is the structural obstruction")
print("   r1 = 5/2, so nu = 5/2 sits exactly at the EDGE: B(r1+nu, r1-nu) = B(5, 0) = G(0) -> POLE.")
print("   *** The electron's address IS the edge of the Beta strip. *** Any symmetric-shift form")
print("   diverges there -- the same 'self-shadow zero' that killed the formal-degree route (Lyra),")
print("   reappearing as a POLE instead of a zero under the reciprocal convention.")
print("   ==> a finite triple requires a form that is regular at nu = r1, which the one-sided and")
print("       Gamma-ratio families are -- and those are the ones evaluated above.")

print("\n"+"="*104); print("VERDICT -- Lane B, Bergman overlap route"); print("="*104)
if not hits:
    print(" (1) ★★★ *** CLEAN NEGATIVE: NO pre-registered form hits 3/2. *** The equal-norm equality")
    print("     does NOT fall out of the Bergman overlap norm at the banked addresses, under either")
    print("     amplitude convention. Six forms, twelve evaluations, zero hits.")
else:
    print(" (1) *** HIT(S): %s -- report as CANDIDATE ONLY. *** Six forms were surveyed, so a single"%hits)
    print("     hit is weak evidence; it banks ONLY if the form is independently FORCED (see (4)).")
print()
print(" (2) *** THE SYMMETRIC-SHIFT FAMILY IS STRUCTURALLY EXCLUDED, not merely wrong: nu = 5/2 = r1")
print("     is the EDGE of the Beta strip, so B(r1+nu, r1-nu) has a POLE at the electron address. ***")
print("     Same self-shadow obstruction that killed the formal degree, in reciprocal form.")
print()
print(" (3) ★★ *** THE SLICE MISMATCH IS THE REAL FINDING, AND IT PRE-DATES THIS TOY: *** T2529 is")
print("     validated at FIXED nu with VARYING DEGREE ({1,3,5} at nu=3). The lepton proposal varies")
print("     nu at fixed degree -- a different slice of the kernel (F741), and F506 already recorded")
print("     'charged LEPTONS do not follow ... no single forced nu fits them.' *** The machinery is")
print("     validated where it was validated; the lepton evaluation is a genuine extrapolation. ***")
print()
print(" (4) *** WHAT WOULD MAKE THIS BANK (unchanged from 5407): the nu-dependence must be DERIVED")
print("     from the kernel, not selected from a menu. *** I surveyed six forms precisely so that")
print("     nobody -- including me -- can pick the one that lands and call it forced.")
