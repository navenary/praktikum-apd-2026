import os

akun = {
    "admin": {"username": "admin", "password": "admin123", "role": "admin"}
}
pakaian = {}
outfit = {}
id_pakaian = 1
id_outfit = 1
user_login = ""
role_login = ""

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


def jeda():
    input("Tekan Enter...")


def tampil_pilihan(daftar):
    nomor = 0
    for nama in daftar:
        nomor += 1
        print(f"{nomor}. {nama}")


def tampil_item(daftar_item):
    nomor = 0
    for id_item, item in daftar_item.items():
        nomor += 1
        print(f"{nomor}. {item['jenis']} (Warna: {item['warna']})")
    if len(daftar_item) == 0:
        print("(Belum ada item di wardrobe)")


def tampil_detail_set(set_outfit):
    print(f" Baju   : {set_outfit['baju']['jenis']} {set_outfit['baju']['warna']}")
    print(f" Celana : {set_outfit['celana']['jenis']} {set_outfit['celana']['warna']}")
    print(f" Sepatu : {set_outfit['sepatu']['jenis']} {set_outfit['sepatu']['warna']}")


def tampil_outfit(daftar_outfit):
    nomor = 0
    for id_set, set_outfit in daftar_outfit.items():
        nomor += 1
        print(f"{nomor}. {set_outfit['nama']} ({set_outfit['style']})")
        tampil_detail_set(set_outfit)
    if len(daftar_outfit) == 0:
        print("(Belum ada outfit)")


def buat_id_pakaian():
    global id_pakaian
    id_baru = id_pakaian
    id_pakaian += 1
    return id_baru


def buat_id_outfit():
    global id_outfit
    id_baru = id_outfit
    id_outfit += 1
    return id_baru


def input_ya_tidak():
    jawab = input("Pilih (Ya/Tidak): ").strip().lower()
    if jawab == "ya":
        return True
    if jawab == "tidak":
        return False
    print("Input harus Ya atau Tidak!")
    return input_ya_tidak()


def kumpulkan_wardrobe():
    atasan = {}
    bawahan = {}
    sepatu = {}
    for id_item, item in pakaian[user_login].items():
        if item["jenis"] in baju_default:
            atasan[id_item] = item
        elif item["jenis"] in celana_default:
            bawahan[id_item] = item
        elif item["jenis"] in sepatu_default:
            sepatu[id_item] = item
    return {"atasan": atasan, "bawahan": bawahan, "sepatu": sepatu}


def input_angka(pesan):
    try:
        angka = int(input(pesan))
    except ValueError:
        print("Input harus berupa angka!")
        return input_angka(pesan)
    else:
        return angka


def validasi_username(username):
    username = username.strip()
    if username == "":
        raise ValueError("Username tidak boleh kosong!")
    if " " in username:
        raise ValueError("Username tidak boleh mengandung spasi!")
    if username.lower() in akun:
        raise ValueError("Username sudah dipakai!")
    return username


def validasi_password(password):
    password = password.strip()
    if password == "":
        raise ValueError("Password tidak boleh kosong!")
    if " " in password:
        raise ValueError("Password tidak boleh mengandung spasi!")
    return password


def pilih_nomor(daftar, pesan):
    tampil_pilihan(daftar)
    nomor = input_angka(pesan)
    if nomor < 1 or nomor > len(daftar):
        raise ValueError("Nomor tidak ada!")
    return daftar[nomor - 1]


def pilih_id(daftar, pesan):
    nomor = input_angka(pesan)
    if nomor < 1 or nomor > len(daftar):
        raise ValueError("Nomor tidak ada!")
    urutan = 0
    for id_item in daftar:
        urutan += 1
        if urutan == nomor:
            return id_item


def register():
    os.system("cls")
    print("==========================================================")
    print("                         REGISTER                         ")
    print("==========================================================")
    try:
        username = validasi_username(input("Username: "))
        password = validasi_password(input("Password: "))
    except ValueError as error:
        print(error)
    else:
        kunci = username.lower()
        akun[kunci] = {"username": username, "password": password, "role": "user"}
        pakaian[kunci] = {}
        outfit[kunci] = {}
        print("Register berhasil! Silakan login.")
    jeda()


def login():
    global user_login, role_login
    os.system("cls")
    print("==========================================================")
    print("                          LOGIN                           ")
    print("==========================================================")
    for percobaan in range(3):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        kunci = username.lower()
        try:
            data = akun[kunci]
        except KeyError:
            print("Username atau password salah! Sisa percobaan:", 2 - percobaan)
            continue
        if data["password"] == password:
            user_login = kunci
            role_login = data["role"]
            return True
        print("Username atau password salah! Sisa percobaan:", 2 - percobaan)
    print("Login gagal 3 kali, kembali ke menu awal.")
    jeda()
    return False


def lihat_akun():
    os.system("cls")
    print("==========================================================")
    print("                  DAFTAR AKUN TERDAFTAR                   ")
    print("==========================================================")
    nomor = 0
    for kunci, data in akun.items():
        nomor += 1
        print(f"{nomor}. Username: {data['username']} : Role: {data['role']}")
    jeda()


def lihat_semua_wardrobe():
    os.system("cls")
    print("==========================================================")
    print("                   SEMUA WARDROBE USER                    ")
    print("==========================================================")
    nomor = 0
    for pemilik, daftar in pakaian.items():
        for item in daftar.values():
            nomor += 1
            print(f"{nomor}. User: {akun[pemilik]['username']} : {item['jenis']} ({item['warna']})")
    if nomor == 0:
        print("(Belum ada data wardrobe)")
    jeda()


def lihat_semua_outfit():
    os.system("cls")
    print("==========================================================")
    print("                       SEMUA OUTFIT                       ")
    print("==========================================================")
    nomor = 0
    for pemilik, daftar in outfit.items():
        for set_outfit in daftar.values():
            nomor += 1
            print(f"{nomor}. User: {akun[pemilik]['username']} : {set_outfit['nama']} ({set_outfit['style']})")
    if nomor == 0:
        print("(Belum ada data outfit)")
    jeda()


def menu_admin():
    aktif = True
    while aktif:
        os.system("cls")
        print("==========================================================")
        print("                        MENU ADMIN                        ")
        print("==========================================================")
        print("1. Lihat Daftar Akun")
        print("2. Lihat Semua Wardrobe User")
        print("3. Lihat Semua Outfit User")
        print("0. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            lihat_akun()
        elif pilih == "2":
            lihat_semua_wardrobe()
        elif pilih == "3":
            lihat_semua_outfit()
        elif pilih == "0":
            aktif = False
        else:
            print("Pilihan tidak valid!")
            jeda()


def tambah_item():
    os.system("cls")
    print("==========================================================")
    print("                       TAMBAH ITEM                        ")
    print("==========================================================")
    daftar_jenis = baju_default + celana_default + sepatu_default
    try:
        jenis = pilih_nomor(daftar_jenis, "Pilih jenis: ")
        warna = pilih_nomor(warna_default, "Pilih warna: ")
    except ValueError as error:
        print(error)
    else:
        pakaian[user_login][buat_id_pakaian()] = {"jenis": jenis, "warna": warna}
        print("Item berhasil ditambahkan!")
    jeda()


def lihat_wardrobe():
    os.system("cls")
    print("==========================================================")
    print("                      WARDROBE ANDA                       ")
    print("==========================================================")
    tampil_item(pakaian[user_login])
    jeda()


def ubah_item():
    os.system("cls")
    print("==========================================================")
    print("                        UBAH ITEM                         ")
    print("==========================================================")
    daftar_pakaian = pakaian[user_login]
    tampil_item(daftar_pakaian)
    if len(daftar_pakaian) > 0:
        try:
            id_item = pilih_id(daftar_pakaian, "Pilih nomor item: ")
            warna = pilih_nomor(warna_default, "Pilih warna baru: ")
        except ValueError as error:
            print(error)
        else:
            daftar_pakaian[id_item]["warna"] = warna
            print("Item berhasil diubah!")
    jeda()


def hapus_item():
    os.system("cls")
    print("==========================================================")
    print("                        HAPUS ITEM                        ")
    print("==========================================================")
    daftar_pakaian = pakaian[user_login]
    tampil_item(daftar_pakaian)
    if len(daftar_pakaian) > 0:
        try:
            id_item = pilih_id(daftar_pakaian, "Pilih nomor item: ")
        except ValueError as error:
            print(error)
        else:
            print("Yakin hapus?")
            if input_ya_tidak():
                del daftar_pakaian[id_item]
                print("Item berhasil dihapus!")
            else:
                print("Dibatalkan.")
    jeda()


def kelola_wardrobe():
    aktif = True
    while aktif:
        os.system("cls")
        print("==========================================================")
        print("                     KELOLA WARDROBE                      ")
        print("==========================================================")
        print("1. Tambah Item")
        print("2. Lihat Wardrobe")
        print("3. Ubah Item")
        print("4. Hapus Item")
        print("0. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_item()
        elif pilih == "2":
            lihat_wardrobe()
        elif pilih == "3":
            ubah_item()
        elif pilih == "4":
            hapus_item()
        elif pilih == "0":
            aktif = False
        else:
            print("Pilihan Tidak Valid!")
            jeda()


def simpan_outfit(pilih_builder):
    if pilih_builder == "1":
        os.system("cls")
        print("==========================================================")
        print("                       BUAT OUTFIT                        ")
        print("==========================================================")
    else:
        os.system("cls")
        print("==========================================================")
        print("                       UBAH OUTFIT                        ")
        print("==========================================================")
    wardrobe = kumpulkan_wardrobe()
    atasan = wardrobe["atasan"]
    bawahan = wardrobe["bawahan"]
    sepatu = wardrobe["sepatu"]

    if len(atasan) == 0 or len(bawahan) == 0 or len(sepatu) == 0:
        print("Wardrobe belum lengkap!")
        print("Minimal punya 1 baju, 1 celana, dan 1 sepatu.")
        print("Tambahkan dulu di menu Kelola Wardrobe.")
        jeda()
        return

    daftar_outfit = outfit[user_login]
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

        print("Pilih Atasan:")
        tampil_item(atasan)
        id_atasan = pilih_id(atasan, "Pilih atasan: ")

        print("Pilih Bawahan:")
        tampil_item(bawahan)
        id_bawahan = pilih_id(bawahan, "Pilih bawahan: ")

        print("Pilih Sepatu:")
        tampil_item(sepatu)
        id_sepatu = pilih_id(sepatu, "Pilih sepatu: ")

        print("Pilih Style Outfit:")
        style_dipilih = pilih_nomor(style_default, "Pilih style: ")
    except ValueError as error:
        print(error)
        jeda()
        return

    data_outfit = {
        "nama": nama_outfit,
        "style": style_dipilih,
        "baju": atasan[id_atasan].copy(),
        "celana": bawahan[id_bawahan].copy(),
        "sepatu": sepatu[id_sepatu].copy(),
    }

    print("Kombinasi outfit:")
    print(f"Nama   : {nama_outfit}")
    print(f"Style  : {style_dipilih}")
    tampil_detail_set(data_outfit)
    print("Simpan outfit?")

    if input_ya_tidak():
        if pilih_builder == "3":
            daftar_outfit[id_ubah] = data_outfit
        else:
            daftar_outfit[buat_id_outfit()] = data_outfit
        print("Outfit berhasil disimpan!")
    else:
        print("Dibatalkan.")
    jeda()


def lihat_outfit():
    os.system("cls")
    print("==========================================================")
    print("                       OUTFIT SAYA                        ")
    print("==========================================================")
    tampil_outfit(outfit[user_login])
    jeda()


def hapus_outfit():
    os.system("cls")
    print("==========================================================")
    print("                       HAPUS OUTFIT                       ")
    print("==========================================================")
    daftar_outfit = outfit[user_login]
    tampil_outfit(daftar_outfit)
    if len(daftar_outfit) > 0:
        try:
            id_set = pilih_id(daftar_outfit, "Pilih nomor outfit: ")
        except ValueError as error:
            print(error)
        else:
            print("Yakin hapus?")
            if input_ya_tidak():
                del daftar_outfit[id_set]
                print("Outfit berhasil dihapus!")
            else:
                print("Dibatalkan.")
    jeda()


def outfit_builder():
    aktif = True
    while aktif:
        os.system("cls")
        print("==========================================================")
        print("                      OUTFIT BUILDER                      ")
        print("==========================================================")
        print("1. Buat Outfit")
        print("2. Lihat Outfit Saya")
        print("3. Ubah Outfit")
        print("4. Hapus Outfit")
        print("0. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            simpan_outfit("1")
        elif pilih == "2":
            lihat_outfit()
        elif pilih == "3":
            simpan_outfit("3")
        elif pilih == "4":
            hapus_outfit()
        elif pilih == "0":
            aktif = False
        else:
            print("Pilihan Tidak Valid!")
            jeda()


def lihat_outfit_style():
    aktif = True
    while aktif:
        os.system("cls")
        print("==========================================================")
        print("                       PILIH STYLE                        ")
        print("==========================================================")
        tampil_pilihan(style_default)
        print("0. Kembali")
        pilih = input_angka("Pilih style: ")

        if pilih == 0:
            aktif = False
        elif pilih < 1 or pilih > len(style_default):
            print("Nomor tidak ada!")
            jeda()
        else:
            style_dipilih = style_default[pilih - 1]
            os.system("cls")
            print("==========================================================")
            print(f"                   OUTFIT STYLE {style_dipilih.upper()}")
            print("==========================================================")
            nomor_urut = 1
            print(f"{nomor_urut}. Set Default")
            tampil_detail_set(outfit_default[style_dipilih])

            for set_outfit in outfit[user_login].values():
                if set_outfit["style"] == style_dipilih:
                    nomor_urut += 1
                    print(f"{nomor_urut}. {set_outfit['nama']} (Buatan Anda)")
                    tampil_detail_set(set_outfit)
            jeda()


def menu_user():
    aktif = True
    while aktif:
        os.system("cls")
        print("==========================================================")
        print("                      MENU PENGGUNA                       ")
        print("==========================================================")
        print("Halo,", akun[user_login]["username"])
        print("1. Kelola Wardrobe (Pakaian & Sepatu)")
        print("2. Outfit Builder")
        print("3. Lihat Outfit Berdasarkan Style")
        print("0. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            kelola_wardrobe()
        elif pilih == "2":
            outfit_builder()
        elif pilih == "3":
            lihat_outfit_style()
        elif pilih == "0":
            aktif = False
        else:
            print("Pilihan Tidak Valid!")
            jeda()


def sesi_login():
    global user_login, role_login
    if role_login == "admin":
        menu_admin()
    else:
        menu_user()
    user_login = ""
    role_login = ""


def main():
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
            register()
        elif pilih == "2":
            if login():
                sesi_login()
        elif pilih == "3":
            print("Terima kasih!")
            jalan = False
        else:
            print("Pilihan tidak valid!")
            jeda()


if __name__ == "__main__":
    main()