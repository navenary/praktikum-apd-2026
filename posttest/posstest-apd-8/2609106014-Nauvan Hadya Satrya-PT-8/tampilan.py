import os
from colorama import Fore, init
from prettytable import PrettyTable

init(autoreset=True)


def bersih():
    os.system("cls" if os.name == "nt" else "clear")


def jeda():
    input("Tekan Enter...")


def header(judul):
    tabel = PrettyTable()
    tabel.header = False
    tabel.add_row([judul])
    tabel.align = "c"
    print(Fore.WHITE + str(tabel))


def sukses(pesan):
    print(Fore.GREEN + pesan)


def gagal(pesan):
    print(Fore.RED + str(pesan))


def info(pesan):
    print(Fore.YELLOW + pesan)


def _cetak(tabel):
    tabel.align = "l"
    print(tabel)


def tampil_pilihan(daftar):
    tabel = PrettyTable(["No", "Pilihan"])
    nomor = 0
    for nama in daftar:
        nomor += 1
        tabel.add_row([nomor, nama])
    _cetak(tabel)


def tampil_item(daftar_item):
    if len(daftar_item) == 0:
        info("(Belum ada item di wardrobe)")
        return
    tabel = PrettyTable(["No", "Jenis", "Warna"])
    nomor = 0
    for id_item, item in daftar_item.items():
        nomor += 1
        tabel.add_row([nomor, item["jenis"], item["warna"]])
    _cetak(tabel)


def tampil_detail_set(set_outfit):
    tabel = PrettyTable(["Bagian", "Jenis", "Warna"])
    for bagian in ("baju", "celana", "sepatu"):
        tabel.add_row([bagian.capitalize(), set_outfit[bagian]["jenis"], set_outfit[bagian]["warna"]])
    _cetak(tabel)


def tampil_outfit(daftar_outfit):
    if len(daftar_outfit) == 0:
        info("(Belum ada outfit)")
        return
    tabel = PrettyTable(["No", "Nama", "Style", "Baju", "Celana", "Sepatu"])
    nomor = 0
    for id_set, s in daftar_outfit.items():
        nomor += 1
        tabel.add_row([
            nomor, s["nama"], s["style"],
            f"{s['baju']['jenis']} {s['baju']['warna']}",
            f"{s['celana']['jenis']} {s['celana']['warna']}",
            f"{s['sepatu']['jenis']} {s['sepatu']['warna']}",
        ])
    _cetak(tabel)