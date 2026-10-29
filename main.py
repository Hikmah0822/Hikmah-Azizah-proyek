
from src.input_data import input_nilai, baca_nilai_contoh
from src.proses import ringkasan_nilai
from src.output import tampilkan_hasil, simpan_hasil


def main():
    print("=== PROGRAM ANALISIS NILAI SISWA ===")
    print("1. Masukkan nilai sendiri")
    print("2. Gunakan data contoh")

    pilihan = input("Pilih menu (1/2): ").strip()

    if pilihan == "1":
        nilai = input_nilai()
    elif pilihan == "2":
        nilai = baca_nilai_contoh()
    else:
        print("Pilihan tidak valid.")
        return

    if not nilai:
        print("Data nilai kosong. Program dihentikan.")
        return

    hasil = ringkasan_nilai(nilai)
    tampilkan_hasil(hasil)

    simpan = input("Simpan hasil ke file? (y/n): ").strip().lower()

    if simpan == "y":
        simpan_hasil(hasil)
        print("Hasil berhasil disimpan.")


if __name__ == "__main__":
    main()
