from tampilan import bersih, header, info
from menu import pilih_menu
from autentikasi import register, login, sesi_login


def main():
    jalan = True
    while jalan:
        bersih()
        header("MANAJEMEN & PERENCANAAN OUTFIT")
        pilih = pilih_menu("Silahkan Pilih Menu", [
            ("Register", "1"),
            ("Login", "2"),
            ("Keluar", "3"),
        ])
        if pilih == "1":
            register()
        elif pilih == "2":
            if login():
                sesi_login()
        else:
            info("Terima kasih!")
            jalan = False


if __name__ == "__main__":
    main()
    