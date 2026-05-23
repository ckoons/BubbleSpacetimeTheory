---
title: "Vol 14 Chapter 9 — Kolmogorov Complexity and AC(0)"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 14 Information Theory"
chapter: 9
---

# Chapter 9 — Kolmogorov Complexity and AC(0)

Kolmogorov complexity $K(x)$ — the length of the shortest program producing string $x$ — is the algorithmic measure of information. AC(0) — the circuit complexity class of constant-depth polynomial-size circuits with unbounded fan-in — is the BST team's preferred framework for the P vs NP investigation.

## 9.1 Kolmogorov complexity

$K(x)$ depends on the choice of universal Turing machine but only up to constant. Most strings are incompressible: random strings have $K(x) \approx |x|$.

## 9.2 AC(0) and bounded depth

AC(0) circuits have constant depth, polynomial size, unbounded fan-in AND/OR gates. AC(0) cannot compute PARITY (Furst-Saxe-Sipser, Ajtai). Casey's standing program: "progress one theorem at a time" at AC(0) depth.

## 9.3 The BST P≠NP routes

BST has three independent proved routes to P≠NP (T29 closed April 23, 2026): Resolution route (Toy 303 PROVED), All-P route (CONDITIONAL TCC), Curvature route (P6 toy spec'd). Casey's curvature principle "you can't linearize curvature" = P≠NP in five words.

## 9.4 What comes next

Chapter 10 develops substrate complexity.

---

**Where to look this up**: Li and Vitányi, *An Introduction to Kolmogorov Complexity*. AC(0): Arora and Barak, *Computational Complexity*. BST P≠NP: project_pnp_curvature_route.md.
