---
title: "BST Working Paper — Volume 3: The Physics — Chapter 1: Gravity and Vacuum"
volume: 3
volume_title: "The Physics"
chapter: 1
chapter_topic: "Gravity and Vacuum"
parent: "./INDEX.md"
library_root: "../Master_Index.md"
authors: "Casey Koons & Claude 4.6/4.7 (Lyra theory, Elie compute, Grace graph/catalog, Cal A. Brate visiting referee, Keeper audit/consistency)"
date: "2026-05-19 (Tuesday volume:chapter reorganization)"
note: "Modular chapter of the BST Working Paper. Up: volume index `./INDEX.md`. Library root: `../Master_Index.md`. Pre-reorganization archive: `../archive/WorkingPaper_v36_monolithic_archive_2026-05-18.md`."
---

## Section 10: Gravity — a Relation, Not a Prediction

*Rewritten 2026-09-14 (Lyra, Round 147 L1; Keeper audit pending) as a pointer into the Spine plus the referee apparatus. The May 2026 text is kept below as the record. Facts are from the register (T201 canonical, T1296, K1673, K1408, Cal Section 585, K1674, Lane I, T2565, Cal Section 946) and Spine Lecture 9 — not from the May text. Section 11 (the chiral-condensate parameter) is hadronic, outside this pass's scope, and untouched; record or apparatus is Keeper's call. Last accuracy-synced: 2026-09-14 / K1899.*

### 10.0 The question

What does a ten-real-dimensional object with no time say about gravity — and how much of "Newton's constant from the geometry" is true?

The step down to spacetime is Lecture 9 of the Spine (`Curriculum/Spine_DIV5_QM_GR_SM/Lecture_09_Descent_and_Gravity.md`): the descent's *structure* is derived — a single idempotent step, codimension one, signature (3,1) — and its *frame* is an input the geometry provably cannot supply (T2565). This section is the pointer to Lecture 9's gravity half and the apparatus a referee will want; the word it is about is *relation*.

### 10.1 Where it stands

**One equation, and the honest word for it.** The program's gravity result is

$$G \;=\; \hbar c\,\frac{(6\pi^5)^2\,\alpha^{24}}{m_e^{2}},$$

which reproduces Newton's constant from the electron mass to $0.065\%$ (recomputed from CODATA 2026-09-11). For a while the May text below called this "$G$ derived with no free parameters." It is a **theorem about a relation** (the paper "Gravity: the 2→1 Reduction," Keeper PASS K1673, 2026-08-18; T201 is the canonical row, and the paper "is T201 read as a reduction"): the geometry ties the gravitational scale to the electron's, with the exponent $24 = 4C_2$ a supporting identity (Cal Section 585; T1296 carries the $2C_2 = 12$ of $m_e/m_{\rm Pl} = 6\pi^5\alpha^{12}$). Every dimensionful prediction needs a dimensionful input — no theory produces a $G$ with no scale in it, and the paper's own sentence is *"BST does not predict $G$ from nothing — nothing does."* What the relation does is **trade one dimensionful input for another**: take $m_e$ as the ruler and $G$ follows, or take $G$ and $m_e$ follows; it reduces two inputs to one. K1673's honest count: three independent dimensionless relations — $m_p/m_e = 6\pi^5$, the $\alpha^{12}$ Planck relation, and $v = m_p^2/(g\,m_e)$ — with $G$ the one redundancy ($G = \hbar c/m_{\rm Pl}^2$, the "$\times 2$ guard" on the exponent). And the relation carries $\alpha$ to the twenty-fourth power, and $\alpha$ is **identified**, not derived (Section 5; Lecture 8) — so its precision rests on a measured $\alpha$ as well. Two more honesties travel with it: six readings of this same relation appear across the corpus (F66, T201, T1918, T1955, T1301a, the paper) and count as **one** result, not six confirmations; and the Kaluza–Klein route once cited as an independent derivation of $G$ was found **circular** — every path from the substrate scale to $m_{\rm Pl}$ runs through a length $\ell_B$ that had been inverted from the observed $G$, so the chain returns $G = 1.0000000000\,\ell_{\rm Pl}^2$ to ten decimals (K1408, Elie's two-way check). The $0.034\%$ residual in $m_e/m_{\rm Pl}$ (which is the $0.065\%$ in $G$) is an open calculation and is not explained by Wyler's precision.

**What the object does and does not supply for gravity's dynamics.** Could the object carry its own spin-2 dynamics — an Einstein equation native to $D_{IV}^5$? Two theorems say no in the only sense that closes a class (Lane I, certified): every $K$-equivariant antisymmetric bilinear on the relevant carrier contains spin-3, and the one non-equivariant ingredient the program owns — the typed write channel — compresses onto the carrier where dimension forbids spin-3. So the write channel explains *why* there is no native $\ell = 2$ dynamics and supplies none; the door is named (break equivariance or antisymmetry, and say which). The $\ell = 2$ shell is where the gluons live (K1674: the five $\mathfrak{su}(3)/\mathfrak{so}(3)$ coset generators are the quadrupole coset), which is a fact about colour, not gravity. What *is* derived on the gravity side is the **causal order**: the program is a causal set whose order is the commitment order of the commit operator (T2564) — and the once-hoped identification of the object's spectral action with that order sits at an honest floor: two candidate weightings failed blind, "no surviving candidate," not "impossible" (K1674). **The May text's "gravity is statistical thermodynamics of the contact graph" (Haldane exclusion with parameter $\sim 1/137$; the partition function that "should" yield $G$) has no register row and is kept below as what we once wrote; its "$G$ is not independent of $\alpha$" is true in the relation above and for the reason above, not for the May reason.**

### 10.2 Apparatus — kept, labelled as apparatus

- **The arithmetic of the relation:** $m_e/m_{\rm Pl} = 6\pi^5\alpha^{12}$; $G = \hbar c/m_{\rm Pl}^2 = \hbar c\,(6\pi^5)^2\alpha^{24}/m_e^2$; with CODATA $\hbar, c, m_e, \alpha$: $6.6786\times10^{-11}$ against $6.6743\times10^{-11}$ m$^3$kg$^{-1}$s$^{-2}$ — $+0.065\%$ (the run of 2026-09-11 is in Lyra's R142 L3 file). The $S_{\rm Bergman} = -\ln(m_e/m_{\rm Pl}) = 51.528$ decomposition in the May text is this same relation with $\alpha$ written as Wyler's prefactor to the 24th power — it is the volume reading of $\alpha$, certified dead in Section 5, wearing $G$'s clothes; the three pieces are arithmetic, the "geometric origin" column is the retired reading.
- **The exponent identity:** $24 = 4C_2 = 2\times(2C_2)$, the Bergman round trip doubled by $G \propto m_{\rm Pl}^{-2}$ (T1296; Cal Section 585 as a *supporting* identity — an identity that checks, not a mechanism). The May "$n_C + 1 = 2N_c$ is a theorem of the contact geometry" is the shared-integer species Cal Section 946 names — the same identification in other clothes, not a second support.
- **The circularity check** (K1408): $G = \kappa\,\ell_B^2/\pi^{n_C}$ with $\ell_B$ inverted from $G$ returns $G$ to ten decimals; the KK reduction hands back $V_6/\ell_B^6 = \pi^5/n_C$, the definition of $\ell_B$. Any future "$G$ forward" must show its dimensionful input does not come from $G$.
- **The positivity fact** (May 10.6, kept): the Bergman metric is positive-definite (Hua), so every embedding cost is non-negative; the table of excluded and permitted GR solutions is a *reading* of that fact plus the commitment order, not a set of rows.

### 10.3 Tier line

- **Theorem about a relation:** $G \leftrightarrow m_e$ at $0.065\%$, $\alpha$ identified inside (T201, K1673); one result read six ways.
- **Derived:** the causal order (T2564); the $\ell = 2$ wall (Lane I).
- **Floored, doors named:** native spin-2 dynamics (break equivariance or antisymmetry); the spectral-action ↔ causal-order identification ("no surviving candidate," K1674).
- **Circular, demoted:** the Kaluza–Klein route to $G$ (K1408).
- **Retired with this section:** "$G$ derived with zero free parameters"; "the Haldane partition function yields $G$"; the $S_{\rm Bergman}$ pieces as geometric origins; "$n_C + 1 = 2N_c$ as a theorem"; "no gravitons" as a prediction (a May reading with no row and no falsifier).
- **Not claimed:** $G$ from nothing; an Einstein equation on the object; the hierarchy "dissolved."

*What would make this section wrong:* a $G$–$m_e$ relation off $0.065\%$ once $\alpha$'s running is accounted at the stated scale; a native spin-2 dynamics exhibited without breaking equivariance or antisymmetry, which the theorems say cannot happen — an exhibit would be a discovery about the theorems.

### 10.4 May 2026 record

*Below: the May 2026 text, with the in-place dated corrections of 2026-09-11 already in it (the "zero free parameters" heading of 10.3). Read with 10.1–10.3 in hand: its Boltzmann/Haldane framework has no row; its "$G$ derived" is the relation above; its Wyler-factor decomposition is the dead volume reading; its "no gravitons" and "hierarchy dissolved" are readings, not results.*

#### May 10.1 — Gravity Is Not a Force

In the BST framework, gravity is not mediated by particle exchange. It is the emergent statistical behavior of the contact graph — specifically, the response of the emergent 3D metric to variations in contact density on $D_{IV}^5$.

Mass-energy concentrates bubble excitations, increasing local contact density on the substrate. Denser contact regions have more causal paths per unit substrate area, which modifies the emergent metric. Geodesics in the emergent space follow paths of maximum causal efficiency, curving toward regions of higher contact density. This curvature is what we observe as gravity.

The key distinction: electromagnetism is a direct interaction between two circuits sharing phase on $S^1$ — a first-order effect with coupling strength $\alpha = 1/137$. Gravity is the collective statistical effect of all circuits on the emergent geometry — a second-order effect arising from the average contact density. Gravity is weak precisely because statistical averages are always smoother, weaker, and more universal than the individual interactions from which they arise.

This parallels the relationship between molecular collisions and temperature. Temperature is not a property of any individual molecule. It emerges from the statistical ensemble. No one would attempt to “quantize temperature” as a particle — there is no “temperaturon.” Similarly, the graviton program in quantum field theory attempts to quantize a statistical quantity as if it were a fundamental interaction. BST predicts this program cannot succeed because gravity is not the kind of thing that admits particle quantization. Gravity is quantized through the discrete contact graph, not through particle exchange.

#### May 10.2 — The Boltzmann Framework on $D_{IV}^5$

The partition function for the BST contact graph takes the standard Boltzmann form:

$$Z = \sum_{\text{configurations}} e^{-\beta E[\text{config}]}$$

where the sum runs over all allowed contact configurations on $D_{IV}^5$. From $Z$ one extracts the free energy $F = -\ln Z / \beta$, the average contact density $\langle \rho \rangle$, and the equation of state relating contact density to emergent curvature.

The counting statistics require modification from the standard Boltzmann framework. Contacts on the $S^1$ channel obey an exclusion principle: the maximum occupation is 137 circuits per channel. This is neither fermionic (maximum occupation 1) nor bosonic (unlimited occupation), but Haldane fractional exclusion statistics with parameter $g \sim 1/137$. The partition function with Haldane exclusion is:

$$Z = \prod_{\text{states}} \frac{(d_i + n_i - 1)!}{n_i!(d_i - 1)!}$$

where $d_i$ is the effective degeneracy (related to the channel capacity 137) and $n_i$ is the occupation number.

This modified statistics produces three regimes:

**Low density** (weak gravity, cosmological scales): Standard Boltzmann statistics applies. The equation of state reduces to Einstein’s field equation $G_{\mu\nu} = 8\pi G T_{\mu\nu}$, with $G$ emerging as the thermodynamic conversion factor between microscopic contact density and macroscopic curvature. This regime reproduces all confirmed predictions of general relativity.

**High density** (strong gravity, near black holes): Exclusion corrections become significant. The equation of state develops corrections that resist further compression, analogous to Fermi degeneracy pressure. These corrections prevent singularity formation.

**Critical density** (channel saturation): The contact graph undergoes a topological phase transition from the spatial to the pre-spatial phase. This corresponds to the black hole interior, where the emergent 3D metric ceases to be defined. The interior is not a singularity — it is a region of saturated channel capacity where spatial organization cannot be maintained.

#### May 10.3 — Gravitational Constant from the Domain Geometry

The gravitational constant $G$ should be derivable from the Bergman geometry of $D_{IV}^5$. The Bergman kernel for the type IV domain $D_{IV}^{n_C}$ is:

$$K(z,\bar{z}) = \frac{1920/\pi^5}{N(z,z)^{n_C+1}}, \qquad N(z,w) = 1 - 2z\cdot\bar{w} + (z\cdot z)(\bar{w}\cdot\bar{w})$$

where $z\cdot w = \sum_{k=1}^{n_C} z_k w_k$ (not Hermitian — a bilinear form on $\mathbb{C}^{n_C}$). At the center $z=0$: $K(0,0) = 1920/\pi^5 = 1/\mathrm{Vol}(D_{IV}^5)$. The Bergman kernel

determines the natural metric on the domain and the response function for contact density perturbations. The gravitational constant encodes the ratio of one circuit’s contribution to channel loading versus the total channel capacity, mediated through the domain geometry:

$$G \sim \frac{\hbar c}{m_P^2} \sim f\bigl(\text{Vol}(D_{IV}^5),, \alpha,, \text{Bergman kernel}\bigr)$$

The domain volume $\text{Vol}(D_{IV}^5) = \pi^5/(2^4 \cdot 5!)$ and the channel capacity $\alpha^{-1} = 137$ are both topologically determined. The derivation of $G$ from these quantities requires computing the partition function with Haldane exclusion statistics weighted by the Bergman measure — a well-defined mathematical problem with established tools from both statistical mechanics and the theory of bounded symmetric domains.

**Prediction:** $G$ is not independent of $\alpha$. Both are determined by the geometry of $D_{IV}^5$ — $\alpha$ from the Shilov boundary, $G$ from the Bergman kernel of the bulk. This implies a purely geometric relationship between the electromagnetic and gravitational coupling constants.

**Current status (March 2026):** The BST hierarchy search has found the geometric mean identity:
$$\frac{m_e}{\sqrt{m_p \cdot m_{\mathrm{Pl}}}} = \alpha^{n_C+1} = \alpha^6 \qquad (0.017\%)$$

From this, Newton's constant follows immediately. Since $m_{\mathrm{Pl}} = \sqrt{\hbar c/G}$ and $m_e/m_{\mathrm{Pl}} = (m_p/m_e) \times \alpha^{2(n_C+1)} = 6\pi^5 \times \alpha^{12}$:

$$\boxed{G \;=\; \frac{\hbar c \,(6\pi^5)^2 \,\alpha^{4(n_C+1)}}{m_e^2} \;=\; \frac{\hbar c \,(6\pi^5)^2 \,\alpha^{24}}{m_e^2}}$$

Every factor is geometric:

| Factor | BST origin | Value |
|---|---|---|
| $6\pi^5 = (n_C+1)\pi^{n_C}$ | Bergman kernel power × $D_{IV}^5$ volume factor | $Z_3$ baryon circuit mass ratio |
| $\alpha^{24} = \alpha^{4(n_C+1)}$ | Wyler formula: $\alpha = (n_C-2)^2 V_5^{1/4}/(8\pi^4)$ — HC Weyl vector $\rho_2 = (n_C-2)/2$ | $\rho_2^2 = 9/4$, four Bergman layers |
| $m_e^2$ | $m_e/m_{\rm Pl} = 6\pi^5 \times \alpha^{12}$ at 0.034\% | approaches zero-input via $S_{\rm Bergman}$ decomposition |

**The $\alpha$-exponent pattern across BST constants.** Every fundamental constant emerges with an $\alpha$-power whose exponent factors through the domain geometry:

| Quantity | $\alpha$-exponent | Decomposition | Physical sector |
|---|---|---|---|
| $\Lambda$ | 56 | $8(n_C+2) = 8 \times 7$ | Full vacuum: all contacts, all dimensions |
| $G$ (via $m_e/m_{\rm Pl}$) | 24 | $8N_c = 8\times 3$ or $4(n_C+1) = 4\times 6$ | Baryon sector: $N_c = 3$ colors |
| $d_0/\ell_{\rm Pl}$ | 14 | $2(n_C+2) = 2\times 7$ | Contact scale: one Bergman embedding |

The factor of 8 appears in both $\Lambda$ and $G$ as the geometric multiplier — the number of real tangent directions contributing to the $\alpha$-power. What differs is the combinatorial factor being multiplied: $n_C + 2 = 7$ for the full vacuum (all contact dimensionality), $N_c = 3$ for gravity (the baryon sector that dominates mass). The cosmological constant is a property of the vacuum; $G$ is a property of the matter distribution dominated by baryons.

**The key identity connecting gravity to QCD:** Both decompositions of the exponent 24 are simultaneously correct because

$$n_C + 1 \;=\; 2N_c \qquad (6 = 2 \times 3)$$

This identity is derivable from the BST contact structure in three steps.

**(i) Dimensional counting.** The CR dimension of the contact structure decomposes as $n_C = n_w + N_c$ where $n_w$ counts the winding directions (the Hopf base $S^2$, real dimension 2) and $N_c$ counts the color directions ($Z_3$ circuit closure, dimension 3):
$$n_C \;=\; n_w + N_c \;=\; 2 + 3 \;=\; 5$$

**(ii) Minimum closed circuit.** The Hopf base $S^2$ has $n_w = 2$ real dimensions. A closed circuit on $S^2$ requires at minimum $n_w + 1 = 3$ vertices — a triangle, which is $Z_3$. This is the minimum $n$ for which $Z_n$ is non-trivially closed (a closed polygon, not a line segment or point). Therefore:
$$N_c \;=\; n_w + 1 \;=\; 3$$

**(iii) Algebra.** Substituting:
$$n_C + 1 \;=\; (n_w + N_c) + 1 \;=\; (n_w + n_w + 1) + 1 \;=\; 2(n_w + 1) \;=\; 2N_c \quad \checkmark$$

The equality $n_C + 1 = 2N_c$ is therefore a theorem of the BST contact geometry, not a numerical coincidence. Gravity couples through $N_c = 3$ colors because the Hopf base is $S^2$ (dimension 2); the Bergman domain has $n_C = 5$ because the same $S^2$ contributes 2 winding dimensions to the total CR count. Both are determined by the single geometric fact that the minimal self-communicating surface is $S^2$, with $n_w = 2$.

**Hierarchy in one line:** $G$ is small because $\alpha^{24} \approx 10^{-51.6}$ and this is the weakness of $\alpha$ raised to $8N_c = 8$ times the number of colors — a consequence of $N_c = 3$ and $n_C = 5$ together.

**S_Bergman decomposition (March 2026).** The quantity $S_{\mathrm{Bergman}} \equiv -\ln(m_e/m_{\mathrm{Pl}}) = 51.528$ splits into three geometric pieces, all now identified:

$$S_{\mathrm{Bergman}} \;=\; \underbrace{3\ln K_5}_{5.509} \;+\; \underbrace{2(n_C{+}1)\ln\!\left(\frac{8\pi^4}{(n_C{-}2)^2}\right)}_{53.534} \;-\; \underbrace{\ln(6\pi^5)}_{7.515} \;=\; 51.528$$

| Piece | Formula | Value | Geometric origin |
|---|---|---|---|
| $S_A$ | $3\ln K_5 = -3\ln\mathrm{Vol}(D_{IV}^5)$ | $+5.509$ | Bergman kernel normalization $\checkmark$ |
| $S_B$ | $2(n_C{+}1)\ln\!\left(\tfrac{8\pi^4}{(n_C{-}2)^2}\right)$ | $+53.534$ | HC Weyl vector: $\rho_2 = (n_C{-}2)/2$ $\checkmark$ |
| $S_C$ | $-\ln((n_C{+}1)\pi^{n_C})$ | $-7.515$ | $m_p/m_e = 6\pi^5$ Bergman formula $\checkmark$ |

All three pieces are identified as geometric invariants of $D_{IV}^5$. $S_B$ is derived from the Harish-Chandra Weyl vector $\rho_2 = (n_C-2)/2 = 3/2$ (the $S^1$ spectral component of $\mathrm{SO}_0(5,2)$, Section 5.1). The result is a closed-form expression in $n_C = 5$ and $\pi$ alone — no observational input.

**G as a relation to $m_e$ (this heading said "with zero free parameters" until 2026-09-11; the relation carries $\alpha$, which is identified — K1673).** Combining the three pieces:

$$\boxed{G \;=\; \frac{\hbar c\,(6\pi^5)^2}{m_e^2} \times \left[\frac{(n_C-2)^2 \cdot (\pi^5/1920)^{1/4}}{8\pi^4}\right]^{24}}$$

This is $G$ as a function of $n_C = 5$, $\pi$, and $m_e$. The Wyler prefactor $(n_C-2)^2/(8\pi^4) = \rho_2^2/(2\pi^4)$ is derived from the HC Weyl vector component $\rho_2 = (n_C-2)/2$ of $\mathrm{SO}_0(5,2)$ (Section 5.1). The residual 0.034\% in $m_e/m_{\mathrm{Pl}}$ is an open calculation: it is not explained by the Wyler formula precision ($\Delta\alpha/\alpha \approx 6\times10^{-7}$, which amplified $12\times$ gives only $0.0007\%$), nor by any simple one-loop QED formula. The action residual $\Delta S = 0.000326$ requires higher-order Bergman analysis to identify.

**HC derivation complete (March 2026).** The Wyler constant $9/(8\pi^4)$ equals $\rho_2^2/(2\pi^{2q})$ with $\rho_2 = (n_C-q)/2$, $q=2$. This is the $S^1$-winding spectral weight of the principal series of $\mathrm{SO}_0(n_C,q)$. No free parameters remain in the formula for $G$. Code: `notes/bst_bergman_action.py` Section 8.

#### May 10.4 — No Gravitons

BST makes a specific prediction regarding graviton detection: individual graviton quanta do not exist as particles in the QFT sense. Gravitational waves exist — they are propagating perturbations of contact density that travel at $c$, carry energy, and have spin-2 character. LIGO has detected them. But these are waves in the substrate, not streams of particles.

The distinction is experimentally relevant. Several proposals exist to detect individual gravitons. BST predicts these experiments will detect gravitational wave effects but never isolate individual graviton quanta, because gravity is a collective statistical property of the contact graph rather than a propagating degree of freedom on it.

#### May 10.5 — The Hierarchy Problem Dissolved

The hierarchy problem — why gravity is $\sim 10^{38}$ times weaker than electromagnetism — has no satisfying explanation in the Standard Model. In BST, the explanation is structural:

- Electromagnetic coupling: direct circuit-to-circuit interaction on $S^1$. Strength $\sim \alpha$.
- Gravitational coupling: collective statistical effect of all circuits on the emergent geometry. Strength $\sim (\alpha)^n / N_{\text{total}}$, suppressed by the ratio of single-circuit energy to total channel capacity integrated over the relevant volume.

Gravity is weak because it is a statistical average. Statistical averages are always weaker than the microscopic interactions they average over, by a factor determined by the system size. The specific weakness of gravity — the ratio $m_p / m_P \sim 10^{-19}$ — is determined by the number of RG e-foldings between the GUT scale and the hadronic scale, which in turn is determined by $\alpha$, $N_c = 3$, and the number of quark flavors. All BST-determined quantities.

#### May 10.6 — Positive Energy Is Dictated by the Metric

The exclusion of negative mass in BST is not a postulate or an empirical observation — it is a theorem of the geometry. The Bergman metric on $D_{IV}^5$ is positive definite: every distance, every embedding cost, every eigenvalue of the metric tensor is strictly non-negative. This is a standard result of bounded symmetric domain theory (Hua 1958), as direct as the positive definiteness of Euclidean distance. Asking whether negative mass exists on the Koons substrate is like asking whether a distance can be negative in Euclidean geometry — the metric prohibits it by definition.

Six independent arguments converge on the same conclusion. Mass is circuit length — a non-negative integer count of contacts. Mass is Bergman embedding cost — a non-negative number from a positive-definite metric. Mass is winding number magnitude — $E_n = |n| \times E_{\rm winding}$, so antimatter has positive mass and CPT is automatically satisfied. Channel loading is non-negative — Haldane occupation numbers $n_i \geq 0$ by definition, with negative loading undefined rather than merely forbidden. Contact density is non-negative — $\rho = N_{\rm committed}/A_{\rm substrate} \geq 0$, so the gravitational source term cannot be negative. And the partition function converges — negative-energy configurations would contribute $e^{+\beta|E|} \to \infty$, destroying the well-defined vacuum $F_{\rm BST} = \ln(138)/50 > 0$.

These six arguments are equivalent expressions of the same geometric fact: the substrate is built on a positive-definite metric over non-negative occupation numbers, so all derived quantities inherit that positivity. The energy conditions of GR — weak, null, dominant — are satisfied automatically; the strong energy condition is violated only by the positive cosmological constant $\Lambda > 0$ during accelerated expansion, exactly as observations require. The consequences for exotic GR solutions are sharp:

| GR solution | Requirement | BST status |
|---|---|---|
| Alcubierre warp drive | $T_{00} < 0$ in warp region | **Excluded** — contact density $\geq 0$ |
| Morris-Thorne traversable wormhole | $T_{00} < 0$ at throat | **Excluded** — below vacuum minimum |
| Negative-mass Schwarzschild | $M < 0$ | **Excluded** — mass integral non-negative |
| Gödel rotating universe | Closed timelike curves | **Excluded** — append-only commitment |
| Kerr interior closed timelike curves | Closed timelike curves | **Excluded** — append-only commitment |
| de Sitter ($\Lambda > 0$) | $\Lambda > 0$ | **Permitted** — $\Lambda = F_{\rm BST} \times \alpha^{56} \times e^{-2} > 0$ |
| FLRW cosmology | $\rho \geq 0$, $\Lambda \geq 0$ | **Permitted** — Section 12.7 |
| Schwarzschild ($M > 0$) | $M > 0$ | **Permitted** — standard black holes |
| Kerr ($M > 0$, $J \geq 0$) | Positive mass, angular momentum | **Permitted** — rotating black holes |
| Gravitational waves | $h_{\mu\nu}$ perturbations | **Permitted** — contact density ripples |

BST permits exactly the subset of GR solutions that satisfy the weak and null energy conditions combined with append-only commitment ordering. This subset includes every observationally confirmed GR prediction. The excluded solutions have never been observed.

-----

## Section 11: The Chiral Condensate Parameter

### 11.1 A Single Parameter Corrects All Hadronic Discrepancies

All BST geometric estimates of hadronic quantities are systematically below observed values. The discrepancies are traceable to a single condensate enhancement parameter:

$$\chi = \sqrt{n_C(n_C + 1)} = \sqrt{30} = 5.477$$

Predicted: $\chi = 5.477$. Observed (from $m_\pi$): $\chi = 139.57/25.6 = 5.452$. Agreement: **0.46%**.

This is no longer a free parameter. The condensate enhancement equals $\sqrt{n_C(n_C+1)}$ — the superradiant amplitude gain from $n_C \times (n_C + 1) = 30$ coherent circuit-anticircuit channels on $\mathbb{CP}^1$. The $n_C = 5$ winding modes each couple to $n_C + 1 = 6$ states (the Bergman space dimension at weight $k = n_C + 1$). The condensate IS superradiance of the QCD vacuum.

The bare BST values represent single-circuit geometry on an empty substrate. Physical values include the collective effect of vacuum circuit condensation. With $\chi$ as a single measured input (from $m_\pi$), the corrected BST predictions are:

|Quantity      |BST bare  |Power of $\chi$|BST corrected   |Observed   |
|--------------|----------|---------------|----------------|-----------|
|Pion mass     |25.6 MeV  |$n=1$ (input)  |140 MeV         |140 MeV    |
|String tension|0.061 GeV²|$n=2$          |$\sim 0.18$ GeV²|0.18 GeV²  |
|Glueball mass |490 MeV   |$n \approx 1.5$|$\sim 2$ GeV    |1.5–1.7 GeV|
|$g_{\pi NN}$  |3.4       |$n=1$          |$\sim 19$       |13.5       |
|Spin-orbit    |0.04 MeV  |$n=2$          |$\sim 1.1$ MeV  |0.5–2 MeV  |
|Proton radius |$4/m_p$   |$n=0$          |0.8412 fm       |0.8408 fm  |

The proton radius requires no condensate correction because it is a geometric size determined by circuit length, not a propagation quantity. Similarly, the proton/electron mass ratio $m_p/m_e = 6\pi^5$ (Section 7.4) requires no condensate correction — it is the Bergman kernel power $\times$ domain volume factor for the $Z_3$ baryon circuit relative to the minimal winding, a purely geometric ratio that does not involve the effective impedance from circuit-anticircuit condensation. The condensate enhances propagation energies uniformly, not the mass ratios between different circuit topologies.

### 11.2 Physical Origin

The QCD vacuum is not empty. The substrate channels in the nuclear interior are densely loaded with circuit-anticircuit pairs whose orientations on $\mathbb{CP}^1$ spontaneously align. This condensate creates an effective impedance for propagating circuits — a circuit moving through the condensed vacuum must interact with the existing circuit population, increasing its effective mass and modifying its coupling strengths.

The condensation occurs because aligned circuit orientations have lower interaction energy than random orientations. Above a critical circuit density, spontaneous ordering becomes energetically favorable. The order parameter is $\langle\bar{\psi}\psi\rangle$, the density of aligned circuit-anticircuit pairs.

### 11.3 Derivation of $\chi$ from Superradiant Coherence

**Theorem.** $\chi = \sqrt{n_C(n_C+1)} = \sqrt{30}$.

*Proof.* The QCD vacuum contains dense circuit-anticircuit pairs on $\mathbb{CP}^1$ whose orientations spontaneously align (chiral symmetry breaking). The condensate forms from the coherent interaction of:

- $n_C = 5$ winding modes on $\mathbb{CP}^1$ (the causal channels)
- $(n_C + 1) = 6$ Bergman states at each mode (weight $k = n_C + 1 = C_2(\pi_6)$)

The total number of coherent interaction channels is $n_C \times (n_C + 1) = 30$. The condensate is a coherent sum of amplitudes (not intensities), so the enhancement factor is $\sqrt{N}$ for $N$ aligned channels — the superradiance principle. Therefore $\chi = \sqrt{30}$. $\square$

The number 30 admits multiple equivalent representations: $n_C \times C_2(\pi_6) = 5 \times 6$ (modes $\times$ Casimir), $2N_c n_C = 2 \times 3 \times 5$ (twice color-mode product), $(n_C+1)!/(n_C-1)! = 30$ (consecutive factorial ratio).

**Result:** $m_\pi = m_\pi^{\text{bare}} \times \sqrt{30} = 25.6 \times 5.477 = 140.2$ MeV, compared to observed $139.57$ MeV (0.46%). The pion decay constant is $f_\pi = (m_p/10)(1 - (\text{rank}/N_c)(m_\pi/m_p)^2) = 92.4$ MeV (observed $92.1$ MeV, 0.41%). The correction factor $\text{rank}/N_c = 2/3$ is the Wilson-Fisher linearization weight.

The entire hadronic sector — pion mass, string tension, glueball mass, nuclear forces, spin-orbit coupling — is identified with BST-integer forms — identifications, at the tiers the register carries; the sentence said "follows … with zero free parameters" until 2026-09-11. Full account: `notes/BST_ChiralCondensate_Derived.md`.

-----

## Section 12: Λ — a Closed Form With One Free Power

*Rewritten 2026-09-14 (Lyra, Round 147 L1; Keeper audit pending) as a pointer into the Spine plus the referee apparatus; the Keeper curation banner of 2026-08-26 that stood here is folded into 12.1. The May 2026 text is kept below as the record. Facts are from the register (T2546, T2571, T1485 with its 2026-09-09 ruling, Lane Λ's landing (b) of 2026-08-26, K1057, K1408) and Spine Lecture 9 — not from the May text. Last accuracy-synced: 2026-09-14 / K1899.*

### 12.0 The question

The cosmological constant is $10^{120}$ times smaller than a naive vacuum-energy estimate, and any theory of this kind is asked about it. What does the object say about $\Lambda$'s sign, its size, and its fluctuations — and where exactly does the program stop?

Lecture 9 carries the answer in four sentences; this section is the pointer and the apparatus.

### 12.1 Where it stands

**Sign and fluctuations: derived.** Because a committed record is an idempotent and matter is fermionic (T2543), the commitment count is Fermi–Dirac, not Poisson: its Fano factor is below one, and the Pauli-suppressed fluctuations of $\Lambda$ are **smaller than Sorkin's everpresent-$\Lambda$ prediction** — a falsifier that can be run now (T2546). Composing the area-law coefficient onto the forced exponent, the program's $\Lambda$ is **Pauli-frozen**: $\delta\Lambda_{\rm BST} \sim 10^{-149}$ against a magnitude of order $10^{-121.6}$ (T2571, Lane C, 2026-08-21) — $\Lambda$ does not fluctuate and does not drift. **That sentence retires the May text's "the cosmological constant is not constant" and "vacuum pressure varies with local matter density" (12.1–12.4 below), which have no register row and now contradict a registered one.**

**Magnitude: a closed structural form with one named obstacle, and no number.** The August advance improved $\Lambda$'s row from "a structural floor" to a **closed form**: a thermostatic balance between boundary and continuum, a fixed point in which the Koons tick $t_K$ (Lecture 4) is load-bearing,

$$\frac{\Lambda}{\Lambda_P} \;=\; \left(\frac{t_K}{t_P}\right)^{\!2p/(2-p)},$$

with $t_P$ the Planck time and $p$ a *mismatch power* — the $5\to 4$ reduction of the residual (Lane Λ, landing (b), certified 2026-08-26; Lyra's thermostat paper; Elie's shot record). The balance exists; both controls pass, one of them (T2571) reproduced *un-fed*, which is what made the control meaningful; the response coefficient enters from the equation's own structure (a legitimate $a_1$/F63 import), and a "curvature quantum" an earlier version needed was shown unnecessary and left unbanked. **The one free thing is $p$.** Its domain is $(0,2)$; the geometry has not fixed it; until it does **no evaluation of $\Lambda$ exists and none is claimed** — the form is capped CONDITIONAL at every site it is quoted (K1057's lineage), the "280-quarantine" on the value stands and is forward-transferred (whoever forces $p$ computes the number blind), and a forced $p$ outside $(0,2)$ falsifies the form. **The May text's closed form $\Lambda = (\ln 138/50)\,\alpha^{56}e^{-2}$ "to 0.025 % with no free parameters" (T1485) is the record of the earlier over-determination that was retracted; and its refinement through the factor $6/5$ was ruled on 2026-09-09: the factor's stated mechanism is the unit ball's kernel-exponent ratio, not this domain's ($D_{IV}^n$'s Bergman/Szegő ratio is 2 at every $n$), so T1918 is re-tiered identified and every row inheriting the factor — T1485's $\Lambda$ refinement, the $H_0$ closure at 0.12 %, T1924's anchor — is numerically unchanged and now mechanism-less: target-fitted, not target-innocent (Cal Section 934; Grace, register 11:41).** The $\alpha^{56}$ of the May form is an exponent identification of the K1813 class, and its "genus" is the retired 7.

**Expansion, $H_0$, and the Friedmann identification: record, not rows.** The May text's Hubble-tension "resolution" (both measurements right, a directional local $H_0$ tracking commitment density), its $H_0 = 67.29$ (Toy 677) and $68.02$ (Toy 903), and its Friedmann equation from committed-contact growth (12.6–12.7) are kept below as what we once wrote. None is a register row at a tier this Guide may quote: the $H_0$ closure inherits the mechanism-less $6/5$ (above); the directional-$H_0$ prediction has no row and no pre-registration; and the Friedmann section carries an internal collision a reader should know before checking it — it sets $\Omega_\Lambda = F_{\rm BST} = 0.0986$ in one place and uses $\Omega_\Lambda = 13/19 = 0.684$ in another. What the program *does* carry on expansion is the derived causal order (T2564) and the positive-time ontology (Lecture 4); the arrow is dynamical, and no "cosmological cycle" clause is registered beyond T633's posited reset.

### 12.2 Apparatus — kept, labelled as apparatus

- **The thermostat form** and its two controls: the balance equation, the un-fed reproduction of T2571's $10^{-149}$, and the shot record with the exponent $2p/(2-p)$ left unforced — `notes/BST_paper_The_Thermostat_Closes_as_Structure_*_2026-08-26.md`, `notes/Elie_LANE_LAMBDA_SHOT_RECORD_*_2026-08-26.md`, the pre-registration with the 280-quarantine. The pincer a referee can run: pick any $p \in (0,2)$, compute, compare — and see that the *value* was never fixed by the form.
- **The Fano-factor arithmetic** (T2546): $\mathrm{Fano} = 1 - \sum\langle N_i\rangle^2/\sum\langle N_i\rangle$, $\approx 0.73$ degenerate $\to 1$ dilute; the everpresent-$\Lambda$ comparison it falsifies against is named in the row.
- **The May closed form as arithmetic:** $(\ln 138/50)\,\alpha^{56}e^{-2} = 2.8993\times10^{-122}$ in Planck units against the observed $2.90\times10^{-122}$ — a match of the K1813 class (an integer exponent and a shape's small integers landing on a target), kept so nobody re-derives it as new.
- **The $6/5$ ruling's instrument** (Cal Section 934, Elie 5746): with the true genus the same construction gives $-30.6\%$, $-16.8\%$ or $+66.5\%$; only at the registered value does it give $0.11\%$.

### 12.3 Tier line

- **Derived:** $\Lambda > 0$ and its Pauli-suppressed fluctuations (T2546); $\Lambda$ Pauli-frozen at $10^{-149}$ against $10^{-121.6}$ (T2571); the causal order (T2564).
- **Closed structural form, one named obstacle:** $\Lambda/\Lambda_P = (t_K/t_P)^{2p/(2-p)}$, $p \in (0,2)$ free; conditional at every site (K1057); no value claimed.
- **Identified:** the May $\alpha^{56}$ form's match; the $6/5$ refinement and everything that inherits it ($\Lambda$ refinement, $H_0$ at 0.12 %, T1924).
- **Retired with this section:** "$\Lambda$ derived to 0.025 % with no free parameters"; "$\Lambda$ is not constant / varies with local density" (contradicts T2571); the Hubble-tension resolution and directional $H_0$ as predictions; $\Omega_\Lambda = F_{\rm BST}$ (collides with $13/19$ in the same text).
- **Live falsifiers:** a forced $p$ outside $(0,2)$; everpresent-$\Lambda$ fluctuations at Sorkin's Poisson level (T2546).
- **Not claimed:** $\Lambda$'s value; the Hubble constant; a mechanism for $p$.

*What would make this section wrong:* a forced $p$ outside $(0,2)$; $\Lambda$-fluctuations measured at the Poisson level; a $\Lambda$ that drifts.

### 12.4 May 2026 record

*Below: the May 2026 text, unedited on 2026-09-14 (the 2026-08-26 banner that stood above it is now 12.1's second paragraph). Read with 12.1–12.3 in hand: its "not constant" is contradicted by T2571; its closed form and its $H_0$ are identifications after the 2026-09-09 ruling; its Friedmann section collides with itself on $\Omega_\Lambda$; its neutrino–$\Lambda$ "genus" is the retired 7.*

#### May 12.1 — The Cosmological Constant Is Not Constant

The standard cosmological constant $\Lambda$ is treated as a uniform property of spacetime — the same everywhere, unchanging. BST contradicts this directly.

If the 3D expression of reality is a statistical macrostate computed from the partition function on $D_{IV}^5$, then the vacuum energy density is a thermodynamic quantity — the free energy density of the substrate in its local equilibrium state. Like all thermodynamic quantities, it depends on local conditions. Specifically, it depends on the local contact density, which varies with the local matter density.

The vacuum energy is not a cosmological constant. It is vacuum pressure — a local, thermodynamic, state-dependent quantity.

#### May 12.2 — Spatial Variation of Vacuum Pressure

BST predicts that the vacuum energy density correlates with local matter density:

- In cosmic voids (low contact density, sparse graph): low vacuum pressure, slow expansion
- Along filaments (higher contact density, denser graph): higher vacuum pressure, modified expansion
- Near galaxy clusters (high contact density): highest vacuum pressure outside black holes

The global average over all regions gives the observed mean acceleration of cosmic expansion. Local variations produce measurable deviations.

#### May 12.3 — Resolution of the Hubble Tension

The Hubble tension — the $\sim 8\%$ disagreement between the locally measured expansion rate ($H_0 \approx 73$ km/s/Mpc from supernovae) and the globally inferred rate ($H_0 \approx 67.4$ km/s/Mpc from CMB) — has been a major open problem since $\sim 2014$.

BST resolves this: **both measurements are correct — they measure different things.**

The CMB measurement gives the **background floor** — the natural expansion rate of the substrate at the time the radiation was generated. CMB photons traveled most of their journey through low-commitment-density space (voids, intergalactic medium). This floor is set by the substrate geometry and the Reality Budget. It does not budge.

The local measurement (SH0ES, z < 0.15) looks **through the highly committed matter streams** of the local large-scale structure — filaments, walls, the Great Attractor, Laniakea. The committed matter adds velocity to the measurement. Standard corrections account for gravitational peculiar velocities but not for the vacuum pressure variation from locally elevated contact density, because standard cosmology assumes constant $\Lambda$.

**Predictions:**

1. Supernovae in denser environments should give systematically higher $H_0$ after standard peculiar velocity corrections. Supernovae in voids should approach the CMB value.
2. **Cleanest test:** Measure $H_0$ through voids vs. through filaments. BST predicts a directional dependence of the local Hubble rate that tracks commitment density. $\Lambda$CDM with particle dark matter predicts no such directional dependence. Testable with DESI/Rubin environment-selected SN Ia samples.
3. The residual correlation magnitude gives the thermodynamic susceptibility $\partial \Lambda / \partial \rho_{\text{matter}}$, computable from the $D_{IV}^5$ partition function.

#### May 12.4 — Resolution of the Coincidence Problem

Standard cosmology has no explanation for why the dark energy density ($\sim 68%$ of critical density) and matter density ($\sim 32%$) are comparable at the present epoch. In a universe with truly constant $\Lambda$, this coincidence requires fine-tuning of initial conditions.

BST dissolves this problem. If vacuum pressure is thermodynamically coupled to matter density, the two track each other. When matter density is high (early universe), vacuum pressure is high. As matter dilutes with expansion, vacuum pressure adjusts. They remain in rough thermodynamic equilibrium because they are both determined by the same substrate state. The “coincidence” is simply thermodynamic equilibrium, no more mysterious than the pressure of a gas tracking its density.

#### May 12.5 — Resolution of the Cosmological Constant Problem

The “worst prediction in physics” — the 120-order-of-magnitude discrepancy between the QFT vacuum energy calculation and the observed value — arises from summing zero-point energies of all quantum field modes. This sum diverges quartically.

In BST, the vacuum energy is not computed by mode summation. It is the free energy density of the substrate, computed from the partition function with Haldane exclusion statistics. The exclusion constraint (maximum 137 circuits per channel) provides a natural UV cutoff that prevents the divergent sum. The resulting vacuum energy is finite, small, and determined by the domain geometry.

**Result (March 2026).** The cosmological constant has been derived in closed form from BST geometry alone:

$$\boxed{\Lambda \;=\; \frac{\ln(N_{\max}+1)}{2n_C^2} \;\times\; \alpha^{8(n_C+2)} \;\times\; e^{-2}}$$

Every factor is purely geometric. Substituting $n_C = 5$, $N_{\max} = 137$, $\alpha = 1/137.036$ — with $8(n_C+2) = 8\times 7 = 56$ and $2n_C^2 = 2\times 25 = 50$:

$$\Lambda \;=\; \frac{\ln 138}{50} \;\times\; \alpha^{56} \;\times\; e^{-2} \;=\; 2.8993 \times 10^{-122} \;\text{Planck units}$$

matching the observed $2.90 \times 10^{-122}$ to 0.025% with no free parameters.

The vacuum free energy $F_{\mathrm{BST}} = \ln(N_{\max}+1)/(2n_C^2)$ is an exact closed-form expression: the Haldane ground state entropy $\ln(N_{\max}+1) = \ln 138$ divided by $2n_C^2 = 50$, the product of the complex and real dimensions of $D_{IV}^5$. The physical inverse temperature $\beta_{\mathrm{phys}} = 2n_C^2$ is fixed geometrically by the condition that the Bergman oscillator zero-point energy $E_0 = \tfrac{1}{2}$ equals $n_C^2 = 25$ thermal quanta — the domain is in a deeply quantum regime, dominated by geometry rather than thermal fluctuations.

The equivalent statement for the committed contact scale:

$$\frac{d_0}{\ell_{\mathrm{Pl}}} \;=\; \alpha^{14} \;\times\; e^{-1/2} \;=\; \alpha^{2(n_C+2)} \;\times\; e^{-1/2}$$

where $n_C = 5$ is the complex dimension of $D_{IV}^5$. The power $14 = 2(n_C + 2)$ decomposes as: $\alpha^{2n_C}$ from the contact area in the bulk of $D_{IV}^5$, $\alpha^2$ from the $S^1$ factor of the Shilov boundary $\Sigma = S^4 \times S^1$, and $\alpha^2$ from the normal-direction quantum oscillator. The factor $e^{-1/2}$ is the quantum amplitude for completing one $S^1$ winding in the Bergman metric of $D_{IV}^5$.

**The $S^1$ winding origin of $e^{-1/2}$.** A channel pair on $\Sigma = S^4 \times S^1$ is \textit{committed} if and only if it has winding number 1 around the $S^1$ direction — uncommitted pairs have winding number 0. Commitment requires traversing $S^1$ once, a topological event that cannot be undone by local fluctuations. Three equivalent derivations give the same amplitude: (1) the committed contact is a quantum oscillator in the Bergman metric with ground state energy $E_0 = \tfrac{1}{2}\hbar\omega_B = \tfrac{1}{2}$ in Bergman natural units, giving weight $e^{-E_0} = e^{-1/2}$; (2) the winding energy for one $S^1$ traversal with Bergman effective mass $m_{\rm eff} R_B^2 = \hbar^2$ is $E_{\rm wind} = \tfrac{1}{2}$; (3) the instanton action for tunneling from winding-0 to winding-1 is $S_{\rm inst} = \tfrac{1}{2}$, giving amplitude $e^{-S} = e^{-1/2}$. All three agree because the Bergman geometry of $D_{IV}^5$ sets a unique natural unit in which the minimal $S^1$ winding action is exactly $\tfrac{1}{2}$. Raising to the 4th power for the four-dimensional contact area: $(e^{-1/2})^4 = e^{-2}$.

The cosmological constant is small because $\alpha \approx 1/137$ appears to the 56th power. That smallness is not fine-tuned — it is the geometric consequence of $D_{IV}^5$ having complex dimension $n_C = 5$, forced by the CR dimension of the Standard Model gauge structure. The "worst prediction in physics" is resolved: the Haldane exclusion cap ($N_{\max} = 137$) plus the committed contact geometry gives a finite, derivable result rather than a divergent mode sum.

**The neutrino–$\Lambda$ connection (March 2026).** The committed contact scale $d_0/\ell_{\rm Pl} = \alpha^{14} \times e^{-1/2}$ and the neutrino mass $m_{\nu_2}/m_{\rm Pl} \sim \alpha^{14}$ share the same power of $\alpha$, where $14 = 2(n_C+2) = 2 \times \text{genus}$. This means $\Lambda \sim \alpha^{56} = (\alpha^{14})^4 \propto m_\nu^4$. The "cosmic coincidence" — that $\Lambda^{1/4} \sim m_\nu$ — is a geometric identity: both the vacuum energy and the neutrino mass scale are determined by the same exponent, $2 \times \text{genus of } D_{IV}^5$. The massless $\nu_1$ IS the vacuum quantum — the propagating mode of the $D_{IV}^5$ vacuum itself. Neutrino oscillation is the vacuum shifting between geometric modes. See `notes/BST_VacuumQuantum_NeutrinoLambda.md`.

Full derivation and verification: `notes/BST_Lambda_Derivation.md`.

#### May 12.6 — Hubble Expansion as Committed Contact Graph Growth

The qualitative picture of Section 12.2 — vacuum pressure coupled to contact density — has a precise quantitative form when applied to cosmic expansion.

**Definition.** The *committed contact graph* $G_c(t)$ is the subgraph of all channel pairs that have permanently exchanged substrate state. Let $A_c(t)$ denote the area of $G_c(t)$ on the Shilov boundary $\Sigma$ of $D_{IV}^5$.

**Core relation.** The 3D FLRW scale factor is the square root of the committed contact area:

$$a(t) \;\propto\; \sqrt{A_c(t)}$$

This follows from the isotropic structure of the $S^4$ factor of $\Sigma$: the Bergman metric on $D_{IV}^5$ restricted to the Shilov boundary produces an isotropic measure, so the 3D volume element scales as $A_c^{3/2}$ and the linear scale factor as $A_c^{1/2}$. The Hubble parameter is then:

$$H(t) \;=\; \frac{\dot{a}}{a} \;=\; \frac{1}{2}\,\frac{\dot{A}_c}{A_c} \;=\; \frac{1}{2}\,\frac{d}{dt}\ln A_c(t)$$

**The expansion rate equals half the fractional rate of new contact commitment on the substrate.** This is a property of the information dynamics of the substrate, not of 3D geometry.

**Vacuum limit.** At $T \to 0$ the committed fraction saturates at:

$$f(T \to 0) \;=\; F_{\mathrm{BST}} \;=\; 0.09855 \quad\text{(exact, from partition function)}$$

About 9.9% of all possible channel contacts are committed even in the zero-temperature vacuum, driven by topological adjacency on $\Sigma$. These are the contacts counted by $\Lambda = F_{\mathrm{BST}} \times (d_0/\ell_{\mathrm{Pl}})^4$. The vacuum commitment rate gives the $\Lambda$-driven Hubble floor.

**Single unknown.** Both the cosmological constant and the Hubble parameter share one unknown, $d_0$ (the physical scale of a committed contact pair on $\Sigma$ in Planck units):

$$\Lambda \;=\; F_{\mathrm{BST}} \times \left(\frac{d_0}{\ell_{\mathrm{Pl}}}\right)^4, \qquad H_0 \;\propto\; \left(\frac{d_0}{\ell_{\mathrm{Pl}}}\right)^2$$

Deriving $d_0$ from the partition function simultaneously predicts $\Lambda$ and $H_0$ with no observational input.

**Hubble tension, quantified.** The local distance ladder measures $H$ in an overdense patch of the committed graph. If the local fractional excess of committed contacts is $\delta_c$:

$$\frac{H_{\mathrm{local}}}{H_{\mathrm{cosmic}}} \;=\; \sqrt{1 + \delta_c}$$

The observed ratio $73/67.4 \approx 1.09$ requires $\delta_c \approx 0.19$. This is a prediction, not a parameter: $\delta_c$ should correlate with the local matter overdensity field on scales of $\sim 100$ Mpc. Supernovae in denser environments should give systematically higher $H_0$ after peculiar velocity correction but before vacuum pressure correction. This is the same prediction as Section 12.3, now with a specific functional form.

**H(z) and the uncommitted reservoir.** The cosmic chronometer data shows $H(z)$ rising by $\sim 45\%$ from $z = 0.07$ to $z = 0.75$ — inconsistent with a $\Omega_\Lambda \approx 0.95$ flat universe, which predicts nearly flat $H(z)$. In BST, the rising $H(z)$ is explained by the uncommitted channel reservoir: at higher $z$, a larger fraction of channels was uncommitted and driving faster commitment rates, producing a $(1+z)^{n_c}$ contribution. If $n_c = 3$ (commitment rate proportional to contact area), BST exactly reproduces the ΛCDM functional form $H^2(z) \propto \Omega_\Lambda + \Omega_{\mathrm{eff}}(1+z)^3$ with no dark matter particles — the effective matter term is the uncommitted reservoir draining into committed contacts. The exponent $n_c$ is a geometric quantity derivable from the contact topology of $\Sigma$.

**Numerical estimates** are tabulated in `notes/BST_HubbleConstant_H0.md`. The BST Hubble floor from backfit calculations was $H_0 \approx 58.2$ km/s/Mpc. With the derivation of $\eta = 2\alpha^4/(3\pi)(1+2\alpha)$ (March 2026), the BST value improved dramatically to $H_0 \approx 67.9$ km/s/Mpc — +0.7% from Planck 2018 (67.36). This is the **background floor**. The local value ($\approx 73$) adds the committed matter stream contribution: $H_{\rm local}/H_{\rm floor} = \sqrt{1 + \delta_c} \approx 1.08$ for local overdensity $\delta_c \approx 0.17$. Full details: `notes/BST_HubbleConstant_H0.md`.

**Pure-BST route (April 2026, Toy 903).** With $\Lambda$ derived from the heat kernel chain (Section 15.1a) and $\Omega_\Lambda = 13/19$: $H_0 = c\sqrt{19\Lambda/39} = 68.02$ km/s/Mpc ($0.98\%$ from Planck, $1.2\sigma$). This route uses zero external inputs — not even $\Omega_m h^2$. BST decisively favors Planck ($67.36 \pm 0.54$) over SH0ES ($73.04 \pm 1.04$).

**Full CAMB Boltzmann verification (April 2026).** A complete CAMB run (Toy 677) with BST-derived parameters — $H_0 = 67.29$ km/s/Mpc, $\Omega_b h^2 = 0.02258$, $\Omega_\Lambda = 13/19$, $n_s = 1 - 5/137$, $\tau = 0.054$ — produces a CMB TT power spectrum statistically identical to Planck. Central result: $\chi^2/N = 0.01$ over 2500 multipoles, RMS deviation 0.276%. All three acoustic peaks match: $\ell_1 = 220$ (exact), $\ell_2 = 537$ ($\pm 1$), $\ell_3 = 813$ (exact). Recombination redshift $z_* = 1089.71$ (0.4$\sigma$ from Planck $z_* = 1089.94$). Sound horizon $r_* = 144.17$ Mpc (1.0$\sigma$). The earlier $\ell_A$ tension (7.6$\sigma$ from Toy 675 analytic approximation) was a method artifact — the full Boltzmann treatment resolves it completely. See `notes/BST_Paper15_CMB_Draft.md` and Toys 673–678.

**The Friedmann equation is the contact commitment rate equation.** Every term in the standard Friedmann equation corresponds to a distinct commitment regime on the substrate:

| Friedmann term | ΛCDM interpretation | BST identification |
|---|---|---|
| $\Omega_r(1+z)^4$ | photon + neutrino density | radiation-mode commitments; rate $\propto T^4$ |
| $\Omega_b(1+z)^3$ | baryon density | committed baryon-mode contacts |
| $\Omega_{\mathrm{DM}}(1+z)^3$ | dark matter density | **uncommitted reservoir draining** at rate $\propto (1+z)^3$ |
| $\Omega_\Lambda$ | cosmological constant | $F_{\mathrm{BST}} = 0.09855$, vacuum committed fraction |

The dark matter term requires no dark matter particles. It is the uncommitted channel reservoir — channels not yet permanently linked — draining into committed contacts as the universe evolves. The $(1+z)^3$ scaling is not imposed; it follows from the volume density of channel pairs on $\Sigma$ (Section 12.7). $\Lambda$CDM is the correct effective phenomenology of BST: it fits the contact commitment rate equation with good empirical parameters, but without knowing what those parameters mean. The full derivation is in Section 12.7.

#### May 12.7 — The Friedmann Equation from First Principles: Full Derivation

##### May 12.7.1 — Setup and Definitions

Let $\Sigma$ denote the Shilov boundary of $D_{IV}^5$, the physical substrate. Define:

- $N_{\mathrm{total}}$ — total channel pairs on $\Sigma$ (constant; fixed by BST geometry)
- $N_c(t)$ — committed contact pairs at time $t$
- $N_u(t) = N_{\mathrm{total}} - N_c(t)$ — uncommitted reservoir
- $A_0$ — area on $\Sigma$ per committed contact pair (a BST geometric constant, equivalent to $d_0^2$)
- $A_c(t) = N_c(t) \cdot A_0$ — total committed area on $\Sigma$

The FLRW scale factor is proportional to the square root of the committed area:

$$a(t) \;\propto\; \sqrt{A_c(t)} \;=\; \sqrt{N_c(t) \cdot A_0}$$

This follows from the isotropy of the $S^4$ factor of $\Sigma$: the Bergman metric on $D_{IV}^5$, restricted to its Shilov boundary, produces an isotropic area measure. The 3D volume element at any epoch scales as $A_c^{3/2}$, giving the linear scale factor $a \propto A_c^{1/2}$. The Hubble parameter is:

$$\boxed{H(t) \;=\; \frac{\dot{a}}{a} \;=\; \frac{1}{2}\frac{\dot{N}_c}{N_c}}$$

The expansion rate is half the fractional rate at which new channel contacts are committed.

##### May 12.7.2 — The Three Commitment Regimes

The rate of new commitments $\dot{N}_c$ depends on two factors: the number of uncommitted pairs available, and the energy density driving commitment at that epoch. Three physically distinct regimes are present:

**Regime 1 — Radiation (early universe, $T \gg T_c$):**
High-energy substrate modes commit at a rate proportional to $T^4$ (Stefan-Boltzmann scaling of the radiation energy density). The committed radiation-mode contact density $\rho_{\mathrm{rad}}$ scales as $(1+z)^4$ as the universe cools and the photon wavelengths redshift:

$$\frac{\dot{N}_c^{(\mathrm{rad})}}{N_c} \;\propto\; (1+z)^4$$

**Regime 2 — Matter-like (intermediate, $T < T_c$):**
After the BST phase transition at $T_c = 0.487$ MeV, the substrate enters its spatial phase. The uncommitted reservoir $N_u$ commits at a rate proportional to the local contact density on $\Sigma$. As the universe expands by factor $a$, the 3D volume grows as $a^3$, so the channel pair density falls as $a^{-3} \propto (1+z)^3$. The commitment rate per uncommitted pair:

$$\frac{\dot{N}_c^{(\mathrm{mat})}}{N_c} \;\propto\; \frac{N_u}{N_c} \cdot (1+z)^3$$

This is the key step. The $(1+z)^3$ exponent — identical to that of cold dark matter — is not imposed. It is the inverse volume scaling of contact density on the substrate. The uncommitted reservoir drains matter-like because contact density scales as volume$^{-1}$.

**Regime 3 — Vacuum ($T \to 0$, today):**
At zero temperature, thermally-driven commitments cease. The committed fraction saturates at $F_{\mathrm{BST}} = 0.09855$ (exact from the partition function). The residual commitment rate from quantum fluctuations is small and constant, driving the $\Lambda$-dominated floor. The vacuum energy density $\rho_\Lambda = F_{\mathrm{BST}} \times (d_0/\ell_{\mathrm{Pl}})^4 \times \rho_{\mathrm{Pl}}$ is constant by definition: it is the zero-temperature free energy of the substrate.

##### May 12.7.3 — Recovery of the Friedmann Equation

Combining all three regimes, the total fractional commitment rate at redshift $z$ is:

$$\frac{\dot{N}_c}{N_c} \;=\; 2H_0 \left[\Omega_r(1+z)^4 \;+\; \Omega_b(1+z)^3 \;+\; \Omega_u(1+z)^3 \;+\; \Omega_\Lambda\right]^{1/2}$$

where $\Omega_u \equiv N_u(0)/N_{\mathrm{total}}$ is the uncommitted reservoir fraction today, and the factor of 2 comes from $H = \frac{1}{2}\dot{N}_c/N_c$. Squaring and substituting $H = \frac{1}{2}\dot{N}_c/N_c$:

$$H^2(z) \;=\; H_0^2\left[\Omega_r(1+z)^4 \;+\; \Omega_b(1+z)^3 \;+\; \Omega_u(1+z)^3 \;+\; \Omega_\Lambda\right]$$

This is the standard flat Friedmann equation with $\Omega_u$ playing the role of $\Omega_{\mathrm{DM}}$. No dark matter particles appear. The matter term in the Friedmann equation is the uncommitted channel reservoir.

##### May 12.7.4 — Identification of the Dark Matter Term

In $\Lambda$CDM, the dark matter density parameter $\Omega_{\mathrm{DM}} \approx 0.264$ is fit from observations and left unexplained. In BST:

$$\Omega_{\mathrm{DM}}^{(\Lambda\mathrm{CDM})} \;\longleftrightarrow\; \Omega_u \;=\; \frac{N_u(0)}{N_{\mathrm{total}}} \;=\; 1 - F_{\mathrm{BST}} - \Omega_b - \Omega_r$$

This is not a free parameter. Once $F_{\mathrm{BST}}$, $\Omega_b$, and $\Omega_r$ are derived from the partition function (the first two from baryon asymmetry and channel mode counting, the third from the CMB temperature), $\Omega_u$ is determined. The dark matter abundance is the uncommitted fraction of the substrate — a geometric fact about $D_{IV}^5$, not a property of an undiscovered particle.

This identification explains immediately why dark matter:
- Does not interact with light (uncommitted channels carry no photon-mode committed state)
- Clusters like matter (commitment rate traces local contact density, which traces baryonic density)
- Has never been detected as a particle (there is no particle; there is only an uncommitted reservoir)
- Has the same $(1+z)^3$ scaling as baryons (both scale as volume density on $\Sigma$)

##### May 12.7.5 — Why $\Lambda$CDM Is the Correct Effective Theory

$\Lambda$CDM works because it correctly fits the contact commitment rate equation to cosmological data. Its four parameters ($H_0$, $\Omega_b$, $\Omega_{\mathrm{DM}}$, $\Omega_\Lambda$) are real physical quantities in BST — they are not wrong, they are incomplete. What $\Lambda$CDM lacks is the interpretation: $\Omega_{\mathrm{DM}}$ is the uncommitted reservoir, $\Omega_\Lambda$ is $F_{\mathrm{BST}}$, and $H_0$ is the current fractional commitment rate.

$\Lambda$CDM fails precisely where this interpretation matters:

| $\Lambda$CDM failure | BST explanation |
|---|---|
| Hubble tension | Local $H$ reflects local contact density; $H_{\mathrm{local}}/H_{\mathrm{cosmic}} = \sqrt{1+\delta_c}$ |
| No DM detection | $\Omega_u$ is an uncommitted reservoir, not a particle species |
| $\Lambda$ fine-tuning | $\Omega_\Lambda = F_{\mathrm{BST}} = 0.09855$ is exact from the partition function |
| Coincidence problem | $\Omega_u$ and $\Omega_\Lambda$ both come from $F_{\mathrm{BST}}$; they are thermodynamically coupled |
| High-$z$ $H(z)$ tension | $\Omega_u$ is not conserved: the reservoir actively drains; $H(z)$ deviates from $\Lambda$CDM at $z \gtrsim 2$ |

The last row is a distinctive prediction: at $z > 2$, when significant commitment was still occurring, the uncommitted fraction $N_u/N_{\mathrm{total}}$ was larger than its present value, and the effective $\Omega_u(z) > \Omega_u(0)$. BST $H(z)$ should be systematically higher than $\Lambda$CDM at $z > 2$, detectable in 21cm hydrogen surveys and high-redshift CMB lensing.

##### May 12.7.6 — The Single Remaining Unknown

Every quantity in the Friedmann equation is now either:
- **Known exactly**: $F_{\mathrm{BST}} = 0.09855$, $T_{\mathrm{CMB}} = 2.725$ K, $\Omega_r h^2 = 4.18 \times 10^{-5}$
- **Derivable from partition function**: $\Omega_b h^2$ (baryon asymmetry), $n_c$ (commitment exponent), $\Omega_u$ (uncommitted fraction)
- **Shared unknown**: $d_0/\ell_{\mathrm{Pl}}$ — the physical scale of one committed contact pair on $\Sigma$

The single remaining unknown $d_0$ appears in both:

$$\Lambda \;=\; F_{\mathrm{BST}} \times \left(\frac{d_0}{\ell_{\mathrm{Pl}}}\right)^4 \qquad\text{and}\qquad H_0 \;\propto\; \left(\frac{d_0}{\ell_{\mathrm{Pl}}}\right)^2$$

The cosmological constant problem and the Hubble constant problem are the same problem: derive $d_0$ from the partition function on $D_{IV}^5$. Backfit calculations constrain $d_0 \approx 7.37 \times 10^{-31}\,\ell_{\mathrm{Pl}}$ from observed $\Lambda$. A first-principles derivation of this number — the area per committed contact pair on the Shilov boundary — completes the cosmological prediction of BST.

-----

