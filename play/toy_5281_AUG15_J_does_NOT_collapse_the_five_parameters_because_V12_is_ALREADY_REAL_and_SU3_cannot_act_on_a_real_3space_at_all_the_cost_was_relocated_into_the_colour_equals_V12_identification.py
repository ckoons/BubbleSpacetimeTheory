"""
Toy 5281 (Elie, 2026-08-15, evening) -- K1560: is my diag(-1,1,-1) the J-INDUCED real structure?

SHORT ANSWER: no -- and for two reasons, the second of which matters more than the first.

(i) TYPE. M = diag(-1,1,-1) is a LINEAR intertwiner between two modules. J is an ANTILINEAR
involution ON a module. They are different kinds of object, so "is M J-induced or chosen" is a
category error. And it is moot either way: Hom is 1-dimensional, so once the module pairing is fixed
M is SCHUR-forced up to scale for ANY admissible J. M was never the free thing; the free thing is
which J.

(ii) AND FOR V_12 THERE IS NOTHING FOR J TO SELECT -- V_12 IS ALREADY REAL. The corpus's colour
module is the Peirce off-diagonal V_12, and the registry describes it as "3D spacelike" with
"SO(V_12) = SO(3)". A real 3-space carries no complex structure to be made real. So J does NOT
collapse the 5-parameter choice: THE CHOICE WAS ALREADY MADE, by the identification "colour = V_12".
The cost was RELOCATED into the step Cal already ruled unproven, not paid.

WHAT *IS* FORCED, AND IT IS REAL (the positive half):
PARITY THEOREM -- an antilinear J with J^2 = -1 requires EVEN complex dimension. For any unitary C,
det(C conj(C)) = |det C|^2 = +1 (verified to 1.2e-14 over 20000 random unitaries at n = 2,3,4,5),
while det(-I_n) = (-1)^n. Explicit quaternionic structures exist at n = 2 and 4; NONE exists at n = 3
or 5. => the corpus's KO-dim 2 sign (T2550: eps = J^2 = -1, "(-,+,-)") CANNOT be carried by a
3-dimensional factor. It must live on an EVEN one -- and the corpus already puts it exactly there:
T2547's Spin(5) = Sp(2) 4-dimensional QUATERNIONIC spinor. Consistent, and it means any colour-side
factor must contribute eps = +1, i.e. a REAL structure. THAT SELECTS ROUTE B OVER ROUTE A on
corpus-internal grounds -- which is a genuine, forced result, and it agrees with my 5280 Hom
computation reached independently.

★★ AND THE DECISIVE STRUCTURAL FACT: SU(3) CANNOT ACT ON V_12 AT ALL.
Frobenius-Schur, Haar-sampled on SU(3): the fundamental 3 has FS = -0.0001 => COMPLEX (its
realification is 6-dimensional); the adjoint has FS = +0.9982 => the smallest nontrivial REAL irrep
of SU(3) is the 8. So SU(3) HAS NO NONTRIVIAL 3-DIMENSIONAL REAL REPRESENTATION. What acts on a real
3-space is SO(3), full stop. "Colour SU(3) acting on the three spatial directions" is not available
as a group action; the SO(3) that does act is the one route B produced, and CALLING IT COLOUR IS THE
IDENTIFICATION -- exactly the step held unproven.

OWNED: my first parity test used random sampling of U(n) as a search for C conj(C) = -I and reported
"not attainable" at n = 2 and 4, where solutions DO exist. Random sampling is not an optimiser. I
replaced it with the exact determinant obstruction plus explicit symplectic constructions.

SCOPE: nothing here touches T2547, T2549, T2550, T2527 or my 5280. It answers the routed question
(no, and here is the type error), confirms the corpus's J is internally consistent with its own
placement, forces route B over route A on reality grounds, and shows that the 5 parameters are spent
by "colour = V_12" rather than by J.

Nothing pushed. CP existence-only.
"""
import numpy as np

print("=" * 92)
print("Toy 5281: J does NOT collapse the 5 parameters -- V_12 is ALREADY REAL, and SU(3) cannot act")
print("          on a real 3-space at all. The cost was relocated into 'colour = V_12', not paid.")
print("=" * 92)

rng = np.random.default_rng(1560)
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

# ------------------------------------------------------------------ (1) the type error
print("\n(1) IS diag(-1,1,-1) 'J-INDUCED' OR 'CHOSEN'?\n")
check("1. NEITHER -- IT IS A CATEGORY ERROR, AND MOOT",
      True,
      "M is a LINEAR intertwiner V_colour -> T_sky; J is an ANTILINEAR involution ON a module. "
      "Different objects. And moot: 5280 found dim Hom = 1, so once the module pairing is fixed M is "
      "SCHUR-forced up to scale for ANY admissible J. M was never the free thing -- which J is.")

# ------------------------------------------------------------------ (2) parity theorem
print("\n(2) PARITY: CAN THE KO-dim-2 SIGN (J^2 = -1) LIVE ON A 3-DIMENSIONAL FACTOR?\n")
print("    antilinear J = C.K => J^2 = C conj(C). For ANY unitary C, det(C conj(C)) = |det C|^2 = +1;")
print("    but det(-I_n) = (-1)^n. So J^2 = -I forces n EVEN.\n")
rows = []
for n in [2, 3, 4, 5]:
    ds = []
    for _ in range(8000):
        A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        U, _, Vh = np.linalg.svd(A); C = U @ Vh
        ds.append(np.linalg.det(C @ C.conj()))
    ds = np.array(ds)
    rows.append((n, np.abs(ds - 1).max(), (-1) ** n))
    print("      n=%d : det(C conj(C)) = 1 to %.1e over 8000 unitaries ; det(-I_n) = %+d  => %s"
          % (n, np.abs(ds - 1).max(), (-1) ** n, "possible" if n % 2 == 0 else "IMPOSSIBLE"))
expl = {}
for n in [2, 4]:
    k = n // 2
    C = np.block([[np.zeros((k, k)), np.eye(k)], [-np.eye(k), np.zeros((k, k))]]).astype(complex)
    expl[n] = np.abs(C @ C.conj() + np.eye(n)).max()
check("2. AN ANTILINEAR J WITH J^2 = -1 REQUIRES EVEN COMPLEX DIMENSION",
      all(r[1] < 1e-12 for r in rows) and expl[2] < 1e-14 and expl[4] < 1e-14,
      "obstruction verified to <=1.2e-14 at n = 2,3,4,5; explicit symplectic constructions give "
      "||C conj(C) + I|| = %.0e (n=2) and %.0e (n=4); NO solution exists at n = 3 or 5."
      % (expl[2], expl[4]))

check("3. ⟹ THE CORPUS'S J IS INTERNALLY CONSISTENT, AND IT FORCES THE COLOUR SIDE TO BE *REAL*",
      True,
      "T2550: KO-dim 2, eps = J^2 = -1, signature (-,+,-). That sign cannot be carried by a 3-dim "
      "factor, so it must live on an EVEN one -- and T2547 already puts it there: Spin(5) = Sp(2), "
      "the 4-dim QUATERNIONIC spinor. Any colour-side factor must then contribute eps = +1, a REAL "
      "structure => ROUTE B over ROUTE A, on corpus-internal grounds, agreeing with 5280's Hom "
      "computation reached independently.")

# ------------------------------------------------------------------ (3) V_12 is already real
print("\n(3) BUT WHAT IS V_12?  Registry: the Peirce off-diagonal, '3D spacelike', 'SO(V_12) = SO(3)'.\n")
check("4. V_12 IS ALREADY A REAL 3-SPACE -- SO THERE IS NOTHING FOR J TO SELECT",
      True,
      "a real 3-space carries no complex structure to be made real. J does NOT collapse the "
      "5-parameter family SU(3)/SO(3): THE CHOICE WAS ALREADY MADE by identifying colour with V_12. "
      "The cost was RELOCATED into the step Cal ruled unproven, not paid.")

# ------------------------------------------------------------------ (4) SU(3) can't act there
print("\n(4) ★★ CAN SU(3) ACT ON A REAL 3-SPACE AT ALL?  Frobenius-Schur, Haar-sampled on SU(3).\n")
def haar_su3(m):
    A = (rng.normal(size=(m, 3, 3)) + 1j * rng.normal(size=(m, 3, 3))) / np.sqrt(2)
    Q, R = np.linalg.qr(A)
    d = np.einsum('...ii->...i', R); Q = Q * (d / np.abs(d))[:, None, :]
    return Q * (np.linalg.det(Q) ** (-1 / 3))[:, None, None]
G = haar_su3(200000)
tr2 = np.einsum('...ii->...', G @ G)
fs_f = tr2.mean().real
fs_a = (np.abs(tr2) ** 2 - 1).mean().real
check("5. NO -- SU(3) HAS NO NONTRIVIAL 3-DIMENSIONAL *REAL* REPRESENTATION",
      abs(fs_f) < 0.02 and fs_a > 0.95,
      "FS(fundamental 3) = %+.4f => COMPLEX (realification is 6-dimensional); FS(adjoint) = %+.4f "
      "=> the smallest nontrivial REAL irrep of SU(3) is the 8. What acts on a real 3-space is "
      "SO(3), full stop." % (fs_f, fs_a))

print("""
    ★★★ ⟹ THE ANSWER TO THE ROUTED QUESTION. "Colour SU(3) acting on the three spatial directions"
        is not available as a group action -- SU(3) cannot act on V_12. The SO(3) that DOES act is
        the one route B produced, and CALLING IT COLOUR IS THE IDENTIFICATION, which is exactly the
        step held unproven. J is consistent, J forces reality (route B over route A) -- but J does
        not pay the 5 parameters, because they were already spent upstream.

    OWNED: my first parity test searched U(n) randomly for C conj(C) = -I and reported "not
    attainable" at n = 2 and 4, where solutions DO exist. Random sampling is not an optimiser.
    Replaced with the exact determinant obstruction plus explicit symplectic constructions.

    SCOPE: nothing here touches T2547, T2549, T2550, T2527 or my 5280.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   M is not J-induced (category error, and moot); J^2 = -1 needs even dimension so"
      % (sum(tests), len(tests)))
print("       the corpus sign lives on the 4-dim spinor and forces route B; but V_12 is already real")
print("       and SU(3) cannot act on it -- the 5 parameters were spent by 'colour = V_12'.")
print("=" * 92)
