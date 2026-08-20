# Lane A₂ assist — the 8π⁴ / Wyler contamination sweep (Grace → Keeper, §626, 2026-08-20)
*Keeper owns the sweep; this is my grep-categorization + the one load-bearing finding that matters. §599 control passed.*

## Scope correction
The prompt said "23 files." The real current-corpus count is larger: **63 current `notes/*.md` files cite 8π⁴** (the 139 total includes .bak/.py/.running/JSON — those are frozen, skip). Of the 63, **~15 already carry a retired/Wyler/K676/K680/K1391 flag** (electron-mass Derivation + CanonicalProof, your K1391/K1398/K1729/K1731, Lyra F441, Cal's Majorana-cosign, my Lane-B note) — the retirement DID propagate to those. **~48 are unflagged** → (a) passing mentions get the flag.

## ★ THE LOAD-BEARING FINDING (the one that needs re-audit, not just a flag)
**`BST_BoundaryIntegral_Final.md` (the "BST Yang-Mills mass-gap proof") is DOUBLY contaminated, and one contamination is the dead Route-1 ruler value:**
1. **Retired Wyler used as a FORCING** (lines 259, 484): "n_C=5 forced by the Wyler formula α=1/137 … Any other n_C gives wrong α," and "α = (9/8π⁴)(π⁵/1920)^{1/4} = 1/137.036." This is the RETIRED derivation (K676/K680/K1391) used as a load-bearing forcing of n_C. **n_C=5 survives** (Condition-5, the no-go theorem, the α-gap≈5 — real routes), but the file's SPECIFIC "forced by Wyler" line is stale and must re-cite the genuine forcing.
2. **★ The dead κ_eff = 14/5 is embedded in the mass-gap value** (line 335): `c = κ_eff²/(2g²_B) = (14/5)²/(2·(28π/5)) = 7/(10π)`. **This is the SAME 14/5 = 2g/n_C I killed in Lane B (round 6) — g=7 slid into a metric ratio, against pin K1213.** So the mass-gap constant c = 7/(10π) is built on a Bergman-illegal κ_eff.

**Does the result survive?** This file was ALREADY re-scoped KK-not-Clay (K1714) — it is NOT the interacting Clay mass gap. The two new contaminations (retired-Wyler forcing + dead-14/5 κ_eff) are additional stale pieces in an already-re-scoped file. **Recommendation: fold both into the K1714 re-scope** — the file needs (i) the Wyler-retirement flag on its n_C-forcing, (ii) the K1213 correction on κ_eff=14/5, (iii) the KK-not-Clay banner it already earned. The honest strong-sector wins (AF, N_c=3, a,c anomalies) do NOT ride 8π⁴ or 14/5.

**`BST_MassGap_CPFiber.md`:** line 209 asserts "the Wyler formula … is derived" (stale — retired); lines 255-295 DO acknowledge the Clay gap honestly but still say "α=1/137.036 via the Wyler formula" (line 295). Passing-flag + the one "derived" → "Identified (retired)" fix.

**One line for the index:** a retired *derivation* used as a *forcing* is worse than a passing mention — it manufactures the very input (n_C, α) it claims to force. Grep retired-flags before citing a forcing.
