from fractions import Fraction as Fr
import numpy as np
def c(j,k):  # closed form (Lyra L2 = Elie 5735)
    j=Fr(j);k=Fr(k)
    return 1 - Fr(k+3,2*k+3)*(j+k+Fr(5,2))/(j+k+5) - Fr(k,2*k+3)*(j+1)/(j+Fr(7,2))
assert c(0,0)==Fr(1,2) and c(1,0)==Fr(5,12) and c(2,0)==Fr(5,14) and c(1,1)==Fr(25,63)
# chain DP: state (j,k) prob; per write: matter (j+1,k-1) w.p. k/(2k+3), light (j,k+1) w.p. (k+3)/(2k+3)
def run(j0,N=137,kcap=None):
    st={(j0,0):1.0}; tot=0.0; n=0
    for step in range(10**6):
        if kcap is None and n==N: break
        if kcap is not None and all(k>=kcap for (j,k) in st): break
        # accumulate expected c over current words (a push at each write)
        tot+=sum(p*float(c(j,k)) for (j,k),p in st.items()); n+=1
        new={}
        for (j,k),p in st.items():
            if kcap is not None and k>=kcap: new[(j,k)]=new.get((j,k),0)+p; continue
            pm=k/(2*k+3); new[(j+1,k-1)]=new.get((j+1,k-1),0)+p*pm if k>0 else new.get((j+1,k-1),0)
            new[(j,k+1)]=new.get((j,k+1),0)+p*(1-pm)
        st={s:p for s,p in new.items() if p>1e-15}
    return tot, n, tot/n
for j0 in (0,58,570,2329):
    tot,n,mean=run(j0)
    print("m-cap 137 writes: j0=%5d  sum c = %.3f   failed-push fraction (mean c) = %.4f"%(j0,tot,mean))
# alpha drift under R2
tH=1.38e10; bound=1.1e-18
jmin=2.5/(tH*bound); print("alpha-drift R2: j_min = %.2e  -> cycles at k-cap (2329/cycle) %.1e, at m-cap (58/cycle) %.1e"%(jmin,jmin/2329,jmin/58))
for j in (100,1000,10000): print("  if j=%6d today: alpha_dot/alpha = %.1e /yr"%(j,2.5/(j*tH)))
