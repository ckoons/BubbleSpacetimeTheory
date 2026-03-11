# SO(5,2) Uniqueness — Closing the Section 4.3 Gap

**Status**: Open problem from WorkingPaper Section 4.3, Step II. Wednesday target.

## The Gap

The paper notes: "The precise mechanism by which the S^1 real-analyticity selects the real form SO(5,2) subset SU(6,1) over other real forms requires a rigorous argument via Cartan involution theory."

## Casey's Argument (March 10, 2026)

**Claim**: SO(5,2) is the *unique* real form of so(7,C) that is both non-compact AND Hermitian symmetric.

**The four real forms of so(7,C)**:

| Real form | Compact? | Hermitian symmetric? | Why it fails |
|-----------|----------|---------------------|--------------|
| SO(7)     | Yes      | N/A                 | Compact, no bounded domain, no physics |
| SO(6,1)   | No       | No                  | K = SO(6)×SO(1) — no complex structure on tangent space, no Bergman kernel |
| SO(5,2)   | No       | **Yes**             | K = SO(5)×SO(2) — the SO(2) provides complex structure J on m |
| SO(4,3)   | No       | No                  | K = SO(4)×SO(3) — no U(1) factor, not Hermitian |

**The two-line proof**:

1. S^1 real-analyticity of the BST boundary requires holomorphic structure on the domain => Hermitian symmetric space.
2. Among real forms of so(7,C), only SO(5,2)/[SO(5)×SO(2)] is Hermitian symmetric (the SO(2) factor is essential — it generates J).

**QED.** The "open problem" closes as a classification fact.

## Wednesday Amy Session

- Verify the Hermitian symmetric classification of all real forms of so(7,C)
- Confirm SO(5,2) uniqueness via Helgason's classification table (Type BD I, p=5, q=2)
- Draft the two-line insertion for Section 4.3, Step II, replacing the open problem note
