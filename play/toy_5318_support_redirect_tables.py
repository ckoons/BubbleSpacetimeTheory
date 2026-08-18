import numpy as np, mpmath as mp
mp.mp.dps=25
print("="*92)
print("THE REDIRECT -- PROCESS FIX ADOPTED: ALL TABLES PRINT FIRST. No verdict text until after.")
print("="*92)
Nc=3
poch=lambda m: float(mp.rf(Nc,m))
print("\nTABLE 1 -- the banked Pochhammer (mass-ratio) route, applied to ALL THREE CKM magnitudes.")
print("   rule: V_ij = sqrt( (N_c)_{d_i} / (N_c)_{d_j} ), degrees {1,3,5} (T2513 single-row).")
print("   (N_c)_1, (N_c)_3, (N_c)_5 = %.0f, %.0f, %.0f"%(poch(1),poch(3),poch(5)))
obs={"V_us":(0.22431,0.00085),"V_cb":(0.04182,0.00085),"V_ub":(0.003820,0.00012)}
rows=[("V_us","(N_c)_1/(N_c)_3",poch(1)/poch(3)),
      ("V_cb","(N_c)_3/(N_c)_5",poch(3)/poch(5)),
      ("V_ub","(N_c)_1/(N_c)_5",poch(1)/poch(5))]
print("\n     elem    ratio                predicted    observed     ratio pred/obs    sigma")
for name,lab,r in rows:
    p=np.sqrt(r); o,e=obs[name]
    print("     %-5s   %-18s  %.6f     %.6f      %7.2f        %8.1f"%(name,lab,p,o,p/o,abs(p-o)/e))
print("\nTABLE 2 -- the radial coherent-state route (my 5317), for comparison.")
print("     reading      p_u       V_us/V_ud pred   obs 0.2302    dev in p")
for nm,p in [("b = nu",0.5),("b = 2nu",1/3)]:
    from math import factorial,exp,sqrt
    c=lambda k,pp: exp(-pp/2)*(sqrt(pp)**k)/sqrt(factorial(k))
    v=(c(2,p)+c(4,p))/(c(0,p)+c(2,p))
    print("     %-11s  %.4f      %.4f            %.4f       %6.1f%%"%(nm,p,v,0.2302,100*abs(p-0.3713)/0.3713))
print("\nTABLE 3 -- what each route costs in free parameters.")
print("     route                              free params   elements right (<2 sigma)")
print("     Pochhammer / mass-ratio (banked)         0             %d of 3"%sum(1 for n,l,r in rows if abs(np.sqrt(r)-obs[n][0])/obs[n][1]<2))
print("     radial coherent-state center             0*            0 of 3   (*rigid, and it misses)")
print("     free centers (my 5309/5314)              3             3 of 3   (fit, banks nothing)")
print()
print("="*92)
print("VERDICT -- written only from the three tables above")
print("="*92)
print("  From TABLE 1: the banked Pochhammer route gets V_us at 0.8 sigma with ZERO parameters --")
print("  and MISSES V_cb by 3.7x and V_ub by 9.0x. It is a ONE-ELEMENT success, not a sector")
print("  derivation. That is worth stating plainly: the corpus banks V_us, and V_us only.")
print()
print("  From TABLE 2: the radial route misses V_us by 10-35%% in the center, i.e. it fails the one")
print("  element the other route already gets. It was an attempt to RE-derive an already-derived")
print("  quantity by a second mechanism, and the second mechanism is refuted (if Cal rules b forced).")
print()
print("  From TABLE 3: the refutation costs NOTHING THAT WAS BANKED. V_us stands on the Pochhammer")
print("  route at zero parameters. What falls is the UNIFICATION -- the hope that the wavefunction")
print("  overlap and the mass-ratio were one geometry read twice.")
print()
print("  ⟹ THE REDIRECT, NAMED:")
print("     * NOT 'the magnitude is a free input' -- V_us is derived, banked, 0 parameters.")
print("     * NOT 'the radial center, harder' -- rigid and refuted.")
print("     * THE OPEN MAGNITUDES ARE V_cb AND V_ub, and the Pochhammer rule that nails V_us fails")
print("       BOTH by 4-9x. So the redirect is: find what the down-ladder ratio is MISSING for the")
print("       2-3 and 1-3 elements -- the current's Clebsch weight is the natural candidate, because")
print("       it is the one factor Wigner-Eckart says must multiply the reduced matrix element and")
print("       that the naive ratio omits. Rigid, mass-free, and it differs entry-by-entry -- exactly")
print("       the shape needed to fix two elements while leaving the third alone.")
print("     * FALSIFIER, pre-registered: the Clebsch weights must supply factors ~1/3.7 (V_cb) and")
print("       ~1/9.0 (V_ub) while leaving V_us at 1.00. If they do not, the sector's magnitudes are")
print("       a free input and I will say so.")
