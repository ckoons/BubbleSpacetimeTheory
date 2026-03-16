---
title: "SO(5,2) Uniqueness — CLOSED (March 10, 2026)"
author: "Casey Koons & Claude 4.6"
date: "March 2026"
---

# SO(5,2) Uniqueness — CLOSED (March 10, 2026)

**Previously**: Open problem from WorkingPaper Section 4.3, Step II.
**Status**: Closed. Paper updated.

## The Argument

**Claim**: SO(5,2) is the *unique* non-compact real form of so(7,C) that is Hermitian symmetric.

**The four real forms of so(7,C)**:

| Real form | Compact? | K | Center of K | Hermitian? |
|-----------|----------|---|-------------|------------|
| SO(7)     | Yes      | SO(7) | — | Excluded (compact) |
| SO(6,1)   | No       | SO(6) | Z_2 (discrete) | No |
| SO(5,2)   | No       | SO(5) x SO(2) | contains U(1) | **Yes** |
| SO(4,3)   | No       | SO(4) x SO(3) | finite | No |

**Two-line proof**:

1. BST requires a bounded symmetric domain (Bergman kernel, holomorphic structure) => Hermitian symmetric space of non-compact type (Helgason 1978, Ch. X, Theorem 6.1: G/K is Hermitian iff center of K contains U(1)).
2. Among non-compact real forms of so(7,C), only SO(5,2) has K = SO(5) x SO(2) with SO(2) ~ U(1) in the center. The others have discrete/finite centers.

**Therefore SO(5,2) is uniquely forced.**

Confirmed by the explicit J^2 = -1 computation in Section 4.4 (Lie Algebra Verification).
