from fractions import Fraction as F
print("="*104)
print("TOY 5385 -- THE a,c INSTRUMENT: do the anomalies READ OUT which content the geometry took?")
print("  *** SPACE, LINE ONE: R^4 -- a and c are LOCAL invariants (5382). ***")
print("  Coefficients from my 5383 (units 1/360): scalar (1,3), Weyl (11/2,9), vector (62,36).")
print("="*104)
a_s,a_w,a_v = F(1),F(11,2),F(62)
c_s,c_w,c_v = F(3),F(9),F(36)
def ac(nv,nw,ns=4): return ns*a_s+nw*a_w+nv*a_v, ns*c_s+nw*c_w+nv*c_v

print("\nTABLE 1 -- the two forks, and what each changes")
print("   fork                       option A                   option B")
print("   complexification (#108)    SU(3): 8 gluons -> 12 vec  SO(3): 3 -> 7 vec")
print("   fermion content            48 Weyl (with nu_R)        45 Weyl (BST forbids nu_R, T1949/T1953)")
print("   (scalars held at 4 real = one Higgs doublet in all variants)")

print("\nTABLE 2 -- *** the four variants, computed ***")
print("   variant                          vectors  Weyl   a (/360)     c (/360)     a/c")
rows=[]
for gl,nv in [("SU(3) 8-gluon",12),("SO(3) 3-gluon",7)]:
    for nw in (48,45):
        a,c=ac(nv,nw); rows.append((gl,nw,nv,a,c,F(a,c)))
        print("   %-32s %-8d %-6d %-12s %-12s %.4f"%(gl+", "+str(nw)+" Weyl",nv,nw,str(a),str(c),float(F(a,c))))

print("\nTABLE 3 -- *** WHICH FORK DOES THE INSTRUMENT READ SHARPLY? ***")
su3=[r for r in rows if r[0].startswith("SU(3)")]; so3=[r for r in rows if r[0].startswith("SO(3)")]
print("   a/c by gluon count:  SU(3) -> %.4f, %.4f   |   SO(3) -> %.4f, %.4f"%(
      float(su3[0][5]),float(su3[1][5]),float(so3[0][5]),float(so3[1][5])))
sep=100*abs(float(su3[0][5])-float(so3[0][5]))/float(so3[0][5])
print("   *** COMPLEXIFICATION separation in a/c: %.1f%% -- LARGE, a clean read. ***"%sep)
w48=[r for r in rows if r[1]==48]; w45=[r for r in rows if r[1]==45]
sepw=100*abs(float(w48[0][5])-float(w45[0][5]))/float(w45[0][5])
print("   a/c by Weyl count (at fixed SU(3)): 48 -> %.4f, 45 -> %.4f"%(float(w48[0][5]),float(w45[0][5])))
print("   *** nu_R separation in a/c: %.1f%% -- SMALL. ***"%sepw)
print("   ==> *** the instrument reads the GAUGE fork sharply and the FERMION fork weakly. ***")

print("\nTABLE 4 -- *** now read it against what NATURE actually has ***")
print("   observable                     measured           which variant")
print("   gluon count                    8 (3-jet events)   *** SU(3) ***")
print("   nu_R as a gauge field          absent             *** 45 Weyl ***")
print("   Higgs doublet                  1 (4 real)         all variants")
a2,c2=ac(12,45)
print("   ==> nature's content is *** SU(3) + 45 Weyl ***:")
print("       *** a_SM = %s/360 = %s ,  c_SM = %s/360 = %s ,  a/c = %.4f ***"%(
      a2,F(a2,360),c2,F(c2,360),float(F(a2,c2))))
print("   ** this SUPERSEDES my 5384 a_SM = 1012/360, which used the generic 48 with nu_R.")
print("      @Grace's catch is right: BST's own content forbids nu_R, so 45 is the number. **")

print("\nTABLE 5 -- what the instrument therefore SAYS")
ageo,cgeo=ac(7,45)
print("   fully-geometric content (SO(3) + 45): a = %s, c = %s, a/c = %.4f"%(ageo,cgeo,float(F(ageo,cgeo))))
print("   nature's content     (SU(3) + 45):    a = %s, c = %s, a/c = %.4f"%(a2,c2,float(F(a2,c2))))
print("   ==> *** the gap between them IS the complexification import, in numbers: ***")
print("       Delta a = %s (%.1f%%),  Delta c = %s (%.1f%%),  Delta(a/c) = %.1f%%"%(
      a2-ageo,100*float((a2-ageo)/ageo),c2-cgeo,100*float((c2-cgeo)/cgeo),
      100*abs(float(F(a2,c2))-float(F(ageo,cgeo)))/float(F(ageo,cgeo))))

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** THE INSTRUMENT WORKS, AND IT IS ASYMMETRIC: *** a/c separates the COMPLEXIFICATION")
print("     fork by %.1f%% (SU(3) ~1.16 vs SO(3) ~1.01) and the nu_R fork by only %.1f%%."%(sep,sepw))
print("     *** So a,c read the GAUGE content sharply and the FERMION count weakly. *** Worth knowing")
print("     before anyone leans on them to settle 45-vs-48 -- they barely can.")
print()
print(" (2) *** I SUPERSEDE MY OWN 5384 a_SM. *** @Grace is right: BST forbids nu_R (T1949/T1953), so")
print("     BST's content is 45 Weyl, not the generic 48. Corrected:")
print("       *** a_SM = %s/360 ,  c_SM = %s/360 ,  a/c = %.4f *** (was 1012/360, 876/360)"%(
      a2,c2,float(F(a2,c2))))
print("     And 45 is ALSO what nature shows -- no nu_R as a gauge field -- so BST and the data agree")
print("     on the fermion content here.")
print()
print(" (3) *** AND THE INSTRUMENT READS THE #108 BOUNDARY AS A NUMBER: *** the fully-geometric")
print("     content (SO(3) + 45) gives a/c = %.4f; nature gives %.4f. *** That %.1f%% gap IS the"%(
      float(F(ageo,cgeo)),float(F(a2,c2)),100*abs(float(F(a2,c2))-float(F(ageo,cgeo)))/float(F(ageo,cgeo))))
print("     complexification import, quantified. *** The geometry-only content is excluded by data")
print("     (gluons are observed) -- which is container-yes-mechanism-open, restated numerically.")
print()
print(" (4) SCOPE, UNCHANGED: a and c are CONTENT-DETERMINED. This toy uses them as an INSTRUMENT to")
print("     label which content is in play -- it does NOT predict them. *** Reading a dial is not")
print("     building the dial. *** And everything upstream still waits on @Cal's T2551 completeness vet.")
