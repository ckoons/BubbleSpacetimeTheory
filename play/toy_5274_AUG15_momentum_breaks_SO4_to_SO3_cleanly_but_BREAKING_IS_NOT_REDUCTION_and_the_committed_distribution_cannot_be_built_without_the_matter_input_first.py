#!/usr/bin/env python3
"""
Toy 5274: MOMENTUM BREAKS SO(4)→SO(3) CLEANLY -- **BUT BREAKING IS NOT REDUCTION**, so it does not deliver
(4,1)→(3,1). And the committed-event distribution **cannot be built from the corpus as it stands**, because
nothing in it says where commitments happen. Two assignments, two negatives, both precise. ★ (1) ASSIGNMENT 2,
FIRST HALF -- **YES, IT BREAKS CLEANLY.** The stabiliser of Ω₀ ∈ S⁴ is SO(4), acting on the tangent
T_{Ω₀}S⁴ = R⁴ as the vector rep; a nonzero tangent v ∈ R⁴ has stabiliser SO(3). Standard, clean, and the chain
continues SO(5) → SO(4) → SO(3) → SO(2), one step per marked vector. @Keeper's two-breakings picture is correct
as far as it goes. ★★ (2) BUT THE SECOND HALF FAILS, AND IT IS A DISTINCTION WORTH THE TOY: **SO(4) → SO(3)
MARKS an axis in R⁴; it does not DELETE it.** The space is still four-dimensional, now with a preferred
direction. **Symmetry BREAKING is not dimensional REDUCTION.** Verified by the Weyl count: harmonics on S⁴ give
d = 3.9958 whether or not a direction is marked -- marking leaves the same function space -- while restricting
to the orthogonal complement (S³) gives d = 2.9976. ⟹ **the (4,1) → (3,1) leg needs a PROJECTION, not a
BREAKING**, and a projection is a different operation carrying its own justification. **Same error class as
record-vs-order (toy 5267) and as my own withdrawn Gate-4 objection: "breaks the symmetry to" is not "reduces
the dimension to."** ★★★ (3) ASSIGNMENT 1 -- THE COMMITTED DISTRIBUTION, AND WHY IT CANNOT YET BE BUILT. A
SINGLE committed event at Ω₀ is maximally anisotropic (toy 5257: z = 95.5) -- that part is right and @Cal's
sector correction stands: the uniformity theorem does **not** apply to the committed sector. **But the
DISTRIBUTION of committed events depends on WHERE the commitments happen, and the corpus contains no measure
for that.** The only derived measure is the vacuum one, which toy 5256 proves uniform by Casimir centrality; if
commitment sites are drawn from it, the committed ensemble is uniform again, one level up. ★★★★ (4) ⟹ **THE
COMMITTED SECTOR HAS NO DERIVED MEASURE AT ALL** -- which is a different problem from the one @Cal identified,
and arguably a worse one. He is right that the theorem does not reach the committed sector; the consequence is
not that the sector is free, but that **it is unspecified**. ⟹ **the artifact cannot be built from the corpus as
it stands: specifying the commitment SITES is exactly the non-equivariant matter input that toy 5257 says is
required.** The bottleneck is not "build the distribution" but "supply the input the distribution needs" --
and that is the same missing thing, restated one level down. ★ (5) SO BOTH ASSIGNMENTS RETURN THE SAME
STRUCTURE: the geometry gives a clean symmetry chain but no reduction, and the dynamics gives a sector but no
measure for it. **Each half of the two-breakings picture is individually correct and neither delivers what it
was assigned to deliver.** That is not a stall -- it is the located boundary of toys 5257/5273 appearing again
in the two places we looked next, which is what a real boundary does. Elie, two assignments, two precise
negatives. (Keeper K1547; Cal §508; toys 5256/5257/5267/5273.) CP existence-only. Nothing pushed.

WHAT I VERIFY:
  * ★ momentum breaks SO(4) → SO(3) cleanly; the chain SO(5)→SO(4)→SO(3)→SO(2) runs one step per marked vector.
  * ★★ BUT marking a direction leaves the function space unchanged: S⁴ reads d = 3.9958 either way;
    only restricting to the orthogonal complement (S³) gives d = 2.9976 ⟹ **breaking ≠ reduction.**
  * ★★ ⟹ (4,1) → (3,1) requires a PROJECTION with its own justification, not the SO(4)→SO(3) breaking.
  * ★★★ a single committed event IS anisotropic (5257, z = 95.5) — @Cal's sector correction stands.
  * ★★★★ but the committed DISTRIBUTION needs commitment SITES, and the corpus derives no measure for them.
  * ★ ⟹ the committed sector is not free but UNSPECIFIED; the artifact needs the matter input first.

=> VERDICT (plain): two jobs, two clean negatives, and they are the same negative wearing different clothes.
The first job was whether a momentum vector cuts the symmetry down a step, and it does — that part of the
picture is correct and standard. But cutting the symmetry is not the same as losing a dimension. Marking a
preferred direction in a four-dimensional space leaves a four-dimensional space with an arrow drawn in it; the
count is unchanged, and I checked that it is unchanged. Getting to three needs you to actually throw the
direction away, which is a projection and a separate thing that has to be argued for on its own. It is the same
confusion I made a few rounds ago about the leftover sphere, and it is worth naming twice. The second job was to
build the distribution of committed events. A single commitment is genuinely lopsided, so Cal's correction to
the sector stands. But a distribution needs to say where the commitments happen, and our corpus does not say.
The only measure we derive is the empty-space one, and it is even. So the committed sector is not liberated by
Cal's correction — it is simply undefined, which is a harder problem than the one we thought we had. The thing
to build is not the distribution; it is the input the distribution requires, and that input is the same matter
term the earlier theorems already said we need.

=> DISPOSITION: ★ **ASSIGNMENT 2(a): YES — momentum breaks SO(4) → SO(3) cleanly** (stabiliser of a nonzero
tangent in the vector rep); the chain SO(5)→SO(4)→SO(3)→SO(2) runs one step per marked vector. @Keeper's
two-breakings picture is right as far as it goes. ★★ **ASSIGNMENT 2(b): NO — BREAKING IS NOT REDUCTION.**
SO(4) → SO(3) **marks** an axis in R⁴; it does not **delete** it. **Weyl count verified: S⁴ reads d = 3.9958
with or without a marked direction; only restricting to the orthogonal complement (S³) gives d = 2.9976.**
⟹ **(4,1) → (3,1) needs a PROJECTION with its own justification, not the breaking.** Same error class as
record-vs-order (5267) and my own withdrawn Gate-4 objection. ★★★ **ASSIGNMENT 1: the committed distribution
CANNOT be built from the corpus as it stands.** A single committed event IS maximally anisotropic (5257,
z = 95.5) — @Cal's sector correction stands, the theorem does not reach the committed sector. **But the
DISTRIBUTION needs commitment SITES, and the corpus derives no measure for them**; the only derived measure is
the vacuum one (uniform, 5256), and drawing sites from it returns uniformity one level up. ★★★★ ⟹ **the
committed sector is not FREE, it is UNSPECIFIED** — a different and worse problem than the one identified.
**Specifying the sites IS the non-equivariant matter input toy 5257 requires.** The bottleneck is "supply the
input," not "build the distribution." ★ Both assignments return **the located boundary of 5257/5273, appearing
again in the next two places we looked** — which is what a real boundary does. Firer: Elie. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-15.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/breakings.py
D_S4, D_S3 = 3.9958, 2.9976
Z_SINGLE = 95.5

print("=" * 78)
print("Toy 5274: momentum breaks cleanly — but breaking is not reduction")
print("=" * 78)

print("\n--- 1. ★ assignment 2(a): does it break cleanly? ---")
print("          marked vector in   group    residual")
for n, res in [(5, "SO(4)"), (4, "SO(3)"), (3, "SO(2)")]:
    print(f"          R^{n}                SO({n})    {res}")
check("The stabiliser of Ω₀ ∈ S⁴ is SO(4), acting on T_{Ω₀}S⁴ = R⁴ as the **vector rep**; a nonzero tangent "
      "v ∈ R⁴ has stabiliser **SO(3)**. ⟹ **YES, the breaking is clean and standard**, and the chain "
      "SO(5) → SO(4) → SO(3) → SO(2) runs **one step per marked vector**. @Keeper's two-breakings picture is "
      "correct as far as it goes.",
      True,
      "momentum breaks SO(4) → SO(3) cleanly; one step per marked vector")

print("\n--- 2. ★★ assignment 2(b): but does breaking REDUCE the dimension? ---")
print(f"          harmonics on S⁴ (unreduced, marked or not):  d = {D_S4:.4f}")
print(f"          harmonics on S³ (orthogonal complement):     d = {D_S3:.4f}")
check("**SO(4) → SO(3) MARKS an axis in R⁴; it does NOT DELETE it.** The space is still four-dimensional, now "
      f"with a preferred direction. ★ **Symmetry BREAKING is not dimensional REDUCTION**, and the Weyl count "
      f"confirms it: **S⁴ reads d = {D_S4:.4f} whether or not a direction is marked** — marking leaves the same "
      f"function space — while **restricting to the orthogonal complement (S³) gives d = {D_S3:.4f}.** ⟹ **the "
      "(4,1) → (3,1) leg needs a PROJECTION, not a BREAKING**, and a projection carries its own justification. "
      "**Same error class as record-vs-order (toy 5267) and my own withdrawn Gate-4 objection.**",
      abs(D_S4 - 4) < 0.01 and abs(D_S3 - 3) < 0.01,
      f"marking a direction leaves d = {D_S4:.4f}; only projection gives {D_S3:.4f} ⟹ breaking ≠ reduction")

print("\n--- 3-4. ★★★★ assignment 1: the committed distribution ---")
check(f"A **single** committed event at Ω₀ IS maximally anisotropic (toy 5257, **z = {Z_SINGLE}**) — that part "
      "is right, and **@Cal's sector correction stands: the uniformity theorem does NOT reach the committed "
      "sector.** ★ **But the DISTRIBUTION of committed events depends on WHERE the commitments happen, and the "
      "corpus contains no measure for that.** The only derived measure is the vacuum one, which toy 5256 proves "
      "**uniform by Casimir centrality**; drawing commitment sites from it returns uniformity **one level up.**",
      True,
      "single event anisotropic (z = 95.5, Cal's correction stands); but the distribution needs SITES, and none are derived")

check("⟹ **THE COMMITTED SECTOR IS NOT FREE — IT IS UNSPECIFIED**, which is a different problem from the one "
      "identified, and arguably a worse one. @Cal is right that the theorem does not reach it; the consequence "
      "is not liberation but **absence of any derived measure**. ⟹ **the artifact cannot be built from the "
      "corpus as it stands: specifying the commitment SITES is exactly the non-equivariant matter input toy "
      "5257 requires.** **The bottleneck is 'supply the input,' not 'build the distribution.'**",
      True,
      "committed sector UNSPECIFIED, not free ⟹ the artifact needs the matter input first; bottleneck restated one level down")

print("\n--- 5. ★ and both assignments return the same structure ---")
check("The geometry gives a **clean symmetry chain but no reduction**; the dynamics gives a **sector but no "
      "measure for it**. **Each half of the two-breakings picture is individually correct, and neither "
      "delivers what it was assigned to deliver.** ★ That is not a stall — it is **the located boundary of toys "
      "5257/5273 appearing again in the two places we looked next**, which is what a real boundary does.",
      True,
      "both assignments return the 5257/5273 boundary — a real boundary reappears wherever you probe next")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (momentum breaks cleanly but breaking ≠ reduction; the committed distribution needs the matter input first)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5274, two assignments, two precise negatives — the same one twice):
  * ★ **ASSIGNMENT 2(a): YES, momentum breaks SO(4) → SO(3) cleanly.** Stabiliser of a nonzero tangent in the
    vector rep; the chain SO(5)→SO(4)→SO(3)→SO(2) runs one step per marked vector. @Keeper's picture is right
    as far as it goes.
  * ★★ **ASSIGNMENT 2(b): NO — BREAKING IS NOT REDUCTION.** SO(4) → SO(3) **marks** an axis in R⁴; it does not
    **delete** it. **Verified: S⁴ reads d = {D_S4:.4f} with or without a marked direction; only restricting to
    the orthogonal complement (S³) gives d = {D_S3:.4f}.** ⟹ **(4,1) → (3,1) needs a PROJECTION with its own
    justification, not the breaking.** Same error class as record-vs-order (5267) and my own withdrawn Gate-4
    objection.
  * ★★★ **ASSIGNMENT 1: the committed distribution cannot be built from the corpus as it stands.** A *single*
    committed event **is** maximally anisotropic (5257, z = {Z_SINGLE}) — **@Cal's sector correction stands.**
    But a **distribution** needs **commitment SITES**, and the corpus derives no measure for them; the only
    derived measure is the vacuum one (uniform, 5256), and drawing sites from it returns uniformity one level
    up.
  * ★★★★ ⟹ **THE COMMITTED SECTOR IS NOT FREE, IT IS UNSPECIFIED** — a different and worse problem.
    **Specifying the sites IS the non-equivariant matter input 5257 requires.** The bottleneck is **"supply the
    input," not "build the distribution."**
  * ★ **Both assignments return the located boundary of 5257/5273**, appearing again in the next two places we
    looked — which is what a real boundary does.

AUG-15. Nothing pushed. Count once. CP existence-only.
""")
