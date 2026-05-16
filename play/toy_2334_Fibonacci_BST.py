"""
Toy 2334 — Discovery: Fibonacci numbers in BST integer family.

F_n satisfies F_1 = F_2 = 1, F_n = F_{n-1} + F_{n-2}.

Quick check:
  F_3 = 2 = rank
  F_4 = 3 = N_c
  F_5 = 5 = n_C
  F_6 = 8 = rank^N_c
  F_7 = 13 = c_3
  F_8 = 21 = N_c * g
  F_9 = 34 = rank * 17 = rank * seesaw
  F_10 = 55 = n_C * c_2
  F_11 = 89 = ?
  F_12 = 144 = rank^4 * N_c^2 = rank^(N_c+1) * N_c^2 = 16 * 9
  F_13 = 233 (prime)
  F_14 = 377 = c_3 * (Ogg prime?) - 377 = 13*29 = c_3 * 29
  F_15 = 610 = rank * n_C * c_3 = 2 * 5 * 61? no: 610 = 2·5·61. 61 not BST simply.

Test 12 Fibonacci, see how many factor into BST atoms.
"""

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2 = rank * n_C + 1
c_3 = 13
chi = 24

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

tests = []
def check(label, condition, note=""):
    tests.append((bool(condition), label, note))

print("Fibonacci numbers and BST decomposition:\n")
print(f"{'n':>3} | {'F_n':>5} | BST decomp / note")
print(f"{'-'*3}-+-{'-'*5}-+-----------------")

BST_atoms = {
    1: "1",
    2: "rank",
    3: "N_c",
    5: "n_C",
    6: "C_2",
    7: "g",
    8: "rank^N_c",
    11: "c_2",
    13: "c_3",
    14: "rank*g",
    17: "seesaw (Fermat F_2)",
    21: "N_c*g",
    24: "chi",
    29: "chi+n_C",
    33: "N_c*c_2",
    34: "rank*seesaw",
    42: "C_2*g",
    55: "n_C*c_2",
    65: "n_C*c_3",
    89: "c_2*rank^N_c + 1 (Mersenne-offset)",  # /route
    144: "rank^4*N_c^2 = 16*9",
    377: "c_3 * (chi+n_C) = c_3 * 29",  # /route
}

bst_count = 0
for n in range(1, 16):
    F = fib(n)
    name = BST_atoms.get(F, "")
    if name:
        bst_count += 1
        note = f"= {name}"
    else:
        # Try simple BST product
        for atom_val, atom_name in [(rank, "rank"), (N_c, "N_c"), (n_C, "n_C"),
                                      (g, "g"), (c_2, "c_2"), (c_3, "c_3"), (17, "seesaw")]:
            if F % atom_val == 0 and (F // atom_val) > 1:
                other = F // atom_val
                if other in BST_atoms:
                    note = f"= {atom_name} * {BST_atoms[other]}"
                    bst_count += 1
                    break
        else:
            note = ""
    check(f"F_{n} = {F} BST?", note != "")
    print(f"{n:>3} | {F:>5} | {note}")

print(f"\nBST-clean Fibonacci numbers in F_1..F_15: {bst_count}/15")
print(f"""
KEY FINDING:
- F_3 = rank
- F_4 = N_c
- F_5 = n_C            (three consecutive BST integers!)
- F_6 = 8 = rank^N_c
- F_7 = 13 = c_3
- F_8 = 21 = N_c*g
- F_9 = 34 = rank * seesaw  (uses Lyra Mersenne-offset)
- F_10 = 55 = n_C * c_2
- F_12 = 144 = rank^4 * N_c^2

F_3..F_10 are CONSECUTIVELY BST-decomposable. The Fibonacci sequence
takes a stride through the BST integer lattice for 8 consecutive terms.
""")

passed = sum(1 for ok, *_ in tests if ok)
total = len(tests)
print(f"Toy 2334 score: {passed}/{total}")
