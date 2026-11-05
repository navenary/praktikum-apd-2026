import pwinput
import data
from tampilan import bersih, header, jeda, sukses, gagal
from validasi import validasi_username, validasi_password
from admin import menu_admin
from pengguna import menu_user


def register():
    bersih()
    header("REGISTER")
    try:
        username = validasi_username(input("Username: "))
        password = validasi_password(pwinput.pwinput("Password: "))
    except ValueError as error:
        gagal(error)
    else:
        kunci = username.lower()
        data.akun[kunci] = {"username": username, "password": password, "role": "user"}
        data.pakaian[kunci] = {}
        data.outfit[kunci] = {}
        sukses("Register berhasil! Silakan login.")
    jeda()


def login():
    bersih()
    header("LOGIN")
    for percobaan in range(3):
        username = input("Username: ").strip()
        password = pwinput.pwinput("Password: ").strip()
        kunci = username.lower()
        try:
            akun_ada = data.akun[kunci]
        except KeyError:
            gagal(f"Username atau password salah! Sisa percobaan: {2 - percobaan}")
            continue
        if akun_ada["password"] == password:
            data.user_login = kunci
            data.role_login = akun_ada["role"]
            return True
        gagal(f"Username atau password salah! Sisa percobaan: {2 - percobaan}")
    gagal("Login gagal 3 kali, kembali ke menu awal.")
    jeda()
    return False


def sesi_login():
    if data.role_login == "admin":
        menu_admin()
    else:
        menu_user()
    data.user_login = ""
    data.role_login = ""