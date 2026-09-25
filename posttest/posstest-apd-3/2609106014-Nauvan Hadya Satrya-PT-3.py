print("==========================================================")
print("                          BIOSKOP                         ")
print("==========================================================")
print("Rules & Harga Tiket")
print("Umur Dibawah 13 Tahun Dilarang Menonton")
print("Reguler : Rp. 50.000")
print("Premium : Rp. 75.000")
print("VIP     : Rp. 100.000")
print("Member Mendapat Diskon 20%")
print("==========================================================")
print("                 SILAHKAN ISI DATA ANDA                   ")
print("==========================================================")

print()

nama = input("Masukkan Nama Pembeli:")
umur = int(input("Masukkan Umur Pembeli:"))
if umur < 13:
    print("==========================================================")
    print("                        PERINGATAN                        ")
    print("==========================================================")
    print("      Mohon Maaf Anda Belum Cukup Umur Untuk Menonton     ")
    print("==========================================================")
else: 
    jenis_tiket = input("Pilih Jenis Tiket Anda (Reguler/Premium/VIP):").lower()
    if jenis_tiket != "reguler" and jenis_tiket != "premium" and jenis_tiket != "vip":
        print("==========================================================")
        print("                        PERINGATAN                        ")
        print("==========================================================")
        print("                  Jenis Tiket Tidak Valid                 ")
        print("             Silahkan Pilih Tiket Yang Sesuai             ")
        print("==========================================================")
    else:
        status_member = input("Apakah Anda Member (Ya/Tidak):").lower()
        uang_bayar = int(input("Masukkan Uang Pembayaran:"))
        
        print()

        if jenis_tiket == "reguler":
            harga = 50000
        elif jenis_tiket == "premium":
            harga = 75000
        elif jenis_tiket == "vip":
            harga = 100000

        diskon = 20/100 if status_member == "ya" else 0 
        biaya_admin = 0 if status_member == "ya" else 2000

        nominal_diskon = int(harga * diskon)
        total_bayar = harga - nominal_diskon + biaya_admin

        if uang_bayar < total_bayar:
             print("==========================================================")
             print("                        PERINGATAN                        ")
             print("==========================================================")
             print("                Uang Pembayaran Anda Kurang               ")
             print("                Total Bayar : Rp.",total_bayar)
             print("                Uang Anda   : Rp.",uang_bayar)
             print("                Kekurangan  : Rp.",total_bayar - uang_bayar)
             print("                Transaksi Anda Dibatalkan                 ")
             print("==========================================================")
        else:
            kembalian = uang_bayar - total_bayar

            print("==========================================================")
            print("                     STRUK PEMBAYARAN                     ")
            print("==========================================================")
            print("Nama            :",nama.capitalize())
            print("Umur            :",umur, "Tahun")
            print("Jenis Tiket     :",jenis_tiket.capitalize())
            print("Status Member   :",status_member.capitalize())
            if status_member == "ya":
                print("Harga Awal      : Rp.",harga)
                print("Diskon 20%      : Rp.",nominal_diskon)
                print("Harga Diskon    : Rp.",harga - nominal_diskon)
            else:
                print("Harga Tiket     : Rp.",harga)
                print("Biaya Admin     : Rp.",biaya_admin)
            print("Total Bayar     : Rp.",total_bayar)
            print("Kembalian       : Rp.",kembalian)
            print("==========================================================")
            print("               TERIMA KASIH SELAMAT MENONTON              ")
            print("==========================================================")
            