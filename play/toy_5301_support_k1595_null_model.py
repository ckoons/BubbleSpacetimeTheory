import sympy as sp
from collections import Counter
import itertools
n=sp.symbols('n')
print("="*92)
print("THE K1595 NULL MODEL: how many SIMPLE relations among the five integers single out some n?")
print("="*92)
print("  Grammar fixed BEFORE looking at any answer (no cherry-picking):")
atoms={"rank":sp.Integer(2),"n_C":n,"N_c":n-2,"g":n+2,"C_2":2*n-4}
for k,v in atoms.items(): print("     %-5s = %s"%(k,sp.expand(v)))
print("  relations tested:  X = Y op Z   and   X = Y^2 op Z,   for X,Y,Z atoms, op in {+, -, *}")
ops=[("+",lambda a,b:a+b),("-",lambda a,b:a-b),("*",lambda a,b:a*b)]
rels=[]
for X,vx in atoms.items():
    for (Y,vy),(Z,vz) in itertools.product(atoms.items(),repeat=2):
        for s,f in ops:
            rels.append(("%s = %s %s %s"%(X,Y,s,Z), vx, f(vy,vz)))
            rels.append(("%s = %s^2 %s %s"%(X,Y,s,Z), vx, f(vy**2,vz)))
print("     total relations enumerated: %d"%len(rels))
LO,HI=3,40
ident=0; nosol=0; uniq=Counter(); multi=0
uniq_examples={}
for name,lhs,rhs in rels:
    d=sp.expand(lhs-rhs)
    if d==0: ident+=1; continue
    sols=[k for k in range(LO,HI+1) if d.subs(n,k)==0]
    if len(sols)==0: nosol+=1
    elif len(sols)==1:
        uniq[sols[0]]+=1
        uniq_examples.setdefault(sols[0],[]).append(name)
    else: multi+=1
tot=len(rels)
print("\n  RESULTS over n in [%d,%d]:"%(LO,HI))
print("     identities (true for all n)          : %4d  (%.1f%%)"%(ident,100*ident/tot))
print("     no solution in range                 : %4d  (%.1f%%)"%(nosol,100*nosol/tot))
print("     SINGLE OUT EXACTLY ONE n             : %4d  (%.1f%%)  <-- the fishing pool"%(sum(uniq.values()),100*sum(uniq.values())/tot))
print("     multiple solutions                   : %4d  (%.1f%%)"%(multi,100*multi/tot))
print("\n  WHICH n do they single out?  (top of the distribution)")
for k,c in uniq.most_common(12):
    star="   <-- BST's n" if k==5 else ""
    print("       n = %2d : %4d relations%s"%(k,c,star))
print("\n  ⟹ %d relations single out n = 5 alone."%uniq[5])
print("     and n = 5 ranks #%d among the singled-out values."%(1+sum(1 for k,c in uniq.items() if c>uniq[5])))
print("\n  the specific relation in question, g = N_c^2 - rank, is one of these %d:"%uniq[5])
for ex in uniq_examples.get(5,[])[:10]: print("       %s"%ex)
print("\n  ⟹ VERDICT: singling out a unique n is COMMON in this grammar (%.0f%% of relations do it),"%(100*sum(uniq.values())/tot))
print("     and %d distinct relations single out n = 5 specifically. FINDING ONE IS NOT EVIDENCE."%uniq[5])
print("     The fishing question is settled: a relation that picks n = 5 is exactly what a random")
print("     simple relation does. Only a TARGET-INNOCENT DERIVATION -- one that never evaluates at")
print("     n = 5 -- can carry any weight, which is precisely the crux routed to @Lyra.")
