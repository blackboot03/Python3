import time
number = int(input("Masukkan angka anda : "))
for i in range(1,10):
    if i is number:
        print("Angka anda ditemukan pada looping ke ", i)
        break # fungsinya untuk mengakhiri
        #continue
        #pass = digunakan untuk dummy looping atau dummy if
    print(i, "Bukan angka anda")
    time.sleep(1)
else:
    print("Angka anda tidak ditemukan, total loop =",number)