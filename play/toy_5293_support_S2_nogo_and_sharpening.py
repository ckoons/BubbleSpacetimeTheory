import numpy as np
print("="*92)
print("(A) THE S2 CHECK: does the R^4 no-go, AS STATED, also block things that demonstrably EXIST?")
print("="*92)
print("  The mechanism as written: 'the gap is a BULK property of D_IV^5; R^4-alone cannot carry it.'")
print("  That sentence names NO gauge group and NO dimension. So run it against its false neighbours.\n")
neigh=[
 ("free/abelian U(1) gauge theory on R^4",
  "RIGOROUSLY CONSTRUCTED (Gaussian measure, textbook)",
  "no bulk needed -- the loose no-go would block a construction that EXISTS"),
 ("phi^4 in d=2 (Glimm-Jaffe)",
  "RIGOROUSLY CONSTRUCTED, and MASSIVE (has a gap)",
  "a gap built natively on FLAT space, no bulk"),
 ("phi^4 in d=3 (Glimm-Jaffe/Feldman-Osterwalder)",
  "RIGOROUSLY CONSTRUCTED, and MASSIVE (has a gap)",
  "again a flat-space gap -- 'flat space cannot carry a constructed gap' is FALSE"),
 ("SU(3) YM on a 4D lattice",
  "gap MEASURED numerically (glueball spectrum)",
  "the gap is demonstrably THERE on discretised R^4; what is missing is a CONSTRUCTION"),
]
for a,b,c in neigh:
    print("   - %-42s %s\n       -> %s"%(a,b,c))
print("\n  ⟹ THE LOOSE NO-GO PROVES TOO MUCH, ON THREE FRONTS:")
print("     (1) it would block ABELIAN R^4 gauge theory, which is rigorously constructed;")
print("     (2) it would block phi^4_2 and phi^4_3, which are rigorously constructed WITH gaps on")
print("         flat space -- so 'flat space cannot carry a gap' is simply false;")
print("     (3) it never mentions N_c, so it cannot distinguish the case that is actually hard.")
print("  ⟹ AND (4), the subtler one: the gap on discretised R^4 is MEASURED. So the no-go cannot be")
print("     about the gap's EXISTENCE at all -- only about the rigorous CONSTRUCTION. Those are")
print("     different claims and the draft must not slide between them.")
print()
print("="*92)
print("(B) THE SHARPENING: what is genuinely NON-ABELIAN-specific and d=4-specific?")
print("="*92)
print("  one-loop beta:  b_0 = 11 N/3 - 2 n_f/3.  The 11N/3 term is the GLUON SELF-INTERACTION.")
print("  It is EXACTLY ZERO for an abelian group -- photons do not couple to photons.\n")
print("      group        N     11N/3      b_0 (n_f=0)   b_0 (n_f=6)    asymptotically free?")
for name,N in [("U(1) abelian",0),("SU(2)",2),("SU(3)",3),("SU(5)",5)]:
    t=11*N/3
    print("    %-12s %3d   %8.3f   %11.3f   %11.3f      %s"%(
        name,N,t,t-0,t-4.0,"YES" if t-4.0>0 else "NO (abelian: b_0<0, IR-free)"))
print("\n  ⟹ the 11N/3 term IS the abelian/non-abelian discriminator, and it is a NUMBER, not a story.")
print("     Any BST no-go must be CONDITIONED ON IT, or it applies to the photon too.")
print()
print("  and the d=4 half -- why FOUR dimensions is the hard case:")
print("      [g^2] has mass dimension 4 - d, so the coupling is:")
for d in [2,3,4,5]:
    dim=4-d
    kind="SUPER-renormalisable (dim>0, easy)" if dim>0 else ("MARGINAL (dim=0, the hard case)" if dim==0 else "non-renormalisable (dim<0)")
    print("        d=%d : [g^2] = %+d   -> %s"%(d,dim,kind))
print("  ⟹ phi^4_2 and phi^4_3 are constructible precisely BECAUSE the coupling is super-renormalisable.")
print("     d=4 is marginal -- that is why Clay-YM is hard, and it is a DIMENSION statement, not a")
print("     bulk-vs-flat statement.")
print()
print("  ★ SHARPENED NO-GO (the form that survives S2):")
print("     'No R^4-native construction is available for a theory that is MARGINAL (d=4) AND")
print("      ASYMPTOTICALLY FREE (b_0 > 0, i.e. non-abelian) -- the two conditions that jointly force")
print("      dimensional transmutation, so the gap cannot be read off the Lagrangian.'")
print("     This excludes abelian (b_0 < 0), excludes phi^4_{2,3} (not marginal), and is silent about")
print("     the gap's EXISTENCE on the lattice. Those are exactly the four false neighbours.")
