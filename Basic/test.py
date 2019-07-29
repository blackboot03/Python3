# a = 10
# b = 100
#
#
# # penjumlahan
# print("Hasil penjumlahan a + b = ", a+b)
#
# # pengurangan
# print("Hasil pengurangan a - b = ", a-b)
#
# # perkalian
# print("Hasil perkalian a x b = ", a*b)
#
# # pembagian
# print("Hasil pembagian a : b = ", a/b)
#
# # sisa hasil
# print("Sisa hasil bagi a : b = ", a//b)
#
# Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # menampilkan isi list
# print(Data)
#
# # mengakses isi data ke 3
# Subdata1 = Data[2]
# print(Subdata1)
#
# # menambahkan list baru
# Data2 = [100, 200, 300, 400, 500, 600]
# Data3 = Data + Data2
# Data4 = [Data,Data2]
# print(Data3)
# print(Data4)
#
# # method list
# Data.append(11)
# print(Data)
#
# for i in range(0,10):
#     if i % 2 != 0:
#         print(i)

# menampilkan bilangan prima

# for i in range(1,10):
#     if i % 2 is not 0:
#         print(i)
# angka = int(input("masukkan angka :"))
#
# if angka % 2 is 0:
#     print(angka,"adalah bilangan genap")
# else:
#     print(angka,"adalah bilangan ganjil")
#

pilihan = 'y'
while(pilihan != 'n'):
    angka = int(input("masukkan angka :"))
    print(angka)
    if angka % 2 is 0:
        print("angka genap")
    else:
        print("angka ganjil")
    #pilihan = input('ulangi lagi :')
    print(input("ulangi lagi "),end='')


