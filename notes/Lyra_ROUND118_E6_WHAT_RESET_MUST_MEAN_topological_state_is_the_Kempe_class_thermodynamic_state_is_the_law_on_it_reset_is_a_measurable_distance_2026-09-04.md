# Round 118 E6 — WHAT "RESET" MUST MEAN, before any number
**Lyra. Friday 2026-09-04, 09:03 EDT (from `date`, rendered 09:03:17). Casey's sentence under test: "thermodynamics resets after a big bang or a new assembly." T633's clause is POSITED (K1859 B2). This file defines the words so that E6 can fail.**

## 0. The spaces
- **Col₄(T)** with the WSK dynamics at zero temperature: one step = a uniformly chosen Kempe change (colour pair {i,j}, a component of the {i,j}-subgraph, swap). Each step is an involution, so the transition matrix is symmetric.
- **Topological state** of a colouring c: its Kempe class [c] ∈ Col₄(T)/~ (a WSK ergodic component). Invariants of the topological state: Mohar–Salas's deg mod 12 (E4: the parity of the charge-neutral period area).
- **Thermodynamic state**: a probability law μ on a fixed class K. The WSK stationary law on K is UNIFORM (symmetric chain on a connected component) — call it u_K. "Thermodynamic equilibrium" = μ = u_K.
- **Assembly step**: a construction map A: T → T′ (vertex insertion carrying its colouring; the inverse of a reduction), with the induced map on colourings ι_A: Col₄(T) → Col₄(T′) — the inherited colouring. A must be stated as a map before anything is measured.

## 1. The two halves of "reset", as measurements
**(T) Topological persistence / topological reset.** The assembly A *preserves the topological state* if ι_A maps each Kempe class of T into ONE Kempe class of T′ (the class of ι_A(c) depends only on [c]); it *resets* it if some class of T is split by ι_A across two or more classes of T′, or if the invariant of ι_A(c) is not a function of the invariant of c. Big-bang case = reset; interstasis case = persistence. Measurement: the partition of ι_A(K) by classes of T′, for every class K of T. Statement to be proved or refuted per construction step, not asserted.
**(Θ) Thermodynamic reset.** Push the parent's equilibrium forward: μ_A := (ι_A)_* u_K, a law on Col₄(T′) supported on the classes hit. Within a hit class K′, "the inherited state starts cold" means μ_A restricted to K′ is far from u_{K′}:
  d_A(K′) := ‖ μ_A|_{K′} − u_{K′} ‖_TV.
The NULL (Grace): a uniformly random subset S ⊂ K′ with |S| = |ι_A(K) ∩ K′|, d_null := ‖u_S − u_{K′}‖_TV, which is the finite-size floor 1 − |S|/|K′|; "cold" = d_A(K′) exceeds the null's distribution (it cannot exceed 1 − |S|/|K′| for an injective ι_A, so on that face the right statistic is the MIXING one below).
**(Θ′) Thermalization time.** t_A(K′) := the number of WSK steps from the law μ_A|_{K′} to TV distance ≤ 1/4 from u_{K′}; null: the same from u_S for random S of the same size. "Thermodynamics resets" (Casey's sentence, made falsifiable) = t_A is finite and the chain forgets μ_A: TRUE by ergodicity within a class, with a rate; the CONTENT is whether t_A ≫ t_null (the inherited law is structured, not a random subset) or t_A ≈ t_null (the assembly step is already "hot"). Either outcome is a result; neither is a law until (T) is decided across a family of steps.

## 2. What would make it a LAW
A conserved quantity under a named dynamics across the assembly step: (T) = persistence for every step in a family, with the invariant (E4's det/12 mod 2, or the height datum if E5(i) = YES) carried by ι_A — that is "knowledge conservation across assemblies". A reset of (T) at some step is not a failure of the program; it is the big-bang cell, and its frequency across steps is the number to report.

## 3. Pre-scored kills (Cal to hold)
K-a: ι_A is not well defined on classes for a single-vertex insertion on T(9,9) (a class splits) — then (T) is false at the smallest step and "persistence" is not generic. K-b: t_A within the null's spread on every step — then "cold start" has no content on lattice tori. K-c: the invariant of ι_A(c) is not a function of the invariant of c — the topological state does not survive the assembly at all.
— Lyra
