# Cal R136: three questions about Keeper's K1885-PRE family sweep.
# (1) Is the admissible family BIGGER than {|z|^{2n}}? The Lie ball has TWO K-invariants, |z|^2 and |z.z|,
#     both = 1 on the Shilov boundary. Exhibit a member outside Keeper's chain.
# (2) Is |z|^2 built from the dictionary's own writes?  sum_i |z_i|^2 = |z|^2 exactly (W_i = mult by z_i).
# (3) Is the ORDER invariant across the WHOLE family, or only across the monotone sub-family?
#     Exhibit an admissible effect (=1 on S, 0<=g<=1) whose cost is NON-monotone in j.
import numpy as np
rng = np.random.default_rng(7)
N, acc = 0, []
while N < 400000:
    u = rng.uniform(-1,1,(600000,5)) + 1j*rng.uniform(-1,1,(600000,5))
    a = (np.abs(u)**2).sum(1); b = np.abs((u*u).sum(1))
    lie = a + np.sqrt(np.maximum(a*a - b*b, 0.0))          # Lie norm SQUARED
    ok = lie < 1.0; acc.append(u[ok]); N += ok.sum()
z = np.concatenate(acc)[:400000]
r  = (np.abs(z)**2).sum(1)          # |z|^2
s  = np.abs((z*z).sum(1))           # |z.z|
print("sampler: acceptance %.4f ; max |z|^2 = %.4f ; max |z.z| = %.4f" % (N/ (len(acc)*600000), r.max(), s.max()))
print("write-tuple identity  max| sum_i |z_i|^2 - |z|^2 | =", np.abs((np.abs(z)**2).sum(1) - r).max())
def mean(f, j):                                            # <f> in the Bergman-normalised word (z.z)^j
    w = s**(2*j); return float((f*w).sum()/w.sum())
print("\n j |  1-<|z|^2>   1-<|z|^4>   1-<|z|^6>  |  1-<|z.z|^2>  1-<|z.z|^4> | exact 5/(2(j+5))")
for j in range(6):
    print(" %d |  %.4f      %.4f      %.4f     |  %.4f       %.4f      | %.4f"
          % (j, 1-mean(r,j), 1-mean(r**2,j), 1-mean(r**3,j), 1-mean(s**2,j), 1-mean(s**4,j), 5/(2*(j+5))))
# (3) an admissible NON-monotone effect: g = 1 - h, h a bump in |z|^2 away from the boundary, h(1)=0
h = np.exp(-((r-0.45)/0.12)**2) * 0.9                      # 0<=h<0.9, h -> 0 at r=1  => g=1-h admissible
print("\nnon-monotone member g = 1 - 0.9*exp(-((|z|^2-0.45)/0.12)^2):  cost = <h>")
costs = [mean(h,j) for j in range(9)]
print("  j=0..8 cost:", " ".join("%.4f" % c for c in costs))
print("  monotone decreasing?", all(costs[i] > costs[i+1] for i in range(len(costs)-1)), " -> limit 0:", "%.4f" % costs[-1])
# stochastic dominance check: P(|z|^2 > t) rising in j
for t in (0.5, 0.8):
    print("  P(|z|^2 > %.1f) by j:" % t, " ".join("%.3f" % mean((r>t).astype(float), j) for j in range(6)))
