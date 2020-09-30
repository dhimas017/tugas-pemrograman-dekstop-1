user="dhimas"
pw="190411100017"

def login(namauser,pasword):
    if namauser == user and pasword == pw:
        hasil = True
    else:
        hasil = False

    return hasil
n=3
while n >=1:
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    hasil = (login(username,password))
    if hasil == True:
        print("Anda berhasil masuk")
        break
    else:
        n-=1
        print("Username atau Password anda Salah")
