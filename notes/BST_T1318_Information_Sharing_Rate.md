# T1318 -- Information Sharing Rate Between Observers

*The maximum rate at which two observers can share knowledge is bounded by the Bergman kernel overlap. For observers at "distance" d on D_IV^5, the mutual information rate is I(A;B) = f_c² · (1 - d²/d_max²) · R_max, where R_max = n_C · ln 2 bits per interaction. At zero distance (identical observers), sharing is f_c² ≈ 3.65% of total bandwidth — the Gödel cost of self-knowledge limiting what can be communicated. At maximum distance (orthogonal observers), sharing drops to zero. The optimal sharing distance is d* = d_max/√2, giving I* = f_c²/2 · R_max.*

**AC**: (C=1, D=0). One computation (Bergman kernel evaluation). Zero self-reference.

**Authors**: Lyra (derivation), Casey Koons (Bergman overlap insight).

**Date**: April 18, 2026.

**Domain**: cooperation_science.

---

## Statement

**Theorem (T1318, Information Sharing Rate).** *For two observers A, B on D_IV^5:*

1. *Each observer accesses f_c = N_c/(n_Cπ) ≈ 19.1% of the total information (T318).*
2. *The overlap of their accessible regions is governed by the Bergman reproducing kernel K(z,w):*

        I(A;B) = |K(z_A, z_B)|² / [K(z_A, z_A) · K(z_B, z_B)]

    *This is the normalized Bergman kernel squared — the coherence function between observer positions.*

3. *The maximum is I(A;A) = 1 (self-coherence). The minimum is I(A;B_⊥) = 0 (orthogonal observers).*
4. *For cooperation to be effective, I(A;B) must exceed the noise floor:*

        I(A;B) > 1/N_max = 1/137

    *This defines the cooperation radius: observers separated by more than d_coop in the Bergman metric cannot cooperate effectively.*

5. *The information sharing rate in bits per interaction:*

        R(A;B) = I(A;B) · f_c · n_C · ln 2

    *Each interaction shares f_c of the n_C dimensions, each carrying 1 bit, weighted by the coherence I(A;B).*

---

## Derivation

### Step 1: Observer overlap geometry

Two observers A and B on D_IV^5 each occupy a position (z_A, z_B) in the bounded symmetric domain. The Bergman kernel K(z,w) is the reproducing kernel for holomorphic functions on D_IV^5. It measures how much information at position z is "visible" from position w.

The normalized kernel:

    k(z,w) = |K(z,w)|² / [K(z,z) · K(w,w)]

is the coherence between positions. It satisfies:
- k(z,z) = 1 (perfect self-coherence)
- 0 ≤ k(z,w) ≤ 1 (bounded)
- k(z,w) = k(w,z) (symmetric)

This is exactly the mutual information kernel for observer pairs.

### Step 2: The sharing formula

Observer A can express f_c of its own state. Observer B can receive f_c of what A expresses. The net transfer per interaction:

    bits_transferred = f_c(express) · f_c(receive) · k(z_A, z_B) · H_total

where H_total = n_C · ln 2 (total information content = one bit per matter dimension).

The rate:

    R(A;B) = f_c² · k(z_A, z_B) · n_C · ln 2

### Step 3: Self-sharing limit

Even at k = 1 (identical observers), the sharing rate is f_c² ≈ 3.65% of total bandwidth. This is the Gödel cost squared: each observer can only express 19.1% of itself, and the receiver can only absorb 19.1% of what's expressed.

This predicts: even perfect communication between identical minds transfers ≈ 3.65% of total information per interaction. To reach 50% transfer requires ≈ ln(2)/f_c² ≈ 19 interactions. To reach 90% requires ≈ ln(10)/f_c² ≈ 63 interactions.

### Step 4: Optimal cooperation distance

The cooperation benefit C(d) minus coordination cost K(d):

    Net(d) = C(d) - K(d) = [f_c² · k(d) · R_max] - [c_pair · (1 - k(d))]

where c_pair is the pairwise coordination cost from T1316.

Maximizing: dNet/dd = 0 gives d* where the marginal benefit of new information equals the marginal cost of coordination. For the Bergman metric on D_IV^5 (where k(d) ≈ 1 - d²/d_max² for small d):

    d* = d_max · √(f_c² · R_max / (f_c² · R_max + c_pair))

In the symmetric case (R_max = c_pair): d* = d_max/√2. Observers cooperate best at intermediate distance — close enough to share but different enough to contribute new information.

### Step 5: The cooperation radius

The minimum useful sharing rate is 1/N_max = 1/137 (one bit per spectral cap). Setting R(A;B) ≥ R_max/N_max:

    f_c² · k(d) ≥ 1/N_max
    k(d) ≥ 1/(f_c² · N_max) = 1/(0.0365 · 137) ≈ 0.200

So observers cooperate effectively when their coherence exceeds ≈ 20% — which is itself approximately f_c. The cooperation radius is the Bergman distance where coherence drops to f_c.

This means: the Gödel limit controls both how much each observer can know (f_c) AND how far apart observers can usefully cooperate (coherence ≥ f_c).

---

## Cross-Domain Bridges

| Target Domain | Bridge | Through |
|:-------------|:-------|:--------|
| information_theory | Sharing rate = f_c² · coherence · capacity | Shannon channel capacity |
| observer_science | Each observer limited by Gödel | T318 |
| biology | Neural synchrony rates ∝ coherence | T1005 (biological networks) |
| coding_theory | Cooperation radius from code distance | T1238 (Hamming perfection) |

---

## For Everyone

When two people try to communicate, each can only express about 19% of what they know (that's the Gödel limit — you can't fully describe yourself). And the other person can only absorb 19% of what you express. So each conversation transfers about 19% × 19% = 3.6% of the total information.

That's why understanding takes time. It takes about 19 deep conversations to transfer half of what you know to someone else. About 63 conversations for 90%.

And there's an optimal distance: talk to someone too similar and you learn nothing new. Talk to someone too different and you can't understand each other. The sweet spot is in between — different enough to have new information, similar enough to share it.

This is why diverse teams outperform homogeneous ones — up to a point. The magic number for team size (6, from T1316) puts each pair at roughly the optimal sharing distance.

---

## Parents

- T318 (Gödel Limit — f_c = 19.1%)
- T1316 (Optimal Group Size = C₂ = 6)
- T1172 (Cooperation IS Compression)
- T186 (Bergman kernel master theorem)
- T1111 (Cooperation Theorem)

## Children

- Language efficiency as information channel optimization
- Teaching as directed Bergman overlap maximization
- Consensus formation rates
- Economic trade as information exchange

---

*T1318. AC = (C=1, D=0). Information sharing rate = f_c² · coherence · n_C ln 2 bits/interaction. Self-sharing capped at 3.65%. Cooperation radius where coherence ≥ f_c. Optimal distance d* = d_max/√2. Domain: cooperation_science. Lyra derivation. April 18, 2026.*
