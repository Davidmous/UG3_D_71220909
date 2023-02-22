nama = input("Masukan Nama Lengkap Anda >>> ")
prodi = input("Masukan Prodi Anda >>>")
dalam_huruf = input("Masukan Nilai (dalam huruf) yang Anda Dapat >>>")

try :
    nilai = (dalam_huruf)
    if nilai == "A" :
        print("Nilai anda adalah 4.0, tbl tbl serem bgt lohh")
    elif nilai == "A-" :
        print("Nilai anda adalah 3.75, kamu keren")
    elif nilai == "B+" :
        print("Nilai anda adalah 3.25, Mantap")
    elif nilai == "B" :
        print("Nilai anda adalah 3.0, Tingkatkan lagi")
    elif nilai == "B-" :
        print("Nilai anda adalah 2.75, kurang semangat belajar nihh")
    elif nilai == "C+" :
        print("Nilai anda adalah 2.25, Jangan sering absen")
    elif nilai == "C" :
        print("Nilai anda adalah 2.0, Minimal Rajin ngerjain tugas lah")   
    elif nilai == "D" :
        print("Nilai anda adalah 1.0, apakah sudah ada pikiran untuk pindah jurusan?")
    elif nilai == "E" :
        print("Nilai anda adalah 0, niat kuliah nggak sih???")
except :
    print("Inputan nilai yang anda masukan tidak valid")