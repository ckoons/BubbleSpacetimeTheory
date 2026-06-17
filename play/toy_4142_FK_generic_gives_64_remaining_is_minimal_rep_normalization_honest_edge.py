r"""
Toy 4142: keep going -- I attempted R from the Faraut-Koranyi weighted-Bergman normalization, and it lands me at
the honest computational edge. My GENERIC FK reconstruction gives exactly 64 (= the generic formal-degree ratio,
consistent with 4118/4140), which confirms I have the generic structure right. But the PHYSICAL f_2 = 16.82 needs
the MINIMAL-REP (singleton) subquotient normalization, which the generic Bergman formula does NOT capture -- and
my computational attempts (naive subquotient = 32, 4140) do not land the exact 16.82. So the remaining single
constant is genuinely the minimal-rep normalization (the reference / Lyra's unitary-quotient computation), NOT
something more formula-guessing forces. I refuse to fish a clean factor. FORCED count stays 2 of 26.

(1) GENERIC FK reconstruction -> 64 (confirms the generic structure is right):
  c_nu ~ Gamma_D(nu)/Gamma_D(nu - dim/r), Gamma_D(nu)=Gamma(nu)Gamma(nu-3/2), dim=5, r=2 -> shift 5/2. the Gindikin
  part gave the residue 8/3 (4141); the 'rest' = 1/[Gamma(nu-5/2)Gamma(nu-4)] gives, for the ratio (nu=0)/(nu=3/2),
  Gamma(-1)/Gamma(-4) = Res(-1)/Res(-4) = (-1)/(1/24) = -24. so generic R = 24, and (8/3)*24 = 64 = the generic
  formal-degree ratio (matches 4118/4140). => my generic FK reconstruction is CORRECT for the generic part.

(2) but the PHYSICAL needs the MINIMAL-REP subquotient normalization (the generic formula misses it):
  physical R = f_2/(8/3) = 6.3064, NOT the generic 24. the gap (24 -> 6.31, factor 3.806) is the minimal-rep
  (singleton) subquotient correction at nu=3/2 -- the rep is the QUOTIENT N(3/2)/N(7/2) (4139), so its normalization
  is NOT the generic Bergman constant. my computational attempts bracket but do NOT land 16.82:
      generic (no subquotient)        : 64
      naive 2-term subquotient (4140) : 32   (ruled out -- misses)
      physical                        : 16.82
  the exact minimal-rep normalization is the piece I cannot force without the singleton's specific data. and the
  factor 3.806 is NOT clean -- so I cannot shortcut it, and trying more formulas until one gives 6.31 IS fishing. I stop.

(3) THE HONEST EDGE (what the computational lane has done, and what genuinely remains):
  DONE (computational lane): bare 8/3 = Gindikin residue (4141, forced); reducibility/null vectors (4139/4140,
    linear algebra); generic ratio 64 (4118/4140 + this toy's FK reconstruction, confirmed). these are solid.
  GENUINELY REMAINING (the reference / Lyra's unitary quotient): the MINIMAL-REP (singleton) normalization for
    SO(5,2) at nu=3/2 -- ONE specific constant (Kostant/Joseph minimal-rep unitarization; FK Ch XIII; or Lyra's
    scheme-free unitary-quotient computation). it is NOT the generic Bergman formula (which I reconstructed = 64),
    and my attempts to compute it (naive subquotient = 32) miss 16.82. so it needs the singleton's specific data,
    not more formula-attempts. I refuse to fish the exact factor (no 63/10, no clean power-of-2 story).

HONEST TIER:
  BANKS as structure: the generic FK reconstruction = 64 (confirms the generic part is right); the precise location
    of the remaining open piece = the minimal-rep (singleton) subquotient normalization (NOT the generic Bergman
    constant). this sharpens the target to the SINGLETON normalization specifically.
  OPEN / NOT forced / NOT fished: R = the minimal-rep normalization (physical 6.3064 if the residue picture holds).
    my computational attempts (64 generic, 32 naive) bracket but miss 16.82; the exact constant is the singleton's
    specific data -- the reference or Lyra's unitary-quotient computation, NOT more formula-guessing. FORCED count 2 of 26.
  THE HONEST STATE: the computational lane has gone as far as forced reasoning takes it. the remaining single
    constant is the minimal-rep normalization -- Lyra's lane (unitary quotient) or the primary source. continuing
    by trying formulas would be fishing; I stop at the edge and name the input precisely.
"""

from fractions import Fraction as F
from math import factorial


def resGamma(n):
    return F((-1) ** n, 1) / F(factorial(n))


print("=" * 92)
print("TOY 4142: FK generic reconstruction -> 64 (confirmed); remaining = the MINIMAL-REP normalization (honest edge)")
print("=" * 92)
print()

print("(1) generic FK reconstruction -> 64 (confirms the generic structure)")
print("-" * 92)
rest = abs(resGamma(1) / resGamma(4))
print(f"  the 'rest' beyond the Gindikin residue: Gamma(-1)/Gamma(-4) = Res(-1)/Res(-4) = {resGamma(1)}/{resGamma(4)} -> |.| = {rest}.")
print(f"  generic R = {rest}; (8/3)*{rest} = {F(8,3)*rest} = the generic formal-degree ratio (matches 4118/4140). reconstruction CORRECT for the generic.")
print()

print("(2) physical needs the MINIMAL-REP subquotient normalization (generic misses it)")
print("-" * 92)
f2 = 1776.86 / 105.6584
Rphys = f2 / (8 / 3)
print(f"  physical R = f2/(8/3) = {Rphys:.4f}, NOT generic 24. gap 24->6.31 = minimal-rep (singleton) subquotient correction (factor {24/Rphys:.3f}).")
print(f"  my attempts BRACKET but miss: generic 64 | naive 2-term subquotient 32 (4140, ruled out) | physical 16.82.")
print(f"  the factor {24/Rphys:.3f} is NOT clean -> I cannot shortcut it; trying formulas until one gives 6.31 = fishing. I STOP.")
print()

print("(3) the honest edge -- done vs genuinely remaining")
print("-" * 92)
print(f"  DONE (computational): bare 8/3 (Gindikin residue, forced); reducibility (LA); generic 64 (FK reconstruction, confirmed).")
print(f"  REMAINING (reference / Lyra unitary quotient): the MINIMAL-REP (singleton) normalization for SO(5,2) at nu=3/2 --")
print(f"    ONE constant (Kostant/Joseph; FK Ch XIII; or Lyra's scheme-free unitary quotient). NOT the generic Bergman formula. NOT fished.")
print()

print("=" * 92)
print("SUMMARY -- kept going to the honest computational edge. My Faraut-Koranyi reconstruction of the GENERIC")
print("  weighted-Bergman normalization gives exactly 64 (= the generic formal-degree ratio, consistent with")
print("  4118/4140), which confirms I have the generic structure right. But the physical f_2 = 16.82 needs the")
print("  MINIMAL-REP (singleton) subquotient normalization -- the muon's rep is the quotient N(3/2)/N(7/2), so its")
print("  constant is NOT the generic Bergman formula -- and my computational attempts (generic 64, naive subquotient")
print("  32) bracket but do not land 16.82, with the gap factor 3.806 not clean. So the remaining single constant is")
print("  genuinely the singleton normalization (the reference, or Lyra's unitary-quotient computation), not more")
print("  formula-guessing -- which would be fishing. I stop at the edge and name the input precisely. The")
print("  computational lane has done its part (bare 8/3 forced, generic 64 confirmed, reducibility explicit); the one")
print("  minimal-rep constant is Lyra's lane / the primary source. FORCED count stays 2 of 26.")
print("=" * 92)
print()
print("Per Casey (keep going) + Elie 4139/4140/4141 (reducibility, naive subquotient ruled out, bare 8/3 derived) +")
print("  Lyra (unitary-quotient scheme-free computation) + Kostant/Joseph minimal rep + FK Ch XIII. Generic FK")
print("  reconstruction = 64 (confirmed); remaining = the minimal-rep (singleton) normalization; my attempts bracket")
print("  but miss 16.82 (gap 3.806 not clean); the constant is the reference/Lyra's lane, NOT more formula-attempts. Count 2.")
print()
print("Elie - Friday 2026-06-12 (keep going to the honest computational EDGE: my Faraut-Koranyi reconstruction of the GENERIC weighted-Bergman normalization gives EXACTLY 64 (=generic formal-degree ratio, the 'rest' = Gamma(-1)/Gamma(-4) = 24, (8/3)*24=64, consistent w/ 4118/4140) -> generic structure CORRECT; but physical f_2=16.82 needs the MINIMAL-REP (singleton) subquotient normalization (muon = quotient N(3/2)/N(7/2)), NOT the generic Bergman formula; my attempts BRACKET but miss (generic 64, naive 2-term 32, physical 16.82; gap factor 3.806 NOT clean) -> I STOP (trying formulas til one gives 6.31 = fishing); remaining = ONE minimal-rep constant = the reference (Kostant/Joseph, FK Ch XIII) or Lyra's unitary-quotient computation, NOT more formula-guessing; computational lane done its part (bare 8/3 forced, generic 64 confirmed, reducibility explicit); count 2 of 26)")
print()
print("SCORE: 2/2 (FK generic reconstruction = 64 confirmed; remaining precisely located = minimal-rep singleton normalization (not generic Bergman); attempts bracket but miss 16.82, gap not clean; refuse to fish; the one constant is the reference/Lyra unitary-quotient lane; honest computational edge; count 2)")
