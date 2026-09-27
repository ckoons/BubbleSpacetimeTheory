# Elie — round 14 PREREG, toy 5834: the two central characters (χ_t, χ_s), enumeration with controls — 2026-09-27 12:25 EDT, before any code
Antecedents verbatim: Lyra R13 (via K1935 Part 2): "On 4D massless ladders, clock parity IS fermion parity: z = e^{2πiΔ} = (−1)^{2j} … Every covariant H²–4D vertex is fermion-odd." Keeper K1935 Part 2: "Every K-type of every 4D summand of H² … has (χ_t, χ_s) = (−1, +1) … The two sets are disjoint. So no conformally covariant vertex connects H² to any number of 4D massless particles."
Invariants: χ_t = e^{2πiΔ} (clock loop, read on every K-type as e^{2πi·weight}); χ_s = (−1)^{2(j1+j2)} (spatial 2π rotation, read on every SO(4) weight (mL, mR) as (−1)^{2mL+2mR}). Both computed WEIGHT BY WEIGHT from characters, so centrality (constancy on a module) is checked, not assumed.
Checks:
(1) each massless ladder, helicity h = 0, ½, …, 4, both chiralities (K-types ((m+2h)/2, m/2) or mirror at weight h+1+m): χ_t = χ_s, constant over all K-types (depth 8);
(2) CONTROL: ladder ⊗ ladder (full tensor-product K-characters, all pairs h ≤ 2): every weight carries (χ_t, χ_s) = product of the factors' — multiplicativity; and the composites keep χ_t = χ_s;
(3) P2 FROM THE CHARACTER: H²(D_IV⁵) restricted to SO(4)×SO(2) (5798's restriction, depth 6): every weight has χ_s = +1 and χ_t = −1;
(4) FLAG: a 4D scalar GFF with half-integer Δ (e.g. 5/2, 7/2): (−1, +1), same class as H²;
(5) products of 1..6 ladders (all multisets over the 18 ladders): the set of (χ_t, χ_s) is exactly {(+,+), (−,−)}; disjoint from (−,+);
(6) DROP χ_s: with χ_t alone, H² (χ_t = −1) matches exactly the products with an odd number of half-integer-helicity factors — Lyra's rule reproduced;
(7) SENSITIVITY: if P2 failed (a hypothetical half-integer-spin piece of H² in 4D, (−1,−1)), the sets would overlap — the conclusion rests on P2 and is shown to.
DIRECTION: all as stated. KILL (for K1935's disjointness): any product of ≤ 6 ladders with (−1,+1), or any weight of H²'s restricted character with χ_s = −1.
