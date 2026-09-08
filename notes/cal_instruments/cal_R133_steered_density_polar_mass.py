# Cal R133: how much of the steered density |Z_k^xi(u)|^2 dsigma(u) on S^4 sits near the pole?
# Z_k = C_k^{3/2}(cos t)/C_k^{3/2}(1); S^4 marginal in the polar angle t: sin^3 t dt. Haar = sin^3 t dt alone.
import numpy as np
from scipy.special import eval_gegenbauer
from scipy.integrate import quad
def dens(k):
    f=lambda t:(eval_gegenbauer(k,1.5,np.cos(t))/eval_gegenbauer(k,1.5,1.0))**2*np.sin(t)**3
    Z=quad(f,0,np.pi,limit=400)[0]; return lambda t:f(t)/Z
haar=lambda t:np.sin(t)**3*3/4
print("k : mass(t<pi/4)  mass(t<pi/8)  E[cos^2 t]   (Haar: %.3f %.3f %.3f)"%(quad(haar,0,np.pi/4)[0],quad(haar,0,np.pi/8)[0],quad(lambda t:haar(t)*np.cos(t)**2,0,np.pi)[0]))
for k in (2,5,10,20,68):
    d=dens(k); print(k,": %.3f  %.3f  %.3f"%(quad(d,0,np.pi/4,limit=400)[0],quad(d,0,np.pi/8,limit=400)[0],quad(lambda t:d(t)*np.cos(t)**2,0,np.pi,limit=400)[0]))
