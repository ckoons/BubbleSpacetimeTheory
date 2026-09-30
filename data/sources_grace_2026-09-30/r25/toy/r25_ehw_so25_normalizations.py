# R25 instrument: EHW normalization for so(2,5) (B3), scalar line, exact arithmetic.
# Coordinates: PPST3 (arXiv 2412.06317) Sec. 3: noncompact positive roots e1 +- ej, e1;
# rho = (n-1/2,...,1/2); beta = e1+e2. EHW line: zeta _|_ Delta(k), (zeta, beta^vee) = 1,
# z = (lambda + rho, beta^vee)  [BH 2409.16555 :54-64; BEHJ 2512.08199 :459-462].
from fractions import Fraction as F
n = 3                                   # so(2,2n-1) with n=3 -> so(2,5), B3
dot = lambda a, b: sum(x*y for x, y in zip(a, b))
rho = tuple(F(2*(n-i)-1, 2) for i in range(n))            # (5/2,3/2,1/2)
beta = (F(1), F(1), F(0))
bv = tuple(2*x/dot(beta, beta) for x in beta)              # coroot
zeta = (F(1), F(0), F(0))
assert dot(zeta, bv) == 1
compact = [(0,1,-1),(0,1,1),(0,1,0),(0,0,1)]
assert all(dot(zeta, a) == 0 for a in compact)
noncompact = [(1,-1,0),(1,1,0),(1,0,-1),(1,0,1),(1,0,0)]
rb = dot(rho, bv); c = F(2*n-3, 2); r = 2
print("rho =", rho, " (rho,beta^vee) =", rb, " c =", c, " r =", r, " dim p+ =", len(noncompact))
print("Table-1 check: (rho,beta^vee)=2n-2 ->", 2*n-2, "; c=n-3/2 ->", c, "; h^vee=(rho,beta^vee)+1 =", rb+1)
z_k = [rb - k*c for k in range(r+1)]
print("z_k = (rho,beta^vee) - k c, k=0..r:", z_k)
z = lambda nu: dot(tuple(a+b for a, b in zip((-nu, F(0), F(0)), rho)), bv)  # scalar lambda = (-nu,0,0)
for nu in [F(0), F(1), F(3,2), F(5,2), F(3), F(4), F(9,2), F(5)]:
    lam_rho = (-nu+rho[0], rho[1], rho[2])
    hds = all(dot(lam_rho, a) < 0 for a in noncompact)   # Harish-Chandra: (lambda+rho, alpha) < 0 all alpha in Delta(p+)
    unit = (nu == 0) or (nu >= F(3,2))                   # PPST3 Thm 3.5 with lambda1 = -nu
    print(f"nu={str(nu):>4}  z={str(z(nu)):>5}  unitary={unit!s:5}  HDS(z<0)={hds!s:5}  "
          f"k_BH=nu/c={str(nu/c):>5}  k_shift=nu-3/2={str(nu-F(3,2)):>4}  k_dbl=2nu={str(2*nu):>3}")
print("Thresholds by scale (L2 = HDS):")
print("  EHW z      : Wallach z in {4, 5/2} U (-inf,5/2); Hardy z=3/2; L2 z<0")
print("  FK nu=4-z  : Wallach {0,3/2} U (3/2,inf); Hardy 5/2; L2 nu>4")
print("  BH k=nu/c  : Wallach {0,1} U (1,inf); Hardy 5/3; L2 k>8/3")
print("  k=nu-3/2   : Wallach {-3/2,0} U (0,inf); Hardy 1; L2 k>5/2")
print("  k=2nu      : Wallach {0,3} U (3,inf); Hardy 5; L2 k>8")
# first L2 point on each lattice of nu
for name, step in [("nu in Z (SO_0(2,5))", F(1)), ("nu in Z/2 (double cover along the central SO(2); NOT Spin(2,5): B3 weights are all-integer or all-half-integer, and (nu,0,0) with nu in 1/2+Z is neither)", F(1,2))]:
    nu = F(4) + step
    print(f"  first L2 nu on {name}: {nu} -> k_BH={nu/c}, k_shift={nu-F(3,2)}, k_dbl={2*nu}")
print("  general n: first Z/2 L2 point nu=n_C-1/2 -> k_shift=(n_C+1)/2 for all n_C; k_BH=(2n_C-1)/(n_C-2) equals 3 only at n_C=5")
for N in range(3, 10):
    print(f"    n_C={N}: k_shift={F(2*N-1,2)-F(N-2,2)}  (n_C-1)/2+1={F(N-1,2)+1}  k_BH={F(2*N-1,2)/F(N-2,2)}")
