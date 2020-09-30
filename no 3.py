print ("program menghitung index massa tubuh (BMI)")
print()
a=float(input("masukkan berat badan anda : "))
b=float(input("masukkan tinggi badan anda : "))
BMI = a/(b*b)
print ("BMI anda : ",BMI)
if BMI < 18.5:
    print ("berat badan anda kurang")
elif BMI < 22.9:
    print ("berat badan anda normal")
elif BMI < 29.9:
    print ("berat badan anda berlebih dan cenderung obesitas")
elif BMI > 30:
    print ("anda obesitas")
        
