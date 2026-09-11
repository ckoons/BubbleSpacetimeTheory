# POSITIVE CONTROL on the multiplicity table: the known exceptional isomorphisms
# among low-dimensional Hermitian symmetric domains must give MATCHING (rank,a,b,dim).
def IV(n): return ("IV_%d"%n, 2, n-2, 0, n)
def I(p,q): return ("I_%d,%d"%(p,q), p, 2, q-p, p*q)
def II(n): r=n//2; return ("II_%d"%n, r, 4, 0 if n%2==0 else 2, n*(n-1)//2)
def III(n): return ("III_%d"%n, n, 1, 0, n*(n+1)//2)
pairs=[("IV_1 = disc = I_1,1", IV(1), I(1,1)),
       ("IV_3 = III_2",        IV(3), III(2)),
       ("IV_4 = I_2,2",        IV(4), I(2,2)),
       ("IV_6 = II_4",         IV(6), II(4))]
print("known exceptional isomorphisms — table must agree on (rank, a, b, dim):")
ok=True
for name,x,y in pairs:
    same=(x[1],x[2],x[3],x[4])==(y[1],y[2],y[3],y[4]); ok&=same
    print("  %-22s %-10s (r=%d,a=%d,b=%d,d=%d)   vs %-8s (r=%d,a=%d,b=%d,d=%d)   %s"%(
        name,x[0],x[1],x[2],x[3],x[4],y[0],y[1],y[2],y[3],y[4],"MATCH" if same else "MISMATCH"))
print("control:", "PASSED" if ok else "FAILED")
print("\nIV_2: a = n-2 = 0  -> a=0 flags the REDUCIBLE case (IV_2 = disc x disc). Consistent.")
print("IV_5: not in the coincidence list — genuinely its own family member.")
print("\nSCOPE: is a=3 unique among REDUCIBLE domains too?")
print("  A product has one multiplicity per factor; a product of copies of IV_5 has a=3 in every factor.")
print("  => the theorem's scope clause must read IRREDUCIBLE, or add a factor-count criterion.")
