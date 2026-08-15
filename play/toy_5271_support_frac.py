import numpy as np
exec(open('parallax.py').read().split('print("  PARALLAX')[0])
print("HONEST CORRECTION: f_max is GRID-DEPENDENT -- it DIVERGES at the antipodal conjugate point.")
for n in [80,400,2000,10000]:
    Ds=np.linspace(0.05,3.10,n); f=np.array([parallax(0.01,D)/0.01 for D in Ds])
    print("   grid %5d points -> f_max = %8.1f"%(n,np.nanmax(f)))
print("   => f_max -> infinity. So NO baseline is small enough to blind the exact antipode.")
print("      'fully depthless sky' is unreachable for any b > 0. The honest quantity is the FRACTION.")
print()
Ds=np.linspace(0.02,3.12,4000); f=np.array([parallax(0.01,D)/0.01 for D in Ds])
w=np.sin(Ds)**3                      # S^4 measure weight
w/=w.sum()
print("DEPTHLESS FRACTION OF THE SKY (S^4 measure), vs sigma/b:")
print("   sigma/b       depthless fraction   resolvable region")
for r in [0.01,0.1,1.0,10.0,100.0,1000.0]:
    frac=w[f<r].sum()
    res=Ds[f>=r]
    reg=("none" if len(res)==0 else "D in [%.2f, %.2f]"%(res.min(),res.max()))
    print("   %-12.4g  %6.3f               %s"%(r,frac,reg))
print()
print("  => the record is angular over MOST of the sky once sigma/b is large, with the")
print("     un-blinded set shrinking onto the antipode. Casey's 'cannot move enough' is the")
print("     right mechanism; the caveat is that a conjugate point always survives it.")
