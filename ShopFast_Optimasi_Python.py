from scipy.optimize import linprog

# ==================================================
# OPTIMASI SISTEM INFORMASI PENJUALAN SHOPFAST
# Menggunakan Linear Programming (SciPy)
# ==================================================

print("==============================================")
print(" OPTIMASI SISTEM INFORMASI PENJUALAN SHOPFAST ")
print("==============================================\n")

# --------------------------------------------------
# INPUT DATA PRODUK
# --------------------------------------------------
print("Masukkan data per kategori produk:\n")

# Elektronik
pend_e = float(input("Pendapatan per session Elektronik       : "))
biaya_e = float(input("Biaya sistem per session Elektronik     : "))

# Fashion
pend_f = float(input("\nPendapatan per session Fashion          : "))
biaya_f = float(input("Biaya sistem per session Fashion        : "))

# Rumah Tangga
pend_r = float(input("\nPendapatan per session Rumah Tangga      : "))
biaya_r = float(input("Biaya sistem per session Rumah Tangga    : "))

# --------------------------------------------------
# PERHITUNGAN KEUNTUNGAN BERSIH
# --------------------------------------------------
profit_e = pend_e - biaya_e
profit_f = pend_f - biaya_f
profit_r = pend_r - biaya_r

print("\nKeuntungan Bersih per Session:")
print(f"Elektronik   : Rp {profit_e}")
print(f"Fashion      : Rp {profit_f}")
print(f"Rumah Tangga : Rp {profit_r}")

# --------------------------------------------------
# INPUT KENDALA MODEL
# --------------------------------------------------
print("\nMasukkan kendala model:\n")

total_session = float(input("Total session maksimum                 : "))
min_elektronik = float(input("Minimum session Elektronik             : "))
max_fashion = float(input("Maksimum session Fashion               : "))

# --------------------------------------------------
# MODEL LINEAR PROGRAMMING
# --------------------------------------------------

# Fungsi tujuan (linprog melakukan minimisasi)
c = [-profit_e, -profit_f, -profit_r]

# Kendala (A_ub * X <= b_ub)
A = [
    [1, 1, 1],          # Total session
    [-1, 0, 0],         # Elektronik minimum
    [0, 1, 0]           # Fashion maksimum
]

b = [
    total_session,
    -min_elektronik,
    max_fashion
]

# Batas variabel keputusan
bounds = [
    (0, None),          # X1: Elektronik
    (0, max_fashion),   # X2: Fashion
    (0, None)           # X3: Rumah Tangga
]

# --------------------------------------------------
# PENYELESAIAN MODEL
# --------------------------------------------------
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

# --------------------------------------------------
# OUTPUT HASIL
# --------------------------------------------------
print("\n==============================================")
print(" HASIL OPTIMASI (VARIABEL KEPUTUSAN) ")
print("==============================================")

print("Jumlah Session (Variabel Keputusan):")
print(f"X1 - Elektronik   : {round(result.x[0], 2)}")
print(f"X2 - Fashion      : {round(result.x[1], 2)}")
print(f"X3 - Rumah Tangga : {round(result.x[2], 2)}")

print("\nKeuntungan Maksimum : Rp", round(-result.fun, 2))
