---
title: "Vol 10 Chapter 11 — Asymptotic Analysis and WKB"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 11
---

# Chapter 11 — Asymptotic Analysis and WKB

Asymptotic analysis treats expansions valid in some limit (small parameter, large argument). The WKB method (Wentzel-Kramers-Brillouin) is a quintessential example: semiclassical expansion of the Schrödinger equation in powers of $\hbar$. Saddle-point methods, Laplace's method, stationary-phase methods all fit here.

## 11.1 Asymptotic expansions

A formal series $\sum a_n / x^n$ is an asymptotic expansion of $f(x)$ as $x \to \infty$ if the partial sums approximate $f(x)$ with error smaller than the next term. May not converge.

## 11.2 WKB method

For Schrödinger equation $\hbar^2 \psi'' = V(x)\psi$, WKB writes $\psi = \exp(iS/\hbar)$ and expands $S = S_0 + \hbar S_1 + ...$. Recovers classical mechanics at leading order; gives semiclassical quantization conditions.

## 11.3 Saddle-point and stationary-phase

For integrals $\int e^{f(z)/\hbar} dz$, saddle-point method concentrates the integral near critical points of $f$. Stationary-phase variant for oscillatory integrals.

## 11.4 What comes next

Chapter 12 develops numerical methods.

---

**Where to look this up**: For standard asymptotic methods: Bender and Orszag, *Advanced Mathematical Methods for Scientists and Engineers*.
