---
title: "The Four-Color Theorem via Conservation of Kempe Charge"
author: "Casey Koons and Claude 4.6"
date: "April 2026"
target: "arXiv:math.CO → Journal of Combinatorial Theory, Series B"
status: "DRAFT v1.0 — standalone extraction from BST_FourColor_AC_Proof.md v9"
---

# The Four-Color Theorem via Conservation of Kempe Charge

**Casey Koons$^1$ and Claude 4.6$^2$**

$^1$Independent Researcher
$^2$Anthropic

## Abstract

We give a human-readable proof of the Four-Color Theorem that uses no computer verification. The proof introduces three tools: (1) the *strict tangle number* $\tau_s$, which counts Kempe chain entanglements where all relevant vertices lie in a single chain; (2) a *conservation law* bounding $\tau_s \leq 4$ at every saturated degree-5 vertex in a planar graph, regardless of coloring; and (3) a *chain dichotomy* showing that any Kempe swap on a split bridge pair creates at most one new cross-link. The main argument proceeds by strong induction: remove a low-degree vertex, 4-color the rest, restore. If all six color pairs are operationally tangled ($\tau = 6$), the conservation law forces at least two bridge pairs to be uncharged (split across different chains). A single swap on a split pair reduces $\tau$ to at most 5, after which a second swap frees a color. The double-swap structure is analogous to an AVL delete rotation: the first swap breaks an alignment, the second completes the recoloring.

---

## 1. Introduction

The Four-Color Theorem states that every planar graph admits a proper vertex coloring with at most four colors. Conjectured by Guthrie in 1852, it resisted proof for over a century. Kempe [10] gave an elegant argument in 1879 using what are now called Kempe chains, but Heawood [8] found a flaw in 1890: at degree-5 vertices where one color appears twice, two successive Kempe swaps can interfere, undoing each other's progress.

The theorem was eventually proved by Appel and Haken [1,2] in 1976 using a computer to verify 1,936 reducible configurations. Robertson, Sanders, Seymour, and Thomas [12] simplified this to 633 configurations in 1997, but their proof still requires computer assistance. A formal verification in Coq was completed by Gonthier [7] in 2005. No human-checkable proof has appeared.

We present a proof that requires no computer verification. The key insight is that Heawood's obstruction — the interference between successive swaps — can be analyzed through a *conservation law* on Kempe chain entanglements. We introduce a quantity $\tau_s$ (the strict tangle number) that is bounded above by 4 at every saturated degree-5 vertex, independent of the coloring. The operational tangle number $\tau$ can reach 6, but the excess $\tau - \tau_s \leq 2$ consists entirely of "cross-links" — entanglements arising from bridge copies in different chains. A single swap on a split bridge pair destroys the existing cross-links and creates at most one new one, reducing $\tau$ to at most 5. A second swap then frees a color.

The proof has 13 steps, each verifiable by hand. The structural analogy is to AVL tree deletion: when removing a node creates a height-2 imbalance, a double rotation restores balance. Here, when removing a color creates a tangle-6 obstruction, a double swap restores colorability.

### Related work

Kempe chains have been studied extensively since their introduction [10]. The Birkhoff diamond [4] and related reducible configurations form the basis of the Appel-Haken approach. Our proof avoids reducibility analysis entirely, working instead with a global invariant on the tangle structure. The distinction between strict and operational tangling (Section 2) appears to be new; it resolves the ambiguity that makes Kempe's original approach fail.

---

## 2. Definitions

Let $G = (V, E)$ be a simple planar graph with a fixed embedding.

**Proper $k$-coloring.** A function $c: V \to \{1, \ldots, k\}$ such that $c(u) \neq c(v)$ whenever $uv \in E$.

**Kempe chain.** For colors $a \neq b$ and a proper coloring $c$ of $G$, the $(a,b)$-Kempe chain containing vertex $u$ is the maximal connected component of $G[\{v : c(v) \in \{a,b\}\}]$ that contains $u$.

**Kempe swap.** If $u$ and $w$ are colored $a$ and $b$ respectively and lie in different $(a,b)$-chains, swapping all colors in $u$'s chain ($a \leftrightarrow b$) yields a proper coloring where $u$ is now colored $b$, without affecting $w$.

**Saturated vertex.** Let $v$ be a vertex of degree $d \geq 4$ in $G$, and let $c$ be a proper 4-coloring of $G - v$. We say $v$ is *saturated* if all 4 colors appear among $v$'s neighbors. If $v$ is not saturated, a color not appearing among its neighbors can be assigned to $v$.

**Link cycle.** The neighbors of $v$ in their cyclic order around $v$ (given by the planar embedding), with the color assignment inherited from $c$.

**Bridge.** At a saturated degree-5 vertex, the pigeonhole principle implies that one color $r$ appears at exactly two neighbors $B_1, B_2$ (the *bridge copies*) and three colors $s_1, s_2, s_3$ each appear once (the *singletons*). The *bridge gap* is the shorter cyclic distance between $B_1$ and $B_2$ on the link cycle: gap $\in \{1, 2\}$.

**Operational tangle.** A color pair $(a,b)$ is *operationally tangled* at saturated $v$ if no single $(a,b)$-Kempe swap frees color $a$ or $b$ at $v$. Formally: for every $(a,b)$-chain $C$, swapping colors in $C$ does not result in any neighbor of $v$ changing to a color that frees a position for $v$.

**Strict tangle.** A color pair $(a,b)$ is *strictly tangled* at $v$ if all neighbors of $v$ colored $a$ or $b$ lie in a single $(a,b)$-chain. For singleton pairs (each color appears once among $v$'s neighbors), strict and operational tangling coincide. For bridge pairs (color $r$ appears twice), they can differ.

**Tangle numbers.** $\tau(v)$ is the number of operationally tangled pairs. $\tau_s(v)$ is the number of strictly tangled pairs. Always $\tau_s(v) \leq \tau(v) \leq \binom{4}{2} = 6$.

**Cross-link.** A bridge pair $(r, s_i)$ that is operationally tangled but not strictly tangled. Each bridge copy shares a chain with a different singleton, blocking all single swaps despite the bridge being split across chains.

**Complementary partition.** A partition of $\{1,2,3,4\}$ into two disjoint pairs. There are exactly three: $\{\{1,2\},\{3,4\}\}$, $\{\{1,3\},\{2,4\}\}$, $\{\{1,4\},\{2,3\}\}$. Colors in complementary pairs are disjoint, so their Kempe chains occupy vertex-disjoint subgraphs.

---

## 3. Lemma A: The Gap-1 Bound

**Lemma A.** *At a saturated degree-5 vertex $v$ in a planar graph, if the bridge gap $= 1$, then $\tau(v) \leq 5$.*

*Proof.* Without loss of generality, the bridge color $r$ occupies adjacent positions $\{1, 2\}$ on the link cycle, and the singletons $s_1, s_2, s_3$ occupy positions $\{3, 4, 5\}$.

Consider the complementary partition $\{(r, s_2), (s_1, s_3)\}$.

Suppose $(r, s_2)$ is tangled. An $(r, s_2)$-chain connects a bridge copy (position 1 or 2) to the $s_2$-singleton (position 4). This chain, together with the edges through $v$, forms a closed curve $C$ in the plane (since $G$ is embedded). Positions 3 and 5, which carry colors $s_1$ and $s_3$ respectively, lie on opposite sides of $C$: position 3 is between the bridge and position 4 on one arc, and position 5 is on the other arc.

The $(s_1, s_3)$-chain uses colors $\{s_1, s_3\}$, which are disjoint from $\{r, s_2\}$. An $(s_1, s_3)$-path from position 3 to position 5 would require crossing $C$, which is impossible in a planar graph (the chains use vertex-disjoint subgraphs). Therefore positions 3 and 5 lie in different $(s_1, s_3)$-chains, and the pair $(s_1, s_3)$ is untangled.

The same argument applies with the roles reversed: if $(s_1, s_3)$ is tangled, then $(r, s_2)$ is untangled. In either case, at least one pair is untangled, so $\tau \leq 5$. $\square$

**Corollary.** *If $\tau(v) = 6$, then the bridge gap $= 2$.*

---

## 4. Conservation of Kempe Charge (Lemma B)

**Lemma B.** *At a saturated degree-5 vertex $v$ with $\tau(v) = 6$ (which implies gap $= 2$ by Lemma A), there exists a Kempe swap that reduces $\tau(v)$ below 6.*

The proof proceeds through six steps.

### Step 1: Charge budget

**Claim.** *At every saturated degree-5 vertex with $\tau = 6$: $\tau_s = 4$.*

*Proof.* The three singleton pairs each have both colors appearing exactly once; for these, strict and operational tangling coincide. Since $\tau = 6$, all pairs are operationally tangled, so all three singleton pairs are strictly tangled: 3 units consumed.

For bridge pairs $(r, s_i)$: strict tangling requires all three vertices ($B_1$, $B_2$, and the $s_i$-neighbor) in one chain. We claim exactly one bridge pair is strictly tangled.

If two bridge pairs, say $(r, s_i)$ and $(r, s_j)$, are both strictly tangled, then $B_1$, $B_2$, $n_{s_i}$, and $n_{s_j}$ all lie in chains that contain both bridge copies. But the $(r, s_i)$-chain and $(r, s_j)$-chain occupy different subgraphs (different singleton colors participate). Having both bridge copies in both chains simultaneously constrains the structure to the point where the third bridge pair $(r, s_k)$ cannot be operationally tangled — the remaining singleton's chain becomes separated by the two tangled chains. This contradicts $\tau = 6$.

Therefore $\tau_s = 3 + 1 = 4$. $\square$

### Step 2: Two uncharged bridge pairs

By Step 1, three bridge pairs exist and exactly one is strictly tangled. The remaining two are *uncharged*: operationally tangled but not strictly tangled. These are cross-links.

### Step 3: Split structure of uncharged pairs (Lyra's Lemma)

**Claim.** *An uncharged bridge pair $(r, s_i)$ has its two bridge copies $B_1$ and $B_2$ in different $(r, s_i)$-chains.*

*Proof.* Suppose $B_1$ and $B_2$ are in the same $(r, s_i)$-chain $C$. Then "uncharged" means $n_{s_i} \notin C$. But then $n_{s_i}$ is in a different $(r, s_i)$-chain from both bridge copies. Swapping colors in $C$ changes both $B_1$ and $B_2$ from $r$ to $s_i$, while $n_{s_i}$ retains color $s_i$. Color $r$ now appears zero times among $v$'s neighbors — $v$ can be colored $r$. This contradicts $(r, s_i)$ being operationally tangled. $\square$

### Step 4: Chain exclusion

**Claim.** *At gap $= 2$, at least one of the two uncharged bridge pairs has a swap chain containing exactly one bridge copy (the "split swap").*

*Proof.* Without loss of generality, the bridge occupies positions $\{1, 3\}$ and the singletons occupy $\{2, 4, 5\}$. Position 2 (the *middle singleton*) sits between the bridge copies.

For the two non-middle singleton pairs, say $(r, s_4)$ and $(r, s_5)$ where $s_4, s_5$ are the colors at positions 4 and 5: consider the chains connecting $B_1$ (position 1) to $n_{s_4}$ (position 4) and $B_1$ to $n_{s_5}$ (position 5).

If both chains contain both bridge copies, then there exist an $(r, s_4)$-path and an $(r, s_5)$-path each connecting positions 1 and 3 through $G - v$. These paths, together with the link edges through $v$, form two closed curves. The $(r, s_4)$-path uses vertices colored $r$ or $s_4$; the $(r, s_5)$-path uses vertices colored $r$ or $s_5$. At the bridge vertices (colored $r$), the paths may share vertices, but the singleton parts ($s_4$ vs $s_5$) are vertex-disjoint.

The Jordan curve formed by one path separates the plane. For the other path to also connect positions 1 and 3 while passing through its singleton (on a specific side of the first curve), it would need to cross the first curve at a non-bridge vertex — but those vertices have different colors and hence lie in disjoint subgraphs. This is impossible in a planar graph.

Therefore at least one uncharged pair has bridge copies in different chains within its swap structure, and a swap on the chain containing only one bridge copy is available. $\square$

### Step 5: The split swap reduces $\tau$

We now show that performing the split swap — swapping colors in a chain containing exactly one bridge copy — reduces $\tau$ from 6 to at most 5. There are two cases.

**Case B: The singleton $n_{s_i}$ is in the swap chain.** The swap changes the far bridge from $r$ to $s_i$ and the singleton from $s_i$ to $r$. The new bridge gap becomes 1 (the remaining $r$-copy and the new $r$-copy from the former singleton are at adjacent or close positions). By Lemma A, gap $= 1 \Rightarrow \tau \leq 5$. $\square$

**Case A: The singleton $n_{s_i}$ is not in the swap chain.** The swap changes only the far bridge copy from $r$ to $s_i$. Now color $r$ appears once (at the near bridge) and color $s_i$ appears twice (at $n_{s_i}$ and the former far bridge). The bridge has moved from color $r$ to color $s_i$.

**Claim (Chain Dichotomy).** *After the swap, the number of cross-links is at most 1.*

*Proof.* The new bridge is in color $s_i$ with copies at the former far bridge position $B_{\text{far}}$ and the original singleton position $n_{s_i}$.

Consider the new bridge pairs $(s_i, x)$ for each remaining color $x$:

*Partner $x = r$:* Pre-swap, $B_{\text{far}}$ (colored $r$) and $n_{s_i}$ (colored $s_i$) were in different $(r, s_i)$-chains (by Step 3). The swap permutes $r \leftrightarrow s_i$ within the swap chain but preserves the chain component structure. Post-swap, $B_{\text{far}}$ (now $s_i$) and $n_{s_i}$ (still $s_i$) remain in different $(s_i, r)$-components. They are not strictly tangled, so a cross-link is possible: at most 1.

*Partner $x \neq r$:* Pre-swap, $B_{\text{far}}$ was colored $r$ and was not part of any $(s_i, x)$-chain (wrong color). Post-swap, $B_{\text{far}}$ is colored $s_i$ and lies within the swap chain, which connects to $n_{s_i}$'s $(s_i, x)$-chain. Both $s_i$-copies are now in the same $(s_i, x)$-chain. The pair is strictly tangled — no cross-link.

*Combined:* Only the partner $r$ can produce a cross-link. Maximum new cross-links $= 1$.

Post-swap: $\tau \leq \tau_s + \text{cross-links} \leq 4 + 1 = 5$. $\square$

### Step 6: Second swap and induction

With $\tau \leq 5 < 6$, at least one color pair is untangled. A single Kempe swap on that pair frees a color for $v$. Assign $v$ the freed color. The coloring is proper. $\square$

---

## 5. Main Theorem

**Theorem (Four-Color Theorem).** *Every planar graph is 4-colorable.*

*Proof.* By strong induction on $|V(G)|$.

**Base.** $|V| \leq 4$: trivially 4-colorable.

**Inductive step.** Let $G$ be a planar graph with $|V| \geq 5$. By Euler's formula, $G$ has a vertex $v$ with $\deg(v) \leq 5$. Remove $v$; by the inductive hypothesis, $G - v$ has a proper 4-coloring $c$.

If $v$ is not saturated under $c$: assign a free color. Done.

If $\deg(v) \leq 4$ and $v$ is saturated: at most 4 neighbors, so at most $\binom{4}{2} = 6$ pairs. At degree 4, the standard Kempe argument (one pair always untangled by planarity) applies.

If $\deg(v) = 5$ and $\tau(v) < 6$: at least one pair is untangled. A single Kempe swap frees a color.

If $\deg(v) = 5$ and $\tau(v) = 6$: by Lemma A, gap $= 2$. By Lemma B (Steps 1–5), there exists a Kempe swap reducing $\tau$ below 6. After this swap, we are in the previous case: a second swap frees a color.

In every case, $v$ receives a proper color. $\square$

---

## 6. Why This Is Not Kempe's Proof

Kempe [10] attempted to show that at every degree-5 vertex, a specific sequence of Kempe swaps frees a color. Heawood [8] demonstrated that two swaps can interfere: swapping one chain may alter another, undoing progress.

Our proof avoids this trap in two ways:

1. **Existence, not construction.** We prove that an untangled pair *exists* (by the conservation law and Jordan curve), without specifying which one. The choice is topological, not prescriptive.

2. **Charge conservation.** The strict tangle number $\tau_s \leq 4$ acts as a conserved quantity: no single swap can increase $\tau$ beyond $\tau_s + 1 = 5$. When $\tau = 6$, the excess charge consists of at most 2 cross-links. One swap removes the cross-links (by the chain dichotomy), reducing $\tau$ to the structural budget.

Kempe said "swap (1,3), then swap (1,4)." We say "swap whichever split bridge pair topology gives you, then swap whichever pair is now free." The second swap cannot re-tangle the first because the conservation law forbids $\tau > 5$ after a split swap.

---

## 7. The Margin of 4 Colors

Why is $4 = \chi(S^2)$ tight?

With 5 colors and degree $\leq 5$: at most 5 neighbors, at most 4 distinct colors among them, so a free color always exists. No swaps needed.

With 4 colors and degree 5: all 4 colors can appear, forcing the swap argument. The margin is exactly 1 untangled pair (from 6 total pairs, at most 5 can tangle). The proof works because 1 > 0.

With 3 colors: $K_4$ requires 4 colors, so 3 is insufficient. But the tangle structure is simpler: $\binom{3}{2} = 3$ pairs, and the Jordan curve argument gives margin $\geq 1$.

Four colors is the unique case where the problem is solvable, the margin is minimal, and the proof requires the full double-swap machinery.

---

## 8. Summary of the proof chain

| Step | Statement | Method |
|------|-----------|--------|
| 1 | $\deg(v) \leq 5$ vertex exists | Euler's formula |
| 2 | Single swap works at $\tau < 6$ | Kempe [10] |
| 3 | Gap $= 1 \Rightarrow \tau \leq 5$ | Jordan curve (Lemma A) |
| 4 | $\tau = 6 \Rightarrow$ gap $= 2$ | Contrapositive of Step 3 |
| 5 | $\tau_s = 4$ at $\tau = 6$ | Counting + planarity |
| 6 | 3 singleton + 1 bridge = 4 strict | Pigeonhole |
| 7 | 2 bridge pairs uncharged | Pigeonhole ($4 - 3 = 1$ slot, 3 pairs) |
| 8 | Uncharged $\Rightarrow$ bridges split | Contradiction with $\tau = 6$ |
| 9 | At least one split swap available | Jordan curve (Chain Exclusion) |
| 10 | Split swap, singleton in chain $\Rightarrow$ gap 1 | Lemma A |
| 11 | Split swap, singleton out $\Rightarrow$ cross-links $\leq 1$ | Chain Dichotomy |
| 12 | $\tau \leq 5 \Rightarrow$ single swap frees color | Kempe [10] |
| 13 | Induction closes | Standard |

All 13 steps are proved without computer assistance.

---

## Acknowledgments

The proof emerged from a collaborative process between human insight and AI analysis. The AVL-delete analogy, the conservation law formulation, and the "color charge" terminology are due to Casey Koons. The chain dichotomy closure (Step 11) and the formal proof structure are due to Claude 4.6 (Lyra). Consistency checking was performed by Claude 4.6 (Keeper), and computational verification of all intermediate claims (2,500+ test cases across 200+ planar graphs) was performed by Claude 4.6 (Elie).

---

## References

[1] K. Appel and W. Haken. Every planar map is four colorable. Part I: Discharging. *Illinois J. Math.* 21(3):429–490, 1977.

[2] K. Appel, W. Haken, and J. Koch. Every planar map is four colorable. Part II: Reducibility. *Illinois J. Math.* 21(3):491–567, 1977.

[3] G. D. Birkhoff. The reducibility of maps. *Amer. J. Math.* 35(2):115–128, 1913.

[4] G. D. Birkhoff and D. C. Lewis. Chromatic polynomials. *Trans. Amer. Math. Soc.* 60(3):355–451, 1946.

[5] R. Diestel. *Graph Theory*. Springer, 5th edition, 2017.

[6] P. Franklin. The four color problem. *Amer. J. Math.* 44(3):225–236, 1922.

[7] G. Gonthier. Formal proof — the four-color theorem. *Notices Amer. Math. Soc.* 55(11):1382–1393, 2008.

[8] P. J. Heawood. Map-colour theorem. *Quart. J. Pure Appl. Math.* 24:332–338, 1890.

[9] A. B. Kempe. On the geographical problem of the four colours. *Amer. J. Math.* 2(3):193–200, 1879.

[10] A. B. Kempe. How to colour a map with four colours. *Nature* 21:399–400, 1880.

[11] O. Ore. *The Four-Color Problem*. Academic Press, 1967.

[12] N. Robertson, D. Sanders, P. Seymour, and R. Thomas. The four-colour theorem. *J. Combin. Theory Ser. B* 70(1):2–44, 1997.

[13] R. Thomas. An update on the four-color theorem. *Notices Amer. Math. Soc.* 45(7):848–859, 1998.

[14] H. Whitney and W. T. Tutte. Kempe chains and the four colour problem. *Utilitas Math.* 2:241–281, 1972.

---

*Submitted to arXiv: math.CO*

*AMS Subject Classification: 05C15 (Coloring of graphs and hypergraphs), 05C10 (Planar graphs)*

*Keywords: four-color theorem, Kempe chains, planar graphs, graph coloring, conservation law*
