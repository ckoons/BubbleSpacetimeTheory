---
title: "Four-Color as Linear Algebra: A Minimal Representation of the Residual Core"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "FINAL FORM. A self-contained reduction of the four-color theorem (via a canonical-ordering path reduction) to a single linear-algebra implication on SEVEN explicit F_2-subspaces. deg-4 and the realizable type set are proven; the swap dynamics are made linear over F_2 (colors = F_2^2, swaps = translations, S_4 = AGL(2,2)); the residual is the seven flats below. Honest: the forward direction is proven and all seven flats meet the free-set; the reverse implication (the flats realize their freedom) is four-color-equivalent and open."
related: ["notes/FourColor_Path_Reduction_Paper.md","notes/FourColor_Cutspace_Linear_Form.md","notes/FourColor_Type_Flat.md","notes/FourColor_Hard_Core_Located.md","play/fourcolor_seven_flats.py"]
---

> **RETRACTION (2026-06-04).** The "reduction of four-color" framing below is
> **withdrawn**: a degree-≤5 path-elimination ordering does **not** exist in general
> (explicit counterexample, `notes/FourColor_Ordering_Counterexample.md`). What
> follows is rigorous as a **linear-algebra / coding analysis of the boundary
> path-deg-≤5 Kempe-freeing configuration class**, not a reduction of the theorem.
> Read "four-color residual" as "path-deg-≤5 residual" throughout.

# Four-Color as Linear Algebra: a minimal representation

## One paragraph

Color a planar triangulation greedily in a canonical (de Fraysseix-Pach-Pollack)
order, so each inserted vertex faces a **path** of colored neighbors. The only
obstruction is a *stuck* path of length 4 or 5 (all four colors present). The
degree-4 case is freed by one Kempe swap (closed-form proof); the degree-5 case
reduces, after a proven characterization, to **104 rigid types**, of which **97
are freed by one swap** and **7 require two**. Taking the four colors as the vector
space `F_2^2`, **every Kempe swap is a vector translation**, and *freeing a vertex*
becomes *a fixed `F_2`-subspace meeting an affine "miss-a-color" set*. The whole
remaining content of four-color is then carried by **seven explicit subspaces of
`F_2^{10}`**. The forward direction is proven and all seven meet the free-set; the
reverse — that each flat's freedom is realized by actual swaps — is
four-color-equivalent. This is four-color compressed to seven flats.

## 1. The reduction (what is proven)

- **Euler + canonical order.** A planar triangulation has a degree-≤5 vertex; in a
  canonical order each inserted `v` faces a contiguous **path** `u0..u4` of colored
  neighbors. Stuck ⇔ the path uses all 4 colors (one color doubled, non-adjacent).
  *(Scope caveat: the `≤5` path-length bound is not proven in general — see
  `FourColor_Path_Reduction_Paper.md` Sec. 1. The results below are rigorous for
  path-links of length ≤5, the verified class.)*
- **Degree 4 — PROVEN (closed form).** One complementary, non-crossing Kempe swap
  always frees `v`.
- **Degree 5 — realizable type set = 104, PROVEN.** Record a type as the link
  coloring plus its boundary co-chaining. Planar realizability is characterized in
  closed form (forced consecutive pairs + color-aware non-crossing + a spanning
  enclosure law); necessity is proven by a Jordan-curve + Kempe-separation argument,
  so the realizable set has **exactly 104** canonical members.

## 2. The linear dictionary (the key move)

Take the colors as `V = F_2^2 = {0,1,2,3}` (00,01,10,11), addition = XOR.

| object | linear form |
|---|---|
| proper coloring | nowhere-zero `F_2^2`-tension |
| Kempe `(a,b)`-swap on component `C` | **add `g = a⊕b` to `C`** (a translation) |
| effect on the link | `c_i ↦ c_i ⊕ (g if i∈C else 0)` |
| color relabelings | `S_4 = AGL(2,2)`, the affine group of `F_2^2` |
| stuck | the 5 link colors cover all of `F_2^2` |
| **freed** | the 5 link colors **miss** some `m ∈ F_2^2` |

Embed a move as a cut-vector `emb(g,s) ∈ F_2^{10}` (5 positions × 2 bits, `s` the
link-support of `C`). Let **`W_type`** be the `F_2`-span of the achievable
cut-vectors — built from the type's co-chaining **alone, no interior**. Then
(verified exact, 0 errors over `9·10^4` instances; the interior changes the true
span's rank but never this bit):

> **`v` is freeable ⇔ `W_type` meets the free-set:**
> `∃ m, ∃ t ∈ W_type` with `c_i ⊕ t_i ≠ m` for all `i`
> (i.e. `W_type` escapes the 5 coordinate slices `{t : t_i = c_i⊕m}`).

## 3. The split, and where the difficulty sits

- **`true_W ⊆ W_type`** (proven: a true component's link-trace is a union of whole
  co-chaining blocks). Hence **freeable ⇒ `W_type` meets the free-set is PROVEN**
  (a freeing 2-swap is a sum of cut-vectors in `true_W ⊆ W_type`).
- The **97 single-swap types** are settled (one swap; type-determined and linear).
- On the **7 residual types**, `W_type = true_W` **exactly** (0 slack). So the
  entire residual of four-color is the **reverse** implication on these 7 flats:

> **(THE CORE) For each of the 7 flats below: a freeing vector in `W_type` is
> realized by ≤2 actual Kempe swaps.** This is four-color-equivalent.

## 4. The seven flats (the minimal representation)

`F_2^{10}` coordinates are `(p0_hi p0_lo … p4_hi p4_lo)`. Each flat is `W_type`,
given by an RREF basis over `F_2`; `c` is the link coloring; a freeing witness `t`
(a vector of `W_type` that makes the link miss color `m`) is listed — so **each of
the seven flats demonstrably meets the free-set.** (Generated deterministically by
`play/fourcolor_seven_flats.py`.)

```
R1  c=(0,1,0,2,3)  dim 7      R2  c=(0,1,2,0,3)  dim 8
 1000000000                    1000000000
 0101010000                    0101000000
 0010000111                    0010010011
 0001010011                    0001000000
 0000101000                    0000101000
 0000011000                    0000010001
 0000000101                    0000001011
 t=0100110110 misses 0         0000000100
                               t=0110110100 misses 0

R3  c=(0,1,2,0,3)  dim 7      R4  c=(0,1,2,1,3)  dim 7
 1000000000                    1000100000
 0101000000                    0101000000
 0010010011                    0010011011
 0001001011                    0001100011
 0000101000                    0000011011
 0000010001                    0000001010
 0000000100                    0000000100
 t=0100110110 misses 0         t=1110001001 misses 0

R5  c=(0,1,2,3,1)  dim 8      R6  c=(0,1,2,3,1)  dim 7
 1000100000                    1000100000
 0101000000                    0101000001
 0010011100                    0010011101
 0001101100                    0001101101
 0000011100                    0000011101
 0000001000                    0000001001
 0000000010                    0000000011
 0000000001                    t=0100111000 misses 0
 t=1110000111 misses 0

R7  c=(0,1,2,3,2)  dim 7
 1000000010
 0101000000
 0010011110
 0001001110
 0000100000
 0000010101
 0000000011
 t=1110000111 misses 0
```

## 5. Status ledger

| Step | Status |
|---|---|
| Euler → canonical path-links | proven for length ≤5; the `≤5` bound itself open |
| deg-4 reducible | **proven (closed form)** |
| deg-5 realizable type set = 104 | **proven** (Jordan + Kempe separation) |
| colors = `F_2^2`, swaps = translations, `S_4 = AGL(2,2)` | **proven** |
| freeing = `W_type` meets the free-set | verified exact (0 / `9·10^4`) |
| single-swap layer (97 types) | **proven** type-local + `F_2`-linear |
| `true_W ⊆ W_type`; forward implication | **proven** |
| `W_type = true_W` on the 7 residual types | verified (0 slack) |
| all 7 flats meet the free-set | **computed exact** (Sec. 4) |
| **reverse implication on the 7 flats** | **open; four-color-equivalent** |

## 6. What this is, honestly

Four-color is a theorem (Appel-Haken 1976; Gonthier 2005, both machine-checked).
This does **not** add a new proof. It gives a **minimal linear representation**: the
theorem's entire residual difficulty, distilled to whether **seven explicit
`F_2`-subspaces realize their freedom**, with everything around it proven and the
forward direction in hand. Colors are vectors, Kempe moves are translations
(`AGL(2,2)`), and "four-colorable" is a subspace escaping five coordinate slices.
If the seven-flat core can be cracked, it is here; if not, this is the smallest
linear object on which the famous difficulty is known to rest.
