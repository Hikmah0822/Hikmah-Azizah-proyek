
from pathlib import Path

LOKASI_DATA = Path(__file__).resolve().parent.parent / "data" / "contoh_data.txt"


def input_nilai():
    while True:
        teks = input(
            "Masukkan nilai siswa, pisahkan dengan koma: "
        ).strip()

        try:
            if not teks:
                print("Nilai tidak boleh kosong.")
                continue

            nilai = [float(item.strip()) for item in teks.split(",")]

            if any(x < 0 or x > 100 for x in nilai):
                print("Nilai harus berada antara 0 sampai 100.")
                continue

            return nilai

        except ValueError:
            print("Input tidak valid. Masukkan angka, misalnya 70,80,90.")


def baca_nilai_contoh():
    try:
        teks = LOKASI_DATA.read_text(encoding="utf-8")
        nilai = [
            float(item.strip())
            for item in teks.replace("\n", ",").split(",")
            if item.strip()
        ]

        if any(x < 0 or x > 100 for x in nilai):
            raise ValueError("Nilai harus antara 0 sampai 100.")

        return nilai

    except (OSError, ValueError) as error:
        print(f"Gagal membaca data contoh: {error}")
        return []
