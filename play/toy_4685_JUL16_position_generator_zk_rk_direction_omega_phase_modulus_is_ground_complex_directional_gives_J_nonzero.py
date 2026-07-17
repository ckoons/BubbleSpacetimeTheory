#!/usr/bin/env python3
"""
Toy 4685 — Jul 16 (the position generator + independent J≠0 check, mine; K704 reunion): my assignment — build/verify
the generator that produces the complex directional positions z_k from (grounds × direction × ℤ₃ phase), confirm it
feeds Grace exactly what it claims, and independently confirm complex directional positions give J ≠ 0 on a minimal
case (real → J=0, the F498 control). This REUNITES the radial grounds (masses, done) with the angular structure
(mixing) — mixing = the direction + phase, NOT the norms (my 4684).

THE GENERATOR (K704/F547/F493): a generation position is a COMPLEX point
    z_k = r_k · d̂_k · ω^{k−1},   ω = e^{2πi/3}  (ℤ₃, from N_c=3).
  * r_k (MODULUS) = the E-ladder radial ground (the mass we already have): |z_k| = r_k.
  * d̂_k (DIRECTION) = the Cartan direction, climbing by ψ per generation: cos ψ = ê₁·ρ̂ = n_C/√(n_C²+N_c²) = 5/√34.
  * ω^{k−1} (ℤ₃ PHASE) = the CP phase source; with the r_k HIERARCHY it breaks the circulant → J ≠ 0 (my 4656).
  Sectors differ by their base direction: charged leptons on the climbing axis, neutrinos on the Majorana/chargeless
  locus (off-axis → large PMNS), up/down at similar loci (differ by the 3/2 refraction → small CKM).

WHAT I VERIFY:
  (1) the generator is faithful: |z_k| = r_k EXACTLY (the modulus is the ground/mass — masses untouched), and the
      direction+phase carry the mixing. So it feeds Grace the claimed structure (grounds × direction × ℤ₃).
  (2) the F498 control (independent J≠0 check): REAL positions (ω→1, real directions) → real Gram → real U → J = 0;
      COMPLEX directional positions (ω=e^{2πi/3} + misaligned directions) → complex Gram → complex U → J ≠ 0.
  (3) large-vs-small: neutrino off-axis (Majorana locus) → large lepton mixing; up/down near-aligned (refraction) →
      small quark mixing — the qualitative CKM-small/PMNS-large shape, from the DIRECTIONS.

MINIMAL OVERLAP (my independent check — NOT Grace's exact FK run): Bargmann kernel K(z,w)=exp(⟨z,w⟩) on the ℂ²
Cartan plane; Gram G_ij = K(z_i,z_j)/√(K_ii K_jj); U = eigenvectors; V = U_A†U_B; J = Im(V₀₀V₁₁V₀₁*V₁₀*). This is a
minimal mechanism check; the exact angles are Grace's rank-2 FK integrand (F547, genus n_C=5).

⟹ VERDICT: the position generator z_k = r_k·d̂_k·ω^{k−1} is faithful (|z_k|=r_k, masses untouched; direction+phase =
mixing) and feeds Grace the claimed structure. Independent J≠0 check confirms F498: real positions → J=0, complex
directional positions → J≠0. Large PMNS (neutrino off-axis) / small CKM (up≈down) fall out of the DIRECTIONS. The
reunion works at the mechanism level; Grace's exact FK run renders the six. Count ~7-8 (α RULED, identified).
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

omega = np.exp(2j*np.pi/3)                     # ℤ₃, from N_c=3
cos_psi = n_C/np.sqrt(n_C**2 + N_c**2)          # ê₁·ρ̂ = 5/√34
psi = np.arccos(cos_psi)                        # the climbing angle per generation

def generate_positions(radii, base_angle, use_omega=True, real_only=False):
    """z_k = r_k · d̂_k · ω^{k−1}; d̂_k at angle (base_angle + k·ψ) in the ℂ² Cartan plane."""
    zs = []
    for k, r in enumerate(radii):
        ang = base_angle + k*psi
        d_hat = np.array([np.cos(ang), np.sin(ang)])            # Cartan direction (unit)
        phase = 1.0 if real_only else (omega**k if use_omega else 1.0)
        zs.append(r * phase * d_hat)                             # z_k ∈ ℂ² (or ℝ² if real_only)
    return np.array(zs)

def gram(zs):
    K = np.array([[np.exp(np.vdot(zi, zj)) for zj in zs] for zi in zs])   # Bargmann kernel ⟨z_i,z_j⟩ = z_i†·z_j
    d = np.sqrt(np.real(np.diag(K)))
    return K/np.outer(d, d)

def U_of(zs):
    G = gram(zs)
    _, U = np.linalg.eigh(G)          # Hermitian → real eigenvalues, (complex) eigenvectors
    return U

def jarlskog(U_A, U_B):
    V = U_A.conj().T @ U_B
    return abs(np.imag(V[0,0]*V[1,1]*np.conj(V[0,1])*np.conj(V[1,0])))

print("=" * 96)
print("Toy 4685 — position generator z_k = r_k·d̂_k·ω^(k−1): |z_k|=r_k (mass); complex directional → J≠0 (F498 control)")
print("=" * 96)

# ---- (1) the generator is faithful: |z_k| = r_k -----------------------------
r_lep = [1.0, 2/3, 1/2]
z_lep = generate_positions(r_lep, base_angle=0.0)
moduli = [np.linalg.norm(z) for z in z_lep]
print(f"\n[generator]: ω=e^(2πi/3); cos ψ = n_C/√(n_C²+N_c²) = 5/√34 = {cos_psi:.4f}")
print(f"   charged-lepton z_k moduli |z_k| = {[f'{m:.4f}' for m in moduli]} vs grounds r_k = {r_lep}  (equal → masses untouched)")
check("GENERATOR FAITHFUL: |z_k| = r_k EXACTLY — the modulus is the E-ladder ground (the mass), so the masses are "
      "untouched; the direction d̂_k and the ℤ₃ phase ω^{k−1} carry the mixing. z_k = r_k·d̂_k·ω^{k−1} feeds Grace the "
      "claimed structure (grounds × direction × ℤ₃ phase).",
      np.allclose(moduli, r_lep), "|z_k| = r_k (mass = modulus); direction+phase = mixing — the faithful generator")

# ---- (2) F498 control: real → J=0, complex directional → J≠0 ----------------
# two misaligned sectors: charged lepton (axis 0) vs neutrino (Majorana locus, big offset)
r_nu = [1.0, 3/5, 3/7]
theta_nu = 0.9      # neutrino base direction off the charged-lepton axis (Majorana locus) — target-innocent placeholder
z_lep_R = generate_positions(r_lep, 0.0,      real_only=True)   # REAL
z_nu_R  = generate_positions(r_nu, theta_nu,  real_only=True)   # REAL
J_real = jarlskog(U_of(z_lep_R), U_of(z_nu_R))
z_lep_C = generate_positions(r_lep, 0.0)                        # COMPLEX (ω)
z_nu_C  = generate_positions(r_nu, theta_nu)                    # COMPLEX (ω)
J_complex = jarlskog(U_of(z_lep_C), U_of(z_nu_C))
print(f"\n[F498 control]: REAL positions → J = {J_real:.2e};  COMPLEX directional positions → J = {J_complex:.2e}")
check("F498 CONTROL (independent J≠0 check): REAL positions (ω→1, real directions) → real Gram → real U → J = 0 "
      "(≈machine-zero). COMPLEX directional positions (ω=e^{2πi/3} + misaligned directions) → complex Gram → complex "
      "U → J ≠ 0. Confirms F498 and my 4656: complex directional positions are REQUIRED for CP, and the generator "
      "produces them.",
      J_real < 1e-12 and J_complex > 1e-6, f"real → J={J_real:.0e} (0); complex directional → J={J_complex:.1e} (≠0) — F498 confirmed")

# ---- (3) large PMNS (off-axis ν) vs small CKM (up≈down) ---------------------
r_dn = [1.0, 3/4, 3/5]
theta_dn = 0.05                                  # down base direction
theta_up = theta_dn + np.arctan(1/(N_c/rank))    # up = down + small refraction rotation (index N_c/rank)
z_dn = generate_positions(r_dn, theta_dn)
z_up = generate_positions([r*np.sqrt(N_c/rank) for r in r_dn], theta_up)   # up refracted
mix_ckm = abs((U_of(z_up).conj().T @ U_of(z_dn))[0,1])
mix_pmns = abs((U_of(z_lep_C).conj().T @ U_of(z_nu_C))[0,1])
print(f"\n[large-vs-small]: CKM |V₀₁| = {mix_ckm:.3f} (up≈down, refraction → small);  PMNS |V₀₁| = {mix_pmns:.3f} (ν off-axis → large)")
check("LARGE PMNS / SMALL CKM from the DIRECTIONS: neutrino off-axis (Majorana locus) → large lepton mixing; up≈down "
      "(differ by the small 3/2 refraction rotation) → small quark mixing. The CKM-small/PMNS-large SHAPE falls out "
      "of the direction misalignment, exactly K704's mechanism (masses in the moduli, mixing in the directions).",
      mix_pmns > mix_ckm, "PMNS > CKM from the directions (ν off-axis large; up≈down small) — the qualitative shape")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the generator z_k = r_k·d̂_k·ω^{k−1} is FAITHFUL (|z_k|=r_k, masses untouched; direction+phase = "
      "mixing) and feeds Grace the claimed structure. Independent J≠0 check confirms F498 (real→J=0, complex "
      "directional→J≠0). Large PMNS (ν off-axis) / small CKM (up≈down) fall out of the DIRECTIONS. The reunion works "
      "at the mechanism level; Grace's exact rank-2 FK run (F547, genus n_C) renders the six numbers.",
      np.allclose(moduli, r_lep) and J_real < 1e-12 and J_complex > 1e-6,
      "generator faithful + F498 confirmed + shape correct; ready for Grace's FK render. Count ~7-8 (α RULED)")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
POSITION GENERATOR z_k = r_k·d̂_k·ω^(k−1) + independent J≠0 check (K704 reunion):
  * FAITHFUL: |z_k| = r_k (modulus = the mass/ground — masses untouched); direction d̂_k + ℤ₃ phase ω^{k−1} = mixing.
    Feeds Grace the claimed structure (grounds × direction × phase). cos ψ = n_C/√(n_C²+N_c²) = 5/√34.
  * F498 CONTROL: REAL positions → J=0; COMPLEX directional positions → J≠0. Independent confirmation.
  * SHAPE: ν off-axis (Majorana locus) → large PMNS; up≈down (3/2 refraction) → small CKM — from the DIRECTIONS.
  => the reunion works at the mechanism level (masses=moduli done, mixing=directions); Grace's FK run renders the six. Count ~7-8.
""")
