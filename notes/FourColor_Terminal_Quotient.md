---
title: "Swing 2 (honest negative): Quotient by the Terminal Reveals No New Structure"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "NEGATIVE RESULT (kept per Quaker discipline). Quotienting each residual code W_type by the terminal <(1,...,1)> removes the trivial global-relabel direction but does not expose a recognizable code (not Hamming/simplex) and does not simplify the realizability question. The terminal is confirmed trivial-for-freeing; the genuine freeing space is dim 6-7 with no special structure found."
related: ["notes/FourColor_Code_Structure.md","notes/FourColor_Disjoint_Walk.md"]
---

# Swing 2: quotient by the terminal (negative)

The terminal `(1,…,1) ∈ W_type` is the global `F_4` relabel by 3 — it is
do-nothing for freeing (a stuck coloring stays stuck under global relabel). The
hope: modding it out, `W_type / ⟨terminal⟩`, isolates the genuine freeing
directions and exposes a recognizable code or a cleaner realizability test.

## What we found

Quotient codes (coset-leader weight enumerators):

| class | quotient dim | leader-weight enumerator |
|---|---|---|
| `{R1,R6,R7}` | 6 | `1,1,5,12,26,19` |
| `{R3,R4}` | 6 | `1,2,5,8,26,22` |
| `{R2,R5}` (Set A) | 7 | `1,4,9,24,54,36` |

- **Not a named code.** None matches Hamming, simplex, or Reed-Muller weight
  enumerators. Casey's Hamming hunch does not resolve in the quotient.
- **No realizability simplification.** The terminal only pairs the four omit-targets
  `m` into two classes (`{m,m⊕3}`, `{m⊕1,m⊕2}`); the freeing condition and the
  disjoint-region walk are unchanged in substance.

## Honest conclusion

The terminal is exactly what it looked like — the trivial global-relabel direction
— and quotienting it out neither reveals a classical code nor cracks the
realizability residue. Kept as an honest negative so the path is on record:
the two-set / even-parity / single-1 / terminal structure (Code_Structure note) is
the right description, but the *terminal quotient* is not where the remaining
difficulty yields.
