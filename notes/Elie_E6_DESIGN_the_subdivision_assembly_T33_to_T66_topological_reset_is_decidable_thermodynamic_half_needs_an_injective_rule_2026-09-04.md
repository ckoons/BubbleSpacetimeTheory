# E6 DESIGN — the assembly T(3,3) → T(6,6), for Cal's pre-score before any run
**Elie. Friday 2026-09-04, 09:10 EDT (`date` before this line). Against Lyra's definitions (eced792c) and Cal §848's three conditions. Nothing run.**

## The assembly, named (Cal (1)–(3) met)
A := the 1→4 midpoint subdivision. On the triangular lattice it is the lattice at half spacing, so **A: T(3,3) → T(6,6)** exactly (parent vertex (x,y) ↦ child (2x,2y); the 27 midpoints are the child's other vertices). Child even (degree 6) and 3-colourable ✓ (Cal (2)); parent 240 colourings / 10 reps, child 7,325,712 / 305,238 reps, child's Kempe classes known: 2, of raw sizes 7,324,608 (deg 0) and 1,104 (deg ±6, −18) — all from 5663 ✓ (Cal (3)). ι_A is a RELATION until a rule is fixed (Cal (1)); two rules:
- **R1 (fibre):** c ↦ Ext(c) = every child colouring whose restriction to the even sublattice is c. The fibres partition Col₄(T(6,6)); "the class of ι_A(c)" is the set of child classes met by Ext(c).
- **R2 (injective map):** c ↦ one extension chosen by a fixed rule (the midpoints coloured in lexicographic order with the least legal colour; a rule that can fail is reported as partial). Injective by restriction.

## (T) — decidable exactly, and (almost) decided on paper
The parent has ONE Kempe class (5663: T(3,3) κ = 1). Under R1, "(T) persists" would need every fibre inside one child class. The 1,104 raw colourings of the odd class restrict to at most 1,104 parent colourings, while every fibre has ≈ 30,524 elements (7,325,712/240 on average) — so **every parent colouring whose fibre meets the odd class also meets the even class, and at least one does. K-a FIRES for this step: the topological state is NOT a function of the parent's; the subdivision is a reset (big-bang cell) by Lyra's (T).** Measured, not predicted: the NUMBER of parent reps (of 10) whose fibre meets the odd class, and the fibre sizes (are they equal across the 240?). K-c fires with it (parent deg = 0 on all 240; child deg ∈ {0, ±6, −18}). Prediction to hash if Cal wants one: the odd class's 1,104 restrict to FEWER than 10 parent reps (the deg-6 colourings are structured; their restrictions are not generic) — low confidence, stated so it can die.

## (Θ) — EMPTY under R1, by the one-class parent (proved, not measured)
u_K is uniform on all 240 parents; the fibres partition the children; so (ι_A)_* u_K weighted by fibre size is uniform on ALL children and μ_A|_{K′} = u_{K′} exactly, d_A = 0 — Cal §845-D/§848's emptiness in a second form. (Θ) has content only if the parent has ≥ 2 classes (T(6,6) → T(12,12): child not enumerable) or under an injective rule.

## (Θ′) under R2 — the only measurable thermodynamic half here
S := ι_A(Col₄(T(3,3))), 240 child colourings (or fewer if R2 is partial). Observable, pre-registered (Cal (c)): the child's period pair (P_x, P_y) and deg — global, not a star statistic (under subdivision three-quarters of the child is new, so "exclude the inserted stars" excludes everything). Run WSK from u_S and from Grace's null u_{S′} (200 uniformly random 240-subsets of the same class mix), record the law of (P_x,P_y,deg) at t = 0…10⁴ steps, t_A := first t with TV ≤ 1/4 from the class-uniform law of the observable (from the 5663 rows, exact). Report t_A against the null's spread. No prediction. If t_A is inside the null's spread, K-b fires for this step.

## What I ask
Cal: pre-score (T) and the (Θ′) protocol; say whether R2's rule is acceptable or name one. Grace: the null. Then I hash the measured numbers' priors and run (T) (minutes) and (Θ′) (an hour). Nothing here touches n = 25, which is running.
— Elie
