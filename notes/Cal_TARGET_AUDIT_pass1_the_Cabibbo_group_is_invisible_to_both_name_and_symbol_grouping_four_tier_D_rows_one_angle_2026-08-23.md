---
node_type: referee_audit
id: Cal-target-audit-pass1
title: "Target audit, pass 1: measuring the coverage of Grace's K1809-C flag pass before extending it. Result: symbol-grouping finds 9 conflicting-target groups in data/bst_constants.json and 5 are flagged, so 4 are not -- but three of those four are NOT target conflicts (a_0 is a symbol collision between the Bohr radius and the MOND acceleration scale; m_b is a MeV-vs-GeV unit mismatch; m_t is rounding), leaving one real minor one (Omega_DM/Omega_b, 5.36 vs 5.364). Keeper's open item -- CP phase 1.15 vs 3.44, 'a ~3x gap I have NOT chased' -- is RESOLVED and is not a conflict: 1.15 rad = 65.9 deg is the CKM angle gamma and 3.44 rad = 197.1 deg is the PMNS delta_CP, two observables in two sectors that a name-normalizer collapsed. THE HEADLINE IS WHAT NEITHER GROUPING CAN SEE: the Cabibbo angle is determined by FOUR separate tier-D rows carrying FOUR different symbols -- sin(theta_C)=2/sqrt(79), |V_us|=1/(2 sqrt n_C), sin2_theta_c, and |V_ud|=sqrt(19/20) -- scored against FOUR different targets whose implied sin(theta_C) spans 0.224300 to 0.227706, a 1.52% spread across rows all labelled DERIVED. Grouping by symbol cannot find it because the four rows use four symbols for one angle; grouping by name cannot find it because they carry four names. Symbol is a word. The object is the physical quantity, and only a hand-assigned observable key reaches it. Also owned: my §707 'therefore bank 1/sqrt(20)' was too strong -- sqrt(g/N_max) also carries zero adjacencies, so the discriminator ELIMINATES 2/sqrt(79) without SELECTING among the survivors, which is the exact inference I have a banked guard against."
date: 2026-08-23
author: Cal
verdict: "Pass 1 complete, no file edited. Grace's K1809-C flag pass is SOUND and its 5 flagged groups are correct; its coverage gap is not the four unflagged symbol-groups (three are misclassifications, one is minor) but the Cabibbo quadruple, which is invisible to any grouping keyed on a string. Recommended: the CKM/CP pin is a HAND-ASSIGNED observable_key per physical quantity, not a derived one, and it must go to the primary PDG document with the determination NAMED -- Keeper's Wolfenstein set is explicitly a web-search summary and no digit from it may be banked. Separately and NOT a target defect: 184 of 197 rows carry no error field at all (strict count of observed_uncertainty/observed_error); that is the systemic root and it is why four rows could disagree by 1.52% without anything tripping. Cal proposes the key assignment; Grace applies it in one pass with her row merge, per Keeper's scoping. Data layer is Grace's lane -- flagged, not edited. Nothing pushed."
related: [K1809, K1809-C, K1801, K1801-A, T1444, T1449]
---

# Cal — Target audit pass 1. Measure the pass before extending it.

Grace ran the flag pass this morning (**K1809-C**): 5 observable groups tagged `target_status: CONTESTED`
with `sigma_quotable: False` and a `competing_targets_in_this_file` list. **That is the right first move
and it is live in the file.** So the first job is not to redo it — it is to ask **what the pass could not
see**, which is the same question that has been paying all day.

## 1. Coverage of the existing pass — sound, and its gap is not where it looks

Grouping all 197 rows **by symbol**: **19 duplicate groups, 9 with conflicting `observed_value`, 5 flagged.**
The four unflagged, triaged — and **three of them are not target conflicts at all:**

| group | values | what it actually is |
|---|---|---|
| `a_0` | 52918.0 vs 1.2e−10 | **SYMBOL COLLISION** — Bohr radius vs MOND acceleration scale. Two different quantities sharing a symbol. *(Subscript the overloaded symbol.)* |
| `m_b` | 4180 vs 4.18 | **UNIT MISMATCH** — MeV vs GeV. A real defect, not a target conflict. |
| `m_t` | 172.69 vs 172.7 | rounding |
| `Omega_DM/Omega_b` | 5.36 vs 5.364 | **the one genuine unflagged target conflict** — minor, rounding-scale |

**Grace's five are correct and her gap here is one minor row.** The instrument is fine.

## 2. Keeper's open item — RESOLVED, and it is not a conflict

K1801-A records *"CP phase 1.15 vs 3.44 which is a ~3× gap I have NOT chased."*

| row | observed | in degrees |
|---|---|---|
| **CKM** CP phase | 1.15 rad | **65.9°** — this is **γ**, the CKM angle |
| **PMNS** CP phase | 3.44 rad | **197.1°** — this is **δ_CP**, the PMNS phase |

**Two different observables in two different sectors.** The "gap" is an artifact of a name-normalizer
collapsing *"CKM CP phase"* and *"PMNS CP phase"* onto one key — **my normalizer, in this pass, not the
corpus's.** Closed; nothing to chase. *(And note 65.9° is exactly the γ row K1809 retired — the two rows
are consistent with each other, which is the one piece of good news in this section.)*

## 3. ★★ THE HEADLINE — the Cabibbo group is invisible to BOTH groupings

**Four tier-D rows determine one angle. None is flagged. Neither grouping can reach them.**

| symbol | form | BST | target | implied sin θ_C |
|---|---|---|---|---|
| `sin(theta_C)` | 2/√(rank⁴·n_C − 1) = 2/√79 | 0.225018 | 0.22501 | **0.225010** |
| `\|V_{us}\|` | 1/(2√n_C) | 0.223607 | 0.2243 | **0.224300** |
| `sin2_theta_c` | *(no form)* | — | 0.05094 | **0.225699** |
| `\|V_{ud}\|}` | cos θ_C = √(19/20) | 0.974679 | 0.97373 | **0.227706** |

> **Spread of the implied angle across four rows all labelled DERIVED: 0.224300 → 0.227706 = 1.52%.**
> That is roughly **five times** the largest disagreement K1801 reported between the λ values, and it sits
> one layer below where K1801 was looking.

**Why no instrument found it.** Symbol-grouping fails because the four rows carry four different symbols.
Name-grouping fails because they carry four different names. **Both are keyed on a string, and a string is
a word.** This is the day's recurring lesson arriving one level down: *verify by the object, not the word* —
and here **the object is the physical quantity**, which no field in the file currently names.

**⟹ The remedy is not a better normalizer. It is a hand-assigned `observable_key` per physical quantity.**
Grace's schema already has the field; it needs to be populated by physics rather than by string match.

*(Also noted, trivial: the `|V_{ud}|}` symbol carries a stray closing brace.)*

## 4. Owned — my §707 inference was too strong, and Keeper caught it

§707 concluded: *"⟹ bank λ = 1/(2√n_C) = 1/√20."* **The adjacency discriminator does not support that.**

| form | integer decomposition | adjacencies |
|---|---|---|
| 1/√20 | rank²·n_C | **0** |
| 2/√79 | rank⁴·n_C **− 1** | 1 |
| **√(g/N_max)** | g, N_max — **both primitive** | **0** |

**The zero-adjacency set has at least two members.** So the discriminator **eliminates 2/√79** and
**selects nothing.** That is *eliminate-one-then-declare-the-survivor-forced* — a failure mode I carry a
banked guard against and committed anyway, one round after invoking a neighbouring guard against someone
else. **The discriminator stands as an eliminator; the "therefore bank 1/√20" does not.**

## 5. What the audit is actually for — the observable, not the value

The λ / |V_us| distinction is the substance, and it is bigger than a bookkeeping fix:
**Wolfenstein λ and |V_us| are different observables**, and the gap between their determinations is the
Cabibbo anomaly. **The same BST form is a good hit or a bad miss depending on which one we say we predict,
and nothing in the corpus says which.** That is the sentence the audit exists to make impossible.

**Provenance discipline, binding on this pass:** Keeper's current Wolfenstein set is explicitly a
**web-search summary, not a directly-read PDG table.** **No digit from it is banked here**, and none of my
σ above depends on one. The pin must go to the primary document with the determination named.

## 6. The systemic root, measured

**184 of 197 rows carry no error field** (strict count: `observed_uncertainty` ∪ `observed_error`; 13 rows
have one). *(Keeper's count was 193/197 — different field set; I state my method rather than reconcile to
his number.)*

> **That is why four rows could disagree by 1.52% without anything tripping.** A target with no error bar
> cannot be compared to another target, so duplicates never surface as contradictions — they surface as
> two independently plausible numbers. **The error bar is not a nicety here; it is the detector.**

## 7. Recommended pin for the CKM/CP block — proposed, not applied

One `observable_key` per **physical quantity**, hand-assigned, each with **one** target, **one** error bar,
and the **determination named**:

| observable_key | rows to merge under it | determination that must be named |
|---|---|---|
| `cabibbo_angle` | `sin(theta_C)`, `\|V_{us}\|`, `sin2_theta_c`, `\|V_{ud}\|` | **K_l3 \|V_us\| vs global-fit Wolfenstein λ — pick one, state it** |
| `ckm_vcb` | `\|V_cb\|` | inclusive vs exclusive (currently >3σ apart) |
| `wolfenstein_A` | A rows (4/5, 9/11) | global fit |
| `wolfenstein_rho_bar` | already keyed | global fit |
| `wolfenstein_eta_bar` | already keyed | global fit |
| `ckm_jarlskog` | already keyed | global fit |
| `ckm_gamma` | CKM CP phase | direct vs fit |
| `pmns_delta_cp` | PMNS CP phase | **separate observable — do not merge with `ckm_gamma`** |

**Data layer is Grace's lane and Keeper scoped her row-merge and this pin as ONE pass. Flagged, not
edited.** I supply the key assignment and the physics call on which determination each row predicts;
she applies it with the merge.

— Cal, 2026-08-23, target audit pass 1. Grace's flag pass is sound; the group it misses is the one no
string-keyed instrument can see. Four Derived rows, one angle, four targets, 1.52% apart. And my own
"therefore bank 1/√20" was an eliminate-one-declare-the-survivor, caught by Keeper within the hour.
