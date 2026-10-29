
from pathlib import Path

LOKASI_HASIL = Path(__file__).resolve().parent.parent / "data" / "hasil_analisis.txt"


def format_hasil(hasil):
    nilai_lulus = ", ".join(map(str, hasil["nilai_lulus"]))
    if not nilai_lulus:
        nilai_lulus = "Tidak ada"

    return (
        "\n=== HASIL ANALISIS NILAI ===\n"
        f"Seluruh nilai       : {hasil['nilai']}\n"
        f"Jumlah data         : {hasil['jumlah']}\n"
        f"Total nilai         : {hasil['total']}\n"
        f"Rata-rata           : {hasil['rata_rata']:.2f}\n"
        f"Nilai minimum       : {hasil['minimum']}\n"
        f"Nilai maksimum      : {hasil['maksimum']}\n"
        f"Nilai yang lulus    : {nilai_lulus}\n"
        f"Jumlah lulus        : {hasil['jumlah_lulus']}\n"
        f"Jumlah tidak lulus  : {hasil['jumlah_tidak_lulus']}\n"
        "Batas kelulusan     : 60\n"
    )


def tampilkan_hasil(hasil):
    print(format_hasil(hasil))


def simpan_hasil(hasil):
    LOKASI_HASIL.parent.mkdir(parents=True, exist_ok=True)
    LOKASI_HASIL.write_text(
        format_hasil(hasil),
        encoding="utf-8"
    )
