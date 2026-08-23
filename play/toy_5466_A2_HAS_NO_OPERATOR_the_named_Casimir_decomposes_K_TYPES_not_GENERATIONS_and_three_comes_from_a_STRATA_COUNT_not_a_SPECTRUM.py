# TOY 5466 -- R72's assignment to me: NAME THE OPERATOR BEHIND A2, OR A2 GOES.
# Elie, 2026-08-23. External 3 / up sector. Forward, Rule 1. Reconnected first, Rule 4.
#
# A2 was mine: "the three generation modes are MUTUALLY ORTHOGONAL, being distinct modes of a
# self-adjoint operator." I flagged against myself that NOBODY HAS NAMED THAT OPERATOR.
# Keeper then priced exit (i) at 284x short and said the number lands exactly on A2.
#
# RECONNECTED FROM THE PRIMARY (registry, read this turn):
#   T2428: "its Wallach K-TYPE decomposition has lowest non-trivial Casimir C_2 = 6"; "every BST
#          observable lifts to a bounded SELF-ADJOINT operator with spectrum computable from the
#          BST primary integer set." -- SO AN OPERATOR IS NAMED. The question is WHICH DECOMPOSITION.
#   T2525: "a rank-2 bounded symmetric domain has exactly RANK+1 = 3 BOUNDARY SUPPORT STRATA
#          (Koranyi-Wolf: bulk / Cartan slice / Shilov)."
#   T2517: electron nu=5/2, muon nu=3/2 (Wallach degeneration, Cartan slice), tau nu=0 (Shilov).
#   T2528: "the SUPPORT-ORBIT RANK l (Rossi-Vergne ASSOCIATED VARIETY) names the boundary generation."
#   R71/R72 subscript rule: T2428's space is H^2_{lambda=0}. I will write it that way.

from math import comb
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5466 -- IS THE NAMED OPERATOR THE ONE A2 NEEDS?"); print(BAR)

head("PART A -- the named operator's eigenspaces: K-TYPES of H^2_{lambda=0}, indexed by d")
print("  T2428's Casimir acts on H^2_{lambda=0}; its eigenspaces are the K-types V_(d,0).")
print("   d      dim V_(d,0) = C(d+4,4) - C(d+2,4)")
for d in range(0,7):
    print("   %-6d %d"%(d, comb(d+4,4) - (comb(d+2,4) if d>=2 else 0)))
print("  *** THE INDEX IS d, AND IT RUNS OVER ALL NON-NEGATIVE INTEGERS -- INFINITELY MANY. ***")

head("PART B -- the generations' label: BOUNDARY SUPPORT STRATA, indexed by nu")
print("   generation   nu_strat   Koranyi-Wolf stratum        source")
for g,nu,st,src in (("electron/up-1","5/2","bulk (continuous Wallach)","T2517"),
                    ("muon/up-2","3/2","Cartan slice (degeneration)","T2517"),
                    ("tau/top","0","Shilov (degeneration)","T2517/T2528")):
    print("   %-12s %-10s %-27s %s"%(g,nu,st,src))
print("  *** THE INDEX IS nu_strat, IT RUNS OVER THE WALLACH SET, AND THERE ARE EXACTLY rank+1 = 3. ***")

head("PART C -- ★ THE DECIDING COMPARISON: are these the same decomposition?")
print("   property                  named Casimir (T2428)        generations (T2525/T2517)")
print("   %-25s %-28s %s"%("index","d = 0,1,2,3,...","nu_strat in {5/2, 3/2, 0}"))
print("   %-25s %-28s %s"%("how many","INFINITELY MANY","EXACTLY 3"))
print("   %-25s %-28s %s"%("what it decomposes","ONE space, H^2_{lambda=0}","DIFFERENT spaces H_nu"))
print("   %-25s %-28s %s"%("origin of the count","spectrum of an operator","rank+1, a STRATA COUNT"))
print()
print("  *** THEY ARE NOT THE SAME DECOMPOSITION, AND THE COUNT PROVES IT: ***")
print("      a spectrum on one space gives INFINITELY MANY eigenspaces (d unbounded).")
print("      The generations number EXACTLY THREE, and three comes from rank+1 -- A STRATA COUNT,")
print("      NOT A SPECTRUM. *** If generations were eigenspaces of the named operator there would")
print("      be infinitely many of them. There are three. ***")

head("PART D -- SO WHAT DOES A2 HAVE?")
print(" (1) THE OPERATOR EXISTS AND IS NAMED (T2428's Casimir). *** IT IS NOT THE OPERATOR A2 NEEDS. ***")
print("     It separates K-types WITHIN one space; the generations index DIFFERENT spaces H_nu.")
print(" (2) The group Casimir DOES distinguish different nu_strat -- but it distinguishes them as")
print("     INEQUIVALENT REPRESENTATIONS, i.e. as DIFFERENT HILBERT SPACES, not as orthogonal")
print("     subspaces of ONE Hilbert space. *** That is the wrong kind of separation for A2. ***")
print(" (3) ⟹ A2 IS NOT MERELY UNNAMED. As stated it has NO CANDIDATE in the corpus, and the")
print("     count (3 vs infinity) shows it cannot be repaired by picking a different eigenvalue.")

head("PART E -- AND IT PROPAGATES TO A1 AND A3, WHICH I ALSO ASSERTED")
print("  A1 said the three generations SPAN A 3-DIM SUBSPACE of one H. A3 said h LIES IN that span.")
print("  Both presuppose ONE Hilbert space containing all three as vectors. The corpus gives three")
print("  strata carrying three DIFFERENT spaces. *** NO EMBEDDING INTO A COMMON H HAS BEEN NAMED. ***")
print("  And my own 5456 sharpens it: two of the three addresses (3/2 and 0) are DISCRETE Wallach")
print("  DEGENERATIONS where the continuous family's normalization VANISHES (Gamma_Omega poles).")
print("  They are not three points of one continuous family; they are one generic point and two")
print("  degenerations. *** An embedding has to cross that, and nobody has built it. ***")

head("VERDICT")
print(" (1) *** A2 GOES. *** The one named self-adjoint operator decomposes K-types, not generations,")
print("     and the count (infinitely many vs exactly three) shows no eigenvalue relabelling fixes it.")
print(" (2) A1 and A3 fall with it -- all three presuppose an unnamed embedding into a common H.")
print(" (3) ⟹ *** THE SUM RULE y_1^2+y_2^2+y_3^2 = 1 REQUIRED A1-A3, SO IT WAS NEVER ESTABLISHED. ***")
print("     Keeper's 284x is computed INSIDE a structure nobody has built. His scoping was correct")
print("     ('under A1-A3') -- I am reporting that the scope condition FAILS, so the 284x does not")
print("     yet decide anything. *** NOT WRONG -- PREMATURE. And it was MY structure, not his. ***")
print(" (4) WHAT SURVIVES UNCONDITIONALLY: saturation is RANK ONE, so at most one generation can")
print("     saturate. That needs no embedding -- it is the equality case of an inequality.")
print(" (5) THE REAL QUESTION IS NOW SHARPER AND IT IS NOT MINE: *** what is the common Hilbert")
print("     space in which a Shilov-supported Higgs mode and three differently-stratified fermion")
print("     modes all live? *** Until that is named, no Yukawa OVERLAP is defined at all -- not")
print("     the top's, not the charm's. That is an object question: Lyra's.")
print()
print(" *** RULE 3: ONE CI -- ME. NOT FILED. Attack: (a) is there an embedding I failed to find --")
print("     I searched the registry by the object, not the word, but a null from ONE searcher is")
print("     exactly what today keeps punishing; (b) does the group Casimir argument in (2) hold, or")
print("     can inequivalent reps still sit orthogonally inside a larger space? (b) first. ***")
