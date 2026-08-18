import numpy as np, mpmath as mp
mp.mp.dps=25
print("="*92)
print("THE CLEBSCH TEST -- BLIND POST FIRST, ALL TABLES BEFORE ANY VERDICT (banked procedure).")
print("="*92)
print("\nBLIND POST (K1002) -- the object, its provenance, and the pre-registered falsifier:")
print("  OBJECT: J_W is a degree-1 (vector) tensor operator on SO(5) (T1929). Between single-row")
print("          K-types (k,0) -- the T2513 degrees -- Wigner-Eckart gives the vector matrix element,")
print("          which is the Gegenbauer/spherical-harmonic recursion at lambda = (n-2)/2 = 3/2:")
print("            |<k+1||x||k>|^2 = (k+1)/(2k+n),   n = n_C = 5.")
print("          MASS-FREE, ENTRY-DEPENDENT, ZERO PARAMETERS.")
print("  FALSIFIER (posted in my 5318, before this computation): the weights must supply")
print("          ~1/3.69 for V_cb and ~1/9.03 for V_ub while leaving V_us at 1.00.")
n=5
def w2(k): return (k+1)/(2*k+n)          # one J_W step, k -> k+1
print("\nTABLE 1 -- the one-step Clebsch weights (zero parameters)")
print("     k      |<k+1||x||k>|^2      |<k+1||x||k>|")
for k in range(0,6):
    print("     %d       %.6f            %.6f"%(k,w2(k),np.sqrt(w2(k))))
def amp(k0,k1):
    a=1.0
    for k in range(k0,k1): a*=np.sqrt(w2(k))
    return a
print("\nTABLE 2 -- multi-step amplitudes on the T2513 degree ladder {1,3,5}")
paths=[("V_us","1->3",1,3),("V_cb","3->5",3,5),("V_ub","1->5",1,5)]
for nm,lab,a,b in paths:
    print("     %-5s  %-6s steps=%d   amplitude = %.6f"%(nm,lab,b-a,amp(a,b)))
print("\nTABLE 3 -- what the falsifier requires vs what the Clebsch supplies (both normalised to V_us)")
obs={"V_us":0.22431,"V_cb":0.04182,"V_ub":0.003820}
poch=lambda m: float(mp.rf(3,m))
pred={"V_us":np.sqrt(poch(1)/poch(3)),"V_cb":np.sqrt(poch(3)/poch(5)),"V_ub":np.sqrt(poch(1)/poch(5))}
base=amp(1,3)
print("     elem    required factor    Clebsch factor    agree?")
for nm,lab,a,b in paths:
    req=obs[nm]/pred[nm]; req_rel=req/(obs["V_us"]/pred["V_us"])
    cl=amp(a,b)/base
    print("     %-5s     %10.4f       %10.4f        %s"%(nm,req_rel,cl,"yes" if abs(cl/req_rel-1)<0.1 else "NO"))
print("\nTABLE 4 -- direction check: does the Clebsch weight rise or fall along the ladder?")
for k in range(0,6):
    print("     k=%d -> k=%d :  weight %.6f   %s"%(k,k+1,np.sqrt(w2(k)),"(rising)" if k>0 and w2(k)>w2(k-1) else ""))
print()
print("="*92)
print("VERDICT -- written only from Tables 1-4")
print("="*92)
print("  TABLE 4: the one-step Clebsch weight RISES monotonically with k (0.447, 0.535, 0.577,")
print("  0.603, 0.620, 0.632). It gets LARGER as you climb the ladder.")
print("  TABLE 3: the falsifier needs factors of ~1/3.7 and ~1/9.0 -- i.e. SUPPRESSION that grows")
print("  with the rung. The Clebsch supplies ENHANCEMENT that grows with the rung.")
print("  ⟹ THE CLEBSCH WEIGHT RUNS THE WRONG WAY. Not merely the wrong size -- the wrong SIGN of")
print("     dependence. It cannot suppress V_cb relative to V_us, because it enhances it.")
print()
print("  ⟹ ★★★★ THE PRE-REGISTERED FALSIFIER FIRES. The weak current's Clebsch weight does NOT")
print("     supply the missing factors. I posted the falsifier before computing; it failed.")
print()
print("  ⟹ AND THEREFORE, AS I COMMITTED TO SAY PLAINLY:")
print("     ★★ THE OPEN CKM MAGNITUDES (V_cb, V_ub) ARE A FREE INPUT. ★★")
print("     Three routes are now exhausted: the radial coherent-state centre (rigid, refuted, 5317),")
print("     the Pochhammer ratio (0 parameters, 1 of 3, off 3.7x and 9.0x, 5318), and the current's")
print("     Clebsch weight (0 parameters, wrong direction, here). The sector's honest state is:")
print("       DERIVED  : V_us = 1/sqrt(20) at 0.31%%, and the skeleton (shelves, parity, one-rung).")
print("       FREE     : the two remaining magnitudes.")
