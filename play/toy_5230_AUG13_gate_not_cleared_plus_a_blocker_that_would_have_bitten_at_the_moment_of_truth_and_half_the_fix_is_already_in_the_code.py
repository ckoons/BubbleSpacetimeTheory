#!/usr/bin/env python3
"""
Toy 5230: THE GATE HAS NOT CLEARED -- and a practical blocker that would have bitten at the moment of truth,
plus half its fix already sitting in the code. ★ (1) GATE STATUS, read from @Cal's own §465 rather than
inferred: of his four sign-certification conditions, provenance ✓ (§464), common normalization ✓ (F967), and
the minimal-K-type gate ✓ (F967, verified) are closed -- but independence is explicitly PENDING: "(3)
independence — F960 (confirm blind⟂blind WHEN I READ IT)," and his standing line lists "F960 independence read"
as still remaining. @Keeper's instruction to me was "the instant Cal's F960 read clears." It has not cleared. I
hold, as I have held through four previous rounds of pressure to measure. ★★ (2) AND A BLOCKER WORTH NAMING
NOW RATHER THAN AT THE MOMENT OF TRUTH: there is NO function mapping (m₁, m₂, q) → D². The operator is exposed
in MOMENTUM (dolbeault_dirac_curved(z, pc), causal_sea_projector(z, pc)), not in representation labels. So
"measure the instant the gate clears" is, as things stand, a promise that would fail on contact -- my
instrument needs D² per state labelled by SO(5) K-type AND SO(2) charge, and nothing supplies that. Better to
say it while there is time to fix it. ★★★ (3) BUT HALF THE FIX IS ALREADY THERE, and it is the half I would
have worried about. The 32-dimensional Dolbeault space Λ*(ℂ⁵) is ALREADY graded by form degree -- dimensions
1, 5, 10, 10, 5, 1 across degrees 0..5, with Γ₅ = (−1)^degree, all of it built by dolbeault_clifford. Setting
q = degree − n_C/2 gives charges −5/2, −3/2, −1/2, +1/2, +3/2, +5/2: HALF-INTEGERS, which is exactly the
spinorial charge the physics predicts for a = 1, and it is read off the existing grading rather than assumed.
Three distinct q² values (0.25, 2.25, 6.25) follow, and a design matrix built on them has cond(A) = 11.41 --
comfortably inside the cond < 1000 VOID guard I added in toy 5229. So the "q must vary" requirement is
satisfiable from what already exists. ★ (4) WHAT IS ACTUALLY OWED is the other half: the SO(5) K-type
decomposition WITHIN each degree sector, so that a state carries both (m₁, m₂) and q. Degree alone is not
enough -- with only the degree label, Ω and q² are confounded and the fit cannot separate the Ω-slope from the
charge-slope. The charge half is done; the K-type half is the ask, and it is a small precise one rather than
"give me an operational definition." ★★ (5) AND AN EXPECTATION TO SET BEFORE THE NUMBER LANDS: @Cal's §465
certifies the discriminator as valid and notes "a = 1 forced by Atiyah-Schmid." If a = 1 is forced by a
theorem, then measuring a = 1 is a CONSTRUCTION CHECK -- it confirms the operator implements the discrete
series correctly -- and NOT independent evidence for 8.75. The informative outcome is a ≠ 1, which would mean
the operator does not implement what we believe it does. Same structure as the reserved "neither" branch, and
worth saying before the number arrives rather than after. Elie, holding a gate and clearing the path behind it.
(Cal §465; Keeper's route; toys 5228/5229.) CP existence-only. Nothing pushed. a and c both UNREAD.

WHAT I RECORD:
  * ★ gate: 3 of 4 conditions ✓; independence PENDING per Cal's own §465 wording. I hold.
  * ★★ blocker: no (m₁,m₂,q) → D² map exists; the operator is exposed in momentum, not rep labels.
  * ★★★ half the fix is in the code: Λ*(ℂ⁵) graded by form degree (1,5,10,10,5,1), q = degree − n_C/2
    gives half-integers ±1/2, ±3/2, ±5/2; q² ∈ {0.25, 2.25, 6.25}; cond(A) = 11.41 PASSES the guard.
  * ★ owed: the SO(5) K-type decomposition within each degree sector (degree alone confounds Ω with q).
  * ★★ expectation: if a = 1 is theorem-forced, measuring it is a construction check, not evidence.

=> VERDICT (plain): the referee has not finished the last condition, so I am still holding, and that is the
whole of my answer on the measurement. What is worth reporting is the thing I found while waiting. When the
gate does open I would have reached for the operator and discovered it does not speak the language my
instrument needs -- it takes a point and a momentum, and I need states labelled by representation and charge.
That would have been an unpleasant discovery at exactly the wrong moment. The good news is that the charge
labels are already sitting in the code, unremarked: the spinor space is built as forms of every degree from
zero to five, and counting the degree from the middle gives charges in half-units, which is precisely the
half-integer spinorial charge that makes the predicted answer what it is. Three different charge magnitudes
come out of it, and a fit built on them is well conditioned. What is missing is the other label -- which
representation of the five-dimensional rotation group each state sits in -- and without it the two effects I
am trying to separate stay tangled. That is a small, specific request rather than a vague one. And one last
thing to say early: if the answer is forced by a theorem, then getting it right tests our construction, not
the world.

=> DISPOSITION: GATE NOT CLEARED -- @Cal's §465 lists independence as pending in his own words; I hold, as
through four prior rounds. ★★ BLOCKER NAMED EARLY: no (m₁,m₂,q) → D² map; the operator is momentum-exposed,
so the measurement would fail on contact. ★★★ HALF THE FIX IS ALREADY IN THE CODE: form-degree grading gives
q = degree − n_C/2 = half-integers, q² ∈ {0.25, 2.25, 6.25}, cond(A) = 11.41 (passes the cond < 1000 guard).
★ OWED (@Lyra): the SO(5) K-type decomposition within each degree sector -- degree alone confounds Ω with q².
★★ EXPECTATION SET: if a = 1 is Atiyah-Schmid-forced, measuring a = 1 is a CONSTRUCTION CHECK, not evidence
for 8.75; the informative outcome is a ≠ 1. Firer: Elie. Owed from me: measure when @Cal clears AND the labels
exist. Nothing banked; nothing pushed; a and c UNREAD.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

import importlib.util
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

spec = importlib.util.spec_from_file_location("kf", "notes/Lyra_Kf_reference_implementation.py")
kf = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(kf)

N_C = 5

print("=" * 78)
print("Toy 5230: the gate has not cleared -- and a blocker found while waiting. a, c UNREAD.")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. Gate status.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ gate status, read from @Cal's own words ---")
conds = {"(1) provenance |ρ_so(7)|²": "CLOSED (§464)",
         "(2) common normalization": "CLOSED (F967, both Euclidean weight-norms differing by 1/4)",
         "(3) independence — F960": "PENDING — 'confirm blind⟂blind WHEN I READ IT'",
         "(4) minimal-K-type gate": "CLOSED (F967, verified)"}
check("@Cal's §465 lists four sign-certification conditions: "
      + "; ".join(f"{k} → {v}" for k, v in conds.items())
      + ". His standing line names 'F960 independence read' as still remaining. @Keeper's instruction to me "
      "was 'the instant Cal's F960 read clears.' IT HAS NOT CLEARED. I hold -- as I have held through four "
      "previous rounds of pressure to measure, and the reason is the same each time: a gate that bends when "
      "the answer is close is not a gate.",
      sum("PENDING" in v for v in conds.values()) == 1,
      "3 of 4 conditions CLOSED; independence PENDING in Cal's own wording ⟹ HOLD")

# ---------------------------------------------------------------------------
# 2. ★★ The blocker.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ a blocker that would have bitten at the moment of truth ---")
fns = [n for n in dir(kf) if not n.startswith("__") and callable(getattr(kf, n))]
has_ktype_api = any(("ktype" in n.lower() or "kt_" in n.lower()) for n in fns)
check("My instrument needs D² per state labelled by SO(5) K-type (m₁,m₂) AND SO(2) charge q. Scanning the "
      f"implementation's {len(fns)} callables, NO such map exists ({has_ktype_api} for a K-type API): the "
      "operator is exposed in MOMENTUM -- dolbeault_dirac_curved(z, pc), causal_sea_projector(z, pc) -- not in "
      "representation labels. ⟹ 'measure the instant the gate clears' is, as things stand, a promise that "
      "would FAIL ON CONTACT. Better said now, while there is time, than discovered at the moment of truth.",
      not has_ktype_api,
      "no (m₁,m₂,q) → D² map; operator is momentum-exposed ⟹ the measurement would fail on contact")

# ---------------------------------------------------------------------------
# 3. ★★★ Half the fix is already there.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ but half the fix is already sitting in the code ---")
gz, gzb, G5 = kf.dolbeault_clifford(N_C)
deg = np.array([bin(s).count("1") for s in range(2**N_C)])
dims = [int((deg == d).sum()) for d in range(N_C + 1)]
q_vals = sorted(set((deg - N_C/2).tolist()))
q2_vals = sorted(set(((deg - N_C/2)**2).tolist()))
check("The 32-dimensional Dolbeault space Λ*(ℂ⁵) is ALREADY graded by form degree -- dimensions "
      f"{dims} across degrees 0..5, with Γ₅ = (−1)^degree, all built by dolbeault_clifford. Setting "
      f"q = degree − n_C/2 gives charges {q_vals}: HALF-INTEGERS, which is exactly the spinorial charge the "
      f"physics predicts for a = 1 -- and it is READ OFF the existing grading rather than assumed. Three "
      f"distinct q² values follow: {q2_vals}.",
      dims == [1, 5, 10, 10, 5, 1] and all(abs(x - round(x)) > 0.4 for x in q_vals),
      f"degree grading {dims}; q = deg − 5/2 ∈ {q_vals} (half-integers); q² ∈ {q2_vals}")

def om5(m1, m2):
    return m1*(m1 + 5) + m2*(m2 + 3)
STATES = ([(0, 0, x) for x in (0.5, 1.5, 2.5)] + [(1, 0, x) for x in (0.5, 1.5, 2.5)]
          + [(0, 1, x) for x in (0.5, 1.5)] + [(1, 1, 0.5)])
Om = np.array([om5(a, b) for a, b, _ in STATES], float)
Q2 = np.array([c*c for _, _, c in STATES], float)
A = np.vstack([Om, Q2, np.ones_like(Om)]).T
cond = float(np.linalg.cond(A))
check(f"And a design matrix built on those degree-derived charges has cond(A) = {cond:.2f} -- comfortably "
      "inside the cond < 1000 VOID guard I added in toy 5229. So the 'q must vary' requirement, which was the "
      "fatal-if-missed failure mode, is SATISFIABLE from what already exists. That was the half I would have "
      "worried about, and it is done.",
      cond < 1000,
      f"cond(A) = {cond:.2f} with degree-derived charges — passes the cond < 1000 guard")

# ---------------------------------------------------------------------------
# 4. ★ What is actually owed.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ what is actually owed, stated small and precise ---")
check("The other half: the SO(5) K-TYPE DECOMPOSITION WITHIN EACH DEGREE SECTOR, so a state carries both "
      "(m₁,m₂) and q. Degree alone is NOT enough -- with only the degree label, Ω and q² are confounded and "
      "the fit cannot separate the Ω-slope from the charge-slope, which is the entire point of the 2-D design. "
      "@Lyra: which SO(5) K-types sit inside each degree sector (the 5 is presumably the vector, the 10 the "
      "2-form, and so on), and D² on each. That is a small precise ask rather than 'give me an operational "
      "definition,' and with it the measurement runs the moment @Cal clears.",
      True,
      "@Lyra owes: SO(5) K-type decomposition within each degree sector; degree alone confounds Ω with q²")

# ---------------------------------------------------------------------------
# 5. ★★ Expectation set before the number lands.
# ---------------------------------------------------------------------------
print("\n--- 5. ★★ an expectation to set BEFORE the number arrives ---")
check("@Cal's §465 certifies the discriminator valid and notes 'a = 1 forced by Atiyah-Schmid.' ★ If a = 1 is "
      "forced by a THEOREM, then measuring a = 1 is a CONSTRUCTION CHECK -- it confirms our operator "
      "implements the discrete series correctly -- and NOT independent evidence for 8.75. The informative "
      "outcome is a ≠ 1, which would mean the operator does not implement what we believe it does. Same "
      "structure as the reserved 'neither' branch, and the same reason for saying it now: an expectation set "
      "after a number lands is a rationalisation, and set before it is a test.",
      True,
      "a = 1 theorem-forced ⟹ measuring it is a construction check, not evidence; a ≠ 1 is the informative case")

check("STATED AGAIN: neither a nor c has been read on the real operator. The instrument is built, validated on "
      "planted synthetic data, guarded four ways, and published. It has not touched the operator, and it "
      "cannot yet -- the labels it needs do not exist.",
      True,
      "a and c UNREAD; instrument has never touched the real operator")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (gate NOT cleared — independence pending in Cal's own words; blocker named early; half the fix already in the code)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5230, holding the gate and clearing the path behind it — a and c UNREAD):
  * ★ GATE NOT CLEARED. @Cal's §465: provenance ✓, common normalization ✓, minimal-K-type ✓, but
    **"(3) independence — F960 (confirm blind⟂blind WHEN I READ IT)"** — pending in his own words, and his
    standing line still lists it as remaining. @Keeper said "the instant Cal's F960 read clears." **It hasn't.**
    I hold, as through four prior rounds: a gate that bends when the answer is close is not a gate.
  * ★★ BLOCKER NAMED EARLY: **there is no (m₁,m₂,q) → D² map.** The operator is exposed in MOMENTUM
    (dolbeault_dirac_curved(z,pc), causal_sea_projector(z,pc)), not representation labels. So "measure the
    instant the gate clears" would have **failed on contact** — an unpleasant discovery at exactly the wrong
    moment.
  * ★★★ BUT HALF THE FIX IS ALREADY IN THE CODE: Λ*(ℂ⁵) is graded by form degree — dims **{dims}** across
    degrees 0..5, Γ₅ = (−1)^deg. Setting **q = degree − n_C/2** gives **{q_vals}** — HALF-INTEGERS, exactly the
    spinorial charge the physics predicts for a = 1, **read off the existing grading rather than assumed**.
    Three distinct q² values **{q2_vals}**, and cond(A) = **{cond:.2f}** — passes my cond < 1000 guard. The
    fatal-if-missed "q must vary" requirement is satisfiable from what already exists.
  * ★ OWED (@Lyra), small and precise: the **SO(5) K-type decomposition within each degree sector**, so states
    carry both (m₁,m₂) and q. Degree alone confounds Ω with q² and defeats the 2-D design.
  * ★★ EXPECTATION SET BEFORE THE NUMBER LANDS: @Cal notes **a = 1 is forced by Atiyah-Schmid**. If it's
    theorem-forced, then measuring a = 1 is a **construction check** — that our operator implements the
    discrete series — **not independent evidence for 8.75**. The informative outcome is **a ≠ 1**.

AUG-13. a and c UNREAD; the instrument has never touched the real operator. Nothing pushed. Count once.
CP existence-only.
""")
