# 2-adic distribution of val(q0(u)) over PRIMITIVE u in Z_2^3, for q0 = x^2+y^2+z^2 (anisotropic at 2) and q0' = xy+z^2 (split).
# p_j = P(val q0(u) >= j | u primitive) computed exactly from counts mod 2^j.
from fractions import Fraction as F
def dist_sq(k):
    m=1<<k; d=[0]*m
    for a in range(m): d[(a*a)&(m-1)]+=1
    return d
def dist_prod(k):
    m=1<<k; d=[0]*m
    for a in range(m):
        for b in range(m): d[(a*b)&(m-1)]+=1
    return d
def conv(a,b,m):
    c=[0]*m
    for i,x in enumerate(a):
        if x==0: continue
        for j,y in enumerate(b):
            if y: c[(i+j)&(m-1)]+=x*y
    return c
def zero_count(k, split):
    # all u mod 2^k with q(u) = 0 mod 2^k
    m=1<<k; S=dist_sq(k)
    if split: return conv(dist_prod(k),S,m)[0]
    return conv(conv(S,S,m),S,m)[0]
def prim_zero_frac(j, split):
    # fraction of PRIMITIVE u in Z_2^3 with q(u) = 0 mod 2^j
    if j==0: return F(1)
    total=zero_count(j,split)            # all u mod 2^j
    # non-primitive u = 2u': q(2u') = 4 q(u') = 0 mod 2^j  <=> q(u') = 0 mod 2^{j-2} (j>=2); for j=1: all even u (2^{3(j-1)}... ) 
    if j>=2:
        m2=1<<(j-2); nonprim = zero_count(j-2,split) * (2**(3*(j-2)) and 1)  # count of u' mod 2^{j-2} with q=0 mod 2^{j-2}, each lifts to 2^{3*2}?? careful
        # u = 2u' mod 2^j: u' ranges mod 2^{j-1}; q(u') mod 2^{j-2} is what matters: count u' mod 2^{j-1} with q(u')=0 mod 2^{j-2} = zero_count(j-2)*8
        nonprim = zero_count(j-2,split)*8
    else:
        nonprim = 1  # u = 0 mod 2 : one class mod 2
    prim = total - nonprim
    return F(prim, 7*8**(j-1))          # primitive u mod 2^j: 8^j - 8^{j-1} = 7*8^{j-1}
for split,name in ((False,"aniso x^2+y^2+z^2"),(True,"split xy+z^2")):
    ps=[prim_zero_frac(j,split) for j in range(0,9)]
    print(name)
    print("  P(val>=j), j=0..8:", [str(p) for p in ps])
    print("  ratios p_{j+1}/p_j:", [str(ps[j+1]/ps[j]) if ps[j] else '-' for j in range(8)])
