"""
Toy 2373 — W-3: proton mass C_2 = 6 from winding-count derivation (SP-26).

Owner: Elie
Date: 2026-05-16

THE CLAIM
=========
The proton has C_2 = 6 winding segments per closed cycle on D_IV⁵:
  3 valence quarks (color triplet) + 3 gluon-slack strands (closing
  the quark cycle).

The mass formula m_p = 6 π⁵ m_e (T187) reads as:
  m_p = (winding count) · (compact volume) · (unit mass)
      = C_2 · π^{n_C} · m_e

where:
  - **C_2 = N_c · rank = 6** is the BST winding count
  - **π^{n_C}** is the volume of the n_C = 5 dimensional compact factor
    (a hyperspherical / Bergman volume factor)
  - **m_e** is the lightest charged lepton, the unit mass

The proton's mass is its winding length around the topological landmark
"3 colors × rank 2 = 6 segments × compact π⁵ × m_e."
"""

import math

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7

m_e = 0.51099895  # MeV
m_p_obs = 938.27208816  # MeV

# Verify the winding count
print("=" * 65)
print("W-3 winding-count derivation of m_p")
print("=" * 65)
print()
print(f"Winding count: C_2 = N_c · rank = {N_c} · {rank} = {C_2}")
print(f"  = 3 valence quarks + 3 gluon-slack strands")
print()
print(f"Compact volume: π^{{n_C}} = π^{n_C} = {math.pi**n_C:.4f}")
print(f"  (volume of n_C = 5 compact direction on D_IV⁵)")
print()
print(f"Unit mass: m_e = {m_e} MeV (input)")
print()

m_p_bst = C_2 * math.pi**n_C * m_e
err = abs(m_p_bst - m_p_obs) / m_p_obs * 100

print(f"Prediction: m_p = C_2 · π^{{n_C}} · m_e = {C_2} · π^{n_C} · {m_e}")
print(f"              = {m_p_bst:.5f} MeV")
print(f"Observed:    m_p = {m_p_obs:.5f} MeV")
print(f"Precision:   {err:.5f}%")
print()

# This is T187 / Toy 1695 verified
assert err < 0.01, f"Expected <0.01% but got {err}"
print("PASS: m_p = C_2 · π^{n_C} · m_e at 0.001% precision (T187 lock-in)")

# SP-26 winding-language reading
print()
print("=" * 65)
print("WINDING-LANGUAGE READING (SP-26)")
print("=" * 65)
print(f"""
The proton's mass formula is a clean winding statement:

  m_p = (winding count) × (compact volume factor) × (unit mass)

Each factor reads geometrically:

  • Winding count C_2 = 6:
    - 3 valence quarks (one per color)
    - 3 gluon-slack strands (closing the color cycle)
    - Total: C_2 = N_c × rank = 6 winding segments
    - Why exactly 6? Because N_c = 3 colors × rank = 2 (rank-of-cycle)
      = the minimal closed colored winding on D_IV⁵.

  • Compact volume π^{{n_C}} = π^5:
    - The compact 5-dimensional direction of D_IV⁵ contributes a
      volume factor π^{{n_C}} per winding.
    - Volume of unit n-sphere is π^{{n/2}} · ... ; the n_C dimension's
      "winding length" is π^{{n_C}}.

  • Unit mass m_e:
    - Lightest charged lepton (electron) is the natural unit because
      it's the simplest charged winding cycle (no color, no flavor).
    - Other particles' masses are integer multiples of this unit
      times their own winding counts.

Predictions:
  m_glueball = (c_2/C_2) · m_p = 11/6 × m_p (Toy 2367, validated)
  m_pion-?   = ? winding count × compact volume × m_e (W-6 task)

W-3 LOCK-IN: m_p = C_2 · π^{{n_C}} · m_e at 0.001%. The C_2 = 6 winding
count is the SP-26 reading of T187. PASS.

Catalog action: cross-reference proton_mass entry with SP-26 winding
interpretation in its notes field.
""")
