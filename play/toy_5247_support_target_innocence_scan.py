import numpy as np, itertools
from fractions import Fraction as F
exec(open('shape2.py').read().split('def run(')[0])
exec(open('krein3.py').read().split('U=blockU')[0].split('for name,J in')[0].replace('N=2; nu=F(5,2)','N=2; nu=F(5,2)'))
U=blockU(N,nu)
print("TARGET-INNOCENCE CHECK: is 'rank 2' load-bearing, or does any reflection work?")
print("  r = number of reflected coordinates; J_r = (-1)^(sum n_mu, mu<r) (x) (-1)^(sum deg_mu, mu<r)")
print()
print("   r   det(R)  J^2=1     signature(+,-)     [J,D]=0     GATE 1c ||P‡-P||    verdict")
for r in range(0,6):
    ferm=np.diag([(-1.0)**sum(((i>>m)&1) for m in range(r)) for i in range(32)])
    sm=np.diag([(-1.0)**sum(x[m] for m in range(r)) for x in basis])
    J=np.kron(ferm,U.T@sm@U)
    ev=np.linalg.eigvalsh((J+J.T)/2); npos=int((ev>1e-9).sum()); nneg=int((ev<-1e-9).sum())
    jd=np.abs(J@D-D@J).max(); pk=np.abs(J@P.T@J-P).max()
    bal = "BALANCED" if npos==nneg else ""
    print("   %d   %+d      %.0e   (+%3d, -%3d) %-9s %.1e     %.2e         %s"%(
        r,(-1)**r,np.abs(J@J-np.eye(J.shape[0])).max(),npos,nneg,bal,jd,pk,"PASS" if pk<1e-9 else "FAIL"))
print()
print("  => if EVERY r passes, the pass is generic and 'rank 2' is decorative for the GATE.")
print("  => the discriminating question is then the SIGNATURE, not the gate.")
