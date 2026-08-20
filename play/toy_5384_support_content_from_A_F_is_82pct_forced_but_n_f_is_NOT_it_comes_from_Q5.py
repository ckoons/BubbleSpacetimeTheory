from fractions import Fraction as F
print("="*104)
print("TOY 5384 -- THE CONTENT <- A_F MAP: what does the a,c credential BUY if T2551 clears?")
print("  *** CONDITIONAL: everything below is gated on @Grace/@Cal hardening A_F = C (+) H (+) M_3. ***")
print("  *** SPACE, LINE ONE: R^4 -- a and c are LOCAL invariants (5382). ***")
print("="*104)

print("\nTABLE 1 -- the field content that follows from A_F = C (+) H (+) M_3")
print("   sector     content                                    count   forced BY A_F?")
print("   gauge      U(1) x SU(2) x SU(3) -> 1 + 3 + 8 vectors   12      *** YES -- the algebra IS the gauge group ***")
print("   fermions   per generation: Q_L 6, u_R 3, d_R 3,")
print("              L_L 2, e_R 1, nu_R 1  =  16 Weyl            16/gen  *** YES -- the A_F-bimodule structure ***")
print("   generations multiplicity                               3       *** NO -- not in A_F ***")
print("   scalars    one complex Higgs doublet = 4 real          4       *** NO -- comes from D_F, not A_F ***")

print("\nTABLE 2 -- *** so compute a and c for the SM content, using my 5383 coefficients ***")
Ns,Nw,Nv = 4, 16*3, 12
a_s,a_w,a_v = F(1),F(11,2),F(62)
c_s,c_w,c_v = F(3),F(9),F(36)
a = Ns*a_s + Nw*a_w + Nv*a_v
c = Ns*c_s + Nw*c_w + Nv*c_v
print("   (units of 1/360, per 5383: scalar (1,3), Weyl (11/2,9), vector (62,36))")
print("   sector     N     a-contribution        c-contribution")
for nm,N,av,cv in [("real scalars",Ns,a_s,c_s),("Weyl fermions",Nw,a_w,c_w),("vectors",Nv,a_v,c_v)]:
    print("   %-13s %-5d %-21s %s"%(nm,N,str(N*av),str(N*cv)))
print("   %-13s %-5s %-21s %s"%("TOTAL","",str(a),str(c)))
print("   ==> *** a_SM = %s/360 = %s ,  c_SM = %s/360 = %s ***"%(a,F(a,360),c,F(c,360)))
print("       a/c = %s = %.4f"%(F(a,c),float(F(a,c))))

print("\nTABLE 3 -- *** THE AUDIT: forced by A_F vs imported (the assigned question) ***")
print("   contribution        a-share    forced by A_F?              why")
tot=a
for nm,val,st,why in [("vectors (12)",Nv*a_v,"*** FORCED ***","the algebra determines the gauge group"),
                      ("fermions/gen (16)",F(16)*a_w,"*** SHAPE FORCED ***","A_F-bimodule fixes 16 per generation"),
                      ("x generation count 3",F(32)*a_w,"*** IMPORTED ***","N_gen is NOT in A_F"),
                      ("scalars (4)",Ns*a_s,"*** IMPORTED ***","comes from D_F, not A_F")]:
    print("   %-19s %-10s %-27s %s"%(nm,str(val),st,why))
print("\n   forced-by-A_F share of a: vectors %s + one generation's fermions %s = %s of %s = %.1f%%"%(
      Nv*a_v, F(16)*a_w, Nv*a_v+F(16)*a_w, a, 100*float((Nv*a_v+F(16)*a_w)/a)))

print("\nTABLE 4 -- *** and the n_f question, answered ***")
print("   n_f (quark flavours) = 2 x N_gen = 6")
print("   is N_gen in A_F?  *** NO. *** A_F fixes the content PER generation; the multiplicity is separate.")
print("   BST forces N_gen = 3 from Q^5 cohomology (h^1, h^3, h^5) -- a DIFFERENT banked result.")
print("   ==> *** n_f is NOT forced by A_F. It is forced by Q^5 -- and per Bar 1, crediting A_F with")
print("       it would DOUBLE-COUNT one fact across two lines. ***")

print("\n"+"="*104)
print("VERDICT -- conditional on the T2551 gate")
print("="*104)
print(" (1) *** IF A_F CLEARS, THE UPGRADE IS PARTIAL, NOT TOTAL -- and the split is clean: ***")
print("       FORCED by A_F : the 12 vectors (the algebra IS the gauge group) and the 16-Weyl")
print("                       SHAPE per generation (the bimodule structure).")
print("       NOT forced    : the generation MULTIPLICITY (3) and the scalar sector (from D_F).")
print("     So the central-charge credential upgrades on the gauge sector and the per-generation")
print("     fermion shape -- *** roughly %.0f%% of a *** -- and stays bookkeeping on the rest."%(
      100*float((Nv*a_v+F(16)*a_w)/a)))
print()
print(" (2) *** THE NUMBERS, READY FOR THE MOMENT THE GATE CLEARS: a_SM = %s/360, c_SM = %s/360, ***"%(a,c))
print("     computed from my 5383 coefficients with the SM content (4 real scalars, 48 Weyl, 12")
print("     vectors). These are checkable against the literature -- @Grace, another clean")
print("     second-source target.")
print()
print(" (3) *** n_f IS NOT FORCED BY A_F. *** A_F fixes content PER GENERATION; the multiplicity is")
print("     not in the algebra. BST gets N_gen = 3 from Q^5 cohomology -- a separate banked result.")
print("     *** So the AF-scope question closes NEGATIVE for A_F, and crediting A_F with n_f would")
print("     double-count Q^5 across two lines (Bar 1). ***")
print()
print(" (4) SCOPE, HELD: this whole toy is CONDITIONAL. @Grace/@Cal own the T2551 hardening and")
print("     *** nothing here upgrades anything until that clears. *** I have computed what the")
print("     upgrade BUYS, not that it is available.")
print()
print(" (5) AND THE HONEST CEILING EVEN IF IT ALL CLEARS: a and c are CONTENT-DETERMINED functions.")
print("     Forcing the content makes them PREDICTED rather than fitted -- but they remain")
print("     *** consequences of the spectrum, not independent tests of it. *** One fact (the content),")
print("     two readings (a and c). Bar 1 again.")
