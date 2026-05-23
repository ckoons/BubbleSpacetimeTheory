---
title: "Vol 0 Chapter 6 — The Integer Web"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; preserves v0.1 substance (Casey-named Integer Web Principle, multi-integer catalog statistics, substrate-comprehensive backbone, Mersenne tower cross-coupling T2451, three-layer over-determinism T2465)"
volume: "Vol 0 Substrate Foundation"
chapter: 6
---

# Chapter 6 — The Integer Web

In standard physics, the fundamental constants are isolated. The inverse fine-structure constant $1/\alpha \approx 137.036$ sits in one part of the table, the proton-to-electron mass ratio $m_p/m_e \approx 1836.15$ sits in another, the weak mixing angle $\sin^2\theta_W \approx 0.23$ in a third. They are measured separately, tabulated separately, and to the extent that they are connected, the connections are model-dependent — derivations within QED or the Standard Model that link some constants to others, leaving most of the table as independent inputs.

In BST, the situation is structurally different. The five BST primary integers and the cap $N_{\max}$ do not sit alone. Each integer is the center of a *web* of relations — identities, theorems, catalog invariants, experimental observables — that other parts of the framework attach to. Many catalog entries belong to several webs at once: an identity that simultaneously involves $N_c$, $n_C$, and $C_2$ sits at the intersection of three webs. A small number of entries belong to *all six* webs at once; these are the substrate's most structurally rich identities.

This network of webs and their intersections is what Casey named, in May 2026, the **Integer Web Principle**. It is one of the eight standing structural principles of BST. This chapter is its presentation.

The principle is short to state. The longer version of it — which we will work toward over the course of the chapter — is that the integers' interconnection topology is itself a substrate signature. The framework's coherence is not visible in any individual derivation. It is visible in how the derivations *use the same numbers*.

## 6.1 What Casey saw

The principle as Casey first formulated it, in the substrate-ontology consolidation work of May 20, 2026, reads:

> Inside the substrate, the boundaries are the integers, and each integer holds a web.

There are two claims here. The first is that BST primary integers play a *boundary* role — they are not merely numerical labels but structural endpoints around which the substrate organizes itself. The second is that each such endpoint anchors a *network*: each integer can be tied, by explicit derivation or empirical match, to a set of further mathematical objects, physical observables, and other integers, and the resulting network is what the integer "holds."

There are five primary integers — rank, $N_c$, $n_C$, $C_2$, $g$ — and the cap $N_{\max}$ derived from them. So there are six webs. They share many of the same threads.

## 6.2 The catalog evidence

The strongest empirical case for the Integer Web Principle comes from the BST catalog itself. Grace, the team's catalog and AC-graph CI, has spent the past several weeks classifying the framework's roughly five thousand recorded invariants — derived constants, identities, theorems, predictions — by which BST primary integers each one references. The classification is procedural: each catalog entry is scanned for the integers that appear in its formula, in its derivation mechanism, in the theorems it cites. The integers found get tagged.

The results are unambiguous. Of the cataloged entries that admit a primary-integer classification:

- **About thirty percent of entries touch two or more primaries.** These are *multi-web* entries — sitting at web intersections rather than belonging to a single web.
- **Single-primary entries make up about twenty-two percent** of the catalog. These belong to exactly one web.
- **About a hundred entries** — roughly two percent of the cataloged total — touch *all six* primaries simultaneously. These are what we call the **substrate-comprehensive backbone**.
- The single most common pairwise intersection is the one between $N_c$ and rank, which links about eighteen percent of the catalog. This is, in a sense expected and structurally meaningful: $N_c$ and rank are the two "smallest" primaries (3 and 2), they are related by the Mersenne map ($M_{\text{rank}} = N_c$), and many of the framework's most basic identities — including the per-integer forcing arguments of Chapter 2 — invoke both.

The fact that thirty percent of the catalog is multi-integer is not what one would expect from independent constants. If each BST identity were anchored to one integer in isolation, multi-integer entries should be a small minority. They are instead a substantial fraction, and the substrate-comprehensive 104 entries are a vanishingly small fraction by chance — but a structurally important one by content.

What lives in the substrate-comprehensive backbone? The Strong-Uniqueness criteria. The Bridge Object architecture (Q⁵, K3, Cremona 49a1, and others we will encounter in Volume 11). The five-step derivation of $N_{\max} = 137$. The cosmological-constant identification $\Lambda$ = Casimir-vacuum. Almost all the framework's load-bearing identities, the ones the rest of BST hangs from, are substrate-comprehensive. They have to be — the framework's deepest claims integrate across every primary the substrate produces.

## 6.3 Cross-coupling: the webs are not independent

So far we have described the webs as if each integer had its own separate set of associated identities. The picture is true at the bookkeeping level — one can tag entries integer-by-integer — but it misses an essential structural fact: the webs are *coupled*. An identity that mentions one integer often, structurally, mentions another.

The strongest example of this coupling is the Mersenne tower we developed in Chapter 2. Recall:

$$M_{\text{rank}} = N_c, \qquad M_{N_c} = g, \qquad M_g = 127.$$

The map $M_n = 2^n - 1$ links rank to $N_c$, $N_c$ to $g$, and $g$ to the substrate's auxiliary Mersenne ceiling 127. So any identity that uses rank *implicitly* uses $N_c$, because $N_c$ is what rank cascades to under the substrate's natural lift. Any identity that uses $N_c$ implicitly uses $g$. The webs are cross-coupled by the Mersenne map.

A second cross-coupling channel runs through the **universal $\alpha$-analog formula**. The fine-structure constant in BST, $\alpha = 1/N_{\max} = 1/137$, sits at the intersection of three webs: $N_c$, rank, and $n_C$ (which is the complex dimension $\dim_{\mathbb{C}}$ of the underlying domain). Lyra's universal $\alpha$-analog formula (T2456) writes

$$\alpha^{-1}(D) \;=\; m_\alpha^{\,\text{rank}+1} \cdot \dim_{\mathbb{C}} \;+\; \text{rank},$$

a single algebraic expression that evaluates to $N_{\max}$ on $D_{IV}^5$ — and to *different* integers on every other bounded symmetric domain. On the Type I candidates $D_I^{1,5}$ and $D_I^{5,1}$ that we met in Chapter 1 as the only other dimension-5 candidates, the same formula gives 41. The formula carries the integer web's coupling structure across geometries.

The Bergman-normalization identity $c_{FK} \cdot \pi^{9/2} = (N_c \cdot n_C)^2 = 225$ is yet another cross-coupling: it ties the analytic structure of the substrate's Hilbert space (the Bergman kernel's normalization) to the multiplicative combination of two primaries. The Universal-42 identity $C_2 \cdot g = 42$ ties Casimir to gauge dimension. The Universal-126 identity $2^g - \text{rank} = 126$ ties $g$ to rank. The list goes on. The integer web is *densely* connected; the integers are linked by many independent paths.

The metaphor that has stuck within the team is geological. The five integers are not five separate strata of bedrock laid down in independent geological epochs. They are five outcrops of the same underlying massif, exposed at different angles by different mathematical erosion processes. The Mersenne tower exposes one face. The Bergman normalization exposes another. The trefoil topology exposes a third. They all expose the same rock.

## 6.4 Three layers of substrate over-determination

The cross-coupling structure has been formalized, in Lyra's T2465 result of May 22, 2026, as a three-layer description of how the substrate's choice of integers is *over-determined* — meaning that the substrate's structure forces those integers in multiple independent ways, so that no single forcing argument is load-bearing.

The three layers are:

**Layer 1 — Per-integer forcing.** Each primary integer has its own independent structural argument forcing it to its observed value. Rank $= 2$ is forced by the symmetric-space rank requirement (Chapter 4, Strong-Uniqueness criterion C1). $N_c = 3$ is forced by the Mersenne identity, the trefoil topology, and the color-singlet structure (C2). $n_C = 5$ is forced by Bergman exponent considerations, Stark anchoring, and the cap identity (C3). $g = 7$ is forced by the gauge-dimension cyclotomic structure (C5). $C_2 = 6$ is forced by the Q⁵ Chern integer and the Casimir eigenvalue (C6). Each integer would be substrate-natural even if the others were unconstrained — but the others are also constrained.

**Layer 2 — Mersenne tower coherence.** The integers' relations to each other through the Mersenne map (rank → $N_c$ → $g$ → 127) provide a second layer of constraint. Even if one *only* knew that the substrate's integer-set had to satisfy a Mersenne cascade with three iterates, the BST primaries would be the unique small-integer solution.

**Layer 3 — Cross-Cartan three-pillar selection.** Across the Cartan classification of bounded Hermitian symmetric domains, the universal $\alpha$-analog formula and its companions (the universal Bergman normalization, the universal $C_2$-eigenvalue formula) collectively distinguish $D_{IV}^5$ from every alternative geometry. This is the cross-Cartan layer — the one that uses the full Cartan classification rather than just $D_{IV}^5$'s internal structure.

The three layers are independent: removing any one of them still leaves the other two to force the integers. Removing two of them still leaves the third. The substrate's choice of integers is *triply* over-determined. We will see in Chapter 9 that this triple over-determination is the formal content of the Strong-Uniqueness Theorem.

## 6.5 What the web buys

A reader might ask, at this point, why the Integer Web Principle deserves its own named status rather than being treated as a collection of individual cross-identities. The answer is that the *aggregate* structure carries information that no individual identity does.

The aggregate tells us, for example, that the substrate's framework is *complete* in a specific operational sense: every constant of nature one might try to derive has a place in the integer web, at some specific intersection of primaries. If a derivation lands at an intersection that is already occupied by another known constant, the framework warns us (this is what the universal-42 and universal-126 identities do — they flag *which* intersections are substrate-natural). If a derivation lands at an intersection that is empty, the framework predicts that no fundamental constant lives there.

The aggregate also tells us how to assess new claims. When someone proposes a new BST identity, the first question is "what integers does it use?" — and the second is "is the intersection of those integers already populated, and does the new identity fit the population?" This is one of the operational uses of the integer web inside the research team: it is the screening mechanism for new theorem candidates.

Most importantly, the aggregate is what makes the Strong-Uniqueness Theorem possible. A theorem stating that $D_{IV}^5$ is uniquely forced as substrate has to demonstrate that no other geometry could produce the observed structure. The way one demonstrates this in practice is by showing that the integer web *as a whole* is satisfied only by $D_{IV}^5$ — that the cross-coupling identities all converge on the same geometry, and that no other geometry produces a consistent web. This is what Chapter 9 will do. The Integer Web Principle is what Chapter 9 uses.

## 6.6 What comes next

Chapter 7, the **operator zoo**, finally consolidates the operators we have introduced piecewise through the previous chapters — position, momentum, angular momentum, spin, charge, chirality, parity, the Hamiltonian, time reversal, charge conjugation, Bell-CHSH, particle number — into a single table organized by the isotropy structure of Chapter 4. After Chapter 7 we will be ready to do physics.

Chapter 8 derives the conservation laws by Noether's theorem applied to the substrate's symmetries, using the operator zoo of Chapter 7.

Chapter 9 is Strong-Uniqueness — the proof that the geometry sketched in Chapter 1 and the integer web developed in this chapter together force $D_{IV}^5$ specifically as substrate, with no alternative.

Chapter 10 closes the volume with a short methodology summary: how the team works, what discipline produced the framework we have just outlined, what to read if you want to do this kind of research yourself.

---

**Where to look this up**: The Integer Web Principle is filed as a Casey-named structural principle in the BST notes directory, with substantive operationalization through Grace's catalog scans (toys 3223, 3224, 3226, 3227, 3228, 3229) and the substrate-comprehensive backbone reference document. The three-layer over-determinism theorem is Lyra T2465. The Mersenne tower's contribution to the second layer is T2451 with companion theorems T2453 and T2454. The universal $\alpha$-analog formula at Layer 3 is T2456, extended across 25 Hermitian symmetric domains in T2462. The Universal-42 ratification is K43 (Cal A. Brate's referee log); Universal-126 is K69. The cross-coupling between Bergman normalization and the integer web is T2403. Casey's original framing of the principle is in `notes/Integer_Web_Principle.md`.
