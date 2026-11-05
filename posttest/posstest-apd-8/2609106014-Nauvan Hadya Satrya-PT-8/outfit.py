from prettytable import PrettyTable
import data
from tampilan import (bersih, header, jeda, tampil_item, tampil_outfit, tampil_detail_set,
                      tampil_pilihan, sukses, gagal, info)
from validasi import pilih_nomor, pilih_id, input_ya_tidak, input_angka
from wardrobe import kumpulkan_wardrobe
from menu import pilih_menu


def simpan_outfit(pilih_builder):
    bersih()
    header("BUAT OUTFIT" if pilih_builder == "1" else "UBAH OUTFIT")
    wardrobe = kumpulkan_wardrobe()
    atasan = wardrobe["atasan"]
    bawahan = wardrobe["bawahan"]
    sepatu = wardrobe["sepatu"]

    if len(atasan) == 0 or len(bawahan) == 0 or len(sepatu) == 0:
        gagal("Wardrobe belum lengkap!")
        gagal("Minimal punya 1 baju, 1 celana, dan 1 sepatu.")
        gagal("Tambahkan dulu di menu Kelola Wardrobe.")
        jeda()
        return

    daftar_outfit = data.outfit[data.user_login]
    id_ubah = 0

    try:
        if pilih_builder == "3":
            if len(daftar_outfit) == 0:
                raise ValueError("(Belum ada outfit)")
            tampil_outfit(daftar_outfit)
            id_ubah = pilih_id(daftar_outfit, "Pilih nomor outfit yang diubah: ")

        nama_outfit = input("Nama outfit: ").strip()
        if nama_outfit == "":
            raise ValueError("Nama outfit tidak boleh kosong!")

        info("Pilih Atasan:")
        tampil_item(atasan)
        id_atasan = pilih_id(atasan, "Pilih atasan: ")

        info("Pilih Bawahan:")
        tampil_item(bawahan)
        id_bawahan = pilih_id(bawahan, "Pilih bawahan: ")

        info("Pilih Sepatu:")
        tampil_item(sepatu)
        id_sepatu = pilih_id(sepatu, "Pilih sepatu: ")

        info("Pilih Style Outfit:")
        style_dipilih = pilih_nomor(data.style_default, "Pilih style: ")
    except ValueError as error:
        gagal(error)
        jeda()
        return

    data_outfit = {
        "nama": nama_outfit,
        "style": style_dipilih,
        "baju": atasan[id_atasan].copy(),
        "celana": bawahan[id_bawahan].copy(),
        "sepatu": sepatu[id_sepatu].copy(),
    }

    info("Kombinasi outfit:")
    print(f"Nama  : {nama_outfit}")
    print(f"Style : {style_dipilih}")
    tampil_detail_set(data_outfit)
    info("Simpan outfit?")

    if input_ya_tidak():
        if pilih_builder == "3":
            daftar_outfit[id_ubah] = data_outfit
        else:
            daftar_outfit[data.buat_id_outfit()] = data_outfit
        sukses("Outfit berhasil disimpan!")
    else:
        info("Dibatalkan.")
    jeda()


def lihat_outfit():
    bersih()
    header("OUTFIT SAYA")
    tampil_outfit(data.outfit[data.user_login])
    jeda()


def hapus_outfit():
    bersih()
    header("HAPUS OUTFIT")
    daftar_outfit = data.outfit[data.user_login]
    tampil_outfit(daftar_outfit)
    if len(daftar_outfit) > 0:
        try:
            id_set = pilih_id(daftar_outfit, "Pilih nomor outfit: ")
        except ValueError as error:
            gagal(error)
        else:
            info("Yakin hapus?")
            if input_ya_tidak():
                del daftar_outfit[id_set]
                sukses("Outfit berhasil dihapus!")
            else:
                info("Dibatalkan.")
    jeda()


def outfit_builder():
    aktif = True
    while aktif:
        bersih()
        header("OUTFIT BUILDER")
        pilih = pilih_menu("Pilih menu", [
            ("Buat Outfit", "1"),
            ("Lihat Outfit Saya", "2"),
            ("Ubah Outfit", "3"),
            ("Hapus Outfit", "4"),
            ("Kembali", "0"),
        ])
        if pilih == "1":
            simpan_outfit("1")
        elif pilih == "2":
            lihat_outfit()
        elif pilih == "3":
            simpan_outfit("3")
        elif pilih == "4":
            hapus_outfit()
        else:
            aktif = False


def lihat_outfit_style():
    aktif = True
    while aktif:
        bersih()
        header("PILIH STYLE")
        tampil_pilihan(data.style_default)
        print("0. Kembali")
        pilih = input_angka("Pilih style: ")

        if pilih == 0:
            aktif = False
        elif pilih < 1 or pilih > len(data.style_default):
            gagal("Nomor tidak ada!")
            jeda()
        else:
            style_dipilih = data.style_default[pilih - 1]
            bersih()
            header(f"OUTFIT STYLE {style_dipilih.upper()}")
            tabel = PrettyTable(["No", "Nama", "Baju", "Celana", "Sepatu"])
            d = data.outfit_default[style_dipilih]
            tabel.add_row([
                1, "Set Default",
                f"{d['baju']['jenis']} {d['baju']['warna']}",
                f"{d['celana']['jenis']} {d['celana']['warna']}",
                f"{d['sepatu']['jenis']} {d['sepatu']['warna']}",
            ])
            nomor_urut = 1
            for s in data.outfit[data.user_login].values():
                if s["style"] == style_dipilih:
                    nomor_urut += 1
                    tabel.add_row([
                        nomor_urut, f"{s['nama']} (Buatan Anda)",
                        f"{s['baju']['jenis']} {s['baju']['warna']}",
                        f"{s['celana']['jenis']} {s['celana']['warna']}",
                        f"{s['sepatu']['jenis']} {s['sepatu']['warna']}",
                    ])
            tabel.align = "l"
            print(tabel)
            jeda()