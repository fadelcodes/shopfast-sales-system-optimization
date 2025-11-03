# shopfast-sales-system-optimization
Proyek riset operasional yang menganalisis kelayakan finansial implementasi sistem informasi penjualan ShopFast melalui pendekatan Cost–Benefit Analysis (CBA). Mencakup perumusan model, fungsi tujuan, serta perhitungan NPV, B/C Ratio, dan Payback Period menggunakan Excel Modeling.

# 🛍️ ShopFast Sales System Optimization  
**Analisis Efisiensi Sistem Informasi Penjualan Menggunakan Metode Cost–Benefit Analysis (CBA)**  
Proyek Riset Operasional – Fakultas Teknik Industri  

---

## 📘 Deskripsi Proyek
Proyek ini merupakan studi kasus analisis dan optimasi sistem informasi penjualan pada startup e-commerce fiktif bernama **ShopFast**.  
Tujuannya adalah untuk menilai efisiensi biaya implementasi sistem informasi baru dengan menggunakan **metode Cost–Benefit Analysis (CBA)** berbasis **perhitungan manual dan Microsoft Excel**.

Analisis ini dilakukan untuk menentukan apakah investasi sistem informasi layak secara finansial dengan mempertimbangkan seluruh komponen biaya dan manfaat yang diperoleh.

---

## 🎯 Tujuan Penelitian
1. Mengidentifikasi seluruh komponen **biaya (cost)** dan **manfaat (benefit)** dari implementasi sistem.  
2. **Membangun model matematis** evaluasi investasi dengan pendekatan *Cost–Benefit Analysis*.  
3. Menentukan **kelayakan proyek** melalui perhitungan NPV (Net Present Value), B/C Ratio, dan Payback Period.  
4. Memberikan **rekomendasi implementasi sistem** berdasarkan hasil analisis.

---

## 🏢 Studi Kasus: ShopFast
- **Nama perusahaan:** ShopFast (startup e-commerce fiktif)  
- **Periode analisis:** 2024–2029  
- **Investasi awal:** Rp 85.000.000  
- **Tingkat diskonto:** 10% per tahun  
- **Metode perhitungan:** Manual dan Excel (tanpa pemrograman Python)

---

## 📊 Model dan Formulasi

### Fungsi Tujuan
Maksimalkan nilai kelayakan investasi dengan:
\[
\text{Maximize: } NPV = \sum_{t=1}^{n} \frac{Benefit_t - Cost_t}{(1+r)^t} - I
\]

### Kendala Model
- \( I \leq 85{,}000{,}000 \) (batas investasi awal)  
- \( Benefit_t \geq 0 \) untuk setiap tahun t  
- Horizon waktu \( n = 5 \) tahun  
- Diskonto \( r = 10\% \)

---

## 🧮 Metode Perhitungan
Perhitungan dilakukan menggunakan **Microsoft Excel**, dengan langkah:
1. Menyusun tabel biaya & manfaat tahunan.  
2. Menghitung arus kas bersih (Net Cash Flow) tiap tahun.  
3. Menggunakan rumus:
   - `NPV = SUM(PV Cash Flow) - Investment`
   - `PV Cash Flow = Net Cash Flow / (1+r)^t`
   - `B/C Ratio = PV(Benefit) / PV(Cost)`
   - `Payback Period = waktu hingga kumulatif PV ≥ 0`

---

## 🗂️ Struktur Folder

shopfast-sales-system-optimization/
├─ README.md
├─ Laporan_Proyek_Riset_Operasional_Fadel_UPDATED.docx
├─ ShopFast_CBA_Analysis_Updated.xlsx
├─ monthly_transactions_updated.csv
├─ annual_costs_benefits_updated.csv
└─ kpi_metrics_updated.csv



---

## 📈 Hasil Analisis
| Parameter | Nilai | Interpretasi |
|------------|--------|--------------|
| **NPV** | Rp 82.370.398 | Positif → proyek layak |
| **Benefit/Cost Ratio** | 1.61 | > 1 → proyek menguntungkan |
| **Discounted Payback Period** | ± 3,2 tahun | Modal kembali sebelum akhir periode analisis |

---

## 🧩 Interpretasi
Hasil menunjukkan bahwa sistem informasi penjualan yang diimplementasikan oleh **ShopFast** efisien secara biaya dan memberikan manfaat nyata dalam jangka menengah.  
Dengan NPV positif dan B/C Ratio di atas 1, proyek ini **layak diimplementasikan** dan berpotensi meningkatkan produktivitas serta profitabilitas perusahaan.

---

## 📄 Lisensi
Proyek ini dibuat untuk tujuan akademik dalam mata kuliah **Teknik Riset Operasional**.  
Diperbolehkan digunakan sebagai referensi dengan mencantumkan sumber dan nama penyusun asli:  
**Fadel Ripai** – Teknik Informatika S1, 2025.
**Tias Anggara Putra** - Teknik Informatika S1, 2025.
**Yumaarya Sutaanjali** - Teknik Informatika S1, 2025.




