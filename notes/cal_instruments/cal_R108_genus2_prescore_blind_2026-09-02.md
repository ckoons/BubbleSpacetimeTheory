# Cal — GENUS-2 PRE-SCORE, written BLIND (no genus-2 numbers exist on disk; K1851 §2 and Lyra's torsor note NOT yet read by me) — 2026-09-02 16:4x EDT
Frame: closed orientable genus-2 triangulations (Lutz/HLZ census, n = 10 minimal; Grace pins the count to arXiv math/0507592). Record = Heawood face signs; Φ_r: π₁(Σ₂) → A₄ the flat torsor of a closed record (Lyra); θ = Φ_r mod V ∈ Hom(π₁, ℤ₃); realized ⟺ Φ_r trivial; sheets of the derived cover = |image Φ_r|.

## A. Positions (group theory; cannot be tuned)
- |Hom(π₁Σ_g, A₄)| = 12^{2g−1}(3 + 3^{2−2g}) (Frobenius–Mednykh). g=1: 48. g=2: 5,376. g=3: 749,568. Recomputed here from the irreps of A₄ (dims 1,1,1,3).
- |image Φ_r| ∈ {1, 2, 3, 4, 12}; 6 is impossible (A₄ has no subgroup of order 6). If a 6 appears, the INSTRUMENT is wrong — this is a control, not a finding.
- Torus control is a THEOREM's zero: π₁(T²) abelian ⟹ image abelian ⟹ |image| ≤ 4; a torus can never show 12. Sphere control: image 1 only (Lemma R).
- Under equidistribution over Hom (counted with multiplicity — the convention the g = 1 one-generator measurement log₂ 12 = log₂|Hom(ℤ, A₄)| pins; equidistribution over CONJUGACY CLASSES would have given log₂ 4), the genus-2 null vector by |image| is:
    |image| = 1 : 1        share 0.0002
    |image| = 2 : 45       share 0.0084   (3 subgroups × 15 surjections ℤ⁴ → ℤ₂)
    |image| = 3 : 320      share 0.0595   (4 subgroups × 80 surjections ℤ⁴ → ℤ₃)
    |image| = 4 : 210      share 0.0391   (V: 256 − 46)
    |image| = 12: 4,800    share 0.8929
  D_null = log₂ 5376 = 12.392 bits. Staged: N_{θ=0} = |Hom(π₁, V)| = 256, so D1_null = log₂(5376/256) = 4.392 and D2_null = log₂ 256 = 8.000.
- THE SEPARATING NUMBER. The rival reading "cost = product of the two cohomology-group orders" predicts |H¹(Σ₂;ℤ₃)| · |H¹(Σ₂;V)| = 81 · 256 = 20,736 → 14.340 bits, with D1 → log₂ 81 = 6.340. Mednykh predicts 12.392 with D1 → 4.392. They part company by 1.95 bits, all of it in the θ-stage. Equivalent sharp observable: under the A₄-null the θ-classes are NOT equidistributed — N_{θ=0} : N_{θ=c≠0} = 256 : 64 = 4 : 1 (trivial θ is four times as likely as any fixed nonzero θ), whereas the pure-ℤ₃ null predicts 1 : 1. The same 4 : 1 is predicted at g = 1 with two free generators (16 : 4 of 48; share(θ=0) → 1/3, not 1/9) — Grace's "trending to 48" data already contains this check for free; report it.

## B. Values (finite-size; a number at n = 10 is not the position)
- D at n = 10 is a VALUE. Every cycle is short at n = 10; on T(a,3) the short generator's holonomy was forced trivial exponentially (Grace 5631). Pre-registered DIRECTION of the finite-size deviation: toward trivial holonomy — D(n=10) < 12.392 and share(|image| = 12) < 0.893, with share(image ⊆ V) and share(θ = 0) ABOVE the null. Size not predicted. A deviation in the OTHER direction (D above 12.39, image-12 share above 0.893) is unexplained by the mechanism and gets flagged.
- No genus-2 family with growing n exists yet; without one, nothing at genus 2 can KILL the Mednykh reading tonight. What tonight can do: (i) exhibit image-12 records (existence); (ii) compare the five-class share vector to the null and to the deviation direction; (iii) measure the 4 : 1 θ-ratio, which is finite-size-robust relative to D itself (same triangulation, same short cycles, ratio of two counts).

## C. The empty-confirmation map for the "12-sheet witness"
GUARANTEED BY CONSTRUCTION (report as checks, never as findings):
  1. A record is realized on the derived cover of ker Φ_r — pullback of a homomorphism to its own kernel is trivial. True at every genus. In the TORSOR formulation, "One-Floor" is a tautology.
  2. The sheet count equals |image Φ_r|.
  3. Torus never shows 12; sphere shows 1 only (theorems, above).
CONTENT (can fail; these are the findings):
  4. EXISTENCE of an image-12 record at genus 2. The null predicts they are the MAJORITY (0.893). One such record kills the STAGED One-Floor Lemma as stated on "closed orientable surfaces": its θ-cover (3 sheets) still carries a nonzero V-class, so the staged tower has height 2 (3 then 4 sheets). This is the genus-2 kill I pre-registered in §828 §5, now with a predicted count instead of "unknown."
  5. The share vector vs the null (A) and the deviation direction (B).
  6. The θ-ratio 4 : 1 (A) — the observable that separates the A₄-torsor null from a ℤ₃-cohomology null at n = 10 without a family.
THE CONFLATION TO REFUSE: "One-Floor" in the torsor formulation is EMPTY (item 1) and in the staged formulation is predicted FALSE at genus 2 (item 4). Neither may be written as a genus-2 result. What survives as a theorem is the TORUS statement, and it has a one-line group-theoretic proof that replaces my deck-isotopy sketch: the image of ℤ² is an abelian subgroup of A₄; if θ ≠ 0 it contains an element of order 3, whose centralizer in A₄ is just ⟨itself⟩ ≅ ℤ₃; so image = ℤ₃ and the V-part is trivial. Same conclusion, no isotopy, and it is exactly WHY the torus never sees 12.

## D. What I will call each outcome
- Image-12 records found, shares within the deviation direction of the null, θ-ratio near 4:1 → "genus-2 existence PASS; the null's shape confirmed at n = 10; the position 12.392 remains a prediction for a family." No "solved," no "predicted 5,376" in prose — 5,376 is |Hom|, not a count of anything measured.
- No image-12 record on any 4-colorable genus-2 triangulation → the null is WRONG at genus 2 in the one place it is most confident; report as the day's result with its witness (the triangulation list).
- θ-ratio near 1:1 → the record→torsor map does not equidistribute over Hom; the Mednykh reading loses its null; report, do not rescue.
- Any 6 → instrument.
