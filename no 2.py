while True:    
    print("selamat datang")
    print("silahkan pilih menu dibawah ini")
    print("1. Mencari Luas dan keliling Segitiga")
    print("2. Mencari Luas dan keliling persegi panjang")
    print("3. Keluar")
    a = int(input("masukkan angka = "))
    if a == 3:
        print ("terima kasih")
        pass
    else:
        if a == 1:
            while True:    
                print("Selamat datang di menu mencari luas dan keliling segitiga")
                sisi = float(input("silahkan masukkan sisi segitiganya : "))
                luas = sisi*sisi
                keliling = sisi+sisi+sisi+sisi
                print ("luas segitiganya adalah = ",luas)
                print ("keliling segitiganya adalah = ",keliling)
                break
        else:
            if a == 2:
                while True:  
                    print("Selamat datang di menu mencari luas dan keliling persegi panjang")
                    p = float(input("silahkan masukkan panjangnya : "))
                    l = float(input("silahkan masukkan lebarnya : "))
                    luas = p*l
                    keliling = p+l+p+l
                    print ("luas persegi panjangnya adalah = ",luas)
                    print ("keliling persegi panjangya adalah = ",keliling)
                    break
            else:
                print("angka yang anda masukkan tidak ada dalam menu")

