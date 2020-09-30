print ("mencari nilai maksimal dan minimal")
print ()
n=int(input("masukkan banyak data yang ingin dimasukkan : "))
data = []

for i in range (0,n):
    m=int(input("masukkan angka ke-{0} = ".format (i)))
    data.append(m)

print ("nilai maksimalnya adalah = ",max(data))
print ("nilai minimalnya adalah = ",min(data))
