import data
from tampilan import bersih, header
from menu import pilih_menu
from wardrobe import kelola_wardrobe
from outfit import outfit_builder, lihat_outfit_style


def menu_user():
    aktif = True
    while aktif:
        bersih()
        header("MENU PENGGUNA")
        print("Halo,", data.akun[data.user_login]["username"])
        pilih = pilih_menu("Pilih menu", [
            ("Kelola Wardrobe (Pakaian & Sepatu)", "1"),
            ("Outfit Builder", "2"),
            ("Lihat Outfit Berdasarkan Style", "3"),
            ("Logout", "0"),
        ])
        if pilih == "1":
            kelola_wardrobe()
        elif pilih == "2":
            outfit_builder()
        elif pilih == "3":
            lihat_outfit_style()
        else:
            aktif = False