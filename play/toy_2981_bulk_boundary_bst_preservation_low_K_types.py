"""
Toy 2981 — Bulk-boundary BST integer preservation at low Wallach K-types.

Gap #4 (Bulk-boundary partition function identity) push: Step 7 in the
skeleton (notes/BST_Bulk_Boundary_Partition_Identity_Skeleton.md) flags
computational verification as the path from skeleton → proof. This toy
executes the smallest version of that verification.

CLAIM (leading-order, per skeleton Step 7):
For Wallach K-type labeled by (m_1, m_2) on D_IV⁵, the boundary primary
operator conformal dimension is, to leading order,
    Δ(m_1, m_2) = m_1·rank + m_2·N_c
(see skeleton Step 7 bullet 3 — "in appropriate normalization").

This toy:
  (a) computes Δ for (m_1, m_2) in 0..6
  (b) checks each Δ is BST-expressible (primary or simple BST polynomial)
  (c) computes Wallach K-type dim d_m = (2m+N_c)(m+1)(m+rank)/C_2 for same m
  (d) cross-references — does the boundary Δ AND the bulk dim d_m use the
      same BST integer scaffold at each level?

HONEST SCOPE:
This is leading-order verification, not the full Knapp-Wallach proof.
The actual Faraut-Koranyi boundary conformal dimension formula includes
correction terms beyond the leading m_1·rank + m_2·N_c. Those corrections
may also be BST (that's the question for the full proof); this toy
establishes the leading-order BST pattern only.

TIER (per Casey May 16 discipline):
I-tier — partial verification of a conjectured identity. Full D-tier
requires the rigorous Knapp-Wallach + Faraut-Koranyi argument.

Owner: Lyra (Gap #4)
Date: 2026-05-17
Status: pushing the bulk-boundary skeleton from filed → with low-K-type verification
"""


def wallach_dim(m, N_c=3, rank=2, C_2=6):
    """d_m = (2m+N_c)(m+1)(m+rank) / C_2 (T1830)."""
    return (2 * m + N_c) * (m + 1) * (m + rank) // C_2


def leading_conformal_dim(m1, m2, rank=2, N_c=3):
    """Δ(m_1, m_2) = m_1·rank + m_2·N_c (skeleton Step 7 leading order)."""
    return m1 * rank + m2 * N_c


def bst_decompose(n, rank=2, N_c=3, n_C=5, C_2=6, g=7, c_2=11, c_3=13):
    """Try to express n as a small combination of BST primaries.

    Returns a string description or None if no clean decomposition found
    within the small-combination search space.
    """
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    # Direct primaries
    primaries = {
        rank: "rank", N_c: "N_c", n_C: "n_C", C_2: "C_2", g: "g",
        c_2: "c_2", c_3: "c_3",
    }
    if n in primaries:
        return primaries[n]
    # Powers of rank
    for k in range(2, 8):
        if rank ** k == n:
            return f"rank^{k}"
    # Single products of two primaries
    for p1, n1 in primaries.items():
        for p2, n2 in primaries.items():
            if p1 * p2 == n:
                return f"{n1}·{n2}"
    # rank^k times another primary
    for k in range(2, 6):
        rk = rank ** k
        for p, name in primaries.items():
            if rk * p == n:
                return f"rank^{k}·{name}"
    # Sums of two primaries (small)
    for p1, n1 in primaries.items():
        for p2, n2 in primaries.items():
            if p1 + p2 == n:
                return f"{n1}+{n2}"
    # primary * primary + primary
    for p1, n1 in primaries.items():
        for p2, n2 in primaries.items():
            for p3, n3 in primaries.items():
                if p1 * p2 + p3 == n:
                    return f"{n1}·{n2}+{n3}"
    return None


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    print("=" * 78)
    print("Toy 2981 — Bulk-boundary BST integer preservation at low K-types")
    print("Gap #4 partial verification (skeleton Step 7)")
    print("=" * 78)

    print("\n[A] Leading-order boundary conformal dim Δ(m_1, m_2) = m_1·rank + m_2·N_c")
    print("-" * 78)
    print(f"  {'(m_1,m_2)':>10}  {'Δ':>4}  {'BST decomposition':<25}")
    print(f"  {'-'*10}  {'-'*4}  {'-'*25}")

    delta_results = []
    for m1 in range(7):
        for m2 in range(7):
            d = leading_conformal_dim(m1, m2)
            decomp = bst_decompose(d)
            ok = decomp is not None
            delta_results.append((m1, m2, d, decomp, ok))

    # Print first 25 + summary
    for m1, m2, d, decomp, ok in delta_results[:25]:
        marker = "✓" if ok else "?"
        decomp_str = decomp if decomp else "(no clean BST form found)"
        print(f"  ({m1},{m2}):      {d:>3}  {decomp_str:<25} {marker}")

    if len(delta_results) > 25:
        print(f"  ... ({len(delta_results)-25} more entries omitted from print) ...")

    bst_count = sum(1 for _, _, _, _, ok in delta_results if ok)
    total = len(delta_results)
    print(f"\n  Δ BST-decomposable: {bst_count}/{total} ({100*bst_count/total:.1f}%)")

    print("\n[B] Bulk K-type dimension d_m = (2m+N_c)(m+1)(m+rank)/C_2 (T1830, single index)")
    print("-" * 78)
    print(f"  {'m':>3}  {'d_m':>4}  {'BST decomposition':<25}")
    print(f"  {'-'*3}  {'-'*4}  {'-'*25}")

    dim_results = []
    for m in range(8):
        d = wallach_dim(m)
        decomp = bst_decompose(d)
        ok = decomp is not None
        dim_results.append((m, d, decomp, ok))
        decomp_str = decomp if decomp else "(no clean BST form)"
        marker = "✓" if ok else "?"
        print(f"  {m:>3}  {d:>4}  {decomp_str:<25} {marker}")

    dim_bst = sum(1 for _, _, _, ok in dim_results if ok)
    print(f"\n  Wallach d_m BST-decomposable: {dim_bst}/{len(dim_results)}")

    print("\n[C] Cross-reference: bulk d_m and boundary Δ — same BST scaffold?")
    print("-" * 78)
    print("  For each m, what BST integers appear in d_m vs Δ?")
    print("  Bulk Δ are weighted sums m_1·rank + m_2·N_c — generates {0, 2, 3, 4, 5, 6, 7, 8, 9, ...}")
    print("  Bulk d_m are products of primary integers — generates {1, 5, 14, 30, 55, 91, ...}")
    print()
    print("  Overlap analysis (smallest 20 integers covered by either side):")
    boundary_integers = set()
    for _, _, d, _, _ in delta_results:
        if d > 0:
            boundary_integers.add(d)
    bulk_integers = set()
    for _, d, _, _ in dim_results:
        bulk_integers.add(d)

    both = sorted(boundary_integers & bulk_integers)
    only_boundary = sorted(boundary_integers - bulk_integers)[:10]
    only_bulk = sorted(bulk_integers - boundary_integers)[:10]

    print(f"  Both sides:    {both}")
    print(f"  Only boundary: {only_boundary}")
    print(f"  Only bulk:     {only_bulk}")
    print()
    print(f"  Critically: integers in BOTH lists are double-anchored — bulk K-type and")
    print(f"  boundary primary at the same integer level. This is the BST preservation")
    print(f"  signal Gap #4 needs as evidence at small m.")

    print("\n[D] Honest tier reading")
    print("-" * 78)
    print("  This toy verifies BST integer preservation at LEADING ORDER for low K-types.")
    print(f"  Boundary Δ BST-decomposable: {bst_count}/{total} = {100*bst_count/total:.1f}%")
    print(f"  Bulk d_m BST-decomposable: {dim_bst}/{len(dim_results)} = {100*dim_bst/len(dim_results):.1f}%")
    print(f"  Bulk-boundary integer overlap: {len(both)} integers")
    print()
    print("  NOT a proof. The actual Faraut-Koranyi boundary conformal dim formula has")
    print("  correction terms beyond the leading m_1·rank + m_2·N_c. Those corrections")
    print("  may also be BST (open question for the full proof). This toy establishes")
    print("  the leading-order BST pattern only.")
    print()
    print("  Tier: I (partial verification, skeleton Step 7 partially done).")
    print("  Gap #4 status update: 'skeleton + low-K-type leading-order verification'.")
    print("  Full closure still requires rigorous Knapp-Wallach + Faraut-Koranyi argument.")

    # Score = how cleanly the verification holds at leading order
    leading_order_pass = (bst_count >= total * 0.9 and dim_bst >= len(dim_results) * 0.9)

    print("\n" + "=" * 78)
    if leading_order_pass:
        print(f"SCORE: leading-order verification PASS")
        print(f"  Boundary {bst_count}/{total} + Bulk {dim_bst}/{len(dim_results)} both ≥ 90%")
    else:
        print(f"SCORE: leading-order verification PARTIAL")
        print(f"  Boundary {bst_count}/{total} + Bulk {dim_bst}/{len(dim_results)}")
    print(f"  Overlap integers (double-anchored): {len(both)}")
    print("=" * 78)
    return bst_count + dim_bst, total + len(dim_results)


if __name__ == "__main__":
    run()
