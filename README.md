🛍️ ShopFast Sales System Optimization

Analisis dan Optimasi Sistem Informasi Penjualan Menggunakan
Cost–Benefit Analysis (CBA) dan Linear Programming

Proyek Riset Operasional – Fakultas Teknik
Program Studi Teknik Informatika

📘 Deskripsi Proyek

Proyek ini merupakan studi kasus analisis dan optimasi sistem informasi penjualan pada sebuah perusahaan e-commerce fiktif bernama ShopFast.
Penelitian difokuskan pada dua aspek utama:

Evaluasi kelayakan finansial implementasi sistem informasi menggunakan metode Cost–Benefit Analysis (CBA).

Optimasi alokasi traffic/session penjualan antar kategori produk menggunakan Linear Programming, yang diselesaikan dengan Excel Solver dan Python (SciPy).

Pendekatan ini bertujuan untuk membantu manajemen dalam mengambil keputusan investasi sistem yang efisien, optimal, dan berbasis data.

🎯 Tujuan Penelitian

Mengidentifikasi seluruh komponen biaya (cost) dan manfaat (benefit) dari implementasi sistem informasi penjualan.

Membangun model matematis Cost–Benefit Analysis (CBA) untuk mengevaluasi kelayakan investasi.

Mengoptimalkan alokasi session penjualan untuk memaksimalkan revenue dan profit.

Membandingkan hasil optimasi menggunakan dua software berbeda (Excel Solver vs Python).

Melakukan analisis sensitivitas untuk menilai stabilitas model terhadap perubahan parameter.

Memberikan rekomendasi strategis sebagai konsultan bisnis.

🏢 Studi Kasus: ShopFast

Nama perusahaan : ShopFast (startup e-commerce fiktif)

Kategori produk : Fashion, Electronics, Home & Living, Beauty, Sports

Periode analisis CBA : 2024 – 2029

Investasi awal : Rp 85.000.000

Tingkat diskonto : 10% per tahun

Total session bulanan : 100.000

Pendekatan : Manual, Excel Solver, dan Python

📊 Model dan Formulasi
🔹 Fungsi Tujuan (Optimasi)

Maksimisasi total revenue dari seluruh kategori produk:

Maximize 
𝑍
=
∑
𝑖
=
1
𝑛
(
𝑅
𝑒
𝑣
𝑒
𝑛
𝑢
𝑒
_
𝑝
𝑒
𝑟
_
𝑆
𝑒
𝑠
𝑠
𝑖
𝑜
𝑛
𝑖
×
𝑆
𝑒
𝑠
𝑠
𝑖
𝑜
𝑛
𝑠
𝑖
)
Maximize Z=
i=1
∑
n
	​

(Revenue_per_Session
i
	​

×Sessions
i
	​

)
🔹 Kendala

Total session tidak melebihi batas:

∑
𝑆
𝑒
𝑠
𝑠
𝑖
𝑜
𝑛
𝑠
𝑖
≤
100.000
∑Sessions
i
	​

≤100.000

Batas minimum dan maksimum session tiap kategori:

𝑀
𝑖
𝑛
𝑖
≤
𝑆
𝑒
𝑠
𝑠
𝑖
𝑜
𝑛
𝑠
𝑖
≤
𝑀
𝑎
𝑥
𝑖
Min
i
	​

≤Sessions
i
	​

≤Max
i
	​


Sessions ≥ 0

🔹 Fungsi Tujuan (Cost–Benefit Analysis)
𝑁
𝑃
𝑉
=
∑
𝑡
=
1
𝑛
𝐵
𝑒
𝑛
𝑒
𝑓
𝑖
𝑡
𝑡
−
𝐶
𝑜
𝑠
𝑡
𝑡
(
1
+
𝑟
)
𝑡
−
𝐼
NPV=
t=1
∑
n
	​

(1+r)
t
Benefit
t
	​

−Cost
t
	​

	​

−I

Dengan:

𝑟
=
10
%
r=10%

𝑛
=
5
n=5 tahun

𝐼
I = investasi awal

🧮 Metode Penyelesaian
1️⃣ Metode Manual

Perhitungan kontribusi revenue dan profit secara langsung.

Verifikasi kendala min–max session.

Validasi total session dan total revenue.

2️⃣ Excel Solver

Menggunakan Simplex LP.

Formula Excel aktif untuk:

Revenue Contribution

Profit Contribution

Total Revenue

Total Sessions

Dilengkapi grafik hasil optimasi dan sensitivitas.

3️⃣ Python (SciPy – linprog)

Library: pandas, numpy, scipy.optimize

Model optimasi identik dengan Excel Solver.

Digunakan untuk validasi hasil.

📊 Analisis Sensitivitas

Dilakukan dengan memvariasikan total session:

80.000

100.000

120.000

Hasil menunjukkan:

Kategori Electronics selalu menjadi prioritas utama.

Peningkatan kapasitas session secara langsung meningkatkan total revenue.

Model optimasi bersifat stabil dan robust.

📈 Hasil Analisis Utama
🔹 Optimasi Session
Kategori	Session Optimal
Fashion	5.000
Electronics	40.000
Home & Living	25.000
Beauty	5.000
Sports	25.000

Total Revenue Optimal
➡️ Rp 1.913.700.000

Hasil Excel Solver dan Python identik.

🔹 Cost–Benefit Analysis (CBA)
Parameter	Nilai	Interpretasi
NPV	Positif	Proyek layak
B/C Ratio	> 1	Proyek menguntungkan
Payback Period	< 5 tahun	Modal kembali sebelum akhir periode
🧩 Interpretasi & Rekomendasi

Berdasarkan hasil optimasi dan CBA:

Implementasi sistem informasi penjualan layak secara finansial.

Fokus utama strategi penjualan sebaiknya diarahkan pada kategori Electronics.

Penambahan kapasitas traffic akan memberikan peningkatan revenue yang signifikan.

Model optimasi dapat dijadikan alat bantu pengambilan keputusan manajerial.

🗂️ Struktur Repository
shopfast-sales-system-optimization/
│
├── README.md
├── Metode_Manual_ShopFast.xlsx
├── ShopFast_Excel_Solver_Lengkap_Dengan_Grafik.xlsx
├── optimization_shopfast.py
└── laporan_akhir.pdf

📄 Lisensi & Catatan Akademik

Proyek ini dibuat untuk keperluan akademik pada mata kuliah
Riset Operasional / Teknik Riset Operasional.

Diperbolehkan digunakan sebagai referensi dengan mencantumkan sumber dan nama penyusun:

Fadel Ripai – Teknik Informatika S1, 2025

Tias Anggara Putra – Teknik Informatika S1, 2025

Yumaarya Sutaanjali – Teknik Informatika S1, 2025
