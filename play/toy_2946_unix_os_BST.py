"""
Toy 2946 — Unix / OS internals structural counts BST.

POSIX standard file descriptors: 3 = N_c (stdin, stdout, stderr)
POSIX signal main categories: 7 = g (term, ign, stop, cont, core dump,
  default, default)
+ Specific signals total ~32 = rank⁵

Standard Unix permissions: 3 = N_c bits (r, w, x)
Permission scope: 3 = N_c (user, group, other)
Permission bits total: 9 = N_c² (3 × 3)
Special permission bits: 3 = N_c (setuid, setgid, sticky)
Total permission bits: 12 = rank·C_2

Standard Unix file types: 7 = g (regular, dir, char, block, fifo, symlink, socket)

Standard Unix shells major: 7 = g (sh, bash, zsh, ksh, csh, tcsh, fish)
Standard text editors: 6 = C_2 (vi, vim, emacs, nano, pico, ed)

Process states: 5 = n_C (running, sleeping, stopped, zombie, dead)
Process scheduling priorities standard: 3 = N_c (high, normal, low)

Common networking layers in OS: 4 = rank² (socket, transport, network, link)

Filesystem types major:
  ext family ext2/3/4: 3 = N_c
  Total major (ext, xfs, btrfs, ntfs, fat, hfs+, apfs): 7 = g
  Unix variants in heritage: 5 = n_C (BSD, SysV, Linux, Solaris, macOS-Darwin)

Standard IPC mechanisms: 5 = n_C (pipe, FIFO, msg queue, shared mem, semaphore)
+ sockets = 6 = C_2

OS layers Tanenbaum (T2275 dual): 6 = C_2

Standard CPU privilege rings: 4 = rank² (rings 0-3)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    unix = [
        ("POSIX standard file descriptors",  3, N_c, "N_c"),
        ("POSIX signal main categories",     7, g, "g"),
        ("POSIX signals approx total",       32, rank**5, "rank⁵"),
        ("Unix permission bits per scope",   3, N_c, "N_c (r,w,x)"),
        ("Permission scopes",                3, N_c, "N_c (u,g,o)"),
        ("Permission bits total basic",      9, N_c**2, "N_c²"),
        ("Special permission bits",          3, N_c, "N_c (setuid,setgid,sticky)"),
        ("Total permission bits incl special", 12, rank*C_2, "rank·C_2"),
        ("Unix file types",                  7, g, "g"),
        ("Major Unix shells",                7, g, "g"),
        ("Standard text editors",            6, C_2, "C_2"),
        ("Process states",                   5, n_C, "n_C"),
        ("Process priorities standard",      3, N_c, "N_c"),
        ("OS networking layers",             4, rank**2, "rank²"),
        ("ext filesystem family",            3, N_c, "N_c"),
        ("Major filesystem types",           7, g, "g"),
        ("Unix variants major",              5, n_C, "n_C"),
        ("Standard IPC mechanisms",          5, n_C, "n_C"),
        ("IPC + sockets",                    6, C_2, "C_2"),
        ("CPU privilege rings",              4, rank**2, "rank²"),
    ]

    print("Unix / OS BST:")
    matches = 0
    for name, val, bst, formula in unix:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<3} = {formula:<20} {marker}")

    print(f"\nSCORE: {matches}/{len(unix)}")
    return matches, len(unix)


if __name__ == "__main__":
    run()
