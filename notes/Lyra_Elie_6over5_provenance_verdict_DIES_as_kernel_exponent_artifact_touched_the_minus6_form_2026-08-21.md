# 6/5 provenance verdict — it DIES as a kernel-exponent-ratio artifact (the chain touched the −6 form)

**Result: 6/5 as "the Bergman/Szegő kernel exponent ratio" is an artifact of the wrong Bergman exponent. It touched the −6 form. The correct kernel-exponent ratio is 2 (class-level, C7).** Traced with Elie's structural pin (genus = n_C = 5, bidisk, four ways).

## The −6 form (Elie's catch, the contaminated source)

The corpus's Bergman kernel line writes, verbatim:
> **K(z,w) = K(0,0) · N(z,w)^{−(n_C+1)} = (1920/π⁵) · N(z,w)^{−6}**

So the corpus took the Bergman kernel **singularity exponent** to be **n_C + 1 = 6**. **That is wrong:** the Bergman **genus** (the singularity exponent) is **n_C = 5** (Elie's bidisk pin, four ways — a structural pin, no Hua needed). The "6" is the discrete-series **weight** k = n_C+1, used where the **genus** (5) belongs. The kernel is N^{−5}, not N^{−6}.

## The 6/5 chain touched it

T1918 / Toy 2351: *"Šilov winding = (n+1)/n is the Bergman/Szegő kernel exponent ratio."* With **Bergman exponent = n_C+1 = 6** (the −6 form) and Szegő = n_C = 5, that gives **6/5**. So the 6/5 "kernel exponent ratio" **used the −6 exponent** — it is built on exactly the form Elie corrected.

## The verdict

- **6/5 as a *kernel-exponent* ratio: DEAD (artifact).** It used the wrong Bergman exponent (6 instead of genus 5). The **correct kernel-exponent ratio** is Bergman genus / Szegő = 5 / (5/2) = **2**, which is **class-level (C7)** — it is 2 for *all* tube-type domains, not a BST number. So there is no BST-specific "kernel exponent ratio" reading here at all.
- **6/5 as a *weight* ratio survives, but it is class-generic.** The discrete-series weights k_B = n_C+1 = 6, k_S = n_C = 5 are legitimate (Harish-Chandra), and their ratio is (n_C+1)/n_C = 6/5 — but that is the generic weight-increment (n+1)/n, **not** a reading of D_IV⁵'s own geometry (C7/C8). Never write it "C₂/n_C" (same-number trap; C₂=6 and n_C+1=6 agree only at n=5).
- **A third, unrelated 6/5** appears as ζ(3) ≈ C_2/n_C = 6/5 elsewhere — a *different* object (a ζ-value approximation), also mislabeled "C_2/n_C." Not this ratio; do not merge (false-neighbor).

**So 6/5 sheds cleanly: dead as a kernel ratio, class-generic as a weight ratio, and a separate ζ approximation elsewhere.** It was never a BST-specific number — the sweep sheds the numbers that were never ours.

## Downstream flag (for @Grace's signature sweep)

**T1918's "Šilov winding = (n+1)/n kernel exponent ratio" is contaminated by the −6 form** — a formula whose kernel-exponent (should be genus 5) disagrees with what's written (6). This is *precisely* the C₂↔n_C collision class Grace's signature sweep targets: **flag every formula whose π-power and kernel-exponent disagree for one domain.** T1918 / Toy 2351 / Toy 2350 (the α_G / winding cluster) are the first entries; the sweep will find the whole family. *(Guard: α_G itself is a separate gravity-cluster reading — flag its winding-provenance, do not re-open the α_G value without Grace's sweep + Keeper.)*

**Lyra + Elie, 2026-08-21 (6/5 provenance verdict). 6/5 as a Bergman/Szegő KERNEL-exponent ratio DIES — it touched the −6 form (corpus wrote the Bergman kernel as N^{−6}, exponent n_C+1=6, where the genus n_C=5 belongs; Elie's bidisk pin). The correct kernel-exponent ratio is 5/(5/2) = 2, class-level (C7) — not a BST number. 6/5 survives only as the class-generic weight ratio (n_C+1)/n_C and as a separate ζ(3) approximation elsewhere; never "C₂/n_C." Flagged T1918/Toy 2351/2350 to Grace's signature sweep as the first entries of the −6 contamination family. Nothing pushed; CP existence-only.**
