import data
from tampilan import tampil_pilihan, gagal


def input_ya_tidak():
    jawab = input("Pilih (Ya/Tidak): ").strip().lower()
    if jawab == "ya":
        return True
    if jawab == "tidak":
        return False
    gagal("Input harus Ya atau Tidak!")
    return input_ya_tidak()


def input_angka(pesan):
    try:
        angka = int(input(pesan))
    except ValueError:
        gagal("Input harus berupa angka!")
        return input_angka(pesan)
    else:
        return angka


def validasi_username(username):
    username = username.strip()
    if username == "":
        raise ValueError("Username tidak boleh kosong!")
    if " " in username:
        raise ValueError("Username tidak boleh mengandung spasi!")
    if username.lower() in data.akun:
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