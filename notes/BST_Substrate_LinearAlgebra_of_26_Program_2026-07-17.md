# PROGRAM — The Substrate Linear Algebra of the 26: treat the whole parameter table as one module over the primaries, find the EXACT identities that force it, and collapse the independent-input count.

**Casey's directive + Keeper design | 2026-07-17 | Realizing the Vol-16 "linearize everything" vision on the 26 itself. The neutrino sector proved the template — 4 observables forced by 2 exact integer identities (g²=45+4, N_c+g=10), target-innocent by construction (Cal: you cannot retrofit an identity among fixed integers). Now do it for all 26.**

## THE VISION (Casey)
Every BST observable lives in Q̄(6 primaries)[π] (T719). So the 26 are VECTORS in a module over the primaries. The EXACT algebraic identities among the primaries are the RELATIONS (syzygies) that FORCE the observables to be dependent — reducing the independent-input count and giving solid (exact) derivations. The three by-design may turn out FORCED by the structure (linear combinations / pinned columns), not free.

## THE SEED (verified, linalg_program_seed.py)
**All 6 primaries CHAIN from rank=2 by exact operations:**
- N_c = 2^rank − 1 = 3 (Mersenne) · n_C = rank + N_c = 5 (sum) · C_2 = rank·N_c = 6 (product) · g = 2N_c+1 = 7 · N_max = N_c³·n_C + rank = 137.
**A rich set of EXACT integer identities (the forcing relations, target-innocent):**
- g² = N_c²·n_C + rank² (49 = 45+4) · N_c + g = rank·n_C (10) · n_C = N_c + rank = g − rank · C_2 = rank·N_c = n_C+1 · g = C_2+1 · N_c·n_C = 15 = dim Sym²(V₅) · N_c·g = 21 = dim so(5,2).
**Observables ARE primary-forms** (α⁻¹ = N_c³n_C+rank; sin²θ13 = 1/(N_c²n_C) = 1/(g²−rank²); sin²θ23 = rank²/g; sin²θ12 = N_c/(N_c+g); m_s/m_d = rank²·n_C; m_t/m_b = C_2·g; sin²θ_W(M_Z) = N_c/(C_2+g)).
**THE REDUCTION:** 26 observables → Q̄(6 primaries)[π] → **rank=2 (via the chain) + π + ONE scale (gravity).** The dimensionless integer skeleton collapses to rank=2. **What stays genuinely free (the honest caveat): ONE dimensionful scale (gravity/Planck — m_e, v ride on it), π (the one transcendental), and the STRUCTURAL-tier corrections (the ~% physics the integer forms don't capture).**

## THE 5-PHASE PROGRAM
1. **[Grace] Build the primary-exponent MATRIX M of all 26 + anchors.** Each observable = a vector of primary-powers (× π-power × gravity-scale power). A 26×(6+π+scale) matrix, in the data layer. This is the linear-algebra object.
2. **[Lyra + Cal] Enumerate the SYZYGIES — all EXACT algebraic identities among the primaries** (the g²=45+4 type), up to reasonable degree. These are the forcing relations. **Cal gate: EXACT only** — an approximate numerical near-coincidence is NOT a syzygy (that's the fishing the discipline forbids). The primary chain itself is the deepest syzygy set (all from rank=2).
3. **[Grace + Keeper] Compute the RANK and NULL SPACE of M.** The null space = the linear dependencies among observables = the forced relations. The rank = the number of independent inputs. Show it's small. Each null-vector must correspond to an EXACT identity (Phase 2), not a numerical accident.
4. **[Elie] Test the 3 BY-DESIGN + 2 SOFT spots against the structure.** Are m_e (= 6π⁵α¹²m_Planck), sin²θ_W (= N_c/(C_2+g) = 3/13), α_s, m_u (√(3/14)), V_ub FORCED by the identity structure (rows in the span of the others) or genuinely INDEPENDENT? m_e folds into gravity; sin²θ_W has a form; α_s + V_ub are the honest holdouts — quantify which are forced.
5. **[Lyra] The COLUMN/form-dominance structure (Casey's key intuition).** The neutrino sector showed "pin a column (ν1 = the origin) → force the rest" — that IS a linear-algebraic constraint (form dominance). Look for the analogous pinned-column/vector structure across the OTHER sectors (CKM, masses): which vectors are pinned by geometry (target-innocent, like ν1=origin) and which follow. This is the mechanism that turns "the observable is a primary-form" into "the observable is FORCED."

## DISCIPLINE (Cal-gated, non-negotiable)
- **EXACT identities only.** g²=45+4 is a syzygy (can't retrofit). A ~% numerical match among primary-combinations is NOT — that's fishing (there are many primary-combinations; some will be close by chance). Every forcing relation must be an exact integer/algebraic identity.
- **Honest reduction claim:** "the integer skeleton reduces to rank=2" — NOT "the whole SM from one integer." The dimensionful scale (gravity), π, and the structural-tier corrections are separate and stay.
- **Target-innocence:** the identities reference only fixed integers (no observable in them) → innocent by construction (Cal). The COLUMN-pinning (Phase 5) must be geometric (like ν1=origin), not chosen to force the answer.

## THE PAYOFF (what this delivers for the 26)
- **Solid values:** exact identities replace approximate forms where they exist.
- **Independent-input count:** a rigorous statement — how many of the 26 are genuinely free vs forced (target: very few + gravity scale + π).
- **By-design resolved:** shown forced-or-free by the linear structure.
- **New derivations:** the syzygies + column-pinning FORCE observables that were only "identified forms."
- **Independent verification:** the matrix rank/null-space is a computational check of the whole table's consistency.

— Keeper + Casey, 2026-07-17. The Substrate Linear Algebra of the 26: primaries chain from rank=2; exact syzygies (g²=45+4, N_c+g=10, ...) force the observables; build the 26×primaries matrix, compute rank/null-space, test the by-design & soft spots, find the pinned-column structure (ν1=origin template). EXACT identities only (Cal). Honest reduction: integer skeleton → rank=2 + π + gravity scale + structural corrections. See [[Keeper_K719...]] (neutrino template), [[BST_Projection_Theory_substrate_to_continuum_2026-07-16]].
