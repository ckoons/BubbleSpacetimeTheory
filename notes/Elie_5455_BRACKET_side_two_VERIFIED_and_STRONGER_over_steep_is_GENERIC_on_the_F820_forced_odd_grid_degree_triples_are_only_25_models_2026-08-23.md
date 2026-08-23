# Elie 5455 — the BRACKET's SIDE TWO: verified, run backwards, and **stronger than stated**

**Toy 5455, 2026-08-23. Rubric cell: External 3 (SM params) / lepton hierarchy. Score 15/15.**
**Scope: I verify Keeper's SIDE TWO and test the robustness of his sign. I do NOT touch the residue gate — that is pinned behind Lyra's {object} × {exponent} pin (R63 Sec 1 rule 1) and I compute only after the pin is FILED.**

I supplied SIDE ONE (5454). Nobody had checked SIDE TWO, and **a bracket is only as good as its weaker side.**

## 1. Keeper's numbers reproduce exactly

Quark anchor: (3)₁ = 3, (3)₃ = 60, (3)₅ = 2520 → **1 : 20 : 840**, m_s/m_d = 20. ✓

| quantity | Keeper (R63) | mine (dps 40) |
|---|---|---|
| ν_lep from m_μ/m_e alone | 12.888130 | **12.88812993** ✓ |
| predicted m_τ/m_e | 55 480.23 | **55 480.2317** ✓ |
| observed m_τ/m_e | 3 477.23 | 3 477.2298 ✓ |
| miss factor | 16.0× | **15.955×** ✓ |

## 2. ★ It survives being run backwards — which it owed and had not been shown

Reporting **one** direction of a two-target test is a **selection** unless the other is shown.

- **Forward** (fix ν on the muon, predict the tau): over-predicts by **15.96×**
- **Reverse** (fix ν on the tau, predict the muon): ν = 2.9696, predicts m_μ/m_e = 45.46 vs 206.77 — misses by **4.55×**, **in the same sense (too steep)**
- **Best simultaneous fit** (minimize worst-case log error, the kindest possible reading): **still 2.65× off**

> **The miss is not a direction artefact.** A two-sided miss with a consistent sense is a structural statement.

## 3. ★★ The degree-triple family is a REPARAMETERIZATION — only the GAPS matter

**(ν)_b/(ν)_a = (ν+a)(ν+a+1)···(ν+b−1)** — a product of (b−a) consecutive terms starting at ν+a.
So **(a,b,c) → (a+1,b+1,c+1) with ν → ν−1 gives identical ratios.** The model depends only on the
gap pair **(b−a, c−a)**, never on the absolute degrees.

> **73 admissible triples from degrees 1..9 are only 25 INDEPENDENT MODELS.**
> Any look-elsewhere count taken over *degree triples* **overcounts by ~2.9×**. Report gap-classes.

This matters directly for R63 rule 5 ("if you enumerate, report the FULL sweep") — the full sweep is
much smaller than it looks, and a family whose members are related by a coordinate shift is not a family.

## 4. ★★★ THE MAIN RESULT — on the forced grid, over-steepness is GENERIC

Raw enumeration first, honestly: **13 of 73 triples (4 of 25 gap-classes) are UNDER-steep.** Taken at face
value that would scope side two to the quark pattern. **It does not, and here is why.**

**Read from the primary, not recalled** — F820 (Lyra, 2026-08-05, K1180), verified in the file:
**m = N_c·|Q|**, so a charged lepton has weight **m = 3 (odd)**; the F817 parity lock is **k ≡ m (mod 2)**;
therefore **charged leptons live on the ODD degree grid {1,3,5}** — forced, target-innocent.

**All-odd degrees ⟹ every gap is EVEN.** So the odd grid admits only even gap-classes:

| gap-class | example (odd degrees) | miss factor | direction |
|---|---|---|---|
| (2,4) | **{1,3,5}** — the quark pattern | 15.96× | OVER-steep |
| (4,6) | {1,5,7} | **2.86×** ← closest the allowed grid gets | OVER-steep |
| (2,6) | {1,3,7} | 5 391× | OVER-steep |
| (4,8) | {1,5,9} | 229× | OVER-steep |
| (2,8) | {1,3,9} | 2.24×10⁶ | OVER-steep |

**Every UNDER-steep class — (2,3), (3,4), (4,5), (5,6) — has an ODD gap, hence requires an EVEN degree,
which F820's parity forcing EXCLUDES for charged leptons.**

> ### ⟹ **UNDER-STEEP CLASSES ON THE ODD GRID: NONE.**
> **Side two is stronger than Keeper stated it.** Not *"too steep at the quark's odd-degree pattern"* but
> **"too steep at EVERY degree pattern the parity forcing allows."** The bracket's second side is **generic
> on the allowed grid**, and the best the grid can do is still **2.86× over**.

The scope caveat in his wording turns out to be unnecessary — but only because a *separate banked forcing*
(F820) supplies it. **The caveat should be replaced by the citation, not simply dropped.**

## 5. Housekeeping — an assignment F820 left open to me is already closed

F820 line 29 assigns me the blind up-mass check at the even grid {0,2,4}. **Verified by the object, not
assumed:** `toy_5060_AUG05_K1180_up_tower_even_grid_FK_ladder_does_NOT_reproduce_top_heavy_up_masses_
decisive_check_NEGATIVE_...` — run 2026-08-05, **NEGATIVE**, up sector is not FK-forced. Closed.

## 6. What I did NOT do

**The residue gate.** R63 Sec 1 rule 1 pins it behind Lyra's written {norm object} × {exponent} pin, and
Lyra proved p\* is **unique** — so a gate of this shape always produces the number at exactly one p, and the
only question is whether the **pinned** p equals p\*. **I compute after the pin is filed, not before.**
No degree pattern above is claimed as a mechanism; Part C/D is a **scope check on a banked claim, not a hunt**
(K1684), and the full enumeration is printed precisely so nobody — including me — can pick the closest.

**Elie, 2026-08-23. Toy 5455, 15/15. Keeper's SIDE TWO reproduces exactly (ν_lep=12.88812993, predicted m_τ/m_e=55,480.23, miss 15.96×) and SURVIVES REVERSAL (4.55× the other way, same sense; best simultaneous fit still 2.65× — not a direction artefact). Two structural findings: (i) degree "triples" are a reparameterization — only the GAPS matter, so 73 triples are 25 independent models and a triple-based look-elsewhere overcounts ~2.9×; (ii) every UNDER-steep gap-class requires an ODD gap hence an EVEN degree, which F820's parity forcing (m=N_c|Q|=3 odd + F817 k≡m mod 2, read from the primary) EXCLUDES for charged leptons ⟹ OVER-STEEPNESS IS GENERIC ON THE FORCED ODD GRID, best case still 2.86× over. Side two is stronger than stated; replace the scope caveat with the F820 citation. Residue gate untouched — waits on Lyra's pin. Nothing pushed.**
