# Elie — toy 5840 sweep, every flagged row READ and classified (2026-09-27 15:54 EDT) — for Grace (Lane B fixes)
Instrument: play/toy_5840_… (prereg 67c5534c). Scanned 197 rows. Run 2 flags 57 rows. Run 1 LEAKED: my 'simple rational p/q, q ≤ 30' rule had no numerator bound, and it swallowed 938.272, 1089.71, 96485.33212, 1776.86 and 140.2. I fixed it (|p| ≤ 100) and kept run 1. CONTROL const_100 (H₀) is caught. NOTE: const_100's formula_code already reads '100*sqrt(0.1430/(6/19))' with 'MEASURED INPUT' in its chain in the working tree (uncommitted; presumably Grace's fix in progress). I did not touch the file.

## S / V — a measured value enters (or IS) the row, not named on its face (10, incl. the control)
| row | name | what | fix suggested |
|---|---|---|---|
| const_110 | Bottom quark mass | formula_code g/N_c·**1776.86**: measured m_τ is the base | name m_τ (measured) as the input; status 'ratio m_b/m_τ = 7/3' |
| const_123 | QCD string tension | formula_code √10·**139.57**: measured m_π. **Code ≠ chain** (the chain says m_p·√(3/14)) | reconcile; name the input |
| const_082 | Pion decay constant | formula_code contains **140.2**: a pion mass that is neither BST's 139.9 (const_057) nor the measured 139.57 | source it or replace it with const_057's expression |
| const_114 | Proton gyromagnetic ratio | code = 2·**2.7928473446**·**5.0507837461e-27**/**1.054571817e-34**: CODATA μ_p, μ_N, ħ. The row computes CODATA's own number, while the chain claims 'μ_p derived from BST' | use const_043's μ_p, or mark it as a unit conversion of a measured value |
| const_113 | Faraday constant | code = **96485.33212**, the CODATA value restated | not a BST row: move it, or mark 'SI definition' |
| const_037 | Recombination redshift | code = bare **1089.71** ('Full CAMB run'). The chain's input list omits h (H₀) and T_CMB, which CAMB requires | name the CAMB inputs (likely H₀ = 67.29 → measured ω_m, and T_CMB) |
| const_038 | Sound horizon | code = bare **144.17**, same CAMB caveat | same |
| const_101 | CMB temperature | code = bare **2.735**; the chain uses H₀ = 67.29, so it inherits the measured ω_m | name the inheritance |
| const_102 | Cosmic age | code = bare **13.78**; uses H₀ = 67.29, so it inherits the measured ω_m | name the inheritance |
| const_100 | Hubble constant (CONTROL) | measured ω_m h² = 0.1430 | in progress (working tree) |

## weak — a measured literal where BST has its own value (numerically small)
| const_031 | C–H bond | **13.6057** is the MEASURED Rydberg (α = 1/137.036); BST's own Ry = m_e/(2·137²) = 13.6128 eV (−0.05 %) | use m_e/(2·N_max²) |
| Proton charge radius | (no id) | **938.272** measured m_p; BST 6π⁵m_e = 938.254 (0.002 %); chain empty | use the namespace m_p |

## other
| const_115 | Z width | formula_code EMPTY; the chain's headline 2.486 GeV uses measured G_F and m_Z (the 'simple' 16π⁵m_e is BST) | give the row a code; name G_F |
| const_012 | W mass | the chain's ARITHMETIC writes 938.272 while saying 'm_p derived'; the code uses the namespace m_p = 6π⁵m_e (fine) | text only |

## NOT the species (read, cleared)
- **18 rows using the variable m_p:** the namespace defines m_p = 6·pi**5·m_e (derived). This is clean, and it is MY PREREG MISS: I predicted the m_p cluster would be the largest.
- Units: ħc 197.327 (const_030, 111; also the charge radius); 1e6 MeV→eV (const_061, 062).
- Every other flagged number (const_001, 007, 008, 009, 010, 013, 015, 016, 020–023, 028, 029, 034, 035, 040, 042–044, 053, 057, 058?, 073, 076–078, 083, 093, 098, 099, 105–109, 124–127) is the row's own RESULT or an OBSERVED value quoted for comparison in the chain text. It does not enter the value.
