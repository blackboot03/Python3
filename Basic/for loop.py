# list sebagai iterable
# nama_murid = ["bagas", "calvin", "aleya", "ezra", "runa", "gege"]
#
# for i in nama_murid:
#     print(i)
#     print(len(i))
#     for g in i:
#         print(g)

# string sebagai iterable

# nama = "yoyok"
# for i in nama:
#     print(i)
#
nama_murid = ["bagas", "calvin", "aleya", "ezra", "runa", "gege"]
nama_guru = ["Ahmad", "Budi", "Bagus"]
nama_kelas = ["IPA", "IPS", "Bahasa"]

KomponenSekolah = [nama_murid, nama_guru, nama_kelas]

for subSekolah in KomponenSekolah:
    print(subSekolah)
    for detail in subSekolah:
        print(detail)
        for spell in detail:
            print(spell)

