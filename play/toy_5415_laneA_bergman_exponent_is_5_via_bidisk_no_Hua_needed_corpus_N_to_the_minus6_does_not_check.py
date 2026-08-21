import numpy as np
rng=np.random.default_rng(23)
print("="*104)
print("TOY 5415 -- LANE A: PIN THE BERGMAN EXPONENT. *** I CANNOT READ HUA (1963) — I do not have it.")
print("  So I do NOT pin to the page. Instead I verify the exponent by a route that needs no Hua. ***")
print("  FOUND IN CORPUS: 'Bergman kernel K(z,w) = 1920/pi^5 * N(z,w)^-6 | Hua (1963) | Classical'")
print("  FOUND IN CORPUS: Lyra F831 — 'FK genus = n_C = 5, NOT BST g = 7'.")
print("  *** THOSE TWO DISAGREE: exponent 6 vs genus 5. Both are in-corpus, neither verified to a page. ***")
print("="*104)

print("\nTABLE 1 -- *** THE INDEPENDENT CHECK: D_IV^2 is isomorphic to the BIDISK. ***")
print("  Standard map: (z1,z2) -> (u,v) = (z1 + i z2, z1 - i z2).")
print("  Type-IV norm  N(z,z) = 1 - 2<z,z_bar> + |z.z|^2 .  Claim: N(z,z) = (1-|u|^2)(1-|v|^2).")
print("   trial   N(z,z)            (1-|u|^2)(1-|v|^2)   |diff|")
worst=0
for t in range(6):
    z=(rng.normal(size=2)+1j*rng.normal(size=2))*0.25
    zz=complex(np.dot(z,z)); n2=float(np.vdot(z,z).real)
    N=1-2*n2+abs(zz)**2
    u=z[0]+1j*z[1]; v=z[0]-1j*z[1]
    P=(1-abs(u)**2)*(1-abs(v)**2)
    worst=max(worst,abs(N-P))
    print("   %-7d %-17.12f %-20.12f %.2e"%(t,N,P,abs(N-P)))
print("   *** N FACTORS EXACTLY (max dev %.1e). The type-IV norm IS the bidisk product. ***"%worst)

print("\nTABLE 2 -- *** SO THE EXPONENT IS FIXED BY THE DISK, WHICH NOBODY DISPUTES ***")
print("  Disk Bergman kernel: K_disk(u,u) = 1/(pi (1-|u|^2)^2)  -- exponent 2, classical.")
print("  Bidisk = product => K = K_disk(u) * K_disk(v) = (1/pi^2) [(1-|u|^2)(1-|v|^2)]^-2")
print("                                                = (1/pi^2) N(z,z)^-2 .")
print("   ==> *** for D_IV^2 the Bergman exponent is 2 = n. NOT n+1 = 3. ***")
print("  FK genus formula, with a = n-2 (my 5402 computed the Peirce dims (1,n-2,1) independently):")
print("     p = 2 + a(r-1) + b = 2 + (n-2) + 0 = n .   At n=2: p=2 ✓ matches the bidisk.")

print("\nTABLE 3 -- *** CROSS-CHECK ON THE OTHER LOW-RANK ISOMORPHISMS (genus is classical there) ***")
print("   domain     isomorphic to     that type's genus        D_IV^n genus = n ?")
rows=[("D_IV^2","disk x disk","2 (each disk genus 2, product)",2),
      ("D_IV^3","Sp(2,R)/U(2) = III_2","n+1 = 3 for III_n, n=2",3),
      ("D_IV^4","SU(2,2)/S(U2xU2) = I_{2,2}","p+q = 4 for I_{p,q}",4),
      ("D_IV^6","SO*(8)/U(4) = II_4","2n-2 = 6 for II_n, n=4",6)]
for a,b,c,d in rows:
    print("   %-10s %-17s %-24s %s"%(a,b,c,"*** %d = n ✓ ***"%d))
print("   *** FOUR independent classical isomorphisms, all giving genus = n. ***")
print("   ==> *** THE D_IV^5 BERGMAN EXPONENT IS 5, NOT 6. ***")

print("\nTABLE 4 -- ★★★ *** WHAT THIS SAYS ABOUT THE CORPUS'S HUA CITATION ***")
print("   corpus line: 'K(z,w) = 1920/pi^5 * N(z,w)^-6 | Hua (1963) | Classical'")
print("   *** The 1920/pi^5 PREFACTOR is consistent: Vol(D_IV^5) = pi^5/1920 (also Hua-attributed),")
print("       and K(0,0) = 1/Vol = 1920/pi^5 ✓ — the prefactor checks out independently. ***")
print("   *** The EXPONENT -6 does NOT check out: four classical isomorphisms give genus = n = 5. ***")
print("   POSSIBLE INNOCENT EXPLANATIONS I CANNOT RULE OUT WITHOUT THE PAGE:")
print("     (a) Hua normalizes N with a different power (e.g. N^{1/2} or a rank-1 convention);")
print("     (b) the corpus line transcribed the genus of a DIFFERENT domain in Hua's list;")
print("     (c) 6 was substituted from C_2 = 6 at some point (the n_C=5 coincidence again).")
print("   *** (c) is the one worth grepping: C_2 = 6 and 'exponent 6' at n_C = 5 is exactly the")
print("       collision class we just made a standing rule about. ***")

print("\n"+"="*104); print("VERDICT -- Lane A, Hua pin"); print("="*104)
print(" (1) ★★★★ *** I DID NOT DO THE ASSIGNED TASK AS WRITTEN: I do not have Hua (1963), so I cannot")
print("     pin anything 'to the page'. I will not cite a source I have not read — that is precisely")
print("     the failure this round warned about ('the unread source'). ***")
print()
print(" (2) *** BUT THE EXPONENT IS PINNABLE WITHOUT HUA, AND I PINNED IT: D_IV^2 is the BIDISK —")
print("     N(z,z) = (1-|u|^2)(1-|v|^2) verified exactly (max dev %.0e) — so its Bergman exponent is"%worst)
print("     2 = n from the DISK kernel alone. Three more classical isomorphisms (III_2, I_{2,2}, II_4)")
print("     agree. *** THE D_IV^5 BERGMAN EXPONENT IS 5. ***")
print()
print(" (3) ★★★ *** SO THE CORPUS'S HUA-ATTRIBUTED 'N^-6' IS WRONG, OR ITS N IS NOT MY N. *** The")
print("     PREFACTOR 1920/pi^5 independently checks (= 1/Vol), which makes the exponent the odd one")
print("     out. @Keeper — this is a cited-but-unverified line that three results may sit on.")
print()
print(" (4) *** AND THE MOST LIKELY INNOCENT CAUSE IS THE ONE WE JUST MADE A RULE ABOUT: C_2 = 6 at")
print("     n_C = 5. An exponent of 6 and a Casimir of 6 coincide only here. *** Worth a grep, not an")
print("     accusation — I cannot distinguish (a), (b), (c) without the page.")
print()
print(" (5) ⟹ PROMOTION STAYS BLOCKED, but for a SHARPER reason than 'Hua unread': *** the ratio 2")
print("     (nu_B/nu_S = n/(n/2)) is now independently verified and does NOT depend on Hua at all.")
print("     The RATIO can promote; the individual exponents need the page only to resolve the")
print("     corpus's own -6 line. ***")
