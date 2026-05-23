---
title: "Vol 14 Chapter 3 — Shannon Channel Capacity"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 14 Information Theory"
chapter: 3
---

# Chapter 3 — Shannon Channel Capacity

Shannon 1948 founded information theory. The Shannon entropy $H(X) = -\sum p(x)\log p(x)$ quantifies information content; channel capacity $C = \max I(X; Y)$ is the maximum rate at which information can be transmitted reliably across a noisy channel.

## 3.1 Shannon entropy

For probability distribution $p(x)$: $H(X) = -\sum_x p(x)\log_2 p(x)$. Maximum at uniform distribution; zero for deterministic.

## 3.2 Mutual information

$I(X; Y) = H(X) + H(Y) - H(X,Y)$ = how much knowing $Y$ tells you about $X$.

## 3.3 Channel capacity and Shannon's noisy-channel theorem

For a channel with input $X$, output $Y$, and noise model $p(y|x)$: the capacity $C = \max_{p(x)} I(X; Y)$ is the maximum achievable transmission rate with arbitrarily small error.

## 3.4 BST substrate channel capacity

The BST substrate's channel capacity is determined by the Koons-tick rate (samples/second) × symbols/sample on $\text{GF}(128)$. The substrate operates at its theoretical Shannon limit (or arbitrarily close) per the BST framework's optimal-coding reading (Chapter 8).

## 3.5 What comes next

Chapter 4 develops Nyquist and Koons tick.

---

**Where to look this up**: Shannon 1948 paper. Cover and Thomas, *Elements of Information Theory*.
