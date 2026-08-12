#!/usr/bin/env python3
"""
Toy 5209: K_f IMPORTED AND RUN -- 5201, 5204 and the boundedness integral on Lyra's real kernel, at
leading-order tier as instructed. Four results, and they do not all point the same way, so I am giving the
positives first and in full because they are real. ★ (1) THE KERNEL VERIFIES INDEPENDENTLY. All 25 Clifford
anticommutators {γ^a,γ^b} = 2δ^{ab} check exactly; J² = I with signature (2,2); the causal Lagrangian is
normalised by 1/8 = 1/4n with 2n = 4, which ANSWERS MY OWN 5206 FLAG -- K_f is spin dimension 2, the Dirac case,
not the spin-dimension-1 my rank-2 model had silently assumed. Good object, correctly normalised. ★ (2) A
GENUINELY NEW POSITIVE ON THE REAL OBJECT: under Finster's closed chain the eigenvalue moduli come in
DEGENERATE PAIRS -- e.g. (1.372, 3.386, 3.386, 1.372) and (7.783, 1.931, 1.931, 7.783). That is exactly the
structure toy 5206 argued a physical fermionic projector must carry and generic random operators cannot. K_f
HAS the degeneracy. That is the thing the withdrawn 215/185 could never have shown, and it is real. ★ (3)
BOUNDEDNESS, CONFIRMED ON THE REAL KERNEL: ⟨|xy|²⟩ is finite at each cutoff radius but explodes with it --
5.5×10³ → 1.6×10⁶ → 1.7×10¹⁴ as the sampling radius goes 0.10 → 0.15 → 0.25, roughly a 26th-power growth. The
integral is finite only because the radius cuts it off. Toy 5207's theorem -- a finite cap is MANDATORY -- is
now confirmed on K_f itself rather than on a rank model. ★★ (4) AND THE ONE THAT MATTERS FOR THE ROUND'S
HEADLINE, reported straight. The favorable ~36% spacelike / ~64% timelike / 0% pathological split is computed
with the closed chain A = P(x,y)·P(x,y)^krein. FINSTER'S CLOSED CHAIN IS A_xy = P(x,y)·P(y,x). Those two are
the same object only if Krein symmetry holds -- P(y,x) = P(x,y)^krein -- and that is the very property
disclosed as unmet: I measure its relative error at MEDIAN 1.40 (140%), with the best of 200 samples still
0.67. It is not a small perturbation; it is a different operator. Running the classification with FINSTER'S
chain on the same kernel and the same points gives 0% spacelike, 0% timelike, 100% neither -- the same
degenerate bucket that killed the random-matrix model. ⟹ THE CAUSAL NON-DEGENERACY CHECK DOES NOT YET RESOLVE
FAVOURABLY ON THE REAL OBJECT UNDER FINSTER'S OWN DEFINITION. It resolves favourably under a stand-in whose
validity is precisely what is missing. ★ AND THE CONSTRUCTIVE HALF, which is why this is not a refutation: this
is not a NEW problem, it is the SAME gap with its consequence traced. Krein symmetry failing is exactly what
makes the two chains different objects. If the three named corrections restore Krein symmetry, the two chains
BECOME THE SAME OBJECT and the favourable result follows automatically. So the result is not dead -- it is
conditional on exactly the corrections already owed, and it cannot be claimed until they land. Recommendation:
@Grace HOLD the causal-non-degeneracy registration alongside the identity node; @Keeper the "resolves
favourably on the actual object" line needs the same softening the P²=P line already received. Elie running the
real object, at leading-order tier. (Lyra F946 K_f; Cal §433(c) A_xy = P(x,y)P(y,x); Finster Def 1.2.7;
toys 5201/5204/5206/5207.) CP existence-only. Nothing pushed.

WHAT I COMPUTE (all on Lyra's kernel, m = 0.3, leading-order tier):
  * Clifford 25/25 exact; J² = I, signature (2,2); Lagrangian 1/4n with 2n = 4 ⟹ spin dim 2 (my 5206 flag: answered).
  * ★ Finster chain eigenvalue moduli come in DEGENERATE PAIRS -- the structure random operators lacked.
  * ★ boundedness finite per cutoff, ~26th-power growth in radius ⟹ cap mandatory, 5207 confirmed on K_f.
  * ★★ Krein symmetry rel-error: median 1.401, best-of-200 0.670. Idempotence ‖P²−P‖/‖P‖ median 37.2.
  * ★★ causal split: Krein stand-in chain 36%/64%/0% -- Finster's own chain 0%/0%/100%.

=> VERDICT (plain): the kernel is a real object and it checks out as one -- the gamma matrices are right, the
metric is right, the normalisation quietly answers a question I had raised about spin dimension, and it carries
the paired-eigenvalue structure that random matrices could never produce. Two of the three things I was asked
to run come back positive on it. The third does not, and the reason is a substitution rather than a defect. The
favourable causal split was computed by multiplying the kernel by its own Krein adjoint, which is Finster's
closed chain only when the kernel is Krein-symmetric, and this one is off by more than its own size. Using the
product Finster actually defines, every pair lands in the degenerate bucket -- the same collapse we saw with
random matrices, on the real kernel. That does not make the kernel wrong. It makes the causal result an
IOU written against the same three corrections already owed: fix the Krein symmetry and the two products become
one product, and the answer we want follows for free. What it does mean is that nobody should say the
non-degeneracy check resolved favourably on the actual object yet, because under the actual definition it has
not.

=> DISPOSITION: K_f imported and run at leading-order tier. ★ POSITIVES, real and new: kernel verifies (Clifford
25/25, J signature (2,2)); spin dimension = 2 confirmed (answers my 5206 flag); DEGENERATE EIGENVALUE PAIRS
present -- the structure a physical projector needs and random operators lack; boundedness cap MANDATORY,
confirming 5207 on the real kernel. ★★ CORRECTION OWED TO THE BOARD: the favourable 36/64/0 split uses
A = P·P^krein, not Finster's A_xy = P(x,y)P(y,x); the two coincide only under Krein symmetry, which fails at
median 140%. Under Finster's own chain the split is 0/0/100 -- degenerate. The causal non-degeneracy check is
therefore PENDING, not resolved. Also on the record: idempotence is ‖P²−P‖/‖P‖ ≈ 37, further off than
"approximate" conveys. @Grace HOLD the non-degeneracy registration too; @Keeper soften the headline line.
NOT a refutation -- conditional on the three corrections already named. Firer: Elie. Owed from me: re-run all
of it the session the corrected kernel lands. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

import importlib.util
import collections
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

spec = importlib.util.spec_from_file_location("kf", "notes/Lyra_Kf_reference_implementation.py")
kf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kf)
J = kf.J_KREIN
M = 0.3

def krein_adj(P):
    return J @ P.conj().T @ J

def rand_pt(rng, sc=0.15):
    while True:
        z = (rng.normal(size=5) + 1j*rng.normal(size=5))*sc
        if kf.in_domain(z):
            return z

def classify(ev):
    mo = np.abs(ev)
    mx = max(mo.max(), 1e-300)
    if np.allclose(mo, mo[0], rtol=1e-6, atol=1e-12*mx):
        return "spacelike"
    if np.allclose(ev.imag, 0, atol=1e-9*mx):
        return "timelike"
    return "lightlike/other"

print("=" * 78)
print("Toy 5209: K_f imported and run -- 5201, 5204, boundedness, at leading-order tier")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The kernel verifies.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ the kernel verifies independently ---")
cliff = all(np.allclose(kf.gamma[a] @ kf.gamma[b] + kf.gamma[b] @ kf.gamma[a], 2*(a == b)*np.eye(4))
            for a in range(1, 6) for b in range(1, 6))
sig = sorted(np.linalg.eigvalsh(J).tolist())
check("All 25 Clifford anticommutators {γ^a,γ^b} = 2δ^{ab} check exactly; J² = I with signature (2,2) "
      f"(eigenvalues {sig}); and the causal Lagrangian is normalised by 1/8 = 1/4n with 2n = 4. That last "
      "detail ANSWERS MY OWN 5206 FLAG: K_f is spin dimension TWO -- the Dirac case -- not the spin-dimension-1 "
      "my rank-2 projector model had silently assumed. Good object, correctly normalised, and one open "
      "question closed in passing.",
      cliff and np.allclose(J @ J, np.eye(4)) and sig == [-1, -1, 1, 1],
      f"Clifford 25/25 ✓; J²=I ✓; signature {sig}; 1/4n with 2n=4 ⟹ spin dim 2 (5206 flag answered)")

# ---------------------------------------------------------------------------
# 2. ★ The genuinely new positive: degenerate eigenvalue pairs.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ new positive on the real object: the degeneracy random matrices lacked ---")
rng = np.random.default_rng(0)
paired = 0
samples = []
for _ in range(200):
    x, y = rand_pt(rng), rand_pt(rng)
    mo = np.sort(np.abs(np.linalg.eigvals(kf.K_f(x, y, M) @ kf.K_f(y, x, M))))
    if np.isclose(mo[0], mo[1], rtol=1e-6) and np.isclose(mo[2], mo[3], rtol=1e-6):
        paired += 1
    if len(samples) < 2:
        samples.append(np.round(mo, 4))
check("★ Under FINSTER'S closed chain the eigenvalue moduli come in DEGENERATE PAIRS -- "
      + "; ".join(str(s) for s in samples)
      + f" -- in {paired}/200 sampled pairs. That is exactly the structure toy 5206 argued a physical "
      "fermionic projector must carry and that generic random operators cannot produce. K_f HAS the "
      "degeneracy. This is a real, new result on the real object, and it is precisely the thing the withdrawn "
      "215/185 could never have shown.",
      paired >= 190,
      f"{paired}/200 closed chains show doubly-degenerate moduli -- the physical structure is present")

# ---------------------------------------------------------------------------
# 3. ★ Boundedness on the real kernel.
# ---------------------------------------------------------------------------
print("\n--- 3. ★ boundedness: the cap is mandatory, now confirmed on K_f ---")
growth = []
for sc in (0.10, 0.15, 0.25):
    r = np.random.default_rng(7)
    vals = []
    for _ in range(300):
        x, y = rand_pt(r, sc), rand_pt(r, sc)
        vals.append(float(np.sum(np.abs(np.linalg.eigvals(kf.K_f(x, y, M) @ kf.K_f(y, x, M))))**2))
    growth.append((sc, float(np.mean(vals))))
power = np.log(growth[-1][1]/growth[0][1])/np.log(growth[-1][0]/growth[0][0])
check("⟨|xy|²⟩ is finite at each cutoff radius but explodes with it: "
      + ", ".join(f"r={s:.2f} → {v:.3e}" for s, v in growth)
      + f" -- roughly a {power:.0f}th-power growth. The integral is finite ONLY because the radius cuts it "
      "off. So toy 5207's theorem -- a finite cap is MANDATORY for the causal action to exist -- is now "
      "confirmed on K_f itself rather than on a generic rank model. The cap is doing the work, on the real "
      "kernel.",
      power > 10 and all(np.isfinite(v) for _, v in growth),
      f"⟨|xy|²⟩ grows as r^{power:.0f}: {[f'{v:.2e}' for _, v in growth]} -- finite only via the cutoff")

# ---------------------------------------------------------------------------
# 4. leg1_check criterion (b): the projector algebra, quantified.
# ---------------------------------------------------------------------------
print("\n--- 4. leg1_check (b): idempotence and Krein self-adjointness, quantified ---")
r = np.random.default_rng(1)
idem, ksym = [], []
for _ in range(200):
    x = rand_pt(r)
    P = kf.K_f(x, x, M)
    n = max(np.linalg.norm(P), 1e-30)
    idem.append(np.linalg.norm(P @ P - P)/n)
    ksym.append(np.linalg.norm(krein_adj(P) - P)/n)
med_i, med_k = float(np.median(idem)), float(np.median(ksym))
check("Criterion (b) of Cal §433, measured rather than described. On the diagonal kernel: "
      f"‖P²−P‖/‖P‖ has median {med_i:.1f} and ‖P^krein−P‖/‖P‖ has median {med_k:.2f}. Lyra disclosed both as "
      "unmet and she is right to; I am putting the SIZES on the record because 'approximate' undersells the "
      f"first one -- the idempotence defect is about {med_i:.0f} times the norm of P itself, not a few percent. "
      "leg1_check (b) FAILS at leading order, as expected and as disclosed.",
      med_i > 1 and med_k > 0.5,
      f"‖P²−P‖/‖P‖ median {med_i:.1f}; ‖P^krein−P‖/‖P‖ median {med_k:.2f} -- both fail, sizes on record")

# ---------------------------------------------------------------------------
# 5. ★★ The closed-chain substitution.
# ---------------------------------------------------------------------------
print("\n--- 5. ★★ the correction owed to the board: which closed chain? ---")
r2 = np.random.default_rng(0)
cK, cF, sym_err = collections.Counter(), collections.Counter(), []
for _ in range(600):
    x, y = rand_pt(r2), rand_pt(r2)
    P = kf.K_f(x, y, M)
    Pyx = kf.K_f(y, x, M)
    sym_err.append(np.linalg.norm(Pyx - krein_adj(P))/max(np.linalg.norm(Pyx), 1e-30))
    cK[classify(np.linalg.eigvals(P @ krein_adj(P)))] += 1
    cF[classify(np.linalg.eigvals(P @ Pyx))] += 1
tot = sum(cK.values())
check("★★ The favourable split is computed with A = P(x,y)·P(x,y)^krein. FINSTER'S closed chain is "
      "A_xy = P(x,y)·P(y,x) (his Def 1.2.7; Cal §433(c) states it the same way). The two are the same object "
      "ONLY if Krein symmetry holds, P(y,x) = P(x,y)^krein -- the very property disclosed as unmet. I measured "
      f"it: median relative error {np.median(sym_err):.2f}, and the BEST of 600 samples is still "
      f"{min(sym_err):.2f}. That is not a small perturbation; it is a different operator. Same kernel, same "
      "points, the two classifications are: "
      f"Krein stand-in {dict(cK)} versus Finster's own {dict(cF)}. Under Finster's actual definition the "
      "leading-order K_f gives ZERO spacelike, ZERO timelike, and 100% neither -- the same degenerate bucket "
      "that killed the random-matrix model.",
      cF["spacelike"] == 0 and cK["spacelike"] > 0.2*tot,
      f"Krein stand-in: {dict(cK)}  |  Finster A_xy=P(x,y)P(y,x): {dict(cF)}  |  sym-error median {np.median(sym_err):.2f}")

check("⟹ THE CAUSAL NON-DEGENERACY CHECK DOES NOT YET RESOLVE FAVOURABLY ON THE REAL OBJECT UNDER FINSTER'S "
      "OWN DEFINITION. It resolves favourably under a stand-in whose validity is exactly what is missing. "
      "@Grace -- HOLD the causal-non-degeneracy registration alongside the identity node; the discipline you "
      "applied to one applies to the other. @Keeper -- the line 'resolves favourably on the actual object' "
      "needs the same softening the P²=P line already received.",
      True,
      "@Grace hold the non-degeneracy registration; @Keeper soften the headline. Pending, not resolved.")

check("★ AND WHY THIS IS NOT A REFUTATION -- it is the SAME gap with its consequence traced. Krein symmetry "
      "failing is precisely what makes the two chains different objects. If the three named corrections (the "
      "Kähler-covariant derivative, the g=7 discrete-series weight, J from the exact Cl(5,2) embedding) "
      "restore Krein symmetry, then P(y,x) = P(x,y)^krein and THE TWO CHAINS BECOME ONE -- at which point the "
      "favourable result follows automatically from what is already computed. So the causal result is not "
      "dead; it is an IOU written against corrections already owed, and it cannot be cashed until they land. "
      "I re-run all of this the session the corrected kernel appears.",
      True,
      "restore Krein symmetry ⟹ the two chains coincide ⟹ favourable result follows. Conditional, not refuted.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (kernel verifies + degeneracy present + cap mandatory; but the favourable causal split uses a stand-in chain -- under Finster's own A_xy it is 0/0/100)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5209, K_f imported and run at leading-order tier -- positives first, because they are real):
  * ★ KERNEL VERIFIES: Clifford 25/25 exact; J² = I, signature (2,2); Lagrangian normalised 1/4n with 2n = 4
    ⟹ K_f is SPIN DIMENSION 2, which answers my own 5206 flag in passing.
  * ★ NEW POSITIVE ON THE REAL OBJECT: under Finster's chain the eigenvalue moduli come in DEGENERATE PAIRS
    ({paired}/200) -- exactly the structure toy 5206 argued a physical projector must have and random operators
    cannot produce. K_f HAS the degeneracy. The withdrawn 215/185 could never have shown this.
  * ★ BOUNDEDNESS CONFIRMED ON K_f: ⟨|xy|²⟩ finite per cutoff but growing as r^{power:.0f}
    ({', '.join(f'{v:.1e}' for _, v in growth)} at r = 0.10/0.15/0.25). Finite ONLY via the cutoff ⟹ toy 5207's
    "a finite cap is mandatory" now holds on the real kernel, not just a rank model.
  * leg1_check (b) FAILS as disclosed, and here are the SIZES: ‖P²−P‖/‖P‖ median {med_i:.1f} (the idempotence
    defect is ~{med_i:.0f}× the norm of P -- "approximate" undersells it); ‖P^krein−P‖/‖P‖ median {med_k:.2f}.
  * ★★ CORRECTION OWED TO THE BOARD: the favourable ~36/64/0 split uses A = P·P^krein. Finster's chain is
    A_xy = P(x,y)P(y,x). They coincide only under Krein symmetry, which fails at median {np.median(sym_err):.2f}
    (best of 600: {min(sym_err):.2f}). Same kernel, same points: stand-in gives {dict(cK)};
    Finster's own gives {dict(cF)} -- ZERO spacelike, the same degenerate bucket that killed the random model.
    ⟹ the non-degeneracy check is PENDING, not resolved. @Grace hold that registration too; @Keeper soften
    the headline line.
  * ★ NOT A REFUTATION: it is the same gap with its consequence traced. Restore Krein symmetry via the three
    named corrections and the two chains BECOME ONE -- the favourable result then follows from what is already
    computed. An IOU against corrections already owed. I re-run everything the session the fix lands.

AUG-12. Nothing pushed. Nothing banked. Leading-order tier throughout, as instructed. Count once.
CP existence-only.
""")
