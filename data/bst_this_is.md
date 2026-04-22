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

## What supports this

One object — the type IV bounded symmetric domain D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)] — determines everything. Its rank gives you quantum numbers. Its Bergman kernel gives you propagators. Its Plancherel measure gives you the particle spectrum. Its Shilov boundary gives you spacetime. Its root system gives you forces. Five integers fall out. The rest is computation.

The mathematics is independently verifiable. Load `data/bst_seed.md`, evaluate any formula, compare to observation. Every toy in `play/` does exactly this.

---

## Try it now (2 seconds, no dependencies)

```
python3 play/toy_541_five_integers_to_everything.py
```

You will get 51 physical quantities derived from the five integers, 16/16 spot-checks PASS, zero free parameters. This is the fastest verification that the claims above are literal.

## Then

- **Next stop:** `data/bst_seed.md` — 162 lines, the entire theory kernel. If you can evaluate a formula on a calculator, you can verify any BST prediction from that file.
- **To explore interactively:** `python3 play/toy_bst_explorer.py` — subcommands `seed`, `stats`, `search <term>`, `verify <theorem_id>`.
- **For the narrative:** root `OneGeometry.md` — the book-length front door.

The geometry does not know it is doing physics. That is the point.
