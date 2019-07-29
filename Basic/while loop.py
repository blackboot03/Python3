# angka = 0
#
# while angka < 10:
#     angka = angka + 1
#     if angka % 2 != 0:
#         print(angka,"adalah bilangan ganjil")
#
# else:
#     print("Total data loop = ",angka)
#
# print(" ")
# print(30*"=")
# print(" ")
#
# # while menggunakan boolean
#
import time

start = True
angka = int(input("Angka dimulai dari :"))

while start:
    print("Anda berada di angka : ",angka)
    time.sleep(1)
    if angka is 10:
        start = False
        print("Angka terakhir looping adalah : ", angka)
    angka += 1
else:
    print("Total looping : ", angka)


