from fractions import Fraction as F
import itertools
print("="*92)
print("VERIFYING THE CONDITION-FORM INDEPENDENTLY -- what a paper will rest on.")
print("Tables first (banked procedure).")
print("="*92)
print("\n  CLAIM (Cal's condition-form, post-correction): exp(i theta J) closes at T = 4pi")
print("  <=> every charge lies in (1/2)Z.  Corrected E_0: Di = 2, Rac = 3/2.")
print("\n  THE ACTUAL CLOSURE CONDITION, derived not assumed:")
print("     exp(i T J) = (phase) * identity  <=>  T*(lam_i - lam_j) in 2*pi*Z for ALL pairs i,j.")
print("     So the period is set by the DIFFERENCES, not by the levels themselves.")
def period(spec):
    ds=set()
    for a,b in itertools.combinations(sorted(spec),2): ds.add(abs(a-b))
    ds.discard(0)
    if not ds: return None
    # smallest T with T*d in 2 pi Z for all d  ->  T = 2 pi / gcd(differences)
    from math import gcd
    num=0; den=1
    for d in ds:
        d=F(d).limit_denominator(10**6)
        num=gcd(num,d.numerator*(den//gcd(den,d.denominator)))
        den=den*d.denominator//gcd(den,d.denominator)
        num=gcd(num*1, d.numerator*(den//d.denominator))
    g=F(num,den)
    return g
print("\nTABLE 1 -- towers built from E_0 with the Fernando-Gunaydin +2-per-level step")
def tower(E0,n=6): return [F(E0)+2*k for k in range(n)]
Di=F(2); Rac=F(3,2)
print("     Di  (E_0 = 2)   : %s"%[str(x) for x in tower(Di,5)])
print("     Rac (E_0 = 3/2) : %s"%[str(x) for x in tower(Rac,5)])
print("\nTABLE 2 -- gcd of level differences, and the resulting period T = 2pi/gcd")
cases=[("Di alone",tower(Di,5)),
       ("Rac alone",tower(Rac,5)),
       ("Di + Rac together",tower(Di,5)+tower(Rac,5))]
for name,spec in cases:
    g=period(spec)
    print("     %-20s gcd of differences = %-6s  ->  T = 2pi/%s = %spi"%(name,str(g),str(g),str(F(2)/g)))
print("\nTABLE 3 -- what happens if the two E_0 differ by an INTEGER instead")
alt=[("E_0 = 2 and 3 (both integer)",tower(F(2),5)+tower(F(3),5)),
     ("E_0 = 5/2 and 3/2 (both half-int, gap 1)",tower(F(5,2),5)+tower(F(3,2),5)),
     ("E_0 = 2 and 3/2 (gap 1/2)  <- BST",tower(F(2),5)+tower(F(3,2),5))]
for name,spec in alt:
    g=period(spec); print("     %-42s -> T = %spi"%(name,str(F(2)/g)))
print()
print("="*92)
print("VERDICT -- from Tables 1-3 only")
print("="*92)
print("  * Di alone: differences are all multiples of 2 -> T = pi.  Rac alone: same -> T = pi.")
print("    NEITHER TOWER ALONE FORCES 4pi. Each closes faster.")
print("  * Together, the smallest difference is |2 - 3/2| = 1/2 -> gcd = 1/2 -> T = 4pi. ✓")
print("  * Table 3 confirms the mechanism: two integer E_0 give 2pi; two half-integer E_0 separated")
print("    by 1 give 2pi; only a HALF-INTEGER GAP between the towers gives 4pi.")
print()
print("  ⟹ ★★ THE 4pi IS FORCED BY THE **GAP** BETWEEN THE TWO TOWERS BEING HALF-INTEGRAL --")
print("     not by either tower being spinorial, and not by the scalar tower alone. It is a")
print("     property of the PAIR. Neither Di nor Rac forces it in isolation.")
print("  ⟹ This SHARPENS Cal's correction rather than contradicting it: the retraction of 'matter is")
print("     spinorial from the shape of time' was right, and the replacement is not 'the scalar")
print("     forces it' either -- it is 'the Rac-Di mismatch forces it'.")
print("  ⟹ AND IT GIVES THE PAPER A CLEANER CONDITION-FORM, checkable in one line:")
print("       T = 2*pi / gcd{ lam_i - lam_j }.  4pi closure  <=>  gcd of level differences = 1/2.")
print("     That is equivalent to 'all charges in (1/2)Z' ONLY IF the set actually contains a")
print("     half-integer gap -- so the gcd form is the safer statement to publish.")
