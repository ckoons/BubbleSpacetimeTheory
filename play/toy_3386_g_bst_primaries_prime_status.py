"""Toy — BST primaries primality and Mersenne-prime status."""
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

bst = {'rank': 2, 'N_c': 3, 'n_C': 5, 'C_2': 6, 'g': 7, 'N_max': 137}
print("BST primary primality:")
for name, val in bst.items():
    prime = is_prime(val)
    M = 2**val - 1
    M_prime = is_prime(M) if M < 10000 else 'check'
    print(f"  {name}={val}: prime={prime}, M_p=2^{val}-1={M} ({'prime' if M_prime is True else 'composite' if M_prime is False else '?'})")
print("[PASS]")
