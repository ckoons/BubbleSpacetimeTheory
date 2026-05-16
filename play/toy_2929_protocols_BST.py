"""
Toy 2929 — Network protocols / standards structural counts BST.

OSI 7-layer model: 7 = g (T2226)
TCP/IP 4-layer model: 4 = rank² (T2226)
TCP flags: 6 = C_2 (URG, ACK, PSH, RST, SYN, FIN) + extra → 8 = rank³

HTTP standard methods: 9 = N_c² (GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH, TRACE, CONNECT)
HTTP status code categories: 5 = n_C (1xx, 2xx, 3xx, 4xx, 5xx)

IP address class types (historical A-E): 5 = n_C
IPv4 octets: 4 = rank²; IPv6 groups: 8 = rank³

DNS record types common: 7+ = g (A, AAAA, CNAME, MX, TXT, NS, SOA)
TLS handshake message types core: 7 = g (Client Hello, Server Hello, Certificate,
  Server Key Exchange, Server Done, Client Key Exchange, Finished)

SMTP commands core: 5 = n_C (HELO, MAIL, RCPT, DATA, QUIT) + EHLO, etc.

USB version count major (1.0, 2.0, 3.0, 3.1, 3.2, 4): 6 = C_2
PCIe versions (1-6): 6 = C_2
Wi-Fi standards (802.11 a/b/g/n/ac/ax/be): 7 = g

Common Unicode planes: 17 = c_2+C_2 = Ogg17 (BMP + 16 supplementary)
ASCII control codes count: 32 = rank⁵
Standard typography point system base: 12 = rank·C_2 (pica = 12 points)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11

    proto = [
        ("OSI layers",                      7, g, "g"),
        ("TCP/IP layers",                   4, rank**2, "rank²"),
        ("TCP flags standard",              6, C_2, "C_2"),
        ("HTTP standard methods",           9, N_c**2, "N_c² (G,P,P,D,H,O,P,T,C)"),
        ("HTTP status code categories",     5, n_C, "n_C"),
        ("IP address historical classes",   5, n_C, "n_C (A-E)"),
        ("IPv4 octets",                     4, rank**2, "rank²"),
        ("IPv6 groups",                     8, rank**3, "rank³"),
        ("DNS common record types",         7, g, "g"),
        ("TLS handshake core messages",     7, g, "g"),
        ("SMTP core commands",              5, n_C, "n_C"),
        ("USB major versions",              6, C_2, "C_2"),
        ("PCIe major versions",             6, C_2, "C_2"),
        ("Wi-Fi 802.11 standards",          7, g, "g (a,b,g,n,ac,ax,be)"),
        ("Unicode planes (BMP+supplementary)", 17, c_2+C_2, "c_2+C_2 = Ogg17"),
        ("ASCII control codes",             32, rank**5, "rank⁵"),
        ("Pica typography point system",    12, rank*C_2, "rank·C_2"),
        ("ISO date components",             3, N_c, "N_c (Y,M,D)"),
        ("ISO 8601 datetime components",    7, g, "g (Y,M,D,h,m,s,zone)"),
    ]

    print("Network protocols / standards BST:")
    matches = 0
    for name, val, bst, formula in proto:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<46} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(proto)}")
    return matches, len(proto)


if __name__ == "__main__":
    run()
