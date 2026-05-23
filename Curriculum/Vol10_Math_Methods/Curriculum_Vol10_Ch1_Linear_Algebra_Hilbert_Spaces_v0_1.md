---
title: "Vol 10 Chapter 1 — Linear Algebra and Hilbert Spaces"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 1
---

# Chapter 1 — Linear Algebra and Hilbert Spaces

This volume develops the mathematical apparatus that the physics volumes use. Mathematicians often read it first; physicists read the physics volumes first and reach back for the math when needed. Both audiences are intended.

Linear algebra and Hilbert spaces underlie quantum mechanics, quantum field theory, and the substrate operator zoo of Volume 0. Bergman Hilbert space $H^2(D_{IV}^5)$ — BST's substrate Hilbert space — is a specific operator-theoretic Hilbert space with reproducing kernel structure.

## 1.1 Vector spaces and inner products

A vector space over $\mathbb{C}$ with sesquilinear inner product $\langle \cdot, \cdot \rangle$ yields the norm $\|v\| = \sqrt{\langle v, v\rangle}$. Cauchy completeness gives a Hilbert space.

## 1.2 Hilbert space basics

Hilbert space axioms (completeness + inner product) admit orthonormal bases. Linear operators $A: \mathcal{H} \to \mathcal{H}$ have adjoints $A^*$; self-adjoint operators ($A = A^*$) have real spectra and play the role of observables in quantum mechanics.

## 1.3 The Bergman Hilbert space $H^2(D_{IV}^5)$

The Bergman Hilbert space on the bounded symmetric domain $D_{IV}^5$ consists of holomorphic $L^2$ functions on $D_{IV}^5$ with the standard sesquilinear inner product. It has a reproducing kernel — the Bergman kernel — which is the structural anchor of the BST framework's Born-rule mechanism (Volume 5 Chapter 7).

The Faraut-Koranyi normalization gives $c_{FK} \cdot \pi^{9/2} = 225$ EXACTLY, an algebraic identity that runs throughout the BST substrate.

## 1.4 What comes next

Chapter 2 develops complex analysis.

---

**Where to look this up**: For standard linear algebra and Hilbert spaces: Reed and Simon, *Methods of Modern Mathematical Physics, Vol 1*; Conway, *A Course in Functional Analysis*. For Bergman Hilbert space: Faraut and Koranyi, *Analysis on Symmetric Cones*.
