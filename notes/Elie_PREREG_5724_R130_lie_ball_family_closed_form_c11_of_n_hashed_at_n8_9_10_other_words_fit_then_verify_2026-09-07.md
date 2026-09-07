# PRE-REGISTRATION — Toy 5724, Round 130: the Lie-ball family in n — a closed form for the matter word's cost, hashed at n = 8, 9, 10 before computing

**Elie, 2026-09-07 (Monday) 10:01 EDT (shell-copied). Hashed before the run.**

## What is known (5722, exact): c(1,1)(n) = 12/35, 3/8, 25/63, 33/80, 14/33 at n = 3..7. The denominators are (n+2)(n+4) (35, 48, 63, 80, 99) and the numerators 12, 18, 25, 33, 42 = n(n+5)/2. So the fitted form is
**c(1,1)(n) = n(n+5) / (2(n+2)(n+4))**, five points, three-parameter fit (two checks already inside the five).

## Hashed lines
- **F1 (can fail, blind):** c(1,1)(8) = 13/30, c(1,1)(9) = 63/143, c(1,1)(10) = 25/56 — exactly, by the Hua-kernel Gram instrument of 5722. Kill: any of the three off.
- **F2 (fit-then-verify inside the run, stated as such):** for the words (0,1), (0,2), (0,3), (1,0) compute n = 3..7 exactly, fit a rational form of degree ≤ 2/2 in n, then verify at n = 8, 9. Each verification is can-fail (a 5-point fit of a form with ≤ 4 free parameters leaves ≥ 1 internal check plus the two new points). Kill: any word whose fit fails at n = 8 or 9.
- **F3 (control):** the constant word's cost is 1/2 at n = 8, 9, 10.
- **Two shared-number traps named before reading:** (i) the numerator n(n+5) at n = 5 reads "5 × 10" and shares its FORM with T1452's k(k+5) — a coincidence of algebraic shape, not an object; (ii) c(1,1)(10) = 25/56 equals c(0,3)(5) — same fraction, different (word, n) cell.

Score X/3, of which F1 and F2 can fail.
