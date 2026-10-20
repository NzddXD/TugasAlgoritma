# fungsi untuk menentukan jenis segitiga
def jenisSegitiga(a, b, c):
    # memvalidasi apakah sisi tesebut bisa membentuk segitiga?
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "bukan segitiga."

    # penentuan jenis berdasarkan panjang sisi
    if a == b == c:
        return "Segitiga sama sisi."
    elif a == b or a == c or b == c:
        return "Segitiga sama kaki."
    else:
        return "Segitiga sembarang"


# input nilai dari user.
# gunakan float agar user dapat memasukkan nilai desimal.
try:
    sisi_a = float(input("Masukkan nilai sisi pertama (A): "))
    sisi_b = float(input("Masukkan nilai sisi pertama (B): "))
    sisi_c = float(input("Masukkan nilai sisi pertama (C): "))

    hasil = jenisSegitiga(sisi_a, sisi_b, sisi_c)
    print("Hasil: ", hasil)

# handle error dengan menampilkan pesan error dan mengulangi
# pengisian nilai.
except ValueError:
    print("Masukkan nilai yang valid!")