import os

akun = {
    "admin": {"username": "admin", "password": "admin123", "role": "admin"}
}

style_default = ("Casual", "Semi Casual", "Semi Formal", "Formal")
baju_default = ("Kemeja", "Polo Shirt", "Kaos")
celana_default = ("Celana Bahan", "Celana Chino", "Celana Jeans")
sepatu_default = ("Loafers", "Sneakers")
warna_default = ("Hitam", "Putih", "Navy", "Abu-abu", "Coklat")

outfit_default = {
    "Casual": {
        "baju": {"jenis": "Kaos", "warna": "Putih"},
        "celana": {"jenis": "Celana Jeans", "warna": "Navy"},
        "sepatu": {"jenis": "Sneakers", "warna": "Putih"},
    },
    "Semi Casual": {
        "baju": {"jenis": "Polo Shirt", "warna": "Navy"},
        "celana": {"jenis": "Celana Jeans", "warna": "Hitam"},
        "sepatu": {"jenis": "Sneakers", "warna": "Putih"},
    },
    "Semi Formal": {
        "baju": {"jenis": "Kemeja", "warna": "Putih"},
        "celana": {"jenis": "Celana Chino", "warna": "Coklat"},
        "sepatu": {"jenis": "Loafers", "warna": "Coklat"},
    },
    "Formal": {
        "baju": {"jenis": "Kemeja", "warna": "Putih"},
        "celana": {"jenis": "Celana Bahan", "warna": "Hitam"},
        "sepatu": {"jenis": "Loafers", "warna": "Hitam"},
    },
}

pakaian = {}
outfit = {}
id_pakaian = 1
id_outfit = 1

user_login = ""
role_login = ""
jalan = True

while jalan:
    os.system("cls")
    print("==========================================================")
    print("              MANAJEMEN & PERENCANAAN OUTFIT              ")
    print("==========================================================")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    pilih = input("Silahkan Pilih Menu: ")

    if pilih == "1":
        os.system("cls")
        print("==========================================================")
        print("                         REGISTER                         ")
        print("==========================================================")
        username = input("Username: ").strip()
        kunci = username.lower()

        if username == "":
            print("Username tidak boleh kosong!")
        elif " " in username:
            print("Username tidak boleh mengandung spasi!")
        elif kunci in akun:
            print("Username sudah dipakai!")
        else:
            password = input("Masukkan Password Anda: ").strip()
            if password == "":
                print("Password Tidak Boleh Kosong!")
            elif " " in password:
                print("Password Tidak Boleh Mengandung Spasi!")
            else:
                akun[kunci] = {"username": username, "password": password, "role": "user"}
                pakaian[kunci] = {}
                outfit[kunci] = {}
                print("Register berhasil! Silakan login.")
        input("Tekan Enter untuk kembali...")

    elif pilih == "2":
        os.system("cls")
        print("==========================================================")
        print("                          LOGIN                           ")
        print("==========================================================")
        berhasil = False

        for percobaan in range(3):
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            kunci = username.lower()

            if kunci in akun and akun[kunci]["password"] == password:
                berhasil = True
                user_login = kunci
                role_login = akun[kunci]["role"]

            if berhasil:
                break
            print("Username atau password salah! Sisa percobaan:", 2 - percobaan)

        if berhasil:
            sedang_login = True
            while sedang_login:
                os.system("cls")

                if role_login == "admin":
                    print("==========================================================")
                    print("                        MENU ADMIN                        ")
                    print("==========================================================")
                    print("1. Lihat Daftar Akun")
                    print("2. Lihat Semua Wardrobe User")
                    print("3. Lihat Semua Outfit User")
                    print("0. Logout")
                    pilih_admin = input("Pilih menu: ")

                    if pilih_admin == "1":
                        os.system("cls")
                        print("==========================================================")
                        print("                   DAFTAR AKUN TERDAFTAR                  ")
                        print("==========================================================")
                        nomor = 0
                        for kunci, data in akun.items():
                            nomor += 1
                            print(f"{nomor}. Username: {data['username']} : Role: {data['role']}")
                        input("Tekan Enter...")

                    elif pilih_admin == "2":
                        os.system("cls")
                        print("==========================================================")
                        print("                     SEMUA WARDROBE USER                  ")
                        print("==========================================================")
                        nomor = 0
                        for pemilik, daftar in pakaian.items():
                            for id_item, item in daftar.items():
                                nomor += 1
                                print(f"{nomor}. User: {akun[pemilik]['username']} : {item['jenis']} ({item['warna']})")
                        if nomor == 0:
                            print("(Belum ada data wardrobe)")
                        input("Tekan Enter...")

                    elif pilih_admin == "3":
                        os.system("cls")
                        print("==========================================================")
                        print("                        SEMUA OUTFIT                      ")
                        print("==========================================================")
                        nomor = 0
                        for pemilik, daftar in outfit.items():
                            for id_set, set_outfit in daftar.items():
                                nomor += 1
                                print(f"{nomor}. User: {akun[pemilik]['username']} : {set_outfit['nama']} ({set_outfit['style']})")
                        if nomor == 0:
                            print("(Belum ada data outfit)")
                        input("Tekan Enter...")

                    elif pilih_admin == "0":
                        user_login = ""
                        role_login = ""
                        sedang_login = False

                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter...")

                else:
                    print("==========================================================")
                    print("                       MENU PENGGUNA                      ")
                    print("==========================================================")
                    print("Halo,", akun[user_login]["username"])
                    print("1. Kelola Wardrobe (Pakaian & Sepatu)")
                    print("2. Outfit Builder")
                    print("3. Lihat Outfit Berdasarkan Style")
                    print("0. Logout")
                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        di_koleksi = True
                        while di_koleksi:
                            daftar_pakaian = pakaian[user_login]
                            daftar_jenis = baju_default + celana_default + sepatu_default

                            os.system("cls")
                            print("==========================================================")
                            print("                      KELOLA WARDROBE                     ")
                            print("==========================================================")
                            print("1. Tambah Item")
                            print("2. Lihat Wardrobe")
                            print("3. Ubah Item")
                            print("4. Hapus Item")
                            print("0. Kembali")
                            pilih_koleksi = input("Pilih menu: ")

                            if pilih_koleksi == "1":
                                os.system("cls")
                                print("==========================================================")
                                print("                       TAMBAH ITEM                        ")
                                print("==========================================================")
                                nomor_urut = 0
                                for jenis in daftar_jenis:
                                    nomor_urut += 1
                                    print(f"{nomor_urut}. {jenis}")
                                pilih_jenis = int(input("Pilih jenis: "))

                                if pilih_jenis < 1 or pilih_jenis > len(daftar_jenis):
                                    print("Nomor tidak ada!")
                                else:
                                    nomor_urut = 0
                                    for warna in warna_default:
                                        nomor_urut += 1
                                        print(f"{nomor_urut}. {warna}")
                                    pilih_warna = int(input("Pilih warna: "))

                                    if pilih_warna < 1 or pilih_warna > len(warna_default):
                                        print("Nomor tidak ada!")
                                    else:
                                        jenis_dipilih = daftar_jenis[pilih_jenis - 1]
                                        warna_dipilih = warna_default[pilih_warna - 1]
                                        daftar_pakaian[id_pakaian] = {"jenis": jenis_dipilih, "warna": warna_dipilih}
                                        id_pakaian += 1
                                        print("Item berhasil ditambahkan!")
                                input("Tekan Enter...")

                            elif pilih_koleksi == "2":
                                os.system("cls")
                                print("==========================================================")
                                print("                      WARDROBE ANDA                       ")
                                print("==========================================================")
                                for id_item, item in daftar_pakaian.items():
                                    print(f"{id_item}. {item['jenis']} (Warna: {item['warna']})")
                                if len(daftar_pakaian) == 0:
                                    print("(Belum ada item di wardrobe)")
                                input("Tekan Enter...")

                            elif pilih_koleksi == "3":
                                os.system("cls")
                                print("==========================================================")
                                print("                        UBAH ITEM                         ")
                                print("==========================================================")
                                for id_item, item in daftar_pakaian.items():
                                    print(f"{id_item}. {item['jenis']} (Warna: {item['warna']})")
                                if len(daftar_pakaian) == 0:
                                    print("(Belum ada item di wardrobe)")
                                else:
                                    pilih_pakaian = int(input("Pilih nomor item: "))

                                    if pilih_pakaian not in daftar_pakaian:
                                        print("Nomor tidak ada!")
                                    else:
                                        nomor_urut = 0
                                        for warna in warna_default:
                                            nomor_urut += 1
                                            print(f"{nomor_urut}. {warna}")
                                        pilih_warna = int(input("Pilih warna baru: "))

                                        if pilih_warna < 1 or pilih_warna > len(warna_default):
                                            print("Nomor tidak ada!")
                                        else:
                                            daftar_pakaian[pilih_pakaian]["warna"] = warna_default[pilih_warna - 1]
                                            print("Item berhasil diubah!")
                                input("Tekan Enter...")

                            elif pilih_koleksi == "4":
                                os.system("cls")
                                print("==========================================================")
                                print("                        HAPUS ITEM                        ")
                                print("==========================================================")
                                for id_item, item in daftar_pakaian.items():
                                    print(f"{id_item}. {item['jenis']} (Warna: {item['warna']})")
                                if len(daftar_pakaian) == 0:
                                    print("(Belum ada item di wardrobe)")
                                else:
                                    pilih_pakaian = int(input("Pilih nomor item: "))

                                    if pilih_pakaian not in daftar_pakaian:
                                        print("Nomor tidak ada!")
                                    else:
                                        yakin = input("Yakin hapus? (Ya/Tidak): ").lower()
                                        if yakin == "ya":
                                            del daftar_pakaian[pilih_pakaian]
                                            print("Item berhasil dihapus!")
                                        elif yakin == "tidak":
                                            print("Dibatalkan.")
                                        else:
                                            print("Input harus Ya atau Tidak!")
                                input("Tekan Enter...")

                            elif pilih_koleksi == "0":
                                di_koleksi = False

                            else:
                                print("Pilihan Tidak Valid!")
                                input("Tekan Enter...")

                    elif pilih_user == "2":
                        di_builder = True
                        while di_builder:
                            daftar_atasan = {}
                            daftar_bawahan = {}
                            daftar_sepatu = {}
                            for id_item, item in pakaian[user_login].items():
                                if item["jenis"] in baju_default:
                                    daftar_atasan[id_item] = item
                                elif item["jenis"] in celana_default:
                                    daftar_bawahan[id_item] = item
                                elif item["jenis"] in sepatu_default:
                                    daftar_sepatu[id_item] = item

                            daftar_outfit = outfit[user_login]

                            os.system("cls")
                            print("==========================================================")
                            print("                      OUTFIT BUILDER                      ")
                            print("==========================================================")
                            print("1. Buat Outfit")
                            print("2. Lihat Outfit Saya")
                            print("3. Ubah Outfit")
                            print("4. Hapus Outfit")
                            print("0. Kembali")
                            pilih_builder = input("Pilih menu: ")

                            if pilih_builder == "1" or pilih_builder == "3":
                                lanjut = True
                                id_ubah = 0

                                os.system("cls")
                                if pilih_builder == "1":
                                    print("==========================================================")
                                    print("                       BUAT OUTFIT                        ")
                                    print("==========================================================")
                                else:
                                    print("==========================================================")
                                    print("                       UBAH OUTFIT                        ")
                                    print("==========================================================")

                                if len(daftar_atasan) == 0 or len(daftar_bawahan) == 0 or len(daftar_sepatu) == 0:
                                    print("Wardrobe belum lengkap!")
                                    print("Minimal punya 1 baju, 1 celana, dan 1 sepatu.")
                                    print("Tambahkan dulu di menu Kelola Wardrobe.")
                                    lanjut = False

                                if lanjut and pilih_builder == "3":
                                    if len(daftar_outfit) == 0:
                                        print("(belum ada outfit)")
                                        lanjut = False
                                    else:
                                        for id_set, set_outfit in daftar_outfit.items():
                                            print(f"{id_set}. {set_outfit['nama']} ({set_outfit['style']})")
                                        pilih_outfit = int(input("Pilih nomor outfit yang diubah: "))
                                        if pilih_outfit not in daftar_outfit:
                                            print("Nomor tidak ada!")
                                            lanjut = False
                                        else:
                                            id_ubah = pilih_outfit

                                if lanjut:
                                    nama_outfit = input("Nama outfit: ").strip()
                                    if nama_outfit == "":
                                        print("Nama outfit tidak boleh kosong!")
                                        lanjut = False

                                if lanjut:
                                    print("Pilih Atasan:")
                                    for id_item, item in daftar_atasan.items():
                                        print(f"{id_item}. {item['jenis']} {item['warna']}")
                                    pilih_atasan = int(input("Pilih atasan: "))
                                    if pilih_atasan not in daftar_atasan:
                                        print("Nomor tidak ada!")
                                        lanjut = False

                                if lanjut:
                                    print("Pilih Bawahan:")
                                    for id_item, item in daftar_bawahan.items():
                                        print(f"{id_item}. {item['jenis']} {item['warna']}")
                                    pilih_bawahan = int(input("Pilih bawahan: "))
                                    if pilih_bawahan not in daftar_bawahan:
                                        print("Nomor tidak ada!")
                                        lanjut = False

                                if lanjut:
                                    print("Pilih Sepatu:")
                                    for id_item, item in daftar_sepatu.items():
                                        print(f"{id_item}. {item['jenis']} {item['warna']}")
                                    pilih_sepatu = int(input("Pilih sepatu: "))
                                    if pilih_sepatu not in daftar_sepatu:
                                        print("Nomor tidak ada!")
                                        lanjut = False

                                if lanjut:
                                    print("Pilih Style Outfit:")
                                    nomor_urut = 0
                                    for style in style_default:
                                        nomor_urut += 1
                                        print(f"{nomor_urut}. {style}")
                                    pilih_style = int(input("Pilih style: "))
                                    if pilih_style < 1 or pilih_style > len(style_default):
                                        print("Nomor tidak ada!")
                                        lanjut = False

                                if lanjut:
                                    atasan = daftar_atasan[pilih_atasan]
                                    bawahan = daftar_bawahan[pilih_bawahan]
                                    sepatu = daftar_sepatu[pilih_sepatu]
                                    style_dipilih = style_default[pilih_style - 1]

                                    print("Kombinasi outfit:")
                                    print(f"Nama   : {nama_outfit}")
                                    print(f"Style  : {style_dipilih}")
                                    print(f"Baju   : {atasan['jenis']} {atasan['warna']}")
                                    print(f"Celana : {bawahan['jenis']} {bawahan['warna']}")
                                    print(f"Sepatu : {sepatu['jenis']} {sepatu['warna']}")
                                    simpan = input("Simpan outfit? (Ya/Tidak): ").lower()

                                    if simpan == "ya":
                                        data_outfit = {
                                            "nama": nama_outfit,
                                            "style": style_dipilih,
                                            "baju": atasan.copy(),
                                            "celana": bawahan.copy(),
                                            "sepatu": sepatu.copy(),
                                        }
                                        if pilih_builder == "3":
                                            daftar_outfit[id_ubah] = data_outfit
                                        else:
                                            daftar_outfit[id_outfit] = data_outfit
                                            id_outfit += 1
                                        print("Outfit berhasil disimpan!")
                                    elif simpan == "tidak":
                                        print("Dibatalkan.")
                                    else:
                                        print("Input harus Ya atau Tidak!")
                                input("Tekan Enter...")

                            elif pilih_builder == "2":
                                os.system("cls")
                                print("==========================================================")
                                print("                       OUTFIT SAYA                        ")
                                print("==========================================================")
                                for id_set, set_outfit in daftar_outfit.items():
                                    print(f"{id_set}. {set_outfit['nama']} ({set_outfit['style']})")
                                    print(f" Baju   : {set_outfit['baju']['jenis']} {set_outfit['baju']['warna']}")
                                    print(f" Celana : {set_outfit['celana']['jenis']} {set_outfit['celana']['warna']}")
                                    print(f" Sepatu : {set_outfit['sepatu']['jenis']} {set_outfit['sepatu']['warna']}")
                                if len(daftar_outfit) == 0:
                                    print("(belum ada outfit)")
                                input("Tekan Enter...")

                            elif pilih_builder == "4":
                                os.system("cls")
                                print("==========================================================")
                                print("                       HAPUS OUTFIT                       ")
                                print("==========================================================")
                                for id_set, set_outfit in daftar_outfit.items():
                                    print(f"{id_set}. {set_outfit['nama']} ({set_outfit['style']})")
                                    print(f" Baju   : {set_outfit['baju']['jenis']} {set_outfit['baju']['warna']}")
                                    print(f" Celana : {set_outfit['celana']['jenis']} {set_outfit['celana']['warna']}")
                                    print(f" Sepatu : {set_outfit['sepatu']['jenis']} {set_outfit['sepatu']['warna']}")
                                if len(daftar_outfit) == 0:
                                    print("(belum ada outfit)")
                                else:
                                    pilih_outfit = int(input("Pilih nomor outfit: "))

                                    if pilih_outfit not in daftar_outfit:
                                        print("Nomor tidak ada!")
                                    else:
                                        yakin = input("Yakin hapus? (Ya/Tidak): ").lower()
                                        if yakin == "ya":
                                            del daftar_outfit[pilih_outfit]
                                            print("Outfit berhasil dihapus!")
                                        elif yakin == "tidak":
                                            print("Dibatalkan.")
                                        else:
                                            print("Input harus Ya atau Tidak!")
                                input("Tekan Enter...")

                            elif pilih_builder == "0":
                                di_builder = False

                            else:
                                print("Pilihan Tidak Valid!")
                                input("Tekan Enter...")

                    elif pilih_user == "3":
                        di_style = True
                        while di_style:
                            os.system("cls")
                            print("==========================================================")
                            print("                       PILIH STYLE                        ")
                            print("==========================================================")
                            nomor_urut = 0
                            for style in style_default:
                                nomor_urut += 1
                                print(f"{nomor_urut}. {style}")
                            print("0. Kembali")
                            pilih_style = int(input("Pilih style: "))

                            if pilih_style == 0:
                                di_style = False
                            elif pilih_style < 1 or pilih_style > len(style_default):
                                print("Nomor tidak ada!")
                                input("Tekan Enter...")
                            else:
                                style_dipilih = style_default[pilih_style - 1]
                                os.system("cls")
                                print("==========================================================")
                                print("                   OUTFIT STYLE", style_dipilih.upper())
                                print("==========================================================")
                                nomor_urut = 0

                                set_outfit = outfit_default[style_dipilih]
                                nomor_urut += 1
                                print(f"{nomor_urut}. Set Default")
                                print(f" Baju   : {set_outfit['baju']['jenis']} {set_outfit['baju']['warna']}")
                                print(f" Celana : {set_outfit['celana']['jenis']} {set_outfit['celana']['warna']}")
                                print(f" Sepatu : {set_outfit['sepatu']['jenis']} {set_outfit['sepatu']['warna']}")

                                for id_set, set_outfit in outfit[user_login].items():
                                    if set_outfit["style"] == style_dipilih:
                                        nomor_urut += 1
                                        print(f"{nomor_urut}. {set_outfit['nama']} (Buatan Anda)")
                                        print(f" Baju   : {set_outfit['baju']['jenis']} {set_outfit['baju']['warna']}")
                                        print(f" Celana : {set_outfit['celana']['jenis']} {set_outfit['celana']['warna']}")
                                        print(f" Sepatu : {set_outfit['sepatu']['jenis']} {set_outfit['sepatu']['warna']}")
                                input("Tekan Enter...")

                    elif pilih_user == "0":
                        user_login = ""
                        role_login = ""
                        sedang_login = False

                    else:
                        print("Pilihan Tidak Valid!")
                        input("Tekan Enter...")
        else:
            print("Login gagal 3 kali, kembali ke menu awal.")
            input("Tekan Enter...")

    elif pilih == "3":
        print("Terima kasih!")
        jalan = False

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter...")
