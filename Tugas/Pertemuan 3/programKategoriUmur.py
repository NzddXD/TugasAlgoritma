# menjalankan kode loop untuk mengecek apakah user hanya memasukkan tipe
# bilangan bulat saja.

# Mengapa dibungkus di dalam loop? Karena python memperlakukan 'input()'
# sebagai string. Hasilnya bagian perbandingan nilai di dalam kode blok
# logic gate akan error duluan sebelum user dapat meng-input nilai.
while True:
    try:
        umur = int(input("Masukkan umur anda: "))

        # langsung keluar dari loop jika pengguna memasukkan tipe
        # nilai yang benar.
        break

    except ValueError:

        # Meng-handle tipe nilai error secara baik dengan menampilkan pesan
        # karena tipe nilai tidak valid, lalu menyuruh user untuk input ulang
        # dengan tipe nilai yang benar.
        print("Masukkan umur yang valid.")

# bagian Logic Gate untuk menentukan pesan apa yang akan di output berdasarkan
# besar kecilnya nilai yang diinput user.
if umur < 13:
    print("Anak - anak")
elif umur > 13 and umur < 17:
    print("Remaja")
elif umur > 17 and umur <= 59:
    print("Dewasa")
elif umur >= 60:
    print("Lansia")