
BATAS_LULUS = 60


def hitung_rata_rata(nilai):
    if not nilai:
        return 0

    return sum(nilai) / len(nilai)


def status_lulus(nilai, batas=BATAS_LULUS):
    return [x for x in nilai if x >= batas]


def ringkasan_nilai(nilai):
    return {
        "nilai": nilai,
        "jumlah": len(nilai),
        "total": sum(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "nilai_lulus": status_lulus(nilai),
        "jumlah_lulus": len(status_lulus(nilai)),
        "jumlah_tidak_lulus": len(nilai) - len(status_lulus(nilai)),
    }
