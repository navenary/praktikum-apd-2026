username_benar = "Nauvan"
password_benar = "014"
pin_benar = password_benar + password_benar
saldo = 5000000

percobaan = 0
login_berhasil = False

print("========================================")
print("              BANK DIGITAL              ")
print("========================================")
print()
while percobaan < 3:
    username = input ("Masukkan Username Anda:")
    password = input ("Masukkan Password Anda:")

    if username == username_benar and password == password_benar:
        login_berhasil = True
        print("============ LOGIN BERHASIL ============")
        print("         Selamat Datang,", username      )
        print("      Silahkan Pilih Menu Di Bawah"      )
        print("========================================")
        break

    elif username != username_benar and password != password_benar:
        percobaan += 1
        print("============== PERINGATAN ==============")
        print("    Username Dan Password Anda Salah    ")
        print("          Sisa Kesempatan :", 3 - percobaan)
        print("========================================")
    elif username != username_benar:
        percobaan += 1
        print("============== PERINGATAN ==============")
        print("          Username Anda Salah           ")
        print("          Sisa Kesempatan :", 3 - percobaan)
        print("========================================")
    else:
        percobaan += 1
        print("============== PERINGATAN ==============")
        print("          Password Anda Salah           ")
        print("          Sisa Kesempatan :", 3 - percobaan)
        print("========================================")

if not login_berhasil:
    print("============ AKUN DIBLOKIR =============")
    print("        Anda Gagal Login 3 Kali         ")
    print("========================================")

if login_berhasil:
    menu_aktif = True

    while menu_aktif:
        print()
        print("============== MENU UTAMA ==============")
        print("            1. Transfer Uang"            )
        print("            2. Logout"                   )
        print("========================================")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            while True:
                print("============ TRANSFER UANG =============")
                print("       Saldo Anda : Rp.", saldo          )
                print("========================================")

                if saldo < 50000:
                    print ("============== PERINGATAN ==============")
                    print ("    Saldo Tidak Cukup Untuk Transfer    ")
                    print ("========================================")
                    break
                else:
                    penerima = input("Masukkan Username Penerima:")

                    while True:
                        nominal = int(input("Masukkan Nominal Transfer:"))

                        if nominal < 50000:
                            print("============== PERINGATAN ==============")
                            print("       Nominal Minimal Rp. 50.000       ")
                            print("========================================")
                            continue
                        elif nominal > 1000000:
                            print("============== PERINGATAN ==============")
                            print("     Nominal Maksimal Rp. 1.000.000     ")
                            print("========================================")
                            continue
                        elif nominal > saldo:
                            print("============== PERINGATAN ==============")
                            print("       Saldo Anda Tidak Mencukupi       ")
                            print("========================================")
                            continue
                        break

                    kesempatan_pin = 0
                    pin_valid = False
                    while kesempatan_pin < 3:
                        pin = input("Masukkan PIN:")

                        if pin == pin_benar:
                            pin_valid = True
                            break
                        else:
                            kesempatan_pin += 1
                            print("============== PERINGATAN ==============")
                            print("             PIN Anda Salah             ")
                            print("          Sisa Kesempatan :", 3 - kesempatan_pin)
                            print("========================================")

                    if not pin_valid:
                        print("============ AKUN DIBLOKIR =============")
                        print("            PIN Salah 3 Kali            ")
                        print("========================================")
                        menu_aktif = False
                        break
                    else:
                        saldo -= nominal
                        print()
                        print("============ STRUK TRANSFER ============")
                        print("  Pengirim    :", username_benar)
                        print("  Penerima    :", penerima)
                        print("  Nominal     : Rp.", nominal)
                        print("  Sisa Saldo  : Rp.", saldo)
                        print("           Transfer Berhasil            ")
                        print("========================================")
                        lanjut = input("Apakah Anda ingin melakukan transfer lagi (y/n)? ")
                        if lanjut == "y":
                            continue
                        else:
                            break

        elif pilihan == "2":
            print("=========== LOGOUT BERHASIL ============")
            print("             Terima Kasih               ")
            print("========================================")
            break
        else:
            print("============== PERINGATAN ==============")
            print("          Pilihan Tidak Valid           ")
            print("        Silahkan Pilih 1 Atau 2         ")
            print("========================================")
            continue