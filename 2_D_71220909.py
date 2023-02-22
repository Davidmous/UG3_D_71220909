plat = input("Masukan plat nomor >>> ").lower().split()
try : 
    DA = int(plat[1])
    if DA >= 0 and DA <= 3000 : 
        print("Plat nomor tersebut diperuntukan untuk mobil")
    elif DA >= 3001 and DA <= 4000 :
        print("Plat nomor tersebut diperuntukan untuk motor")
    elif DA >= 4001 and DA >= 5000 :
        print("Plat nomor tersebut diperuntukan untuk angkutan umum")
except :
    print("Plat Nomor Tidak Terindikasi, setelah kode daerah harus berupa nomor kendaraan")