# F615 — CP is a commutator, and the rank-1 condensate DERIVES its smallness. J ∝ det[H_u,H_d]; at rank-1 (single condensate) the commutator is rank-2 → det = 0 → J = 0. So CP VANISHES at leading order and is a purely subleading off-rank-1 effect — structurally explaining why J_CKM ≈ 3×10⁻⁵ is tiny, before computing it. And it predicts CKM CP ≪ PMNS CP (quark sector rank-1-suppressed; neutrino sector rank-2, not) — matching J_CKM tiny vs δ_PMNS ~ maximal. Smallness DERIVED; the value of J still needs the corrections.

**Lyra, Mon 2026-07-20 (new row, CP).** Casey: "what do you think?" — CP-as-commutator is the right framing, and the rank-1 structure we already built pays off cleanly. It *derives* the smallness of CP. Here it is, with the discipline lines held.

## The framing (right, and rephasing-invariant)
CP violation is the Jarlskog invariant J, and with H_u = M_u M_u†, H_d = M_d M_d† (the up/down Hermitian mass-squared matrices):
$$ J \;\propto\; \det[H_u, H_d], \qquad \text{CP} \ne 0 \iff [H_u, H_d] \ne 0. $$
CP is exactly the part of flavor that **can't be rotated away** — the mixing angles are the misalignment (rotatable, Tier-2, slippery), the commutator is the invariant. **This is the right object** (rephasing-invariant J, not the parameterization-dependent δ — the discipline line Elie/Grace set; the old "δ=2/7" was a single-ratio coincidence risk, J is physical). Geometric shadow: |J| = 2× the unitarity-triangle area.

## ★ The derived result — the single condensate forces J = 0 at leading order
The mass matrices are **rank-1** at leading order (single condensate O, F585/F602): M = a⊗b. Then H = M M† = |b|²(a a†) — a **rank-1 projector**. The commutator of two rank-1 projectors:
$$ [H_u, H_d] \propto [a_u a_u^\dagger,\, a_d a_d^\dagger] $$
is supported on span{a_u, a_d} — **rank ≤ 2**. A 3×3 rank-2 matrix has **det = 0**. Therefore:
$$ \boxed{\;\text{rank-1 condensate} \;\Rightarrow\; \det[H_u,H_d] = 0 \;\Rightarrow\; J = 0. \;}$$
**Verified numerically:** rank-1 M's → [H_u,H_d] rank 2 → det ≈ 0 (J=0); rank-1 + corrections → full rank → det ≠ 0 (J≠0). So **CP vanishes at leading order and is ENTIRELY a subleading off-rank-1 effect.**

**This structurally explains why J_CKM ≈ 3×10⁻⁵ is tiny — DERIVED, before computing the value.** CP is *doubly* suppressed: it needs (i) the corrections that lift M to full rank (break the rank-1 alignment) AND (ii) all three generations non-degenerate. That's the "framework explains CP smallness before you compute it" payoff — and it's real linear algebra, not a frame.

## ★ Structural prediction — CKM CP ≪ PMNS CP (matches the data)
The quark sector: both M_u, M_d are rank-1 (single condensate) → J_CKM is rank-1-*suppressed* → tiny (~10⁻⁵). ✓
The neutrino sector: the Majorana mass is **rank-2** (F589: m₁=0, two nonzero) — a *different* structure, **not rank-1-suppressed** the same way → PMNS CP is **parametrically larger.** So the framework structurally predicts **CKM CP ≪ PMNS CP** — which matches: J_CKM ~ 3×10⁻⁵ (tiny) vs δ_PMNS ~ maximal (the T2K/NOvA hint of near −π/2). **Tier: STRUCTURAL** — a qualitative derived distinction (the rank difference explains the CKM/PMNS CP hierarchy), consistent with the maximal-PMNS-CP hint. That hint (δ_PMNS ≈ −π/2) is a near-term falsifier (like FA#7): if the neutrino-sector CP is *not* large, the rank-structure story is wrong.

## Discipline (held)
- **DERIVED:** CP smallness (J=0 at rank-1; CP purely subleading). This is the genuine new result of the row.
- **NOT derived (yet):** the *value* of J_CKM (≈3×10⁻⁵) — that needs the off-rank-1 corrections computed (the same corrections that give charm/up masses + the CKM angles). Structurally it's a product of mass-splittings × the correction-misalignment; the smallness is explained, the number is not free.
- **Invariant, not phase:** working with J (rephasing-invariant), not δ (parameterization-dependent). The old δ=2/7 lead is superseded by the invariant — don't resurrect the single-ratio.
- **PMNS ≫ CKM: STRUCTURAL** (rank difference), consistent with data; δ_PMNS≈−π/2 = falsifiable.

## The unification (why this is the clean "easier" case)
Flavor = the SVD of one overlap matrix (the rank-1 condensate O + corrections): **masses = radial Σ (done), mixings = angular U/V (done), CP = the commutator/phase (this).** All three from one object. And CP's smallness is *structural*: at rank-1 both mass matrices are the same object → they commute (in the det sense) → no CP; CP only appears when the corrections break the alignment. Three readings of one condensate, and the third (CP) comes out small *for free*.

## Tiers / handoffs
- **CP = commutator J∝det[H_u,H_d]: correct framing** (rephasing-invariant).
- **★ J=0 at rank-1 → CP smallness: DERIVED** (linear algebra; verified). The row's genuine new result.
- **CKM CP ≪ PMNS CP: STRUCTURAL** (rank-1 quark vs rank-2 neutrino); matches data; δ_PMNS≈−π/2 falsifiable.
- **Value of J_CKM (3×10⁻⁵): NOT derived** — needs the off-rank-1 corrections.
- **@Cal** — the derived claim is CP *smallness* (J=0 at rank-1, verified), NOT the value; it's the invariant J not δ; the CKM≪PMNS is structural (rank difference). Don't let it read as "J computed" — the value needs the corrections. The δ_PMNS≈−π/2 is a legitimate near-term falsifier.
- **@Elie** — verify: rank-1 M's → det[H_u,H_d]=0 (J=0); corrections → J≠0. Then the real target: does the *off-rank-1 correction structure* (from the same condensate) give J_CKM ~ 3×10⁻⁵? That's the value computation — the corrections are the charm/up-mass + CKM-angle corrections you're already handling.
- **@Keeper** — new row banked honestly: CP smallness DERIVED (rank-1 → J=0); CKM≪PMNS structural; J value not derived; δ_PMNS maximal = falsifiable. Flavor now = one condensate, three readings (mass/mixing/CP), with CP's smallness structural.
- **@Grace** — render: CP = the commutator (can't rotate away); J=0 at rank-1 → CP is the corrections' misalignment; |J|=2×triangle-area; CKM≪PMNS from the rank difference; δ_PMNS≈−π/2 falsifier.

Notes only; no toys/theorems claimed. — Lyra
