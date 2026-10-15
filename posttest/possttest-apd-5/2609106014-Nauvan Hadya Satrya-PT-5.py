import os

akun = [["admin", "admin123", "admin"]]

style_default = ("Casual", "Semi Casual", "Semi Formal", "Formal")
baju_default = ("Kemeja", "Polo Shirt", "Kaos")
celana_default = ("Celana Bahan", "Celana Chino", "Celana Jeans")
sepatu_default = ("Loafers", "Sneakers")
warna_default = ("Hitam", "Putih", "Navy", "Abu-abu", "Coklat")

outfit_default = (
    ("Casual", "Kaos", "Putih", "Celana Jeans", "Navy", "Sneakers", "Putih"),
    ("Semi Casual", "Polo Shirt", "Navy", "Celana Jeans", "Hitam", "Sneakers", "Putih"),
    ("Semi Formal", "Kemeja", "Putih", "Celana Chino", "Coklat", "Loafers", "Coklat"),
    ("Formal", "Kemeja", "Putih", "Celana Bahan", "Hitam", "Loafers", "Hitam"),
)

pakaian = []   
outfit = []    

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

        if username == "":
            print("Username tidak boleh kosong!")
        elif " " in username:
            print("Username tidak boleh mengandung spasi!")
        else:
            sudah_ada = False
            for data in akun:
                if data[0].lower() == username.lower():
                    sudah_ada = True

            if sudah_ada:
                print("Username sudah dipakai!")
            else:
                password = input("Masukkan Password Anda: ").strip()
                if password == "":
                    print("Password Tidak Boleh Kosong!")
                elif " " in password:
                    print("Password Tidak Boleh Mengandung Spasi!")
                else:
                    akun.append([username, password, "user"])
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

            for data in akun:
                if data[0] == username and data[1] == password:
                    berhasil = True
                    user_login = data[0]
                    role_login = data[2]

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
                        for data in akun:
                            nomor += 1
                            print(f"{nomor}. Username: {data[0]} : Role: {data[2]}")
                        input("Tekan Enter...")
                        
                    elif pilih_admin == "2":
                        os.system("cls")
                        print("==========================================================")
                        print("                     SEMUA WARDROBE USER                  ")
                        print("==========================================================")
                        nomor = 0
                        for item in pakaian:
                            nomor += 1
                            print(f"{nomor}. User: {item[0]} : {item[1]} ({item[2]})")
                        if nomor == 0:
                            print("(Belum ada data wardrobe)")
                        input("Tekan Enter...")
                        
                    elif pilih_admin == "3":
                        os.system("cls")
                        print("==========================================================")
                        print("                        SEMUA OUTFIT                      ")
                        print("==========================================================")
                        nomor = 0
                        for set_outfit in outfit:
                            nomor += 1
                            print(f"{nomor}. User: {set_outfit[0]} : {set_outfit[8]} ({set_outfit[1]})")
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
                    print("Halo,", user_login)
                    print("1. Kelola Wardrobe (Pakaian & Sepatu)")
                    print("2. Outfit Builder")
                    print("3. Lihat Outfit Berdasarkan Style")
                    print("0. Logout")
                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        di_koleksi = True
                        while di_koleksi:
                            daftar_pakaian = []
                            for item in pakaian:
                                if item[0] == user_login:
                                    daftar_pakaian.append(item)

                            daftar_jenis = list(baju_default) + list(celana_default) + list(sepatu_default)

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
                                        pakaian.append([user_login, jenis_dipilih, warna_dipilih])
                                        print("Item berhasil ditambahkan!")
                                input("Tekan Enter...")

                            elif pilih_koleksi == "2":
                                os.system("cls")
                                print("==========================================================")
                                print("                      WARDROBE ANDA                       ")
                                print("==========================================================")
                                nomor_urut = 0
                                for item in daftar_pakaian:
                                    nomor_urut += 1
                                    print(f"{nomor_urut}. {item[1]} (Warna: {item[2]})")
                                if nomor_urut == 0:
                                    print("(Belum ada item di wardrobe)")
                                input("Tekan Enter...")

                            elif pilih_koleksi == "3":
                                os.system("cls")
                                print("==========================================================")
                                print("                        UBAH ITEM                         ")
                                print("==========================================================")
                                nomor_urut = 0
                                for item in daftar_pakaian:
                                    nomor_urut += 1
                                    print(f"{nomor_urut}. {item[1]} (Warna: {item[2]})")
                                if nomor_urut == 0:
                                    print("(Belum ada item di wardrobe)")
                                else:
                                    pilih_pakaian = int(input("Pilih nomor item: "))

                                    if pilih_pakaian < 1 or pilih_pakaian > len(daftar_pakaian):
                                        print("Nomor tidak ada!")
                                    else:
                                        item = daftar_pakaian[pilih_pakaian - 1]
                                        nomor_urut = 0
                                        for warna in warna_default:
                                            nomor_urut += 1
                                            print(f"{nomor_urut}. {warna}")
                                        pilih_warna = int(input("Pilih warna baru: "))

                                        if pilih_warna < 1 or pilih_warna > len(warna_default):
                                            print("Nomor tidak ada!")
                                        else:
                                            item[2] = warna_default[pilih_warna - 1]
                                            print("Item berhasil diubah!")
                                input("Tekan Enter...")

                            elif pilih_koleksi == "4":
                                os.system("cls")
                                print("==========================================================")
                                print("                        HAPUS ITEM                        ")
                                print("==========================================================")
                                nomor_urut = 0
                                for item in daftar_pakaian:
                                    nomor_urut += 1
                                    print(f"{nomor_urut}. {item[1]} (Warna: {item[2]})")
                                if nomor_urut == 0:
                                    print("(Belum ada item di wardrobe)")
                                else:
                                    pilih_pakaian = int(input("Pilih nomor item: "))

                                    if pilih_pakaian < 1 or pilih_pakaian > len(daftar_pakaian):
                                        print("Nomor tidak ada!")
                                    else:
                                        yakin = input("Yakin hapus? (Ya/Tidak): ").lower()
                                        if yakin == "ya":
                                            pakaian.remove(daftar_pakaian[pilih_pakaian - 1])
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
                            daftar_atasan = []
                            daftar_bawahan = []
                            daftar_sepatu = []
                            for item in pakaian:
                                if item[0] == user_login:
                                    if item[1] in baju_default:
                                        daftar_atasan.append(item)
                                    elif item[1] in celana_default:
                                        daftar_bawahan.append(item)
                                    elif item[1] in sepatu_default:
                                        daftar_sepatu.append(item)

                            daftar_outfit = []
                            for item in outfit:
                                if item[0] == user_login:
                                    daftar_outfit.append(item)

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
                                outfit_lama = []

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
                                        nomor_urut = 0
                                        for set_outfit in daftar_outfit:
                                            nomor_urut += 1
                                            print(f"{nomor_urut}. {set_outfit[8]} ({set_outfit[1]})")
                                        pilih_outfit = int(input("Pilih nomor outfit yang diubah: "))
                                        if pilih_outfit < 1 or pilih_outfit > len(daftar_outfit):
                                            print("Nomor tidak ada!")
                                            lanjut = False
                                        else:
                                            outfit_lama = daftar_outfit[pilih_outfit - 1]

                                if lanjut:
                                    nama_outfit = input("Nama outfit: ").strip()
                                    if nama_outfit == "":
                                        print("Nama outfit tidak boleh kosong!")
                                        lanjut = False

                                if lanjut:
                                    print("Pilih Atasan:")
                                    nomor_urut = 0
                                    for item in daftar_atasan:
                                        nomor_urut += 1
                                        print(f"{nomor_urut}. {item[1]} {item[2]}")
                                    pilih_atasan = int(input("Pilih atasan: "))
                                    if pilih_atasan < 1 or pilih_atasan > len(daftar_atasan):
                                        print("Nomor tidak ada!")
                                        lanjut = False

                                if lanjut:
                                    print("Pilih Bawahan:")
                                    nomor_urut = 0
                                    for item in daftar_bawahan:
                                        nomor_urut += 1
                                        print(f"{nomor_urut}. {item[1]} {item[2]}")
                                    pilih_bawahan = int(input("Pilih bawahan: "))
                                    if pilih_bawahan < 1 or pilih_bawahan > len(daftar_bawahan):
                                        print("Nomor tidak ada!")
                                        lanjut = False

                                if lanjut:
                                    print("Pilih Sepatu:")
                                    nomor_urut = 0
                                    for item in daftar_sepatu:
                                        nomor_urut += 1
                                        print(f"{nomor_urut}. {item[1]} {item[2]}")
                                    pilih_sepatu = int(input("Pilih sepatu: "))
                                    if pilih_sepatu < 1 or pilih_sepatu > len(daftar_sepatu):
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
                                    atasan = daftar_atasan[pilih_atasan - 1]
                                    bawahan = daftar_bawahan[pilih_bawahan - 1]
                                    sepatu = daftar_sepatu[pilih_sepatu - 1]
                                    style_dipilih = style_default[pilih_style - 1]

                                    print("\nKombinasi outfit:")
                                    print(f"Nama   : {nama_outfit}")
                                    print(f"Style  : {style_dipilih}")
                                    print(f"Baju   : {atasan[1]} {atasan[2]}")
                                    print(f"Celana : {bawahan[1]} {bawahan[2]}")
                                    print(f"Sepatu : {sepatu[1]} {sepatu[2]}")
                                    simpan = input("Simpan outfit? (Ya/Tidak): ").lower()

                                    if simpan == "ya":
                                        if pilih_builder == "3":
                                            outfit.remove(outfit_lama)
                                        outfit.append([user_login, style_dipilih, atasan[1], atasan[2], bawahan[1], bawahan[2], sepatu[1], sepatu[2], nama_outfit])
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
                                nomor_urut = 0
                                for set_outfit in daftar_outfit:
                                    nomor_urut += 1
                                    print(f"{nomor_urut}. {set_outfit[8]} ({set_outfit[1]})")
                                    print(f"   Baju   : {set_outfit[2]} {set_outfit[3]}")
                                    print(f"   Celana : {set_outfit[4]} {set_outfit[5]}")
                                    print(f"   Sepatu : {set_outfit[6]} {set_outfit[7]}")
                                if nomor_urut == 0:
                                    print("(belum ada outfit)")
                                input("Tekan Enter...")

                            elif pilih_builder == "4":
                                os.system("cls")
                                print("==========================================================")
                                print("                       HAPUS OUTFIT                       ")
                                print("==========================================================")
                                nomor_urut = 0
                                for set_outfit in daftar_outfit:
                                    nomor_urut += 1
                                    print(f"{nomor_urut}. {set_outfit[8]} ({set_outfit[1]})")
                                    print(f"   Baju   : {set_outfit[2]} {set_outfit[3]}")
                                    print(f"   Celana : {set_outfit[4]} {set_outfit[5]}")
                                    print(f"   Sepatu : {set_outfit[6]} {set_outfit[7]}")
                                if nomor_urut == 0:
                                    print("(belum ada outfit)")
                                else:
                                    pilih_outfit = int(input("Pilih nomor outfit: "))

                                    if pilih_outfit < 1 or pilih_outfit > len(daftar_outfit):
                                        print("Nomor tidak ada!")
                                    else:
                                        yakin = input("Yakin hapus? (Ya/Tidak): ").lower()
                                        if yakin == "ya":
                                            outfit.remove(daftar_outfit[pilih_outfit - 1])
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
                                for set_outfit in outfit_default:
                                    if set_outfit[0] == style_dipilih:
                                        nomor_urut += 1
                                        print(f"{nomor_urut}. Set Default")
                                        print(f"   Baju   : {set_outfit[1]} {set_outfit[2]}")
                                        print(f"   Celana : {set_outfit[3]} {set_outfit[4]}")
                                        print(f"   Sepatu : {set_outfit[5]} {set_outfit[6]}")
                                for set_outfit in outfit:
                                    if set_outfit[0] == user_login and set_outfit[1] == style_dipilih:
                                        nomor_urut += 1
                                        print(f"{nomor_urut}. {set_outfit[8]} (Buatan Anda)")
                                        print(f"   Baju   : {set_outfit[2]} {set_outfit[3]}")
                                        print(f"   Celana : {set_outfit[4]} {set_outfit[5]}")
                                        print(f"   Sepatu : {set_outfit[6]} {set_outfit[7]}")
                                if nomor_urut == 0:
                                    print("(belum ada outfit)")
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