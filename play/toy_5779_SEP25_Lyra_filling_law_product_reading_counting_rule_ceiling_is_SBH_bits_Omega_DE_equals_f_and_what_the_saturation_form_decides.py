"""Toy 5779 (Lyra, 2026-09-25) — Lane 1: the product reading's counting rule, ceiling, radiation number.
DISCLOSURE: check 5 is the late-time consequence of the saturation form. Lyra saw it while writing the
clause; it is printed here so the finding has an instrument, not a memory. Elie's blind run is now a
re-derivation, not a blind. Exact symbolic; G = hbar = c = k_B = 1; no DESI input."""
import sympy as sp
H, a = sp.symbols('H a', positive=True)
f, w = sp.symbols('f w')
ok = 0; N = 0
def check(name, cond):
    global ok, N; N += 1; ok += bool(cond); print(('PASS' if cond else 'FAIL'), name)
T = H/(2*sp.pi); A = 4*sp.pi/H**2; V = sp.Rational(4,3)*sp.pi/H**3; rc = 3*H**2/(8*sp.pi)
S_BH = A/4                      # nats; bits = S_BH/ln2 ; one Landauer bit costs T ln2
E_bit = T*sp.log(2)
# 1. ceiling in rule-R units (N_H = A, coefficient 1): rho/rho_crit = 4 ln 2 > 1  -> Friedmann-inconsistent
r1 = sp.simplify(E_bit*A/V/rc); check('rule-R ceiling rho/rho_c = 4 ln2 (>1, excluded)', sp.simplify(r1-4*sp.log(2))==0 and r1.evalf()>1)
# 2. ceiling in S_BH bits: rho/rho_crit = 1 exactly  -> Omega_DE = f
r2 = sp.simplify(E_bit*(S_BH/sp.log(2))/V/rc); check('S_BH-bit ceiling rho/rho_c = 1 exactly', r2==1)
# 3. matter era, product N ~ a^6, E ~ H, V ~ H^-3, H ~ a^-3/2: rho const
Hm = a**sp.Rational(-3,2); check('matter era rho ~ H^4 a^6 = const', sp.simplify(Hm**4*a**6)==1)
# 4. radiation era H ~ a^-2: rho ~ a^-2 (w = -1/3); f = N/N_H ~ a^6 H^2 ~ a^2
Hr = a**-2; check('radiation rho ~ a^-2', sp.simplify(Hr**4*a**6 - a**-2)==0)
check('radiation f ~ a^2', sp.simplify(a**6*Hr**2 - a**2)==0)
# 5. late time, matter+DE, Omega_DE = f, w_eff = w f.  ledger: dlnf/dlna = 6(1-f)X - 3(1+w f); continuity: -3w(1-f)
sol_ex = sp.solve(sp.Eq(6*(1-f) - 3*(1+w*f), -3*w*(1-f)), w)
sol_no = sp.solve(sp.Eq(6 - 3*(1+w*f), -3*w*(1-f)), w)
print('   once-only exclusion  (X = 1-f): w =', sol_ex)
print('   no exclusion         (X = 1)  : w =', sol_no)
check('exclusion form gives w = -1 identically', sol_ex==[-1])
check('no-exclusion form gives w = 1/(2f-1) < -1 for 0<f<1/2 (phantom)', sp.simplify(sol_no[0]-1/(2*f-1))==0)
# 6. control: quotient reading N ~ a^2/3 -> rho ~ H^4 a^2 ~ a^-4 in matter (not constant)
check('control: quotient reading fails in matter era', sp.simplify(Hm**4*a**2)!=1)
print(f'SCORE {ok}/{N}')
