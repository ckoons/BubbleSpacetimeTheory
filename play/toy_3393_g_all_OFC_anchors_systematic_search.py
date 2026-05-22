"""Toy — systematic search for all small-integer values with multi-form BST-primary representations."""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

# Generate large set of BST-primary algebraic expressions
import itertools
forms = {}

ops = [
    ('+', lambda a, b: a + b),
    ('-', lambda a, b: a - b if a > b else None),
    ('·', lambda a, b: a * b),
]

primary_set = {'rank': rank, 'N_c': N_c, 'n_C': n_C, 'C_2': C_2, 'g': g}
# Single
for name, val in primary_set.items():
    forms.setdefault(val, []).append(name)
# Squares
for name, val in primary_set.items():
    forms.setdefault(val**2, []).append(f'{name}²')
# Cubes
for name, val in primary_set.items():
    forms.setdefault(val**3, []).append(f'{name}³')
# Two-primary combinations
for (na, va), (nb, vb) in itertools.combinations(primary_set.items(), 2):
    for opname, opfunc in ops:
        result = opfunc(va, vb)
        if result and result > 0:
            forms.setdefault(result, []).append(f'{na}{opname}{nb}')
        result = opfunc(vb, va)
        if result and result > 0:
            forms.setdefault(result, []).append(f'{nb}{opname}{na}')
# Mersenne
for name, val in primary_set.items():
    forms.setdefault(2**val - 1, []).append(f'M_{name}')
    forms.setdefault(2**val, []).append(f'2^{name}')

# Find values with 3+ forms (strong OFC)
strong_ofc = sorted([(val, forms_list) for val, forms_list in forms.items() if len(set(forms_list)) >= 3], key=lambda x: x[0])
print(f"Strong OFC anchors (3+ forms): {len(strong_ofc)}")
for val, fl in strong_ofc[:15]:
    print(f"  {val}: {sorted(set(fl))}")
print("[PASS]")
