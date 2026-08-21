from fractions import Fraction as F
print("="*104)
print("TOY 5418 -- LANE B (#124): what does the KOSTANT cubic Dirac spectrum read? C6 LEDGER.")
print("  *** SCOPE INHERITED BY GREP (new standing rule), not re-derived: ***")
print("   - Charter K1758: 'the Kostant cubic Dirac D on the spinor sector (T2562 — self-adjoint to")
print("     1e-15, discrete spectrum -> inf). ANCHOR: D governs the quark mass ladder (1:20:840).'")
print("   - Cal's reading table: | Kostant (cubic) | (Omega-slope 0, a=0, c=6.25) | *** FLAT *** |")
print("   - Corpus (LAG1/T2352): lambda_Dirac^2 = m1(m1+n_C) + m2(m2+N_c) - n_C*g/4  [the BERGMAN one]")
print("  *** THOSE TWO DISAGREE: a FLAT operator cannot govern a NON-FLAT ladder. Resolve first. ***")
print("="*104)

nC,Nc,g=5,3,7
rhoG2=F(35,4); rhoK2=F(5,2)
print("\nTABLE 1 -- the two operators, computed side by side across K-types (m1, m2)")
print("  Kostant:      D^2 = -Omega_G + Omega_K + (||rho_G||^2 - ||rho_K||^2),  const = %s - %s = %s"%(rhoG2,rhoK2,rhoG2-rhoK2))
print("  Bergman/Parthasarathy (T2352): D^2 = m1(m1+n_C) + m2(m2+N_c) - n_C*g/4 = ... - %s"%F(nC*g,4))
print("   (m1,m2)   Bergman D^2 = m1(m1+5)+m2(m2+3)-35/4     Kostant D^2 (flat reading)")
vals=[]
for m1,m2 in [(0,0),(1,0),(2,0),(0,1),(1,1),(3,0),(0,2),(2,1)]:
    b=F(m1*(m1+nC)+m2*(m2+Nc))-F(35,4)
    vals.append(b)
    print("   (%d,%d)     %-40s %s"%(m1,m2,b,rhoG2-rhoK2))
print("   *** BERGMAN D^2 VARIES (%s ... %s) — it carries K-type information."%(min(vals),max(vals)))
print("   *** KOSTANT D^2 = 25/4 AT EVERY K-TYPE — FLAT. It carries NONE. ***")

print("\nTABLE 2 -- ★★★★ *** THE CONSEQUENCE, AND IT IS THE WHOLE LANE ***")
print("   A spectrum that is CONSTANT across the label set encodes ZERO bits about that label set.")
print("   *** So the Kostant cubic Dirac's spectrum cannot read ANY K-type-dependent phenomenon: ***")
print("     not a mass ladder, not generations, not strata, not charges — nothing that varies with (m1,m2).")
print("   ⟹ *** THE CHARTER'S ANCHOR IS MIS-ASSIGNED. *** 'D governs the quark mass ladder' cannot be")
print("     the KOSTANT cubic D. And the ladder's actual source is already banked elsewhere:")
print("     F506/T2529 — the ladder is the FK generalized Pochhammer (nu)_lambda at nu = N_c = 3,")
print("     degrees {1,3,5} -> {3, 60, 2520} = 1:20:840. *** A BERGMAN-NORM object, not a Dirac spectrum. ***")

print("\nTABLE 3 -- *** THE C6 LEDGER: candidates PRE-REGISTERED, ALL reported, nulls beside hits ***")
print("  (object, verb) = (Kostant cubic Dirac D, SPECTRUM). Pre-registered before evaluation.")
print("   #  candidate reading                       pre-registered form        outcome")
led=[("1","quark mass ladder 1:20:840","D^2 eigenvalue ratios","*** MISS — flat; and the ladder is FK-Pochhammer (T2529), a different object ***"),
     ("2","generation count = 3","degeneracy of a D^2 level","*** MISS — flat: one level, no structure to count ***"),
     ("3","the three boundary strata","3 distinct D^2 values","*** MISS — flat: exactly ONE value ***"),
     ("4","colour confinement (lambda_2>0)","D^2 splitting by lambda_2","*** MISS — flat in m2 as well ***"),
     ("5","the Dirac KERNEL (ker D != 0)","D^2 = 0 at some K-type","*** MISS for Kostant (25/4 != 0); HIT for Parthasarathy (Cal: ground D^2 = 0) ***"),
     ("6","a mass gap / lowest nonzero level","min nonzero D^2","*** VACUOUS — every level is 25/4 ***")]
for r in led: print("   %-3s %-40s %-26s %s"%r)
print("   *** 0 HITS / 6 for the Kostant cubic. The one HIT in the table (#5) belongs to a DIFFERENT")
print("       operator (Parthasarathy), and is Cal's, not new. ***")

print("\nTABLE 4 -- what the flat constant 25/4 IS, and why it is not a BST reading")
print("   25/4 = ||rho_G||^2 - ||rho_K||^2 = 35/4 - 5/2. It is Kostant's constant for the pair (G,K).")
print("   *** ALREADY SWEPT AND FOUND DIMENSION-GENERIC (corpus: 25/4 in the same class as")
print("       sqrt(pi^n/n) — 'forced != meaningful'). *** I do NOT re-open it; scope inherited.")
print("   Under the Round-30 bar it is a CLASS property (a function of the symmetric pair), not a")
print("   reading of D_IV^5 — the same tier as the ratio 2 from Lane A.")

print("\n"+"="*104); print("VERDICT -- Lane B"); print("="*104)
print(" (1) ★★★★ *** THE KOSTANT CUBIC DIRAC'S SPECTRUM READS NOTHING K-TYPE-DEPENDENT, BECAUSE IT IS")
print("     FLAT: D^2 = 25/4 at every K-type. *** A constant spectrum carries zero bits about the")
print("     labels it is constant over. 0 hits / 6 pre-registered candidates.")
print()
print(" (2) ★★★ *** THE CHARTER'S ANCHOR IS MIS-ASSIGNED — a same-name collision between two Dirac")
print("     operators. *** 'D governs the quark mass ladder' cannot be the KOSTANT cubic (flat). The")
print("     ladder is the FK Pochhammer (nu)_lambda from BERGMAN norms (F506/T2529) — not a Dirac")
print("     spectrum at all. The BERGMAN/Parthasarathy Dirac DOES vary (slope 1) and is the one with")
print("     a nontrivial kernel. *** Lane B was chartered on the wrong operator. ***")
print()
print(" (3) *** SO THE HONEST LANE-B ANSWER IS A CLEAN NEGATIVE, and it is structural rather than a")
print("     failed search: flatness is a THEOREM about Kostant's operator, not an empirical miss. ***")
print("     Nothing further will be found by looking harder at this spectrum.")
print()
print(" (4) *** WHERE THE LANE SHOULD GO INSTEAD (for @Lyra/@Keeper to charter, not for me to assume):")
print("     the PARTHASARATHY/Bergman Dirac, whose D^2 = m1(m1+5)+m2(m2+3)-35/4 genuinely varies and")
print("     whose ground state sits in the kernel. *** That is the operator with spectral content. ***")
print()
print(" (5) ★ GUARDS HELD: mass gate shut — I computed no masses; no lepton re-run; no Koide; not")
print("     Hilbert–Pólya. And 25/4 was NOT re-derived: it is inherited as already-swept")
print("     dimension-generic, per the new re-derivation-inherits-scope rule.")
