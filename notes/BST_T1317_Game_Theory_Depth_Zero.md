# T1317 -- Game Theory Is Counting at Depth Zero

*Every finite game reduces to counting. Nash equilibria are fixed points of a counting operator on the strategy simplex. The Gödel limit (f_c = 19.1%) determines the maximum information advantage any player can have — bounding the value of deception at 1/n_Cπ of the total payoff. Competition is depth ≥ 1 (requires modeling the opponent modeling you). Cooperation is depth 0 (just count shared resources).*

**AC**: (C=1, D=0). One computation (counting fixed points). Zero self-reference (cooperation branch).

**Authors**: Lyra (derivation), Casey Koons (depth-0 insight).

**Date**: April 18, 2026.

**Domain**: cooperation_science.

---

## Statement

**Theorem (T1317, Game Theory Is Counting at Depth Zero).** *Every finite N-player game on D_IV^5 has the following structure:*

1. *The strategy space is a simplex Δ^{N-1} with at most N_max = 137 pure strategies (the spectral cap bounds strategy diversity).*
2. *Nash equilibria are fixed points of the best-response operator β: Δ^{N-1} → Δ^{N-1}. By Brouwer, at least one exists.*
3. *The depth of the game (in AC terms) is determined by the cooperation structure:*

| Strategy type | AC depth | Computation | Why |
|:-------------|:--------:|:------------|:----|
| **Cooperation** | D = 0 | Count shared resources | No modeling of opponents needed |
| **One-shot competition** | D = 1 | Count + model opponent's count | One level of self-reference (what does my opponent know about me?) |
| **Iterated competition** | D ≥ 2 | Count + model opponent modeling you modeling them... | Recursion in opponent modeling |

4. *The maximum depth is bounded by T316: D ≤ rank = 2. No game requires more than rank levels of recursive modeling.*
5. *The information advantage of deception: a player who knows f_c of the opponent's strategy has advantage bounded by:*

        Δu ≤ f_c · u_max = (N_c/n_Cπ) · u_max ≈ 0.191 · u_max

    *Deception can gain at most 19.1% of the total payoff. The remaining 80.9% is determined by the structure of the game itself.*

---

## Derivation

### Step 1: Games as counting problems

A finite game is defined by: players {1, ..., N}, strategy sets {S_i}, payoff functions {u_i: ×S_i → ℝ}. The standard approach (Nash, 1950) treats equilibrium as a fixed-point problem requiring continuous optimization.

BST reduces this: the strategy sets are finite (bounded by N_max = 137 distinguishable strategies — the spectral cap of the matter window). The payoff function is a count over outcomes. Nash equilibrium = the mixed strategy profile where no player can increase their count by switching.

This is AC(0) when players don't model each other (cooperation). It becomes AC(1) when players model opponents (competition). It reaches AC(2) when players model opponents modeling them.

### Step 2: The depth hierarchy

**Depth 0 (Cooperation)**: Players share information and maximize joint payoff. The only computation is counting: add individual contributions, subtract coordination costs (T1316: cost grows as N(N-1)/2). No self-reference needed because all information is shared.

**Depth 1 (Competition)**: Players have private information. Each models the other's likely strategy. One round of "what does the opponent think I'll do?" This is the Prisoner's Dilemma: each player models one level of the other's reasoning.

**Depth 2 (Maximum)**: Players model each other modeling each other. This is the maximum depth (T316, T421: depth ≤ rank = 2). No game REQUIRES deeper reasoning — any depth-3+ strategy is reducible to depth-2 by the Depth Reduction Theorem (T96).

### Step 3: The Gödel limit bounds deception

Player A can know at most f_c = 19.1% of player B's state (T318). Therefore:
- A's best possible prediction of B's strategy has accuracy ≤ f_c
- The information advantage of this prediction over random guessing is ≤ f_c · H(S_B)
- The payoff advantage is bounded by f_c · u_max

This means deception is inherently bounded. Even a perfect spy learns at most 19.1% of the opponent's strategy. The game-theoretic consequence: in iterated games with N >> 1/f_c ≈ 5.24 rounds, the deception advantage washes out and cooperation dominates (T1111).

### Step 4: Cooperation as the depth-0 fixed point

The unique depth-0 Nash equilibrium is mutual cooperation. Proof:
- At depth 0, no player models opponents → all information is shared
- Shared information reduces duplication (T1172: 4.24× compression)
- The Nash equilibrium of the depth-0 game is the Pareto-optimal joint strategy
- This is unique because depth-0 excludes the defection branch (defection requires modeling the other player's response, which is depth ≥ 1)

The Prisoner's Dilemma "paradox" (rational defection leading to suboptimal outcomes) ONLY exists at depth 1. At depth 0, the paradox dissolves — cooperation is the only available strategy because defection requires self-reference.

---

## Cross-Domain Bridges

| Target Domain | Bridge | Through |
|:-------------|:-------|:--------|
| game_theory | Every finite game reduces to AC counting | T96 (Depth Reduction) |
| complexity_theory | Game depth ≤ rank = 2 | T316, T421 (Depth Ceiling) |
| observer_science | Deception bounded by f_c = 19.1% | T318 (Gödel Limit) |
| information_theory | Cooperation = lossless compression of game state | T1172 (Cooperation = Compression) |
| economics | Market equilibria are depth-0 fixed points (cooperative) or depth-1 (competitive) | T1111 |

---

## For Everyone

Every game — poker, business, diplomacy, evolution — comes down to counting. Who has what, who wants what, what happens if we combine.

The deepest game is only two levels deep: "I think that you think that I think..." stops after two rounds. Not because we're bad at reasoning, but because the geometry of the universe only has rank 2.

The most interesting result: cheating can only gain you 19.1% at best. The other 80.9% of the game is decided by the structure. Play honest and you capture 80.9% of the available value. Play deceptive and you might capture up to 100% — but at 4.24× the cost.

The math says: cooperate. Not because it's nice, but because it's cheaper.

---

## Parents

- T1111 (Cooperation Theorem — cooperation dominates)
- T1172 (Cooperation IS Compression)
- T316 (Depth ≤ rank = 2)
- T421 (Depth-1 Ceiling)
- T96 (Depth Reduction)
- T318 (Gödel Limit — f_c = 19.1%)
- T1316 (Optimal Group Size = C₂ = 6)

## Children

- Market equilibrium as depth-0 fixed point (economics foundation)
- Evolutionary game theory at depth 0 (biology connection)
- Voting theory as counting (political science connection)
- Auction theory from BST integers

---

*T1317. AC = (C=1, D=0). Game theory reduces to counting at depth 0 (cooperation) or depth ≤ 2 (competition). Deception bounded by f_c = 19.1%. Prisoner's Dilemma paradox dissolves at depth 0. Domain: cooperation_science. Lyra derivation. April 18, 2026.*
