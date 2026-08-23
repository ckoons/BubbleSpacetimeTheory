# TOY 5456 -- TYPING FLAG on the BRACKET's SIDE ONE (which is MY result, 5454).
# Elie, 2026-08-23. Rubric cell: External 3 (SM params) / lepton hierarchy.
#
# Arose while checking Keeper's R64 stand-down. His Wallach typing is CORRECT (T2517 registry:
# the lepton rho-addresses ARE nu_W values), so my overloading worry resolved in his favour --
# but verifying it surfaced something about the THREE ADDRESSES that I do not think anyone has stated.
#
# D_IV^5: rank r = 2, a = n_C - 2 = 3  =>  Wallach set = {0, 3/2} U (3/2, inf).
# T2517: electron nu = 5/2 ; muon nu = 3/2 (Wallach DEGENERATION, Cartan slice) ;
#        tau nu = 0 (Wallach DEGENERATION, Shilov points).
# => ONE address is in the CONTINUOUS part; TWO are DISCRETE degenerations.
#
# Gindikin Gamma (rank 2, a=3): Gamma_Omega(nu) ~ G(nu)G(nu - 3/2). The weighted-Bergman
# normalization ~ 1/Gamma_Omega, so a POLE of Gamma_Omega is a ZERO of the normalization =
# the continuous family DEGENERATES there.
#
# THIS IS A FLAG, NOT A RESULT. I do not run the alternative; it is a new object and Lyra pins it.

from mpmath import mp, mpf, gamma
mp.dps = 30
BAR = "="*100
print(BAR); print("TOY 5456 -- the three forced lepton addresses are TWO KINDS of Wallach point"); print(BAR)

print("\n   address        type in the Wallach set        G(nu)        G(nu-3/2)     Gamma_Omega")
for name, nu in [("electron 5/2", mpf(5)/2), ("muon 3/2", mpf(3)/2), ("tau 0", mpf(0))]:
    def sh(f):
        try:
            v = f()
            return "POLE" if (mp.isinf(v) or mp.isnan(v)) else mp.nstr(v, 7)
        except Exception:
            return "POLE"
    g1, g2 = sh(lambda: gamma(nu)), sh(lambda: gamma(nu - mpf(3)/2))
    go = "POLE -> normalization ZERO" if "POLE" in (g1, g2) else mp.nstr(gamma(nu)*gamma(nu-mpf(3)/2), 7)
    typ = "CONTINUOUS (above floor 3/2)" if nu > mpf(3)/2 else "DISCRETE Wallach point"
    print("   %-14s %-29s %-12s %-13s %s" % (name, typ, g1, g2, go))

print("\n   pole confirmation (eps -> 0):")
for lbl, base in [("nu = 3/2 + eps", mpf(3)/2), ("nu = 0 + eps", mpf(0))]:
    vals = [mp.nstr(gamma(base+mpf(e))*gamma(base+mpf(e)-mpf(3)/2), 6) for e in ('1e-3','1e-5','1e-7')]
    print("     %-16s 1e-3: %-14s 1e-5: %-14s 1e-7: %s" % (lbl, vals[0], vals[1], vals[2]))
print("     nu = 5/2 (electron):  Gamma_Omega = %s   FINITE, REGULAR"
      % mp.nstr(gamma(mpf(5)/2)*gamma(mpf(1)), 8))

print("\n"+BAR); print("THE FLAG"); print(BAR)
print(" (1) The three FORCED addresses are of TWO KINDS:")
print("     electron 5/2 -> CONTINUOUS part, Gamma_Omega finite, genuine bulk weighted-Bergman space")
print("     muon 3/2     -> DISCRETE Wallach point, Gamma_Omega POLE, degenerates to the Cartan slice")
print("     tau 0        -> DISCRETE Wallach point, Gamma_Omega POLE, degenerates to the Shilov boundary")
print()
print(" (2) *** ANY SINGLE ANALYTIC FORMULA IN nu TREATS ALL THREE AS ONE TYPE. *** That is exactly")
print("     what 5408 did -- six forms, one formula each, evaluated at all three addresses -- and it")
print("     is what SIDE ONE of the bracket measured as 'the nu axis is bounded / too flat'.")
print()
print(" (3) A formula analytic across the addresses CANNOT SEE a degeneration. So:")
print("     *** 'the nu axis is too flat' may be a statement about the FORMULA, not the GEOMETRY. ***")
print("     Side one is not overturned -- it is given an UNTESTED ALTERNATIVE EXPLANATION, and this")
print("     names the test: evaluate the norm at 3/2 and 0 on their OWN degenerate measures")
print("     (Cartan slice, Shilov boundary), NOT by analytic continuation in nu.")
print()
print(" (4) SAME DISEASE AS KEEPER'S R64 CATCH, MIRRORED. He found 'the self-shadow' was an overloaded")
print("     NAME covering a zero, a pole and a regular point. This is an overloaded SET: three")
print("     addresses covering one regular point and two degenerations. One letter, two kinds.")
print()
print(" (5) NOT RUN, DELIBERATELY. The degenerate-measure norm is a NEW OBJECT; per R63 rule 1 the")
print("     object gets pinned in writing before anyone computes, and that is Lyra's. Flag only.")
print("     Nothing pushed. CP existence-only.")
