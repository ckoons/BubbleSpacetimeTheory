---
title: "Vol 10 Chapter 12 — Numerical Methods and Computation"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; Vol 10 closing; BST toy verification framework"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 12
load_bearing: "Numerical methods overview; BST toy verification practice"
---

# Chapter 12 — Numerical Methods and Computation

## Level 1 — one sentence

Numerical methods convert analytic problems into computations (ODE/PDE solvers, eigenvalue routines, Monte Carlo integration, FFTs, finite-difference/finite-element methods) — and the BST team's ~3500 toys are computational verifications using this apparatus, all archived in the `play/` directory of the BST repository.

## Level 2 — graduate-physicist precision

### 12.1 ODE solvers

- **Euler method** (forward): simplest; $O(h)$ error per step
- **Runge-Kutta 4** (RK4): $O(h^4)$; workhorse
- **Adams-Bashforth-Moulton**: multistep methods
- **Implicit methods**: for stiff equations (backward Euler, BDF, Rosenbrock)
- **Symplectic integrators** for Hamiltonian systems (preserve phase-space volume)

### 12.2 PDE solvers

- **Finite difference**: discretize derivatives; explicit/implicit/Crank-Nicolson schemes
- **Finite element**: weak form, basis functions on mesh
- **Spectral methods**: Fourier or Chebyshev basis, exponential convergence for smooth problems
- **Multigrid**: hierarchical relaxation for elliptic problems
- **Discontinuous Galerkin**: handles shocks, complex geometries

### 12.3 Linear algebra

- **LU decomposition** for solving $Ax = b$
- **QR decomposition** for least-squares, eigenvalues
- **SVD** for general matrix factorization
- **Lanczos / Arnoldi** for large sparse eigenvalue problems

Standard libraries: NumPy/SciPy, LAPACK, MAGMA (GPU), PETSc, Trilinos.

### 12.4 Monte Carlo methods

- **Plain MC**: $\int f\, d\mu \approx (1/N)\sum f(x_i)$ with $x_i$ random samples; error $\sim 1/\sqrt{N}$
- **Importance sampling**: weight by good distribution
- **Markov chain MC**: Metropolis-Hastings, Hamiltonian MC for Bayesian inference
- **Quantum MC**: path integral, world-line, lattice gauge theory

### 12.5 FFT

Fast Fourier Transform: $O(N \log N)$ vs naive $O(N^2)$. Foundation for signal processing, PDE solvers, convolution, polynomial multiplication. Cooley-Tukey 1965.

### 12.6 BST toy practice

The BST team's ~3500 toys in `play/` directory implement these numerical methods to verify specific BST predictions. Pattern:
1. State claim (docstring)
2. Define BST quantities (BST primaries, formulas)
3. Evaluate numerically
4. Compare to observation (target precision stated)
5. PASS/FAIL with explicit numerical precision
6. SCORE line at end

Casey's standing rule: every claim has a toy. Build computational evidence simultaneously with theoretical derivation.

### 12.7 K-audit anchors

- **BST `play/README.md`**: toy verification framework
- **`play/claim_number.sh`**: atomic toy-number assignment
- **2056+ toys** as of recent counts

## Level 3 — 5th-grader accessibility

**Numerical methods** = computer methods for physics. ODE solvers (RK4), PDE solvers (finite element), linear algebra (LAPACK), Monte Carlo, FFT — the standard toolkit. **BST practice**: every claim has a "toy" — a short Python script that verifies the claim numerically. ~3500 toys exist. No theorem without computational evidence. Casey's standing rule: "/toy claim before write."

---

## Vol 10 closing

This volume developed the math toolkit for the BST physics volumes. The math foundations: Hilbert spaces (Ch 1), complex analysis (Ch 2), ODEs + PDEs (Ch 3-4), Fourier (Ch 5), group theory + Lie groups (Ch 6, LOAD-BEARING), differential geometry (Ch 7, LOAD-BEARING — Bergman curvature → Newton's G), representation theory (Ch 8, LOAD-BEARING — Wallach), special functions (Ch 9), variational + path integrals (Ch 10), asymptotics + WKB (Ch 11), numerical methods (Ch 12).

Vol 11 (Generative Geometry + Topology) extends these foundations with the BST-specific math: K3 surfaces, Heegner numbers, Monster moonshine, Mersenne primes, Cremona elliptic curves, generative-geometry framing.

## Where to look this up

- Press et al., *Numerical Recipes*
- BST `play/README.md`
