STOP. You have hit a wall. Route around it.

You are blocked on a problem. Instead of pushing harder in the same direction, use the AC theorem graph and the BST toolbox to find alternative paths. Walls are doors approached from the wrong side.

## Step 1: Name the wall.
State in one sentence: "I cannot get from X to Y because Z is missing/unproved/too hard."

## Step 2: Search the graph for alternative paths.
Run: `python3 play/toy_bst_explorer.py connect <X> <Y>`
This does BFS across 1700+ nodes and 48+ domains. If a path exists, it will show the intermediate concepts and which domains they traverse.

If `connect` doesn't find a path, try:
- `python3 play/toy_bst_explorer.py search <X>` — what touches X?
- `python3 play/toy_bst_explorer.py search <Y>` — what touches Y?
- `python3 play/toy_bst_explorer.py domain <likely_domain>` — what tools exist in adjacent domains?

## Step 3: Identify bridges from other domains.
For each domain that touches BOTH X and Y (or concepts near them), ask:
- Does this domain have a proven result that connects them?
- Is there an isomorphism, duality, or correspondence that translates the problem?
- Can I restate the blocked step in this domain's language?

Common bridge patterns in BST:
- **Topology ↔ Number theory**: Chern classes, Euler characteristics, L-functions
- **Representation theory ↔ Physics**: K-types, Casimir eigenvalues, selection rules
- **Algebraic geometry ↔ Analysis**: Bergman kernel, Poisson kernel, theta lifts
- **Combinatorics ↔ Geometry**: Root systems, Weyl groups, lattice constructions
- **Modular forms ↔ Automorphic forms**: Borcherds lift, theta correspondence, Langlands

## Step 4: Reverse the approach.
Instead of building from X toward Y, start from Y and work backward toward X. Ask:
- What would Y look like if viewed from D_IV^5's geometry?
- What tools PRODUCE Y as output? Can we feed them BST input?
- Is there a dual/adjoint/inverse construction that goes the other direction?

Example: Lyra's Borcherds Bridge (Toy 2238). Wall: "VOA construction needs algebra, BST has geometry." Reversal: Borcherds lift goes FROM modular forms (which BST has) TO automorphic forms on Type IV domains (which IS D_IV^5). The bridge existed — we were just facing the wrong way.

## Step 5: If no path exists, document the gap.
If after Steps 2-4 you still cannot find a route, this is genuine new information:
- File the gap in `notes/BACKLOG.md` with: what's blocked, what domains you checked, why no bridge exists
- The gap itself may be a research target — "why doesn't domain X connect to domain Y?" is a question worth answering

## The principle
"Every wall is really a question: is there a path through a domain we haven't checked yet?" — Lyra, May 15 2026

Casey standing order May 15: When encountering walls, search the graph for alternative paths through other domains. Use existing tools from ANY mathematical domain. The graph is the instrument.
