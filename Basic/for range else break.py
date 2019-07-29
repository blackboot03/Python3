# for i in range

# for i in range(0,10,2):# (0,10,2) 0,10 = range "2"= increment
#     print(i)

number = int(input("Masukkan angka anda : "))
for i in range(1,10):
    if i is number:
        print("Angka anda ditemukan pada loop ke ", i)
        break
    print(i, "Bukan angka anda")
else:
    print("Angka anda tidak ditemukan")

