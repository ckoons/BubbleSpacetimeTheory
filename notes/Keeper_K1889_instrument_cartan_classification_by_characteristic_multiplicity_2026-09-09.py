# Characteristic multiplicities a (and b) for irreducible bounded symmetric domains,
# standard Jordan-triple root data.  genus p = (r-1)a + b + 2.
rows=[]
for p_ in range(1,13):
    for q in range(p_,13):
        rows.append(("I_%d,%d"%(p_,q), p_, 2, q-p_, p_*q))          # rank p, a=2, b=q-p
for n in range(5,13):
    r=n//2; b=0 if n%2==0 else 2
    rows.append(("II_%d"%n, r, 4, b, n*(n-1)//2))                    # a=4
for n in range(2,13):
    rows.append(("III_%d"%n, n, 1, 0, n*(n+1)//2))                   # a=1
for n in range(3,15):
    rows.append(("IV_%d"%n, 2, n-2, 0, n))                           # a=n-2
rows.append(("V (E6)", 2, 6, 4, 16)); rows.append(("VI (E7)", 3, 8, 0, 27))
print("genus check on IV_5:", (2-1)*(5-2)+0+2, " (dim 5, expect 5)")
hits=[r for r in rows if r[2]==3]
print("\nDomains with characteristic multiplicity a = 3 (= N_c measured):")
for h in hits: print("   %-10s rank=%d  a=%d  b=%d  dim_C=%d   genus=%d"%(h[0],h[1],h[2],h[3],h[4],(h[1]-1)*h[2]+h[3]+2))
print("\ncount =",len(hits))
r2=[r for r in rows if r[1]==2]
print("\nrank = 2 alone (generations-1) leaves:",len(r2),"families:", ", ".join(r[0] for r in r2[:8]),"...")
d5=[r for r in rows if r[4]==5]
print("dim_C = 5 alone leaves:", ", ".join(r[0] for r in d5))
