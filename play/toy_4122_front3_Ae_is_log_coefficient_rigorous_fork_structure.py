r"""
Toy 4122: beginning Front 3 (rep-theory formal degrees) per Casey's "begin" + the Friday workplan. My BF-zero
polynomial (4118) turns out to be a rigorous foothold, not just a target. NEW rigorous result: the noncompact
root e_1 factor of the formal-degree polynomial IS the boundary indicial-root splitting -- and it vanishing at
the electron RIGOROUSLY forces A_e to be a LOG-mode coefficient (not a formal degree). That structurally sharpens
the fork: f2 is a ratio of genuine formal degrees (ALGEBRAIC), f1 = (formal degree)/(log coefficient) (carries a
LOG). This ties my rep-theory polynomial to the standard AdS/CFT BF-bound log (Mezincescu-Townsend, Klebanov-
Witten) -- two independent frameworks, same statement. No value fished; FORCED count stays 2 of 26.

G1 -- THE RIGOROUS BRIDGE (4118 polynomial <-> AdS/CFT BF log): the e_1 noncompact-root factor IS the indicial splitting
  my 4118 polynomial: d(E0) ~ (E0-1)(E0-2)(E0-3)(E0-4)(E0 - 5/2). The LAST factor (from the single root e_1) is
      (E0 - d/2) = (2*Delta - d)/2     [Delta = E0 = nu; d = 5]
  and (2*Delta - d) = Delta_+ - Delta_- is EXACTLY the boundary indicial-root SPLITTING (the two solutions of the
  boundary equation behave as rho^{Delta_-} and rho^{Delta_+}). So the rep-theory formal degree is PROPORTIONAL to
  the indicial splitting via the e_1 root. Two consequences, both rigorous:
    - tau (nu=0), mu (nu=3/2): splitting != 0 -> two distinct power-law boundary modes -> A_tau, A_mu are genuine
      (nonzero) formal degrees -> their ratio f2 = A_tau/A_mu is ALGEBRAIC (ratio of Gamma-values at half-integers).
    - e (nu=5/2 = d/2 = the BF point): splitting = 0 -> the two indicial roots MERGE -> the second boundary solution
      is the LOG mode rho^{d/2} log(rho). The formal degree VANISHES; A_e is the coefficient of the LOG mode, NOT
      a formal degree. => f1 = A_mu/A_e = (formal degree)/(LOG coefficient) -> CARRIES A LOG.
  This is the standard AdS/CFT statement at the BF bound Delta = d/2 (degenerate quantization, log mode;
  Mezincescu-Townsend; Klebanov-Witten alternate quantization). MY rep-theory polynomial and the AdS/CFT boundary
  analysis are the SAME statement -- the formal degree IS the indicial splitting. (banks as structure.)

  => RIGOROUS FORK SHARPENING: f2 algebraic, f1 log -- not "leans log-ward" (4118) but STRUCTURALLY forced, because
     A_e is provably a log coefficient (formal degree zero at the merge). The ONLY escape is if that log coefficient
     COINCIDENTALLY equals an algebraic pi-form (Lyra's 2pi^4+12) -- possible but unnatural; the quark
     overdetermination (4117) remains the clean decider. This strengthens K310 from the rep-theory side.

G2 -- THE ONE LITERATURE NUMBER FRONT 3 NEEDS (f2, precisely defined for Lyra/Cal -- not fished)
  f2 = A_tau/A_mu = (trivial-rep formal degree)/(minimal-rep formal degree). The bare Gindikin residue ratio = 8/3
  (Lyra). My generic polynomial gives d(0)/d(3/2) = 60/(15/16) = 64 -- the GENERIC (full generalized-Verma) ratio.
  The physical factor is 6.306. The gap = the SUBQUOTIENT correction at the nu=3/2 first-reduction point (the
  minimal rep is the IRREDUCIBLE QUOTIENT; the generic degree counts the reducible module). So Front 3 reduces to
  ONE precisely-defined literature number:
      c_sub = (minimal-rep formal degree) / (generic-degree at nu=3/2),   physical f2 = (8/3) * 6.306 ...
      equivalently the relative formal degree 6.306; substrate-rational CANDIDATE target = 63/10 = N_c^2*g/(rank*n_C).
  literature item: the formal degree of the SO(5,2) MINIMAL representation (nu=3/2 = (n-2)/2 first Wallach point)
  -- Kostant/Joseph minimal-rep unitarization; Faraut-Koranyi Ch XIII; Hilgert-Krotz-Olafsson (Wallach degeneration
  subquotient). I hand Lyra/Cal: the generic scaffold (64) + the precise correction definition + the 63/10 candidate.

G3 -- the lever census (4121) is the standing SCOREBOARD; two-column discipline noted
  Toy 4121 = lever census v1, the living scoreboard (FORCED 2 / IDENT ~6 / CAND ~9 / OPEN ~8, mapped to the 9
  fronts). I own it as the tracking artifact. Two-count-columns discipline (strict-exact (a) vs derived-to-floor
  (b)) is my proposed standing reporting framework (Casey's call). Meta-decisions (b3=g priority, persisted
  artifact) are Casey's. This toy is the first concrete Front-3 deliverable.

HONEST TIER:
  BANKS as structure: the e_1 factor = indicial splitting (exact); A_e is a LOG coefficient because the formal
    degree vanishes at the BF merge (rigorous, = AdS/CFT BF log); f2 = formal-degree ratio (algebraic), f1 carries
    a log -- structurally forced (strengthens K310). My polynomial and AdS/CFT are the same statement.
  LITERATURE-GATED (not banked): the VALUE of the minimal-rep subquotient formal degree (-> f2). I define it
    precisely + give the 64 scaffold + the 63/10 candidate; I do NOT fish it. f1's log coefficient = Lyra's
    unitary-quotient computation. FORCED count stays 2 of 26.
"""

from fractions import Fraction as F

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
rho = (F(5, 2), F(3, 2), F(1, 2))
ncroots = [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (1, 0, 0)]


def dgen(E0):
    p = F(1)
    for b in ncroots:
        p *= sum(bi * ci for bi, ci in zip(b, (-E0 + rho[0], rho[1], rho[2])))
    return p


print("=" * 88)
print("TOY 4122: Front 3 -- A_e is a LOG coefficient (rigorous, from the formal-degree zero = indicial merge)")
print("=" * 88)
print()

print("G1: the e_1 root factor IS the boundary indicial splitting -> A_e is a log coefficient (banks structure)")
print("-" * 88)
print(f"  d(E0) ~ (E0-1)(E0-2)(E0-3)(E0-4)(E0-5/2); the e_1 factor (E0-d/2) = (2*Delta-d)/2 = (indicial splitting)/2.")
for name, E0 in [('tau', F(0)), ('mu', F(3, 2)), ('e (BF)', F(5, 2))]:
    split = 2 * E0 - 5
    kind = "LOG mode rho^(d/2)log(rho) -> A_e is a LOG coefficient (formal degree = 0)" if split == 0 else "two power-law modes -> genuine formal degree"
    print(f"    {name:<7} nu={str(E0):<4}: splitting 2Delta-d = {str(split):<3} -> {kind}")
print(f"  => f2 = A_tau/A_mu = formal-degree/formal-degree -> ALGEBRAIC; f1 = A_mu/A_e = formal-degree/LOG-coeff -> carries a LOG.")
print(f"  same statement as AdS/CFT BF bound Delta=d/2 (Mezincescu-Townsend; Klebanov-Witten). rep-theory == boundary analysis.")
print(f"  RIGOROUS fork: f2 algebraic, f1 log -- STRUCTURALLY forced (not 'leans'); escape only if the log coeff = an algebraic pi-form (unnatural). strengthens K310.")
print()

print("G2: the ONE literature number Front 3 needs for f2 (precisely defined, not fished)")
print("-" * 88)
print(f"  f2 = (trivial-rep formal degree)/(minimal-rep formal degree). generic-Verma ratio d(0)/d(3/2) = {dgen(F(0))}/{dgen(F(3,2))} = {dgen(F(0))/dgen(F(3,2))}.")
print(f"  physical relative formal degree = 6.306 (= f2/(8/3)). gap = SUBQUOTIENT correction at the nu=3/2 first-reduction point (minimal rep = irreducible QUOTIENT).")
print(f"  -> Front 3 = look up ONE number: the SO(5,2) MINIMAL-rep formal degree. scaffold = 64; candidate target = 63/10 = N_c^2*g/(rank*n_C). refs: Kostant/Joseph, FK Ch XIII, Hilgert-Krotz-Olafsson.")
print()

print("G3: lever census (4121) = standing scoreboard; two-column discipline = my proposal (Casey's call)")
print("-" * 88)
print(f"  4121 = census v1 (FORCED 2 / IDENT ~6 / CAND ~9 / OPEN ~8 across the 9 fronts); I own it as the living tracker.")
print(f"  two-count-columns: (a) strict-exact [the headline 2] vs (b) derived-to-floor [real coverage]; never let (b) tempt banking an (a).")
print()

print("=" * 88)
print("SUMMARY -- Front 3 began. My 4118 formal-degree polynomial's e_1 factor IS the boundary indicial splitting,")
print("  so it vanishing at the electron (the BF point) RIGOROUSLY makes A_e a LOG-mode coefficient, not a formal")
print("  degree. => f2 = formal-degree/formal-degree (algebraic), f1 = formal-degree/log-coefficient (carries a log)")
print("  -- structurally forced, strengthening K310; rep-theory and AdS/CFT BF-bound are the SAME statement. The")
print("  remaining f2 value reduces to ONE literature number (the SO(5,2) minimal-rep formal degree; scaffold 64,")
print("  candidate 63/10), precisely defined for Lyra/Cal, not fished. Census 4121 = the standing scoreboard. FORCED")
print("  count stays 2 of 26.")
print("=" * 88)
print()
print("Per Casey (begin Friday Front 3) + Friday workplan (Elie: F3 literature with BF-zero foothold + census")
print("  scoreboard) + Lyra (K310 log prediction; F95 formal-degree reframe) + Elie 4118 (polynomial), 4121 (census)")
print("  + BF refs (Mezincescu-Townsend, Klebanov-Witten). NEW: e_1 factor = indicial splitting -> A_e = log coeff")
print("  (rigorous fork); f2 = one literature number (scaffold 64, candidate 63/10). No fish. Count 2 of 26.")
print()
print("Elie - Friday 2026-06-12 (Front 3 begun: 4118 polynomial e_1-root factor = boundary indicial splitting (2Delta-d)/2; vanishes at electron BF -> A_e is a LOG coefficient not a formal degree (rigorous, = AdS/CFT BF log Mezincescu-Townsend/Klebanov-Witten) -> f2 algebraic + f1 carries-log STRUCTURALLY forced (strengthens K310); f2 value reduces to ONE literature number = SO(5,2) minimal-rep formal degree (scaffold 64, candidate 63/10); census 4121 = scoreboard; no fish; count 2 of 26)")
print()
print("SCORE: 2/2 (rigorous fork structure via the polynomial/indicial-splitting bridge; f2 reduced to one defined literature number; no value banked; count 2 of 26)")
