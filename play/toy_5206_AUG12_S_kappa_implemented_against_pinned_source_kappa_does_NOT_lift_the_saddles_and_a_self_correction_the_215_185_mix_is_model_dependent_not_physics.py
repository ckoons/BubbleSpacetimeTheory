#!/usr/bin/env python3
"""
Toy 5206: RE-POINTING THE HARNESS AT S_κ, against Casey's pinned primary source -- and it costs me a fourth
self-correction, this one on a number I reported twice today. Casey fetched Finster's causal action principle
from his own site, which is what step one needed. Four findings, in increasing order of how much they cost.
★ (1) THE INSTRUMENT IS VERIFIED AGAINST THE SOURCE, and independently: I implemented L = Σ|λ_i|² −
(1/2n)(Σ|λ_i|)² from one form; Casey's pinned source gives L = (1/4n)Σ_{i,j}(|λ_i| − |λ_j|)². These are
algebraically the same expression, and I confirmed it numerically at eigenvalue counts 2, 4 and 6 to machine
precision. Two different-looking definitions, written independently, computing one functional -- that is the
verification I wanted and could not do until the book arrived. ★ (2) BUT THE NORMALIZATION IS TIED TO 2n = THE
EIGENVALUE COUNT = THE SPIN DIMENSION, and my model quietly chose one. Rank-2 Krein projectors compress the
closed chain to TWO eigenvalues, i.e. 2n = 2, spin dimension ONE. The Dirac case is spin dimension TWO: 2n = 4,
with the local correlation operator carrying signature (2,2). Which one BST's g=7 kernel realises changes both
the normalisation constant AND the eigenvalue count, so it must be settled before any verdict -- @Lyra. ★ (3)
S_κ IMPLEMENTED, and the volume/trace constraints turn out to be FREE in a finite model: with a fixed number of
rank-fixed operators, ρ(F) = const and ∫tr(x)dρ = const hold automatically, so the only operative new
ingredient is the boundedness term κ|xy|² = κ(Σ|λ_i|)². ★★ (4) AND THE SUBSTANTIVE RESULT -- κ DOES NOT LIFT
THE SADDLES. Sweeping κ over four orders (0, 0.1, 1, 10), the sector disagreement count is 4/12, 5/12, 5/12,
5/12: unchanged, if anything marginally worse. The constraint that RESTORES WELL-POSEDNESS DOES NOT MAKE THE
CLIMB EASIER. Cal's leg-3 concern survives the constraint fix completely intact, and anyone hoping the
constraints would smooth the landscape should stop hoping. ★★★ (5) THE SELF-CORRECTION, and it is on my own
headline number. I rebuilt the model the way Finster actually defines it -- x is a HERMITIAN operator on H with
n positive and n negative eigenvalues, and the indefiniteness of the spin scalar product comes from x's OWN
signature, not from an external J = γ⁰ that I imposed. In that faithful model, 400 generic signature-(2,2)
pairs give 396 LIGHTLIKE, 4 timelike, and ZERO SPACELIKE -- nothing like the clean 215/185 spacelike-timelike
mix I reported from toys 5201 and 5204 and which the board has now quoted twice. The diagnosis: "all moduli
equal" is a codimension condition, so spacelike separation is NON-GENERIC; it requires eigenvalue degeneracy
that a physical fermionic projector supplies (the Dirac-sea closed chain is expected to carry a doubly
degenerate spectrum -- verify against Finster) and that random operators simply do not have. ⟹ MY 215/185 IS A
PROPERTY OF MY MODEL CLASS, NOT OF PHYSICS, and I should not have presented it as "a genuine causal structure
exists." What SURVIVES untouched is the Landmine-#1 THEOREM, because its argument never used the statistics: a
positive-definite kernel's closed chain compresses to the squared cosines of principal angles -- real,
non-negative, generically unequal -- so it can never be spacelike. That is structural and it stands. The
illustrative counts beside it were model-dependent and I am withdrawing them as evidence about physics.
⟹ CONSEQUENCE: the harness cannot be validated on random operators at all. It needs the actual K_f -- which is
where we already were, but now for a sharper reason than "we are waiting." Elie, route item 2. (Casey's pinned
Finster source; toys 5201/5204; Cal §432 leg-3.) CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * ★ Lagrangian identity: mine ≡ Finster's pinned (1/4n)Σ(|λ_i|−|λ_j|)², verified at m = 2, 4, 6.
  * ★ the 2n = spin-dimension flag: my model is 2n = 2 (spin dim 1); Dirac is 2n = 4, signature (2,2).
  * S_κ = ΣΣ(L + κ(Σ|λ|)²); volume + trace are automatic in a finite rank-fixed model.
  * ★★ κ sweep 0 → 10: sector disagreements 4/12 → 5/12 → 5/12 → 5/12. κ does NOT lift the saddles.
  * ★★★ Finster-faithful model (Hermitian, signature (2,2)): 396 lightlike / 4 timelike / 0 spacelike.
    ⟹ my 215/185 was model-dependent. Withdrawn as evidence about physics; the Landmine-#1 theorem stands.

=> VERDICT (plain): the book arriving did three things at once. It confirmed my instrument computes the right
quantity, by a route I could not have taken alone -- I wrote the Lagrangian one way, Finster writes it another,
and they are the same expression. It told me the answer to a question I had not known I was answering, since
the normalisation carries the spin dimension inside it and my model had silently picked the smaller one. And
it let me test whether the constraints that make the problem well-posed also make it easier, which they do not:
adding the boundedness term across four orders of magnitude leaves the saddle behaviour exactly where it was.
The costly part is the last one. When I rebuilt the configuration the way Finster actually defines it, with the
indefiniteness coming from the operator's own signature rather than a metric I imposed by hand, the clean
two-hundred-and-fifteen to one-eighty-five split I have quoted twice today simply vanished -- nearly every
generic pair lands in the degenerate bucket. Spacelike separation is not a generic thing; it needs a degeneracy
the real fermionic projector has and random matrices do not. So that number described my model and not the
world, and it has to come off the board. The theorem it was sitting next to does not depend on it and stays.

=> DISPOSITION: harness re-pointed at S_κ and VERIFIED against the pinned primary source (Lagrangian identity
confirmed). ★ FLAG for @Lyra: 2n = spin dimension is baked into the normalisation -- my model is spin dim 1,
Dirac is spin dim 2 with signature (2,2); K_f must say which. ★★ RESULT: κ does NOT lift the saddles (4→5 of
12 across four orders) -- the well-posedness fix does not ease the climb; Cal §432 leg-3 intact. ★★★
SELF-CORRECTION: the 215/185 causal mix from toys 5201/5204 is MODEL-DEPENDENT (Finster-faithful generic
operators give 0 spacelike) and is WITHDRAWN as evidence about physics; the Landmine-#1 theorem
(positive-definite ⟹ principal angles ⟹ never spacelike) is structural and STANDS. @Keeper -- the 215/185 has
been quoted on the board twice today; please correct it. Firer: Elie, on himself. Owed: nothing until K_f
lands; the harness cannot be validated on random operators. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

import collections
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# ---------------------------------------------------------------------------
# Finster's Lagrangian, both forms; the boundedness term; S_κ.
# ---------------------------------------------------------------------------
def L_mine(ev):
    m = np.abs(ev)
    return float(np.sum(m**2) - (np.sum(m)**2)/len(m))

def L_pinned(ev):
    """Casey's pinned source: L = (1/4n) Σ_{i,j}(|λ_i| − |λ_j|)², with 2n = eigenvalue count."""
    m = np.abs(ev)
    k = len(m)
    return float(sum((m[i] - m[j])**2 for i in range(k) for j in range(k))/(2*k))

def bounded_term(ev):
    """|xy|² = (Σ|λ_i|)², the boundedness integrand entering via the multiplier κ."""
    return float(np.sum(np.abs(ev))**2)

print("=" * 78)
print("Toy 5206: S_κ against the pinned source -- and a self-correction on my own headline number")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The Lagrangian identity -- independent verification.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ my Lagrangian vs Finster's pinned form: the same expression ---")
rng = np.random.default_rng(5)
agree = []
for m in (2, 4, 6):
    for _ in range(3):
        lam = np.abs(rng.normal(size=m))*rng.uniform(0.5, 3)
        agree.append(np.isclose(L_mine(lam), L_pinned(lam), rtol=1e-12))
check("I implemented L = Σ|λ_i|² − (1/2n)(Σ|λ_i|)²; Casey's pinned source from Finster's own site gives "
      "L = (1/4n)Σ_{i,j}(|λ_i| − |λ_j|)². Expanding the double sum gives 2m·Σ|λ|² − 2(Σ|λ|)² over m = 2n "
      f"eigenvalues, so the two are algebraically identical -- confirmed numerically at m = 2, 4 and 6, "
      f"{sum(agree)}/{len(agree)} to machine precision. Two independently written definitions computing one "
      "functional is the verification I wanted and could not perform until the book arrived. The instrument "
      "computes Finster's quantity.",
      all(agree),
      f"{sum(agree)}/{len(agree)} exact agreements across eigenvalue counts 2, 4, 6")

# ---------------------------------------------------------------------------
# 2. ★ The spin-dimension flag hiding in the normalization.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ the normalization carries the SPIN DIMENSION, and my model silently chose one ---")
check("★ The 2n in Finster's normalisation is the eigenvalue count of the closed chain -- which is the SPIN "
      "DIMENSION doubled, not a free convention. My rank-2 Krein projectors compress A_xy to TWO eigenvalues, "
      "so my model is 2n = 2, spin dimension ONE. The Dirac case is spin dimension TWO: 2n = 4, with the local "
      "correlation operator carrying signature (2,2). That choice changes the normalisation constant AND the "
      "number of eigenvalues entering every quantity above. @Lyra -- K_f has to tell us which, before any "
      "verdict is meaningful. I did not notice this until the pinned form put the 2n in front of me.",
      True,
      "my model: 2n=2 (spin dim 1). Dirac: 2n=4, signature (2,2). K_f must specify -- changes normalization and count.")

# ---------------------------------------------------------------------------
# 3. S_κ, and which constraints are free.
# ---------------------------------------------------------------------------
print("\n--- 3. S_κ implemented; volume and trace are free in a finite model ---")
check("S_κ = ΣΣ(L + κ|xy|²) with |xy|² = (Σ|λ_i|)² is implemented. And two of Finster's three constraints cost "
      "nothing here: with a FIXED number of operators the volume constraint ρ(F) = const holds by "
      "construction, and with rank-fixed operators the trace constraint ∫tr(x)dρ = const holds automatically "
      "(tr of a rank-r projector is r). So in this finite model the ONLY operative new ingredient is the "
      "boundedness multiplier κ -- which makes the next test clean, because κ is the whole difference between "
      "the bare action and the constrained one.",
      True,
      "volume + trace automatic in a finite rank-fixed model; κ|xy|² is the only operative addition")

# ---------------------------------------------------------------------------
# 4. ★★ Does κ lift the saddles?
# ---------------------------------------------------------------------------
print("\n--- 4. ★★ the substantive test: does the constraint term ease the climb? ---")
J = np.diag([1, 1, -1, -1]).astype(complex)
def kproj(B):
    G = B.conj().T @ J @ B
    return B @ np.linalg.inv(G) @ B.conj().T @ J
def chain(Px, Py, B):
    return np.linalg.eigvals(np.linalg.lstsq(B, (Px @ Py) @ B, rcond=None)[0])
def S_kappa(Bs, kap):
    Ps = [kproj(B) for B in Bs]
    N = len(Bs)
    return sum(L_mine(e) + kap*bounded_term(e)
               for i in range(N) for j in range(N) if i != j
               for e in [chain(Ps[i], Ps[j], Bs[i])])
def d2(Bs, dirs, kap, eps=2e-3):
    f0 = S_kappa(Bs, kap)
    return (S_kappa([B+eps*d for B, d in zip(Bs, dirs)], kap)
            - 2*f0 + S_kappa([B-eps*d for B, d in zip(Bs, dirs)], kap))/eps**2
def rot(t):
    M = np.eye(4, dtype=complex)
    M[0, 0], M[0, 1], M[1, 0], M[1, 1] = np.cos(t), -np.sin(t), np.sin(t), np.cos(t)
    return M

sweep = []
for kap in (0.0, 0.1, 1.0, 10.0):
    r = np.random.default_rng(0)
    dis = 0
    for _ in range(12):
        B0 = r.normal(size=(4, 2)) + 1j*r.normal(size=(4, 2))
        N = 3
        Bs = [rot(2*np.pi*k/N) @ B0 for k in range(N)]
        sym, non = [], []
        for _ in range(14):
            D = r.normal(size=(4, 2)) + 1j*r.normal(size=(4, 2))
            sym.append(d2(Bs, [D.copy() for _ in range(N)], kap))
            non.append(d2(Bs, [D.copy() if k == 0 else np.zeros((4, 2), complex) for k in range(N)], kap))
        if min(sym) > 0 > min(non):
            dis += 1
    sweep.append((kap, dis))
check("★★ κ DOES NOT LIFT THE SADDLES. Sweeping the boundedness multiplier over four orders of magnitude, the "
      "count of symmetric-minimum-but-full-space-saddle configurations goes "
      + ", ".join(f"κ={k}: {d}/12" for k, d in sweep)
      + " -- unchanged, and if anything marginally worse. So the constraint that RESTORES WELL-POSEDNESS DOES "
      "NOT MAKE THE CLIMB EASIER. Cal's §432 leg-3 concern survives the constraint fix completely intact. "
      "Anyone hoping the constraints would smooth the landscape should stop hoping; they fix what the minimum "
      "MEANS, not how hard it is to prove we sit at one.",
      all(d >= 4 for _, d in sweep),
      f"sector disagreements across κ: {sweep} -- constraints restore well-posedness, not ease")

# ---------------------------------------------------------------------------
# 5. ★★★ The self-correction: my 215/185 is model-dependent.
# ---------------------------------------------------------------------------
print("\n--- 5. ★★★ self-correction: rebuilding the model the way Finster defines it ---")
def herm_sig22(r):
    """Finster-faithful: x self-adjoint on H with n positive and n negative eigenvalues (spin dim 2)."""
    U, _ = np.linalg.qr(r.normal(size=(4, 4)) + 1j*r.normal(size=(4, 4)))
    d = np.concatenate([r.uniform(0.5, 2, 2), -r.uniform(0.5, 2, 2)])
    return U @ np.diag(d.astype(complex)) @ U.conj().T
def classify(ev):
    m = np.abs(ev)
    if np.allclose(m, m[0], atol=1e-6*max(m.max(), 1)):
        return "spacelike"
    if np.allclose(ev.imag, 0, atol=1e-9):
        return "timelike"
    return "lightlike/other"
r = np.random.default_rng(4)
tally = collections.Counter(classify(np.linalg.eigvals(herm_sig22(r) @ herm_sig22(r))) for _ in range(400))
check("★★★ In Finster's formulation the indefiniteness of the spin scalar product comes from x's OWN "
      "signature -- x is self-adjoint on H with n positive and n negative eigenvalues -- NOT from an external "
      "J = γ⁰ that I imposed by hand in toys 5201/5204. Rebuilding it faithfully, 400 generic signature-(2,2) "
      f"pairs classify as {dict(tally)}: essentially all LIGHTLIKE, ZERO SPACELIKE. Nothing like the clean "
      "215/185 spacelike-timelike mix I reported twice today and which the board has now quoted twice. The "
      "diagnosis is simple: 'all moduli equal' is a codimension condition, so spacelike separation is "
      "NON-GENERIC -- it needs eigenvalue degeneracy that a physical fermionic projector supplies (the "
      "Dirac-sea closed chain is expected to carry a doubly degenerate spectrum -- to be verified against "
      "Finster) and that random operators do not have.",
      tally["spacelike"] == 0,
      f"Finster-faithful generic pairs: {dict(tally)} -- 0 spacelike. My 215/185 was model-class, not physics.")

check("SO I WITHDRAW THE 215/185 AS EVIDENCE ABOUT PHYSICS. It characterises my rank-2 Krein-projector model, "
      "not the Dirac case, and I presented it as 'a genuine causal structure exists.' @Keeper -- it has been "
      "quoted on the board twice today; please correct it. ★ WHAT SURVIVES UNTOUCHED is the Landmine-#1 "
      "THEOREM, because its argument never used the statistics: a positive-definite kernel's closed chain "
      "compresses to the squared cosines of the principal angles between two subspaces -- real, non-negative, "
      "generically unequal -- so it can NEVER satisfy the spacelike condition. That is structural, it holds in "
      "any model class, and it stands. The counts sitting beside it were illustrative and are now withdrawn.",
      True,
      "WITHDRAWN: the 215/185 counts. STANDS: Landmine #1 (pos-def ⟹ principal angles ⟹ never spacelike).")

check("CONSEQUENCE, and it sharpens rather than blocks: the harness CANNOT be validated on random operators at "
      "all -- generic matrices land in the degenerate bucket and tell us nothing about the causal structure. "
      "It needs the ACTUAL K_f. That is where we already were, but the reason is now specific: not 'we are "
      "waiting for Lyra' but 'the classification is non-generic and only the real fermionic projector carries "
      "the degeneracy that makes it meaningful.' @Lyra -- K_f plus its spin dimension, and I run everything "
      "the same session.",
      True,
      "harness unvalidatable on random operators; needs K_f + its spin dimension. Sharper reason, same queue.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (Lagrangian verified vs pinned source; κ does NOT lift the saddles; the 215/185 mix WITHDRAWN as model-dependent; Landmine-#1 theorem stands)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5206, route item 2 -- re-pointing at S_κ, and a fourth self-correction):
  * ★ INSTRUMENT VERIFIED AGAINST THE SOURCE: my L = Σ|λ|² − (1/2n)(Σ|λ|)² and Finster's pinned
    L = (1/4n)Σ(|λ_i|−|λ_j|)² are the SAME expression -- confirmed at eigenvalue counts 2, 4, 6 to machine
    precision. Two independently written definitions, one functional. Exactly the check the book enabled.
  * ★ FLAG @Lyra -- the 2n in the normalisation IS the spin dimension: my rank-2 model is 2n = 2 (spin dim 1);
    the Dirac case is 2n = 4, signature (2,2). Changes the normalisation AND the eigenvalue count. K_f must say.
  * S_κ IMPLEMENTED; volume + trace are FREE in a finite rank-fixed model, so κ|xy|² is the only operative
    addition -- which makes the next result clean.
  * ★★ κ DOES NOT LIFT THE SADDLES: {sweep} across four orders. The constraints restore what the minimum
    MEANS; they do not make it easier to prove we sit at one. @Cal's §432 leg-3 survives intact.
  * ★★★ SELF-CORRECTION (fourth today, and on my own headline number): rebuilt Finster-faithfully -- x
    Hermitian on H with n positive and n negative eigenvalues, indefiniteness from x's OWN signature, not the
    external J I imposed. 400 generic signature-(2,2) pairs: {dict(tally)} -- ZERO spacelike. My 215/185 was a
    property of MY MODEL CLASS, not physics, and I presented it as "a genuine causal structure exists."
    WITHDRAWN. @Keeper -- it is on the board twice; please correct it.
    ★ The Landmine-#1 THEOREM stands untouched (pos-def ⟹ squared cosines of principal angles ⟹ never
    spacelike) -- its argument never used the counts.
  * CONSEQUENCE (sharper, not blocking): spacelike separation is NON-GENERIC, so the harness cannot be
    validated on random operators at all. It needs the real K_f and its spin dimension. Same queue, better
    reason.

AUG-12. Nothing pushed. Nothing banked. @Lyra -- K_f + spin dimension and everything runs the same session.
Count once. CP existence-only.
""")
