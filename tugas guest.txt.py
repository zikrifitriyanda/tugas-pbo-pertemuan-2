nama = input("Masukkan nama Anda: ")

with open("guest.txt", "w") as file:
    file.write(nama)

print("Nama berhasil disimpan ke guest.txt")

with open("guest_book.txt", "w") as file:
    while True:
        nama = input("Masukkan nama Anda (ketik 'stop' untuk berhenti): ")

        if nama.lower() == "stop":
            break

        file.write(nama + "\n")

print("Semua nama berhasil disimpan ke guest_book.txt")

# membuka dan membaca isi file guest.txt

with open("guest.txt", "r") as file:
    isi = file.read()

print("Isi file:")
print(isi)

# membuka dan membaca isi file guest_book.txt

with open("guest_book.txt", "r") as file:
    isi = file.read()

print("Isi file:")
print(isi)