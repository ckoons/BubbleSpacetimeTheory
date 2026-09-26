# Lyra R10: sparing s ≤ 2 is generic, not a mechanism. The question collapses to "an interaction plus a 4D stress tensor", and neither restriction carries a 4D stress tensor. W is a Lie-algebra element; point commits see only channel 0

**Lyra, Saturday 2026-09-26, 16:21 EDT (from `date`).** Written in K1653's **K-type mode picture**: statements concern which bilinear K-type modes sit at the conservation weight. Nothing here claims that particles are Flato–Fronsdal composites.

**Blindness disclosure:** Cal hashed Sections 999/1000 at 16:18. I have not opened those files. I read their commit subjects at 16:20:53, and they say "sparing s ≤ 2 is consistent and GENERIC … not creditable to a mechanism". I had reached the same reframe from the pinned theorem statements a minute earlier. It is recorded in my session messages to Casey but was **not hashed**, so treat item 1's reframe as **not blind**.

**Pins, from the numbered statements in the paper bodies (read 16:19; neither abstract used):**
- **Maldacena–Zhiboedov** (arXiv:1112.1016, "Assumptions" a–e and "The theorem, or conclusion"): (c) a conserved current of spin **s > 2**; (d) d = 3; (e) a **unique conserved spin-2 current, the stress tensor**; (a′) a finite stress-tensor two-point function (this excludes N = ∞ vector models). Conclusion: the correlators are those of free bosons or free fermions.
- **Alba–Diab** (arXiv:1510.02535, the introduction's statement (a)–(d)): unitarity, cluster decomposition, (c) a symmetric conserved current of **spin larger than 2**, (d) a **unique stress tensor, d > 3**. Conclusion: free bosons, free fermions, or free (d−2)/2-forms.

**Instrument:** `play/toy_5825_lyra_R10_…no_stress_tensor.py`, sha256 `2c21b76dc65d82f6…`, hashed before the run. **SCORE 3/3**, output `play/.out_toy_5825.txt`.
**didwe:** Keeper's sweep ("higher spin" → K3; "Coleman-Mandula" → K443). Both are reconnected below.

---

## Item 1: the breaking pattern

**Kill line (Keeper's, restated verbatim):** *"if every BST candidate either preserves all currents (so Maldacena–Zhiboedov makes it free) or breaks them uniformly (sparing neither 1 nor 2), BST has no mechanism for the observed pattern of conserved spins."*

**The K-type content (C1/C2, exact to weight 40):**
> **Rac ⊗ Rac = [scalar at 3] ⊕ ⊕_{s≥1} [conserved spin-s current at 3 + s], one of each.**

This is the conservation quotient, and the control without the divergence subtraction fails. Spin 1 is at 4 (a gauge field's source), and spin 2 is at 5 = d (the stress tensor).

**Lifts above conservation, at every spin (C3):**

| module | 5D lift | 4D lift (after restriction) |
|---|---|---|
| Rac | 0 (all currents) | Rac| → H_{3/2}(D_IV⁴): **1** |
| H² | 2 (none) | H²| → H_{5/2}(D_IV⁴): **3** |
| 4D singleton (λ = 1) | — | 0, **but it is absent from both restrictions** (R6/R7) |

**The candidates, enumerated before any is preferred:**

| candidate | which currents stay conserved (γ_s = 0) | spares exactly s ≤ 2? |
|---|---|---|
| **odd clock** (H² = Rac ⊗ odd clock) | none: a uniform lift of 2 | no (spares nothing) |
| **ruler** (a scale, no vertex) | a free massive theory; the S-matrix is trivial, so Coleman–Mandula's premise fails | no (nothing interacts) |
| **N_max = 137 cutoff** | currents whose lowest K-type fits below the cutoff (3 + s ≤ 137, i.e. s ≤ 134) survive in their low modes; higher ones are cut | no (the edge is at s ≈ 134, not 2) |
| **descent as a slice** (restriction) | none in 4D: a lift of 1 (Rac) or 3 (H²) | no (spares nothing, **not even the 4D stress tensor**) |
| **descent as KK** (compact normal direction, zero modes) | the zero modes of **all** currents (∫ J over the compact direction is conserved by periodicity) | no (spares everything, so free) |
| **the commit as a point evaluation** | at first order, **all s ≥ 1** (item 2: it touches only the scalar channel) | no (at first order; see below) |

**Verdict: the kill line fires as written.** No candidate by itself spares exactly s ≤ 2.

**But the question is mis-posed, and the pinned theorems say why.** Both theorems **assume** a unique conserved stress tensor (s = 2) and conclude "free" only from a conserved **s > 2** current. Coleman–Mandula's own statement allows conserved spin-1 currents as internal symmetries whose charges are Lorentz scalars (Alba–Diab's introduction, restating it).
- **So "every s > 2 broken, s = 2 and s = 1 kept" is what ANY interacting, local, unitary CFT with an internal symmetry looks like.** The Wilson–Fisher O(N) model is the standard example.
- **The observed pattern needs no special selection mechanism.** It needs three ordinary things:
  - **(i) an interaction.** This is round 9's wall; the one door is the commit.
  - **(ii) a unique stress tensor at the level where physics is read.**
  - **(iii) an internal symmetry for the s = 1 currents.** The record's PU(3) (K1926) is a global symmetry and would supply conserved adjoint spin-1 currents. Gauging them is a further step.

**The new finding, (ii) in 4D.** In 5D the Rac level has its stress tensor (s = 2 at 5). **In 4D, neither restriction carries one**: Rac| is lifted by 1 and H²| by 3. A 4D conserved stress tensor, and a 4D conserved spin-1 current, need the 4D singleton λ = 1, and BST's restrictions never contain it.
- This is the **same absence as R7's Gauss's-law result**: the missing λ = 1 is what 4D's r^{−2} flux law needs, and it is what 4D current conservation needs. **Gauss's law in 4D and a 4D stress tensor are one missing module.**
- As a slice, the descent gives a defect with no 4D T (energy leaks into the normal direction). As KK, it gives a 4D T (the zero mode) but keeps every higher-spin zero mode too, so the result is free.
- **So BST's descent, in either reading, does not produce "interacting 4D theory with T".** That is the third wall seen from 4D.

**The commit at second order (calibrated, not claimed):** iterating a point-evaluation vertex would generically break s > 2 at second order and keep T, provided a T exists at that level. That is the generic pattern again. It is creditable to "there is an interaction", not to the commit's form.

**Reconnects:**
- **K443** (Coleman–Mandula on F(4), 06-20): MZ and Alba–Diab are its CFT form. Both say that one exactly conserved s > 2 current means free.
- **K3** (SO(5) → SO(4) → SO(3,1) spin labels): a 5D spin-s current restricts to 4D spins s, s−1, …, 0 (branching (s,0) → ⊕_{i≤s} (i/2, i/2)). For the 5D stress tensor this gives **4D spins 2, 1, 0** (graviton, graviphoton, radion), the Kaluza–Klein labels. **A lead only, flagged as a menu risk:** a 4D spin-1 appearing together with spin-2 from one 5D stress tensor is Kaluza's photon. Under KK it arrives with every higher-spin zero mode, so it is free.
- **The 08-08 "gravity emergent, no graviton" capture** (tier: a capture, not a registered theorem; checked by name): **it is compatible with a composite stress tensor.** The Rac ⊗ Rac spin-2 mode at weight 5 is an **operator** (a conserved bilinear K-type mode), not a propagating spin-2 **field**. A CFT has T without a graviton (holography puts the graviton in the bulk). What this round adds: **in 4D there is no T from either restriction**, so whatever couples to 4D energy is not a boundary bilinear. That is consistent in shape with the capture's "gravity = the SO(5,2)/SO(4,2) bulk". Stated, not assumed.

## Item 2: is the commit a point evaluation?

**Antecedent (K1932 Part 2), verbatim:** *"If BST FORCES 'commit = point evaluation' (Casey: a write at a point; K1925's W = D(x,e); Elie's W_x² = −q(x,x) ē ēᵀ), then interactions live only in the (0,0) channel."*

**(a) W = D(x,e) is NOT a point evaluation. It is a Lie-algebra element.**
- D(x,y) spans the structure algebra of the Jordan triple, which is **k_ℂ** (Loos). Cal Section 988: dim_ℂ 11 = so(5,ℂ) ⊕ ℂ. So W_x ∈ k_ℂ.
- It acts on H² as a **linear vector field**, z ↦ {x,e,z}, which **preserves polynomial degree**. A point evaluation f ↦ f(z₀)·S(·,z₀) is **rank one** and mixes every degree.
- **Consequence:** a Lie-algebra element acts on two-body states by the coproduct, W ⊗ 1 + 1 ⊗ W. So **W can never produce a γ.** The algebraic write belongs to the kinematics. (This also completes K1925/Cal Section 988: W is forced and arrow-aligned, and it is part of the symmetry, not an interaction.)

**(b) The point evaluation is a different object. The geometry supplies the family; BST does not force the choice.**
- The family {S(·, z)} (the Szegő reproducing kernels, coherent states) and its normalization (the Born density |f(z)|²/S(z,z), R9 item 3) are canonical and carry zero knobs.
- "**A commit IS an evaluation at a point**" is Casey's ontology ("a write at a point"): a posit, not a theorem. The point z₀ is also a frame choice (it breaks G to K_{z₀}), so a fixed-point commit is K-invariant, not G-invariant. That is **K1878's lane** (a K-invariant perturbation), and its STOP reason (zero Casimir cost for the push) has to be checked against it.

**(c) The structural lemma behind "(0,0) only". It is zero-knob given (b)'s posit.**
- **Every fusion channel m ≠ 0 vanishes identically on the diagonal of D × D.** Its lowest vector is built from z₁ − z₂ (Elie 5820). G acts diagonally, preserving the diagonal. So the whole G-module vanishes there.
- Equivalently: the multiplication map f ⊗ g ↦ fg (restriction to the diagonal) is G-equivariant onto the weight-5 Bergman module, with kernel exactly ⊕_{m≠0}.
- **So any vertex that sees two quanta only where they coincide (a commit of both at one point, whatever the point or the measure) touches only channel 0, the Bergman (0,0) channel.** On the Rac level the same lemma means only the scalar at 3 is touched, **so every current s ≥ 1 is untouched at first order.**
- **Why AdS φ⁴ differs (Elie 5821: all l = 0):** holomorphic two-body states in channels b ≥ 1 vanish at coincidence (they carry q(z₁ − z₂)^b). The AdS bulk extension is harmonic, not holomorphic, so its n ≥ 1 double traces do not vanish at a bulk point. **Holomorphy is the reason for the (0,0)-only shape.** This is a position.
- **Scope, per Elie's R10 prereg subject ("diagonal restriction ≠ fixed-point commit"):** the lemma covers both. Channels m ≠ 0 vanish on the whole diagonal, hence at any single point (z₀, z₀). The difference Elie flags is covariance (G vs K_{z₀}), not the channel content.

**Verdict:** "commit = W" gives no interaction, since W is kinematics. "Commit = point evaluation" gives the (0,0)-only shape, **zero-knob given the posit**, with its strength free. It is also frame-dependent (K-invariant), which puts it in K1878's lane: that STOP must be re-read before the lane opens.

## Item 3: Time, Derived
Cal pre-gated the three-line fix as PASS on the K1653 premise (Section 1000). **Waiting only on Casey's GO; I apply it the moment it comes.**

---
**For Cal:** compare with Sections 999/1000.
- (1) I agree that sparing is generic. The addition is that **in 4D there is no T from either restriction** (lifts 1 and 3), which is the same missing λ = 1 as Gauss's law.
- (2) W ∈ k_ℂ is kinematics. The diagonal-vanishing lemma, and holomorphy as the reason for the difference from AdS.

**For Keeper (tomorrow's file):** the day's three walls gain a 4D corollary. **4D current conservation (spin 1: Gauss; spin 2: T) needs the λ = 1 module that BST's descent never produces.** That is a sharper door than "the breaking pattern": **how does D_IV⁴'s minimal representation enter BST's 4D physics at all?**
