import data
from tampilan import bersih, header, jeda, tampil_item, sukses, gagal, info
from validasi import pilih_nomor, pilih_id, input_ya_tidak
from menu import pilih_menu


def kumpulkan_wardrobe():
    atasan = {}
    bawahan = {}
    sepatu = {}
    for id_item, item in data.pakaian[data.user_login].items():
        if item["jenis"] in data.baju_default:
            atasan[id_item] = item
        elif item["jenis"] in data.celana_default:
            bawahan[id_item] = item
        elif item["jenis"] in data.sepatu_default:
            sepatu[id_item] = item
    return {"atasan": atasan, "bawahan": bawahan, "sepatu": sepatu}


def tambah_item():
    bersih()
    header("TAMBAH ITEM")
    daftar_jenis = data.baju_default + data.celana_default + data.sepatu_default
    try:
        jenis = pilih_nomor(daftar_jenis, "Pilih jenis: ")
        warna = pilih_nomor(data.warna_default, "Pilih warna: ")
    except ValueError as error:
        gagal(error)
    else:
        data.pakaian[data.user_login][data.buat_id_pakaian()] = {"jenis": jenis, "warna": warna}
        sukses("Item berhasil ditambahkan!")
    jeda()


def lihat_wardrobe():
    bersih()
    header("WARDROBE ANDA")
    tampil_item(data.pakaian[data.user_login])
    jeda()


def ubah_item():
    bersih()
    header("UBAH ITEM")
    daftar_pakaian = data.pakaian[data.user_login]
    tampil_item(daftar_pakaian)
    if len(daftar_pakaian) > 0:
        try:
            id_item = pilih_id(daftar_pakaian, "Pilih nomor item: ")
            warna = pilih_nomor(data.warna_default, "Pilih warna baru: ")
        except ValueError as error:
            gagal(error)
        else:
            daftar_pakaian[id_item]["warna"] = warna
            sukses("Item berhasil diubah!")
    jeda()


def hapus_item():
    bersih()
    header("HAPUS ITEM")
    daftar_pakaian = data.pakaian[data.user_login]
    tampil_item(daftar_pakaian)
    if len(daftar_pakaian) > 0:
        try:
            id_item = pilih_id(daftar_pakaian, "Pilih nomor item: ")
        except ValueError as error:
            gagal(error)
        else:
            info("Yakin hapus?")
            if input_ya_tidak():
                del daftar_pakaian[id_item]
                sukses("Item berhasil dihapus!")
            else:
                info("Dibatalkan.")
    jeda()


def kelola_wardrobe():
    aktif = True
    while aktif:
        bersih()
        header("KELOLA WARDROBE")
        pilih = pilih_menu("Pilih menu", [
            ("Tambah Item", "1"),
            ("Lihat Wardrobe", "2"),
            ("Ubah Item", "3"),
            ("Hapus Item", "4"),
            ("Kembali", "0"),
        ])
        if pilih == "1":
            tambah_item()
        elif pilih == "2":
            lihat_wardrobe()
        elif pilih == "3":
            ubah_item()
        elif pilih == "4":
            hapus_item()
        else:
            aktif = False