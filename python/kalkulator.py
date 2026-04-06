print ("kalkulator sederhana")

print("1.penjumlahan")
print("2.pengurangan")
print("3.perkalian")
print("4.pembagian")
print("5.modulus")

pilihan = int(input("input pilihan operasi:"))
num1 = int(input('angka pertama:'))
num2 = int(input('angka kedua:'))
print()

if pilihan == 1:
    print('hasil dari',num1,'+',num2,'=',round(num1+num2,2))
elif pilihan == 2 :
    print('hasil dari',num1,'-',num2,'=',round(num1-num2,2))
elif pilihan == 3 :
    print('hasil dari',num1,'*',num2,'=',round(num1*num2,2))
elif pilihan == 4 :
    print('hasil dari',num1,'/',num2,'=',round(num1/num2,2))
elif pilihan == 5 :
    print('hasil dari',num1,'%',num2,'=',round(num1%num2,2))
else :
    print('maaf,pilihan menu tidak tersedia')