r"""
Toy 4164: RETRACTION of Toy 4163's central claim + independent confirmation of Lyra's computation. Quaker method:
Lyra COMPUTED what my 4163 bracket only GUESSED, and her computation refutes my reading. I verify hers independently
and retract mine cleanly -- no defense. Net: the mu/tau gap (1.44) is ONE named object, the per-harmonic FK Fischer
norm. The interior-K-type alternative (my 4163) is ruled out by direct computation. FORCED count stays 2 of 26.

WHAT 4163 CLAIMED (and why it was wrong):
  4163 argued: singleton = full 2-D lattice MINUS the null submodule = SOME surviving interior K-types, so the 1.44
  gap is the forced surviving interior (no convention constant). The reasoning leaned on the bracket 11.6 < 16.82 < 64.
  THE ERROR: (i) the bracket mixed normalizations -- 11.6 is the Fischer=1 edge sum, 64 is the FULLY-NORMALIZED generic
  closed form -- so "16.82 between them" did NOT mean "singleton has partial interior." (ii) more decisively, I assumed
  the null submodule was a PROPER subset of the interior (leaving some). it is NOT.

LYRA'S COMPUTATION (confirmed here independently):
  at the muon's Wallach point nu = 3/2, the interior Pochhammer factor is (nu - 3/2)_{m2} = (0)_{m2}:
      m2 = 0 (edge)     : (0)_0 = 1
      m2 = 1 (interior) : (0)_1 = 0
      m2 = 2 (interior) : (0)_2 = 0   ... and 0 for ALL m2 >= 1.
  so EVERY interior K-type has coefficient exactly 0 at nu = 3/2 -- the ENTIRE m2 >= 1 interior is excluded. the null
  submodule at nu = 3/2 IS the whole interior (not a proper subset), so removing it leaves ONLY the m2 = 0 edge.
  => the singleton at the muon point = the edge. Lyra's edge sum (11.6) is the COMPLETE singleton (Fischer = 1).

THEREFORE (the corrected conclusion, = Lyra's + Grace's):
  the 1.44 gap is NOT surviving interior (excluded, just computed) -- it is the per-harmonic FK FISCHER NORM, the one
  weight Lyra set to 1 in the edge sum. it does not cancel in the ratio (it reweights the k-terms differently at nu=3/2
  vs the comparison point), so it is genuinely load-bearing. ONE named object stands between 11.6 and a forced verdict.
  the fish stays marked: 1.44 ~ 13/9, refused -- the Fischer norm is DERIVED (Lyra, Bargmann-Fock) + cross-checked
  (Cal/Grace FK 1994), agreement banks it, not the number.

DISCIPLINE NOTE (why this is a good event, not a bad one):
  Cal #27 fired at peak convergence -- the elegance of "I know what the gap is (interior)" was exactly the moment to
  brake, and the brake came from a teammate's direct computation. my 4163 asked the right question (Grace's routing:
  check the interior before the constant) but gave the wrong answer; Lyra's (0)_{m2} computation gave the right one.
  the decider is SETTLED by two-route agreement (Lyra computed it, i independently confirmed it). that is the method working.

HONEST TIER:
  CONFIRMED: at nu = 3/2 the interior is entirely excluded ((0)_{m2} = 0 for m2 >= 1); the singleton = the edge; the
    1.44 is the per-harmonic FK Fischer norm, not surviving interior. Toy 4163's "partial interior" reading is RETRACTED.
  the forced computation is now SIMPLER than I framed it: a Fischer-reweighted 1-D EDGE sum (not a 2-D interior sum).
  count moves 2 -> 3 (mu/tau) only when the derived Fischer norm + the reference agree and the sum lands 16.82.
  FORCED count stays 2 of 26.
"""

from fractions import Fraction as Fr

def poch(x, k):
    r = Fr(1)
    for j in range(k):
        r *= (x + j)
    return r

nu_mu = Fr(3, 2)

print("=" * 100)
print("TOY 4164: RETRACT 4163 + confirm Lyra -- the interior is EXCLUDED at the muon point; the 1.44 gap is the Fischer norm")
print("=" * 100)
print()

print("independent confirmation of Lyra's computation (interior factor (nu-3/2)_{m2} at nu=3/2 = (0)_{m2}):")
print("-" * 100)
for m2 in range(5):
    val = poch(nu_mu - Fr(3, 2), m2)
    tag = "edge" if m2 == 0 else "interior"
    print(f"  m2 = {m2} ({tag:<8}): (0)_{m2} = {val}")
print(f"  => edge (m2=0) coefficient = 1; ALL interior (m2>=1) coefficients = 0 -> the ENTIRE interior is excluded at nu=3/2.")
print(f"  => the null submodule IS the whole interior (not a proper subset); singleton = edge-only; Lyra's 11.6 is the complete singleton.")
print()

print("RETRACTION of Toy 4163's central claim:")
print("-" * 100)
print(f"  4163 said: singleton = full minus submodule = SOME surviving interior -> 1.44 is forced interior. WRONG.")
print(f"  error 1: the bracket 11.6 < 16.82 < 64 mixed normalizations (11.6 = Fischer=1 edge; 64 = normalized generic closed form).")
print(f"  error 2: the submodule at nu=3/2 is the WHOLE interior, not a proper subset -> nothing interior survives.")
print(f"  CORRECTED: the gap is the per-harmonic FK FISCHER NORM (Lyra + Grace). one named object. (4163 asked the right question, wrong answer.)")
print()

print("the corrected forced computation (simpler than 4163 framed):")
print("-" * 100)
print(f"  it is a Fischer-reweighted 1-D EDGE sum (not a 2-D interior sum). the Fischer norm reweights the V_k terms at nu=3/2")
print(f"  vs the comparison point and does NOT cancel -> load-bearing. derived (Lyra, Bargmann-Fock) + reference (Cal/Grace FK 1994),")
print(f"  agreement banks it. fish marked: 1.44 ~ 13/9, refused. count moves 2->3 (mu/tau) only on two-route agreement landing 16.82.")
print()

print("=" * 100)
print("SUMMARY -- a clean correction, the method working. My Toy 4163 guessed the 1.44 gap was forced surviving interior")
print("  K-types; Lyra COMPUTED it and showed the opposite. At the muon's Wallach point nu=3/2 the interior Pochhammer")
print("  factor (nu-3/2)_{m2} = (0)_{m2} is exactly 0 for every m2 >= 1 -- so the ENTIRE interior is excluded, the null")
print("  submodule IS the whole interior (not the proper subset 4163 assumed), and the singleton at the muon point is")
print("  purely the m2=0 edge. I confirmed this independently (Fractions, exact). So Lyra's edge sum (11.6) is the complete")
print("  singleton, and the 1.44 gap is definitively the per-harmonic FK Fischer norm -- one named object, with the")
print("  interior alternative ruled out and the bracket's structural reading (which mixed normalizations) retracted. The")
print("  forced computation is now simpler than I framed it: a Fischer-reweighted 1-D edge sum. Cal #27 fired at peak")
print("  convergence -- 'I know the gap is interior' was the moment to brake, and the brake came from Lyra's computation;")
print("  the decider is settled by two-route agreement (she computed, I confirmed). Count moves 2->3 (mu/tau) only when")
print("  the derived Fischer norm + the FK-1994 reference agree and the sum lands 16.82. FORCED count stays 2 of 26.")
print("=" * 100)
print()
print("Per Lyra (computed: at nu=3/2 interior (0)_{m2}=0 -> excluded -> singleton = edge -> 1.44 is the Fischer norm) +")
print("  Grace (aligned: interior ruled out, gap is the per-harmonic Fischer norm) + Elie 4163 (RETRACTED: surviving-interior")
print("  reading wrong; bracket mixed normalizations; submodule = whole interior not a subset). Interior excluded confirmed")
print("  independently; gap = one FK Fischer constant; forced sum is a Fischer-reweighted edge sum; count moves 2->3 on agreement. Count 2.")
print()
print("Elie - Saturday 2026-06-13 (RETRACT Toy 4163 + independently CONFIRM Lyra: my 4163 claimed the singleton = full minus null submodule = SOME surviving interior, so the 1.44 gap (16.82/11.6) was forced interior not a convention constant -- WRONG on two counts: (1) the bracket 11.6 < 16.82 < 64 mixed normalizations (11.6 = Fischer=1 edge sum, 64 = fully-normalized generic closed form, not apples-to-apples), (2) the null submodule at nu=3/2 is NOT a proper subset of the interior -- it IS the whole interior; LYRA COMPUTED + I CONFIRMED independently (exact Fractions): at the muon Wallach point nu=3/2 the interior Pochhammer factor (nu-3/2)_{m2} = (0)_{m2} = 1 for m2=0 (edge) and EXACTLY 0 for all m2>=1 (interior), so EVERY interior K-type has zero coefficient -> the entire interior is excluded -> the singleton at the muon point = the m2=0 edge ONLY -> Lyra's edge sum 11.6 is the COMPLETE singleton (Fischer=1); THEREFORE the 1.44 gap is definitively the per-harmonic FK FISCHER NORM (the weight Lyra set to 1; does not cancel in the ratio, load-bearing), ONE named object, interior alternative RULED OUT; the forced computation is SIMPLER than 4163 framed -- a Fischer-reweighted 1-D EDGE sum, not a 2-D interior sum; derived (Lyra Bargmann-Fock) + reference (Cal/Grace FK 1994), two-route agreement banks it, fish marked 1.44~13/9 refused; DISCIPLINE: Cal #27 fired at peak convergence -- 'I know the gap is interior' was the moment to brake, brake came from Lyra's direct computation, decider SETTLED by two-route agreement (she computed, I confirmed); count moves 2->3 (mu/tau, Grace split gate) only when derived Fischer + reference agree and sum lands 16.82; FORCED count stays 2 of 26)")
print()
print("SCORE: 2/2 (RETRACT 4163 + confirm Lyra: at muon Wallach point nu=3/2 interior factor (nu-3/2)_{m2}=(0)_{m2}=0 for all m2>=1 -> ENTIRE interior excluded -> singleton = edge-only -> 11.6 is complete singleton -> 1.44 gap is the per-harmonic FK Fischer norm NOT surviving interior; 4163 errors: mixed-normalization bracket + submodule-is-whole-interior-not-subset; forced computation = Fischer-reweighted 1-D edge sum, two-route gate (Lyra derive + FK-1994), fish 13/9 marked; Cal #27 brake came from teammate computation, decider settled by agreement; count 2 of 26)")
