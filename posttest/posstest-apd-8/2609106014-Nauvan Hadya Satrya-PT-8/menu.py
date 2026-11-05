from prettytable import PrettyTable
from tampilan import gagal


def pilih_menu(judul, pilihan):
    tabel = PrettyTable(["Kode", "Menu"])
    daftar_kode = []
    for label, kode in pilihan:
        tabel.add_row([kode, label])
        daftar_kode.append(kode)
    tabel.align = "l"
    print(tabel)

    while True:
        jawab = input(f"{judul}: ").strip()
        if jawab in daftar_kode:
            return jawab
        gagal("Pilihan tidak valid!")