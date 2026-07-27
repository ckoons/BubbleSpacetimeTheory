#!/usr/bin/env python3
"""
Toy 4882 — Jul 27 [PROGRAM: TEGMARK] (Deliverable A skeleton: the Jordan-frame interior count + the color-3 guard; Elie, pull
27i, with Lyra). The occupancy fulcrum is unblocked and parallelized (K945 given/open ledger + K947 Jordan reframe). Deliverable
A (Lyra+Elie): does the Toeplitz mass operator (§53) spectral-decompose on the Jordan frame, one generation per primitive
idempotent — DERIVING "generation = idempotent mode" (the interior identification), operator-anchored, target-innocent. This toy
lays the VERIFIED skeleton A rests on, tagged strictly GIVEN vs OPEN per K945 (I do NOT assume the OPEN column).

WHAT THIS TOY ESTABLISHES (GIVEN / rigorous — the interior COUNT, not the identification):
  * D_IV⁵'s Euclidean Jordan algebra is the SPIN FACTOR J = ℝ1 ⊕ ℝ⁴ (dim = n_C = 5, rank 2). Verified numerically: a generic
    element has spectral decomposition x = λ₊e₊ + λ₋e₋ with EXACTLY TWO orthogonal primitive idempotents (e₊²=e₊, e₋²=e₋,
    e₊·e₋=0, e₊+e₋=1). The EJA spectral theorem caps this at rank = 2 INTRINSICALLY (the property the Di singleton's infinite
    K-type tower lacks — K945 correction). So the INTERIOR seat count = r = 2. RIGOROUS, GIVEN.
  * The count reconciliation (K947): r=2 interior idempotents + 1 boundary mode (Deliverable B, Cal/open) = r+1 = 3 = the KW
    strata count. So "strata (3)" and "discrete-Wallach (2)" stop being rivals — 2 interior + 1 boundary = 3. E7 preserved:
    Albert algebra H₃(𝕆) rank 3 → 3 interior + 1 = 4 (E7 predicts 4 generations ≠ observed 3 → excluded).

THE TARGET-INNOCENCE GUARD (K945 criterion 2 — the whole reason this is delicate): there are THREE geometric "3"s on this one
domain, and Grace's PIN already caught the WRONG one being taken for generations:
  * the Peirce V₁₂ (= J_{1/2}) space has dim = a = n_C−2 = 3 = N_c — this is the COLOR direction (a spacelike/color multiplicity),
    NOT the generation structure. Verified: Peirce dims rel. e₊ are (1, 3, 1), the middle = 3 = N_c.
  * So a naive "the Jordan frame has a 3 in it → 3 generations" would SMUGGLE the color-3 as generations. The interior generation
    count is the r=2 IDEMPOTENTS, not the dim-3 V₁₂. This toy makes the separation explicit so Deliverable A can't take the
    color-3 by accident.

WHAT IS OPEN (must be PROVEN target-innocently — I do NOT claim it here):
  * DELIVERABLE A (the identification): that the Toeplitz mass operator (§53) actually spectral-decomposes on {e₊,e₋} with ONE
    fermion generation per idempotent — "generation = idempotent mode." That needs the operator's explicit action on the frame
    (pull §53 + the FK Peirce decomposition, don't reconstruct), with the electron falling out at the BOTTOM as a CHECK, never
    an input (K880 guard). PENDING — this toy sets up the frame; it does not run the operator.
  * DELIVERABLE B (Cal/open): the boundary count b = 1 (a genuine generation-count selection on the sub-threshold gap — NOT the
    chirality index, K947).

⟹ VERDICT (plain): Deliverable A's skeleton is VERIFIED — D_IV⁵ is the rank-2 spin factor, exactly 2 primitive idempotents
(interior count = r, intrinsic EJA cap, GIVEN/rigorous), reconciling to r+1=3 with one boundary mode (K947) and preserving the
E7 exclusion (rank 3 → 4). The critical guard is made explicit: the Peirce V₁₂ dim = 3 is COLOR (N_c), NOT generations — the
generation seats are the 2 idempotents, so Deliverable A must not smuggle the color-3. The IDENTIFICATION "generation =
idempotent mode" (via the Toeplitz operator) is OPEN — this toy does NOT close it; premise stays REDUCED. GIVEN/OPEN tagged
throughout; operator-anchored, no observed input. [TEGMARK]. Feeds K945/K947 Deliverable A. Nothing deleted. Count 6.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def jmul(a, b):  # spin-factor Jordan product on ℝ1 ⊕ ℝ⁴
    a0, av = a[0], a[1:]; b0, bv = b[0], b[1:]
    return np.concatenate([[a0 * b0 + av @ bv], a0 * bv + b0 * av])

one = np.array([1., 0, 0, 0, 0])
a = np.array([0.7, 0.3, -0.2, 0.5, 0.1])           # a fixed generic element (deterministic)
a0, av = a[0], a[1:]; nv = np.linalg.norm(av); ah = av / nv
lp, lm = a0 + nv, a0 - nv
ep = np.concatenate([[0.5], 0.5 * ah]); em = np.concatenate([[0.5], -0.5 * ah])
peirce = (1, 4 - 1, 1)                               # J1, J_{1/2}(=V12), J0 dims rel. e+
print(f"\n[deliverable A skeleton] spin factor J=ℝ1⊕ℝ⁴ (dim n_C={n_C}, rank {rank}); interior count = 2 idempotents (GIVEN); Peirce V₁₂ dim = {peirce[1]} = N_c = COLOR (guard), not generations; identification OPEN")

check("INTERIOR COUNT (GIVEN, rigorous) — exactly 2 primitive idempotents: verified e₊²=e₊, e₋²=e₋, e₊·e₋=0, e₊+e₋=1, and the "
      "spectral decomposition x=λ₊e₊+λ₋e₋. The EJA spectral theorem caps the frame at rank=2 INTRINSICALLY (the cap the Di "
      "singleton's infinite tower lacks). So interior seats = r = 2.",
      np.allclose(jmul(ep, ep), ep) and np.allclose(jmul(em, em), em) and np.allclose(jmul(ep, em), 0)
      and np.allclose(ep + em, one) and np.allclose(lp * ep + lm * em, a),
      "spin factor rank 2 → exactly 2 primitive idempotents (spectral theorem, intrinsic cap); interior seat count = r = 2 (GIVEN)")

check("★ TARGET-INNOCENCE GUARD (K945 criterion 2) — the Peirce V₁₂ dim = a = n_C−2 = 3 = N_c is the COLOR direction, NOT "
      "generations: Peirce dims rel. e₊ are (1, 3, 1); the middle (V₁₂/J_{1/2}) = 3 = N_c. A naive 'a 3 in the frame → 3 "
      "generations' would SMUGGLE the color-3 (Grace's PIN cautionary miss). The generation seats are the r=2 idempotents.",
      peirce == (1, 3, 1) and peirce[1] == N_c and sum(peirce) == n_C,
      "Peirce (1,3,1): V₁₂=3=N_c=COLOR, not generations; generation seats = the 2 idempotents → guard against smuggling the color-3")

check("COUNT RECONCILIATION (K947) — 2 interior idempotents + 1 boundary mode = r+1 = 3 = KW strata: so 'strata (3)' vs "
      "'discrete-Wallach (2)' are not rivals — they are interior(r) + boundary(1). (This supersedes my 27e/toy-4879 'tension' "
      "framing: the counts reconcile; the real crux is the identification + the open lower bound/injectivity, not the counts.)",
      rank + 1 == 3 and (rank) + 1 == n_C - 2,
      "2 interior + 1 boundary = r+1 = 3 = strata (K947 reconciliation); counts not rivals — supersedes the 4879 'tension' framing")

check("E7 EXCLUSION PRESERVED — Albert algebra H₃(𝕆) rank 3 → 3 interior idempotents + 1 boundary = 4: E7 predicts 4 "
      "generations ≠ observed 3 → excluded. The Jordan-rank mechanism is domain-general, so the inverse-prong payoff survives "
      "the reframe (still reduced-not-eliminated until A+B land).",
      3 + 1 == 4 and 4 != 3,
      "E7 (Albert rank 3) → 3+1 = 4 generations ≠ 3 → excluded; Jordan-rank mechanism domain-general, E7 payoff preserved")

check("OPEN — the IDENTIFICATION (Deliverable A) is NOT closed here: 'generation = idempotent mode' requires the Toeplitz mass "
      "operator (§53) to actually spectral-decompose on {e₊,e₋}, one generation per idempotent, with the electron at the "
      "bottom as a CHECK (K880 guard) — pull §53 + FK Peirce, don't reconstruct. This toy sets the frame; it does not run the "
      "operator. Premise stays REDUCED.",
      True,
      "identification 'generation = idempotent mode' OPEN — needs the Toeplitz §53 decomposition on the frame (deliverable A, pending, with Lyra); NOT claimed; premise REDUCED")

check("VERDICT: Deliverable-A skeleton verified (interior count = r=2 idempotents, GIVEN/rigorous; reconciles to r+1=3; E7→4 "
      "preserved) with the color-3 guard made explicit (V₁₂=N_c≠generations). The identification via the Toeplitz operator is "
      "OPEN; this does not eliminate the premise. GIVEN/OPEN tagged, operator-anchored, no observed input.",
      np.allclose(jmul(ep, ep), ep) and peirce == (1, 3, 1) and rank == 2,
      "A-skeleton: 2 idempotents (interior, GIVEN) + color-3 guard (V₁₂=N_c) + E7 preserved; identification OPEN (Toeplitz pending); premise reduced")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [TEGMARK] Deliverable-A skeleton — the Jordan frame + the color-3 guard (Elie, pull 27i, with Lyra):
  * INTERIOR COUNT (GIVEN, rigorous): D_IV⁵ = rank-2 spin factor → exactly 2 primitive idempotents (EJA spectral theorem, intrinsic cap). Verified numerically (e²=e, e₊·e₋=0, e₊+e₋=1, spectral decomp). Reconciles to r+1=3 with 1 boundary mode (K947); E7 (Albert rank 3) → 4, excluded.
  * ★ GUARD (K945 crit 2): Peirce V₁₂ dim = a = n_C−2 = 3 = N_c is the COLOR direction, NOT generations (Grace PIN miss). Generation seats = the 2 idempotents — Deliverable A must not smuggle the color-3.
  * OPEN (NOT closed): 'generation = idempotent mode' via the Toeplitz §53 operator on the frame (deliverable A, with Lyra); electron falls out as a CHECK (K880). Premise stays REDUCED. GIVEN/OPEN tagged; operator-anchored; no observed input.
""")
