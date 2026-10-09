import sympy as sp
f,Or,D,H=sp.symbols('f Omega_r D H',positive=True); w=sp.Symbol('w')
Om=1-f-Or
dlnH2=-3*Om-4*Or-3*(1+w)*f            # Friedmann
dlnNH=-dlnH2                           # N_H ∝ H^-2
sN=sp.symbols('s_N')
w_of_sN=sp.solve(sp.Eq(-3*(1+w), sN+2*dlnH2), w)[0]        # continuity, rho_DE ∝ H^4 N
print("w(s_N) =", sp.simplify(w_of_sN))
print("Law N∝N_H^2  ⇒ w =", sp.solve(sp.Eq(w, w_of_sN.subs(sN, 2*dlnNH)), w))
expr=sp.expand((2*dlnNH).subs(w,-1)); print("2 dlnN_H at w=-1 =", expr, " → beta =", sp.simplify((expr-6*(1-f))/Or))
for name,rad in (("rho+p (null focusing)",sp.Rational(4,3)),("rho+3p (timelike focusing)",2)):
    s=sp.expand(6*(Om+rad*Or)); beta=sp.simplify((s-6*(1-f))/Or)
    print(f"source ∝ {name}: s_N = {s}; beta = {beta}; w = {sp.solve(sp.Eq(w, w_of_sN.subs(sN,s)),w)}")
print("rho_DE ∝ H^(", sp.simplify(1-2*(D-1)+D), ") → constant iff D = 3")
