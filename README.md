
# 📊 ShopFast Sales System Optimization
**Analisis dan Optimasi Sistem Informasi Penjualan Menggunakan  
Cost–Benefit Analysis (CBA) dan Linear Programming**

---

## 📌 Deskripsi Proyek
Proyek ini merupakan proyek akademik pada mata kuliah **Riset Operasional / Teknik Riset Operasional**.  
Studi kasus yang digunakan adalah perusahaan e-commerce fiktif bernama **ShopFast**, yang menghadapi keterbatasan kapasitas sistem informasi penjualan dalam melayani session transaksi harian.

Melalui pendekatan **Cost–Benefit Analysis (CBA)** dan **Linear Programming**, proyek ini bertujuan untuk menentukan alokasi session penjualan yang optimal agar keuntungan perusahaan dapat dimaksimalkan dengan tetap memperhatikan batasan kapasitas dan kebijakan operasional.

---

## 🎯 Tujuan Proyek
1. Memodelkan permasalahan optimasi sistem informasi penjualan ke dalam bentuk matematis.
2. Menentukan alokasi session penjualan optimal pada setiap kategori produk.
3. Mengimplementasikan model menggunakan **Excel Solver** dan **Python (SciPy)**.
4. Membandingkan hasil perhitungan dari kedua tools.
5. Melakukan analisis sensitivitas terhadap perubahan parameter biaya.
6. Memberikan rekomendasi manajerial berdasarkan hasil optimasi.

---

## 🧩 Studi Kasus
ShopFast memiliki tiga kategori produk utama:
- **Elektronik**
- **Fashion**
- **Rumah Tangga**

Kapasitas sistem dibatasi hingga **1.000 session per hari**, dengan kebijakan operasional:
- Minimum session Elektronik: 200
- Maksimum session Fashion: 500

Setiap kategori memiliki keuntungan bersih per session yang berbeda dan menjadi dasar dalam perhitungan optimasi.

---

## 🛠️ Metodologi
- **Metode:** Linear Programming (Maximization)
- **Variabel Keputusan:** Jumlah session penjualan per kategori
- **Fungsi Tujuan:** Memaksimalkan total keuntungan
- **Kendala:** Kapasitas sistem dan kebijakan operasional
- **Tools yang digunakan:**
  - Microsoft Excel (Solver)
  - Python (SciPy – `linprog`)

---

## 📁 Struktur Repository
```
📦 ShopFast-Sales-System-Optimization
├── 📄 Laporan_ShopFast_FINAL_LENGKAP_DENGAN_LAMPIRAN.docx
├── 📊 ShopFast_Excel_Solver.xlsx
├── 🐍 ShopFast_Optimasi_Python.py
├── 📄 README.md
```

---

## ▶️ Cara Menjalankan Program Python
Pastikan Python telah terinstal, kemudian install library yang dibutuhkan:

```bash
pip install scipy
```

Jalankan program:
```bash
python ShopFast_Optimasi_Python.py
```

Program akan:
- Menerima input data
- Menampilkan jumlah session optimal (variabel keputusan)
- Menampilkan keuntungan maksimum

---

## 📈 Ringkasan Hasil
- Model berhasil menentukan alokasi session optimal.
- Hasil Excel Solver dan Python (SciPy) menunjukkan hasil yang **konsisten**.
- Analisis sensitivitas menunjukkan bahwa perubahan biaya sistem berpengaruh signifikan terhadap solusi optimal.

---

## 📝 Kesimpulan
Pendekatan Linear Programming efektif digunakan untuk membantu pengambilan keputusan berbasis data pada sistem informasi penjualan.  
Model ini dapat dikembangkan lebih lanjut dengan menambahkan variabel lain seperti kapasitas server dinamis, permintaan pasar, atau indikator kualitas layanan.

---

## 👨‍🎓 Informasi Penyusun
Proyek ini disusun oleh mahasiswa Program Studi **Teknik Informatika (S1)**:

- **Fadel Ripai** – 2025  
- **Tias Anggara Putra** – 2025  
- **Yumaarya Sutaanjali** – 2025  

Universitas Pamulang

---

## 📚 Referensi
- Taha, H. A. (2017). *Operations Research: An Introduction*. Pearson.  
- Winston, W. L. (2004). *Operations Research: Applications and Algorithms*. Duxbury Press.

---

## ⚠️ Catatan Lisensi & Penggunaan
Proyek ini dibuat untuk **keperluan akademik** pada mata kuliah **Riset Operasional / Teknik Riset Operasional**.

Diperbolehkan digunakan sebagai **referensi pembelajaran** dengan mencantumkan sumber dan nama penyusun:

- Fadel Ripai – Teknik Informatika S1, 2025  
- Tias Anggara Putra – Teknik Informatika S1, 2025  
- Yumaarya Sutaanjali – Teknik Informatika S1, 2025
