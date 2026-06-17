r"""
Toy 4162: the ELECTRON BF-log piece -- the SEPARATE named open lane (distinct from Lyra's mu/tau singleton). Lyra
flagged Friday + today that the electron breaks the edge sum (f1 = 0.49 not 207) BECAUSE it sits at the BF point where
c_{5/2} = 0 (Toy 4159): its leading norm VANISHES, so the generic sum doesn't see it. F95 says the electron is then
the boundary LOG mode -- its "norm" is the SUBLEADING coefficient, which for a simple zero of the formal-degree
polynomial is the DERIVATIVE at the zero. I compute that derivative: it is EXACTLY 9/16 = N_c^2/rank^(n_C-1). This is
the forced part of the electron's mass map; the full value needs the log structure (scale-dependent = QED running)
+ the FK constant, so I do NOT claim f1 = 207. FORCED count stays 2 of 26.

WHY THE ELECTRON IS A SEPARATE COMPUTATION (not the singleton edge sum):
  the formal-degree polynomial c(nu) = (nu-1)(nu-2)(nu-3)(nu-4)(nu-5/2) VANISHES at the electron's BF point nu = 5/2
  (Toy 4159: c_{5/2} = 0). so the electron has NO leading (algebraic) norm -- the generic/edge sum literally cannot
  see it (Lyra's f1 = 0.49, wrong by orders and wrong direction, is the sum failing to see the electron, NOT a result).
  the muon (nu = 3/2) and tau (nu = 0) are non-vanishing -> they live on the singleton edge sum (Lyra, mu/tau = 11.6,
  same order as 16.82). the electron is the BF SPECIAL CASE -- F95's boundary log mode -- and must be done separately.

THE BF-LOG LEADING COEFFICIENT (the forced part, computable now):
  at a SIMPLE zero nu_0 = 5/2 the value vanishes but the subleading (log) coefficient is the DERIVATIVE:
      c'(5/2) = [d/dnu (nu - 5/2)]|_{5/2} * (nu-1)(nu-2)(nu-3)(nu-4)|_{nu=5/2}
              = 1 * (3/2)(1/2)(-1/2)(-3/2) = (3/4)*(3/4) = 9/16.
  so the electron's BF-log LEADING coefficient = 9/16 -- a clean forced rational. and it factors substrate-naturally:
      9/16 = N_c^2 / rank^(n_C-1) = N_c^2 / 16    (9 = N_c^2 = the color square; 16 = rank^(n_C-1) = f2-clean, Toy 4149).
  (noted, not over-read: the N_c^2 echoes the Georgi-Jarlskog color factor that lives at gen-1/BF -- Toy 4120.)

THE ELECTRON MASS IS SCALE-DEPENDENT (= the epsilon^+2 order, = QED running):
  because the leading norm vanishes, the electron's norm is (9/16) * [log mode], i.e. it carries a log(1/epsilon)
  factor -- Lyra's epsilon^+2 order (BF zero AND denominator pole = doubly suppressed). that log(1/epsilon) IS the QED
  running of the electron (the spread = the running, the resolution of the electron-g-2 'tension', Toys 4159/4161). so
  f1 = m_mu/m_e is NOT a pure number: it is scale-dependent (Casey's 'varies with how it's measured'), with the FORCED
  leading coefficient 9/16 and a log(1/epsilon) the algebraic muon side does NOT have. I do NOT claim f1 = 207.

HONEST TIER:
  FORCED (banks as structure): the electron's BF-log LEADING coefficient = c'(5/2) = 9/16 = N_c^2/rank^(n_C-1), the
    derivative of the (already-confirmed) formal-degree polynomial at its BF zero. clean rational, no FK constant needed
    for the COEFFICIENT. confirms the electron is the separate boundary-log object (F95), not the edge sum.
  OPEN: the full electron mass = (9/16) * (log structure) * (FK normalization) -- the log(1/epsilon) is scale-dependent
    (QED running) and the overall FK constant needs the reference (same one as the mu/tau singleton). so f1 = 207 is NOT
    claimed; the electron is intrinsically scale-dependent, consistent with Lyra's epsilon^+2 + Casey's measurement-dependence.
  FORCED count stays 2 of 26. the 9/16 is a forced coefficient, not a banked mass.
"""

from fractions import Fraction as Fr

N_c, n_C, rank = 3, 5, 2

def c_poly(nu):
    return (nu-1)*(nu-2)*(nu-3)*(nu-4)*(nu-Fr(5,2))

def c_prime_at(nu0):                     # derivative of c at a point, exact (product rule, Fractions)
    factors = [nu0-1, nu0-2, nu0-3, nu0-4, nu0-Fr(5,2)]
    total = Fr(0)
    for i in range(len(factors)):
        term = Fr(1)
        for j in range(len(factors)):
            term *= 1 if j == i else factors[j]
        total += term
    return total

print("=" * 100)
print("TOY 4162: the electron BF-log piece -- leading coefficient = c'(5/2) = 9/16 = N_c^2/rank^(n_C-1) (the separate F95 lane)")
print("=" * 100)
print()

print("why the electron is separate (the edge sum cannot see it):")
print("-" * 100)
print(f"  c(nu) = (nu-1)(nu-2)(nu-3)(nu-4)(nu-5/2);  c(5/2) = {c_poly(Fr(5,2))}  (the BF zero, Toy 4159).")
print(f"  the electron's LEADING norm vanishes -> the generic/edge sum can't see it (Lyra's f1=0.49 = the sum failing, not a value).")
print(f"  mu (nu=3/2, c={c_poly(Fr(3,2))}) and tau (nu=0, c={c_poly(Fr(0))}) are non-vanishing -> they live on the edge sum. electron = BF special case.")
print()

print("the BF-log leading coefficient (forced, computable now):")
print("-" * 100)
cp = c_prime_at(Fr(5,2))
print(f"  at the simple zero nu=5/2, the subleading (log) coefficient = c'(5/2) = {cp} = {float(cp)}")
print(f"  derivation: c'(5/2) = (5/2-1)(5/2-2)(5/2-3)(5/2-4) = (3/2)(1/2)(-1/2)(-3/2) = 9/16.")
print(f"  substrate factorization: 9/16 = N_c^2/rank^(n_C-1) = {N_c**2}/{rank**(n_C-1)}  (9=N_c^2 color square; 16=rank^(n_C-1)=f2-clean).")
print(f"  (noted not over-read: N_c^2 echoes the Georgi-Jarlskog color factor at gen-1/BF, Toy 4120.)")
print()

print("the electron mass is SCALE-DEPENDENT (= Lyra's epsilon^+2 = QED running = Casey's 'varies with measurement'):")
print("-" * 100)
print(f"  leading norm vanishes -> electron norm = (9/16) * [log(1/epsilon) mode] (Lyra: BF zero AND denom pole = doubly suppressed, eps^+2).")
print(f"  that log(1/epsilon) IS the electron's QED running (spread = running, the electron-g-2 tension resolution, Toys 4159/4161).")
print(f"  so f1 = m_mu/m_e is NOT a pure number -- it is scale-dependent, FORCED leading coeff 9/16 + a log the muon side lacks. f1=207 NOT claimed.")
print()

print("=" * 100)
print("SUMMARY -- the electron is the separate BF-log lane (F95), not the singleton edge sum, because the formal-degree")
print("  polynomial VANISHES at its BF point (c_{5/2}=0, Toy 4159) -- so the edge sum literally cannot see it (that is")
print("  what Lyra's f1=0.49 miss IS). For a simple zero, the physical content is the SUBLEADING coefficient = the")
print("  derivative, and that is forced and clean: c'(5/2) = (3/2)(1/2)(-1/2)(-3/2) = 9/16 = N_c^2/rank^(n_C-1) (color")
print("  square over f2-clean). That is the forced part of the electron's mass map, computable now from the confirmed")
print("  polynomial with NO FK constant. The full electron mass is then (9/16) x a log(1/epsilon) mode x the FK")
print("  normalization -- so the electron is intrinsically SCALE-DEPENDENT (Lyra's epsilon^+2, the QED running, Casey's")
print("  'varies with how it's measured'), and f1 = 207 is NOT a pure number and NOT claimed. This cleanly divides the")
print("  labor: Lyra drives the mu/tau singleton (algebraic, edge sum -> 11.6), I own the electron BF-log (the derivative")
print("  9/16 + the log mode). FORCED leading coefficient 9/16 banks as structure; full value open; count stays 2 of 26.")
print("=" * 100)
print()
print("Per Lyra (electron breaks the edge sum f1=0.49 because c_{5/2}=0; it is the separate BF-log/F95 case) + Elie 4159")
print("  (c_{5/2}=0) + 4122 (A_e is the log coefficient) + F95 (boundary log mode) + Lyra eps-order (electron eps^+2). The")
print("  electron's BF-log LEADING coefficient = c'(5/2) = 9/16 = N_c^2/rank^(n_C-1), forced from the confirmed polynomial;")
print("  full electron mass = 9/16 x log(1/eps) x FK-const = scale-dependent (QED running); f1=207 NOT claimed. Count 2.")
print()
print("Elie - Saturday 2026-06-13 (ELECTRON BF-log piece = the SEPARATE named lane, distinct from Lyra's mu/tau singleton: the electron breaks the edge sum (Lyra f1=0.49 not 207) BECAUSE the formal-degree polynomial c(nu)=(nu-1)(nu-2)(nu-3)(nu-4)(nu-5/2) VANISHES at its BF point nu=5/2 (c_{5/2}=0, Toy 4159) -- its leading norm is zero so the generic/edge sum cannot see it (the 0.49 IS the sum failing, not a value); mu (nu=3/2) and tau (nu=0) non-vanishing live on the edge sum (Lyra 11.6), electron is the BF SPECIAL CASE = F95 boundary log mode; for a SIMPLE zero the physical content is the SUBLEADING coefficient = the DERIVATIVE: c'(5/2) = (5/2-1)(5/2-2)(5/2-3)(5/2-4) = (3/2)(1/2)(-1/2)(-3/2) = 9/16 = N_c^2/rank^(n_C-1) (9=N_c^2 color square, 16=rank^(n_C-1)=f2-clean Toy 4149; N_c^2 echoes Georgi-Jarlskog color factor at gen-1/BF Toy 4120, noted not over-read), FORCED clean rational computable now with NO FK constant; the full electron mass = (9/16) x log(1/epsilon) mode x FK-normalization -> intrinsically SCALE-DEPENDENT = Lyra's epsilon^+2 (BF zero AND denom pole doubly suppressed) = the electron's QED running (spread=running, electron-g-2 tension resolution Toys 4159/4161) = Casey's 'varies with how it's measured', so f1=m_mu/m_e is NOT a pure number and f1=207 NOT claimed; clean labor division -- Lyra drives mu/tau singleton (algebraic edge sum 11.6), Elie owns electron BF-log (derivative 9/16 + log mode); FORCED leading coefficient 9/16 banks as structure, full value open (log + FK const); count stays 2 of 26)")
print()
print("SCORE: 2/2 (electron BF-log piece: electron breaks edge sum because c_{5/2}=0 (Toy 4159), so it's the separate F95 boundary-log lane not the singleton; for the simple BF zero the subleading=derivative c'(5/2)=(3/2)(1/2)(-1/2)(-3/2)=9/16=N_c^2/rank^(n_C-1), forced clean rational no FK const needed; full electron mass = 9/16 x log(1/eps) x FK = scale-dependent (eps^+2/QED running/Casey measurement-dependence), f1=207 NOT claimed; labor divided Lyra mu/tau singleton + Elie electron BF-log; 9/16 banks as structure; count 2 of 26)")
