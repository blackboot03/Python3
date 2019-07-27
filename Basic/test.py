a = 10
b = 100


# penjumlahan
print("Hasil penjumlahan a + b = ", a+b)

# pengurangan
print("Hasil pengurangan a - b = ", a-b)

# perkalian
print("Hasil perkalian a x b = ", a*b)

# pembagian
print("Hasil pembagian a : b = ", a/b)

# sisa hasil
print("Sisa hasil bagi a : b = ", a//b)

Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# menampilkan isi list
print(Data)

# mengakses isi data ke 3
Subdata1 = Data[2]
print(Subdata1)

# menambahkan list baru
Data2 = [100, 200, 300, 400, 500, 600]
Data3 = Data + Data2
Data4 = [Data,Data2]
print(Data3)
print(Data4)

# method list
Data.append(11)
print(Data)
