import sympy as sp
n=sp.symbols('n', positive=True)
print("="*92)
print("IS THE INTEGER WEB FORCED, OR MATCHED?  The test: express BOTH sides as functions of n,")
print("and ask whether the relation is an IDENTITY IN n or holds only at the special point.")
print("="*92)
print("  This is the same test that certified c_2 = dim K (identity in n) and killed the others.")
print()
print("  STRUCTURAL quantities of D_IV^n, each with its own independent source:")
struct={
 "rank": (sp.Integer(2), "rank of every type-IV domain"),
 "n_C" : (n,             "the complex dimension of D_IV^n"),
 "N_c" : (n-2,           "dim of the Peirce off-diagonal V_12 (my 5297 / T2527)"),
 "g"   : (n+2,           "the signature total of SO(n,2): n + 2  [corpus: g is embedding/signature, NOT the genus]"),
 "C_2" : (2*(n-2),       "the adjoint Casimir of so(n) = 2 h^v, h^v = n-2"),
}
for k,(v,why) in struct.items():
    print("     %-5s = %-12s   at n=5 -> %2d    (%s)"%(k,sp.simplify(v),int(v.subs(n,5)) if hasattr(v,'subs') else v,why))
print()
print("  PROPOSED WEB RELATIONS -- test each as an identity in n:")
props=[("g = N_c^2 - rank",   struct["g"][0],    (n-2)**2-2),
       ("n_C = g - rank",     struct["n_C"][0],  (n+2)-2),
       ("C_2 = n_C + 1",      struct["C_2"][0],  n+1),
       ("N_max = N_c^3*n_C + rank", None,        (n-2)**3*n+2)]
print("\n      relation                LHS(n)        RHS(n)        identity in n?    solutions")
for name,lhs,rhs in props:
    if lhs is None:
        print("      %-24s %-13s %-13s %-16s %s"%(name,"(definition)",sp.expand(rhs),"n/a","at n=5 -> %d"%int(rhs.subs(n,5))))
        continue
    diff=sp.simplify(sp.expand(lhs-rhs))
    ident=(diff==0)
    sols=sp.solve(sp.Eq(lhs,rhs),n)
    print("      %-24s %-13s %-13s %-16s %s"%(name,sp.expand(lhs),sp.expand(rhs),ident,sols if not ident else "all n"))
print()
print("  ⟹ THE VERDICT, relation by relation:")
print("     * g = N_c^2 - rank      : NOT an identity. Structural g = n+2 equals (n-2)^2-2 ONLY at n=5")
print("                               (and n=0). AN INTEGER-MATCH AT THE SPECIAL POINT.")
print("     * n_C = g - rank        : an IDENTITY -- but TAUTOLOGICAL, it is g = n_C + rank rearranged.")
print("                               No independent content.")
print("     * C_2 = n_C + 1         : NOT an identity. Structural C_2 = 2(n-2) equals n+1 ONLY at n=5.")
print("                               AN INTEGER-MATCH AT THE SPECIAL POINT.")
print("     * N_max = N_c^3 n_C+rank: a DEFINITION, not a relation to test.")
print("  ⟹ ONE tautology, TWO integer-matches, ONE definition. THE WEB IS NOT FORCED.")
print("     And the pattern is diagnostic: every proposed relation coincides with the structural")
print("     quantity at EXACTLY n = 5 and nowhere else. That is the signature of a formula fitted at")
print("     one point, not a structural law -- the same discriminator that certified c_2 = dim K.")
print()
print("="*92)
print("★ CASEY'S 7 = 2 + 3 + 2 -- it is BETTER than a partition, and it has ONE named gap.")
print("="*92)
print("  Two structural decompositions chain together:")
print("     g = n_C + rank        = 5 + 2   [the signature of SO(5,2)]            -- structural")
print("     n_C = rank + dim V_12 = 2 + 3   [the PEIRCE split of the spin factor] -- structural")
print("     => g = (rank + dim V_12) + rank = 2 + 3 + 2 = 7")
print("  So 7 = 2+3+2 is NOT an arbitrary partition -- both splits are corpus-structural, and the")
print("  middle 3 is the Peirce off-diagonal, which is ALSO the d_min = 3 slot in Casey's coding")
print("  reading. His 'decision + validation + boilerplate' maps onto (Peirce diagonal) +")
print("  (Peirce off-diagonal) + (the SO(2) of the signature).")
print()
print("  ★★ THE ONE GAP, and it is the day's SIXTH #35: THE TWO 2s.")
print("     the first 2 is the JORDAN RANK (the Peirce diagonal, 2 idempotents);")
print("     the second 2 is the SO(2) IN THE SIGNATURE (n,2).")
print("     Both equal 2 for every n, so they can never be separated by varying n -- the usual")
print("     discriminator is UNAVAILABLE here. Whether they are the SAME object needs an EXHIBITED")
print("     map, not a coincidence of value. Until then: a structurally-grounded decomposition with")
print("     one un-tested identification. That is a genuinely better position than 'a partition of 7'.")
