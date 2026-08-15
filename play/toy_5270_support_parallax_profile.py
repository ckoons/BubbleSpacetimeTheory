import numpy as np
exec(open('parallax.py').read().split('print("  PARALLAX')[0])
b0=0.01
Ds=np.linspace(0.05,3.09,80)
f=np.array([parallax(b0,D)/b0 for D in Ds])
print("SHAPE OF f(D) = parallax/b  (linearity in b confirmed: rows scaled by 1,5,20 in the last run)")
print()
imin=int(np.nanargmin(f)); imax=int(np.nanargmax(f))
print("   f(D) minimum at D = %.3f rad  (f = %.4f)   <- the DEPTHLESS SHELL"%(Ds[imin],f[imin]))
print("   f(D) maximum at D = %.3f rad  (f = %.4f)   <- MOST resolvable, near the antipode"%(Ds[imax],f[imax]))
print("   f at the near field D=0.05 : %.4f"%f[0])
print("   f at the far  field D=3.09 : %.4f"%f[-1])
print()
print("   ⟹ f(D) is NOT monotonically decreasing. Near-field %.3f, dip %.4f at D=%.2f, then RISES to %.3f."%(
    f[0],f[imin],Ds[imin],f[imax]))
print()
print("="*80)
print("WHAT THAT DOES TO THE MECHANISM")
print("="*80)
print("  resolution criterion: depth recoverable iff  b*f(D) > sigma.")
print("  Since f is NOT monotone, the UNRESOLVABLE set is a SHELL around D ~ %.2f, not a far field."%Ds[imin])
print()
print("   sigma/b      unresolvable region")
for r in [0.001,0.01,0.05,0.2,0.5,1.5]:
    bad=Ds[f<r]
    if len(bad)==0: reg="none -- entire sky resolvable"
    elif len(bad)==len(Ds): reg="EVERYTHING -- whole sky depthless"
    else: reg="shell D in [%.2f, %.2f]  (width %.2f of pi)"%(bad.min(),bad.max(),(bad.max()-bad.min())/np.pi)
    print("   %-10.4g  %s"%(r,reg))
print()
print("  ⟹ THERE IS NO PARAMETER CHOICE GIVING 'near depth recoverable, far depth NOT'.")
print("     Either the whole sky is depthless, or a mid-distance SHELL is, with the far field")
print("     among the MOST resolvable. The flat-space horizon picture does not transfer to S^4.")
