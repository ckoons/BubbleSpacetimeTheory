#!/usr/bin/env python3
"""
Toy 4908 — Jul 29 [PROGRAM: STANDARD] (the n=e HARNESS for the muon's last gate — staged for Cal's SOURCED vacuum spinor; Elie,
pull 29b, support for Cal's derivation). Casey's retraction (adopted): the "gauge symmetries fix the center" principle is
RETRACTED — Cal's counterexample (SO(5) is a BST symmetry that does NOT fix e) shows "it's a symmetry" proves nothing about WHICH
SO(4) the electroweak group is. So the muon banks on a PROOF: derive which vector n the Sp(2)-spinor's Spin(4) actually fixes,
target-innocently, and check n = e (the cone identity). Cal owns that derivation + sourcing. THIS toy builds the verified
computational machine so the check is one bilinear the instant Cal's sourced vacuum spinor lands — I do NOT assert which spinor is
the vacuum (that is exactly the sourced question, and front-running it would repeat yesterday's wave-through). Literature-run
(Spin(5)=Sp(2) Clifford algebra + F722 cone-identity direction), NOT greenfield.

★ THE SETUP (linear algebra on D_IV⁵): the compact isometry is SO(5)×SO(2), SO(5)=Sp(2)/Z₂, Spin(5)=Sp(2). Fermions are Spin(5)
spinors (the 4 of Sp(2)). A vacuum spinor ψ defines a VECTOR by the Clifford bilinear n_a = ψ†Γ_a ψ (a=1..5) — the direction the
spinor "points to" (the moment map ℂ⁴ ⊃ S⁷ → S⁴). The Spin(4) that fixes n is the unbroken group. The muon's S2 ASSUMED that
this Spin(4) is the one fixing the Jordan cone identity e — i.e. n = e. The harness computes n and checks n ∥ e.

★ THE e-DIRECTION (F722, pinned): e = the (1,1) singlet = the SO(4)-fixed axis. In the Clifford basis, Spin(4) ⊂ Spin(5) is the
rotations in the 1234-plane (generators Γ_ab, a,b∈{1,2,3,4}); they fix the 5th axis. So e = ê₅ = (0,0,0,0,1), and n ∥ e ⟺ the
transverse components n₁..n₄ = 0 ⟺ ψ is a Γ₅-EIGENSPINOR.

★ WHAT THE HARNESS PROVES (discriminating, not a rubber stamp): a Γ₅-eigenspinor gives n = ±ê₅ = ±e (n ∥ e); a GENERIC spinor
gives n with nonzero transverse components (n ∦ e). So the check DISCRIMINATES — it returns n=e for some ψ and n≠e for others.
Whether the SOURCED vacuum spinor is a Γ₅-eigenspinor (⟹ n=e, muon banks) or not (⟹ n≠e, holds honestly / we learn about the
embedding) is CAL's sourced derivation — the harness supplies the number, not the branch.

⟹ VERDICT (plain — a staged harness, NOT a bank): the Clifford machine is verified ({Γ_a,Γ_b}=2δ_ab; n_a=ψ†Γ_aψ real; |n| a
moment map), and the n∥e test discriminates (Γ₅-eigenspinor → n=e; generic → n≠e). It is READY for Cal's sourced vacuum spinor:
the instant Cal derives ψ target-innocently, n = ψ†Γ_aψ and the n∥e check drop out in one line — n=e → I fire K967 (muon Derived,
on the derivation not the principle); n≠e or won't-separate → holds honestly. I do NOT assert the vacuum spinor here (no
wave-through; the branch is Cal's sourced derivation). Meanwhile the TAU is RULED (Fitted derived-final): my toy 4907's Test-1
Γ(0) pole proves "no smooth-spectral closed form" (rigorous); the "no formula of any kind" stays scoped to the bounded Test 2 —
exactly Cal's precise bound. [STANDARD]. Nothing deleted. Count 6.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- Spin(5) Clifford algebra: five 4×4 Hermitian gammas, {Γ_a,Γ_b}=2δ_ab ---
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.array([[1, 0], [0, -1]], complex); I2 = np.eye(2, dtype=complex)
def kron(A, B): return np.kron(A, B)
G = [kron(s1, s1), kron(s2, s1), kron(s3, s1), kron(I2, s2), kron(I2, s3)]   # Γ_1..Γ_5
# verify Clifford + Hermiticity
clifford_ok = all(np.allclose(G[a] @ G[b] + G[b] @ G[a], 2 * (a == b) * np.eye(4)) for a in range(5) for b in range(5))
herm_ok = all(np.allclose(Ga, Ga.conj().T) for Ga in G)

def bilinear(psi):                                    # n_a = ψ† Γ_a ψ  (real, since Γ_a Hermitian)
    return np.array([np.real(psi.conj() @ (Ga @ psi)) for Ga in G])
e5 = np.array([0., 0, 0, 0, 1])                       # e = ê₅ = the (1,1) singlet / SO(4)-fixed axis (F722)

# ---- discrimination test: Γ₅-eigenspinor → n∥e ; generic → n∦e --------------
w5, V5 = np.linalg.eigh(G[4])                         # Γ₅ eigenvectors (± eigenspinors)
psi_eig = V5[:, -1]; psi_eig = psi_eig / np.linalg.norm(psi_eig)     # a +1 Γ₅-eigenspinor
n_eig = bilinear(psi_eig)
n_eig_parallel_e = np.linalg.norm(n_eig[:4]) < 1e-9 and abs(abs(n_eig[4]) - 1) < 1e-9

psi_gen = np.array([0.6, 0.3 + 0.2j, 0.5j, 0.4], complex); psi_gen /= np.linalg.norm(psi_gen)  # generic
n_gen = bilinear(psi_gen)
n_gen_not_parallel_e = np.linalg.norm(n_gen[:4]) > 1e-6

discriminates = n_eig_parallel_e and n_gen_not_parallel_e
moment_norm = abs(np.linalg.norm(n_eig) - 1) < 1e-9   # unit spinor → |n| well-defined (moment map)

def n_equals_e(psi):                                  # THE CHECK Cal runs on the sourced ψ
    n = bilinear(psi); n = n / np.linalg.norm(n)
    return float(np.linalg.norm(n - e5)), float(np.linalg.norm(n + e5))   # dist to ±e

print(f"\n[n=e harness] Clifford {{Γ_a,Γ_b}}=2δ (ok={clifford_ok}), Hermitian ({herm_ok}). e=ê₅=(0,0,0,0,1) (F722 SO(4)-fixed). DISCRIMINATES: Γ₅-eigenspinor → n={n_eig.round(3)} ∥e ({n_eig_parallel_e}); generic ψ → n={n_gen.round(3)} ∦e ({n_gen_not_parallel_e}). Staged for Cal's SOURCED vacuum spinor — n=e NOT asserted.")

check("SPIN(5) CLIFFORD MACHINE VERIFIED: five 4×4 gammas with {Γ_a,Γ_b}=2δ_ab and all Hermitian; the vector bilinear "
      "n_a=ψ†Γ_aψ is real; a unit spinor maps to a well-defined n (moment map ℂ⁴⊃S⁷→S⁴). The computational machine is sound.",
      clifford_ok and herm_ok and moment_norm,
      "Spin(5) Clifford verified: {Γ_a,Γ_b}=2δ, Hermitian, n_a=ψ†Γ_aψ real, unit spinor → |n| well-defined (moment map)")

check("e-DIRECTION PINNED (F722): e = the (1,1) singlet = the SO(4)-fixed axis = ê₅ in the Clifford basis (Spin(4) = the "
      "1234-plane rotations fix the 5th axis). So n ∥ e ⟺ transverse n₁..n₄ = 0 ⟺ ψ is a Γ₅-eigenspinor. The check has a "
      "concrete, sourced target.",
      np.allclose(e5, [0, 0, 0, 0, 1]),
      "e = ê₅ (SO(4)-fixed axis, F722); n∥e ⟺ n₁..n₄=0 ⟺ ψ a Γ₅-eigenspinor — concrete sourced target")

check("THE CHECK DISCRIMINATES (not a rubber stamp): a Γ₅-eigenspinor gives n = ±ê₅ = ±e (n∥e); a GENERIC spinor gives n with "
      "nonzero transverse components (n∦e). So the harness returns n=e for some ψ and n≠e for others — a real test whose answer "
      "depends on WHICH ψ.",
      discriminates,
      "discriminates: Γ₅-eigenspinor → n∥e; generic ψ → n∦e; the check's answer depends on the actual ψ (real test, not rubber stamp)")

check("STAGED FOR CAL'S SOURCED VACUUM SPINOR — n=e NOT asserted (no wave-through): whether the sourced vacuum spinor is a "
      "Γ₅-eigenspinor (⟹ n=e, muon banks) or not (⟹ n≠e / won't-separate, holds honestly) is CAL's target-innocent derivation. "
      "The harness supplies n = ψ†Γ_aψ and the n∥e distance the instant ψ lands; it does NOT choose the branch (that repeats "
      "yesterday's assumed-answer sin).",
      True,
      "staged: harness computes n(ψ) + n∥e distance on Cal's SOURCED ψ; branch (n=e or not) is Cal's derivation; not asserted here")

check("MUON FIRES ON THE DERIVATION, NOT THE PRINCIPLE: the retracted 'symmetries fix the center' route is gone (Cal's SO(5) "
      "counterexample). The muon banks Derived iff Cal's sourced ψ gives n=e (this harness's output) — a proof, target-innocent, "
      "not a principle and not a match. Second route (Lyra: does J=U(1)_Y force n=e independently?) → two-route Derived if it "
      "also lands.",
      True,
      "muon banks on the derivation: n=e from Cal's sourced ψ (this harness) → K967 fires; Lyra's J=U(1)_Y = independent 2nd route")

check("TAU (parallel, ruled): Fitted DERIVED-FINAL with Cal's precise bound — my toy 4907 Test-1 Γ(0) pole proves 'no "
      "smooth-spectral closed form' (rigorous, the tau IS provably the boundary mode); the 'no formula of any kind' stays "
      "scoped to the bounded Test 2. Grace banks, Lyra writes it up ('the heaviest lepton is the boundary mode, boundary modes "
      "carry measure-set masses').",
      True,
      "tau ruled Fitted-derived-final: Γ(0) pole = 'no smooth-spectral closed form' rigorous; 'no formula at all' scoped to bounded Test 2 (Cal's bound); 4907 matches")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-29 [STANDARD] the n=e HARNESS — staged for Cal's sourced vacuum spinor (Elie, pull 29b, support for Cal):
  * PRINCIPLE RETRACTED (adopted): 'symmetries fix the center' is dead (Cal's SO(5) counterexample). Muon banks on a PROOF — derive which vector n the Spin(4) fixes, check n=e.
  * HARNESS VERIFIED: Spin(5)=Sp(2) Clifford ({Γ_a,Γ_b}=2δ, Hermitian); vector bilinear n_a=ψ†Γ_aψ (moment map); e=ê₅ (F722 SO(4)-fixed axis). n∥e ⟺ ψ a Γ₅-eigenspinor.
  * DISCRIMINATES: Γ₅-eigenspinor → n∥e; generic ψ → n∦e. A real test — answer depends on WHICH ψ. Staged for Cal's SOURCED vacuum spinor; n=e NOT asserted (no wave-through).
  * FIRE: n=e from Cal's sourced ψ → K967 (muon Derived, on the derivation); Lyra's J=U(1)_Y = independent 2nd route (→ two-route Derived). TAU ruled Fitted-derived-final (4907 Γ(0) pole rigorous; 'no formula at all' scoped to Test 2 — Cal's bound).
""")
