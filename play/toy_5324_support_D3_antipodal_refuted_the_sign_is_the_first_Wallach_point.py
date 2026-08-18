import numpy as np
from fractions import Fraction as F
n_C=5
a=n_C-2                      # Faraut-Koranyi multiplicity, BANKED
Di=[F(2)+2*k   for k in range(6)]
Rac=[F(3,2)+2*k for k in range(6)]
def ph(T,l):
    z=np.exp(1j*T*float(l)); return complex(round(z.real,10),round(z.imag,10))
print("="*94)
print("TOY 5324 -- D3 BLIND: is the -1 in exp(2 pi i J) = -(-1)^F the ANTIPODAL MAP?")
print("  Tables FIRST, verdict after. (procedure banked K1642)")
print("="*94)

print("\nTABLE 1 -- the HALF-period operator exp(i pi J), level by level")
print("   tower   " + "".join("%-9s"%str(l) for l in Di[:4]))
for nm,tw in [("Di",Di),("Rac",Rac)]:
    print("   %-7s "%nm + "".join("%-9s"%("%+g"%ph(np.pi,l).real if abs(ph(np.pi,l).imag)<1e-9
          else "%+gi"%ph(np.pi,l).imag) for l in tw[:4]))

print("\nTABLE 2 -- ANTIPODAL TEST.  The antipodal map A is an INVOLUTION (A^2 = id on S^4),")
print("           so ANY operator equal to A must have eigenvalues in {+1,-1}. Check exp(i pi J):")
print("   tower   exp(i pi J)   is it +-1 ?   can it BE the antipodal map?")
for nm,tw in [("Di",Di),("Rac",Rac)]:
    v=ph(np.pi,tw[0]); inv=abs(abs(v.real)-1)<1e-9 and abs(v.imag)<1e-9
    print("   %-7s %-13s %-13s %s"%(nm,("%+g"%v.real if abs(v.imag)<1e-9 else "%+gi"%v.imag),
          "YES" if inv else "NO",  "possible" if inv else "*** REFUTED ***"))

print("\nTABLE 3 -- so WHAT carries the phase?  Spacing is 2, so exp(2 pi i (E0+2m)) = exp(2 pi i E0)")
print("           -- every level gives the SAME phase and it is fixed by the GROUND STATE E0 alone.")
print("   tower   E0     exp(2 pi i E0)   exp(2 pi i J) [toy 5322]   agree?")
for nm,tw in [("Di",Di),("Rac",Rac)]:
    E0=tw[0]; p=ph(2*np.pi,E0); q={ph(2*np.pi,l) for l in tw}
    print("   %-7s %-6s %-16s %-26s %s"%(nm,str(E0),"%+g"%p.real,"%+g"%list(q)[0].real,
          len(q)==1 and abs(p-list(q)[0])<1e-9))

print("\nTABLE 4 -- and where does E0 come from?  The corpus, from n_C = 5 ALONE:")
print("   a = n_C - 2 = %d                      (Faraut-Koranyi multiplicity -- BANKED)"%a)
print("   first Wallach point of D_IV^%d = a/2 = %s   <-- Rac's E0 = 3/2  MATCH: %s"%(
      n_C,F(a,2),F(a,2)==Rac[0]))
print("   Di = a/2 + 1/2 = %s                       <-- Di's E0 = 2      MATCH: %s"%(
      F(a,2)+F(1,2),F(a,2)+F(1,2)==Di[0]))
print("   ==> exp(2 pi i J)|_Rac = exp(i pi a) = (-1)^a = (-1)^%d = %+d"%(a,(-1)**a))

print("\n"+"="*94)
print("VERDICT -- read off Tables 2-4 only")
print("="*94)
print(" (1) *** THE ANTIPODAL CANDIDATE IS REFUTED. ***  exp(i pi J) = -i on the Rac tower.")
print("     -i is a FOURTH root of unity. The antipodal map is an involution, eigenvalues +-1 only.")
print("     An operator that squares to -1 CANNOT be an involution. The half-period conformal shift")
print("     is NOT the antipodal map. I flagged this reading as a candidate last round; it is dead.")
print("     (Third flag on the pretty-story shape -- and this time the pretty story was MINE.)")
print()
print(" (2) THE ACTUAL MECHANISM, and it is corpus linear algebra on D_IV^5:")
print("     exp(2 pi i J) = exp(2 pi i E0) EXACTLY -- the tower is rigid (spacing 2 contributes")
print("     exp(4 pi i m) = 1 at every level), so the entire phase is the GROUND-STATE weight E0.")
print("     E0 is not free: E0(Rac) = a/2 = the FIRST WALLACH POINT of D_IV^5, a = n_C - 2 = 3.")
print("     ==> exp(2 pi i J)|_Rac = (-1)^a.  THE SIGN IS -1 BECAUSE a = 3 IS ODD.")
print("     ==> a odd  <==>  n_C odd  <==>  the minus sign.  n_C = 5 FORCES it.")
print()
print(" (3) WHAT THE ANTIPODAL MAP DOES DO (candidate, NOT asserted): the Z_2 of BST's own Shilov")
print("     boundary Shilov = (S^4 x S^1)/Z_2 is antipodal-paired-with-half-shift. Under it a tower")
print("     with half-odd E0 picks up a tower-wide phase e^{i pi E0} != 1, i.e. it is a SECTION of a")
print("     twisted bundle, not a function -- the Rac would live in the TWISTED SECTOR. That reading")
print("     is a CANDIDATE and I am not banking it: it needs the l-assignment pinned to a source.")
