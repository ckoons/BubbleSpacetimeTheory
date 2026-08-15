"""Support to Toy 5276 -- I own a correction to my OWN 5275 filter.

5275 stated the parallax filter PER TICK (b = v*Delta_tau < sigma/f_max). That is the wrong
quantity: a parallax measurement uses the ACCUMULATED baseline over the observation window,
not one tick. Accumulated >= per-tick, so my stated filter was too WEAK -- a process can pass
per-tick and still fail. The corrected condition is on total displacement.

The VERDICT of 5275 survives unchanged (IID sites give 1.57 rad in a SINGLE tick, so they blow
even the weak form), but the binding condition is the accumulated one, and it turns the filter
into a physical statement instead of a constraint on the site-process.
"""
sig, fmax = 1e-2, 156.0
need = sig / fmax
R = 1.30e26          # Hubble radius c/H0, m -- the standard identification for the S^4 radius (INPUT)
yr = 3.156e7
print("corrected condition:  b_total = v*T/R < sigma/f_max = %.3e" % need)
print("=>  T  <  (sigma/f_max) * (R/v)\n")
for name, v in [("solar system vs CMB (370 km/s)", 3.7e5),
                ("Earth orbital (30 km/s)", 3.0e4),
                ("ultrarelativistic (c)", 3.0e8)]:
    T = need * R / v
    print("   v = %-32s  T_max = %.2e s = %.2e yr" % (name, T, T / yr))
print("\n=> the angular record survives for any realistic observer by ~8-9 orders in time.")
print("=> and note what dropped out: the condition is v*T/R -- observer displacement over the")
print("   S^4 radius. THE COMMIT PROCESS DOES NOT APPEAR. So the corrected filter is NOT a")
print("   filter on the site-measure at all; it is a bound on how far the observer moves.")
print("   Casey's line, quantified: 'parallax is lost if the observer cannot move sufficiently.'")
