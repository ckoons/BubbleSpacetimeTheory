# The Minimal Generating Set of BST (#66) — the whole theory on one page
*Grace, 2026-08-09. The consolidated statement: ONE object, FIVE operations, every observable a reading.*

---

## The object (one)

**D_IV⁵ = SO₀(5,2) / [SO(5)×SO(2)]** — the rank-2 type-IV bounded symmetric domain (the APG).
Equivalently, **one operator**: the invariant Laplacian / Casimir **H** on the Bergman space **H²(D_IV⁵)**.
Everything below is a reading of that single operator. No second object is ever introduced.

## The five integers (read off the object — not chosen)

| integer | what it is on D_IV⁵ | value |
|---|---|---|
| rank | # of Cartan circles / boundary strata − 1 | **2** |
| N_c | census rank²−1 = short-root Peirce dim V₁₂ | **3** |
| n_C | complex dimension (Wallach-selected) | **5** |
| C₂ | K-type ground Casimir = n_C+1 | **6** |
| g | signature/embedding = 2·N_c+1 | **7** |
| N_max | N_c³·n_C + rank | **137** |

## The generating set — FIVE operations (each a way to read H)

Every BST observable is produced by applying ONE of these to the one object. In Casey's frame:
**every result IS an eigenvalue, a matrix element, or a grading of the one operator** — plus the two readings that build the arena (boundary) and the labels (count).

| # | operation | linear-algebra object | reads out | example observables |
|---|---|---|---|---|
| **1** | **COUNT** | integer weights / dimensions / rank | the five integers, quantum numbers, charges | α⁻¹=N_max=137 (charge-count); Q=integer SO(2)-weight; magic numbers |
| **2** | **SPECTRUM** (eigenvalue) | Plancherel / discrete-series eigenvalues of H | the particle mass spectrum | m_p=6π⁵m_e; lepton strata {5/2,3/2,0}; m_s/m_d=20; y_t=1 (top saturation) |
| **3** | **OVERLAP** (matrix element) | Bergman-kernel inner products ⟨f\|g⟩ | propagators, couplings, mixing angles | Cabibbo=1/√20; CKM/PMNS shape; α-correction n_C/N_max; sin²θ_W=3/13 |
| **4** | **GRADE** (decompose) | root system / Peirce / K-type grading | the forces, generations, color, CP | SU(3)×SU(2)×U(1); 3 generations=rank+1; CP forced (odd-5 quaternionic twist, T2547) |
| **5** | **RESTRICT** (to boundary) | Shilov boundary S⁴×S¹/ℤ₂ | spacetime and its signature | (3,1) Lorentzian (color-triplet irreducibility, T2545); the arena fields live on |

**Closure (T719).** Every BST observable lives in Q̄(rank, N_c, n_C, C₂, g, N_max)[π] — the algebraic closure over the five integers with π adjoined (π is forced by curvature, operation 3). There is no sixth operation and no external input: apply COUNT / SPECTRUM / OVERLAP / GRADE / RESTRICT to D_IV⁵ and you generate the Standard Model + cosmology.

## Why it's *minimal*

- **Drop the object** → nothing to read. **Drop any operation** → a whole observable class disappears (drop RESTRICT → no spacetime; drop GRADE → no forces/generations; drop SPECTRUM → no masses).
- **The object itself is forced modulo one datum** (T2548, #79): input the observed generation count (=3 boundary strata) and Korányi–Wolf forces rank=2, hence D_IV⁵. So the generating set reduces to **one measured number → one geometry → five readings → all of physics.**
- Zero free parameters: no operation has a tunable knob; each is a fixed functor of H.

## The bright-high-schooler version

There's one shape. You can do five things to it: **count** its pieces, find its **ringing tones**, measure how two tones **overlap**, sort the pieces into **families**, and look at its **edge**. Counting gives you the pure numbers (like 137). The ringing tones are the particle masses. The overlaps are how particles turn into each other. The families are the forces. The edge is space and time. That's the whole theory — one shape, five readings, nothing put in by hand.

## Honest tier note (calibrated both ways)

The *generating-set claim itself* is **Structural** (a true and useful organizing statement, not a per-observable proof). What each reading yields is tiered individually in the ledger: some Derived (m_p, Cabibbo, 3 generations, (3,1) signature, CP-existence), some Identified (mixing values, θ₁₃), some Structural (Λ, α-exact-value normalization). The one page says *how* the theory is generated; it does not upgrade any single number's tier. Λ stays Structural; α-exact stays favored-not-closed; nothing here is "derived dark energy."

---
*Cross-refs: T186 (five-integers uniqueness), T704/T1917/T2548 (object forced), T719 (observable closure), T2547 (CP via GRADE), T2545 (signature via RESTRICT), bst_this_is.md line 62 (the five readings, prose form).*
