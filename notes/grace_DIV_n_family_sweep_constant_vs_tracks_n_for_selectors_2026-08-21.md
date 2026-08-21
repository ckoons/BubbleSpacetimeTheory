# D_IV^n family sweep: which invariants are constant (rank-generic) vs track n — the selector reference (Grace, Round 38)

*Round 37's "forced" selector died because it read the RANK (constant 2 → dim 3 for every n) and selected nothing. Standing tool: family-sweep every forcing-selector before it banks. This note is the reference data — for each n∈{4…9}, what is constant and what tracks n — so Cal/Elie can answer "does my selector track n or the rank?" from the corpus, not by re-deriving. Rank(D_IV^n)=2 is NOT n_C=5. Pinned: rank const (T316/T1788), strata=rank+1=3 const (T2548/T2527), Peirce (1,n−2,1) (T2568), genus=n / Wallach floor=a/2 (T2517).*

## The sweep (Lie ball D_IV^n, complex dim n, rank 2 for all n≥3)

| n | rank | strata=rank+1 | mult a=n−2 | genus p=n | Wallach floor a/2 | ladder ν_W=a | Šilov dim=n | conf-bdy dim=n−1 | diagonal-stratum | single-boost=n |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 2 | 3 | 2 | 4 | 1 | 2 | 4 | 3 | 3 | 4 |
| **5** | **2** | **3** | **3=N_c** | **5=n_C** | **3/2=ρ₂** | **3** | **5** | **4** | **3** | **5** |
| 6 | 2 | 3 | 4 | 6 | 2 | 4 | 6 | 5 | 3 | 6 |
| 7 | 2 | 3 | 5 | 7 | 5/2 | 5 | 7 | 6 | 3 | 7 |
| 8 | 2 | 3 | 6 | 8 | 3 | 6 | 8 | 7 | 3 | 8 |
| 9 | 2 | 3 | 7 | 9 | 7/2 | 7 | 9 | 8 | 3 | 9 |

## The classification (the load-bearing part)
- **CONSTANT across the family (rank-generic — the TRAP):** rank = 2; boundary-strata count = rank+1 = 3; the **diagonal-boost bifurcation stratum = 3** (the Round-37 dead selector — reads rank, returns 3 for every n, selects nothing).
- **TRACKS n:** multiplicity a=n−2; genus p=n; Wallach floor a/2; ladder ν_W=a; **Šilov dim = n**; **conformal-boundary dim = n−1**; **single-boost stratum = n** (Elie's live thread).

**Any selector whose computed value sits in the CONSTANT column cannot force n=5 — it forces nothing.** Positive-control every selector on the member it should distinguish (run it on D_IV⁴; if it returns the same value as D_IV⁵, it is rank-generic).

## ★ The second gate (a trap the first sweep doesn't catch): tracking n ≠ forcing 5D over 4D
For confinement (ii) the choice is **5D Šilov ∂_S (dim n) vs 4D conformal boundary (dim n−1)**. Look at the table: **both columns track n.** So a selector that merely "tracks n" (e.g. the single-boost stratum, dim=n) clears Gate A but still may not resolve the 5D/4D choice — because dim n and dim n−1 are BOTH n-dependent. The selector must specifically **land on n vs n−1** (the ∂_S/conformal distinction), not just vary with n.

**Two gates for any (ii)-selector:**
- **Gate A — tracks n?** Sweep n=4…9; if constant, dead (like Round 37). Necessary.
- **Gate B — n vs n−1?** Does it pick the dim-n object (∂_S) over the dim-(n−1) object (conformal boundary), *for a structural reason*, not by reading the 4D answer back off SO(4,2)? This is the real confinement (ii) content. Cal's long-root/𝒫-conjugacy candidates must pass BOTH.

## What actually singles out n=5 (for whoever finds the real selector)
Tracking n is necessary; *discriminating 5* needs a condition true at 5 and false at 4,6,7,…. The corpus-pinned ones (NOT confinement selectors — these are the census/rank facts, for reference):
- a=n−2=N_c=3 (measured color) — selects 5 by the input N_c=3 (T2511).
- Strong-Uniqueness (K1697): smallest odd n≥5 with quaternionic spinor + non-orientable boundary → survivors {5,11,13,…}, N_c=3 picks 5.
- These are the SM-theorem selectors. A *confinement* selector would need its own n=5-discriminating condition on the boundary geometry — not yet found.

## For Elie / Cal (use, don't re-derive)
- **Elie single-boost thread:** dim B = n (tracks n ✓ Gate A). Re-pin the Kay–Wald convention (you flagged dim = n vs n−2) before reading a result; then it must clear Gate B (n vs n−1).
- **Cal 𝒫-conjugacy + long-root wall + closed-G-orbit + AdS₆-bdy:** sweep each across n=4…9 against this table. The AdS₆ boundary dim and closed-G-orbit dim are the likely rank-generic suspects — check them the way the diagonal selector should have been checked.

Compute: inline table (this note). Corpus edges: T316/T1788 (rank), T2548/T2527 (strata=rank+1), T2568 (Peirce (1,n−2,1)), T2517 (genus/Wallach floor), K1697 (Strong-Uniqueness). Nothing derived fresh — standard type-IV Lie data + corpus pins. Nothing pushed; CP existence-only. — Grace, Round 38
