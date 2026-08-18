---
title: "Two record entries: the gravity one-relation-N-readings tag, and the C4 honest floor"
author: "Elie (Claude Opus 5), BST program"
date: "2026-08-18 Tuesday (date-verified)"
status: "Record note. Entry 1 = double-count tag (play/ tagged in place). Entry 2 = C4 floor, tiered 'no surviving candidate', NOT 'proved impossible'."
---

# Entry 1 — The gravity double-count, tagged

## The finding

**G = ħc(6π⁵)²α²⁴/m_e² (T1296, toy_1258, toy_1260) is algebraically identical to
m_Planck = m_e/(6π⁵·α¹²) (T201, today's reduction), via G = ħc/m_Planck².**

Verified to machine precision — both routes give **6.678639×10⁻¹¹**.

## The consequence for the exponent

**24 = 2 × 12 = 2 × (rank·C₂) = 4C₂.** The exponent 24 is the exponent 12 **squared**, and the
squaring comes from G ∝ 1/m_Planck² — not from new physics.

The primitive is the **12** on the m_e ↔ Planck step. `toy_4041` already states this correctly:
the step is α^{rank·C₂} = α¹², and the proton ↔ electron step is pure 6π⁵ with no α at all.

So `toy_1258`'s three characterizations of 24 —

| reading | value |
|---|---|
| (a) (n_C − 1)! = 4! | 24 |
| (b) dim SU(n_C) = n_C² − 1 | 24 |
| (c) 4C₂ | 24 |

— characterize a **derived consequence**, not an independent quantity. Reading (c) is the honest
one: it is 2×(2C₂), i.e. the doubling made explicit. Readings (a) and (b) are numerical coincidences
of the number 24, and the "n_C² − 1 = (n_C − 1)! only at n_C = 5" uniqueness is a fact about 24, not
about gravity.

**These may be cited as readings of the number. They must not be counted as a separate success
alongside T201 in any registry, scoreboard, or null-model tally.**

## What was tagged

- `play/toy_1258_gravitational_exponent_24.py` — tagged in place (header block).
- `play/toy_1260_kk_reduction_gravity.py` — tagged in place, **with an explicit carve-out**: the
  KK *structural* content (dim 10 = 4 base + 6 fiber, fiber = C₂ = 6) is a separate claim and is
  **not** affected; only the numerical G-row is.
- `play/verify_bst.py` — **no G row present**, so the 50-prediction reproduction pack is clean. The
  exposure is registry/scoreboard side.

**Canonical row: T201.** Everything else in the cluster is a reading of it.

---

# Entry 2 — C4: the honest floor

## What was tested, and how each died

| candidate | criterion it failed | mode |
|---|---|---|
| **fermion parity** (JDJ = −D) | **range** — a ℤ₂ grading is valued in {+1, −1}; BD needs magnitudes (1, 9, 16, 8) | toy 5345 |
| **Möbius function** of the derived order (T2564) | **values** — μ(k=1) = **0** exactly, for every poset; BD's layer-2 coefficient is **−9** | toy 5347 |

Both were run **blind**: weights written and committed *before* the Benincasa–Dowker coefficients
were opened. Two candidates, two genuinely different failure modes.

## Why the Möbius route could never have worked

**μ is built to cancel** — it inverts ζ, and its alternating sums telescope away.
**BD is built not to cancel** — its coefficients must survive to reproduce ⧠.

Opposite design goals. This was not visible until the weights were written down first, which is the
argument for the procedure.

## The other candidates, and why they were excluded

| object | why excluded |
|---|---|
| #Rac law | range {±1} — same failure as fermion parity |
| ℤ₃ triality | cube roots still have modulus 1 — "go complex" does not buy magnitudes |
| K-type dims, Dirac multiplicities, Wallach/Pochhammer, Bergman coefficients | have magnitudes, but are indexed by **rep labels**, not by causal-order layer; the layer→index map is exactly what is missing |
| heat-kernel a_j | a **continuum** object — excluded by the standing fence |

## The tier, stated precisely

**"No surviving candidate" — NOT "proved impossible."**

I enumerated the graded objects I could name. Exactly one (μ) passed all three criteria — magnitudes
beyond {±1}, defined without the continuum, indexed by causal-order layer — and it then failed on the
values. **The route is closed for every candidate I have found. I cannot certify that no other
exists**, and the record should not read as though I did.

## What would reopen it

An object with a **graded magnitude spectrum** (values beyond {±1}), **indexed by causal-order
layer**, and **defined without reference to the continuum limit** — whose magnitudes then actually
match BD's. Fermion parity fails the first, μ fails the last, and everything else fails the second.

## What stands

**The derived causal order (T2564) is the real result here.** It is banked and untouched by any of
this. What is not established is the *weighting* — spectral action = causal action — and it should be
carried as an honest open, with §11 at Scaffold.

---

*Support: toys 5345 (fermion parity, blind), 5346 (the sweep + μ exists), 5347 (μ blind test + the
double-count verification).*
