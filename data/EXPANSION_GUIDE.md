# BST Data Layer — Expansion Guide

How to grow the structured data files. Target: 3-5 new entries per productive session.

---

## Schema Documentation

### `bst_constants.json`

Each constant entry:

```json
{
  "id": "unique_id",
  "name": "Human-readable name",
  "symbol": "LaTeX symbol",
  "category": "particle_mass | coupling | cosmological | nuclear | ...",
  "theorem_id": "TNNN",
  "tier": 1,
  "formula_display": "Human-readable formula string",
  "formula_code": "Python expression using EVAL_NS variables",
  "bst_value": 0.0,
  "observed_value": 0.0,
  "observed_source": "PDG 2024 | CODATA 2018 | ...",
  "precision": "0.002%",
  "unit": "MeV | GeV | dimensionless | ...",
  "bst_integers_used": ["N_c", "n_C", "g"],
  "derivation_chain": ["Step 1", "Step 2"],
  "mechanism": "Brief physical explanation",
  "source_theorems": ["T100"],
  "source_toys": [100]
}
```

**Tier definitions**:
- **Tier 1 (DERIVED)**: Computed entirely from five integers. No measured input except m_e.
- **Tier 2 (STRUCTURAL)**: Follows from D_IV^5 structure but uses an intermediate constant.
- **Tier 3 (OBSERVED)**: BST-motivated relationship, awaiting full derivation.

**EVAL_NS variables**: `rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137, alpha=1/137, pi, m_e=0.511 MeV, m_p=938.272 MeV, hbar_c=197.327 MeV*fm`. Also: `sqrt, log, ln, exp, comb, factorial, cbrt, Fraction`.

### `bst_particles.json`

Each particle entry:

```json
{
  "id": "unique_id",
  "name": "Proton",
  "symbol": "p",
  "geometric_layer": "Z_3 (quark scale)",
  "substrate_description": "Three complete S^1 windings...",
  "winding_number": 3,
  "mass_formula": "6 * pi^5 * m_e",
  "mass_value": 938.272,
  "mass_unit": "MeV",
  "charge": "+1",
  "spin": "1/2",
  "stable": true,
  "key_insight": "Brief note"
}
```

### `bst_forces.json`

Five geometric layers. Each layer entry:

```json
{
  "id": "unique_id",
  "layer": 1,
  "name": "Gravity",
  "bst_origin": "Gaussian curvature of S^2",
  "key_formula": "G = alpha^{C_2} * hbar*c / m_p^2",
  "key_constants": ["gravitational_constant"]
}
```

### `bst_predictions.json`

Each prediction:

```json
{
  "id": "PRED_NNN",
  "name": "Short name",
  "prediction": "Narrative description",
  "bst_value": "Computed value with units",
  "current_measurement": "Current best measurement",
  "experiment": "Which experiment can test this",
  "timeline": "When the test is feasible",
  "falsification_criterion": "What would disprove this",
  "status": "untested | consistent | falsified",
  "sharpest_test": false
}
```

### `bst_domains.json`

Each domain:

```json
{
  "id": "unique_id",
  "name": "Domain name",
  "ac_graph_name": "Graph identifier",
  "theorem_count": 42,
  "description": "What this domain covers",
  "key_results": ["Result 1", "Result 2"],
  "key_constants": ["constant_id_1"],
  "connections": ["other_domain_1"]
}
```

### `audit_log.json`

Managed by `toy_bst_librarian.py`. Each entry:

```json
{
  "path": "relative/path",
  "category": "data | paper | note | toy | tool | config",
  "last_audited": "YYYY-MM-DD",
  "auditor": "CI name or casey",
  "status": "current | stale | needs_review | new | deleted",
  "last_modified": "YYYY-MM-DD",
  "notes": "Audit notes"
}
```

---

## How to Add New Entries

1. **Append** the new entry to the appropriate list in the JSON file
2. **Increment** `meta.count` by 1
3. **Update** `meta.last_updated` to today's date
4. **Verify** the formula evaluates correctly: `python3 play/toy_bst_explorer.py verify <name>`
5. **Run** `python3 play/toy_bst_librarian.py crossref` to spot-check

For constants, always include `formula_code` — this enables automated verification.

---

## Priority Expansion List

### Near-term (next 30 sessions)

| Category | What to Add | Count | Source |
|----------|-------------|-------|--------|
| **Heat kernel coefficients** | a_6 through a_16, ratios, patterns | ~11 | Toys 278-639 |
| **CKM matrix elements** | V_ud, V_us, V_ub, V_cd, V_cs, V_cb, V_td, V_ts, V_tb | 9 | WorkingPaper §20 |
| **PMNS matrix elements** | U_e1..U_e3, U_mu1..U_mu3, U_tau1..U_tau3 | 9 | WorkingPaper §21 |
| **Nuclear magic numbers** | 2, 8, 20, 28, 50, 82, 126, 184 (prediction) | 8 | WorkingPaper §17 |
| **Material properties** | BCS gap, Kolmogorov 5/3, water bond angle, Debye temps | ~10 | Toys 700-706 |
| **Cosmological parameters** | H_0, T_CMB, eta_b, n_s, r, sigma_8 | ~8 | WorkingPaper §14 |
| **Meson masses** | pi, K, rho, omega, phi, J/psi, Upsilon | ~10 | WorkingPaper §12 |
| **Lepton masses** | mu, tau mass ratios | 2 | WorkingPaper §11 |

### Medium-term (next 100 sessions)

- Amino acid properties from BST (20 entries)
- Critical exponents (Ising, percolation, etc.)
- Atomic physics constants (Rydberg, Bohr radius, etc.)
- Condensed matter (Hall conductance quantization, Chandrasekhar mass)
- Turbulence parameters (Reynolds number thresholds, dissipation scale)

---

## Distinction: Constants vs Predictions vs Retrodictions

- **Constants** (`bst_constants.json`): Values derived from BST that match known measurements. These are retrodictions — BST produces a number that was already measured. The agreement is the evidence.

- **Predictions** (`bst_predictions.json`): Values derived from BST that have NOT been tested or where BST disagrees with current measurement. These are falsifiable.

- **Retrodictions** (future `bst_retrodictions.json`): When the list grows large enough, split constants into a separate retrodictions file tracking: which measurement came first, BST derivation date, and whether BST could have been tuned to match.

---

## Growth Target

**3-5 new entries per productive session** yields:
- 1 month (~30 sessions): 90-150 entries
- 3 months: 270-450 entries
- 6 months: 500+ entries (complete catalog)

At 150+ constants, the data layer becomes the authoritative reference — more complete than any single paper, machine-readable, and continuously verified by the librarian.
