# Cal R136 (second run): my first bump was placed BELOW the j=0 median of |z|^2 (0.45 vs median 0.5),
# so it decayed monotonically and did not test the claim. Place it ABOVE the median, where the measured
# dominance table (P(|z|^2>0.8): 0.005 -> 0.299 over j=0..5) says the mass ARRIVES with j.
# Efficient sampler: uniform in the complex Euclidean unit ball, reject to the Lie ball.
import numpy as np
rng = np.random.default_rng(11)
pts, tot, kept = [], 0, 0
while kept < 600000:
    M = 400000
    g = rng.normal(size=(M,10)); g /= np.linalg.norm(g,axis=1)[:,None]
    g *= rng.random(M)[:,None]**(1/10)
    u = g[:,:5] + 1j*g[:,5:]
    a = (np.abs(u)**2).sum(1); b = np.abs((u*u).sum(1))
    ok = a + np.sqrt(np.maximum(a*a-b*b,0.0)) < 1.0
    pts.append(u[ok]); kept += ok.sum(); tot += M
z = np.concatenate(pts)[:600000]
r = (np.abs(z)**2).sum(1); s = np.abs((z*z).sum(1))
print("sampler: acceptance %.4f of the Euclidean ball; n = %d" % (kept/tot, len(z)))
def mean_ess(f, j):
    w = s**(2*j); W = w.sum(); ess = W*W/ (w*w).sum()
    return float((f*w).sum()/W), float(ess)
for c,w in ((0.85,0.05),(0.90,0.04)):
    h = np.exp(-((r-c)/w)**2)*0.9            # admissible: 0<=1-h<=1 and h -> ~0 at r=1
    print("\nbump centre %.2f width %.2f :  cost = <h>  (g = 1-h is 1 on the Shilov boundary to %.1e)"
          % (c,w,float(np.exp(-((1-c)/w)**2)*0.9)))
    row=[]
    for j in range(0,13):
        m,e = mean_ess(h,j); row.append((j,m,e))
    print("  j: " + " ".join("%d=%.4f(ess %.0f)" % t for t in row))
    vals=[m for _,m,_ in row]
    print("  rises then falls?", any(vals[i]<vals[i+1] for i in range(len(vals)-1)) and vals[-1]<max(vals),
          " | j=0 %.4f  max %.4f at j=%d" % (vals[0], max(vals), int(np.argmax(vals))))
