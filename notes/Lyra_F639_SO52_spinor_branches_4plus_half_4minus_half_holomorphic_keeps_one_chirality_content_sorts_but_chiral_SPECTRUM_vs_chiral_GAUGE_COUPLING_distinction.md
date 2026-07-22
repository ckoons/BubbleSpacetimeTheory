# F639 — Placed the fermion in the chambers (pull 07-22i), and it forces a distinction the arc has been blurring: **CHIRAL SPECTRUM ≠ CHIRAL GAUGE COUPLING.** The branching is clean: **SO(5,2) spinor 8 = 4_{c=+1/2} ⊕ 4_{c=−1/2}** under SO(5)×SO(2) — the two spacetime-chirality halves at OPPOSITE SO(2)-charge. Born=Bergman keeps the positive-energy (c=+1/2, holomorphic, q=0) sector = ONE chirality-convention (all-left Weyl); the c=−1/2 sector = the CPT/antiparticle side. And within the surviving +1/2 sector, the SO(4) branching gives **(2,1)⊕(1,2) = SU(2)_L-doublet ⊕ SU(2)_L-singlet = the SM one-generation content.** So the **fermion CONTENT sorts correctly** (candidate, promising). **BUT** that is a chiral *spectrum*; the actual parity violation is that SU(2)_L couples to the (2,1) **only** — a chiral *gauge coupling* — and the flat reduction gave that VECTOR-like (F636). **Born=Bergman delivering a chiral spectrum does NOT automatically deliver a chiral gauge coupling.** Those are two different things, and only the first is (candidately) in hand. Don't bank "parity closed" — the chiral gauge coupling is still open.

**Lyra, Wed 2026-07-22 ~11:58. Pull 07-22i. Computed the placement; it sorts the content but exposes that the coupling-chirality is a separate, still-open leg. Compute-don't-assert.**

## The branching (computed)
SO(5,2) spinor = 8-dim (g=7 odd, irreducible). Weights (±½,±½,±½) in (e_1,e_2,e_3); e_1 = SO(2)-charge. Split by e_1:
$$ \mathbf{8} = \underbrace{\mathbf{4}_{c=+1/2}}_{(+½,\,±½,±½)} \ \oplus\ \underbrace{\mathbf{4}_{c=-1/2}}_{(-½,\,±½,±½)} \quad\text{under } SO(5)\times SO(2), $$
each **4** an SO(5)=B_2 spinor (½,½) at SO(2)-charge ±½. **The two spacetime chiralities sit at OPPOSITE conformal charge** — which is exactly why the SO(2) energy-positivity can select one: it's not a group-orientation, it's a sign-of-energy split (the correct role, F637).

## Chamber placement (F638 formula) + the CPT reading
- **4_{c=+1/2}:** c=+½ > −½ → **q=0 → holomorphic** (Bergman/Hardy), chirality +. **The physical positive-energy sector.** Kept by Born=Bergman.
- **4_{c=−1/2}:** c=−½ sits on the first wall (c+½=0, singular) → the **negative-energy / CPT-conjugate** side (antiparticles). Not an independent physical sector — it's the charge conjugate of the +½ fields.
So Born=Bergman keeping the +½ holomorphic sector = keeping **one chirality convention** (all-left Weyl fields, with right-handed fields appearing as charge conjugates u_R^c etc.) — standard chiral-fermion bookkeeping. **This is a genuinely chiral SPECTRUM** (net one chirality, matching Elie 4777's ±4, evading flat index-0). ✓ candidate.

## Within the surviving sector: the content DOES sort (the promising part)
The kept 4_{+1/2} is an SO(5) spinor; under SO(4)=SU(2)_L×SU(2)_R it branches
$$ \mathbf{4} \to (\mathbf 2,\mathbf 1)\oplus(\mathbf 1,\mathbf 2) = \text{SU(2)}_L\text{-doublet} \ \oplus\ \text{SU(2)}_L\text{-singlet}. $$
So the holomorphic sector automatically contains **a left-handed doublet AND a left-handed singlet** = the SM one-generation Weyl content (Q_L doublet + u_R^c, d_R^c singlets). **The content sorts to L-doublet/R-singlet.** This is Elie's identification, and it holds at the content level. Promising — candidate.

## ★ The distinction the arc has been blurring (the honest brake)
"The fermions are chiral" (chiral SPECTRUM) and "the weak force is chiral" (chiral GAUGE COUPLING) are **DIFFERENT statements:**
- **Chiral spectrum:** the physical fermions are one-chirality Weyl fields with the right content. **Born=Bergman delivers this (candidate).** ✓
- **Chiral gauge coupling (= parity violation):** SU(2)_L couples to the (2,1) doublet **and not** to the (1,2) singlet. This is a statement about the **gauge connection**, not the fermion spectrum. **The flat reduction gave this VECTOR-like** (F636: internal generators Σ^int = 1⊗σ commute with γ⁵ — they act on both halves equally). Born=Bergman projecting the *spectrum* holomorphically does **not** by itself make the *connection* chiral.
**So even with a perfectly chiral spectrum and correctly-sorted content, parity violation is NOT established until the SU(2)_L connection is shown to couple to (2,1)-only.** That is the self-dual/orientation question (g=7), and F636 found the flat version vector-like. **The chiral gauge coupling is the still-open leg — do not let "the spectrum is chiral / the content sorts" bank as "parity closed."**

## Where that leaves the decisive computation
Two separate things must BOTH hold for parity:
1. **Chiral spectrum + content:** Born=Bergman holomorphic sector = one-chirality Weyl, containing (2,1)⊕(1,2). **Candidate, looks good** (this note + F637/F638 + Elie 4777).
2. **Chiral gauge coupling:** SU(2)_L (self-dual connection) couples to (2,1) only. **OPEN — flat is vector-like (F636); needs the connection on the holomorphic sections, not the flat spinor.** The likely resolution: the gauge connection acting on *holomorphic* sections may couple chirally even though the flat one doesn't — but that must be COMPUTED (the covariant ∂̄ on the fermion bundle), not assumed.

## Honest tier
- **Branching 8 = 4_{+½}⊕4_{−½}, holomorphic sector = one chirality, content = (2,1)⊕(1,2): computed, candidate, promising.**
- **Parity violation (chiral gauge coupling): STILL OPEN** — spectrum-chirality ≠ coupling-chirality; the flat coupling is vector-like. **This is the real remaining leg, and it's distinct from the Dolbeault-index/spectrum question the last three notes addressed.**
- **Do NOT bank parity.** Survivors unchanged (split, CP-free, custodial, charge-row 1/6).

## Tiers / handoffs
- **@Elie** — verify 8 = 4_{+½}⊕4_{−½} (weights (±½,±½,±½) split by e_1) and that the +½ SO(5)-spinor → (2,1)⊕(1,2) under SO(4). Then the NEW decisive harness question, distinct from the spectrum index: **does the SU(2)_L (self-dual) connection, acting on the holomorphic sections (covariant ∂̄ on the fermion bundle), couple to (2,1) only** — i.e. is the *coupling* chiral, not just the spectrum? Flat was vector-like (your 4776); does holomorphic projection change the *coupling*? That's the open leg.
- **@Keeper** — important tiering brake: the arc has been treating "chiral spectrum" (Dolbeault index, Born=Bergman — candidate, good) as if it were "parity violation." It is NOT. Parity = chiral GAUGE COUPLING (SU(2)_L to (2,1)-only), which the flat reduction gave vector-like (F636). The spectrum sorting (this note) is promising and the content is right, but **parity does not close until the coupling-chirality is computed on the holomorphic sections.** Hold candidate; keep the two legs separate on the board.
- **@Grace** — render TWO legs, not one: (1) chiral spectrum + content sorting [Born=Bergman, candidate, promising — 8=4_{+½}⊕4_{−½}, holo sector = (2,1)⊕(1,2)]; (2) chiral gauge coupling = parity [OPEN, flat vector-like]. Don't merge them; parity needs both.
- **@Casey** — placing the fermion in the chambers sorts the *content* beautifully: the surviving holomorphic sector is one-chirality and contains exactly a left doublet + left singlets (the SM generation). But it made a distinction sharp that we'd been gliding over — a chiral *spectrum* (which Born=Bergman gives) is not the same as a chiral *force* (SU(2)_L coupling to the doublet only). The flat coupling was vector-like; whether holomorphic projection makes the *coupling* chiral, not just the spectrum, is the real open leg — and it's a covariant-∂̄-on-the-bundle computation, still to do. Content sorts (candidate); the force being chiral is the piece left. Computed the placement, flagged the distinction; not asserting closure.

Notes only; no toys/theorems claimed. Content sorts (candidate); chiral gauge coupling (parity) OPEN and distinct from the spectrum question. — Lyra
