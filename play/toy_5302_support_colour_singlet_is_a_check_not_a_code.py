import numpy as np, itertools
print("="*92)
print("THE N_c CANDIDATE-MAP, ONE LOOK: is the confined 3-quark encoding a CODE at all?")
print("="*92)
print("  Cal's obstruction: the baryon singlet is eps_{abc} q^a q^b q^c -- totally ANTISYMMETRIC;")
print("  a repetition code {000,111} is totally SYMMETRIC. Opposite under S_3. Is that fatal?")
print()
print("(1) BUILD 3 (x) 3 (x) 3 AND SPLIT IT BY PERMUTATION SYMMETRY -- explicit, 27 dimensions.")
basis=list(itertools.product(range(3),repeat=3))
def perm_action(p,v):
    out=np.zeros(27)
    for i,b in enumerate(basis):
        out[basis.index(tuple(b[p[k]] for k in range(3)))]+=v[i]
    return out
perms=list(itertools.permutations(range(3)))
def sgn(p):
    s=1
    for i in range(3):
        for j in range(i+1,3):
            if p[i]>p[j]: s=-s
    return s
Psym=np.zeros((27,27)); Pant=np.zeros((27,27))
for i in range(27):
    e=np.zeros(27); e[i]=1
    for p in perms:
        Psym[:,i]+=perm_action(p,e)/6
        Pant[:,i]+=sgn(p)*perm_action(p,e)/6
ds=int(round(np.trace(Psym))); da=int(round(np.trace(Pant)))
print("     dim TOTALLY SYMMETRIC   part = %2d   (the decuplet, 10)"%ds)
print("     dim TOTALLY ANTISYMM.   part = %2d   (the colour singlet, 1)"%da)
print("     dim MIXED               part = %2d   (the two octets, 8 + 8)"%(27-ds-da))
print("     total = %d  ->  3(x)3(x)3 = 10 (+) 8 (+) 8 (+) 1  ✓ matches the corpus"%(ds+da+(27-ds-da)))
print()
print("(2) ★ WHERE WOULD A REPETITION CODE LIVE?  {000,111} is invariant under EVERY permutation,")
print("    so it lives in the TOTALLY SYMMETRIC part -- the DECUPLET (dim 10).")
rep=[np.zeros(27),np.zeros(27)]
rep[0][basis.index((0,0,0))]=1; rep[1][basis.index((1,1,1))]=1
for w,name in zip(rep,["000","111"]):
    sym=np.linalg.norm(Psym@w); ant=np.linalg.norm(Pant@w)
    print("       codeword %s :  ||P_sym w|| = %.4f   ||P_anti w|| = %.4f"%(name,sym,ant))
print("    ⟹ the repetition codewords are ENTIRELY symmetric and have ZERO antisymmetric component.")
print("       The baryon singlet is ENTIRELY antisymmetric. OPPOSITE ENDS of the decomposition.")
print()
print("="*92)
print("★★★ (3) BUT THE OBSTRUCTION IS WORSE THAN A SYMMETRY MISMATCH -- IT IS A FUNCTION MISMATCH.")
print("="*92)
print("     a CODE needs at least TWO codewords: it carries log2|C| bits.")
print("       repetition code : |C| = 2  ->  1 bit,  d_min = 3,  CORRECTS one error")
print("       colour singlet  : the antisymmetric subspace has dimension %d  ->  ONE state"%da)
print("     ⟹ |C| = 1  ->  log2(1) = 0 BITS. THE COLOUR SINGLET ENCODES NOTHING.")
print("       And with one codeword there is no minimum distance and nothing to correct toward:")
print("       any deviation simply leaves the singlet, with no majority to restore it.")
print()
print("  ⟹ THE CONFINED 3-QUARK STRUCTURE IS A **CONSTRAINT** (a parity CHECK), NOT A **CODE**")
print("     (an ENCODING). Those are different functions. A check says 'this word is legal';")
print("     an encoding says 'these bits mean that message'. Colour-neutrality is the former.")
print()
print("="*92)
print("(4) THE VERDICT ON THE CANDIDATE MAP")
print("="*92)
print("  * my 5299 stands: d_min = 3 IS forced by single-error-correction, r-independently. That is")
print("    a real theorem about CODES.")
print("  * but the map from that 3 to the CONFINED 3-QUARK ENCODING FAILS, and now for a stated")
print("    reason: the colour singlet has ONE codeword, carries ZERO bits, and lives in the")
print("    antisymmetric sector, while a distance-3 code needs >=2 codewords and lives (for the")
print("    repetition realisation) in the symmetric sector.")
print("  ⟹ N_c = 3 STAYS A CANDIDATE. The specific map offered does not close it, and the")
print("     obstruction is not merely 'antisymmetric vs symmetric' -- it is 'check vs encoding'.")
print("     Cal's §540 downgrade is correct, and this is the mechanism behind it.")
print()
print("  ★ WHAT WOULD CLOSE IT (stated so the candidate is actionable, not just parked):")
print("    exhibit a set of >= 2 physically distinguishable confined states that (a) are related by")
print("    a distance-3 structure and (b) permit majority-style recovery. The DECUPLET (dim 10,")
print("    symmetric) is where such a code would have to live -- NOT the singlet. Whether the")
print("    decuplet carries that structure is a separate, checkable question, and it is the one")
print("    the candidate actually needs.")
