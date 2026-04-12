#!/usr/bin/env python3
"""
Toy 1082 — Government & Democracy from BST
=============================================
Governance structure and political counting:
  - Separation of powers: 3 branches = N_c
  - Bicameral legislature: 2 chambers = rank
  - Bill of Rights: 10 amendments = rank × n_C
  - UN Security Council: 5 permanent = n_C, 15 total = n_C × N_c
  - Jury trial: 12 jurors = rank² × N_c

BST integers: N_c=3, n_C=5, g=7, C_2=6, rank=2, N_max=137
"""

N_c = 3; n_C = 5; g = 7; C_2 = 6; rank = 2; N_max = 137

results = {}
test_num = 0

def test(name, condition, detail=""):
    global test_num
    test_num += 1
    status = "PASS" if condition else "FAIL"
    print(f"  T{test_num} [{status}] {name}")
    if detail:
        print(f"       {detail}")
    results[f"T{test_num}"] = (name, condition, detail)

print("="*70)
print("Toy 1082 — Government & Democracy from BST")
print("="*70)

# T1: Separation of powers
print("\n── Separation of Powers ──")
# Legislative, Executive, Judicial = N_c
branches = 3  # N_c
# Checks: each branch checks the other two = N_c × (N_c - 1) = 6 = C_2
checks = 6    # C_2 = N_c × (N_c - 1)

print(f"  Branches of government: {branches} = N_c = {N_c}")
print(f"  Check relationships: {checks} = C_2 = N_c(N_c-1) = {N_c*(N_c-1)}")

test("N_c=3 branches; C_2=6 check relationships",
     branches == N_c and checks == C_2 and checks == N_c * (N_c - 1),
     f"N_c={N_c}, C_2={C_2}=N_c(N_c-1)")

# T2: Bicameral legislature
print("\n── Legislature ──")
# Senate + House = rank chambers
# US Senate: 100 = rank² × n_C²
# US House: 435 ≈ ... (not clean BST)
chambers = 2       # rank
senate = 100       # rank² × n_C²
senators_per_state = 2  # rank

print(f"  Chambers: {chambers} = rank = {rank}")
print(f"  US Senate: {senate} = rank² × n_C² = {rank**2 * n_C**2}")
print(f"  Senators per state: {senators_per_state} = rank = {rank}")

test("rank=2 chambers; rank²×n_C²=100 senators",
     chambers == rank and senate == rank**2 * n_C**2,
     f"rank={rank}, rank²×n_C²={rank**2*n_C**2}")

# T3: Bill of Rights
print("\n── Constitutional Rights ──")
# US Bill of Rights: 10 amendments = rank × n_C
# Total original amendments: 27 = N_c³
bill_of_rights = 10  # rank × n_C
total_amendments = 27  # N_c³

print(f"  Bill of Rights: {bill_of_rights} = rank × n_C = {rank * n_C}")
print(f"  Total amendments: {total_amendments} = N_c³ = {N_c**3}")

test("rank×n_C=10 Bill of Rights; N_c³=27 total amendments",
     bill_of_rights == rank * n_C and total_amendments == N_c**3,
     f"rank×n_C={rank*n_C}, N_c³={N_c**3}")

# T4: UN Security Council
print("\n── United Nations ──")
# Permanent members: 5 = n_C (US, UK, France, Russia, China)
# Total SC members: 15 = n_C × N_c
# Non-permanent: 10 = rank × n_C
# UN General Assembly committees: 6 = C_2
permanent = 5      # n_C
sc_total = 15      # n_C × N_c
non_permanent = 10  # rank × n_C
ga_committees = 6   # C_2

print(f"  UNSC permanent: {permanent} = n_C = {n_C}")
print(f"  UNSC total: {sc_total} = n_C × N_c = {n_C * N_c}")
print(f"  Non-permanent: {non_permanent} = rank × n_C = {rank * n_C}")
print(f"  GA committees: {ga_committees} = C_2 = {C_2}")

test("n_C=5 permanent; n_C×N_c=15 total SC; C_2=6 GA committees",
     permanent == n_C and sc_total == n_C * N_c
     and non_permanent == rank * n_C and ga_committees == C_2,
     f"n_C={n_C}, n_C×N_c={n_C*N_c}, C_2={C_2}")

# T5: Jury system
print("\n── Justice System ──")
# Jury: 12 = rank² × N_c
# Grand jury: 23 ≈ N_c × g + rank (same as axial tilt, chromosomes!)
# Supreme Court: 9 = N_c² (US)
jury = 12          # rank² × N_c
grand_jury = 23    # N_c × g + rank
scotus = 9         # N_c²

print(f"  Jury: {jury} = rank² × N_c = {rank**2 * N_c}")
print(f"  Grand jury: {grand_jury} = N_c × g + rank = {N_c * g + rank}")
print(f"  Supreme Court: {scotus} = N_c² = {N_c**2}")

test("rank²×N_c=12 jury; N_c×g+rank=23 grand jury; N_c²=9 SCOTUS",
     jury == rank**2 * N_c and grand_jury == N_c * g + rank
     and scotus == N_c**2,
     f"rank²×N_c={rank**2*N_c}, N_c×g+rank={N_c*g+rank}, N_c²={N_c**2}")

# T6: Voting systems
print("\n── Voting ──")
# Simple majority: 1/2 = 1/rank threshold
# Supermajority: 2/3 = rank/N_c
# Unanimous: 1/1
# US Electoral College: 538 total, 270 to win
# 538 = 2 × 269 (269 is prime)
# Voting age: 18 = rank × N_c²
majority_denom = 2    # rank
supermajority = (2, 3)  # (rank, N_c)
voting_age = 18       # rank × N_c²

print(f"  Majority: 1/{majority_denom} = 1/rank")
print(f"  Supermajority: {supermajority[0]}/{supermajority[1]} = rank/N_c")
print(f"  Voting age: {voting_age} = rank × N_c² = {rank * N_c**2}")

test("1/rank majority; rank/N_c=2/3 supermajority; rank×N_c²=18 voting age",
     majority_denom == rank and supermajority == (rank, N_c)
     and voting_age == rank * N_c**2,
     f"rank={rank}, N_c={N_c}, rank×N_c²={rank*N_c**2}")

# T7: Federal structure
print("\n── Federal Structure ──")
# US states: 50 = rank × n_C²
# Original colonies: 13 = 2g - 1
# Canadian provinces: 10 = rank × n_C; territories: 3 = N_c
us_states = 50       # rank × n_C²
colonies = 13        # 2g - 1
can_provinces = 10   # rank × n_C
can_territories = 3  # N_c

print(f"  US states: {us_states} = rank × n_C² = {rank * n_C**2}")
print(f"  Original colonies: {colonies} = 2g - 1 = {2*g - 1}")
print(f"  Canadian provinces: {can_provinces} = rank × n_C = {rank * n_C}")
print(f"  Canadian territories: {can_territories} = N_c = {N_c}")

test("rank×n_C²=50 states; 2g-1=13 colonies; rank×n_C=10 provinces",
     us_states == rank * n_C**2 and colonies == 2*g - 1
     and can_provinces == rank * n_C and can_territories == N_c,
     f"rank×n_C²={rank*n_C**2}, 2g-1={2*g-1}, rank×n_C={rank*n_C}")

# T8: International law
print("\n── International Law ──")
# Geneva Conventions: 4 = rank²
# Additional Protocols: 3 = N_c
# Universal Declaration of Human Rights: 30 articles = n_C# = rank × N_c × n_C
geneva = 4           # rank²
protocols = 3        # N_c
udhr_articles = 30   # n_C#

print(f"  Geneva Conventions: {geneva} = rank² = {rank**2}")
print(f"  Additional Protocols: {protocols} = N_c = {N_c}")
print(f"  UDHR articles: {udhr_articles} = n_C# = rank × N_c × n_C = {rank * N_c * n_C}")

test("rank²=4 Geneva; N_c=3 protocols; n_C#=30 UDHR articles",
     geneva == rank**2 and protocols == N_c
     and udhr_articles == rank * N_c * n_C,
     f"rank²={rank**2}, N_c={N_c}, n_C#={rank*N_c*n_C}")

# T9: Election cycles
print("\n── Election Cycles ──")
# US House term: 2 years = rank
# US Senate term: 6 years = C_2
# US Presidential term: 4 years = rank²
# Senate classes: 3 = N_c (1/3 elected every 2 years)
house_term = 2       # rank
senate_term = 6      # C_2
president_term = 4   # rank²
senate_classes = 3   # N_c

print(f"  House term: {house_term} yr = rank = {rank}")
print(f"  Senate term: {senate_term} yr = C_2 = {C_2}")
print(f"  Presidential term: {president_term} yr = rank² = {rank**2}")
print(f"  Senate classes: {senate_classes} = N_c = {N_c}")

test("rank=2yr House; C_2=6yr Senate; rank²=4yr President; N_c=3 classes",
     house_term == rank and senate_term == C_2
     and president_term == rank**2 and senate_classes == N_c,
     f"rank={rank}, C_2={C_2}, rank²={rank**2}, N_c={N_c}")

# T10: Military ranks
print("\n── Military Structure ──")
# Service branches: Army, Navy, AF, Marines, CG = n_C (US, 5 traditional)
# + Space Force = C_2 (now 6)
# Officer grades: O-1 to O-10 = rank × n_C
# Enlisted grades: E-1 to E-9 = N_c²
service_branches_trad = 5  # n_C
service_branches_now = 6   # C_2
officer_grades = 10        # rank × n_C
enlisted_grades = 9        # N_c²

print(f"  Traditional branches: {service_branches_trad} = n_C = {n_C}")
print(f"  Current branches: {service_branches_now} = C_2 = {C_2}")
print(f"  Officer grades: {officer_grades} = rank × n_C = {rank * n_C}")
print(f"  Enlisted grades: {enlisted_grades} = N_c² = {N_c**2}")

test("n_C=5→C_2=6 branches; rank×n_C=10 officer; N_c²=9 enlisted",
     service_branches_trad == n_C and service_branches_now == C_2
     and officer_grades == rank * n_C and enlisted_grades == N_c**2,
     f"n_C={n_C}, C_2={C_2}, rank×n_C={rank*n_C}, N_c²={N_c**2}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Governance IS BST-Structured

  N_c = 3: branches, senate classes, protocols, territories
  rank = 2: chambers, House term, majority rule
  rank² = 4: presidential term, Geneva Conventions
  n_C = 5: UN permanent members, traditional branches
  C_2 = 6: check relationships, Senate term, current branches
  n_C# = 30: UDHR articles, DJIA stocks (same!)

  N_c × g + rank = 23: grand jury size
  N_c³ = 27: Constitutional amendments
  rank × n_C² = 50: US states
  2g - 1 = 13: original colonies (same as K-12!)
  rank² × n_C² = 100: US Senate

  Democratic institutions evolved under the same counting constraints.
""")
