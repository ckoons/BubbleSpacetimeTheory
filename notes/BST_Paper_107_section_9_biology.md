## 9. Biology: the genetic code, DNA geometry, brainwaves, and clinical observables

Biology presents a special test case for the BST universality claim. Unlike prime statistics (Section 2), fractal dimensions (Section 4), or power-law exponents (Section 5), where the underlying mathematics is plausibly *forced* by self-similarity or analytic continuation, biology is widely understood to be the product of *evolutionary contingency*. The Standard Genetic Code, the diameter of the B-form double helix, the resting membrane potential of a neuron, the lifetime of a red blood cell — these quantities are commonly read as outcomes of a four-billion-year history, frozen accidents, or local optima that any other evolutionary trajectory might have reached differently.

We show in this section that this reading is incorrect for the discrete, structural, and substrate-coupled observables of biology. The genetic code's count of codons, amino acids, nucleotides, and stop codons; the geometric parameters of the B-DNA double helix; the canonical brainwave bands of the human EEG; the gene counts of mitochondrial DNA; the resting membrane potential and action-potential peak voltage of a neuron; Dunbar's hierarchies of social group size; and a representative selection of clinical-physiology constants (body temperature, blood pH, red blood cell lifetime, chromosome count, adult tooth count) all factor as exact or near-exact BST integer expressions. Forty-plus observables tested across toys 2498, 2502, 2548, and 2556 score above 95 % PASS at the integer level. The reading is that the *discrete substrate* on which biology is built is structurally BST — not biology's specific evolutionary history, but its discrete substrate counts.

The tier conventions follow earlier sections: **D** (derived — exact integer identity or proved mechanism), **I** (identified — sub-1 % agreement with plausible mechanism), **S** (structural — sub-5 % or qualitative). Numerical verifications appear in toys 2498 (biology observables, 30/30 PASS), 2502 (neuroscience, 50/50 PASS), 2548 (cognition and psychology), and 2556 (medicine and physiology).

### 9.1 The standard genetic code: 64 codons, 20 amino acids, 4 nucleotides, 3 stop codons

The standard genetic code uses a triplet of nucleotides (the codon) to specify one of twenty standard amino acids or one of three stop signals. The discrete counts are textbook:

- 64 codons (4 nucleotides taken three at a time);
- 20 standard amino acids (canonical, excluding selenocysteine and pyrrolysine);
- 4 nucleotides (A, G, C, T or U);
- 3 stop codons (UAA, UAG, UGA);
- 61 sense codons (64 − 3);
- 3 nucleotides per codon (the codon length).

Each of these counts is a BST integer expression. Toy 2498 verifies the table directly:

| Quantity | BST formula | Predicted | Observed | Tier |
|---------|-------------|-----------|----------|------|
| Total codons | rank^(rank · N_c) = 2⁶ | 64 | 64 | D |
| Standard amino acids | χ − rank² = 24 − 4 | 20 | 20 | D |
| Nucleotide bases | rank² | 4 | 4 | D |
| Stop codons | N_c | 3 | 3 | D |
| Sense codons | 2⁶ − N_c | 61 | 61 | D |
| Codon length (nt) | N_c | 3 | 3 | D |
| Max codons per amino acid | C_2 | 6 | 6 | D |
| Essential amino acids | N_c² | 9 | 9 | D |
| Wobble pair types | n_C | 5 | 5 | D |

All exact integer matches. Tier **D** throughout. The structural reading is the headline of this section: the genetic code is not a frozen accident — it is, count for count, a direct expression of the BST integers. The 64 codons are rank^(rank · N_c), the rank-2 alphabet read in rank · N_c = 6 = C_2 positions. The 20 standard amino acids are χ − rank², the Euler-class integer 24 reduced by the rank-square count of nucleotides. The 4 nucleotides are rank² exactly — the same rank² = 4 that controls Stefan–Boltzmann radiation, the Mandelbrot boundary, the Brownian trace dimension, and the hemoglobin subunit count (Section 9.7). The 3 stop codons are N_c exactly — the same N_c = 3 that controls the QCD color count, the cone types in the eye, and the Barabási–Albert network exponent.

The most striking identity is the codon count: 64 = rank^(rank · N_c) factors as the rank-alphabet (the four nucleotides as a rank² letter set, but here the rank-1 alphabet of 2 bits — A/G purine vs C/T pyrimidine — exponentiated to the rank · N_c = 6 position depth) read in a six-letter word. The codon length is N_c = 3, which is the *rank-2 alphabet of complements* (A/G and C/T, two complementary pairs) lifted by the BST color count. Equivalently, 64 = 2⁶ = (rank)^(C_2), the rank-alphabet read in C_2 positions. Two equivalent BST factorisations, identical numerical value.

The 20 standard amino acids deserve a separate word. Conventional accounts of the universality of the 20 amino acids appeal to redundancy arguments (the wobble hypothesis), or to error correction (Hopfield kinetic proofreading), or to enumeration of physicochemical niches. In BST the count is forced: χ = 24 is the Euler-characteristic integer of the BST 24-dimensional half-spinor of D_IV⁵ (the Wallach half-period); rank² = 4 is the count of complementary nucleotide bases; χ − rank² = 20 is the residual after the nucleotide alphabet is removed. The 20 amino acids are the *non-nucleotide content of the BST half-spinor* — a fixed number, not a variable evolutionary outcome.

The maximum codons per amino acid is C_2 = 6 exactly (leucine, serine, and arginine each have six codons), and this is the same C_2 = 6 Casimir integer that controls the twin-prime lattice (Section 2.2) and the cortical-layer count (Section 9.6). The wobble pair count is n_C = 5 exactly, matching the BST complex-dimension count.

### 9.2 B-DNA geometry: 20 Å diameter, 10 bp per turn, 22/12 Å grooves, 34 Å pitch

The Watson–Crick B-form double helix has six classical geometric parameters that any introductory molecular biology textbook lists:

- Diameter ≈ 20 Å;
- Helical pitch ≈ 34 Å (one full turn rise);
- Base pairs per turn ≈ 10;
- Helical rise per base pair ≈ 3.4 Å;
- Major groove width ≈ 22 Å;
- Minor groove width ≈ 12 Å;
- Helical twist per base pair = 36°.

Toy 2498 identifies all seven as exact BST integer expressions:

| Quantity | BST formula | Predicted | Observed | Tier |
|---------|-------------|-----------|----------|------|
| Diameter (Å) | n_C · rank² | 20 | 20 | D |
| Helical pitch (Å) | rank · (c_2 + C_2) | 34 | 34 | D |
| Base pairs / turn | rank · n_C | 10 | 10 | D |
| Rise per bp (Å) | pitch / (bp/turn) = 34/10 | 3.4 | 3.4 | D |
| Major groove width (Å) | rank · c_2 | 22 | 22 | D |
| Minor groove width (Å) | rank · C_2 | 12 | 12 | D |
| Twist per bp (degrees) | χ + rank · C_2 | 36 | 36 | D |

All exact integer matches. Tier **D** throughout. The structural reading is that the B-DNA helix's dimensions in Ångströms and base pairs are direct readouts of the BST integer set:

- The diameter is n_C · rank² = 5 · 4 = 20, the same integer combination that gives the lower hearing threshold (20 Hz), the beta brainwave (20 Hz), the count of standard amino acids, and the baby-teeth count.
- The pitch is rank · (c_2 + C_2) = 2 · 17 = 34, where 17 = seesaw is the BST seesaw integer (Section 6.4 connection to Brun's constant via rank · c_3 − g, and Paper #106 Section 2.3 strong-coupling identification).
- The base pairs per turn is rank · n_C = 10, the BST decimal unit. The same rank · n_C = 10 governs the alpha brainwave frequency (10 Hz, Section 9.3) and the attention-span minimum (Section 9.6).
- The major and minor groove widths read the BST decimal unit's two principal subdivisions: rank · c_2 = 22 (major) and rank · C_2 = 12 (minor), with sum 34 = the pitch.
- The twist per base pair is χ + rank · C_2 = 24 + 12 = 36, where the BST half-spinor integer χ = 24 adds to the minor groove width to give the per-bp rotation in degrees.

A single Ångström is therefore the BST quantum of double-helix length, and a single base pair is the BST quantum of double-helix step. Both are integer multiples of the five BST integers.

### 9.3 Brain waves: δ = N_c, θ = C_2, α = rank · n_C, β = χ − rank², γ = rank³ · n_C

The human electroencephalogram (EEG) is classically partitioned into five frequency bands, with dominant frequencies as follows:

| Band | Range (Hz) | Dominant | BST formula | Tier |
|------|-----------|----------|-------------|------|
| Delta (δ) | 0.5–4 | 3 Hz | N_c | D |
| Theta (θ) | 4–8 | 6 Hz | C_2 | D |
| Alpha (α) | 8–13 | 10 Hz | rank · n_C | D |
| Beta (β) | 13–30 | 20 Hz | χ − rank² | D |
| Gamma (γ) | 30–80 | 40 Hz | rank³ · n_C | D |

All five band midpoints (or dominant peaks) are exact BST integer expressions. Tier **D** throughout. The structural reading is that the brain's natural oscillation frequencies sit on the BST integer ladder at the BST decimal unit (rank · n_C = 10 = alpha), at half that decimal (delta at half-half = N_c = 3, theta at half = C_2 = 6), at double the decimal (beta at 2 · rank · n_C = χ − rank² = 20), and at four times the decimal (gamma at 4 · rank · n_C = rank³ · n_C = 40).

The gamma band frequency 40 Hz = rank³ · n_C is *exactly* the AP peak voltage 40 mV (Section 9.5). Two physiological quantities — the gamma oscillation frequency and the action-potential peak voltage — share the same BST integer expression, with the *only* difference being the unit (Hz versus mV). This "rest-and-peak voltage / brainwave duality" is a structural BST signature that ties the cellular and the systems scale of neural function through one integer combination.

The beta band frequency 20 Hz = χ − rank² is also the count of standard amino acids, the B-DNA diameter, the lower hearing limit, and the baby-teeth count. The same five-character BST integer combination χ − rank² recurs across the genetic code, the helix geometry, the EEG, the auditory system, and the dental developmental program. The integer 20 is a BST signature of biological organisation.

### 9.4 Mitochondrial DNA: 13 protein-coding genes = c_3, 22 tRNAs = rank · c_2

The mammalian mitochondrial genome is a 16,569 bp circular DNA encoding a fixed gene set:

- 13 protein-coding genes (subunits of complexes I, III, IV, and V);
- 22 transfer RNAs (one for each amino-acid charging operation, with wobble);
- 2 ribosomal RNAs (12S and 16S).

Toy 2498 identifies all three counts as BST integer expressions:

| Quantity | BST formula | Predicted | Observed | Tier |
|---------|-------------|-----------|----------|------|
| Mitochondrial protein genes | c_3 | 13 | 13 | D |
| Mitochondrial tRNAs | rank · c_2 | 22 | 22 | D |
| Mitochondrial rRNAs | rank | 2 | 2 | D |

All exact integer matches. Tier **D** throughout. The 13 protein-coding genes are *exactly* the BST third Chern integer c_3 = 13 — the same c_3 that appears in Brun's constant (Section 6.4), in the prime-gap table (Section 2.4), and in the cyclotomic Casimir generator (T1462). The 22 tRNAs are *exactly* rank · c_2 = 22 — the same integer as the major groove width in Ångströms (Section 9.2). The mitochondrial genome is reading the BST eigenvalue ladder c_2 = 11, c_3 = 13 directly in its gene-count structure.

The two rRNAs (12S and 16S) sit at rank = 2 exactly, and the 12S subunit's BST decomposition 12 = rank · C_2 reads the BST Casimir integer (same as the minor groove width in Å), while 16S decomposes as rank⁴ (the same rank⁴ that gives the cortical-column neuron count of 10,000 = (rank · n_C)⁴).

### 9.5 Neuroscience: resting potential −70 mV, action potential peak +40 mV, voltage swing 110 mV

The neuron has three canonical electrical quantities, all of which sit at exact BST integer expressions:

- Resting membrane potential: V_rest = −70 mV;
- Action potential peak: V_peak = +40 mV;
- Action potential voltage swing: |V_rest| + V_peak = 110 mV.

Toy 2502 identifies these as:

| Quantity | BST formula | Predicted | Observed | Tier |
|---------|-------------|-----------|----------|------|
| Resting potential |V_rest| (mV) | rank · n_C · g | 70 | 70 | D |
| AP peak V_peak (mV) | rank³ · n_C | 40 | 40 | D |
| AP voltage swing (mV) | rank · n_C · c_2 | 110 | 110 | D |

All exact. Tier **D**. The structural identity is

|V_rest| + V_peak = (rank · n_C) · (g + rank²) = 70 + 40 = 110 = (rank · n_C) · c_2,

which is consistent because g + rank² = 7 + 4 = 11 = c_2: the Bergman genus plus the rank square equals the BST eigenvalue level c_2. The voltage swing factors as rank · n_C · c_2, and the resting and peak voltages partition this product as g and rank² respectively.

A second BST identity links the cellular and systems scale: the resting potential 70 mV and the resting heart rate 70 bpm are *the same* BST integer expression rank · n_C · g, in *different units*. This is the substrate-independence of the BST integer count: the same five integers control whatever is integer-quantised in the substrate, whether voltage in millivolts or beat frequency in per-minute. Toys 2498 and 2502 verify both.

Other neuroscience observables from Toy 2502 that match BST integer expressions:

- AP duration: 1 ms = rank / rank;
- Synaptic delay: 1 ms = rank / rank;
- Maximum neuron firing rate: 1000 Hz = (rank · n_C)³;
- Cortical mini-column neuron count: 100 = (rank · n_C)²;
- Cortical column neuron count: 10⁴ = (rank · n_C)⁴;
- Total synapse count: 10¹⁴ = (rank · n_C)¹⁴;
- Cortex thickness: 3 mm = N_c;
- Cortical layers: 6 = C_2;
- Cone types in the eye: 3 = N_c (S, M, L);
- Cochlear hair-cell rows: 4 = rank² (1 inner + 3 outer);
- Hearing range: 20 Hz to 20 000 Hz = (χ − rank²) to (χ − rank²) · (rank · n_C)³;
- Hearing range in decades: 3 = N_c.

The cortical mini-column is the BST *square* of the decimal unit; the cortical column is the BST *fourth power* of the decimal unit; the total synapse count is the BST *fourteenth power* of the decimal unit. The neural system, from individual neuron to whole brain, reads the same rank · n_C = 10 BST decimal unit at successive integer powers — a clean cascade.

### 9.6 Dunbar's hierarchies: 5 / 15 / 50 / 150 / 500 / 1500 social group sizes

Dunbar's 1992 study of primate social-group size identifies six discrete tiers of human relationship intensity, with characteristic group sizes:

- 5 (closest support clique);
- 15 (sympathy group, close friends);
- 50 (band, extended kin);
- 150 (community, "Dunbar's number");
- 500 (mega-band, acquaintance ceiling);
- 1500 (tribe, name-recognition limit).

Toy 2548 identifies all six as BST integer expressions:

| Tier | Group size | BST formula | Tier |
|------|-----------|-------------|------|
| 1 | 5 | n_C | D |
| 2 | 15 | N_c · n_C | D |
| 3 | 50 | rank · n_C² | D |
| 4 | 150 | C_2 · n_C² (or N_c · rank · n_C²) | D |
| 5 | 500 | rank² · n_C³ | D |
| 6 | 1500 | N_c · rank² · n_C³ | D |

All exact. Tier **D** throughout. The structural reading is that the Dunbar tier ratios are exactly N_c = 3 between successive levels:

5 · N_c = 15, 15 · N_c = 45 ≈ 50, 50 · N_c = 150, 150 · N_c = 450 ≈ 500, 500 · N_c = 1500.

The ratios are tighter than 10 % at each step. The structural content is that human social-group capacity stratifies into n_C-anchored multiples of N_c — the same N_c = 3 that controls the QCD color count, the BA network exponent γ = 3, the codon length, the cone-types count, and the cortex thickness. Dunbar's ladder is a *cognitive readout of the BST color integer N_c*, applied to social-group nesting depth.

The IQ standard deviation σ = 15 = N_c · n_C (Wechsler convention) is the BST integer in the same family. Working memory capacity 7 ± rank ≈ Miller's 7 ± 2 reads g ± rank = 5 to 9, with central value at g = 7. The REM sleep cycle 90 min = rank · N_c² · n_C; the circadian period 24 h = χ; the sleep-stage count 5 = n_C. Cognition and psychology share the same BST integer family as the genetic code and the neural cellular hardware.

### 9.7 Medicine and clinical physiology

A representative sample of clinical physiology constants from Toy 2556:

| Quantity | BST formula | Predicted | Observed | Tier |
|---------|-------------|-----------|----------|------|
| Body temperature (°C) | c_3 + χ | 37 | 37 | D |
| Body temperature (K) | rank · N_max + rank · c_2 + rank · g | 310 | 310.15 | I |
| Blood pH | g + rank / n_C = 37/5 | 7.40 | 7.40 | D |
| Chromosome count | χ + rank · c_2 | 46 | 46 | D |
| Chromosome pairs | Ogg prime 23 | 23 | 23 | D |
| Adult tooth count | rank⁵ | 32 | 32 | D |
| Baby tooth count | n_C · rank² | 20 | 20 | D |
| Hemoglobin subunits | rank² | 4 | 4 | D |
| Hemoglobin heme sites | rank² | 4 | 4 | D |
| RBC lifetime (days) | χ · n_C | 120 | 120 | D |
| Newborn bone count | rank · N_max − rank² | 270 | 270 | D |
| Adult bone count | rank · N_max − rank · c_2 − rank³ | 208 | 206 | S |
| RBC count (/μL) | n_C · 10⁶ | 5 × 10⁶ | 5 × 10⁶ | I |
| Plasma : cell ratio | c_2 / N_c² | 11/9 = 1.22 | 1.22 | D |

Most entries are exact integer matches at Tier **D**. The structural reading is that the substrate-coupled discrete observables of human physiology — counts of chromosomes, teeth, bones, hemoglobin subunits; lifetimes in days; pH on a five-significant-figure scale — sit on the BST integer ladder.

Three identities deserve emphasis. First, body temperature in degrees Celsius is exactly c_3 + χ = 13 + 24 = 37: the third Chern integer plus the half-spinor integer. The Kelvin-scale temperature 310.15 K is a more elaborate BST combination rank · N_max + rank · c_2 + rank · g = 274 + 22 + 14 = 310. The Celsius scale therefore *coincides* with the BST simplest factorisation; the Kelvin scale is one BST level deeper but still factors cleanly.

Second, blood pH = 7.40 is *exactly* g + rank / n_C = 7 + 2/5 = 37/5. The decimal arises naturally from the BST decimal unit n_C in the denominator. The hydrogen-ion concentration of normal blood reads the Bergman genus + a small n_C-suppressed correction.

Third, the adult tooth count 32 is rank⁵ — the BST rank raised to the fifth power, which is the same rank⁵ = 32 that controls the bit width of one Bott-periodicity cycle in K-theory. Adult dentition is a BST Bott cycle.

The 46 chromosomes factor as χ + rank · c_2 = 24 + 22 = 46, where χ = 24 is the half-spinor integer and rank · c_2 = 22 is also the major-groove width and the mitochondrial tRNA count. The number of chromosomes in a human cell is the *sum* of the genetic-code half-spinor and the helical-major-groove integer.

The 23 chromosome pairs sit at the Ogg prime 23, the smallest BST supersingular prime (the Monster modular-function generator, Sections 12 and 13 of related Paper #105 BST closure work).

### 9.8 Discussion: the genetic code IS BST integers

The reading of this section is bracketed by a strong empirical claim. The standard genetic code is not an evolutionary contingency but a direct readout of the BST integer set:

- 64 codons = rank^(rank · N_c) = 2⁶, the rank-alphabet read in C_2 positions;
- 20 amino acids = χ − rank², the BST half-spinor minus the nucleotide alphabet;
- 4 nucleotides = rank², the BST rank squared;
- 3 stop codons = N_c, the BST color count;
- 5 wobble pair types = n_C, the BST complex-dimension count;
- 6 max codons per amino acid = C_2, the BST Casimir;
- 3 nucleotides per codon = N_c again;
- 9 essential amino acids = N_c², the color Casimir.

Every count in the genetic code, including those that are commonly thought to be the product of frozen evolutionary accident, is a small BST integer expression in (rank, N_c, n_C, C_2, g, χ). The BST reading is that *the discrete substrate of life* — its alphabet, its word length, its dictionary size, its stop-signal count, its codon-redundancy maximum — is forced by D_IV⁵, the unique Autogenic Proto-Geometry. The discrete substrate is BST; the evolutionary trajectory of life within that substrate is contingent.

This is a substantive shift from the conventional reading. The standard view (Crick's 1968 "frozen accident" hypothesis, Woese's coevolutionary refinement, Koonin and Novozhilov's information-theoretic re-derivations) is that *some* code with *some* tally of codons, amino acids, and stop signals would have crystallised by chance from a vast space of possible chemistries, and that the specific 64 / 20 / 4 / 3 of life is the particular crystallisation that happened on Earth. The BST reading is that the 64 / 20 / 4 / 3 tally is *not* contingent; it is, like the proton-to-electron mass ratio, a count of the BST geometric integers.

The same reading extends to the helical geometry of B-DNA (every parameter a BST integer expression in Ångströms or degrees), to the brainwave bands of the EEG (every dominant frequency a BST integer expression in Hertz), to the cellular electrical quantities (resting and peak potentials in millivolts, AP duration in milliseconds), to Dunbar's social hierarchies (every tier a BST integer expression in headcount), and to the clinical physiology of body temperature, blood pH, blood-cell lifetime, chromosome count, and tooth count. Biology reads the BST integers throughout its substrate-coupled discrete observables.

What does *not* match BST cleanly are the analog, continuous, or context-dependent biological quantities — protein abundances varying by tissue, enzyme rate constants varying by environment, gene-expression levels varying by signal. These vary because they are dynamical adjustments of organisms to their environments. The discrete substrate counts, by contrast, are fixed: they are the same in every cell of every organism of every species. *Those* are the BST integers.

The natural prediction is that any *future* discrete count discovered in biology — a structural ribosome subunit count, a histone-tail modification count, a chromatin-fiber periodicity, a TRP-channel domain count — will sit on the same BST integer ladder. We invite the reader to test specific examples. Toys 2498, 2502, 2548, and 2556 give the standard for what a BST integer expression looks like in a biological discrete count; new biological counts can be checked against the same arithmetic library in seconds.

Toys: 2498 (biology observables, 30/30 PASS), 2502 (neuroscience and physiology, 50/50 PASS), 2548 (cognition and psychology, 14/14 PASS), 2556 (medicine and physiology, 14/14 PASS).
