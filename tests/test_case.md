# TEST CASE
## Program Analisis Nilai Siswa

**Nama:** Hikmah Azizah  

**NIM:** 2225250086

**Kelas:** 3B

---

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan bahwa Program Analisis Nilai Siswa berjalan dengan benar. Pengujian mencakup input nilai, pembacaan data dari file, validasi nilai, perhitungan statistik, penentuan kelulusan, serta penyimpanan hasil analisis.

## 2. Ketentuan Program

- Nilai siswa berada pada rentang 0 sampai 100.
- Batas kelulusan adalah 60.
- Siswa dengan nilai lebih besar atau sama dengan 60 dinyatakan **Lulus**.
- Siswa dengan nilai kurang dari 60 dinyatakan **Tidak Lulus**.
- Input yang bukan angka ditolak.
- Data kosong tidak menyebabkan program mengalami pembagian dengan nol.
- Hasil analisis dapat ditampilkan dan disimpan ke file teks.

## 3. Data Pengujian

Isi file `data/contoh_data.txt`:

```text
70, 80, 90, 55, 60, 75, 85, 40, 95, 65
```

Data terdiri dari 10 nilai siswa dengan rentang nilai 40 sampai 95.

## 4. Daftar Test Case

| ID | Skenario Pengujian | Data Masukan | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Memasukkan nilai di atas batas kelulusan | 85 | Nilai diterima dan siswa lulus |
| TC02 | Memasukkan nilai tepat pada batas kelulusan | 60 | Nilai diterima dan siswa lulus |
| TC03 | Memasukkan nilai di bawah batas kelulusan | 45 | Nilai diterima dan siswa tidak lulus |
| TC04 | Memasukkan nilai minimum | 0 | Nilai diterima |
| TC05 | Memasukkan nilai maksimum | 100 | Nilai diterima |
| TC06 | Memasukkan nilai di bawah rentang | -5 | Nilai ditolak dan diminta memasukkan ulang |
| TC07 | Memasukkan nilai di atas rentang | 110 | Nilai ditolak dan diminta memasukkan ulang |
| TC08 | Memasukkan teks sebagai nilai | abc | Pesan input tidak valid ditampilkan |
| TC09 | Memasukkan beberapa nilai valid | 70,80,90 | Data diterima dan diproses |
| TC10 | Memasukkan input kosong |