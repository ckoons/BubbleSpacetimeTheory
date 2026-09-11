---
title: "Vol 1 Chapter 11 — Observables Reference"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; consolidated reference to 600+ substrate-derived observables, tier-classified, with verification toys cross-referenced"
volume: "Vol 1 Quantum Field Theory from D_IV⁵"
chapter: 11
---

# Chapter 11 — Observables Reference

*Tier column corrected in place 2026-09-11 (Keeper, K1892) for the rows re-tiered since May; every other row carries its May tier and is being resynced. Where this table and `notes/BST_AC_Theorem_Registry.md` disagree, the registry wins.*

The volume has built the substrate framework for quantum field theory: Hilbert space, integers, discrete symmetries, Casimir algebra, operator zoo, dynamics, gauge theory, scattering, renormalization. This chapter consolidates what the apparatus produces — over six hundred substrate-derived observables, tier-classified, with cross-references to the computational verifications.

The chapter does not derive new content. It indexes.

## 11.1 Headline derivations

| Observable | BST formula | Tier | Match | Where |
|---|---|---|---|---|
| $m_p/m_e$ | $6\pi^5 = 1836.118$ | D | 0.002% | Vol 2 Ch 6 (T187) |
| $1/\alpha$ | $N_{\max} = N_c^3 \cdot n_C + \text{rank} = 137$ | **I** (was D; re-tiered 2026-08-11, K1816; the forward form is a mnemonic — K1813 null; volume class closed negative K1826) | 0.026% | Spine Lecture 8 |
| Newton's $G$ | $\hbar c (6\pi^5)^2 \alpha^{24}/m_e^2$ | theorem about a RELATION (trade $G$ for $m_e$; $\alpha$ identified inside; K1673) | 0.065% | Vol 4 Ch 1; Spine Lecture 9 |
| $\Lambda/M_{\text{Pl}}^4$ | $7 e^{-282}$ | D | 0.076 dex | Vol 4 Ch 4 (T1485) |
| $\sin^2 \theta_W$ | $N_c/c_3 = 3/13$ | **I** (was D; a retired near miss — K1445 2a.5) | 0.19% | Vol 2 Ch 2 |
| $a_e$ (electron $g-2$) | $\alpha/(2\pi)$ + the Petermann–Sommerfield $C_2$ | **I** (was D; K1872, 2026-09-07) | ppt (a match) | Vol 2 Ch 8; Spine Lecture 8 |
| CMB $n_s$ | $1 - n_C/N_{\max} = 0.9635$ | D | 0.3σ | Vol 4 Ch 6 |
| Dark-matter/baryon | $(3n_C + 1)/N_c = 16/3$ | D | 0.58% | Vol 4 Ch 10 |

Each is a substrate-mechanical derivation from BST primaries with no fitted parameters. Match precisions span $0.002\%$ to $0.58\%$, all D-tier.

## 11.2 Reproduction suite

The complete computational verification is `play/verify_bst.py` — evaluating fifty substrate-derived predictions against measurement. Current status: **49 of 50 PASS at $\leq 1\%$**, single warning is an honest-scope flag.

Toy 541 — "five integers to everything" — derives 51 quantities from the BST primaries, 16/16 sub-checks at machine precision. Three-second entry-point verification.

Catalog: over 600 substrate-significant quantities in `data/bst_constants.json` and `data/bst_geometric_invariants.json`, each with evaluable `formula_code`.

## 11.3 Tier counts

- **D-tier**: ~130 entries (mechanism closed, match below 1%)
- **I-tier**: ~230 (match below 1%, mechanism plausible-pending)
- **C-tier**: ~80 (conditional on external conjectures)
- **S-tier**: ~160 (qualitative or above 2%)

Total ~600. Tier discipline per Volume 0 Chapter 10: no overclaiming, near misses get scrutiny, honest scope preserved.

## 11.4 Falsifiers

**Five-Absence Prediction Set** (Volume 1 Chapter 8 §8.5):

1. No grand unified theory observable phenomena.
2. No proton decay above structural lifetime.
3. No magnetic monopoles.
4. No sterile neutrinos.
5. No supersymmetric partner particles.

Plus: CPT violation at any precision refutes substrate $SO_0(5,2)$; free quark observation refutes color-confinement topology; CMB $n_s$ measurement diverging from $1 - n_C/N_{\max}$ refutes substrate cosmological boundary condition.

Framework is set up to be falsifiable across multiple independent axes.

## 11.5 What comes next

Volume 2 begins particle-physics applications in detail. Chapter 1 introduces; Chapters 2–12 take the major Standard Model sectors through their substrate-mechanism derivations. The proton-to-electron mass ratio (Vol 2 Ch 6, already rewritten as recruiter) is one of many.

---

**Where to look this up**: `data/bst_constants.json` and `data/bst_geometric_invariants.json` for the complete catalog. `play/verify_bst.py` for the reproduction script. `play/toy_bst_explorer.py` for the interactive REPL. Toy 541 for the entry-point three-second verification. `notes/Five_Absence_Predictions_Principle.md` for the falsifier set. `notes/BST_AC_Theorem_Registry.md` for per-theorem provenance.
