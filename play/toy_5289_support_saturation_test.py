import numpy as np
print("MY 5D COUNT WAS BOX-TRUNCATED and my own fit caught it: I got exponent -0.169, i.e. the count")
print("DECREASING with n, which is impossible for a genuine count. Cause: I capped x_0 <= 60, so large")
print("n was cut off. The right test is not 'how many points' but 'DOES THE COUNT SATURATE'.\n")
print("="*92)
print("THE DECISIVE TEST: fix a level n, grow the search box L, and watch the count.")
print("A FINITE level set saturates. An INFINITE one keeps growing.")
print("="*92)
def count2(n,L):                       # 2D cone: u v = n, 1 <= u,v <= L
    return sum(1 for u in range(1,L+1) if n%u==0 and 1<=n//u<=L)
def count3(n,L):                       # 3D: x0^2 - x1^2 - x2^2 = n
    c=0
    for x1 in range(-L,L+1):
        for x2 in range(-L,L+1):
            s=n+x1*x1+x2*x2
            r=int(round(np.sqrt(s)))
            if r*r==s and 1<=r<=L: c+=1
    return c
def count5(n,L):                       # 5D: x0^2 - |xvec|^2 = n, xvec in Z^4
    g=np.arange(-L,L+1)
    X=np.array(np.meshgrid(g,g,g,g,indexing='ij')).reshape(4,-1).T
    q=(X**2).sum(axis=1)
    s=n+q
    r=np.round(np.sqrt(s)).astype(np.int64)
    return int(((r*r==s)&(r>=1)&(r<=L)).sum())
print("\n      L        2D cone (n=12)     3D cone (n=12)     5D cone (n=12)")
for L in [10,20,40,80]:
    print("   %5d        %10d        %12d      %14d"%(L,count2(12,L),count3(12,L),count5(12,L) if L<=40 else -1))
print("   (5D at L=80 skipped -- 161^4 grid; the trend is already decisive)")
print("\n   2D SATURATES at d(12) = 6 and never moves again.")
print("   3D and 5D KEEP GROWING with the box -- the level set is INFINITE.")
print()
print("="*92)
print("WHY -- and this is the structural fact, not a numerical accident")
print("="*92)
print("  The integral automorphism group of the form is what acts on a level set.")
print("   * 2D, Delta = u v : the automorphs are (u,v) -> (a u, v/a) with a integer AND 1/a integer,")
print("     so a = +-1. The group is FINITE => each level set is FINITE, with exactly d(n) points.")
print("   * 5D, Delta = x0^2 - |xvec|^2 : SO(4,1)(Z) is INFINITE (hyperbolic rotations of infinite")
print("     order, Pell-type). Each level set is an INFINITE orbit.")
print("  ⟹ THE NAIVE POINT-COUNT CONE ZETA DIVERGES FOR THE 5D CONE. It has to be defined over")
print("     ORBITS -- which is exactly why Koecher/Sato-Shintani zetas are orbit sums with a")
print("     class-number-like weight. That is a DIFFERENT object from zeta^2, with its own")
print("     functional equation. It is not zeta^2 and it does not inherit RH.")
print()
print("  ★ AND IT SHARPENS THE MAKE-OR-BREAK EXACTLY: 'does the nu=1 flow give zeta, or an")
print("    L-function?' -- the honest answer from the lattice is that the 5D cone gives NEITHER")
print("    directly: it gives an ORBIT zeta. Whether that orbit zeta factors into L-functions is")
print("    the real question, and it is a class-number / Hecke question about OUR specific form.")
print("    That is where Grace's GF(128)/D_3 arithmetic would have to bite -- and it is checkable.")
