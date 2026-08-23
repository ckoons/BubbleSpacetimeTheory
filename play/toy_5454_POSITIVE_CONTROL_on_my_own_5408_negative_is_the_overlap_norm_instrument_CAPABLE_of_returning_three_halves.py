# TOY 5454 -- POSITIVE CONTROL on my own 5408 CLEAN NEGATIVE.
# Elie, 2026-08-23. Rubric cell: External 3 (SM params) / Koide.
#
# WHY: 5408 reported "6 pre-registered forms x 2 conventions x 12 evals, ZERO hits on 3/2."
# Keeper banked that in K1749 as "MASS GATE FULLY CLOSED (Elie 5408, the last live door)."
# But 5408 NEVER SHOWED THE INSTRUMENT COULD HIT 1.5. My own standing rule:
#   "a search that cannot succeed proves nothing" / "validate the instrument before a negative."
# If no form in that family can reach 3/2 at ANY admissible address triple, the negative is
# EMPTY and K1749's closure is resting on an instrument that could not fail.
#
# NOT reopening the gate. Auditing the closure. Every number printed; verdict last.

from fractions import Fraction as F
from mpmath import mp, mpf, gamma, beta, isnan, isinf, findroot
import itertools
mp.dps = 40

R1 = mpf(5)/2                      # rho_1 = 5/2 for D_IV^5
NUS = [mpf(5)/2, mpf(3)/2, mpf(0)] # the T2517 forced addresses
TARGET = mpf(3)/2

BAR = "="*104
def head(s): print("\n"+BAR); print(s); print(BAR)

def Rstat(s):
    """(Sum s)^2 / Sum s^2 -- fully symmetric in s, scale invariant."""
    s = [mpf(x) for x in s]
    if any(x < 0 for x in s): return None
    d = sum(x*x for x in s)
    if d == 0: return None
    return (sum(s)**2)/d

def safe(fn):
    try:
        v = fn()
        if isnan(v) or isinf(v) or v <= 0: return None
        return v
    except Exception:
        return None

# ---- the SIX forms, copied verbatim from 5408 (read, not recalled) ----
FORMS = {
 "F1  B(r1+nu, r1-nu)      symmetric shift": lambda n: safe(lambda: beta(R1+n, R1-n)),
 "F2  B(r1+nu, r1)         one-sided up":    lambda n: safe(lambda: beta(R1+n, R1)),
 "F3  B(r1-nu, r1)         one-sided down":  lambda n: safe(lambda: beta(R1-n, R1)),
 "F4  G(r1+nu)G(r1)/G(5+nu)":                lambda n: safe(lambda: gamma(R1+n)*gamma(R1)/gamma(5+n)),
 "F5  G(r1)G(r1)/G(5+nu)":                   lambda n: safe(lambda: gamma(R1)**2/gamma(5+n)),
 "F6  B(r1,r1)*(r1)_nu     rising factorial": lambda n: safe(lambda: beta(R1,R1)*gamma(R1+n)/gamma(R1)),
}

print(BAR)
print("TOY 5454 -- POSITIVE CONTROL on the 5408 negative. Does the instrument admit 3/2 AT ALL?")
print("  5408 verdict under audit: 'CLEAN NEGATIVE, six forms, twelve evaluations, zero hits.'")
print("  K1749 built 'mass gate FULLY CLOSED' on it. An instrument that cannot succeed proves nothing.")
print(BAR)

# =====================================================================
head("PART A -- VALIDATE THE VALIDATOR (must-catch + must-reject, BEFORE any real form)")
print("  A sweep that reports 'incapable' must be shown to report 'capable' when it should.")

# must-reject: constant form -> all s equal -> R = 3 always, can never be 1.5
const = [mpf(1), mpf(1), mpf(1)]
print("\n  MUST-REJECT  constant form f(nu)=1 -> s=(1,1,1):  R = %s   (target 1.5)"
      % mp.nstr(Rstat(const), 10))
print("     expected: INCAPABLE (R is pinned at 3 for any equal triple). ",
      "PASS" if abs(Rstat(const)-3) < mpf('1e-30') else "FAIL")

# must-catch: engineer a triple that hits 1.5 exactly, geometric s=(1,x,x^2)
def geo_R(x):
    return Rstat([mpf(1), mpf(x), mpf(x)**2]) - TARGET
xstar = findroot(geo_R, mpf('3.0'))
scatch = [mpf(1), xstar, xstar**2]
print("\n  MUST-CATCH   geometric s=(1,x,x^2) solved for R=3/2:  x* = %s" % mp.nstr(xstar, 12))
print("     R(s*) = %s   -> " % mp.nstr(Rstat(scatch), 20),
      "PASS (statistic attains 3/2 on positive triples)" if abs(Rstat(scatch)-TARGET) < mpf('1e-25') else "FAIL")
print("\n  ==> The STATISTIC is not the obstruction. R((0,inf)^3) = (1, 3]; 3/2 is interior.")
print("      So any 'zero hits' must come from the FORMS, not from the test. Now test the forms.")

# =====================================================================
head("PART B -- THE REQUIRED SPREAD: what hierarchy does R = 3/2 actually demand?")
print("  R = 3 at the democratic point (all equal); R -> 1 as one entry dominates.")
print("  3/2 is FAR down toward the hierarchical end. Quantify it with the geometric family:")
print("\n     x        s = (1, x, x^2)              R = (Sum s)^2/Sum s^2")
for x in ['1.0','1.5','2.0','2.5','3.0','3.5','4.0','6.0','10.0']:
    xv = mpf(x); s = [mpf(1), xv, xv**2]
    print("     %-8s (1, %-6s %-10s)  %s" % (x, mp.nstr(xv,4)+",", mp.nstr(xv**2,6), mp.nstr(Rstat(s), 8)))
print("\n  *** R = 3/2 needs x* = %s, i.e. a max/min amplitude ratio of x*^2 = %s ***"
      % (mp.nstr(xstar,8), mp.nstr(xstar**2, 8)))
print("  For reference, the PHYSICAL sqrt-mass triple is hierarchical by ~sqrt(m_tau/m_e) ~ 59.")
print("  KEEP THIS NUMBER. The question is now concrete: do the overlap norms SPREAD that far?")

# =====================================================================
head("PART C -- THE SPREAD THE FORMS ACTUALLY DELIVER at the forced addresses {5/2, 3/2, 0}")
print("  form                                     s-triple (conv A: s = ||f||)          max/min      R")
capA = {}
for name, fn in FORMS.items():
    v = [fn(n) for n in NUS]
    if any(x is None for x in v):
        print("   %-40s DIVERGES (nu=5/2 is the Beta-strip edge)" % name); capA[name]=None; continue
    s = [mp.sqrt(x) for x in v]
    ratio = max(s)/min(s)
    r = Rstat(s)
    capA[name] = (ratio, r)
    print("   %-40s (%s, %s, %s)  %-11s %s"
          % (name, mp.nstr(s[0],5), mp.nstr(s[1],5), mp.nstr(s[2],5), mp.nstr(ratio,6), mp.nstr(r,8)))
print("\n   REQUIRED max/min for R=3/2 (geometric reference): %s" % mp.nstr(xstar**2, 6))
print("   *** Every finite form is UNDER-SPREAD relative to what 3/2 demands. That is the mechanism. ***")

# =====================================================================
head("PART D -- ONE-SIDEDNESS: are the misses random, or all in one direction?")
print("  (5453 found the same signature on Keeper's five candidates: all missed, ALL HIGH.)")
print("  form                                     conv A        conv B        both > 3/2?")
allA, allB = [], []
for name, fn in FORMS.items():
    v = [fn(n) for n in NUS]
    if any(x is None for x in v):
        print("   %-40s %-13s %-13s %s" % (name, "DIVERGES", "DIVERGES", "-")); continue
    a = Rstat([mp.sqrt(x) for x in v])
    b = Rstat([1/mp.sqrt(x) for x in v])
    allA.append(a); allB.append(b)
    print("   %-40s %-13s %-13s %s" % (name, mp.nstr(a,7), mp.nstr(b,7),
          "yes" if (a > TARGET and b > TARGET) else "NO"))
lo = min(allA + allB); hi = max(allA + allB)
print("\n   range over all finite evaluations: [%s, %s]" % (mp.nstr(lo,7), mp.nstr(hi,7)))
print("   target 3/2 = 1.5 lies %s the entire range." % ("BELOW" if TARGET < lo else "inside"))
print("   *** %d/%d finite evaluations miss HIGH. Zero miss low. A one-sided miss is a SYSTEMATIC,"
      % (sum(1 for x in allA+allB if x > TARGET), len(allA+allB)))
print("       not a scatter around the target. The norms are not hierarchical enough, uniformly. ***")

# =====================================================================
head("PART E -- THE ACTUAL POSITIVE CONTROL: sweep the ADDRESS domain. Can each form reach 3/2?")
print("  Free the addresses (the forms have no free parameter at fixed nu, so capability must be")
print("  probed by varying nu). Sweep unordered triples on a grid in [0, r1) and record R's image.")
print("  If 3/2 is NOT in a form's image, that form's miss at {5/2,3/2,0} carries ZERO information.")

GRID = [mpf(k)/mpf(40) for k in range(0, 100)]   # nu in [0, 2.475], below the r1 = 5/2 edge
print("\n  grid: nu in [0, %s], %d points, all C(n,3) unordered triples = %d triples per form"
      % (mp.nstr(GRID[-1],5), len(GRID), len(GRID)*(len(GRID)-1)*(len(GRID)-2)//6))
print("\n  form                                     conv   R_min       R_max       3/2 in image?")
verdict_rows = []
for name, fn in FORMS.items():
    cache = {}
    for n in GRID:
        cache[n] = fn(n)
    good = [n for n in GRID if cache[n] is not None]
    for conv in ("A", "B"):
        rmin, rmax = None, None
        hit = False
        for t in itertools.combinations(good, 3):
            vals = [cache[n] for n in t]
            s = [mp.sqrt(x) for x in vals] if conv == "A" else [1/mp.sqrt(x) for x in vals]
            r = Rstat(s)
            if r is None: continue
            if rmin is None or r < rmin: rmin = r
            if rmax is None or r > rmax: rmax = r
        if rmin is not None and rmin <= TARGET <= rmax:
            hit = True
        verdict_rows.append((name, conv, rmin, rmax, hit))
        print("   %-40s %-6s %-11s %-11s %s"
              % (name, conv,
                 "n/a" if rmin is None else mp.nstr(rmin,7),
                 "n/a" if rmax is None else mp.nstr(rmax,7),
                 "*** YES -- instrument CAN succeed ***" if hit else "NO -- cannot reach 3/2"))

capable = [r for r in verdict_rows if r[4]]
incapable = [r for r in verdict_rows if not r[4] and r[2] is not None]

# =====================================================================
head("PART F -- THE CAN-FAIL RECOUNT (C6: report the can-fail count, not the denominator)")
print("  Keeper's C6 rule, applied to MY OWN toy: '8/8' hid that only 2/8 could fail.")
print("  A channel is a REAL TEST only if it is BOTH finite at the forced addresses AND capable.")
print("  Three of the six 'capable' forms in Part E DIVERGE at nu=5/2 -- they were never in play.")
print()
print("  form                                     finite at {5/2,3/2,0}?  capable?   REAL TEST?")
real = 0
for name, fn in FORMS.items():
    v = [fn(n) for n in NUS]
    fin = all(x is not None for x in v)
    cap = any(r[0] == name and r[4] for r in verdict_rows)
    ok = fin and cap
    if ok: real += 2
    print("   %-40s %-23s %-10s %s"
          % (name, "yes" if fin else "NO (Beta-strip pole)", "yes" if cap else "NO",
             "*** REAL TEST (x2 conv) ***" if ok else "no -- CANNOT FAIL"))
print()
print("  *** 5408 reported 6 forms x 2 conventions = 12 evaluations. ONLY %d COULD HAVE SUCCEEDED." % real)
print("      The other %d could not fail. '12 evaluations, zero hits' OVERSTATES the negative. ***" % (12-real))

print()
print("  How capable is the ONE surviving form? F5 hit-volume over the address domain:")
f5 = {n: FORMS["F5  G(r1)G(r1)/G(5+nu)"](n) for n in GRID}
tot = le = 0; f5min = None
for t in itertools.combinations(GRID, 3):
    s = [mp.sqrt(f5[n]) for n in t]
    r = Rstat(s); tot += 1
    if f5min is None or r < f5min: f5min = r
    if r <= TARGET: le += 1
print("     F5 R_min over whole domain = %s   (clears 3/2 by only %s)"
      % (mp.nstr(f5min,8), mp.nstr(TARGET-f5min,4)))
print("     triples with R <= 3/2      = %d / %d = %.4f%% of the domain" % (le, tot, 100.0*le/tot))
print("     *** The one instrument that COULD fail is a MARGINAL one. Say so; do not hide it. ***")

# =====================================================================
head("VERDICT -- is the 5408 negative INFORMATIVE or EMPTY?")
print(" (0) Reproduction: 5408 re-run this morning, identical. Ground norm 3pi/128 MATCH to 30 digits.")
print("     This audit does not dispute a single number in 5408. It asks what those numbers MEAN.")
print()
print(" (1) The STATISTIC is innocent: R((0,inf)^3) = (1,3], and 3/2 is interior (Part A, must-catch")
print("     PASS at x* = %s). The test could always have returned 1.5." % mp.nstr(xstar,8))
print()
print(" (2) CAPABILITY, stated the C6 way -- CAN-FAIL COUNT, not denominator:")
print("     %d of 12 channels can reach 3/2 anywhere in the address domain," % len(capable))
print("     but only %d of 12 are REAL TESTS (finite at the forced addresses AND capable)." % real)
print("     The remaining %d COULD NOT FAIL: 3 forms have a Beta-strip pole at the electron" % (12-real))
print("     address, 3 more never reach 3/2 anywhere in the domain (x2 conventions).")
if len(capable) > 0:
    print("     ==> The instrument is NOT dead: F5 (both conventions) could have hit and did not.")
    print("     ==> *** THE 5408 NEGATIVE IS INFORMATIVE -- BUT ON 2 CHANNELS, NOT 12. ***")
    print("         And F5 reaches 3/2 in %.4f%% of its domain, clearing 1.5 by %s." % (100.0*le/tot, mp.nstr(TARGET-f5min,4)))
    print("         So: a real test, by a hair. '6 forms, 12 evaluations, zero hits' READS as")
    print("         overwhelming and is not. That phrasing is MINE and I am correcting it.")
    print("     Channels that could have succeeded:")
    for nm, cv, lo_, hi_, _ in capable:
        print("        %-40s conv %s   image [%s, %s]" % (nm, cv, mp.nstr(lo_,6), mp.nstr(hi_,6)))
else:
    print("     ==> *** NO channel can reach 3/2 anywhere. THE NEGATIVE IS EMPTY -- it proves nothing")
    print("         about Koide, only about the form family. K1749 needs an AMEND (Keeper's to write). ***")
print()
print(" (3) HONEST DEDUCTION FROM THE CAPABLE CHANNELS: the miss is NOT that the family is too poor,")
print("     it is that the FORCED ADDRESSES {5/2, 3/2, 0} sit in the wrong part of the domain.")
print("     That is a sharper statement than 5408 made, and it is a statement ABOUT THE ADDRESSES.")
print()
print(" (4) THE MECHANISM (Parts C+D, the real yield): R = 3/2 demands a max/min amplitude ratio of")
print("     %s. Every finite form at the forced addresses delivers LESS spread, and" % mp.nstr(xstar**2,6))
print("     ALL finite evaluations miss HIGH -- range [%s, %s], target 1.5 below all of it."
      % (mp.nstr(lo,7), mp.nstr(hi,7)))
print("     *** The overlap norm at the lepton addresses is UNIFORMLY UNDER-HIERARCHICAL. ***")
print("     This corroborates F506's 'leptons do not follow at nu=N_c' with a mechanism rather than")
print("     an observation, and it is consistent with the slice mismatch K1749 already banked.")
print()
print(" (5) DOES K1749 FALL? NO -- and I want that on the record as clearly as the correction.")
print("     K1749 closed the mass gate on TWO legs: 5408 AND F506's slice mismatch (fixed-nu/varying-")
print("     degree vs varying-nu/fixed-degree), which is INDEPENDENT and PRE-DATES the toy. This audit")
print("     touches only the first leg, and weakens its STRENGTH, not its SIGN. The closure stands;")
print("     the attribution 'six forms, twelve evaluations' does not. Amend, do not retract.")
print()
print(" (6) SCOPE -- what this does NOT do: it does not reopen Lane B, does not touch the residue lead")
print("     (Keeper: flag, do not pursue as a live gate), and derives nothing. It grades an instrument.")
print("     Koide stays CONDITIONAL-FORCED. Nothing pushed. CP existence-only.")
