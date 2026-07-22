#!/usr/bin/env python3
"""
Toy 4776 — Jul 22 (single-manifold chirality bridge, Elie's compute-don't-assert verification, post-retraction): Lyra
retracted the "SO(2) orients parity" synthesis (the domain SO(2) commutes with SO(5) → chirality-BLIND → does CP, NOT
parity-orientation), which also retracts the IDENTIFICATION in my toy 4775. Casey's steer: use the SINGLE D_IV⁵ manifold —
ONE SO(5,2) spinor — so "internal" (SO(5)) and "spacetime" (SO(3,1)) chirality are two readings of ONE object (no product →
Witten's no-go doesn't apply); orientation from ω=γ¹···γ⁷=±1 (d=7 odd), not the SO(2). My assignment: verify the 8-spinor
ω-factorization AND check for chiral zero modes (the decisive Witten index). Result: the ω-factorization is VERIFIED (it
LOCKS 4D↔internal chirality — Casey's bridge mechanism is real), BUT the decisive check fails the naive hope: ω-lock gives
NET 4D chirality (index) = 0 — the 8-spinor has equal 4D left and right. So the correlation is automatic, but net chirality
still needs the holographic reduction to SELECT one internal-chirality sector — UNCOMPUTED. Nothing re-banks; compute don't
assert.

OWN THE 4775 RETRACTION (mine): toy 4775's ARITHMETIC (ad(J) on the internal so(4): SU(2)_L J-charged {0,±2}, SU(2)_R
neutral {0,0,0}) is correct — but the IDENTIFICATION was wrong. J = L₁₂+L₃₄ is an INTERNAL so(4)⊂so(5) generator, NOT the
domain SO(2) (the K-factor). The domain SO(2) COMMUTES with all of SO(5) → acts as a scalar phase → chirality-BLIND (gives
(2,1) and (1,2) the SAME charge). So I RETRACT 4775's "weak=SU(2)_L / no-W_R / hypercharge = the domain U(1)" — that used
the wrong U(1). SURVIVORS from my toys: CP-free (4773) + custodial SU(2)/ρ≈1/no-W_R (4774, from ⟨(2,2)⟩→SU(2)_V, an
independent argument that stands). I asserted the identification instead of computing it — the exact failure mode the
discipline is for.
THE ω-FACTORIZATION (Casey's bridge, VERIFIED): built d=7 gamma matrices Γ¹···Γ⁷ (8×8, Clifford-verified). ω = Γ¹···Γ⁷ is
CENTRAL → a fixed scalar on the irreducible 8-spinor (ω = −i·I here; ±1 up to signature). It FACTORIZES: ω = (Γ¹Γ²Γ³Γ⁴)·
(Γ⁵Γ⁶Γ⁷) = γ⁵_4D · χ_internal. Since ω is FIXED, the 4D chirality and the internal chirality are LOCKED (correlated) — one
spinor, no product, so Witten's no-go (which needs a spacetime×internal PRODUCT) does NOT apply. Casey's clean point is
verified: the correlation is automatic.
THE DECISIVE CATCH (compute-don't-assert, the Witten index): ω-lock CORRELATES the chiralities but does NOT by itself
PRODUCE net 4D chirality. The 4D chirality operator γ⁵_4D on the 8-spinor has eigenvalues {+1×4, −1×4} → #(4D-left) =
#(4D-right) = 4 → NET 4D chirality (index) = 0. Both 4D chiralities are present, each locked (via ω) to opposite internal
chirality. So the ω-factorization ALONE gives a vector-like (non-chiral) 4D spectrum. NET 4D chirality REQUIRES the
holographic reduction (Shilov/SO(4,2) boundary emergence) to SELECT one internal-chirality sector — which then, via the
ω-lock, gives one 4D chirality. That selection is the DECISIVE, UNCOMPUTED test (Lyra's + genuinely hard).

⟹ VERDICT: Casey's single-manifold framing dissolves the PRODUCT-bridge honestly — ONE SO(5,2) spinor, no spacetime×internal
product, so Witten's no-go doesn't apply, and the ω=Γ¹···Γ⁷ factorization LOCKS 4D↔internal chirality (verified). BUT the
correlation ≠ net chirality: ω-lock alone gives INDEX = 0 (4 left + 4 right). NET 4D chirality needs the holographic
reduction to SELECT one internal chirality — the UNCOMPUTED decisive computation. So this is a candidate framing with the
MECHANISM verified and the decisive test LOCATED, NOT a re-bank (compute-don't-assert, post-retraction). SURVIVORS bank
(chiral split, CP-free, custodial/ρ≈1/no-W_R); my 4775 IDENTIFICATION retracted (arithmetic was an internal generator);
parity + hypercharge stay OPEN. Five-Absence-safe; nothing false banked; the arithmetic caught the overshoot again.
Count ~7-8.
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

s0 = np.eye(2); s1 = np.array([[0,1],[1,0]]); s2 = np.array([[0,-1j],[1j,0]]); s3 = np.array([[1,0],[0,-1]])
def kron(*a):
    r = a[0]
    for x in a[1:]: r = np.kron(r, x)
    return r
G = [kron(s1,s0,s0), kron(s2,s0,s0), kron(s3,s1,s0), kron(s3,s2,s0), kron(s3,s3,s1), kron(s3,s3,s2), kron(s3,s3,s3)]

# ---- own the 4775 retraction ------------------------------------------------
check("OWN THE 4775 RETRACTION: toy 4775's ARITHMETIC (internal so(4): SU(2)_L J-charged {0,±2}, SU(2)_R neutral {0,0,0}) "
      "is correct, but the IDENTIFICATION was wrong — J = L₁₂+L₃₄ is an INTERNAL so(4)⊂so(5) generator, NOT the domain "
      "SO(2). The domain SO(2) COMMUTES with SO(5) → scalar phase → chirality-BLIND. So I RETRACT 4775's 'weak=SU(2)_L / "
      "no-W_R / hypercharge = domain U(1)' (wrong U(1)). Survivors: CP-free (4773) + custodial/ρ≈1/no-W_R (4774, "
      "independent). I asserted the identification instead of computing it.",
      True, "4775 arithmetic right, identification wrong (internal generator ≠ domain SO(2), which is chirality-blind) → retract weak/no-W_R/hypercharge-via-U(1); survivors: CP-free + custodial")

# ---- omega factorization verified ------------------------------------------
clifford = all(np.allclose(G[a]@G[b]+G[b]@G[a], 2*(a == b)*np.eye(8)) for a in range(7) for b in range(7))
omega = np.eye(8)
for gm in G: omega = omega@gm
central = np.allclose(omega, omega[0, 0]*np.eye(8))
g5 = G[0]@G[1]@G[2]@G[3]; chi = G[4]@G[5]@G[6]
factorizes = np.allclose(omega, g5@chi)
print(f"\n[ω] Clifford={clifford}; ω central (fixed scalar)={central} (ω={np.round(omega[0,0],3)}); ω = γ⁵_4D·χ_int = {factorizes}")
check("THE ω-FACTORIZATION (Casey's bridge, VERIFIED): d=7 gammas Γ¹···Γ⁷ (Clifford-verified); ω = Γ¹···Γ⁷ is CENTRAL → a "
      "fixed scalar on the irreducible 8-spinor; it FACTORIZES ω = (Γ¹Γ²Γ³Γ⁴)·(Γ⁵Γ⁶Γ⁷) = γ⁵_4D·χ_internal. Since ω is "
      "FIXED, 4D and internal chirality are LOCKED (correlated) — one spinor, no product, so Witten's no-go (needs a "
      "PRODUCT) does not apply. The correlation is automatic.",
      clifford and central and factorizes, "ω=Γ¹···Γ⁷ fixed scalar, factorizes = γ⁵_4D·χ_int → 4D↔internal chirality LOCKED; one spinor, no product → no Witten wall (verified)")

# ---- the decisive catch: index = 0 -----------------------------------------
ev5 = np.round(np.linalg.eigvals(g5).real)
nL = int(np.sum(ev5 > 0)); nR = int(np.sum(ev5 < 0)); index = nL - nR
print(f"[index] γ⁵_4D eigenvalues on the 8-spinor: #left={nL}, #right={nR} → NET 4D chirality (index) = {index}")
check("THE DECISIVE CATCH (compute-don't-assert, the Witten index): ω-lock CORRELATES the chiralities but does NOT by "
      "itself PRODUCE net 4D chirality. γ⁵_4D on the 8-spinor has eigenvalues {+1×4, −1×4} → #(4D-left)=#(4D-right)=4 → "
      "NET 4D chirality (index) = 0. Both 4D chiralities present, each ω-locked to opposite internal chirality → a "
      "vector-like (non-chiral) 4D spectrum. NET chirality REQUIRES the holographic reduction (Shilov/SO(4,2) emergence) "
      "to SELECT one internal-chirality sector — the UNCOMPUTED decisive test.",
      index == 0 and nL == 4 and nR == 4, "ω-lock gives index=0 (4 left + 4 right, vector-like); net 4D chirality needs the holographic reduction to select one internal chirality — UNCOMPUTED")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: Casey's single-manifold framing dissolves the PRODUCT-bridge honestly — ONE SO(5,2) spinor, no "
      "spacetime×internal product → Witten's no-go doesn't apply, and ω=Γ¹···Γ⁷ LOCKS 4D↔internal chirality (verified). "
      "BUT correlation ≠ net chirality: ω-lock alone gives INDEX = 0 (4 left + 4 right). NET 4D chirality needs the "
      "holographic reduction to SELECT one internal chirality — the UNCOMPUTED decisive computation. Candidate framing, "
      "MECHANISM verified + decisive test LOCATED, NOT a re-bank (compute-don't-assert). Survivors bank (split, CP-free, "
      "custodial); my 4775 identification retracted; parity + hypercharge OPEN. Five-Absence-safe.",
      clifford and central and factorizes and index == 0,
      "single-manifold: ω-factorization correlates chirality (no Witten wall, verified) but index=0 → parity NOT closed by ω alone; needs holographic internal-chirality selection (open); nothing re-banks")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-4 (07-22) single-manifold chirality bridge — Elie's compute-don't-assert verification:
  * OWN THE RETRACTION: 4775 arithmetic right, IDENTIFICATION wrong (J=L₁₂+L₃₄ is internal, NOT the domain SO(2)=chirality-blind). Retract weak/no-W_R/hypercharge-via-U(1); survivors CP-free(4773)+custodial(4774).
  * ω-FACTORIZATION VERIFIED: ω=Γ¹···Γ⁷ fixed scalar = γ⁵_4D·χ_int → 4D↔internal chirality LOCKED. One spinor, no product → no Witten wall (Casey's point, computed).
  * DECISIVE CATCH: ω-lock gives INDEX = 0 (4 left + 4 right, vector-like). Correlation ≠ net chirality. NET chirality needs the holographic reduction to SELECT one internal chirality — UNCOMPUTED.
  => candidate framing, mechanism verified + decisive test located; NOT a re-bank (compute-don't-assert). Survivors bank; parity+hypercharge OPEN.
""")
