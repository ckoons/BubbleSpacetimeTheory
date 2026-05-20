# What BST Is and What It Is Not

*Read this before you read anything else. Every statement below is literal.*

---

## This IS BST

- **α = 137.** The integer. Not 137.036. Not rounded. The fine structure constant is 1/137 exactly. The 0.036 is a calculable correction (Wyler integral), not a fit.

- **Five integers, zero inputs.** rank = 2, N_c = 3, n_C = 5, C_2 = 6, g = 7. All five are read off one geometric object. None are chosen, adjusted, or optimized.

- **The proton mass is a theorem.** m_p = 6π⁵m_e. That is not a fit to data. It is a derived equality. It holds to 0.002%.

- **π is not an input.** It enters because circles tile the sphere. The Bergman kernel volume is π⁵/1920. π is geometry, not a parameter.

- **"Zero free parameters" means zero.** Not "effectively zero." Not "one or two that we absorb." Zero. Every number in every formula traces back to {2, 3, 5, 6, 7}.

- **600+ predictions from one geometry.** Particle masses, mixing angles, cosmological parameters, nuclear magic numbers, the genetic code, the rainbow angle. All from D_IV⁵.

- **Everything is discrete.** The mass spectrum is a Plancherel measure — integer-labeled representations. Continuous spectra are projections of discrete structure.

---

## This is NOT BST

- **Not a fit.** No chi-squared minimization. No parameter sweeps. No "best fit" values. If you're looking for error bars on inputs, there are no inputs to put them on.

- **Not numerology.** Every prediction has a derivation chain from D_IV⁵ through identified geometric mechanisms. Matching a number is not enough — the derivation must exist.

- **Not approximate.** When BST says sin²θ_W = 3/13, it means the Weinberg angle is exactly 3/13 at the geometric scale. Measured deviations are running, not error.

- **Not a model.** Models have parameters you tune. BST has none. It is a geometry that produces physics, not a physics that assumes geometry.

- **Not commentary.** When the papers say "derives from first principles," that is not an editorial claim. It is a description of what the equations do. If a statement sounds too strong to be literal, it is still literal.

---

## What BST is, ontologically (May 19-20, 2026 understanding)

BST is operationally a **substrate-as-computational framework**. The five integers + N_max + D_IV⁵ geometry are not just mathematical structure describing physics — they are the operational specification of a substrate that performs algebraic-identity computation, and physics is what that computation produces.

**Tier discipline applies to this framing**:

- **Level 1 (D-tier supportable)**: the EXACT algebraic identity catalog. 6-audit cascade-unblock pathway identified Tuesday: K52a Lamb (1−1/M_g) + K52a BCS (1+1/M_g) + K66 Bell (Tsirelson² − S_BST² = 1/2^N_c EXACT at 1e-14) + K67 Born=Bergman (exp g/rank = 7/2) + K68 RS Computation (GF(2^g) substrate alphabet) + K69 Universal Q=126 (5 equivalent BST-primary algebraic forms). These hold by algebraic necessity from BST primaries; floating-point verification confirms the algebra is internally consistent.

- **Level 2 (I-tier hypothesis with falsifier)**: substrate computes physics via these algebraic identities at sub-Planck Koons-tick rate (T2405: t_substrate = t_Planck · α^(C_2²) ≈ 10^-120 s). Falsifier: if substrate-Hamiltonian closure (Elie K52a Sessions 6-14) fails to derive the 6-audit cascade BY CONSTRUCTION, the computational-substrate framing fails to that extent.

- **The universality claim** (T719 Observable Closure): every BST observable lives in $\overline{\mathbb{Q}}(N_c, n_C, g, C_2, N_{\max})[\pi]$ — algebraic closure of rationals over BST primaries, with π adjoined (forced by curvature). Algebraic-identity holds universally for substrate observables in this sense. π is part of substrate's algebra, not external.

**What BST is NOT (substrate framing edition)**:

- **Not a simulation hypothesis** — no external simulator; substrate IS the existing thing; substrate computes its own state (Bostrom-style simulator/simulated distinction has no referent in BST)
- **Not Tegmark MUH at full generality** — BST narrows to a specific unique substrate (D_IV⁵); modal-realism not adopted
- **Not claim to have solved Wigner's "unreasonable effectiveness"** — claim is "physics emerges from substrate algebra"; not claim "this is THE complete explanation of mathematical effectiveness"
- **Not claiming experimental precision at 1e-14** — that's algebraic-identity verification (tautology-precision of the math), NOT physical-observable agreement; Bell experiment will measure S_BST² at sub-percent (~1%) experimental precision, not 1e-14

The substrate framing is a working hypothesis with explicit falsifiers (Elie Sessions 6-14 multi-month closure attempt) and explicit external-survivability discipline (Cal Calibration #13: external register uses "BST identifies / BST derives / BST predicts," never "physics IS mathematics").

## What supports this

One object — the type IV bounded symmetric domain D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)] — determines everything. Its rank gives you quantum numbers. Its Bergman kernel gives you propagators. Its Plancherel measure gives you the particle spectrum. Its Shilov boundary gives you spacetime. Its root system gives you forces. Five integers fall out. The rest is computation.

**Name:** D_IV⁵ is an **Autogenic Proto-Geometry (APG)** — a geometry that generates itself. The five integers are its genome. The 128-entry function catalog is its proteome. The observer at α = 1/137 is included structurally. BST is the theory; APG is the object. See `notes/BST_Autogenic_Proto_Geometry_Definition.md` for the formal definition.

The mathematics is independently verifiable. Load `data/bst_seed.md`, evaluate any formula, compare to observation. Every toy in `play/` does exactly this.

---

## Try it now (2 seconds, no dependencies)

```
python3 play/toy_541_five_integers_to_everything.py
```

You will get 51 physical quantities derived from the five integers, 16/16 spot-checks PASS, zero free parameters. This is the fastest verification that the claims above are literal.

## Then

- **Full reproduction package:** `python3 play/verify_bst.py` — 50 predictions verified, 49/50 PASS at <1%, 17 EXACT, two open WARNs shown openly. Includes null-model context. One command, complete check.
- **Next stop:** `data/bst_seed.md` — 162 lines, the entire theory kernel. If you can evaluate a formula on a calculator, you can verify any BST prediction from that file.
- **To explore interactively:** `python3 play/toy_bst_explorer.py` — subcommands `seed`, `stats`, `search <term>`, `verify <theorem_id>`.
- **For the narrative:** root `OneGeometry.md` — the book-length front door.

The geometry does not know it is doing physics. That is the point.
