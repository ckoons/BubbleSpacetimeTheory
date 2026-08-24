# TOY 5490 -- K1749-B PIN v2, THE COMPUTE. Elie, 2026-08-24. Last shot: win or close.
# Field 1': exponents = ord_Z = (1,0,0) -- electron = RESIDUE of Z at 5/2; muon, tau = Z's
# finite values. Fields 2-4 inherited verbatim: K_j(0,0) = 1/mass_j; direction larger-kernel =
# larger-mass; WIN = K_{5/2} < K_{3/2} < K_0 both strict; LOSS = any violation; budget: 0/inf
# anywhere => lane closes forever.
from mpmath import mp, mpf, gamma, pi, sqrt
mp.dps=40
BAR="="*100
print(BAR); print("TOY 5490 -- pin v2: the ordinal claim, scored"); print(BAR)
print("Z(nu) = pi^5 G(nu-5/2)G(nu-4)/[G(nu)G(nu-3/2)]  (MC-gated in 5489, gate inherited).")
print("Common pi^5 cancels in an ORDINAL claim; masses reported in pi^5 units, exact.")

def Zred(nu,eps=mpf('1e-20')):
    n=mpf(nu)+eps
    return gamma(n-mpf(5)/2)*gamma(n-4)/(gamma(n)*gamma(n-mpf(3)/2))
print("\nPART A -- the three masses under ord_Z = (1, 0, 0):")
e=mpf('1e-12')
m_e  = e*Zred(mpf(5)/2,e)          # residue (order-1)
m_mu = Zred(mpf(3)/2)              # finite value
m_ta = Zred(mpf(0))                # finite value
print("   electron  mass = Res_{5/2} Z = %s   (exact: 16/9  = %s)"%(mp.nstr(m_e,8),mp.nstr(mpf(16)/9,8)))
print("   muon      mass = Z(3/2)      = %s   (exact: 16/15 = %s)"%(mp.nstr(m_mu,8),mp.nstr(mpf(16)/15,8)))
print("   tau       mass = Z(0)        = %s  (exact: -1/60 = %s)"%(mp.nstr(m_ta,8),mp.nstr(-mpf(1)/60,8)))
print("   exactness check: |num - exact| = %.1e, %.1e, %.1e"%(abs(m_e-mpf(16)/9),abs(m_mu-mpf(16)/15),abs(m_ta+mpf(1)/60)))
print("\n   BUDGET CHECK first: any 0 or infinity? NO -- all three finite and nonzero.")
print("   *** THE COMPARISON RUNS. This is a SCORED outcome, not an abort. ***")
print("\nPART B -- the kernels and the ordinal claim:")
K_e,K_mu,K_ta = 1/m_e, 1/m_mu, 1/m_ta
print("   K_{5/2}(0,0) = %s      (9/16  in 1/pi^5 units)"%mp.nstr(K_e,8))
print("   K_{3/2}(0,0) = %s      (15/16)"%mp.nstr(K_mu,8))
print("   K_0(0,0)     = %s     (-60)  *** NEGATIVE ***"%mp.nstr(K_ta,8))
print("\n   WIN requires: K_{5/2} < K_{3/2} < K_0, both strict.")
print("   first  inequality K_{5/2} < K_{3/2}:  %s  (0.5625 < 0.9375 -- the e < mu leg HOLDS)"%(K_e<K_mu))
print("   second inequality K_{3/2} < K_0   :  %s  (0.9375 < -60 is FALSE)"%(K_mu<K_ta))
print("\n" + BAR)
print("VERDICT -- *** LOSS. THE ORDINAL CLAIM FAILS AT THE TAU. THE SHOT DIES, in my own Part-B")
print("words from 5487: 'if they do not, the shot dies and says so.' ***")
print(BAR)
print(""" (1) SCORED, not aborted: all three functionals finite and nonzero, the comparison ran,
     the second inequality failed. Per the budget: THE LANE CLOSES -- and it closes on a
     RESULT, which is better than closing on a third abort.
 (2) The failure has STRUCTURE, reported not spun:
     - the e < mu leg HOLDS (9/16 < 15/16) -- the direction was right where both kernels are
       kernels of actual Hilbert spaces;
     - the tau's kernel is NEGATIVE: Z(0) = -1/60 < 0 because G(-5/2)/G(-3/2) = -2/5. The
       nu = 0 continuation of the mass is a SIGNED object -- the trivial-rep endpoint does not
       carry a positive residue measure in this family. A negative 'kernel at the base point'
       is not a localization price; it is the family saying the tau address is not IN it.
 (3) CONSONANCE QUARANTINE HONORED: I cite nothing about F2/self-duality; the rhyme stays
     quarantined per the pin. The must-fail control is MOOT on a loss (it guards wins).
 (4) 5487's FINAL STATE: the inversion OBSERVATION stands (3 monotone points, public data);
     the named MECHANISM is dead at its own pre-registered test; NO THIRD PIN exists or will.
     The register keeps the observation as a shape with no mechanism -- honestly labelled.
 (5) Nothing banked. Lane K1749-B: CLOSED, twice-instrumented, budget honored.""")
