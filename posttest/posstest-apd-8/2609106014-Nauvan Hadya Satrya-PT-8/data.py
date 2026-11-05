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