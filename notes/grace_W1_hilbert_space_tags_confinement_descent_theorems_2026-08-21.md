# W1 audit support: which Hilbert space each confinement/descent theorem lives on (Grace, Round 40)

*Cal+Lyra own the W1 physics (which space is correct); this is the tag map — for each load-bearing confinement/descent theorem, which of the three spaces it actually uses, so the collision sweep has a target list. Reconnected: T1416, T1271, T2442/BACKLOG:561, registry:7519, T1807, T2523. Pre-dispatch-blocking. Discipline: name one space or cite the map before dispatch (§666 imported across).*

## The three spaces
- **A²(D_IV⁵)** — Bergman (weighted-holomorphic L²); the H_{ν_W} family; G acts (holomorphic discrete series). Registry:7519: H_sub = L²∩Hol = **A²** (correct).
- **H²(D_IV⁵)** — Hardy (Šilov boundary values); the ν_W-edge/boundary-value space. A² and H² are **standard companions** (weight ↔ boundary-value; the Poisson/Szegő and Π_Š maps connect them).
- **L²(Γ\G/K)** — automorphic (functions on the arithmetic quotient; **G does NOT act**). The modular/Bisognano–Wichmann/W4-net beast. The DIFFERENT one.

## The tag table (confinement + descent + the W1-adjacent)

| theorem / object | lives on | cross-use status |
|---|---|---|
| **T2523** colour ⟺ λ₂>0 ⟺ Šilov-vanishing | **A² ↔ H²** — K-types in A², boundary values via **Π_Š (the A²→H² map)** | **LEGIT** — Π_Š IS the companion map; internally consistent. NOT automorphic. |
| **Wallach-floor pivot / H_{ν_W}** (5423/5428, ν_W-addresses) | **A²_ν (weighted Bergman) = H_{ν_W}**, edge → H² | LEGIT — Bergman side; the floor is the A²→H² edge. |
| **T2572** Casimir-algebra exclusion | **A²** (K-type decomposition of the holo. discrete series) | LEGIT — operators on A². |
| **T2517** Wallach strata / ρ-vector | **A²_ν / holo. discrete series** | LEGIT — the H_ν family. |
| **descent** (T2548, T2522, signature) | **Jordan/Peirce algebra** → physical states on **A²/H²** | LEGIT — algebra, not automorphic. |
| **confinement (ii) modular route** (Toy 337, W4, Bisognano–Wichmann) | **L²(Γ\G/K)** ← the different beast | ★ **CROSS-INTERFACE** — this is where §666 imported into the Bergman/Hardy setting. |
| **T1271** YM uniqueness | Hua Bergman **boundary values (A²↔H²)** + **BW (automorphic-adjacent)** | ★ **CROSS-USE to audit** — mixes the companions with BW. |
| **T1807** Boundary-Interior Modularity | **H² (Šilov data) ↔ L²(Γ\...) (weight-2 automorphic)** | ★ CROSS-INTERFACE, tier Conditional already. |
| **T1416** Wightman W1–W5 | **W1 = L²(Γ\D_IV⁵)** but **W4 = Bergman** | ★★ **THE ROOT** — the axiom set itself names two of the three spaces. |

## The two concrete findings for the audit
1. **The confinement PHYSICS is clean on A²/H².** T2523, the pivot (5423/5428/H_{ν_W}), T2572, T2517, and the descent algebra ALL live on the **Bergman/Hardy companions** — a legitimate, standard weight/boundary-value cross-use (Π_Š is the actual map between them). No automorphic space enters the confinement physics. So the W1 problem is NOT inside the confinement results.
2. **The collision is localized to the A²/H² ↔ L²(Γ\G/K) interface** — where the modular/automorphic machinery (BW, Toy 337, W4-net) meets the Bergman/Hardy physics. §666 crossed exactly there. The W1-audit target list is: **T1416 (root — W1 vs W4 name two spaces), the confinement-(ii) modular route, T1271 (BW + Hua), T1807.**

## ★ A literal name-collision to fix (dimension-tag-class, but for space-type)
- **"Bergman H²(D_IV⁵)"** (BACKLOG:561, "THE BST Hilbert space, T2442") **fuses A² (Bergman) and H² (Hardy) into one symbol.** registry:7519 correctly has H_sub = **A²**. Same object called "A²" in one place and "Bergman H²" in another. **Pin one:** the BST substrate Hilbert space is **A²(D_IV⁵, dμ_sub)** (Bergman); the Hardy H² is its **boundary-value companion**, related by Π_Š — not the same symbol. @Cal — this is the space-type analogue of your dimension-tag rule; every Hilbert-space name should carry its type (A² Bergman / H² Hardy / L²(Γ) automorphic) at first use.

## Recommendation to @Cal/@Lyra (you own the physics; I tagged)
- The physical Hilbert space of the confinement/descent results is **A²(D_IV⁵)**, with **H²** its Šilov boundary-value companion (map = Π_Š, Poisson/Szegő). Cross-use between A² and H² is legitimate and should be stated with the map named.
- **L²(Γ\G/K) is a genuinely different space** (no G-action) — every import between it and A²/H² (BW, modular flow, W4-net) needs an **exhibited map**, not interchangeable use. T1416's W1(=L²(Γ)) vs W4(=Bergman) is the root to resolve: name one physical space and cite the maps to the others.

Edges: T1416, T1271, T2442, T1807, T2523, T2517, T2572, registry:7519. Nothing derived — a tag map for the audit. Nothing pushed; CP existence-only. — Grace, Round 40
