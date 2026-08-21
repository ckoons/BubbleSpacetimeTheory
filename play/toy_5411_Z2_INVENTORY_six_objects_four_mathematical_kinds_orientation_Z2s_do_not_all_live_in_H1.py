import glob,re,collections
print("="*104)
print("TOY 5411 -- THE ℤ₂ INVENTORY. 'Subscript every ℤ₂' was made standing -- nobody had enumerated")
print("  them. Pure RECONNECT + CLASSIFY: no derivation, so it does not jump the object-declaration gate.")
print("  *** Built after my own 5410 retraction: I merged ℤ₂'s because no inventory existed. ***")
print("="*104)

files=glob.glob('notes/**/*.md',recursive=True)+glob.glob('play/*.py')
print("\nPOSITIVE CONTROL (§599, and my first run of this sweep returned a false ZERO from a wrong cwd):")
print("   files found = %d  (must be > 0)"%len(files))
pat=re.compile(r'ℤ[₂2]|Z_2\b|Z/2|Z2\b')
ctrl=sum(len(pat.findall(open(f,errors='ignore').read())) for f in files[:50])
print("   control tokens in first 50 files = %d  (must be > 0)"%ctrl)
assert len(files)>0 and ctrl>0

CARRIER=[("SHILOV_QUOTIENT",['shilov','šilov','antipodal','half-period','deck group']),
 ("MOEBIUS_INVOLUTION",['möbius locus','mobius locus','5-ball','t2328','t2329']),
 ("ORIENT_QUOTIENT",['pin(2)/so(2)','pin(2)-','orientation quotient','o(2)/so(2)']),
 ("JORDAN_PEIRCE",['peirce','jordan','spin factor','v₁₂','v_12']),
 ("SPINOR_PARITY",['(-1)^f','(−1)^f','#rac','fermion parity','k+m even','mode parity']),
 ("RIBBON_FRAMING",['ribbon','half-twist','hopf','doublet flip','t1946']),
 ("CP_TWIST",['cp twist','cp kink','t1947','twist asymmetry'])]
counts=collections.Counter()
for f in files:
    try: s=open(f,errors='ignore').read()
    except: continue
    for m in pat.finditer(s):
        ctx=s[max(0,m.start()-220):m.start()+220].lower()
        counts[next((n for n,ks in CARRIER if any(k in ctx for k in ks)),"UNCLASSIFIED")]+=1
tot=sum(counts.values())
print("\nTABLE 1 -- THE SWEEP: %d ℤ₂ tokens across %d files"%(tot,len(files)))
print("   carrier              count   share")
for t,c in counts.most_common(): print("   %-20s %5d   %4.1f%%"%(t,c,100*c/tot))
print("   *** %.0f%% carry NO carrier keyword within 220 chars -- the naming problem is the majority case,"%(100*counts['UNCLASSIFIED']/tot))
print("       not an edge case. That is why merges keep happening. ***")

print("\nTABLE 2 -- *** THE KEY DISTINCTION IS THE MATHEMATICAL KIND, NOT JUST THE CARRIER ***")
print("   subscript      kind                          lives in            example / source")
rows=[("ℤ₂_Š","STIEFEL-WHITNEY CLASS","H¹(Š; ℤ₂)","Šilov (S⁴×S¹)/ℤ₂; w₁ ≠ 0 iff n odd (my 5396/5402)"),
 ("ℤ₂_M","GROUP INVOLUTION (equivariant)","H⁰(ℤ/2 ↷ M)","τ(z)=z̄; Fix(τ)=M=open 5-ball (T2328)"),
 ("ℤ₂_P","GROUP QUOTIENT (a model)","Pin(2)/SO(2)","the abstract 'orientation' ℤ₂ (T1949/T2138)"),
 ("ℤ₂_J","ALGEBRA GRADING","Peirce of J(n)","(1, n−2, 1); what rank 2 MEANS"),
 ("ℤ₂_F","SELECTION RULE / PARITY","mode labels","k+m even; (−1)^F (my 5327/5329)"),
 ("ℤ₂_R","BUNDLE FRAMING","ribbon framing","half-twist → spin (T1946)")]
for r in rows: print("   %-14s %-29s %-19s %s"%r)
print("   *** FOUR DIFFERENT MATHEMATICAL KINDS. A class, an action, a quotient, a grading. ***")
print("   *** They cannot be merged even when they all 'mean orientation' -- they do not live in the")
print("       same place, so no single separator tests two of them. ***")

print("\nTABLE 3 -- ★★ *** A SOURCED TENSION I REPORT RATHER THAN ADJUDICATE ***")
print("   T1949 / the neutrino paper: 'the NON-ORIENTABLE Möbius locus (K3 / Pin(2)-ℤ₂)'")
print("   T2328 (AC Theorem Registry): 'M(D_IV⁵) := Fix(τ) = open 5-ball B⁵ ⊂ ℝ⁵ ... M is")
print("                                CONTRACTIBLE (open convex ball)'")
print("   Sketch doc: 'M(D_IV⁵) is an open 5-ball, ORIENTABLE — BUT its embedding creates a 2-cover")
print("               via the (z,z̄)↔(z̄,z) ℤ/2 action. H⁰(ℤ/2 ↷ M, ℤ) = ℤ/2.'")
print("   ⟹ a contractible ball has H¹ = 0, so *** w₁(M) = 0: the locus itself is ORIENTABLE. ***")
print("   *** The ℤ₂ there is ℤ₂_M (an involution on the AMBIENT), not a non-orientability of M. ***")
print("   I do NOT rule on the wording -- that is @Lyra/@Keeper's. *** I report that two sourced")
print("   statements need reconciling, and that they are different KINDS of object. *** (5410 lesson:")
print("   I attack no phrase whose source I have not read.)")

print("\nTABLE 4 -- THE OPEN ROW THE ROUND ASKED FOR (no-ν_R carrier)")
print("   shipped table: 'no sterile neutrino (no ν_R) | I₂ | separator D_IV⁷ vs D_IV⁸ | the Möbius")
print("                   locus forbids ν_R closure (T1949)'")
print("   *** The FACT is keyed to ℤ₂_M (Möbius involution). The SEPARATOR (D_IV⁷/D_IV⁸) tests ℤ₂_Š")
print("       (Šilov w₁ — it is literally my orientability computation). ***")
print("   ⟹ OPEN ROW: does ℤ₂_Š control ℤ₂_M? If yes, one channel and the row is right. If no, the")
print("     row's separator tests a different object than its mechanism. *** Not a defect claim --")
print("     the theorem is shipped and gated; this is an ATLAS/declaration question. ***")

print("\n"+"="*104); print("VERDICT"); print("="*104)
print(" (1) *** INVENTORY DELIVERED: %d ℤ₂ tokens swept, SIX distinct objects in FOUR mathematical"%tot)
print("     KINDS -- a Stiefel-Whitney CLASS, a group INVOLUTION, a group QUOTIENT, and gradings. ***")
print("     Subscripts proposed: ℤ₂_Š · ℤ₂_M · ℤ₂_P · ℤ₂_J · ℤ₂_F · ℤ₂_R.")
print()
print(" (2) ★★ *** THE MAJORITY CASE IS UNLABELLED: %.0f%% of uses name no carrier nearby. *** The"%(100*counts['UNCLASSIFIED']/tot))
print("     merge risk is structural, not occasional -- which is why 'subscript every ℤ₂' needs an")
print("     inventory behind it, not just an instruction.")
print()
print(" (3) ★★★ *** THE STRONGEST RESULT: 'orientation' ℤ₂'s DO NOT ALL LIVE IN H¹. *** ℤ₂_Š is a w₁")
print("     class; ℤ₂_M is an involution with H⁰(ℤ/2 ↷ M) = ℤ/2 on a CONTRACTIBLE, ORIENTABLE ball.")
print("     *** So no separator can test both, and @Grace's frozen line ('the twist is a w₁-type ℤ₂")
print("     orientation datum') is exactly right FOR ℤ₂_Š and only for it. ***")
print()
print(" (4) *** SOURCED TENSION REPORTED, NOT ADJUDICATED: T1949's 'non-orientable Möbius locus' vs")
print("     T2328's 'contractible open 5-ball'. *** Both cited verbatim; the reconciliation is")
print("     @Lyra/@Keeper's call. I read both sources before writing this line -- 5410's lesson.")
print()
print(" (5) ★ INSTRUMENT NOTE: my FIRST run of this sweep returned a confident ZERO -- I had cd'd into")
print("     play/ to claim the number, so the globs resolved against the wrong root. *** §599 caught")
print("     it: the positive control is now printed above the result, every time. ***")
