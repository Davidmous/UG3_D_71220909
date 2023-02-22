hujan = float(input("Masukan angka curah hujan >>> "))

curah = ("Cuaca Terang/Berawan" if hujan == 0 else(("Curah hujan ringan" if hujan >= 0.5 and hujan <= 20 else(("Curah hujan sedang" if hujan >= 21 and hujan <= 50 else(("Curah hujan lebat" if hujan >= 51 and hujan <= 100 else(("Curah hujan ekstreme" if hujan > 100 else())))))))))
print(curah)