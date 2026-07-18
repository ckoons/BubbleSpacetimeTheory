# The Conservation Laws of the Standard Model as the Symmetries of One Geometry
### Standalone companion to the flagship — DRAFT, Keeper, 2026-07-18. Every conserved charge is a symmetry — continuous or topological — of D_IV⁵.

**Authors:** Casey Koons with the CI team (Lyra, Keeper, Elie, Grace); referee Cal A. Brate.

---

## Abstract
We account for the conservation laws of the Standard Model as symmetries of a single bounded symmetric domain, D_IV⁵ = SO(5,2)/[SO(5)×SO(2)]. The **continuous** conservation laws are the Noether currents of the domain's isometry group: energy, momentum, and angular momentum from the spacetime isometries; electric charge from the SO(2) complex structure; and weak isospin, hypercharge, and color from the domain's three division-algebra structures. Their count is **20 = g + c₃**, both invariants of the domain. The **discrete** conservation laws are *topological* — beyond Noether: **baryon number is a trefoil-knot count, lepton number a winding count, and generation number a cycle count**. This explains what the Standard Model leaves unexplained — why baryon and lepton number are conserved at all (topology protects them) and how they are violated (only by discrete topology change: the ΔL=2 Majorana neutrino mass). Finally, the *pattern* of which symmetries hold exactly and which are broken is itself a prediction: CPT is exact, while parity, CP, and scale are broken by mechanisms the geometry derives (an odd embedding dimension; the Jarlskog phase; the mass scale).

## 1. Principle
Noether's theorem turns each continuous symmetry into a conserved current; a domain's discrete symmetries give C, P, T; and its *topology* gives conserved counts no continuous symmetry produces. The isometry algebra of D_IV⁵ is **so(5,2)** (dimension 21 = N_c·g), forced by the requirement of three colors, three generations, and complex dimension five. Conservation is therefore not an input — it is the shadow of the domain's symmetry and its topology.

## 2. The continuous (Noetherian) conservation laws
Each is a specific generator of so(5,2) or of the isotropy K = SO(5)×SO(2) (T1945; the 21 generators verified as exact isometries, Elie):

| conservation law | # | origin (symmetry of D_IV⁵) | status |
|---|---|---|---|
| Energy | 1 | time translation | exact |
| Momentum | 3 = N_c | spatial translation | exact |
| Angular momentum | 3 = N_c | SO(3) rotation | exact |
| Electric charge | 1 | the SO(2) complex structure J | exact |
| Weak isospin | 3 = N_c | SU(2)_L ⊂ SO(5) | EWSB-hidden |
| Weak hypercharge | 1 | U(1)_Y | EWSB-hidden |
| Color | 8 = C₂ − N_c | SU(3) (compact-dual Q⁵) | exact |

**Continuous total = 7 (spacetime) + 13 (gauge) = 20 = g + c₃**, both BST integers (c₃ = the third Chern integer of the compact dual Q⁵). The Lorentz subalgebra has dimension 6 = C₂. **[derived tally; the domain fixes which generator gives which law]**

## 3. The topological (non-Noetherian) conservation laws
These are protected by *homotopy*, not by any continuous symmetry — Noether cannot produce them (T1945/T1929):

| conservation law | topological origin | why beyond Noether |
|---|---|---|
| **Baryon number B** | **trefoil (3-crossing) knot count** (N_c = 3 forced) | a knot cannot be continuously unknotted |
| **Lepton number L** | **SO(5) winding count** (leptons colorless) | a winding number is a homotopy class |
| **Generation number** | **Q⁵ cycle count** | cycle count on the compact dual |

## 4. What Noether cannot do — the topological origin explains the SM's accidents
In the Standard Model, baryon and lepton number are *accidental* global symmetries: nothing forces them, and Noether supplies them only as after-the-fact U(1)s. BST gives them a cause:
- **Why they are conserved:** topology protects them (a knot, a winding).
- **How they are violated:** only by *discrete topology change*. B+L is violated by electroweak sphalerons (which preserve B−L); **L (and B−L) is violated by exactly two units by the neutrino Majorana mass** — the ΔL=2 event that makes neutrinoless double-beta decay occur. Baryon number, the trefoil count, is *absolutely* conserved: the proton is stable, τ_p = ∞ (there is no grand-unified scale into which the color integer could dissolve).
This is the content the Standard Model lacks: not just *that* B and L are conserved, but *why*, and *how* they break.

## 5. The exact/broken pattern is itself a prediction
BST reproduces not only the conservation laws but **which hold exactly and which break, and why:**
- **Exact:** energy, momentum, angular momentum, electric charge, color, **CPT** (from the connected isometry group), and **baryon number**.
- **Broken by derived mechanisms:** **parity** (the volume element is central because g = 7 is *odd* — a chirality lock, K729); **CP** (the Jarlskog phase); **scale/dilatation** (broken by the mass ruler — exact only on the conformal, massless boundary); **lepton number** (the ΔL=2 Majorana mass).
Every breaking has a *named geometric source*. The pattern is a downstream prediction of the geometry, not an input.

## 6. Falsifiability
- **Baryon number = trefoil ⇒ the proton is absolutely stable.** A confirmed proton-decay event at *any* lifetime (Super-K / Hyper-K) falsifies BST.
- **Lepton number violated by ΔL=2 (Majorana) ⇒ neutrinoless double-beta decay occurs**, |m_ββ| ∈ [1.44, 3.63] meV — a detection supports BST; a confirmed null below ~1 meV (with m₁ = 0 established) falsifies it.
These two — proton stability and a 0νββ signal in a specific window — are the sharp topological-conservation predictions.

## 7. What is not claimed
- The **explicit** current forms (j^μ_ξ = T^{μν}ξ_ν for isometries; the internal currents) require the explicit Bergman–Dirac Lagrangian; the *inventory* (which symmetry gives which law) is complete, the closed-form currents are framework-pending.
- Color conservation rides the color-structure tier (SU(3) hosted on the compact dual; confinement is derived, the full dynamics is open).
- The continuous tally 20 = g + c₃ is a bookkeeping identity, not a representation dimension (we do *not* claim the unrelated appearance of 27 = 7+13+... as structural).

## 8. Conclusion
The conservation laws of the Standard Model are the symmetries of one domain: its isometries give the continuous charges (20 = g + c₃), and its topology gives three charges no continuous symmetry can — with the topological origin explaining what the Standard Model leaves as accidents, and the exact/broken pattern falling out as a prediction. Conservation is the shadow of the geometry.

---
*Draft status:* complete as a short standalone; companion to the flagship, the α standalone, and the Five-Absence falsifier. Needs: Cal referee on the 20 = g + c₃ split and the topological identifications; the explicit currents inlined once the Bergman–Dirac Lagrangian (LAG-1) is available. Dimension counts verified (`conservation_inventory.py`).

— Keeper, 2026-07-18. Conservation = Noether on so(5,2) (20 = g + c₃) + three topological charges (baryon = trefoil, lepton = winding, generation = cycle — beyond Noether). Topological origin explains the SM's B/L accidents; exact/broken pattern is a prediction (CPT exact; P/CP/scale/L broken by derived mechanisms). Falsifiers: proton stability + 0νββ. See [[Keeper_Conservation_Laws_Inventory_from_the_isometry_group_2026-07-18]], [[BST_FLAGSHIP_The_Standard_Model_as_Representation_Theory_of_D_IV5_DRAFT_2026-07-18]].
