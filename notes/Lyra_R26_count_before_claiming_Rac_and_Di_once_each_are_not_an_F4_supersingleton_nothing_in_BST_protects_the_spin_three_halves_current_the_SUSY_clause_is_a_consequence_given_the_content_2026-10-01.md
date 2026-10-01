# Lyra R26: count before claiming. Rac and Di once each are not an F(4) supersingleton; nothing in BST protects the spin-3/2 current; the SUSY clause is a consequence, given the content

**Lyra, Thursday 2026-10-01 (timestamps from `date`). Toy hashed 13:01:22 and draft written before I read Cal Section 1028's subject (prereg 837618ba, 13:01; file not opened).** **Cal's subject, restated:** *"free-level Q exists (TD line 99 'not an operator Q' false at free level); predicted not F(4) by multiplicity (hyper = Rac × 2 + Di; BST Rac × 1); nothing keeps it (Z_t a selection rule; dS breaks SUSY; interactions); SUSY clause = consequence iff the count fails."* **Independent agreement** on the multiplicity count, the protectors and the consequence. **Cal's first point is one I missed, and it is right** (Section 4).
**Instrument:** `play/toy_5856_lyra_R26_…dof_and_su2R.py`, sha256 `b7ef09ce3067f06c…`, hashed and run at 13:01:22. **SCORE 4/4**, output `play/.out_toy_5856.txt`. F2 and F3 are bookkeeping on the stated content; F4 is the clock-sign check.
**didwe:** "supersymmetry F(4) hypermultiplet" → 0. The corpus lineage is via K434/K443/F235 (named in the prompt).

**Group, family, action (stated first):**
- **F(4) = 24 | 16** (F1): even part so(5,2) ⊕ su(2)_R (21 + 3), odd part = the so(5,2) spinor 8 ⊗ the su(2)_R doublet 2. The odd generators shift J by ±½ and flip the spin.
- **Families:** Rac₅ (scalar, E₀ = 3/2), Di₅ (spinor, E₀ = 2) (K956).
- **The free 5D N=1 hypermultiplet:** 4 real scalars, an **su(2)_R doublet** of complex scalars at Δ = 3/2, plus one symplectic-Majorana pair (one 5D Dirac spinor) at Δ = 2, an su(2)_R singlet. Standard; **pin owed (Grace: Nahm 1978; the hypermultiplet as an F(4) representation).**

**Kill line (Keeper's, restated verbatim):** *"if a BST structure keeps the spin-3/2 current exactly conserved after the breaking, BST predicts superconformal / supersymmetric structure, which contradicts its own Forbidden list."*

---

## 1. The singleton content against the F(4) supersingleton: COUNTED, and it does not match

| | the hypermultiplet (F(4) supersingleton) | BST's stated content (Rac₅ ⊕ Di₅, once each) |
|---|---|---|
| scalars | su(2)_R **doublet**, 4 real on-shell d.o.f. | one Rac: 1 real (or 2 if complex) |
| fermion | one 5D Dirac spinor (su(2)_R singlet), 4 real on-shell d.o.f. | one Di: 4 real |
| bosonic = fermionic? | **4 = 4** | **1 or 2 ≠ 4**: not a supermultiplet (F2) |
| su(2)_R | present (the R-symmetry) | **absent:** no BST structure supplies an su(2) acting on singleton multiplicities |
| the supercurrent | an su(2)_R doublet (it carries the supercharges' index) | the conserved spin-3/2 piece of Rac⊗Di has **multiplicity 1** (R25, toy 5854): **no doublet** (F3) |

- **Verdict: BST's singleton content matches the hypermultiplet in Δ and spin, but NOT in multiplicity or R-structure.**
- Keeper's menu warning holds exactly: the field-content match (Δ = 3/2 scalar, Δ = 2 spinor) is real, and the multiplet match fails on counting.
- **The conserved spin-3/2 piece is a fermionic higher-spin current of the free singleton pair,** one of the infinitely many currents every free theory carries (R10, R25). **It is not F(4)'s supercurrent:** its charge carries no su(2)_R index, and the bosonic and fermionic counts differ, so its anticommutator cannot close on so(5,2) ⊕ su(2)_R. In the free theory it closes into a higher-spin superalgebra, not F(4).

**Reconnects:**
- **F235 (06-19, mine), verbatim:** *"the substrate is ℤ₂-GRADED — a Lie SUPERALGEBRA with even part ⊇ so(5,2) and odd part = the SO(5) spinor … F(4) … exists as the candidate superalgebra … 'μ/τ forced' now contingent only on … 'is Casey #16 even/odd a genuine super-grading (F(4))?'"* **Answered, for the singleton content: no.** A genuine F(4) grading needs the su(2)_R doublet and a matching boson/fermion count, and BST's singletons supply neither. F235's μ/τ conditional therefore stays conditional, with its condition now failed on counting. **F235 should carry a dated head.** The algebra exists, but BST's content does not form its representation.
- **K434 (06-20):** "F(4) is basic classical exceptional, the 5D superconformal". **Stands** as mathematics. It placed the algebra; it did not show that BST's content forms its multiplet.
- **K443 (06-20):** Grace's "no-superpartners wall … superconformal ≠ super-Poincaré; the lepton tower IS a broken multiplet". **The counting here gives that wall a sharper reason:** the singleton level is not a multiplet in the first place.

## 2. The protectors, enumerated (does any BST structure keep the spin-3/2 current after the breaking?)

| candidate | keeps the spin-3/2 current? |
|---|---|
| **the free higher-spin algebra** (the geometric level, the third wall: processes free) | **yes, but only while free.** Every current is conserved there, spin 3/2 included. Any interaction breaks the s > 2 and fermionic higher-spin currents generically (R10's pattern, extended). Not a protector of SUSY in particular |
| **F(4) superconformal symmetry** | **absent:** the content is not an F(4) multiplet (Section 1) |
| **the clock sign Z_t / W** | **no.** A supercharge shifts E by ½ (z_t flips) and flips spin (z_s flips), so W is unchanged: W(Rac) = W(Di) = −1 (F4). W is blind to whether supersymmetry is kept or broken |
| **the Šilov boundary's ℤ₂** (u ~ −u, the 2:1 of real forms) | **no.** It is the double cover's ±i on H² (R6 item 5), a statement about the clock, not about a fermionic generator |
| **the one breaking scale** (the ruler as a mass; Λ as curvature) | **no, and Λ actively forbids it:** both are tensor spurions, and **with Λ > 0 the surviving symmetry is de Sitter, which has no unitary positive-energy superalgebra** (the standard dS-supersymmetry no-go; **pin owed: Pilch–van Nieuwenhuizen–Sohnius 1985**). Unbroken SUSY is incompatible with BST's own Λ > 0 |
| **the commit** | records are ρ = vv† (bilinear, bosonic); a commit maps no boson to a fermion. **No** |

**Verdict:** nothing in BST keeps the spin-3/2 current conserved once there are interactions. **The kill line does not fire.**

## 3. The Forbidden list's SUSY clause: a consequence, given the content

**The clause (verbatim, via K1946):** *"any confirmed detection kills the framework: … a SUSY spectrum."*
**It is now a consequence, by two independent routes:**
1. **Counting:** BST's singleton content (Rac₅ ⊕ Di₅ once each, no su(2)_R) is **not an F(4) multiplet** (Section 1). There is no superconformal pairing at the singleton level to break or keep.
2. **Λ > 0:** BST's ledger picks de Sitter (R16), and de Sitter admits **no unitary positive-energy supersymmetry** (pin owed). Unbroken SUSY is incompatible with BST's own cosmology.

**Conditional on:** the content stated once each. If a future BST structure supplied the Rac with **doublet multiplicity under an su(2)** (that is, a genuine su(2)_R), route 1 would reopen; route 2 would still forbid *unbroken* SUSY. **Tier: a structural consequence (route 1 exact counting; route 2 pinned theorem, owed).** The clause moves from assertion to consequence, as Keeper's calibration hoped, with its one condition named.

**The precise sentence for the Forbidden list:**
> *"No SUSY spectrum: BST's singletons are not an F(4) supermultiplet (one Rac, one Di, no su(2)_R: the boson and fermion counts differ), so its free-level spin-3/2 current is a higher-spin current, broken with the others; and with Λ > 0 no unitary positive-energy supersymmetry exists."*

## 4. Time, Derived line 99 needs scoping (Cal Section 1028's point, adopted)

**v1.5 line 99, verbatim:** *"Disclaimer (not SUSY): the even-#Rac spin-2 (Δ=5) and odd-#Rac spin-3/2 (Δ=9/2) slots differ in weight by ½ — a supercharge's weight — but this is not supersymmetry: two towers are not an operator Q …"*
- **At the free level that is false.** The conserved spin-3/2 current of Rac⊗Di (R25: the s = 1 piece at 9/2) integrates to a **fermionic charge Q**, an operator mapping Rac ↔ Di, raising J by ½.
- **What is true, and what line 99 should say:** *"… at the free level the conserved spin-3/2 current gives a fermionic charge Q, but it is not an F(4) supercharge (one Rac, one Di, no su(2)_R: the counts differ) and it is not conserved once interactions enter; this is not supersymmetry."*
- **A v1.6 item, for Casey's word.** It is the same kind of fix as v1.5's Higgs line, and is not proposed for application today.

---
**For Cal:** compare with your hash; the counting table; the protector table; route 2's pin.
**For Grace:** Nahm 1978; the hypermultiplet as an F(4) representation (doublet scalars, singlet fermion); Pilch–van Nieuwenhuizen–Sohnius (no unitary positive-energy dS supersymmetry); a dated head on F235.
**For Keeper:** the Forbidden list's SUSY clause, upgraded to a consequence (two routes), with its condition named.
