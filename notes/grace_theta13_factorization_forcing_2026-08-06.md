# Grace — sin²θ₁₃ = 1/45: which factorization does the geometry force? (2026-08-06, K1248)

**Cal's mirror-image catch: 1/45 has two BST factorizations and may have been value-matched-first. Task: does the geometry force one? Applied target-innocence (not a value re-fit). This settles the FACTORIZATION, not the forcing.**

## The two factorizations (both = 45)
- **A: N_c²·n_C = 9·5** — color-matrix-dim × genus. (Toy 3855 / K219 / most notes.)
- **B: n_C·(2n_C−1) = 5·9** — genus × (2n_C−1). (**The ledger entry const_024/T332 uses THIS one** — a live internal inconsistency.)

Value: 1/45 = 0.02222 vs observed 0.02224 → 0.08%, 0.027σ (within experiment).

## Target-innocence test — does each factor have an INDEPENDENT home?
| factor | independent home? |
|---|---|
| n_C = 5 | **YES** — recurs: Cabibbo sin²θ_C = 1/(rank²·n_C) = 1/20 shares the ·n_C |
| N_c² = 9 | **YES** — recurs: cos²θ_W = g/N_c² (const_145); N_c² = full color-matrix dimension |
| (2n_C−1) = 9 | **NO** — appears ONLY as this cofactor; no independent geometric role found |

**A's pieces are both target-innocent (recur elsewhere). B's (2n_C−1) is a lone coincidence** — 5·9 = 45 numerically, but only A's factorization is built from independently-motivated objects.

**Corroboration (a recurring family, not a one-off):** mixing angles of form 1/(X²·n_C) — Cabibbo 1/(rank²·n_C)=1/20, θ₁₃ 1/(N_c²·n_C)=1/45. Same ·n_C, same squared-integer structure. A sits in this family; B does not. *(Honest: WHY rank for the 1-2 and N_c for the 1-3 is part of the open forcing, not derived here — the family is corroboration of A's innocence, not a forcing proof.)*

## Verdict
- **Target-innocent factorization = A (N_c²·n_C).** Cal's flag resolved: the geometry-consistent factorization is A; B is the coincidental co-factorization.
- **FORCING still open** (K229b: "why the 1-3 overlap = 1/(N_c²·n_C)" is not a closed theorem). This settles innocence, not derivation.

## Two governance items → Casey (not executed)
1. **const_024 (T332) form B→A:** the ledger uses the non-innocent factorization n_C·(2n_C−1); should read N_c²·n_C to match the toy, the notes, and the target-innocent verdict. (Currency fix on a Derived entry.)
2. **const_024 tier D→I:** forcing open (K229b) → bare Derived is over-stated; Identified fits (target-innocent form, ~0.03σ confirmation, mechanism open) — same shape as the sin²θ_W ruling. Region-rule note: θ₁₃ is π-free and convention-robust (trichotomy), so it does not carry the running/scheme subtlety of θ_W — the value is directly comparable.

## Note
Guard held both directions: I did NOT force A because it's prettier — A wins because its factors have independent homes and B's does not; and I did NOT re-inflate (proposing D→I, not defending D). Nothing pushed.
