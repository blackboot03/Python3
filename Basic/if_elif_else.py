# nilai = 60
#
#
# if nilai == 60: # equal explisit
#     print("Nilai anda adalah :",nilai)
#
# if nilai is 75: # equal
#     print("Nilai anda adalah: ",nilai)
#
# if nilai is not 60: #not equal
#     print("Nilai anda salah")
#
# print(50*"=")
# print("PENGGUNAAN ELIF")
# print(" ")
#
# nilai = 101
#
# if 80 <= nilai <= 100:
#     print("Nilai matakuliah anda A")
# elif 70 <= nilai < 80:
#     print("Nilai mata kuliah anda B")
# elif 60 <= nilai < 70:
#     print("Nilai mata kuliah anda C")
# elif 50 <= nilai < 60:
#     print("Nilai mata kuliah anda T, anda harus mengulang")
# else:
#     print("Anda tidak lulus mata kuliah ini, nilai anda adalah: ",nilai)
#
# print(80*"+")
# print(" ")
# print("OPERATOR LOGIKA UNTUK STRING dan LIST")
# print(38*"-")
# print(" ")

nama_murid = ["andi", "totok", "marto", "bagus", "rahmat"]
absen = input("Masukkan nama murid : ")

if absen in nama_murid:
    print(absen,"masuk hari ini")
if absen not in nama_murid:
    print(absen,"tidak masuk hari ini")

karakter = "g"
if karakter in absen:
    print("Ada huruf" ,karakter, "di nama murid")
else:
    print("Tidak ada huruf" ,karakter, "di nama murid")