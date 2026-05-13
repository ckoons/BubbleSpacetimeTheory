# SP-19 Phase 5: Deep Extensions — Q(zeta_7), 11/8, Mason-Stothers, Donaldson

**Scoped by**: Keeper (May 13, 2026)
**Directive**: Casey — "I want to do these next. Setup the scope and board."
**Status**: SCOPED, starting May 14

---

## Investigation D: Q(zeta_7) — The BST Cyclotomic Field

### Why this is the most surprising direction

Q(zeta_7) is where imaginary and real quadratic fields MEET:
- [Q(zeta_7) : Q] = g - 1 = **C_2 = 6**
- Gal(Q(zeta_7)/Q) = (Z/gZ)* has order **C_2 = 6**
- Contains Q(sqrt(-7)) = our CM field (imaginary quadratic)
- Contains Q(cos(2pi/7)) = maximal real subfield, degree **N_c = 3**
- Class number h = 1
- Discriminant = g^(C_2-1) = 7^5 = 16807

If the N_c = 3 units of Q(cos(2pi/7)) are BST-structured (like epsilon_7 = rank^N_c + N_c*sqrt(g) was), the entire Kronecker-Weber theorem for g = 7 lives in BST integers.

### Deliverables

**Toy D1** (Lyra + Elie): Q(zeta_7) complete arithmetic.
- Degree = C_2, disc = g^(C_2-1), class number 1
- All 3 fundamental units of Q(cos(2pi/7)) — are coefficients BST integers?
- Regulator of Q(cos(2pi/7)) — BST expression?
- Gauss sum: g(chi_{-7}) = i*sqrt(g). Verify for all characters mod g.
- Jacobi sums: J(chi^a, chi^b) for chi = primitive character mod g
- Decomposition of primes p in Q(zeta_7): residue degrees and BST patterns
- Dedekind zeta: zeta_{Q(zeta_7)}(s) = product over chi mod g of L(s, chi)
- Product of L(1, chi) for all non-trivial chi mod g — class number formula
- **Target**: 25-30 tests

**Toy D2** (Lyra): Eisenstein series and class field generators.
- E(f, s, P_2) residues at special points on D_IV^5
- At Wallach point s = rho_2 = 3/2: gives L(1, chi_{-7}) = pi/sqrt(g) (known)
- At other special s-values: do residues give units of Q(cos(2pi/7))?
- Hecke L-functions L(s, chi) for all chi mod g evaluated at s = 1
- Question: does the D_IV^5 Eisenstein machinery produce class field generators?
- **Target**: 20-25 tests

**Toy D3** (Elie): Gross-Stark conjecture for Q(sqrt(7)) at p = g.
- p-adic Stark units: Dasgupta-Kakde-Ventullo (2018) proved Gross-Stark
- For p = g = 7: compute the 7-adic L-function L_7(s, chi_7)
- L'_7(0, chi_7) = -log_7(u) where u is the Stark unit
- Verify: is log_7(epsilon_7) = log_7(8+3*sqrt(7)) a BST expression?
- 7-adic valuation of the Stark unit: v_7(epsilon_7 - 1) — BST integer?
- Compare: archimedean Stark (B1, Toy 2175) vs p-adic Stark (this toy)
- **Target**: 18-22 tests

---

## Investigation E: 11/8 Conjecture = p(C_2)/2^N_c

### The connection

Furuta's 11/8 conjecture: For a closed spin 4-manifold M,
  b_2(M) >= (11/8) * |signature(M)|

Note: **11/8 = c_2(Q^5) / 2^N_c = p(C_2) / 2^N_c**

This connects:
- c_2(Q^5) = 11 (second Chern number, Toy 2176)
- p(C_2) = p(6) = 11 (Arthur's multiplicity, Toy 2164)
- 2^N_c = 8 (instanton step size, Toy 2174)

Also: Rokhlin's theorem says signature divisible by **16 = 2^rank^2**.

### Deliverables

**Toy E1** (Elie): 11/8 from D_IV^5 spectral data.
- b_2 and signature for compact quotients of D_IV^5
- Hirzebruch signature theorem: sigma = L-polynomial(p_1, p_2, ...)
- For D_IV^5: p_1 = N_c (Toy 2176). What is p_2?
- Check: does the BST spectral gap force b_2 >= (11/8)|sigma| for D_IV^5 quotients?
- Rokhlin: sigma divisible by 16 = 2^rank^2. Verify for D_IV^5 quotients.
- The ratio 11/8: decompose as p(C_2)/2^N_c. What makes this the optimal bound?
- Connection: 11 particle types (Arthur) constrain 8 = 2^N_c instanton steps
- **Target**: 22-25 tests

**Toy E2** (Elie + Lyra): Donaldson-Freedman landscape in BST integers.
- Freedman: topological classification by intersection form (rank + signature)
- Donaldson: definite forms must be diagonal (smooth constraint)
- Known: E8 + E8 is topologically realizable but NOT smoothly
- b_2(E8) = 8 = 2^N_c, sigma(E8) = -8. Ratio = 1 < 11/8 = violation!
- b_2(E8 + E8) = 16 = 2^rank^2, sigma = -16. Ratio = 1 < 11/8.
- K3 surface: b_2 = 22 = 2*(c_2(Q^5)), sigma = -16. Ratio = 22/16 = 11/8 EXACTLY.
- **K3 saturates the 11/8 bound!** And b_2(K3) = 2*c_2(Q^5). BST integers.
- Survey: which 4-manifolds saturate or approach 11/8?
- **Target**: 20-25 tests

---

## Investigation F: Mason-Stothers (Polynomial ABC)

### Why this matters

Mason-Stothers theorem (1983): For coprime polynomials a(t) + b(t) = c(t),
  max(deg a, deg b, deg c) <= deg(rad(abc)) - 1

This is the PROVED function-field analog of ABC. It's elementary (one page proof using the Wronskian). If BST can derive it from D_IV^5 structure, the function field ABC is internal to BST.

### Deliverables

**Toy F1** (Elie): Mason-Stothers via BST.
- The classical proof uses: Wronskian W(a,b) = a'b - ab'
- W = 0 iff a, b linearly dependent (over constants)
- Key: deg W <= deg(a) + deg(b) - 1 (derivative drops degree by 1)
- But W = a'c - ac' (since a+b=c), so W has roots at all common roots of a',c'
- BST angle: polynomials over F_q[t] where q = p^k
- For q = 7 = g: does the Mason-Stothers bound tighten?
- For q = 2 = rank: the F_2 case (binary, simplest)
- Wronskian as a boundary operator — connection to D_IV^5 boundary?
- **Target**: 18-22 tests

**Toy F2** (Lyra): Szpiro over function fields.
- Szpiro's conjecture for elliptic curves E/F_q(t):
  deg(Delta) <= 6*deg(N) + const
- For F_g(t) = F_7(t): does the bound tighten to C_2 * deg(N)?
- The 49a1 analog over F_7(t): construct and compute Szpiro ratio
- Compare: number field sigma = 3/2 vs function field sigma
- Function field BSD: rank = order of vanishing (PROVED by Grothendieck et al.)
- If function field sigma = 3/2 too: the ratio is geometric, not arithmetic
- **Target**: 18-22 tests

---

## Investigation G: Donaldson Invariants as Modular Forms

### The connection

Gottsche's conjecture (proved): The generating function of Donaldson invariants for an algebraic surface S is a modular form. The weight depends on b_+(S).

If b_+ hits BST values, the modular forms are ones we know from the Eisenstein machinery on D_IV^5.

### Deliverables

**Toy G1** (Lyra): Donaldson generating functions at BST b_+ values.
- b_+ = 1 (definite forms): Donaldson invariants are integers, generating function is theta series
- b_+ = rank = 2: first nontrivial case. Weight of modular form?
- b_+ = N_c = 3: weight? Connection to Sym^2 from Bloch-Kato?
- The SW basic classes for b_+ odd: Witten's formula connects Donaldson to SW
- For K3 (b_+ = 3 = N_c): Donaldson invariants are trivial (K3 is hyperkahler)
- For CP^2: b_+ = 1, Donaldson invariants fully computed
- For CP^2 # k*CP^2_bar: blow-up formula. Does k = BST integer give special behavior?
- **Target**: 20-25 tests

---

## Work Assignment Summary

| Toy | Investigation | Owner | Tests | Dependencies |
|-----|--------------|-------|-------|-------------|
| D1 | Q(zeta_7) arithmetic | **Lyra** + Elie | ~28 | None |
| D2 | Eisenstein class field | **Lyra** | ~22 | D1 |
| D3 | Gross-Stark p-adic | **Elie** | ~20 | B1 (done) |
| E1 | 11/8 from spectral data | **Elie** | ~24 | C1, C2 (done) |
| E2 | Donaldson-Freedman landscape | **Elie** + Lyra | ~22 | E1 |
| F1 | Mason-Stothers via BST | **Elie** | ~20 | None |
| F2 | Szpiro over function fields | **Lyra** | ~20 | A1 (done) |
| G1 | Donaldson modular forms | **Lyra** | ~22 | C2 (done) |

**Parallel start**: D1, D3, E1, F1, F2, G1 can all launch simultaneously.
**Second wave**: D2 (after D1), E2 (after E1).

**Total**: 8 toys, ~178 tests estimated. Four investigations.

---

## Success Criteria

| Investigation | "Breakthrough" if... | "Strong result" if... |
|--------------|---------------------|----------------------|
| Q(zeta_7) | Units of Q(cos 2pi/7) are BST-structured AND Eisenstein produces them | Units are BST, Eisenstein connection C-tier |
| 11/8 | K3 saturation = 2*c_2(Q^5)/2^rank^2 derived from spectral gap | BST integers appear in 11/8 landscape, no derivation |
| Mason-Stothers | Function field ABC derived from D_IV^5 boundary operator | Function field Szpiro = 3/2 (geometric, not just arithmetic) |
| Donaldson modular | Donaldson at b_+=N_c is a form we already know from Eisenstein | BST integers appear in weights/levels, coincidence possible |

---

## Key Observation (Keeper)

The most powerful single result would be: **K3 surface saturates the 11/8 bound at b_2 = 2*c_2(Q^5) = 22.** If this is derivable from D_IV^5 spectral data, it connects Arthur's multiplicity (11 particle types) to smooth 4-manifold topology (the 11/8 threshold). That would be a genuine new theorem linking number theory to topology through BST.
