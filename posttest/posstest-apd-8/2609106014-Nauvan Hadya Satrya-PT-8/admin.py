from prettytable import PrettyTable
import data
from tampilan import bersih, header, jeda, info
from menu import pilih_menu


def lihat_akun():
    bersih()
    header("DAFTAR AKUN TERDAFTAR")
    tabel = PrettyTable(["No", "Username", "Role"])
    nomor = 0
    for kunci, akun_ada in data.akun.items():
        nomor += 1
        tabel.add_row([nomor, akun_ada["username"], akun_ada["role"]])
    tabel.align = "l"
    print(tabel)
    jeda()


def lihat_semua_wardrobe():
    bersih()
    header("SEMUA WARDROBE USER")
    tabel = PrettyTable(["No", "User", "Jenis", "Warna"])
    nomor = 0
    for pemilik, daftar in data.pakaian.items():
        for item in daftar.values():
            nomor += 1
            tabel.add_row([nomor, data.akun[pemilik]["username"], item["jenis"], item["warna"]])
    if nomor == 0:
        info("(Belum ada data wardrobe)")
    else:
        tabel.align = "l"
        print(tabel)
    jeda()


def lihat_semua_outfit():
    bersih()
    header("SEMUA OUTFIT")
    tabel = PrettyTable(["No", "User", "Nama Outfit", "Style"])
    nomor = 0
    for pemilik, daftar in data.outfit.items():
        for s in daftar.values():
            nomor += 1
            tabel.add_row([nomor, data.akun[pemilik]["username"], s["nama"], s["style"]])
    if nomor == 0:
        info("(Belum ada data outfit)")
    else:
        tabel.align = "l"
        print(tabel)
    jeda()


def menu_admin():
    aktif = True
    while aktif:
        bersih()
        header("MENU ADMIN")
        pilih = pilih_menu("Pilih menu", [
            ("Lihat Daftar Akun", "1"),
            ("Lihat Semua Wardrobe User", "2"),
            ("Lihat Semua Outfit User", "3"),
            ("Logout", "0"),
        ])
        if pilih == "1":
            lihat_akun()
        elif pilih == "2":
            lihat_semua_wardrobe()
        elif pilih == "3":
            lihat_semua_outfit()
        else:
            aktif = False