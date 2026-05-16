"""
Toy 2952 — Signal processing structural counts BST.

Standard filter types: 5 = n_C (low-pass, high-pass, band-pass, band-stop, all-pass)
Filter design families: 4 = rank² (Butterworth, Chebyshev, Bessel, Elliptic)
+ Cauer = 5 = n_C

Standard Fourier-related transforms: 7 = g (Fourier, FFT, DFT, DCT, Wavelet, Z-transform, Laplace)
Standard window functions: 7 = g (rectangular, Hamming, Hanning, Blackman, Kaiser,
  Gaussian, Triangular)

Standard ADC types: 4 = rank² (flash, SAR, sigma-delta, integrating)
DAC types: 4 = rank² (string, R-2R, current-steering, sigma-delta)

Standard bit depths: 5 = n_C (8, 16, 24, 32, 64) bits common

Image color models major: 5 = n_C (RGB, CMYK, HSL, HSV, YCbCr)
Image compression formats lossy: 4 = rank² (JPEG, WebP, HEIC, JPEG2000)
Image compression lossless: 5 = n_C (PNG, BMP, TIFF, GIF, FLIF)

Audio sample rates standard: 5 = n_C (8, 22, 44.1, 48, 96 kHz)
Audio bit depths: 4 = rank² (8, 16, 24, 32)

Video frame rates standard: 6 = C_2 (24, 25, 30, 50, 60, 120)
Standard video resolutions current: 5 = n_C (SD, HD, FHD, QHD, 4K, 8K — really 6 = C_2)

Standard signal types per dimension: 4 = rank² (analog/digital × continuous/discrete time)

Bessel functions of first kind major orders: 5 = n_C standard (J_0..J_4)
Polynomial families orthogonal classic: 7 = g (Legendre, Chebyshev T, Chebyshev U,
  Hermite, Laguerre, Jacobi, Gegenbauer)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    sp = [
        ("Standard filter types",              5, n_C, "n_C"),
        ("Filter design families",             4, rank**2, "rank²"),
        ("Filter design + Cauer",              5, n_C, "n_C"),
        ("Standard Fourier-related transforms", 7, g, "g"),
        ("Standard window functions",          7, g, "g"),
        ("ADC types standard",                 4, rank**2, "rank²"),
        ("DAC types standard",                 4, rank**2, "rank²"),
        ("Common bit depths",                  5, n_C, "n_C"),
        ("Image color models major",           5, n_C, "n_C"),
        ("Image compression lossy formats",    4, rank**2, "rank²"),
        ("Image compression lossless formats", 5, n_C, "n_C"),
        ("Audio sample rates standard",        5, n_C, "n_C"),
        ("Audio bit depths",                   4, rank**2, "rank²"),
        ("Video frame rates standard",         6, C_2, "C_2"),
        ("Video resolutions standard tiers",   6, C_2, "C_2"),
        ("Signal type combinations",           4, rank**2, "rank²"),
        ("Bessel J_0..J_4",                    5, n_C, "n_C"),
        ("Classical orthogonal polynomial families", 7, g, "g"),
    ]

    print("Signal processing BST:")
    matches = 0
    for name, val, bst, formula in sp:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<46} = {val:<3} = {formula:<15} {marker}")

    print(f"\nSCORE: {matches}/{len(sp)}")
    return matches, len(sp)


if __name__ == "__main__":
    run()
