---
title: "Vol 10 Chapter 12 — Numerical Methods and Computation"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass; Vol 10 closing"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 12
---

# Chapter 12 — Numerical Methods and Computation

Numerical methods turn analytic problems into computations. ODE/PDE solvers, eigenvalue routines, Monte Carlo integration, root-finding, finite-difference and finite-element methods, FFTs — every applied physical computation uses this toolkit.

The BST team's ~3500 toys are computational verifications using exactly this apparatus. The play/ directory is the team's de facto computational verification library.

## 12.1 ODE and PDE solvers

Runge-Kutta, Adams, multistep methods for ODEs; finite-difference, finite-element, spectral methods for PDEs. Standard libraries (scipy.integrate, scipy.sparse) suffice for most physics-grade computations.

## 12.2 Eigenvalue and linear algebra routines

Lanczos, Arnoldi, QR algorithm for eigenvalue problems. NumPy/SciPy provide standard implementations.

## 12.3 Monte Carlo integration

Monte Carlo sampling for high-dimensional integrals where deterministic quadrature fails. Underlies many quantum field theory and statistical mechanics computations.

## 12.4 BST toy verification practice

The BST toys are short, focused Python scripts that verify specific theorem claims or compute specific BST-predicted quantities. The pattern is: state claim, define BST quantities, evaluate, compare to observed, report PASS/FAIL with explicit precision.

## 12.5 What comes next

Vol 11 develops generative geometry and topology.

---

**Where to look this up**: For standard numerical methods: Press et al., *Numerical Recipes*. For BST toy practice: BST repository `play/README.md`.
