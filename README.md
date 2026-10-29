# PROGRAM ANALISIS NILAI SISWA

**Nama:** Hikmah Azizah  

**NIM:** 2225250086

**Kelas:** 3B

## 1. Deskripsi Program

Program Analisis Nilai Siswa merupakan aplikasi sederhana berbasis Python yang digunakan untuk menerima, membaca, memvalidasi, mengolah, dan menampilkan data nilai siswa.

Program ini membantu proses analisis nilai dengan menghitung jumlah data, total nilai, rata-rata, nilai tertinggi, nilai terendah, serta jumlah siswa yang lulus dan tidak lulus.

Batas kelulusan yang digunakan adalah 60. Siswa dinyatakan lulus apabila memperoleh nilai minimal 60.

## 2. Tujuan Program

Tujuan pembuatan program ini adalah:

1. Menerima input nilai siswa secara manual.
2. Membaca data nilai dari file teks.
3. Memvalidasi nilai agar berada pada rentang 0–100.
4. Menghitung statistik nilai siswa.
5. Menentukan jumlah siswa yang lulus dan tidak lulus.
6. Menampilkan dan menyimpan hasil analisis ke file teks.
7. Menerapkan penggunaan fungsi, modul, percabangan, perulangan, dan pengolahan file dalam Python.

## 3. Fitur Program

Fitur yang tersedia meliputi:

- Memasukkan nilai siswa secara manual.
- Membaca data nilai dari file teks.
- Menolak input yang bukan angka.
- Memvalidasi nilai agar berada pada rentang 0–100.
- Menghitung jumlah data dan total nilai.
- Menghitung rata-rata nilai.
- Menentukan nilai tertinggi dan terendah.
- Menghitung jumlah siswa yang lulus dan tidak lulus.
- Menampilkan hasil analisis di terminal.
- Menyimpan hasil analisis ke file teks.

## 4. Struktur Folder

```text
perancangan-proyek-rekap-analisis-nilai-matematika/
├── main.py
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── data/
│   ├── contoh_data.txt
│   └── hasil_analisis.txt
└── tests/
    └── test_case.md
```

**Keterangan fungsi file:**

| File | Fungsi |
|---|---|
| `main.py` | Menjalankan program utama dan mengatur alur program |
| `src/__init__.py` | Menandai folder `src` sebagai package Python |
| `src/input_data.py` | Menerima input manual dan membaca data dari file |
| `src/proses.py` | Menghitung statistik nilai dan status kelulusan |
| `src/output.py` | Menampilkan dan menyimpan hasil analisis |
| `data/contoh_data.txt` | Menyimpan data nilai contoh |
| `data/hasil_analisis.txt` | Menyimpan hasil analisis