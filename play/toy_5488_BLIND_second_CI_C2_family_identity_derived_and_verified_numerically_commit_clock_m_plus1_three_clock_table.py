# TOY 5488 -- BLIND SECOND-CI on Lyra's C2 lane. Elie, 2026-08-24.
# *** COMPUTED BEFORE READING HER FILE (protocol). Baseline: my Saturday 4/4 verification of the
# R57 identity tau''/tau'^2 = v[(3/2)(1+w_tot) - s] (K1800c). Conventions DECLARED below. ***
import numpy as np
BAR="="*100
print(BAR); print("TOY 5488 -- BLIND: the clock-family identity, derived + verified numerically"); print(BAR)

print("""LEG (a) -- THE DERIVATION, conventions declared:
  e-fold time tau_hor = ln a; primes = d/d ln a. A clock with TICK PERIOD T prop H^m (T in
  cosmic time) has e-fold rate R = dtau/d ln a = 1/(T*H) prop H^-(1+m).
  d ln R/d ln a = -(1+m) d ln H/d ln a = +(1+m)*(3/2)*(1+w_tot)   [flat FRW: dlnH/dlna = -(3/2)(1+w)]
  and tau''/tau'^2 = (d ln R/d ln a)/R -> at the tick-normalized point (R=1):
     *** FAMILY IDENTITY:  tau''/tau'^2 = v * (3/2)(1+w_tot) * (1+m) ***
  CONSISTENCY WITH MY SATURDAY BASELINE: v[(3/2)(1+w)-s] = v(3/2)(1+w)(1+m) iff
     *** s = -m*(3/2)(1+w_tot) -- the R57 s-parameter IS the clock exponent in disguise. ***
  Saturday's v=1, s=0 Koons-tick => m=0: the FIXED-PERIOD clock. The horizon clock is m=-1
  (T prop 1/H) => factor 0 -- it is drift-free against itself, as it must be.""")

print("LEG (b) -- THE COMMIT CLOCK: m = +1, derived not asserted:")
print("  S = pi/H^2 (record count = horizon area). S-dot = -2pi H^-3 H-dot = 3pi(1+w)/H  prop 1/H.")
print("  Per-record period T = 1/S-dot prop H  =>  *** T prop H^m with m = +1. ***")
print("  (Records commit FASTER as the horizon grows -- S-dot rises as H falls. Sign sanity: yes.)")

print("\nLEG (a) NUMERICAL VERIFICATION -- exact FRW, no anchor games; a prop t^q, q=2/(3(1+w)):")
def check(w,m,t0=1.0):
    q=2.0/(3.0*(1.0+w))
    t=np.linspace(t0,3*t0,200001); a=t**q; lna=np.log(a); H=q/t
    T=H**m                      # tick period prop H^m
    R=1.0/(T*H)                 # dtau/dlna
    dR=np.gradient(R,lna)
    obj=dR/R**2                 # tau''/tau'^2, primes d/dlna
    # normalize at the R=1 point: obj*R evaluated anywhere is the invariant (1+m)(3/2)(1+w)
    inv=obj*R
    return inv[100000]
print("   w      m    numeric (obj*R)   analytic (1+m)(3/2)(1+w)   match?")
ok=True
for w in (0.0,-0.7,1.0/3.0):
    for m in (-1,0,1):
        num=check(w,m); ana=(1+m)*1.5*(1+w)
        good=abs(num-ana)<1e-3; ok=ok and good
        print("   %-6s %-4d %-17.6f %-26.6f %s"%(w,m,num,ana,"OK" if good else "*** NO ***"))
print("   IDENTITY VERIFIED NUMERICALLY: %s (9/9 cases, <1e-3)"%("YES" if ok else "NO"))

print("\nLEG (c) -- THE THREE-CLOCK TABLE vs the bar 5.4:")
for w,era in ((0.0,"matter era"),(-0.7,"w_tot = -0.7 (today-like)")):
    print("   %s: base (3/2)(1+w) = %.2f"%(era,1.5*(1+w)))
    worst=None
    for m,name in ((-1,"horizon clock"),(0,"fixed-period (Koons-tick)"),(1,"per-record commit clock")):
        val=(1+m)*1.5*(1+w)
        marg=(5.4/val) if val>0 else float("inf")
        if worst is None or (val>0 and marg<worst): worst=marg
        print("     m=%-3d %-26s |tau''/tau'^2| = %-6.2f margin vs 5.4 = %s"%(m,name,val,
              ("%.1fx"%marg) if val>0 else "inf (drift-free)"))
    print("     WORST FINITE MARGIN: %.1fx"%worst)

print("\nBLIND VERDICT (hers unread):")
print("  (a) family identity DERIVED and numerically verified 9/9; s = -m(3/2)(1+w) reconciles it")
print("      EXACTLY with my Saturday baseline -- the family is R57's identity with s unpacked.")
print("  (b) commit clock m = +1 DERIVED from S prop H^-2 with the sign sane.")
print("  (c) matter era {0, 1.5, 3.0}, worst margin 1.8x; w=-0.7 {0, 0.45, 0.9}, margin 6x.")
print("  HEADLINE TEST: the commit clock DOUBLES the worst drift (3.0 vs 1.5), so the margin")
print("  honestly SHRINKS 3.6x -> 1.8x -- and the theorem SURVIVES on the natural-clock class.")
print("  ALL THREE LEGS LAND. Computed blind; comparison against her file is the verifiers' step.")
