print ("PROGRAM MENCARI RATA-RATA")
print ()
n=int(input("Banyaknya banyak data yang ingin di masukkan :"))
print()
data = []
jumlah = 0

for i in range (0,n):
    m=float(input("masukkan angka ke- {0} = ".format (i)))
    data.append(m)
    jumlah += data[i]
    rata2=jumlah/n
    
print ("rata-ratanya adalah = ",rata2)
    
