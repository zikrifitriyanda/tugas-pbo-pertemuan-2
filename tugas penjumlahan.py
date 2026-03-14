try:
    angka1 =int(input("masukan angka pertama: "))
    angka2 =int(input("masukan angka kedua: "))

    hasil = angka1 + angka2
    print("hasil penkumlahan: ", hasil)

except ValueError:
    print("input harus berupa angka, bukan teks!")
